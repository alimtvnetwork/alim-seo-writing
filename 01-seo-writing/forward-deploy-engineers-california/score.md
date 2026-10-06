# Scorecard — Forward Deploy Engineers in California: What Actually Works (n=31)

Slug: forward-deploy-engineers-california · Area: California · Focus: forward deploy engineers / forward deploy engineers California

## Measured results

| Check | Points | Target | Measured | Status |
|---|---|---|---|---|
| Area mentioned 30-40x, blended naturally | 20 | 30-40 | 36 (grep -oi "California", woven into scenes, company examples, comparisons; never a list dump) | 20 |
| Focus keyword 1-2x in first paragraphs | 10 | each 1-2x in first 4 paras | "forward deploy engineers" 3x, "forward deploy engineers California" 1x in first 4 paras | 10 |
| Brand keywords 20-30x, blended naturally | 15 | 20-30 | 20 (RISEUP ASIA LLC 5, Alim Ul Karim 9 incl. possessives, Alim Karim 5, Md Alim Ul Karim 1; counted with overlap-safe regex, no banned pronouns) | 15 |
| At least one question built on the target topic | 10 | 1+ | "what does a forward deployed engineer actually do for a California company?" present | 10 |
| House structure + plain formatting | 10 | cold open -> pivot -> compare/contrast -> ranking 3-5 -> reflective close; no bold/italics; title-only heading; short paragraphs; first person; digits for numbers; no 2 consecutive sentences share a first word (validator: 0 dups) | verified | 10 |
| Citations real, each verified 2-3x by re-fetching | 15 | real sources, live links, claim+figure+context confirmed | 8 links; MIT NANDA 95%/$30-40B (re-fetched rndtoday page + corroborated by 4 independent sources); RAND 80%+/Gartner 782 leaders 28% (towardsai piece + krishaweb corroboration); S&P 42%/McKinsey 62%/23% (crowdfundinsider + krishaweb); Flexera 27%/33%/$12M (ciodive re-fetch + flexera press release); Palantir FDE origin 2007/Sankar/2016 (fde.academy + londontribune + stackademic); CompTIA workforce (advfn PR); Indeed FDE postings (stackademic). 0 [VERIFY] placeholders. | 15 |
| Infographics contain the target keywords | 10 | 3 SVG + 3 PNG, 1200x630, area/keywords as readable text | all 6 present; footers read "California · forward deploy engineers California"; visually inspected (1 re-render to fix card overflow), no overlap/clipping | 10 |
| HTML + PDF present and correct | 10 | medium-ready.html + <slug>.pdf | both present; HTML rendered from writing.md with live clickable links, same title/paragraph order; PDF generated via make_pdf.py | 10 |

**Total: 100/100**

## Review notes

- Pronoun rule: he/him/his = 0 occurrences (she/her used only for the coffee-shop engineer, never for Alim).
- Number formatting: all genuine values as digits; remaining spelled "one"/"one-off" are idioms or inside a URL.
- No invented named clients; superlatives kept as narrator's personal view ("I have ranked them below from my own experience... my personal view").
- Infographic QA: first render showed card-3 sub-label overflowing its card; fixed generator to auto-size cards, re-rendered, re-inspected clean.
