# Spec 03 — Medium Account Assistant CLI (human-in-the-loop)

Version: 2.0.0 (2026-10-13) — config-driven, SQLite store, gitmap macro.

## Goal

A Python CLI that removes the bookkeeping overhead of creating Medium accounts
for real people, while the human performs the signup and publishing clicks in
the browser themselves. All behavior comes from config variables (seedable
config pattern); all state lives in SQLite (gitmap-style); Excel is the
feed-in/feed-out format. A gitmap macro chains the pipeline steps.

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

## DONE vs PENDING (no bullshit)

DONE (this build):
- D1: Seedable config: `config.seed.json` → SQLite `config` table, versioned,
  user overrides preserved. Every tunable comes from config (see 02-config-and-pipeline.md).
- D2: SQLite store (`accounts`, `config` tables) at the configured database path.
- D3: CLI commands: `init`, `add`, `suggest-usernames`, `otp` (display + clipboard copy),
  `profile-prep`, `record-article`, `status`, `guide`, `doctor`,
  `config get/set`, `import-excel`, `export-excel`.
- D4: gitmap macro `maa-onboard` (importable JSON) chaining the pipeline steps.
- D5: `doctor` prerequisite checks (python, sqlite, config, binary, db, openpyxl).
- D6: Seamless human assistance: auto-copy OTP to native OS clipboard (`clip`/`pbcopy`/`wl-copy`)
  and optional browser launcher (`--open`) on `guide` and `otp`.

PENDING (spec'd, NOT built — blocked, do not implement):
- P1: Browser automation of the Medium signup form. Blocked: Medium policy.
- P2: OTP auto-submit. Blocked: Medium policy.
- P3: Programmatic draft creation / publishing. Blocked: Medium policy.
- P4: go-email-reader self-update. Blocked: upstream has no updater.

## CLI surface

`gitmap py 03-ai-scripts/medium-account-assistant.py <command>`

`init`, `add --email --first --last [--username]`, `suggest-usernames`,
`otp --email [--open]` (display + auto-clipboard copy, never submits),
`profile-prep --email`, `record-article --email --url`,
`status [--email]`, `guide --step signup|publish [--open]`, `doctor`,
`config get <Key>`, `config set <Key> <Value>`,
`import-excel --file PATH`, `export-excel [--file PATH]`.

Global: `--workbook` no longer needed — paths come from config.

## Data flow

Excel/CSV (user's feed) → `import-excel` → SQLite `accounts` (source of truth)
→ commands read/write SQLite → `export-excel` → Excel report.

Personal data never enters git: database and workbooks live under
`~/.medium-account-assistant/` (configurable).

## Acceptance

- `doctor` passes on this machine; `config get/set` round-trips; version bump
  merges without clobbering user overrides.
- Full pipeline on a scratch config: init → import-excel → status → otp (fixture)
  → record-article → export-excel, all green.
- `gitmap macro import` accepts the shipped macro JSON; `macro run --dry-run`
  previews the steps.
- One atomic `gitmap cpf`, pushed.
