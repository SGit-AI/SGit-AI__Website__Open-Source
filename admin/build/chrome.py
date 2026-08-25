#!/usr/bin/env python3
"""The single definition of this site's nav and footer, and the tool that applies it.

Run from anywhere: python3 admin/build/chrome.py

Every page is hand-written static HTML — that stays true, because a human should
be able to open any file and edit it. What is NOT hand-maintained is the chrome:
the nav row (including the version badge that validate.js requires to agree
everywhere) and the footer columns. Those are defined once here and rewritten in
place across the tree, which is what stops a twenty-page site from drifting.

Adding a page: add it to NAV or FOOTER if it belongs there, write the file with
any nav/footer block at all, then run this — then run gen_markdown.py, because
every page owes a markdown twin.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()
GH = "https://github.com/SGit-AI/SGit-AI__Website__Open-Source"
PARENT = "https://sgit.ai"
PARENT_TITLE = ("sgit.ai — the parent project: the vault layer and the shipped CLI whose "
                "licence and sovereignty argument this site holds")

# The nav, two levels. Each entry is (label, own page, [(sub-label, href), ...], (path prefixes)).
#
# Two rules the structure has to keep:
#   · A group label is always a link to a real page, never a menu-only stub. Nothing on
#     this site should be reachable only by opening a dropdown.
#   · `prefixes` decides the "here" state, so a page that is not itself in the nav still
#     lights up the group it belongs to.
NAV = [
    ("The argument", "views/index.html", [
        ("The position", "views/index.html"),
        ("Sovereignty", "views/sovereignty.html"),
        ("Open core, or packaging?", "views/open-core.html"),
        ("Somebody has to be the villagers", "views/villagers.html"),
    ], ("views/",)),
    ("Survivability", "survivability/index.html", [
        ("Not a licence property", "survivability/index.html"),
        ("The stress test", "survivability/stress-test.html"),
        ("The self-audit", "survivability/self-audit.html"),
    ], ("survivability/",)),
    ("History", "history/index.html", [
        ("Six corrections", "history/index.html"),
        ("The timeline", "history/timeline.html"),
        ("Six success stories", "history/stories.html"),
        ("The numbers", "history/numbers.html"),
    ], ("history/",)),
    ("Practice", "practice/index.html", [
        ("Three licences", "practice/index.html"),
        ("Why Apache-2.0, not MIT", "practice/apache-vs-mit.html"),
        ("Publish the source", "practice/publish-the-source.html"),
    ], ("practice/",)),
    ("Agents &amp; funding", "agents/index.html", [
        ("Agents and open source", "agents/index.html"),
        ("Funding", "funding/index.html"),
        ("cURL", "funding/curl.html"),
        ("OWASP &amp; the summits", "owasp/index.html"),
    ], ("agents/", "funding/", "owasp/")),
    ("Site", "shipped/index.html", [
        ("What is missing", "shipped/index.html"),
        ("Build order", "roadmap/index.html"),
        ("The documents", "documents/index.html"),
        ("Comms: tasks &amp; requests", "admin/comms.html"),
        ("Release history", "admin/versions.html"),
        ("Admin &amp; engineering", "admin/index.html"),
        ("Where we lose", "about/participant.html"),
    ], ("shipped/", "roadmap/", "documents/", "admin/", "about/")),
]

FOOTER = [
    ("The argument", [
        ("The position", "views/index.html"),
        ("Sovereignty", "views/sovereignty.html"),
        ("Open core, or packaging?", "views/open-core.html"),
        ("Somebody has to be the villagers", "views/villagers.html"),
    ]),
    ("Survivability", [
        ("&#8594; Run the stress test", "survivability/stress-test.html"),
        ("Not a licence property", "survivability/index.html"),
        ("The self-audit", "survivability/self-audit.html"),
    ]),
    ("The record", [
        ("Six corrections", "history/index.html"),
        ("The timeline", "history/timeline.html"),
        ("Six success stories", "history/stories.html"),
        ("The numbers", "history/numbers.html"),
        ("Three licences", "practice/index.html"),
    ]),
    ("Site", [
        ("What is missing", "shipped/index.html"),
        ("Build order", "roadmap/index.html"),
        ("The documents", "documents/index.html"),
        ("Comms: tasks &amp; requests", "admin/comms.html"),
        ("Release history", "admin/versions.html"),
        ("Where we lose", "about/participant.html"),
        ("llms.txt", "llms.txt"),
        ("llms-full.txt", "llms-full.txt"),
    ]),
]

BLURB = ("Open source as a strategy rather than a charity: the position, the practice, and a "
         "history checked against its sources. Part of the <a href=\"https://sgit.ai\" "
         "style=\"display:inline;padding:0\"><b>sgit.ai</b></a> network. All content CC BY 4.0.")
PARTNOTE = ('⚠ Participant disclosure: published by the sgit project, whose own estate is the '
            'subject of the <a href="{up}survivability/self-audit.html" '
            'style="display:inline;padding:0">self-audit</a> — and which fails leg one.')
NETLINE = ('<a href="https://sgit.ai"><b>↗ sgit.ai</b></a> — the parent project · '
           '<a href="https://standards.sgit.ai">↗ standards.sgit.ai</a> — SPDX and the compliance machinery · '
           '<a href="https://wardley-maps.sgit.ai">↗ wardley-maps.sgit.ai</a> — the PST pattern · '
           '<a href="https://sgit.ai/network/index.html">↗ the network</a>')
PARTNOTE_SELF = '⚠ Participant disclosure: published by the sgit project. You are on the disclosure page.'


def nav_html(rel, up):
    groups = []
    for label, own, subs, prefixes in NAV:
        active = rel == own or any(rel.startswith(pre) for pre in prefixes)
        links = "\n".join(
            f'      <a class="sl{" here" if href == rel else ""}" href="{up}{href}">{text}</a>'
            for text, href in subs)
        groups.append(
            f'    <div class="ni ni-has">\n'
            f'      <a class="nl{" here" if active else ""}" href="{up}{own}">{label}'
            f'<span class="caret">&#9662;</span></a>\n'
            f'      <div class="sub">\n{links}\n      </div>\n'
            f'    </div>')
    rows = "\n".join(groups)
    return (f'<nav class="site"><div class="row">\n'
            f'  <a class="brand" href="{up}index.html">open-source<span>.sgit.ai</span></a>\n'
            f'  <a class="parent" href="{PARENT}" title="{PARENT_TITLE}">↗ part of <b>sgit.ai</b></a>\n'
            f'  <span class="stage-pill">first draft</span>\n'
            f'  <a class="ver" href="{up}admin/versions.html" title="Site release history">{VERSION}</a>\n'
            f'  <button class="nav-toggle" type="button" aria-expanded="false" aria-label="Menu">Menu</button>\n'
            f'  <div class="nav-items">\n{rows}\n  </div>\n'
            f'  <a class="gh" href="{GH}">★ GitHub</a>\n'
            f'  <script src="{up}assets/nav.js" defer></script>\n'
            f'</div></nav>')


def footer_html(rel, up):
    partnote = PARTNOTE_SELF if rel == "about/participant.html" else PARTNOTE.format(up=up)
    md = rel[:-len("html")] + "md"
    cols = "\n".join(
        "  <div>\n"
        f"    <h4>{head}</h4>\n"
        + "\n".join(f'    <a href="{l if l.startswith("http") else up + l}">{t}</a>' for t, l in links)
        + "\n  </div>"
        for head, links in FOOTER)
    return (f'<footer class="site"><div class="cols">\n'
            f'  <div>\n'
            f'    <div class="brandline">open-source<span>.sgit.ai</span></div>\n'
            f'    <p>{BLURB}</p>\n'
            f'    <p class="netline">{NETLINE}</p>\n'
            f'    <p class="partnote">{partnote}</p>\n'
            f'    <p class="verline">site <a href="{up}admin/versions.html">{VERSION}</a> · '
            f'<a href="{up}admin/index.html">engineering</a> · '
            f'<a href="{up}{md}">this page as markdown</a></p>\n'
            f'  </div>\n{cols}\n</div></footer>')


def stamp_text_twins():
    """The version also appears in llms.txt, and validate.js enforces that it agrees.
    Own it here rather than hand-editing it every release. llms-full.txt and the
    per-page markdown twins are generated by gen_markdown.py, which reads it too."""
    out = []
    llms = ROOT / "llms.txt"
    if llms.exists():
        t = llms.read_text()
        t2, n = re.subn(r"Site version: v\d+\.\d+\.\d+", f"Site version: {VERSION}", t, count=1)
        if n and t2 != t:
            llms.write_text(t2)
            out.append("llms.txt")
    return out


def main():
    changed = []
    for path in sorted(ROOT.rglob("*.html")):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        up = "../" * (len(path.relative_to(ROOT).parts) - 1)
        text = path.read_text()
        before = text
        text, n_nav = re.subn(r'<nav class="site">.*?</nav>', lambda _: nav_html(rel, up),
                              text, count=1, flags=re.S)
        text, n_foot = re.subn(r'<footer class="site">.*?</footer>', lambda _: footer_html(rel, up),
                               text, count=1, flags=re.S)
        if not n_nav or not n_foot:
            print(f"  ! {rel}: missing {'nav' if not n_nav else ''}{' and ' if not n_nav and not n_foot else ''}"
                  f"{'footer' if not n_foot else ''} block", file=sys.stderr)
        if text != before:
            path.write_text(text)
            changed.append(rel)
    changed += stamp_text_twins()
    print(f"chrome: {VERSION} applied — {len(changed)} file(s) updated")
    for c in changed:
        print(f"  · {c}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        # piped into head/less — not an error
        sys.stdout = None
