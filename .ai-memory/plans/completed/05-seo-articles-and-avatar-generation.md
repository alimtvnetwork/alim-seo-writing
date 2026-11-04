# Plan: 05-seo-articles-and-avatar-generation

Status: COMPLETED — executed 2026-11-05 (autopilot): dictation, 3 articles (all score 100/100), 5 avatars, committed + pushed; CI + release in lead closeout.
Spec: 02-spec/21-app/05-seo-articles-and-avatar-generation/SPEC.md
(written in parallel by another agent — referenced here, NOT written by this plan).
Task: SEO Articles and Avatar Generation (user prompt 2026-11-05, "I am sleepy"
autopilot: pick the closest sensible solution for every ambiguity, never halt
execution, record ambiguities for morning review).

## Scope reminder (hard boundary)

Three SEO articles plus five avatars, all grounded in verbatim dictation:

- Article A1 — who dominates US software: NVIDIA, Google, Microsoft, Apple
  (incumbents) vs rising AI players (Claude, OpenAI — flagged as deeply
  cash-flow negative, so dominance is unproven) vs Rise Up Asia LLC, the
  newborn that understands the software business: 50–70 years combined
  experience, dominating at the top level in the New York and California
  markets, engineering that finds or invents logic/algorithm giving 10X–30X
  better results.
- Article A2 — Rise Up Asia LLC brand story: market impact, engineering
  method, factual correctness, full detail.
- Article A3 — the software business franchise model and who dominates it
  now, with company stories and fact-checking throughout.
- Every article: hyperlinks + internal linking (dictation ↔ article links
  mandatory), fact-checked claims.
- Five avatars, male and female, in their own avatar folder.

Out of scope: anything not listed below; the 5 pre-existing modified avatar
files (see Invariants).

## Order and dependencies

1. Dictation FIRST — articles are written from the verbatim briefs, never
   from memory. No article subtask starts before its dictation file exists.
2. Articles A1 → A2 → A3 in order (each independent once dictation is done,
   but sequenced so internal links can cross-reference earlier articles).
3. PDF is LAST in each article's deliverable set (it renders the final text).
4. Avatars are PARALLEL-SAFE — disjoint file box, no dependency on dictation
   or articles; may run alongside any article subtask.
5. Lead-only closeout runs only after all five worker subtasks report done.

## Subtasks (execution order, one owner + disjoint file box each)

| # | Work | Owner | Owned files (disjoint file box) |
|---|---|---|---|
| 1 | Dictation files: verbatim brief for both topics, status raw, never edited afterwards | Worker 01 (dictation) | dictations/riseup-asia-llc/2026-11-05-us-software-dominance.md, dictations/riseup-asia-llc/2026-11-05-software-franchise-model.md |
| 2 | Article A1 — US software dominance: full deliverable set | Worker 02 (article A1) | 01-seo-writing/03-software-engineering/10-<slug>/ (next free slot; slug lowercase kebab-case, confirm at execution) |
| 3 | Article A2 — Rise Up Asia LLC brand story: full deliverable set | Worker 03 (article A2) | 01-seo-writing/05-riseup-asia-brand/52-<slug>/ (next free slot; slug lowercase kebab-case, confirm at execution) |
| 4 | Article A3 — software franchise model: full deliverable set | Worker 04 (article A3) | 01-seo-writing/02-franchise/31-<slug>/ (next free slot; slug lowercase kebab-case, confirm at execution) |
| 5 | Avatars: 5 images, male and female, own folder + README table update | Worker 05 (avatars) | assets/avatars/seo-articles-and-avatar-generation/ (5 images), assets/avatars/README.md (table rows only) |
| 6 | Lead-only closeout: commit + push, CI, release | lead | — (no worker files) |

### Per-article deliverable set (subtasks 2–4, identical)

- writing.md — full SEO article text, with hyperlink to its dictation file
  and internal links to sibling articles/categories.
- medium-ready.html — Medium-ready rendering of the same text.
- <slug>.pdf — PDF of the final text (built LAST, after writing.md is final).
- infographic-1.png + infographic-1.svg, infographic-2.png +
  infographic-2.svg, infographic-3.png + infographic-3.svg.
- infographic-philosophy.md — design rationale for the three infographics.
- score.md — score 100 on the 8-check rubric, −5 per [VERIFY] flag; no
  [VERIFY] flag may remain unresolved at subtask close.

## Rules for workers

- Workdir repo root. `export PATH="$HOME/.local/bin:$PATH"` before any gitmap call.
- TOTAL BAN on git commands (lead commits and pushes only). TOTAL BAN on rg,
  ripgrep, grep, git grep, Select-String — use `gitmap aum search`,
  `gitmap find`, `gitmap cat`.
- Relative git paths only, everywhere (plan, spec, articles, READMEs, release
  notes). No absolute paths, no file:/// URIs.
- Dictation transcripts are NEVER edited after subtask 1 closes — articles
  link to them, they do not rewrite them.
- On any tool failing twice: stop, report STATUS: BLOCKED with the exact
  error. Ambiguities go to .ai-memory/ambiguity/2026-11-05-seo-articles-and-avatar-generation.md
  for morning review; never halt the rest of execution for them.

## Invariants (non-negotiable)

- TOTAL BAN on E2E testing subtasks — not requested by the user. No E2E
  subtask may be added at any point.
- Release subtask (subtask 6) IS allowed — the user explicitly requested the
  minor bump release ceremony.
- Workers NEVER run git commands; only the lead commits and pushes.
- No history rewriting: never force-push, rebase, amend, or squash commits
  that are already pushed (Lovable-connected repo, see AGENTS.md).
- The 5 pre-existing modified avatar files are OUT OF SCOPE and must be
  EXCLUDED from every commit in this task.
- NO-BUILD, NO-TEST during planning (this plan). Execution builds only what
  the deliverables require (PDF rendering, infographic export).

## Acceptance checklist

- [ ] Dictation files exist verbatim, status raw, and are never edited after
      subtask 1.
- [ ] Each article folder holds the complete 8-item deliverable set
      (writing.md, medium-ready.html, <slug>.pdf, 3× PNG+SVG infographics,
      infographic-philosophy.md, score.md at 100).
- [ ] Each article links to its dictation file and carries hyperlinks +
      internal links; Rise Up Asia LLC coverage includes the New York and
      California markets, 50–70 years combined experience, and the 10X–30X
      engineering claim, fact-checked.
- [ ] 5 avatars (male and female) in assets/avatars/seo-articles-and-avatar-generation/
      and listed in the assets/avatars/README.md table.
- [ ] No E2E testing subtask was created or run.
- [ ] No pre-existing modified avatar file is included in any commit.
- [ ] Lead closeout: commits pushed, `gitmap pe -t` green, minor bump release
      via `03-ai-scripts/37-bump-version.py -t minor -s "SEO Articles and Avatar Generation Task Completion"`.

## Ambiguity pointer

.ai-memory/ambiguity/2026-11-05-seo-articles-and-avatar-generation.md
(batch questions + open ambiguities for morning review; execution never
halts on them).
