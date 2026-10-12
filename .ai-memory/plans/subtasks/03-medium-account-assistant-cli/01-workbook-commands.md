# Subtask 01 — Config module, SQLite store, workbook commands

Owner: Worker 01. Owned file: `03-ai-scripts/medium-account-assistant.py` (new).

Spec: 02-spec/21-app/03-medium-account-assistant-cli/01-overview.md +
02-config-and-pipeline.md (read both first — the config catalog and SQLite
schema are normative).

## Deliverable

Single-file Python CLI, argparse-based, run via `gitmap py`. Stdlib only
(`sqlite3`, `argparse`, `json`, `re`, `subprocess`, `pathlib`) plus guarded
`openpyxl` import (only needed for import-excel/export-excel).

### Config (seedable, coding-guidelines v3.2.0 pattern)

- On startup: load `03-ai-scripts/medium-account-assistant/config.seed.json`
  (path relative to the script file, not cwd).
- Ensure DB from `Paths.DatabasePath` (expand `~`); `config` table holds
  Key/Value/Version/UpdatedAt.
- If DB config Version < seed Version: merge new keys (never overwrite
  user-set values), append entry to `<db-dir>/changelog.md`.
- `config get <Key>` / `config set <Key> <Value>` commands.
- EVERY tunable in the spec's catalog comes from config — no hardcoded paths,
  regexes, or limits. `doctor` fails if a required key is missing.

### SQLite store

- Schema exactly as spec 02 section 2. `init` creates tables + seeds config
  (idempotent). `PRAGMA user_version` for schema version.

### Commands

1. `init` — create DB/tables, seed config.
2. `add --email E --first F --last L [--username U]` — email regex validation;
   reject duplicate email/username (case-insensitive); honor
   `Accounts.RequireRealName` (refuse empty names); UTC ISO timestamps.
3. `suggest-usernames --first F --last L` — build from `Usernames.*` config;
   mark taken ones (DB lookup).
4. `status [--email E]` — accounts table.
5. `import-excel --file PATH` — read first sheet, map columns
   email/first_name/last_name/username (case-insensitive headers), stage rows
   via the same validation as `add`; report added/skipped counts.
6. `export-excel [--file PATH]` — dump accounts table to xlsx in
   `Paths.ExportDir` (openpyxl required).
7. Stub (argparse + NotImplementedError): `otp`, `profile-prep`,
   `record-article`, `guide`, `doctor` — Worker 02 fills these.

## Hard prohibitions

- No network calls. No browser code. The string "medium.com" must not appear
  in code except inside the `guide` human-checklist text.
- No function that submits anything anywhere.
