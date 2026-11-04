# Ambiguities — seo-articles-and-avatar-generation (autopilot, 2026-11-05)

Recorded without waking the operator, per the "I am sleepy" checklist.
Each entry: question, autopilot pick, what would change it.

## 01. Article count and split
- Question: user said "two, three articles regarding this" (US dominance)
  plus "another one" (franchise model).
- Pick: 3 articles total — A1 US software dominance (giants + AI players),
  A2 Rise Up Asia engineering edge (10X-30X logic, NY + CA markets),
  A3 software franchise model + who dominates now.
- Change it: user names a different count in the morning; extra articles can
  be added as a follow-up task.

## 02. Article groups and target areas
- Question: which 01-seo-writing group and target area per article?
- Pick: A1 -> 03-software-engineering, area New York; A2 ->
  05-riseup-asia-brand, area California; A3 -> 02-franchise, area New York.
  Each follows 01-seo-writing/seo-rules.md (one area, 1-2 focus keywords,
  area 30-40x, brand 20-30x, score.md must hit 100).
- Change it: research agents may recommend a better group/area in the spec;
  spec step has final say before writing.

## 03. Avatar folder and style
- Question: "put it to its own avatar folder" — new folder or existing?
- Pick: new dedicated folder assets/avatars/seo-articles-and-avatar-generation/,
  5 personas (mixed male/female, writer roles, names not colliding with the
  existing 61 personas), batch-2 style (1080x1080 PNG, white background,
  with-noise finish), one image per persona; assets/avatars/README.md table
  updated accordingly.
- Change it: user prefers black variants too — those can be generated later.

## 04. Rise Up Asia metrics are user-asserted
- Question: "50-70 years combined experience", "dominating NY/CA markets",
  "10X-30X better results" — no third-party source on file.
- Pick: articles attribute these to the company / user account and link
  riseup-seo.com; never presented as independently verified statistics.
  No invented stats about real companies anywhere (seo-rules.md rule 4).
- Change it: user supplies a citable source; articles updated.

## 05. AI companies cash-flow claim
- Question: "all these AI companies are highly negative in cash flow".
- Pick: verify against real reporting (OpenAI / Anthropic losses) with live
  links; if unverifiable, soften to reported/attributed wording.
- Change it: a solid source confirms or refutes; wording follows the source.

## 06. Pre-existing truncated avatar files (NOT mine, left untouched)
- Question: 5 files in assets/avatars/ show as modified, each replaced by a
  ~130-byte truncated JPEG (david-huang-finance-writer-with-noise.png,
  david-kim-proofreader-black.jpg, david-kim-proofreader-white.jpg,
  nora-hassan-seo-writer-white-with-noise.png,
  olivia-bennett-newsletter-writer-black-with-noise.png).
- Pick: left exactly as found; excluded from this task's commits; flagged
  here for morning review (likely a failed sync/LFS artifact).
- Change it: operator confirms restore (git checkout) or intentional change.

## 07. Spec and plan numbers
- Question: task brief uses "XX" placeholder.
- Pick: 05 — next after 01-04 in 02-spec/21-app/; plan at
  .ai-memory/plans/pending/05-seo-articles-and-avatar-generation.md.
- Change it: none expected; numbers are sequential.

## 08. Dictation source
- Question: user said "keep these articles writing into the verbatim folder,
  dictation" — the brief itself is the dictation.
- Pick: the user message saved verbatim as two dictation files under
  dictations/riseup-asia-llc/ dated 2026-11-05 (us-software-dominance,
  software-franchise-model), status raw; each finished article links back
  to its dictation source per dictations/README.md workflow.
- Change it: user dictates corrections; notes appended, never edited.

## 06b. Update (2026-11-05, 01:21 +08): truncated files changed again
- The 5 files from entry 06 are back to full on-disk size (3.8 MB / 34 KB /
  2.0 MB range) but still show as Modified vs HEAD — consistent with another
  agent regenerating them mid-flight. Still OUT OF SCOPE, still excluded
  from this task's commits. Re-check git status before the final commit.

## 09. Research Agent 02 findings (2026-11-05, 01:22 +08) — fact corrections
- "All AI companies highly negative in cash flow" is FALSE as a blanket
  statement: Anthropic's S-1 shows H1 2026 operating cash flow +$3.929B and
  a Q2 2026 operating profit; its $80.7B net loss is ~90% non-cash
  convertible-note revaluation. Articles must say OpenAI is projected
  loss-making (~$14B in 2026, reported internal projections) while
  Anthropic's headline loss is mostly non-cash — never "Anthropic burned
  $80.7B in cash."
- Market-cap figures differ by source/day: date-stamp every figure ("as of
  early November 2026") and never present a ranking as fixed; never present
  the four companies' fiscal-year revenues as one calendar year (different
  fiscal year-ends).
- RISEUP ASIA LLC founding year conflicts (Clutch 2024 vs DesignRush 2025):
  do NOT state a founding year.
- Earlier dictations' flagged items ($500M salaries, 30-40% salary claims,
  100K USD monthly pricing) remain unverified and must NOT migrate into
  these articles.
- Full verified citation shortlist is in the Agent 02 research report
  (market cap, 10-K revenue/profit, OpenAI projections, Anthropic S-1,
  Clutch/DesignRush profiles, franchise trade guides).

## 10. Lead correction (2026-11-05, 01:25 +08): CITATIONS.md A2/A3 labels
- The citations appendix originally mapped A2 = franchise, A3 = RISEUP
  deep dive — the reverse of SPEC.md and the plan (A2 = RISEUP engineering
  edge, A3 = franchise). Lead relabeled the appendix (map, section
  headings, citation IDs A2-F1/F2 -> A3-F1/F2, internal-linking paragraph)
  and reordered the sections to A1, A2, A3 so all three docs agree.
  No citation content changed; article workers must follow SPEC.md mapping.

## 11. Minor deviation logged (2026-11-05, 01:40 +08): A3 worker grep use
- The A3 article worker disclosed using `grep` to inspect line ranges of
  the infographic script and to validate its own new files/PDF text.
  Codebase searching was via GitMap per the ban; the grep use was limited
  to the worker's own files, not repo-wide search. Logged here for
  transparency; deliverables unaffected. No action required.
