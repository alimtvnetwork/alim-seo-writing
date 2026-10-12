# Subtask 01 — CLI skeleton + workbook commands

Owner: Worker 01. Owned file: `03-ai-scripts/medium-account-assistant.py` (new).

## Deliverable

Single-file Python CLI, argparse-based, run via `gitmap py`. Workbook default:
`~/workspace/your_files/medium-accounts.xlsx`, overridable with `--workbook`
(global flag). Never commit a real workbook; tests use `/tmp` workbooks.

## Commands to implement

1. `init` — create workbook with sheet "Accounts" and header:
   email | first_name | last_name | username | display_name | bio |
   avatar_file | status | otp_last_shown_at | article_url | notes |
   created_at | updated_at. `status` starts as `staged`.
2. `add --email E --first F --last L [--username U]` — validate email with a
   simple regex; reject duplicate email or username (case-insensitive);
   stamp created_at/updated_at (UTC ISO).
3. `suggest-usernames --first F --last L` — candidates: `firstlast`,
   `first.last`, `firstlast` + 2-3 digit suffix variants, `f-lastname`;
   lowercase, strip non-alphanumerics except `.`; mark which are already taken
   in the workbook.
4. `status [--email E]` — table of accounts with their pipeline state.
5. Stub out (argparse entries + `NotImplementedError` with the spec's
   description): `otp`, `profile-prep`, `record-article`, `guide`, `doctor`.
   Worker 02 fills these in — do NOT implement them here.

## Constraints

- `openpyxl` import guarded: if missing, print install hint and exit 2.
- No network calls, no browser code, no Medium URLs touched anywhere.
- `--help` for every command.
