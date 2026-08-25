<!-- generated from admin/versions.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.1.0 · canonical: https://open-source.sgit.ai/admin/versions.html*

> Site release history. Every push to dev is a release, validated then auto-tagged by CI against the version in admin/build/version.txt and the release commit's subject.

---

# Release history

Every push to `dev` is a release: CI validates the site, verifies the version bump, tags the commit `v{release}.{major}.{minor}`, and deploys to GitHub Pages. The version is owned by `admin/build/version.txt` and must agree with the release commit's subject. [How the pipeline works →](index.md#pipeline)

| Version | Date | What shipped |
|---|---|---|
| v0.1.0 | 25 Aug 2026 | **First release.** The site, built from the commissioning brief pack, which is [published verbatim alongside it](../documents/index.md). **The pipeline first**, matching the sibling sites: validate → auto-tag → deploy, with the version owned by one file and verified against the release commit's subject. Validation additionally enforces the things this site's own argument depends on — **a markdown twin at every URL**, `llms-full.txt` carrying every page, and a CC BY 4.0 footer on every markdown file.**The content:**[the position](../views/index.md) with every argument carrying its counter-case; [survivability](../survivability/index.md) with [the stress test as a working tool](../survivability/stress-test.md) and [a self-audit that fails three of its four legs](../survivability/self-audit.md); [six corrections](../history/index.md) leading the history rather than a timeline; [the three-licence estate](../practice/index.md) and [the Apache-vs-MIT page that existed nowhere](../practice/apache-vs-mit.md); [agents](../agents/index.md); [the three funding proposals compared for the first time](../funding/index.md) and [cURL](../funding/curl.md); [the summit history, with the first-person account marked pending](../owasp/index.md); and [what is missing, unsoftened](../shipped/index.md).**Two things deliberately not done:** the CC0/CC BY licensing question is [published unresolved](../practice/index.md#reading) rather than settled on the author's behalf, and the SBOM the site tells other people to publish [is named as a gap rather than shipped](../shipped/index.md#supply-chain). Both are [recorded as divergences from the brief](../documents/index.md#divergences). |

> **Reading a version number.**`v{release}.{major}.{minor}` — every push to `dev` increments the minor. CI refuses a tag that is not the next minor (or a deliberate major), and refuses one where `version.txt` and the commit subject disagree, so the history above cannot silently skip a release.

[← Comms](comms.md)[Front page →](../index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
