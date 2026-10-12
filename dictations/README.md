# Dictations

Raw dictated articles from the user, saved verbatim. These are source material —
finished articles get written from them later. Never edit a dictation file's
transcript; if the user corrects something, add a note at the bottom instead.

## Folder structure

```
dictations/
  README.md                  # this file — the convention
  <company-slug>/            # one folder per company, e.g. riseup-asia-llc
    YYYY-MM-DD-<topic-slug>.md
```

- `<company-slug>`: lowercase company name, spaces → hyphens
  (e.g. "RISEUP ASIA LLC" → `riseup-asia-llc`).
- File name: dictation date + short topic slug.
- Each file starts with a metadata header (date, dictated by, intended outlet,
  status) followed by the verbatim transcript.

## Workflow

1. User dictates → save verbatim under the right company folder, status `raw`.
2. Later, when the user asks, draft the finished article from the dictation
   following `01-seo-writing/seo-rules.md` and `writing-preferences.md`,
   and link the article back to its dictation source.
