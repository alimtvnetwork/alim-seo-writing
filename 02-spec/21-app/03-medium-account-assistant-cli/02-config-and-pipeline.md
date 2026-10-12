# Spec 03.2 — Config, SQLite, and gitmap macro

Follows coding-guidelines-v24 `02-spec/17-consolidated-guidelines/09-seedable-config.md`
(v3.2.0): PascalCase field names, `config.seed.json` as source of truth, SemVer
versioning, merge-without-clobber on upgrade, changelog on every version change.

## 1. Seed file: `03-ai-scripts/medium-account-assistant/config.seed.json`

```json
{
  "$schema": "./config.schema.json",
  "Version": "1.0.0",
  "Changelog": "Initial seed",
  "Categories": {
    "Paths": {
      "DisplayName": "Paths",
      "Description": "Filesystem locations. No personal data inside the repo.",
      "Settings": {
        "DatabasePath":   { "Type": "path", "Default": "~/.medium-account-assistant/accounts.db" },
        "ExportDir":      { "Type": "path", "Default": "~/.medium-account-assistant/exports" },
        "GoEmailReaderPath": { "Type": "path", "Default": "~/workspace/go-email-reader/go-email-reader" }
      }
    },
    "Mailbox": {
      "DisplayName": "Mailbox",
      "Description": "OTP retrieval via go-email-reader (display only, never submit).",
      "Settings": {
        "OtpRegex":       { "Type": "string", "Default": "\\b\\d{6}\\b" },
        "OtpMaxAgeMinutes": { "Type": "integer", "Default": 10 },
        "MailboxTimeoutSeconds": { "Type": "integer", "Default": 30 }
      }
    },
    "Usernames": {
      "DisplayName": "Usernames",
      "Description": "Candidate generation for suggest-usernames.",
      "Settings": {
        "MaxSuggestions": { "Type": "integer", "Default": 8 },
        "SuffixDigits":   { "Type": "integer", "Default": 3 },
        "AllowedChars":   { "Type": "string", "Default": "a-z0-9." }
      }
    },
    "Accounts": {
      "DisplayName": "Accounts",
      "Description": "Account record policy.",
      "Settings": {
        "Statuses": { "Type": "list", "Default": ["staged", "signed_up", "published"] },
        "RequireRealName": { "Type": "boolean", "Default": true }
      }
    }
  }
}
```

Rules:
- First run: seed SQLite `config` table from this file; record `Version`.
- On version bump: merge new settings, preserve user-overridden values, append
  to `~/.medium-account-assistant/changelog.md`.
- `config get <Key>` / `config set <Key> <Value>` operate on the DB, never the seed.
- CLI flags (e.g. `--db`) override config for one run only.

## 2. SQLite schema (gitmap-style, stdlib `sqlite3`)

```sql
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
```

- Email/Username uniqueness enforced by the DB (case-insensitive check in code).
- Migrations: `PRAGMA user_version` tracks schema version; `init` is idempotent.

## 3. gitmap macro: `maa-onboard`

Shipped as `03-ai-scripts/medium-account-assistant/macro-maa-onboard.json`,
importable via `gitmap macro import`. Combines the pipeline steps; future
pipeline enhancements ship as new macro versions.

```json
{
  "name": "maa-onboard",
  "description": "Medium account assistant: full human-in-the-loop pipeline",
  "tags": ["medium", "accounts", "human-in-the-loop"],
  "steps": [
    "gitmap py 03-ai-scripts/medium-account-assistant.py doctor",
    "gitmap py 03-ai-scripts/medium-account-assistant.py status",
    "gitmap py 03-ai-scripts/medium-account-assistant.py guide --step signup",
    "# HUMAN: create the account in the browser, then continue",
    "gitmap py 03-ai-scripts/medium-account-assistant.py otp --email {{email}}",
    "# HUMAN: paste the OTP into Medium yourself, then continue",
    "gitmap py 03-ai-scripts/medium-account-assistant.py guide --step publish",
    "# HUMAN: publish in the browser, then: record-article --email {{email}} --url <URL>"
  ]
}
```

- `{{email}}` is a macro parameter filled at run time.
- `# HUMAN:` steps are pause markers — the macro runner prints them and waits.
- `gitmap macro run maa-onboard --dry-run` previews without executing.

## 4. Every-variable-from-config catalog

| Variable | Category.Key | Used by |
|---|---|---|
| Database path | Paths.DatabasePath | all commands |
| Export dir | Paths.ExportDir | export-excel |
| go-email-reader binary | Paths.GoEmailReaderPath | otp, doctor |
| OTP regex | Mailbox.OtpRegex | otp |
| OTP max age | Mailbox.OtpMaxAgeMinutes | otp |
| Mailbox timeout | Mailbox.TimeoutSeconds | otp, doctor |
| Username suggestion count | Usernames.MaxSuggestions | suggest-usernames |
| Username suffix digits | Usernames.SuffixDigits | suggest-usernames |
| Username charset | Usernames.AllowedChars | suggest-usernames |
| Valid statuses | Accounts.Statuses | add, record-article, status |
| Real-name requirement | Accounts.RequireRealName | add |

No hardcoded paths, regexes, or limits in code — `doctor` fails if a required
key is missing.
