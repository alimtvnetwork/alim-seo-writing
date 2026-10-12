# Plan: 03-medium-account-assistant-cli

Status: IN PROGRESS 2026-10-13 — spec written; implementation queued.
Spec: 02-spec/21-app/03-medium-account-assistant-cli/

## Scope reminder (hard boundary)

Human performs Medium signup + publishing in the browser. The CLI assists around
those actions only: workbook bookkeeping, username suggestions, OTP display,
profile prep, URL recording. No browser automation against medium.com, no OTP
submission, no programmatic posting — ever.

## Phases and owners

| Phase | Work | Owner | Owned files |
|---|---|---|---|
| 1 | Spec + this plan + subtasks | lead | 02-spec/21-app/03-medium-account-assistant-cli/, .ai-memory/plans/ |
| 2 | CLI implementation: all 8 commands | Worker 01 | 03-ai-scripts/medium-account-assistant.py (new) |
| 3 | End-to-end verification on test workbook + `doctor` | lead | /tmp test workbook |
| 4 | Atomic `gitmap cpf`, push | lead | — |

## Rules for workers

- Workdir repo root. `export PATH="$HOME/.local/bin:$PATH"` before any gitmap call.
- TOTAL BAN on git commands. TOTAL BAN on rg, ripgrep, grep, git grep, Select-String —
  use `gitmap aum search`, `gitmap find`, `gitmap cat`.
- Python only via `gitmap py`. Relative paths only, lowercase filenames.
- On any tool failing twice: stop, report STATUS: BLOCKED with the exact error.

## Acceptance

- `gitmap py 03-ai-scripts/medium-account-assistant.py --help` lists all 8 commands.
- `init` → `add` → `suggest-usernames` → `status` round-trip works on a /tmp workbook.
- `otp` prints a code from a fixture mailbox entry; no code path submits anything.
- `doctor` reports go-email-reader + openpyxl state truthfully.
- Single `gitmap cpf "seo-writing - <summary>"` commit, pushed (no colon in message).
