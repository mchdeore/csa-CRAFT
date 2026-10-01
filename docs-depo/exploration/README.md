# Exploration

Research on dependencies, open-source tools, and patterns worth tracking for
possible future integration into CRAFT. Each entry is a markdown file following
the template below. Nothing here is consumed by code — it's reference material.

## Entry template

```markdown
# <Project / Topic Title>

**Source:** <URL>
**License:** <SPDX ID, e.g. MIT, Apache-2.0>
**Last reviewed:** <YYYY-MM-DD>
**Stars / adoption signal:** <stars, downloads, or "n/a">
**Primary language:** <Python / TypeScript / mixed / n/a>

## One-line summary
<what it is in a sentence>

## Why it's here
<why we're tracking this — the specific capability or pattern we might lift>

## Structure / key artifacts
<the files, modules, or concepts that matter — bullet list, not a full tour>

## Integration ideas for CRAFT
<concrete ways this could plug into our codebase>

## Risks / caveats
<license incompatibility, abandoned repo, heavy transitive deps, API churn>

## Citations
- <URL #1 — specific file or doc>
- <URL #2>
```

## Adding an entry

1. Create `<slug>.md` using the template above.
2. Fill every header field. Leave "Last reviewed" blank only if you intend to
   fill it in the same commit.
3. Cite specific files or docs — not just the repo root — under Citations.
4. Flag licenses clearly. GPL/AGPL in a dependency chain is a hard stop for us.
