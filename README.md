# open-source.sgit.ai — open source is a strategy, not a charity

Most sites arguing for open source argue that it is generous. This one does not.

> *"the power of open source is not for the community, it is not because it is nice for
> others, and it is not to give back."*

> *"open source is not free, somebody is always paying for it. What you get from open
> source is freedom, that is different… We play the game of empowering the user and
> being the reputable source of trust. **We are selling trust.**"*

The site's best original claim is that **survivability is not a property of the licence
file — it is a property of the copyright and trademark structure**, and it ships that
claim as [a tool you can run on any vendor](https://open-source.sgit.ai/survivability/stress-test.html)
plus [a self-audit that fails three of its own four legs](https://open-source.sgit.ai/survivability/self-audit.html).

Live site: https://open-source.sgit.ai (GitHub Pages, deployed from `dev`).

## Structure

- `index.html` — the thesis, then the six history corrections, because they establish that this site checks things
- `views/` — the argument: the position, sovereignty, open core vs packaging, and the villagers
- `survivability/` — the argument, the Change-of-Control Stress Test as a working tool, and the self-audit
- `history/` — six corrections leading, the timeline behind them, six success stories, and the numbers (including the ones this site refuses to publish)
- `practice/` — the three licences across three layers, why Apache-2.0 rather than MIT, and publish-the-source-next-to-the-render
- `agents/` — the economics, a dated contradiction published rather than resolved, and four theses that are named and unwritten
- `funding/` — three proposals compared for the first time, a position, and cURL
- `owasp/` — the summit history, with the first-person account marked pending rather than invented
- `shipped/` — what is missing, unsoftened
- `roadmap/` — the build order with its open questions visible
- `documents/` — the source briefs, and where this site diverged from them
- `briefs/` — those briefs, published verbatim
- `about/participant.html` — the participant disclosure, and where our own approach loses
- `admin/` — engineering: comms (tasks & requests), versions, build tooling
- `assets/site.css` — shared stylesheet (sgit.ai design language)

## The agent surface

The commissioning brief treats the agent-discovery ladder as a build requirement rather
than a topic, because an agent-access report against this estate found that *"a link
listed inside a fetched document did not count as having been seen… it can read the map
and cannot walk it."* So:

- **A markdown twin at every URL** — same path, extension swapped, and the links inside
  the markdown point at markdown, so a traversing agent never parses HTML and never
  leaves the markdown surface once it arrives.
- **`llms.txt`, self-sufficient** rather than a bare link list — it states the thesis in
  the file.
- **`llms-full.txt`** — every page concatenated into one file, which removes
  link-following from the problem entirely.

All three are generated from the HTML by `admin/build/gen_markdown.py` and **enforced by
CI**: the build regenerates them and fails if what was committed is stale.

## Build tooling

| File | What it owns |
|---|---|
| `admin/build/version.txt` | The version. One file, bumped exactly once per release. |
| `admin/build/chrome.py` | The single definition of the nav and footer, applied across every page. Also stamps the version into `llms.txt`. |
| `admin/build/gen_markdown.py` | The markdown twins, `llms.txt` and `llms-full.txt`. No dependencies — it runs in CI with nothing installed. |
| `admin/build/validate.js` | The pre-release gate. Node, no packages, same reason. |
| `assets/stress-test.{css,js}` | The stress test. Entirely client-side; answers persist in `localStorage` and are never transmitted. |

## Release process

1. Bump `admin/build/version.txt` (vX.Y.Z, exactly once per release) and add a row to
   `admin/versions.html`; update `admin/comms.html`.
2. `python3 admin/build/chrome.py` — propagates the version badge and any nav/footer change to every page.
3. `python3 admin/build/gen_markdown.py` — regenerates the twins, `llms.txt` and `llms-full.txt`.
4. `node admin/build/validate.js`
5. `git commit -am "site vX.Y.Z: ..." && git push origin dev`

Every push to `dev` runs `.github/workflows/deploy-pages.yml`: validate → auto-tag
(`vX.Y.Z`, verified against `version.txt` and the commit subject, next-minor enforced) →
deploy to GitHub Pages. Pull requests run validation only. Same pipeline as
[SGit-AI__Website](https://github.com/SGit-AI/SGit-AI__Website),
[SGit-AI__Website__NHI](https://github.com/SGit-AI/SGit-AI__Website__NHI) and
[SGit-AI__Website__PKI](https://github.com/SGit-AI/SGit-AI__Website__PKI).

Validation additionally enforces what this site's own argument depends on: a markdown
twin for every page, `llms-full.txt` carrying every page, and a CC BY 4.0 footer on every
markdown file — plus the usual structure, link, version, canonical and key-leak checks.

## Two things deliberately not done

- **The CC0 / CC BY licensing question is published unresolved.** `docs.diniscruz.ai` is
  CC0 1.0 while ~1,100 brief footers say CC BY 4.0, and no document in the corpus
  reconciles them. [Both readings are published and neither is picked](https://open-source.sgit.ai/practice/index.html)
  — declaring an intention retrospectively on the author's behalf would be the kind of
  tidying this site argues against.
- **The SBOM this site tells other people to publish is a stated gap**, not a shipped
  artefact. It is named as [the site's largest inconsistency](https://open-source.sgit.ai/shipped/index.html)
  and is first on the build order.

Both are recorded as [divergences from the brief](https://open-source.sgit.ai/documents/index.html).

All content CC BY 4.0 unless noted. Code under the repository licence.
