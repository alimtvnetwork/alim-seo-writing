# Subtask 01 — restructure moves (Worker 01)

Owner: Worker 01. Owned files: 01-seo-writing/** (moves only).
Read first: 02-spec/21-app/01-seo-writing-restructure/01-overview.md (mapping rules).

## Steps

1. Inventory: list every directory directly under 01-seo-writing/ (expect ~200 article
   dirs + seo-rules.md + writing-preferences.md at root). Record total file count
   under 01-seo-writing/ (python pathlib via `gitmap py`, not find/grep).
2. Write a python script implementing the mapping RULES (A, D, B, C, E in order) and
   emit `mapping.json` {old_relpath: new_relpath}. Print a per-group count summary.
3. Verify the mapping: every source exists; no two sources share a destination;
   every destination's parent is creatable; root files (seo-rules.md,
   writing-preferences.md) are NOT moved.
4. Execute the moves with python `shutil.move` (plain filesystem moves — never git).
5. Verify after: file count identical to step 1; every leaf article dir contains its
   `writing.md`; no empty leftover dirs.

## Output contract

Reply with: {"task": "Task-02", "status": "DONE|BLOCKED", "dirs_moved": N,
"checks": "<commands> -> exit codes", "evidence": "file count before/after",
"blockers": []}
