# Subtask 02 — OTP display, profile prep, guide, doctor

Owner: Worker 02. Owned file: `03-ai-scripts/medium-account-assistant.py`
(fill the stubs left by Worker 01; coordinate via the lead — do not start
until Worker 01's skeleton is committed).

## Deliverable

Implement the stubbed commands in the existing CLI file:

1. `otp --email E` — shell out to the go-email-reader binary (locate:
   `~/workspace/go-email-reader/go-email-reader`, else PATH) `read` command
   for the latest message to `--email`; extract the first 6-digit code with
   regex; PRINT it with "paste this into Medium yourself — this tool never
   submits codes anywhere." Update `otp_last_shown_at`. If the binary or
   mailbox is unreachable, print the exact error and exit 3.
2. `profile-prep --email E` — print 3 bio draft options (role + beat +
   "writing about X" templates, no invented credentials); suggest avatar
   filename convention `<username>-white.jpg`; store chosen bio/avatar in
   workbook. Never invent job titles or affiliations.
3. `record-article --email E --url URL` — validate URL looks like a Medium
   post URL; set `article_url`, status → `published`, stamp updated_at.
4. `guide --step signup|publish` — print the human checklist:
   - signup: open medium.com → Sign up with email → enter details from
     `status` → run `otp --email` → paste code manually → complete profile.
   - publish: write/paste article in Medium editor → review → press Publish
     manually → run `record-article --email --url`.
5. `doctor` — report: python version, openpyxl present/missing,
   go-email-reader binary found/missing (+ version if `--version` works),
   workbook path exists/missing. Exit 0 only if all green.

## Hard prohibitions (assert in code review)

- No selenium/playwright/requests calls to medium.com.
- No function that posts, submits, or clicks anything on any website.
- The word "submit" must not appear in OTP handling except in the
  "never submits" notice.
