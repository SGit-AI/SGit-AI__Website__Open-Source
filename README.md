# open-source.sgit.ai — open source is a strategy, not a charity

The position of [Dinis Cruz](https://www.linkedin.com/in/diniscruz) — founder of
[sgit.ai](https://sgit.ai), [MyFeeds.ai](https://investor.myfeeds.ai/),
[The Cyber Boardroom](https://thecyberboardroom.com), [RiskMandate.ai](https://riskmandate.ai)
and [VoiceDebrief.ai](https://voicedebrief.ai), with the sgit layer commercialised through
[sgraph.ai](https://sgraph.ai); former OWASP Board
member — on what open source is for, how to practise it, and the history that supports
it. It is the strategy those companies run on: everything they ship is open source, and
so are their investor materials.

> *"the power of open source is not for the community, it is not because it is nice for
> others, and it is not to give back."*

> *"open source is not free, somebody is always paying for it. What you get from open
> source is freedom, that is different… We play the game of empowering the user and
> being the reputable source of trust. **We are selling trust.**"*

The site's best original claim is that **survivability is not a property of the licence
file — it is a property of the copyright and trademark structure**, and it ships that
claim as [a tool you can run on any vendor](https://open-source.sgit.ai/survivability/stress-test.html),
run on [the author's own estate](https://open-source.sgit.ai/survivability/self-audit.html)
with the result published.

Live site: https://open-source.sgit.ai (GitHub Pages, deployed from `dev`).

## Structure

- `index.html` — the thesis, the founders' guide first, then the six history corrections, because they establish that this site checks things
- `founders/` — **Owning the code, or opening it**: guidance for founders from a strategy session, released CC BY (attribution Dinis Cruz and Kate Curtis-Evans)
- `infographics/` — the argument in four one-page infographics, each with the page it draws on and the caveat the site attaches; images under `assets/infographics/`
- `views/` — the argument: the position, sovereignty, open core vs packaging, and the villagers — each with its counter-case attached
- `survivability/` — the argument, the Change-of-Control Stress Test as a working tool, and the self-audit
- `history/` — six corrections leading, the timeline behind them, six success stories, and the numbers (including the ones this site declines to publish)
- `practice/` — the three licences across three layers, why Apache-2.0 rather than MIT, and publish-the-source-next-to-the-render
- `agents/` — the economics, two dated positions on the junior pipeline, and four theses that are named and next to be written
- `funding/` — three proposals compared, a position on how they fit, and cURL
- `owasp/` — the summit history from the public record, with the first-person account planned and its questions published
- `roadmap/` — what's next: what is built, what is next in order, and eight open questions
- `documents/` — the source briefs, and where this site diverged from them
- `briefs/` — those briefs, published verbatim
- `about/` — the author, the companies the strategy runs on, and interests declared
- `admin/` — engineering: comms (tasks & requests), versions, build tooling
- `assets/site.css` — shared stylesheet (sgit.ai design language)

## The agent surface

The site treats the agent-discovery ladder as a build requirement rather than a topic,
because an agent-access report against this estate found that *"a link listed inside a
fetched document did not count as having been seen… it can read the map and cannot
walk it."* So:

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
   `admin/versions.html`; update `admin/comms.html` if the board changed.
2. `python3 admin/build/chrome.py` — propagates the version badge and any nav/footer change to every page.
3. `python3 admin/build/gen_markdown.py` — regenerates the twins, `llms.txt` and `llms-full.txt`.
4. `node admin/build/validate.js`
5. `git commit -am "site vX.Y.Z: ..." && git push origin dev`

Every push to `dev` runs `.github/workflows/deploy-pages.yml`: validate → auto-tag
(`vX.Y.Z`, verified against `version.txt` and the commit subject, next-minor or a
deliberate major enforced) → deploy to GitHub Pages. Pull requests run validation only.
Same pipeline as
[SGit-AI__Website](https://github.com/SGit-AI/SGit-AI__Website),
[SGit-AI__Website__NHI](https://github.com/SGit-AI/SGit-AI__Website__NHI) and
[SGit-AI__Website__PKI](https://github.com/SGit-AI/SGit-AI__Website__PKI).

Validation additionally enforces what this site's own argument depends on: a markdown
twin for every page, `llms-full.txt` carrying every page, and a CC BY 4.0 footer on every
markdown file — plus the usual structure, link, version, canonical and key-leak checks.

## Open items, published

- **The licence layers — decided 6 Sep 2026: CC BY 4.0 across everything written.** The
  published-articles repository's `LICENSE` file had said CC0 1.0; that was drift, and the
  file follows. [Recorded on the practice page](https://open-source.sgit.ai/practice/index.html#reading).
- **The SBOM this site tells other people to publish** is
  [first on the build order](https://open-source.sgit.ai/roadmap/index.html#supply-chain).

All content CC BY 4.0 unless noted. Code under the repository licence.
