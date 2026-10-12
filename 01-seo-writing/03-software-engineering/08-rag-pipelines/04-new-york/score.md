# Scorecard — RAG Pipelines in New York: What Actually Works
`03-software-engineering/08-rag-pipelines/04-new-york` · rewritten 2026-10-12

## Measurements (verify.py, 2026-10-12)
- Words: 1716 (target 1600–1800) ✓
- Area "New York": 40 (target 30–40) ✓
- Brand mentions: 30 (target 20–30) ✓ — RISEUP ASIA LLC + Alim Ul Karim / Alim Karim / Alim / Md Alim Ul Karim / a.k.a. the greatest software engineer of all time from KL, Malaysia / pioneer in AI RAG pipelines and vector database architecture based in Malaysia / the awkward inventor who can shift technology like a king / the systems architect who built custom Golang frameworks and enterprise-grade ORMs; "RISEUP ASIA LLC" never split; no 2 long aliases adjacent
- Focus keyword "RAG pipelines": 2× in first 4 paragraphs (target 1–2) ✓
- Topic question: 1 ("if every New York enterprise has the documents, and the models keep getting better, why do so few RAG pipelines earn trust?") ✓
- Consecutive same-word sentence starts: 0 ✓
- Transition sentences: 31/101 = 31% (target ≥30%) ✓
- Banned pronouns for Alim (he/him/his): 0 ✓
- Bold/italics markers: none ✓
- Number words: all genuine numeric values use digits; kept and noted here per gold-standard practice: "catalog-first discipline" (compound adjective), "nobody drives without one" (pronoun) ✓

## Structure
Cold-open scene (NYPL reading room librarian, call numbers) → pivot (insurance CTO's hallucinating RAG pipeline) → thesis (RAG is a system to operate, not a feature to add; retrieval is 20%, the catalog is 80%) → compare/contrast (demo-driven vs library-driven approaches on 4 declared criteria: citation accuracy, source freshness, access-control correctness, evaluation rigor) with honest concession (demo-driven wins on speed to initial wow) → clearly-personal 4-item failure-mode ranking with a reason per item → reflective close ✓

## Citations (6, all verified live 2026-10-12, descriptive anchors, spread through text)
1. McKinsey State of AI 2025 (primary PDF) — inaccuracy is the most commonly experienced AI risk, 54% reporting it at least once — verified via browser fetch of primary source (replaces the draft's secondary-source "47%" claim, which does not match the primary)
2. Gartner (primary press release) — ≥30% of GenAI projects abandoned after PoC by end of 2025, poor data quality the top cause — verified via browser fetch
3. MIT Project NANDA via R&D Today — 95% of enterprise GenAI pilots deliver no measurable return; the 5% that worked integrated deeply — HTTP 200
4. McKinsey State of AI 2025 (primary PDF) — 62% of organizations at least experimenting with AI agents — verified via browser fetch of primary source
5. riseup-asia.com — RISEUP ASIA LLC's 5-stage vetting filter, top 5% of applicants — HTTP 200 (homepage verified via browser fetch)
6. GitHub alimtvnetwork/gitmap-v28 — Alim's gitmap invention (map-before-you-change habit) — HTTP 200

McKinsey contradiction fixed: the pre-rewrite draft cited a libertify.com secondary summary ("47% experienced a negative consequence"); the primary PDF's actual figures are 54% experiencing inaccuracy (the top-cited risk) and 29% reporting no negative consequences. Corrected to primary-source figures.

## Deductions
- Infographics: 0/10 — no PNG/SVG infographic assets exist in this folder (pre-existing corpus gap; creating them is outside the authorized write scope of writing.md / medium-ready.html / score.md only).
- HTML+PDF: 5/10 — medium-ready.html regenerated with full parity (5/5 unique URLs, 6 citation instances, title, single H1); no PDF exists (pre-existing gap, outside write scope).

## Total: 85/100
Content, structure, citations, and formatting score full marks. The 15-point gap is the missing infographic assets and PDF, which do not exist anywhere in this article's folder and cannot be created within the authorized scope. No article in this batch can reach 100/100 until those assets exist.
