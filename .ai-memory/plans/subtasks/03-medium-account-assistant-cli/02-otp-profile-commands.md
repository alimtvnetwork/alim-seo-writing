# Subtask 02 — OTP display, profile prep, guide, doctor

Owner: Worker 02. Owned file: `03-ai-scripts/medium-account-assistant.py`
(fill the stubs left by Worker 01; start only after Worker 01's file is committed).

Spec: 02-spec/21-app/03-medium-account-assistant-cli/01-overview.md +
02-config-and-pipeline.md.

## Deliverable

1. `otp --email E` — read `Paths.GoEmailReaderPath`, `Mailbox.OtpRegex`,
   `Mailbox.OtpMaxAgeMinutes`, `Mailbox.MailboxTimeoutSeconds` from config;
   shell out to the binary's `read` for the latest message to the address;
   extract first regex match; check message age ≤ OtpMaxAgeMinutes (warn if
   older); PRINT the code with: "paste this into Medium yourself — this tool
   never submits codes anywhere." Update `OtpLastShownAt`. Binary/mailbox
   unreachable → exact error, exit 3.
2. `profile-prep --email E` — 3 bio draft options (role + beat templates, no
   invented credentials); avatar filename convention `<username>-white.jpg`;
   store chosen bio/avatar.
3. `record-article --email E --url URL` — URL must start with
   `https://medium.com/`; status → `published`; stamp updated_at.
4. `guide --step signup|publish` — human checklists (spec 01).
5. `doctor` — python version; sqlite3 ok; config keys all present;
   go-email-reader binary exists (try `--version`); DB writable;
   openpyxl present/missing (warn only). Exit 0 iff all required green.

## Hard prohibitions (verify before finishing)

- No selenium/playwright/requests. No posting/submitting/clicking on any site.
- "medium.com" appears only inside `guide` checklist text and the
  `record-article` URL prefix check.
