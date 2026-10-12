#!/usr/bin/env python3
"""medium-account-assistant.py -- human-in-the-loop account bookkeeping CLI.

Hard boundary (non-negotiable): this tool never automates the publishing
platform's signup, never submits one-time codes anywhere, and never creates
or publishes content programmatically. The human performs signup and
publishing in the browser; this tool only keeps the books (SQLite),
manages configuration (seedable config), and moves data in/out via Excel.

Run: gitmap py 03-ai-scripts/medium-account-assistant.py <command>
"""

import argparse
import json
import os
import platform
import re
import sqlite3
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import openpyxl
except ImportError:  # optional: only needed for import-excel/export-excel
    openpyxl = None

SCRIPT_DIR = Path(__file__).resolve().parent
SEED_PATH = SCRIPT_DIR / "medium-account-assistant" / "config.seed.json"
SCHEMA_VERSION = 1
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def utcnow():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _vkey(v):
    return tuple(int(p) for p in re.findall(r"\d+", v or "0"))


# ---------------------------------------------------------------------------
# Seedable config (coding-guidelines v3.2.0 pattern)
# ---------------------------------------------------------------------------

def load_seed():
    """Return (version, changelog, flat {Category.Key: {Type, Default}})."""
    try:
        seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        sys.stderr.write(f"ERROR: seed file missing: {SEED_PATH}\n")
        sys.exit(2)
    except json.JSONDecodeError as exc:
        sys.stderr.write(f"ERROR: seed file is not valid JSON: {exc}\n")
        sys.exit(2)
    flat = {}
    for cat, cdef in seed.get("Categories", {}).items():
        for key, sdef in cdef.get("Settings", {}).items():
            flat[f"{cat}.{key}"] = {
                "Type": sdef.get("Type", "string"),
                "Default": sdef.get("Default"),
            }
    return seed.get("Version", "0.0.0"), seed.get("Changelog", ""), flat


def _to_storage(value, ctype):
    if ctype == "list":
        return json.dumps(value if isinstance(value, list) else [value])
    if ctype == "boolean":
        return "true" if value else "false"
    return str(value)


def _from_storage(text, ctype):
    if ctype == "integer":
        return int(text)
    if ctype == "boolean":
        return str(text).strip().lower() in ("1", "true", "yes", "on")
    if ctype == "list":
        try:
            parsed = json.loads(text)
            return parsed if isinstance(parsed, list) else [parsed]
        except (json.JSONDecodeError, TypeError):
            return [p.strip() for p in str(text).split(",") if p.strip()]
    if ctype == "path":
        return os.path.expanduser(str(text))
    return str(text)


def _coerce_to_storage(raw, ctype):
    """Validate a `config set` value; return the DB storage string."""
    if ctype == "integer":
        try:
            return str(int(raw))
        except (TypeError, ValueError):
            raise ValueError(f"expected integer, got {raw!r}")
    if ctype == "boolean":
        low = str(raw).strip().lower()
        if low in ("1", "true", "yes", "on"):
            return "true"
        if low in ("0", "false", "no", "off"):
            return "false"
        raise ValueError(f"expected boolean, got {raw!r}")
    if ctype == "list":
        txt = str(raw).strip()
        if txt.startswith("["):
            try:
                parsed = json.loads(txt)
            except json.JSONDecodeError:
                raise ValueError(f"expected JSON list, got {raw!r}")
            if not isinstance(parsed, list):
                raise ValueError(f"expected JSON list, got {raw!r}")
            return json.dumps(parsed)
        return json.dumps([p.strip() for p in txt.split(",") if p.strip()])
    return str(raw)  # string / path


def resolve_db_path(cli_db, flat):
    """CLI --db wins; else a stored override; else the seed default."""
    if cli_db:
        return os.path.expanduser(cli_db)
    default = os.path.expanduser(str(flat["Paths.DatabasePath"]["Default"]))
    if os.path.exists(default):
        try:
            con = sqlite3.connect(default)
            row = con.execute(
                "SELECT Value FROM config WHERE Key='Paths.DatabasePath'"
            ).fetchone()
            con.close()
            if row and row[0]:
                return os.path.expanduser(row[0])
        except sqlite3.Error:
            pass
    return default


def connect(db_path):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    return con


SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS accounts (
  Email TEXT PRIMARY KEY,
  FirstName TEXT NOT NULL,
  LastName TEXT NOT NULL,
  Username TEXT UNIQUE,
  DisplayName TEXT,
  Bio TEXT,
  AvatarFile TEXT,
  Status TEXT NOT NULL DEFAULT 'staged',
  OtpLastShownAt TEXT,
  ArticleUrl TEXT,
  Notes TEXT,
  CreatedAt TEXT NOT NULL,
  UpdatedAt TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS config (
  Key TEXT PRIMARY KEY,
  Value TEXT NOT NULL,
  Version TEXT NOT NULL,
  UpdatedAt TEXT NOT NULL
);
"""


def ensure_schema(con):
    con.executescript(SCHEMA_SQL)
    uv = con.execute("PRAGMA user_version").fetchone()[0]
    if uv < SCHEMA_VERSION:
        con.execute(f"PRAGMA user_version={SCHEMA_VERSION}")
    con.commit()


def _append_changelog(db_path, seed_version, seed_changelog, added, kept):
    p = Path(db_path).parent / "changelog.md"
    with open(p, "a", encoding="utf-8") as fh:
        fh.write(f"\n## {utcnow()} -- config {seed_version}\n")
        fh.write(f"{seed_changelog}\n")
        fh.write(f"Merged {len(added)} new key(s), preserved {kept} "
                 f"existing value(s).\n")
        if added:
            fh.write("Added: " + ", ".join(sorted(added)) + "\n")


def seed_config(con, db_path, seed_version, seed_changelog, flat):
    """Merge seed into the config table; never overwrite user values."""
    existing = {r["Key"]: r["Version"]
                for r in con.execute("SELECT Key, Version FROM config")}
    added, kept, bumped = [], 0, False
    for key, meta in flat.items():
        if key not in existing:
            con.execute(
                "INSERT INTO config(Key, Value, Version, UpdatedAt)"
                " VALUES(?, ?, ?, ?)",
                (key, _to_storage(meta["Default"], meta["Type"]),
                 seed_version, utcnow()),
            )
            added.append(key)
        else:
            kept += 1
            if _vkey(existing[key]) < _vkey(seed_version):
                con.execute(
                    "UPDATE config SET Version=?, UpdatedAt=? WHERE Key=?",
                    (seed_version, utcnow(), key),
                )
                bumped = True
    con.commit()
    if added or bumped:
        _append_changelog(db_path, seed_version, seed_changelog, added, kept)


def cfg(ctx, key):
    """Typed config read; raises KeyError with a clear message if missing."""
    flat = ctx["flat"]
    if key not in flat:
        raise KeyError(f"config key missing from seed: {key}")
    row = ctx["con"].execute(
        "SELECT Value FROM config WHERE Key=?", (key,)).fetchone()
    if row is None:
        raise KeyError(f"config key not seeded (run `init`): {key}")
    return _from_storage(row["Value"], flat[key]["Type"])


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_init(args, ctx):
    n = ctx["con"].execute("SELECT COUNT(*) FROM accounts").fetchone()[0]
    print(f"initialized: {ctx['db_path']}")
    print(f"accounts: {n} | config version: {ctx['seed_version']}")


def add_account(ctx, email, first, last, username=None):
    """Shared validation for `add` and `import-excel`. Returns (ok, message)."""
    email = (email or "").strip()
    first = (first or "").strip()
    last = (last or "").strip()
    if not EMAIL_RE.match(email):
        return False, f"invalid email: {email!r}"
    if cfg(ctx, "Accounts.RequireRealName") and (not first or not last):
        return False, "first and last name are required (Accounts.RequireRealName)"
    con = ctx["con"]
    if con.execute("SELECT 1 FROM accounts WHERE lower(Email)=lower(?)",
                   (email,)).fetchone():
        return False, f"duplicate email: {email}"
    username = (username or "").strip() or None
    if username and con.execute(
            "SELECT 1 FROM accounts WHERE Username IS NOT NULL"
            " AND lower(Username)=lower(?)", (username,)).fetchone():
        return False, f"duplicate username: {username}"
    statuses = cfg(ctx, "Accounts.Statuses")
    status = statuses[0] if statuses else "staged"
    now = utcnow()
    display = f"{first} {last}".strip()
    con.execute(
        "INSERT INTO accounts(Email, FirstName, LastName, Username,"
        " DisplayName, Status, CreatedAt, UpdatedAt)"
        " VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
        (email, first, last, username, display, status, now, now),
    )
    con.commit()
    extra = f" as {username}" if username else ""
    return True, f"staged {email}{extra}"


def cmd_add(args, ctx):
    ok, msg = add_account(ctx, args.email, args.first, args.last, args.username)
    print(msg)
    if not ok:
        sys.exit(1)


def _expand_charset(spec):
    """Expand a compact charset like 'a-z0-9.' into a set of characters."""
    out = []
    i = 0
    while i < len(spec):
        if i + 2 < len(spec) and spec[i + 1] == "-":
            for code in range(ord(spec[i]), ord(spec[i + 2]) + 1):
                out.append(chr(code))
            i += 3
        else:
            out.append(spec[i])
            i += 1
    return set(out)


def cmd_suggest_usernames(args, ctx):
    maxn = cfg(ctx, "Usernames.MaxSuggestions")
    digits = cfg(ctx, "Usernames.SuffixDigits")
    allowed = _expand_charset(str(cfg(ctx, "Usernames.AllowedChars")))
    first = "".join(c for c in args.first.lower() if c in allowed)
    last = "".join(c for c in args.last.lower() if c in allowed)
    bases = []
    for base in (first + last,
                 f"{first}.{last}" if first and last else "",
                 first[:1] + last,
                 first + last[:1]):
        if base and base not in bases:
            bases.append(base)
    if not bases:
        sys.stderr.write("ERROR: no usable characters in first/last name\n")
        sys.exit(2)
    seen, out = set(), []

    def emit(candidate):
        if candidate and candidate not in seen and len(out) < maxn:
            seen.add(candidate)
            out.append(candidate)

    for base in bases:
        emit(base)
    n = 1
    while len(out) < maxn and n < 10 ** max(digits, 1):
        for base in bases:
            emit(f"{base}{n}")
            if len(out) >= maxn:
                break
        n += 1
    con = ctx["con"]
    for candidate in out:
        taken = con.execute(
            "SELECT 1 FROM accounts WHERE Username IS NOT NULL"
            " AND lower(Username)=lower(?)", (candidate,)).fetchone()
        print(f"{candidate}  [{'taken' if taken else 'free'}]")


def cmd_status(args, ctx):
    con = ctx["con"]
    if args.email:
        rows = con.execute("SELECT * FROM accounts WHERE lower(Email)=lower(?)",
                           (args.email.strip(),)).fetchall()
    else:
        rows = con.execute("SELECT * FROM accounts ORDER BY CreatedAt").fetchall()
    if not rows:
        print("no accounts")
        return
    cols = ["Email", "Username", "DisplayName", "Status", "ArticleUrl", "UpdatedAt"]
    widths = {c: max(len(c), max(len(str(r[c] or "")) for r in rows))
              for c in cols}
    print("  ".join(c.ljust(widths[c]) for c in cols))
    for r in rows:
        print("  ".join(str(r[c] or "").ljust(widths[c]) for c in cols))


def _require_openpyxl():
    if openpyxl is None:
        sys.stderr.write(
            "ERROR: openpyxl is required for Excel import/export.\n"
            "Install it, then re-run via: gitmap py\n")
        sys.exit(2)


def cmd_import_excel(args, ctx):
    _require_openpyxl()
    path = Path(args.file).expanduser()
    if not path.exists():
        sys.stderr.write(f"ERROR: file not found: {path}\n")
        sys.exit(2)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        print("empty sheet")
        return
    header = [str(h or "").strip().lower().replace(" ", "_") for h in rows[0]]

    def col(*names):
        for name in names:
            if name in header:
                return header.index(name)
        return None

    ci = {"email": col("email"),
          "first": col("first_name", "firstname", "first"),
          "last": col("last_name", "lastname", "last"),
          "username": col("username")}
    if ci["email"] is None:
        sys.stderr.write("ERROR: no 'email' column found in header row\n")
        sys.exit(2)
    added, skipped = 0, []
    for lineno, row in enumerate(rows[1:], start=2):
        email = str(row[ci["email"]] or "").strip()
        first = str(row[ci["first"]] or "").strip() if ci["first"] is not None else ""
        last = str(row[ci["last"]] or "").strip() if ci["last"] is not None else ""
        username = (str(row[ci["username"]] or "").strip()
                    if ci["username"] is not None else "") or None
        if not email:
            skipped.append((lineno, "empty email"))
            continue
        ok, msg = add_account(ctx, email, first, last, username)
        if ok:
            added += 1
        else:
            skipped.append((lineno, msg))
    print(f"imported: {added} added, {len(skipped)} skipped")
    for lineno, msg in skipped:
        print(f"  row {lineno}: {msg}")


def cmd_export_excel(args, ctx):
    _require_openpyxl()
    if args.file:
        out = Path(args.file).expanduser()
        out.parent.mkdir(parents=True, exist_ok=True)
    else:
        export_dir = Path(cfg(ctx, "Paths.ExportDir"))
        export_dir.mkdir(parents=True, exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        out = export_dir / f"accounts-{stamp}.xlsx"
    cols = ["Email", "FirstName", "LastName", "Username", "DisplayName", "Bio",
            "AvatarFile", "Status", "OtpLastShownAt", "ArticleUrl", "Notes",
            "CreatedAt", "UpdatedAt"]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Accounts"
    ws.append(cols)
    n = 0
    for r in ctx["con"].execute("SELECT * FROM accounts ORDER BY CreatedAt"):
        ws.append([r[c] for c in cols])
        n += 1
    wb.save(out)
    print(f"exported {n} account(s) -> {out}")


def cmd_config_get(args, ctx):
    flat = ctx["flat"]
    if args.key not in flat:
        sys.stderr.write(f"ERROR: unknown config key {args.key!r}. Valid keys:\n")
        for key in sorted(flat):
            sys.stderr.write(f"  {key}\n")
        sys.exit(2)
    row = ctx["con"].execute(
        "SELECT Value FROM config WHERE Key=?", (args.key,)).fetchone()
    if row is None:
        sys.stderr.write(f"ERROR: key not seeded (run `init`): {args.key}\n")
        sys.exit(2)
    print(row["Value"])


def cmd_config_set(args, ctx):
    flat = ctx["flat"]
    if args.key not in flat:
        sys.stderr.write(f"ERROR: unknown config key {args.key!r}. Valid keys:\n")
        for key in sorted(flat):
            sys.stderr.write(f"  {key}\n")
        sys.exit(2)
    try:
        storage = _coerce_to_storage(args.value, flat[args.key]["Type"])
    except ValueError as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        sys.exit(2)
    ctx["con"].execute(
        "UPDATE config SET Value=?, UpdatedAt=? WHERE Key=?",
        (storage, utcnow(), args.key))
    ctx["con"].commit()
    print(f"{args.key} = {args.value}")


# ---- Worker 02 commands -------------------------------------------------

def _get_account(ctx, email):
    """Fetch the account row (case-insensitive); exit 1 if unknown."""
    email = (email or "").strip()
    row = ctx["con"].execute(
        "SELECT * FROM accounts WHERE lower(Email)=lower(?)",
        (email,)).fetchone()
    if row is None:
        sys.stderr.write(
            f"ERROR: no account for {email!r} — run `add` first\n")
        sys.exit(1)
    return row


def _parse_messages(raw):
    """Parse go-email-reader --json output into a list of message dicts."""
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []
    if isinstance(data, dict):
        return [data]
    if isinstance(data, list):
        return [m for m in data if isinstance(m, dict)]
    return []


def _message_age_minutes(date_raw):
    """Best-effort age of a message date string; None if unparseable."""
    if not date_raw:
        return None
    text = str(date_raw).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    delta = datetime.now(timezone.utc) - dt
    return delta.total_seconds() / 60


def cmd_otp(args, ctx):
    email = args.email.strip()
    _get_account(ctx, email)
    bin_path = os.path.expanduser(str(cfg(ctx, "Paths.GoEmailReaderPath")))
    if not Path(bin_path).is_file():
        sys.stderr.write(
            f"ERROR: go-email-reader binary not found at {bin_path}\n"
            "  (config key Paths.GoEmailReaderPath)\n")
        sys.exit(3)
    otp_re = str(cfg(ctx, "Mailbox.OtpRegex"))
    max_age = cfg(ctx, "Mailbox.OtpMaxAgeMinutes")
    timeout = cfg(ctx, "Mailbox.MailboxTimeoutSeconds")
    try:
        pattern = re.compile(otp_re)
    except re.error as exc:
        sys.stderr.write(f"ERROR: bad Mailbox.OtpRegex {otp_re!r}: {exc}\n")
        sys.exit(2)
    cmd = [bin_path, "read", "--email", email, "--limit", "1", "--json"]
    try:
        proc = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout)
    except FileNotFoundError:
        sys.stderr.write(f"ERROR: cannot execute {bin_path}\n")
        sys.exit(3)
    except subprocess.TimeoutExpired:
        sys.stderr.write(
            f"ERROR: go-email-reader timed out after {timeout}s\n")
        sys.exit(3)
    except OSError as exc:
        sys.stderr.write(f"ERROR: failed to run go-email-reader: {exc}\n")
        sys.exit(3)
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or "").strip()
        sys.stderr.write(
            f"ERROR: go-email-reader failed (exit {proc.returncode})")
        if detail:
            sys.stderr.write(f":\n{detail}")
        sys.stderr.write("\n")
        sys.exit(3)
    messages = _parse_messages(proc.stdout)
    if not messages:
        sys.stderr.write(f"ERROR: no messages found for {email}\n")
        sys.exit(3)
    msg = messages[0]
    text = " ".join(
        str(msg.get(k, "")) for k in
        ("Subject", "Snippet", "BodyText", "subject", "snippet",
         "bodyText", "body", "Body"))
    match = pattern.search(text)
    if not match:
        subject = msg.get("Subject", msg.get("subject", ""))
        sys.stderr.write(
            f"ERROR: no code matching {otp_re!r} in the latest message "
            f"(subject: {subject!r})\n")
        sys.exit(3)
    code = match.group(0)
    age = _message_age_minutes(msg.get("Date", msg.get("date")))
    if age is not None and age > max_age:
        print(f"WARNING: latest message is {age:.0f} minutes old "
              f"(limit: {max_age}) — the code may be expired.")
    print(f"one-time code for {email}: {code}")
    print("paste this into Medium yourself — "
          "this tool never submits codes anywhere.")
    now = utcnow()
    ctx["con"].execute(
        "UPDATE accounts SET OtpLastShownAt=?, UpdatedAt=?"
        " WHERE lower(Email)=lower(?)",
        (now, now, email))
    ctx["con"].commit()


BIO_TEMPLATES = [
    "{name} writes about software, AI, and how things get built.",
    "Notes on engineering and technology by {name}.",
    "{name} — writing about the craft of building software.",
]


def cmd_profile_prep(args, ctx):
    row = _get_account(ctx, args.email)
    name = row["DisplayName"] or \
        f"{row['FirstName']} {row['LastName']}".strip()
    options = [t.format(name=name) for t in BIO_TEMPLATES]
    username = row["Username"] or args.email.strip().split("@")[0]
    avatar_default = f"{username}-white.jpg"
    if args.bio is None and args.avatar is None:
        print(f"profile prep for {row['Email']}:")
        for i, bio in enumerate(options, 1):
            print(f"  [{i}] {bio}")
        print(f"  avatar filename convention: {avatar_default}")
        print("  store a choice with:")
        print("    profile-prep --email <email> --bio <1-3> [--avatar FILE]")
        return
    updates = {}
    if args.bio is not None:
        if args.bio not in (1, 2, 3):
            sys.stderr.write("ERROR: --bio must be 1, 2, or 3\n")
            sys.exit(2)
        updates["Bio"] = options[args.bio - 1]
    if args.avatar is not None:
        updates["AvatarFile"] = args.avatar
    elif args.bio is not None:
        updates["AvatarFile"] = avatar_default
    if updates:
        updates["UpdatedAt"] = utcnow()
        sets = ", ".join(f"{k}=?" for k in updates)
        ctx["con"].execute(
            f"UPDATE accounts SET {sets} WHERE lower(Email)=lower(?)",
            (*updates.values(), args.email.strip()))
        ctx["con"].commit()
        stored = ", ".join(f"{k}={v}" for k, v in updates.items()
                           if k != "UpdatedAt")
        print(f"stored for {row['Email']}: {stored}")


MEDIUM_POST_PREFIX = "https://medium.com/"


def cmd_record_article(args, ctx):
    row = _get_account(ctx, args.email)
    url = (args.url or "").strip()
    if not url.startswith(MEDIUM_POST_PREFIX):
        sys.stderr.write(
            f"ERROR: URL must start with {MEDIUM_POST_PREFIX} — got {url!r}\n")
        sys.exit(2)
    statuses = cfg(ctx, "Accounts.Statuses")
    status = "published" if "published" in statuses else statuses[-1]
    ctx["con"].execute(
        "UPDATE accounts SET ArticleUrl=?, Status=?, UpdatedAt=?"
        " WHERE lower(Email)=lower(?)",
        (url, status, utcnow(), args.email.strip()))
    ctx["con"].commit()
    print(f"recorded for {row['Email']}: status={status} url={url}")


GUIDE_SIGNUP = """\
HUMAN CHECKLIST — account signup (do this in your browser)
  1. Open medium.com and choose "Sign up".
  2. Enter the email address shown by: status --email <email>
  3. Fill in first name, last name, and your chosen username.
  4. When Medium asks for the verification code, run:
       gitmap py 03-ai-scripts/medium-account-assistant.py otp --email <email>
  5. Paste the displayed code into Medium YOURSELF.
  6. Complete the profile (bio from profile-prep, avatar file).
"""

GUIDE_PUBLISH = """\
HUMAN CHECKLIST — publishing (do this in your browser)
  1. Open medium.com and choose Write.
  2. Paste your article, review it fully, make any edits.
  3. Press Publish YOURSELF.
  4. Copy the published article URL.
  5. Record it:
       gitmap py 03-ai-scripts/medium-account-assistant.py \\
         record-article --email <email> --url <URL>
"""


def cmd_guide(args, ctx):
    print(GUIDE_SIGNUP if args.step == "signup" else GUIDE_PUBLISH, end="")


def _check_db_writable(con):
    """Probe write access with a rolled-back transaction; return (ok, detail)."""
    try:
        con.execute("BEGIN IMMEDIATE")
        con.execute("CREATE TABLE IF NOT EXISTS _doctor_probe (x INTEGER)")
        con.execute("DROP TABLE IF EXISTS _doctor_probe")
        con.rollback()
        return True, "write probe ok (rolled back)"
    except sqlite3.Error as exc:
        try:
            con.rollback()
        except sqlite3.Error:
            pass
        return False, str(exc)


def cmd_doctor(args, ctx):
    results = []  # (name, level, detail); level in OK/FAIL/WARN

    ver = sys.version_info
    ok = ver >= (3, 10)
    results.append(("python >= 3.10",
                    "OK" if ok else "FAIL",
                    platform.python_version()))

    try:
        probe = sqlite3.connect(":memory:")
        probe.execute("SELECT 1")
        probe.close()
        results.append(("sqlite3", "OK", "in-memory query ok"))
    except Exception as exc:  # noqa: BLE001 - report any failure
        results.append(("sqlite3", "FAIL", str(exc)))

    flat = ctx["flat"]
    missing = [k for k in flat
               if ctx["con"].execute(
                   "SELECT 1 FROM config WHERE Key=?", (k,)).fetchone()
               is None]
    results.append(("config keys present",
                    "OK" if not missing else "FAIL",
                    f"{len(flat) - len(missing)}/{len(flat)} present"
                    + (f"; missing: {', '.join(missing)}" if missing else "")))

    bin_path = os.path.expanduser(str(flat["Paths.GoEmailReaderPath"]["Default"]))
    try:
        bin_path = os.path.expanduser(str(cfg(ctx, "Paths.GoEmailReaderPath")))
    except KeyError:
        pass
    if Path(bin_path).is_file():
        timeout = 15
        try:
            timeout = int(cfg(ctx, "Mailbox.MailboxTimeoutSeconds"))
        except (KeyError, ValueError):
            pass
        try:
            proc = subprocess.run([bin_path, "--version"],
                                  capture_output=True, text=True,
                                  timeout=timeout)
            out = (proc.stdout or proc.stderr or "").strip().splitlines()
            detail = f"found at {bin_path}; " + \
                (out[0][:80] if out else "--version gave no output")
            results.append(("go-email-reader binary", "OK", detail))
        except Exception as exc:  # noqa: BLE001 - version probe is best-effort
            results.append(("go-email-reader binary", "OK",
                            f"found at {bin_path}; version check failed: {exc}"))
    else:
        results.append(("go-email-reader binary", "FAIL",
                        f"not found at {bin_path} "
                        "(config Paths.GoEmailReaderPath)"))

    ok, detail = _check_db_writable(ctx["con"])
    results.append(("database writable", "OK" if ok else "FAIL", detail))

    results.append(("openpyxl (Excel import/export)",
                    "OK" if openpyxl is not None else "WARN",
                    "installed" if openpyxl is not None
                    else "missing — Excel commands will refuse to run"))

    failed = [n for n, lvl, _ in results if lvl == "FAIL"]
    for name, level, detail in results:
        print(f"[{level}] {name}: {detail}")
    if failed:
        print(f"doctor: {len(failed)} check(s) FAILED")
        sys.exit(1)
    print("doctor: all required checks passed")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser():
    p = argparse.ArgumentParser(
        prog="medium-account-assistant.py",
        description="Human-in-the-loop account bookkeeping CLI. The human "
                    "performs signup and publishing in the browser; this tool "
                    "keeps the books, manages config, and moves data via Excel.")
    p.add_argument("--db", default=None,
                   help="SQLite database path for this run only "
                        "(overrides config)")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("init", help="create database, tables, seed config")
    sp.set_defaults(fn=cmd_init)

    sp = sub.add_parser("add", help="stage a person")
    sp.add_argument("--email", required=True)
    sp.add_argument("--first", default="")
    sp.add_argument("--last", default="")
    sp.add_argument("--username", default=None)
    sp.set_defaults(fn=cmd_add)

    sp = sub.add_parser("suggest-usernames",
                        help="username candidates, collision-checked")
    sp.add_argument("--first", required=True)
    sp.add_argument("--last", required=True)
    sp.set_defaults(fn=cmd_suggest_usernames)

    sp = sub.add_parser("status", help="show accounts and pipeline state")
    sp.add_argument("--email", default=None)
    sp.set_defaults(fn=cmd_status)

    sp = sub.add_parser("import-excel", help="stage rows from an Excel sheet")
    sp.add_argument("--file", required=True)
    sp.set_defaults(fn=cmd_import_excel)

    sp = sub.add_parser("export-excel", help="dump accounts to Excel")
    sp.add_argument("--file", default=None)
    sp.set_defaults(fn=cmd_export_excel)

    sp = sub.add_parser("config", help="inspect/override configuration")
    cfg_sub = sp.add_subparsers(dest="config_cmd", required=True)
    g = cfg_sub.add_parser("get", help="print a config value")
    g.add_argument("key")
    g.set_defaults(fn=cmd_config_get)
    s = cfg_sub.add_parser("set", help="override a config value")
    s.add_argument("key")
    s.add_argument("value")
    s.set_defaults(fn=cmd_config_set)

    sp = sub.add_parser("otp", help="display the one-time code (never submits)")
    sp.add_argument("--email", required=True)
    sp.set_defaults(fn=cmd_otp)

    sp = sub.add_parser("profile-prep", help="bio drafts and avatar prep")
    sp.add_argument("--email", required=True)
    sp.add_argument("--bio", type=int, choices=[1, 2, 3], default=None,
                    help="store bio draft 1-3")
    sp.add_argument("--avatar", default=None,
                    help="store avatar filename")
    sp.set_defaults(fn=cmd_profile_prep)

    sp = sub.add_parser("record-article",
                        help="record a published article URL")
    sp.add_argument("--email", required=True)
    sp.add_argument("--url", required=True)
    sp.set_defaults(fn=cmd_record_article)

    sp = sub.add_parser("guide",
                        help="human checklists for the manual browser steps")
    sp.add_argument("--step", required=True, choices=["signup", "publish"])
    sp.set_defaults(fn=cmd_guide)

    sp = sub.add_parser("doctor", help="prerequisite checks")
    sp.set_defaults(fn=cmd_doctor)

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    seed_version, seed_changelog, flat = load_seed()
    db_path = resolve_db_path(args.db, flat)
    con = connect(db_path)
    try:
        ensure_schema(con)
        seed_config(con, db_path, seed_version, seed_changelog, flat)
        ctx = {"con": con, "flat": flat, "db_path": db_path,
               "seed_version": seed_version}
        args.fn(args, ctx)
    except NotImplementedError as exc:
        sys.stderr.write(f"NOT IMPLEMENTED: {exc}\n")
        sys.exit(4)
    except KeyError as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        sys.exit(2)
    finally:
        con.close()


if __name__ == "__main__":
    main()
