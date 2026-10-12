# Spec 04.2 — Content Pipeline

Version: 1.0.0 — 2026-10-13
Normative companions: 02-spec/21-app/04-blog-folder-creation-and-content-strategy/01-overview.md

This spec is normative for both blog outlets (riseup-asia, medium). It defines the
pipeline every article must pass through, the scorecard rubric with the adapted
density check, the rewrite gate, and the cross-outlet differentiation rule.

## Pipeline stages

1. Scaffold
   - Create 04-blogs/<outlet>/<slug>/ with the house file set: writing.md,
     score.md, medium-ready.html, infographic-philosophy.md.
   - Slugs are lowercase, hyphenated, outlet-agnostic (outlet lives in the path).
2. Draft (writing.md)
   - Style: plain title first line (no #), first-person, cold-open scene in a
     named local place, pivot to thesis, evidence with real verified citation
     links, numbered compare/contrast, personal ranking, reflective close.
   - Constraints: NO bold/italics, NO he/him/his pronouns, digits for all
     quantities, no consecutive same-word sentence starts, brand token exactly
     `RISEUP ASIA LLC`, at least one question on the target topic.
   - Risk handling (mandatory, non-negotiable): delete the "Desi culture
     oversell" passage entirely — keep "metrics-based, no overselling" with zero
     ethnic attribution; never publish "100K USD monthly"; genericize
     "OpenAI/Anthropic trillion-dollar" to "the largest AI labs"; drop fabricated
     Steve Jobs quotes; never state $10k/$12k/$50k as H1B salaries; cut
     "21-day waitlist / people come begging" unless verified; frame "AI product
     does not work" as opinion; convert $500M/30-40% figures to the rhetorical
     question without numbers; cut "100x better"; delete "India/Singapore cheap
     companies" stereotyping; reframe "without H1B paperwork" as "without the
     visa sponsorship process".
   - Keyword cluster: primary keyword cluster (exact phrase + rotated aliases)
     must reach 30-60 combined natural mentions per article; no single exact
     phrase above ~3% density; distribute across intro, 4-6 sections, local
     scenes, conclusion CTA.
3. Critical score (score.md)
   - Format: '# Scorecard — <slug>', Article/Target lines, 8-check table /100,
     Total line, '## Verification notes', '## Checks run (scripted)'.
4. Rewrite gate
   - Total must reach >=95, else a rewrite pass is mandatory. See gate rules below.
5. medium-ready.html render
   - Paragraph-identical to writing.md. Dark-theme render: background #090611,
     Georgia serif, max-width 680px.
   - Paragraph parity is checked mechanically: every paragraph in writing.md
     must appear verbatim in the HTML in the same order.
6. infographic-philosophy.md (visual brief)
   - Written brief only: message, data points, layout direction, brand tokens.
   - PNG/SVG generation via 03-ai-scripts/seo-infographic.py is a FOLLOW-UP,
     not part of this run.

## Scorecard rubric (8 checks, /100)

| # | Check | Max |
|---|-------|-----|
| 1 | Keyword cluster 30-60x natural mentions (exact phrase + rotated aliases; no single exact phrase above ~3% density; spread across intro, sections, local scenes, CTA) | 20 |
| 2 | Local-place cold-open and geographic grounding (named CA/SD/NY places woven into the narrative, not dropped in) | 10 |
| 3 | Thesis clarity and evidence (verifiable citation links, real sources, [VERIFY] dispositions resolved) | 15 |
| 4 | Risk handling compliance (all banned claims removed or genericized per the mandatory list) | 15 |
| 5 | Style constraints (no bold/italics, no he/him/his, digits for quantities, no consecutive same-word starts, brand token exactly `RISEUP ASIA LLC`) | 10 |
| 6 | Website references: 1-2 natural anchors to https://riseup-asia.com (mid-article proof placement + closing CTA) | 10 |
| 7 | Structure (cold-open -> pivot -> evidence -> numbered compare/contrast -> personal ranking -> reflective close; at least one question on the target topic) | 10 |
| 8 | Cross-outlet differentiation (zero duplicated paragraphs vs the sibling outlet's version of the same story) | 10 |

Check 1 note (density reconciliation): the user's 30-60x instruction OUTRANKS the
house 30-40x norm. The scorecard records the deviation explicitly: "house norm
30-40x superseded by user instruction 30-60x for spec 04". Aliases must be
rotated so the exact phrase never reads as stuffed; a density spike above ~3%
for any single exact phrase fails check 1 regardless of the combined count.

'## Verification notes' must list every cited URL with its fetch date and the
disposition of every [VERIFY] item carried over from the dictation notes.
'## Checks run (scripted)' must report machine counts: cluster count, brand
token count, pronoun hits, sentence-start collisions, spelled-out quantities,
sentence count.

## Rewrite gate rules

- Score >=95: ship to medium-ready.html render.
- Score <95: one rewrite pass targeting the lowest-scoring checks first; then
  re-score fully (no partial re-scores).
- Maximum 3 rewrite passes. If still <95 after pass 3, escalate to the user
  with the failing checks — do not silently lower the bar.
- A rewrite pass must change wording, not just keyword counts: density fixes
  that read as stuffing fail check 1.

## Cross-outlet differentiation rule

- Same facts, different framing. The RiseUp Asia outlet version is the brand
  voice; the Medium version is first-person practitioner, slightly more
  contrarian/opinionated.
- Zero duplicated paragraphs across outlets. Shared facts may be cited, but
  every paragraph must be written fresh per outlet.
- Verification: a paragraph-level diff between outlets must show no identical
  paragraphs (scripted check in 'Checks run').

## Follow-ups (not in this run)

- Infographic PNG/SVG generation per infographic-philosophy.md via
  03-ai-scripts/seo-infographic.py (with mandatory overlap self-check).
- PDF render of writing.md (seo-pdf.py pattern) if the outlet needs it.
