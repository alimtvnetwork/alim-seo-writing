# Subtask 03 — backfill missing html/pdf (Worker 02, wave 2)

Owner: Worker 02. Runs AFTER Worker 01's moves are verified complete.
Owned files: 01-seo-writing/** (new files only — never modify existing files).

## Steps

1. Walk the regrouped 01-seo-writing/ tree (python pathlib via `gitmap py`).
2. For every leaf article dir missing `medium-ready.html`: generate it from
   `writing.md` (same wrapper as seo-scaffold.py; reuse its code).
3. For every leaf article dir missing `<slug>.pdf`: run `seo-pdf.py` on it.
4. Verify: zero leaf article dirs lack `medium-ready.html` or `<slug>.pdf`;
   report counts (generated_html=N, generated_pdf=M).

## Output contract

Reply with: {"task": "Task-03b", "status": "DONE|BLOCKED",
"checks": "<commands> -> exit codes",
"evidence": "generated_html=N generated_pdf=M, remaining_missing=0", "blockers": []}
