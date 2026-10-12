#!/usr/bin/env python3
"""Medium Account Assistant CLI (human-in-the-loop).

Bookkeeping helper for creating Medium accounts for real people. The human
performs the signup and publishing clicks in the browser themselves; this tool
only manages the accounts workbook, suggests usernames, and (in later
subtasks) fetches OTP codes for DISPLAY and prepares profiles.

HARD BOUNDARY: this tool never drives a browser against Medium, never submits
an OTP anywhere, and never creates drafts or publishes content programmatically.

Run: gitmap py 03-ai-scripts/medium-account-assistant.py <command> --help
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import openpyxl
except ImportError:  # guarded per subtask: clear hint, exit 2
    print(
        "error: the 'openpyxl' package is required.\n"
        "Install it with: gitmap py -m pip install openpyxl",
        file=sys.stderr,
    )
    sys.exit(2)

SHEET = "Accounts"
HEADERS = [
    "email", "first_name", "last_name", "username", "display_name",
    "bio", "avatar_file", "status", "otp_last_shown_at", "article_url",
    "notes", "created_at", "updated_at",
]
DEFAULT_WORKBOOK = str(Path("~/workspace/your_files/medium-accounts.xlsx").expanduser())
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
STATUSES = ("staged", "signed_up", "published")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def norm_username(raw: str) -> str:
    """Lowercase; keep alphanumerics and dots only."""
    s = re.sub(r"[^a-z0-9.]", "", raw.lower())
    s = re.sub(r"\.+", ".", s).strip(".")
    return s


def load_wb(workbook: str):
    p = Path(workbook).expanduser()
    if not p.exists():
        print(f"error: workbook not found: {p}\nRun `init` first.", file=sys.stderr)
        sys.exit(1)
    wb = openpyxl.load_workbook(p)
    if SHEET not in wb.sheetnames:
        print(f"error: sheet {SHEET!r} missing in {p}", file=sys.stderr)
        sys.exit(1)
    return wb, p


def read_accounts(wb) -> list[dict]:
    ws = wb[SHEET]
    data = list(ws.iter_rows(values_only=True))
    if not data:
        return []
    headers = [str(h) if h is not None else "" for h in data[0]]
    accounts = []
    for r in data[1:]:
        if not any(r):
            continue
        accounts.append(dict(zip(headers, r)))
    return accounts


def taken_usernames(wb) -> set[str]:
    return {(a.get("username") or "").strip().lower()
            for a in read_accounts(wb) if a.get("username")}


def username_candidates(first: str, last: str) -> list[str]:
    f, l = norm_username(first), norm_username(last)
    raw = [f + l, f + "." + l, f + l + "42", f + l + "123", f[0:1] + "-" + l]
    seen, out = set(), []
    for c in raw:
        c = norm_username(c)
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def cmd_init(args) -> None:
    p = Path(args.workbook).expanduser()
    if p.exists():
        print(f"error: {p} already exists — refusing to overwrite.", file=sys.stderr)
        sys.exit(1)
    p.parent.mkdir(parents=True, exist_ok=True)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = SHEET
    ws.append(HEADERS)
    wb.save(p)
    print(f"created workbook: {p}")


def cmd_add(args) -> None:
    email = args.email.strip()
    if not EMAIL_RE.match(email):
        print(f"error: invalid email address: {email!r}", file=sys.stderr)
        sys.exit(1)
    wb, p = load_wb(args.workbook)
    accounts = read_accounts(wb)
    if any((a.get("email") or "").strip().lower() == email.lower() for a in accounts):
        print(f"error: duplicate email: {email!r}", file=sys.stderr)
        sys.exit(1)
    if args.username:
        username = norm_username(args.username)
        if not username:
            print(f"error: username {args.username!r} normalizes to empty.", file=sys.stderr)
            sys.exit(1)
        if username in taken_usernames(wb):
            print(f"error: username already taken: {username!r}", file=sys.stderr)
            sys.exit(1)
    else:
        taken = taken_usernames(wb)
        username = next((c for c in username_candidates(args.first, args.last)
                         if c not in taken), None)
        if username is None:
            print("error: no free username candidate; pass --username explicitly.",
                  file=sys.stderr)
            sys.exit(1)
        print(f"username not given — assigned: {username}")
    ts = now_iso()
    wb[SHEET].append([
        email, args.first.strip(), args.last.strip(), username,
        f"{args.first.strip()} {args.last.strip()}",
        "", "", "staged", "", "", "", ts, ts,
    ])
    wb.save(p)
    print(f"added {email} as {username} (staged)")


def cmd_suggest_usernames(args) -> None:
    wb, _ = load_wb(args.workbook)
    taken = taken_usernames(wb)
    print(f"{'candidate':<24}{'status'}")
    for c in username_candidates(args.first, args.last):
        print(f"{c:<24}{'TAKEN' if c in taken else 'available'}")


def cmd_status(args) -> None:
    wb, _ = load_wb(args.workbook)
    accounts = read_accounts(wb)
    if args.email:
        accounts = [a for a in accounts
                    if (a.get("email") or "").strip().lower() == args.email.strip().lower()]
        if not accounts:
            print(f"error: no account for {args.email!r}", file=sys.stderr)
            sys.exit(1)
    if not accounts:
        print("no accounts yet — run `add` first.")
        return
    print(f"{'email':<32}{'name':<22}{'username':<20}{'status':<10}article_url")
    for a in accounts:
        name = f"{a.get('first_name') or ''} {a.get('last_name') or ''}".strip()
        print(f"{str(a.get('email') or ''):<32}{name:<22}"
              f"{str(a.get('username') or ''):<20}{str(a.get('status') or ''):<10}"
              f"{a.get('article_url') or '-'}")


# --- Stubs for Worker 02 (do NOT implement here) ---

def cmd_otp(args) -> None:
    raise NotImplementedError(
        "otp: fetch the latest OTP email via go-email-reader and DISPLAY the code "
        "(never submit)")


def cmd_profile_prep(args) -> None:
    raise NotImplementedError(
        "profile-prep: draft bio suggestions + avatar guidance; store choices in workbook")


def cmd_record_article(args) -> None:
    raise NotImplementedError(
        "record-article: after the human publishes, record the URL; mark account `published`")


def cmd_guide(args) -> None:
    raise NotImplementedError(
        "guide: print the human checklist for the manual browser steps")


def cmd_doctor(args) -> None:
    raise NotImplementedError(
        "doctor: check prerequisites: go-email-reader binary, openpyxl, mailbox access")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="medium-account-assistant",
        description="Human-in-the-loop bookkeeping for Medium accounts. "
                    "The human does signup/publishing in the browser; this tool "
                    "tracks everything around those steps. It never automates Medium.",
    )
    parser.add_argument(
        "--workbook", default=DEFAULT_WORKBOOK,
        help=f"accounts workbook path (default: {DEFAULT_WORKBOOK})")
    # Subparsers get --workbook with a SUPPRESS default so a value given
    # before the subcommand is never clobbered. (Do NOT use set_defaults
    # for workbook: it would rewrite the shared action's default.)
    wb_parent = argparse.ArgumentParser(add_help=False)
    wb_parent.add_argument(
        "--workbook", default=argparse.SUPPRESS,
        help=f"accounts workbook path (default: {DEFAULT_WORKBOOK})")
    parent = wb_parent
    sub = parser.add_subparsers(dest="command", required=True, metavar="<command>")

    p = sub.add_parser("init", parents=[parent],
                       help="Create the accounts workbook with the standard schema.")
    p.set_defaults(func=cmd_init)

    p = sub.add_parser("add", parents=[parent],
                       help="Stage a person: validate email, reject duplicates.")
    p.add_argument("--email", required=True, help="Person's email address.")
    p.add_argument("--first", required=True, help="First name.")
    p.add_argument("--last", required=True, help="Last name.")
    p.add_argument("--username", help="Desired username (auto-assigned if omitted).")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("suggest-usernames", parents=[parent],
                       help="Username candidates, collision-checked against the workbook.")
    p.add_argument("--first", required=True, help="First name.")
    p.add_argument("--last", required=True, help="Last name.")
    p.set_defaults(func=cmd_suggest_usernames)

    p = sub.add_parser("status", parents=[parent],
                       help="Show pipeline state per account.")
    p.add_argument("--email", help="Show only this account.")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("otp", parents=[parent],
                       help="Fetch the latest OTP email via go-email-reader and DISPLAY "
                            "the code (never submit). [Worker 02]")
    p.add_argument("--email", required=True, help="Account email address.")
    p.set_defaults(func=cmd_otp)

    p = sub.add_parser("profile-prep", parents=[parent],
                       help="Draft bio suggestions + avatar guidance; store choices in "
                            "workbook. [Worker 02]")
    p.add_argument("--email", required=True, help="Account email address.")
    p.set_defaults(func=cmd_profile_prep)

    p = sub.add_parser("record-article", parents=[parent],
                       help="After the human publishes, record the URL; mark account "
                            "`published`. [Worker 02]")
    p.add_argument("--email", required=True, help="Account email address.")
    p.add_argument("--url", required=True, help="Published article URL.")
    p.set_defaults(func=cmd_record_article)

    p = sub.add_parser("guide", parents=[parent],
                       help="Print the human checklist for the manual browser steps. "
                            "[Worker 02]")
    p.add_argument("--step", required=True, choices=["signup", "publish"],
                   help="Which manual step to print the checklist for.")
    p.set_defaults(func=cmd_guide)

    p = sub.add_parser("doctor", parents=[parent],
                       help="Check prerequisites: go-email-reader binary, openpyxl, "
                            "mailbox access. [Worker 02]")
    p.set_defaults(func=cmd_doctor)

    return parser


def main(argv=None) -> None:
    args = build_parser().parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
