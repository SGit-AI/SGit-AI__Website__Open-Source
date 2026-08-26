<!-- generated from index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.1.2 · canonical: https://open-source.sgit.ai/index.html*

> The power of open source is not that it is nice for others. It is that it removes the technology moat, and it is the only structure under which sovereignty is possible. The position, the practice, and a history checked against its sources — including six corrections to the story most sites tell.

---

Open source · sovereignty · survivability · the economics

# Open source is a strategy. It is not a charity.

Most sites arguing for open source argue that it is generous. This one does not. **The power of open source is not for the community, it is not because it is nice for others, and it is not to give back** — it is that technology stops being the moat, that you become free to delete your own code, and that sovereignty becomes possible at all. And the accurate history supports that far better than the romantic one does.

[Read the position →](views/index.md)[Run the stress test on a vendor →](survivability/stress-test.md)[Six corrections to the history →](history/index.md)

## Not free. Free*dom*.

Two sentences carry the whole site. The first is the unfashionable one; the second is the one that makes it land.

> "the power of open source is not for the community, it is not because it is nice for others, and it is not to give back."

> "open source is not free, somebody is always paying for it. What you get from open source is freedom, that is different… We play the game of empowering the user and being the reputable source of trust. **We are selling trust.**"

Everything else here is a consequence of those two. If open source is a gift, then its funding problem is a moral failure and the answer is to shame people into paying. If it is a strategy, the funding problem is an *externality* — and externalities are fixed by structure and by market forces, not by virtue. [cURL is the case that settles it →](funding/curl.md)

## Three asks, and they are in very different states

This site was commissioned to cover the views, the practice, and the history. Being straight about how well-founded each of those is comes first, because the site's whole credibility position is that it corrects other people's unsourced claims.

| The ask | State of the record | What this site does |
|---|---|---|
| **The views** | **Very rich** — 56 catalogued concepts, 24 of them original arguments rather than restatements | [Argues them, and names the counter-case each time](views/index.md) |
| **The practice** | **Rich, and partly undocumented even to its author** — three licences across three layers, one of which nobody had noticed | [Publishes the licences, and the reasoning that was missing](practice/index.md) |
| **The history** | **Absent** — not thin. Zero occurrences of "free software", "copyleft", "Stallman", "Netscape", "SourceForge" or "FSF" anywhere in the corpus | [Researched from scratch, and it changes the standard story](history/index.md) |

That last row is the finding that shaped the site. It is a clean division of labour: **the argument comes from the corpus, the ground under it comes from fresh research** — and the research turned out to support the argument better than the version everybody repeats. [What is still missing, unsoftened →](shipped/index.md)

## Six things the standard history gets wrong

These lead, rather than a timeline, because everyone has a timeline and almost nobody publishes these. Each one is checkable, and each one points the same way: the model wins on **economics and structure**, not on virtue and not on eyeballs.

### [Unix circulated because it was illegal to sell it](history/index.md#unix)

*1955–1982*

The 1956 AT&T consent decree barred Bell Labs from any business but common-carrier communications. Unix shipped for media and postage as a **compliance artefact**. The decree lifted in 1982 and AT&T commercialised System V immediately.

### [BSD lost to litigation risk, not to its licence](history/index.md#bsd)

*1992–1994*

USL v. BSDi clouded free Unix during exactly the window Linux needed. The settlement removed **three files out of eighteen thousand**. The claim was nearly empty; the two years of uncertainty were decisive.

### [Netscape's source release was a six-year near-failure](history/index.md#netscape)

*1998–2004*

The code was so degraded the team threw it away and rewrote. **Firefox 1.0 did not ship until November 2004**, by which time IE had won. The founding case study of the movement is a cautionary tale.

### [Eric Raymond did not coin "open source"](history/index.md#peterson)

*Feb 1998*

**Christine Peterson** did — and deliberately had someone with more credibility as a Linux programmer introduce it, so that it would spread. Sources disagree on the exact day; they do not disagree on who.

### ["Given enough eyeballs" is not a security property](history/index.md#eyeballs)

*2014, 2024*

Heartbleed survived two years in the most security-critical library on the internet. **xz was engineered by the maintainer to survive review** — and was caught by one engineer benchmarking SSH latency, not by a security review.

### [Two of the four relicensings reversed](history/index.md#reversals)

*2018–2025*

Elastic added AGPLv3 in August 2024; Redis 8 shipped AGPLv3 in May 2025. That does not weaken the survivability argument — **it sharpens it**. The same single-holder standing that let them leave let them come back.

## The best idea here, and it fails on its own author

Buyers read licence files. Licence files are the *weakest* of the structural protections, and 2018–2024 is the proof.

> "Survivable is not a property of the licence file. **It is a property of the copyright and trademark structure.**"

The mechanism, which is what makes it a finding rather than an opinion: *"Every catalogued relicensing between 2018 and 2024 followed the same legal pattern: a single corporate copyright holder, having aggregated contributor copyright via a CLA, exercised the right to change terms going forward. Distributed-copyright projects could not be moved the same way, because no single party had standing."* And the kicker — **HashiCorp went BUSL, IBM acquired it, and the licence stayed.** Acquisition entrenches the closure; it does not reverse it.

### [Why the licence is the weakest protection](survivability/index.md)

*The argument*

PostgreSQL is the control case — no company owns it, so no company can relicense it, and it is now the most-used database. OpenSolaris is the counter-case. The licence was not the problem; the copyright holder was.

### [The Change-of-Control Stress Test](survivability/stress-test.md)

*The tool*

Four legs — copyright, trademark, schema licence, named fork capacity — every one answerable from public artefacts, with no cooperation from the vendor. **Run it here, on any project, and keep the result.**

### [We run it on ourselves, and we fail leg one](survivability/self-audit.md)

*The self-audit*

SGraph's copyright is held by one company — the exact single-holder pattern the argument names as the failure mode. Here is the verdict, what would have to change, and whether we intend to change it.

## The positions, with their counter-cases attached

A page that only states one side reads as advocacy. Every argument here carries the strongest objection to it, and two of them carry **dated contradictions from the author's own corpus**, published rather than tidied away.

### [Sovereignty requires open source](views/sovereignty.md)

*Four steps*

You are one SLA away from losing access; the schemas matter as much as the code; and whichever government has jurisdiction over the company that controls the code controls everyone downstream. Necessary, but not sufficient — and the site stays careful about that.

### [Open core, or packaging?](views/open-core.md)

*Contradiction*

18 June: *"There should be nothing proprietary."* 17 July: *"customers only have a subset of the code that exists in the main repo."* Five weeks apart, and the July document diagnoses itself. Here is the test that settles which one it is.

### [Somebody has to be the villagers](views/villagers.md)

*The market*

Maintaining the non-functional requirements as a market, and the ability to read and repair code somebody else wrote as an appreciating asset — published with both of its own counter-arguments, including the sharp one: a firm paid to maintain has no incentive to say the thing should be retired.

### [Agents, and the junior pipeline](agents/index.md)

*Contradiction*

March said the density of learning per hour increases. July said the gains shifted work from juniors to seniors, at exactly the moment the maintenance need is growing. Four months, opposite directions, both published.

### [Three funding answers, and a position](funding/index.md)

*Unsettled*

Labelling, a maintainer platform, sovereignty bounties. None costed, none piloted, never compared — until here. Three unreconciled proposals read as thinking; presented as a position they read as indecision.

### [The position in full](views/index.md)

*All of it*

Technology is not the moat. Lock-in relocates to quality and certification. Lock-in degrades your own architecture. Open source frees you to cannibalise your own code. And the moat is a rate, not a wall: a competitor who forks today gets your position, not your velocity.

## Anyone can hold a position. Showing the licence file is different

This is the page that makes the rest credible — and writing it turned up an inconsistency in the estate's own licensing that nobody had noticed.

### [Apache-2.0, CC BY 4.0 — and CC0](practice/index.md)

*Three licences*

Code is Apache-2.0. Around 1,100 brief footers say CC BY 4.0. And `docs.diniscruz.ai` is **CC0 1.0** — public domain — which no document in the corpus mentions or reconciles. Deliberate layering, or drift? The page answers it.

### [Why Apache-2.0 rather than MIT](practice/apache-vs-mit.md)

*Written fresh*

The entire estate rests on that choice and the reasoning existed nowhere. The patent grant, the defensive termination clause, the NOTICE file — and the honest cost, which is that Apache-2.0 is the heavier licence to comply with.

### [Publish the source next to the render](practice/publish-the-source.md)

*A mechanism*

Every page available as markdown at the same path with the extension swapped, and the links inside the markdown pointing at markdown — **which is how this site is built**. Plus the radical version: publish the evidence, the provenance, and every prompt.

## Agents are a primary audience of this site, so traversal is a build requirement

An agent-access report run against this estate found the failure precisely: *"many agents can only fetch URLs that a search engine has already returned to them… **A link listed inside a fetched document did not count as having been seen.** It can read the map and cannot walk it."* A site about open source that agents cannot traverse fails in exactly the way its own corpus already diagnosed.

| The rung | What this site ships | What it fixes |
|---|---|---|
| **The markdown twin** | **Every page**, same path, extension swapped — and links inside the markdown point at markdown | An agent never parses HTML, and never leaves the markdown surface once it arrives |
| **`llms.txt`** | **Self-sufficient** — it states the thesis rather than linking to it | A bare link list is the failure mode when links inside a document do not count as seen |
| **`llms-full.txt`** | **Every page in one file** | Removes link-following from the problem entirely |
| **Getting indexed** | **Not yet** — the site is new | The real fix, and the one that is not in our gift. [Stated as a gap →](shipped/index.md) |

Read this page as [markdown](index.md), take the whole site as [llms-full.txt](llms-full.txt), or start from [llms.txt](llms.txt). The generator is [published with the rest of the build tooling](admin/index.md), because a site making this argument should show the mechanism.

## Where this site is weak, stated by the site

The house rule is that the gaps get a page rather than a footnote. These are the load-bearing ones.

### By design, and it costs something

*No community*

The position is that open source is right *"even if there are no contributions."* Coherent — and it means this site can say nothing credible about governance, PR review, or codes of conduct **despite the survivability argument turning on DCO-vs-CLA in practice**.

### Telling others to declare what we have not

*The supply chain*

One manual licence review exists, from February 2026: 17 transitive dependencies, an SPDX table, a clean verdict. **No SBOM of the estate, no automated scanning, no policy, no upstream-contribution record.**

### The OWASP account is third-person

*Blocked*

Former board member, named organiser of the 2011 Lisbon and 2017 Woburn summits, the current estate under `owasp-sbot` — **all of it written about him, from public sources.** The summit history ships; the first-person account is marked pending rather than invented.

### [The full list, unsoftened](shipped/index.md)

*All of it*

Including the self-audit that fails, the three funding proposals that were never compared, and every statistic the research could not verify — which are named and **not published as established**.

## Who is writing this

Published by the sgit project, which runs entirely on the model it is arguing for — and which [fails leg one of its own stress test](survivability/self-audit.md). That is stated here rather than discovered later. The discipline applies lightly to the [history](history/index.md), because those claims are externally verifiable and cited, and heavily to the argument, which is why every argument on this site carries its counter-case and why the tool is shipped for you to run rather than as a scorecard we publish about other people.

[The participant disclosure, in full →](about/participant.md)[The build order, published unresolved →](roadmap/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
