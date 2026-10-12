# Spec 03 — Medium Account Assistant CLI (human-in-the-loop)

## Goal

A Python CLI that removes the bookkeeping overhead of creating Medium accounts
for real people (employees), while the human performs the signup and publishing
clicks in the browser themselves.

## Hard scope boundary (non-negotiable)

This tool NEVER:
- drives, fills, clicks, or submits anything on medium.com (no browser automation
  of any kind against Medium),
- submits an OTP anywhere (it only fetches and DISPLAYS the code for the human
  to paste),
- creates drafts, posts, or publishes content programmatically.

The human performs signup and publishing in the browser. The tool assists around
those two moments. This boundary is what keeps the tool inside Medium's rules,
which prohibit registering accounts and posting content "automatically,
systematically, or programmatically."

## CLI surface

`gitmap py 03-ai-scripts/medium-account-assistant.py <command>`

| Command | What it does |
|---|---|
| `init [--workbook PATH]` | Create the accounts workbook with the schema below |
| `add --email E --first F --last L [--username U]` | Stage a person; validates email format; rejects duplicate email/username |
| `suggest-usernames --first F --last L` | Generate username candidates, collision-checked against the workbook |
| `otp --email E` | Fetch the latest OTP email via go-email-reader and DISPLAY the code (never submit) |
| `profile-prep --email E` | Draft bio suggestions + avatar guidance; store choices in workbook |
| `record-article --email E --url URL` | After the human publishes, record the URL; mark account `published` |
| `status [--email E]` | Show pipeline state per account |
| `guide --step signup\|publish` | Print the human checklist for the manual browser steps |
| `doctor` | Check prerequisites: go-email-reader binary, openpyxl, mailbox access |

## Workbook schema (Sheet "Accounts")

email (unique) | first_name | last_name | username (unique) | display_name |
bio | avatar_file | status (staged → signed_up → published) |
otp_last_shown_at | article_url | notes | created_at | updated_at

Default workbook: `~/workspace/your_files/medium-accounts.xlsx` (NOT committed to
git — it holds personal data). Override with `--workbook`.

## GoEmailReader integration

- Locate the binary: `~/workspace/go-email-reader/go-email-reader`, else PATH.
- `otp` shells out to its `read` command for the latest email to the target
  address, extracts a 6-digit code via regex, prints it with expiry warning.
- `doctor` verifies the binary exists and the mailbox is reachable.
- No self-update: go-email-reader has no updater; noted as future work, not claimed.

## Dependencies

- Python 3.10+, `openpyxl` (via `gitmap py`; falls back to a clear error if missing).
- `go-email-reader` built binary (Go toolchain at `~/go/bin/go`).

## Acceptance

- All 8 commands work end-to-end against a test workbook (no real accounts touched).
- `otp` displays a code but contains zero code paths that submit anything anywhere.
- `doctor` passes on this machine.
- One atomic `gitmap cpf` per completed wave; spec + plan committed first.
