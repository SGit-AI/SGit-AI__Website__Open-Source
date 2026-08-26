<!-- generated from admin/versions.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.1.2 · canonical: https://open-source.sgit.ai/admin/versions.html*

> Site release history. Every push to dev is a release, validated then auto-tagged by CI against the version in admin/build/version.txt and the release commit's subject.

---

# Release history

Every push to `dev` is a release: CI validates the site, verifies the version bump, tags the commit `v{release}.{major}.{minor}`, and deploys to GitHub Pages. The version is owned by `admin/build/version.txt` and must agree with the release commit's subject. [How the pipeline works →](index.md#pipeline)

| Version | Date | What shipped |
|---|---|---|
| v0.1.2 | 26 Aug 2026 | **Two external sources cited, where the site had been naming sources without linking them.**[The numbers page](../history/numbers.md#88tn) now links the **HBS AI Institute** summary of working paper 24-038 — the origin of the $8.8tn figure it spends a section correcting — with its authors, its data sources, and the two concentration findings in it that are more useful than the headline. A page whose credibility position is that it checks other people's citations should carry its own. **And [the training-data thesis](../agents/index.md#training) acquires a dated instance.** Mozilla's chief executive, interviewed by **The Deep View** in August 2026, is shipping model choice in Firefox and backing **open-weight** models on lock-in grounds — making this site's standards-and-control argument, in his own words, about models rather than code. Cited with the caveat it needs: it is positioning from an interested party, and it [sharpens Q7](../roadmap/index.md#open) rather than settling it, because open weight is the category the OSI's definition excludes. |
| v0.1.1 | 25 Aug 2026 | **The build tooling was never committed.** The repository's stock Python `.gitignore` carries a bare `build/` rule, which silently swallowed the whole of `admin/build/` — `chrome.py`, `gen_markdown.py`, `validate.js` and `version.txt`. Everything passed locally, where the files exist; the first CI run failed at once, on the very first step, because they were not in the checkout. Fixed with the same `!admin/build/` negation the sibling sites carry. Recorded here rather than amended away, because [a site that publishes its own failed audit](../survivability/self-audit.md) does not get to quietly rewrite a bad release out of its history. It is also a small illustration of the pipeline working as intended: **the release that could not be validated never got a tag and was never published.** |
| v0.1.0 | 25 Aug 2026 | **First release.** The site, built from the commissioning brief pack, which is [published verbatim alongside it](../documents/index.md). **The pipeline first**, matching the sibling sites: validate → auto-tag → deploy, with the version owned by one file and verified against the release commit's subject. Validation additionally enforces the things this site's own argument depends on — **a markdown twin at every URL**, `llms-full.txt` carrying every page, and a CC BY 4.0 footer on every markdown file.**The content:**[the position](../views/index.md) with every argument carrying its counter-case; [survivability](../survivability/index.md) with [the stress test as a working tool](../survivability/stress-test.md) and [a self-audit that fails three of its four legs](../survivability/self-audit.md); [six corrections](../history/index.md) leading the history rather than a timeline; [the three-licence estate](../practice/index.md) and [the Apache-vs-MIT page that existed nowhere](../practice/apache-vs-mit.md); [agents](../agents/index.md); [the three funding proposals compared for the first time](../funding/index.md) and [cURL](../funding/curl.md); [the summit history, with the first-person account marked pending](../owasp/index.md); and [what is missing, unsoftened](../shipped/index.md).**Two things deliberately not done:** the CC0/CC BY licensing question is [published unresolved](../practice/index.md#reading) rather than settled on the author's behalf, and the SBOM the site tells other people to publish [is named as a gap rather than shipped](../shipped/index.md#supply-chain). Both are [recorded as divergences from the brief](../documents/index.md#divergences). |

> **Reading a version number.**`v{release}.{major}.{minor}` — every push to `dev` increments the minor. CI refuses a tag that is not the next minor (or a deliberate major), and refuses one where `version.txt` and the commit subject disagree, so the history above cannot silently skip a release.

[← Comms](comms.md)[Front page →](../index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
