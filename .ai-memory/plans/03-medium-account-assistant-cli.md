# Plan: 03-medium-account-assistant-cli

Status: COMPLETED 2026-10-13 — CLI built, verified end-to-end on scratch config,
macro imported, pushed.
Spec: 02-spec/21-app/03-medium-account-assistant-cli/ (01-overview.md, 02-config-and-pipeline.md)

## Scope reminder (hard boundary)

Human performs Medium signup + publishing in the browser. The CLI assists around
those actions only. No browser automation against medium.com, no OTP submission,
no programmatic posting — ever. PENDING items (P1–P4 in spec) are documented,
not built.

## Phases and owners

| Phase | Work | Owner | Owned files |
|---|---|---|---|
| 1 | Spec v2 + this plan + subtasks | lead | 02-spec/21-app/03-medium-account-assistant-cli/, .ai-memory/plans/ |
| 2 | `config.seed.json` + macro JSON (static files) | lead | 03-ai-scripts/medium-account-assistant/ |
| 3 | CLI implementation: config module, SQLite store, all commands | Worker 01 | 03-ai-scripts/medium-account-assistant.py (new) |
| 4 | End-to-end verification on scratch config + `doctor` | lead | /tmp scratch |
| 5 | Atomic `gitmap cpf`, push | lead | — |

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
