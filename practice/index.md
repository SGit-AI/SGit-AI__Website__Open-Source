<!-- generated from practice/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.1 · canonical: https://open-source.sgit.ai/practice/index.html*

> Apache-2.0 on the code, CC BY 4.0 on around 1,100 working documents, and CC0 1.0 on the published essays. The licensing actually in force across the estate, what each licence is for, the reasoning behind the CC BY choice, and the one alignment question still open.

---

# Three licences, three layers, and one nobody had noticed

Anyone can hold a position on open source. Showing the licence file is different. This page is the licensing actually in force across the estate — three licences, three layers, and what each one is for — followed by the reasoning behind the choices, and the one question about aligning them that is still open.

## What is actually in force

| Layer | Licence | Evidence |
|---|---|---|
| **Code** — the application repositories and the Issues-FS estate | **Apache-2.0** | `LICENSE` files, and `license = "Apache 2.0"` in every `pyproject.toml` |
| **Briefs and corpus documents** | **CC BY 4.0** | A footer on roughly 1,100+ files: *"This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0)."* |
| **Published articles** — `docs.diniscruz.ai` | **CC0 1.0 Universal** — public domain | The repository's `LICENSE` file |

> **Three layers, three jobs.** Apache-2.0 for code, where the patent grant matters. CC BY 4.0 for the working documents, where attribution carries provenance — it is *rule two* of the writing discipline, applied to every document, which is what produced 1,100 consistent footers. And CC0 for the published essays, which are public domain: built to travel, with attribution left to courtesy rather than obligation.

## The alignment question, still open

The CC0 layer sits outside the CC BY rule that governs everything else in writing, and the working documents do not say whether that was a deliberate carve-out. Two readings are available, and the reasoning is worth having either way:

|  | Reading A — deliberate layering | Reading B — drift |
|---|---|---|
| **The claim** | Each layer got the licence its *function* needs: Apache-2.0 for code, where a patent grant matters; CC BY for the working corpus, where attribution carries provenance; CC0 for finished essays, where the goal is maximum reach and attribution is friction. | Three repositories were set up at three different times, each with a sensible default for its job, and the layers were never written up as one policy. |
| **What supports it** | It is genuinely coherent, and the estate does think in layers. There is real logic to a published essay being public domain while a working brief carries attribution: **the essay is meant to travel; the brief is meant to be traceable.** | Rule two says CC BY without a stated carve-out, and a three-layer policy is the sort of thing the author normally writes down. That it is not written up yet is the whole of the evidence. |
| **What it would take to confirm** | One sentence from the author saying it was intended. | The same sentence, saying it was not. |

> **Where it stands.** Reading A is the natural one and it is defensible; writing it up as policy is [Q5 on the build order](../roadmap/index.md#open), and one sentence from the author settles it. What is *not* open is this site's own content, which is CC BY 4.0 throughout and stamped in CI.

## The CC BY reasoning, which *is* documented

Four distinct arguments exist for the CC BY choice, and they are worth separating because they are not the same argument:

**Alignment, not compliance.***"The Creative Commons licence aligns with our zero-lock-in principle. We are already committed to zero lock-in and open standards. A project released entirely under CC BY 4.0, using open source tools, with no proprietary components — this is the natural extension of our existing values."*

**It is a hard rule, not a preference.** Rule two of the writing discipline is a licence footer at the bottom of every document, and every day-index brief closes with it. That is what produced 1,100+ consistent footers — **a rule, mechanically applied**, which is why the CC0 divergence stands out as much as it does.

**BY versus BY-SA was actively considered, and BY won.** The question is recorded — *"CC BY-SA 4.0 or CC BY 4.0 for the licence? BY-SA encourages derivatives to stay open; BY is more permissive"* — and permissive was chosen. That is a real decision, and it sits interestingly against [the survivability argument](../survivability/index.md), which is in effect the claim that **licences are the weakest of the structural protections**. If you believe that, choosing the more permissive licence costs you less than it appears to, because you were never relying on the licence to do the work.

**Openness is a credibility asset, and it is backed.***"The transparency claim is credible because it is **backed** (the CC BY 4.0 corpus, the public briefs, rendering from a public vault)."*

## Downstream licences are respected

*"CC BY 4.0 for the article and most contents; original source materials retain their own licences."* In practice that means Wardley-map briefs carry a bespoke footer crediting Simon Wardley's own Creative Commons terms — a small discipline, and a good illustration of the general rule: **your licence governs your contribution, not the material you built on.**

This site applies the same rule and states it explicitly, because it quotes the open-source world at length: Wikipedia material is CC BY-SA and is quoted with attribution rather than adapted; project documentation and vendor reports are cited with source, date and caveat rather than reproduced; [charts from all-rights-reserved analyst reports are never reproduced at all](../history/numbers.md).

## The line: everything open, except at the customer

> "The line is very simple: **everything is open source**, so you do not even have that conversation. It is a key pillar. It is not for everybody, some investors will not like it, but you find the ones who do, and it is a good match. You can always commercial-license or relicense everything for a customer who wants it, but the core is all open source. **No part of the company or the ecosystem is not open source.**"

Note the mechanism hidden in the middle of that: *"you can always commercial-license or relicense everything for a customer who wants it."* That is only possible **because a single company holds the copyright** — which is [exactly the structure leg one of our own stress test asks about](../survivability/self-audit.md). The flexibility and the exposure are the same fact viewed from two sides, and it is worth being clear that they cannot be separated.

And the commercial hook is explicitly not the code: *"We do not have that lock-in on technology, and that is fundamental. The natural line is a business line, and that is okay: that is when you charge to maintain it. It is the hook, but a hook based on value… The customer's schemas can be closed, a lot of their data is closed, **but our schemas are open**."*

Whether the customer subset makes this open core rather than packaging is [a separate page with a one-question test](../views/open-core.md).

## What has actually been published

| Package or estate | Where | Note |
|---|---|---|
| **`sgit-ai`** | PyPI · `SGit-AI/SGit-AI__CLI` | Named that way because *"`sgit` was already taken"*. CI: push to main → tests → deploy to qa → PyPI publish. |
| `sg-send-cli` | PyPI | **Deprecated 20 March 2026**, superseded by `sgit-ai`. |
| **`issues-fs`** and six siblings | `owasp-sbot` | All Apache-2.0. [The org choice is itself a thread →](../owasp/index.md) |
| **The `osbot-*` / `mgraph-*` family** | PyPI · `owasp-sbot` | Described internally as *"2 years of open source infrastructure"*. **`MGraph-DB` is publicly credited to the OWASP community.** |

> **Next for this page: the retrospectives.** Six published projects, and the story of why each was open-sourced, what the licence decision was, and what happened afterwards is still to be written — the O2 Platform account exists, written about the author rather than by him, and is the model. [On the build order →](../roadmap/index.md#interview)

### [Why Apache-2.0 rather than MIT](apache-vs-mit.md)

*Written fresh*

The most conspicuous unwritten page in the whole brief: the entire estate rests on that choice and the reasoning existed nowhere.

### [Publish the source next to the render](publish-the-source.md)

*A mechanism*

The markdown twin at every URL, how it was actually built, and the radical version nobody has shipped: publish the evidence and every prompt.

[← The numbers](../history/numbers.md)[Why Apache-2.0, not MIT →](apache-vs-mit.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
