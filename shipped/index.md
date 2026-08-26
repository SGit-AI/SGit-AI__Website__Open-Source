<!-- generated from shipped/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.1.2 · canonical: https://open-source.sgit.ai/shipped/index.html*

> No community story by design. No SBOM, despite telling companies to declare their supply chain. Three funding proposals never piloted. A self-audit that fails. And the OWASP account that only one person can write.

---

# What is missing

The house rule is that gaps get a page rather than a footnote. This is that page, and it is deliberately unsoftened — including the items where this site tells other people to do something it has not done itself.

## 1. There is no community story, by design

The position is that open source is right ["even if there are no contributions"](../views/index.md#zero-contributions). That is intellectually coherent and commercially sensible, and it has a specific consequence: **there is nothing here about running a project.** No governance model, no experience of reviewing external pull requests, no code of conduct, no story about a contributor relationship going well or badly.

> **And that is a problem for the site's best idea.**[The survivability argument turns on DCO-versus-CLA in practice](../survivability/index.md#cla) — on what it is actually like to run a project with distributed copyright, and what a maintainer gives up by not aggregating it. This site argues that distinction is the most important structural property of an open-source project, **from a position of having never had to live with either side of it.** That is a real limitation on the argument's authority and it is not fixable by writing more.

It also means this site can say nothing credible about the part of open source most people mean when they say the words: the collaboration.

## 2. Telling companies to declare a supply chain we have not declared

[The labelling argument](../funding/index.md#labelling) asks companies to declare their dependencies, calculate their value contribution, and publish it. What exists on this side:

- **One manual licence review**, from February 2026. One dependency line pulled in **17 transitive dependencies**; each was tabulated with its SPDX identifier against the project's Apache-2.0 licence; the verdict was *"No compliance issues. All MIT, BSD-3-Clause, or Apache-2.0."* It also flagged a non-licence concern — a package entering the tree against an architectural rule.
- **That is it.** One review, once. **No SBOM of the estate. No automated licence scanning. No policy document. No upstream-contribution record.**

**This is the largest inconsistency on the site**, and the honest options were two: state it as an intention with a date, or close it before launch. Closing it is genuinely a day's work — an SBOM of the largest repository plus a CI licence check — and it would convert [the organic-food argument](../funding/index.md#labelling) from a proposal into a demonstration. **It has not been done, and stating it here is the weaker of the two options.**

## 3. The site's best idea fails on its own author

[The self-audit is published in full](../survivability/self-audit.md) and the verdict is **single-party dependent**: three of four legs fail. Single-company copyright, single-company trademark, no named fork capacity, and schemas whose openness is stated but not separately licensed.

It is on this page as well as its own because it belongs in a list of what is missing rather than only in a section where it might read as a display of virtue. **The uncomfortable version:** a project with no external contributors *cannot* have distributed copyright, so the position that makes [gap 1](#community) coherent is the same position that produces this failure. They are one gap wearing two hats.

## 4. Three funding proposals, none costed, none piloted

[The funding page compares them for the first time](../funding/index.md) and takes a position — that they address three different failures and were never competing answers. That is an improvement on presenting three options, and it is still **an argument rather than evidence**.

None has been costed. None has been piloted. The hardest part of the labelling proposal — *how do you calculate a value contribution?* — is unsolved and is the thing that would have to be solved first. And the corpus's own standing admission remains accurate: *"the sustainable funding question is unsettled."*

The [cURL page adds a fourth gap](../funding/curl.md#fix) that none of the three addresses: **nothing funds triage.**

## 5. The strongest human asset is undocumented, and only one person can document it

[The OWASP page ships the summit history and marks the rest pending.](../owasp/index.md) There is no first-person account of the board tenure, no project list, no Open Security Summit founding story, and **no retrospective on any of six published open-source projects** — with one exception, which was written about the author rather than by him.

Thirteen questions are published on that page. They are not researchable; the answers are not on the public record.

## 6. There is no licence taxonomy

[Apache-2.0 versus MIT is now written](../practice/apache-vs-mit.md) — it was the most conspicuous gap and it is closed. What is still absent is the broader treatment: **copyleft versus permissive as a position**, licence compatibility, where AGPL fits, and what to make of the source-available licences that [the relicensing wave produced](../history/index.md#reversals).

The corpus has nothing to build on here — *copyleft* appears zero times with context, AGPL and LGPL zero, GPL twice and both times as litigation precedent. [The history research supplies the ground](../history/index.md); the position has to be written.

## 7. Numbers this site refuses to publish

[Listed in full on the numbers page](../history/numbers.md#unverified): "Linux runs 90% of the cloud" (no primary source, only SEO content citing SEO content), the TOP500 claim (table could not be fetched), Wikipedia's traffic figures (a 2014 number presented as current), GitHub's scale figures (they do not reconcile with each other), and CNCF's 2025 headline (no sample size, no field dates, and 44% of respondents run no AI workloads on Kubernetes at all).

They are named rather than silently omitted, because a reader will meet all of them elsewhere.

## 8. Production gaps

- **No visual assets.** No timeline graphic, no licence-family diagram, no map of the estate, no Wardley map of the open-source landscape. Everything here is prose and tables. That is a real production gap for a site whose [timeline](../history/timeline.md) and [four-leg test](../survivability/stress-test.md) both want a picture.
- **Not indexed.**[The agent-discovery ladder's top rung](../practice/publish-the-source.md#ladder) — getting indexed, which is the real fix — is unaddressed because the site is new. The other three rungs are shipped and enforced in CI.
- **No licence-audit gate in CI.** The build validates structure, links, versions, markdown twins and CC BY footers. It does **not** yet run a dependency licence audit, which is the same gap as [gap 2](#supply-chain) viewed from the pipeline.

## The tensions that will not be resolved by working harder

|  |  |
|---|---|
| **1** | Arguing that open source is a strategy rather than charity — **while depending on a commons built largely by people who thought it was charity.** The position is defensible and the tension is real. Naming it is stronger than resolving it. |
| **2** | **The site's best idea would fail on its author**, and does. See [the self-audit](../survivability/self-audit.md). |
| **3** | **No community, by design** — coherent, commercially sensible, and it silences the site on most of what people mean by open source. |
| **4** | **Telling companies to declare their supply chain without having declared one.** |
| **5** | **Correcting other people's numbers while the corpus carries uncorrected ones** — the $8.8tn figure cited without its definition, the OSSRA percentage cited as share-of-code when it is presence-of-any. [Both are fixed here](../history/numbers.md), and the site must not accumulate new ones. |
| **6** | **Publishing your own weaknesses to an audience that includes people looking for them.** The corpus's own listed tension about publishing security reviews. It applies to this site more than any other — and it is the reason to trust it. |

[← OWASP](../owasp/index.md)[The build order →](../roadmap/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
