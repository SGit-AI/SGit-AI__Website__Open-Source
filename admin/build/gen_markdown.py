#!/usr/bin/env python3
"""Generates the markdown twin of every page, plus llms.txt's index and llms-full.txt.

Run from anywhere: python3 admin/build/gen_markdown.py

WHY THIS EXISTS, and why it is a build requirement rather than a nicety.

The commissioning brief for this site carries a finding from an agent-access report
run against the estate in August 2026:

    "many agents can only fetch URLs that a search engine has already returned to
     them... A link listed inside a fetched document did not count as having been
     seen. It can read the map and cannot walk it."

A site *about* open source that agents cannot traverse fails in exactly the way the
corpus already diagnosed. So the mitigation ladder is built in, not bolted on:

  1. the markdown twin at every URL — same path, extension swapped, and links INSIDE
     the markdown point at markdown, so a traversing agent never has to parse HTML
     and never leaves the markdown surface once it arrives;
  2. llms.txt, self-sufficient rather than a bare link list;
  3. llms-full.txt — every page concatenated into one file, which removes
     link-following from the problem entirely.

The HTML stays hand-written and authoritative. This derives from it, so the two can
never disagree: CI regenerates and fails the build if the result differs from what
was committed.

The converter handles only the tag vocabulary this site actually uses. That is
deliberate — a general HTML-to-markdown converter would be a dependency, and this
has to run in CI with nothing installed.
"""
import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VERSION = (ROOT / "admin/build/version.txt").read_text().strip()
HOST = (ROOT / "CNAME").read_text().strip()
LICENCE = ("This page is released under the Creative Commons Attribution 4.0 "
           "International licence (CC BY 4.0).")

# Rendered in llms.txt / llms-full.txt in this order. Anything not listed is still
# given a twin; it just sorts after these.
ORDER = [
    "index.html", "founders/index.html", "infographics/index.html",
    "views/index.html", "views/sovereignty.html", "views/open-core.html", "views/villagers.html",
    "survivability/index.html", "survivability/stress-test.html", "survivability/self-audit.html",
    "history/index.html", "history/timeline.html", "history/stories.html", "history/numbers.html",
    "practice/index.html", "practice/apache-vs-mit.html", "practice/publish-the-source.html",
    "agents/index.html", "funding/index.html", "funding/curl.html", "owasp/index.html",
    "roadmap/index.html", "documents/index.html",
    "about/index.html", "admin/index.html", "admin/comms.html", "admin/versions.html",
]

BLOCK = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "tr", "blockquote", "pre",
         "div", "section", "header", "main", "table", "thead", "tbody", "ul", "ol",
         "figure", "figcaption"}
SKIP = {"script", "style", "nav", "footer", "head", "button", "svg"}


class Node:
    __slots__ = ("tag", "attrs", "kids", "text")

    def __init__(self, tag, attrs=None, text=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.kids = []
        self.text = text

    def cls(self):
        return self.attrs.get("class", "").split()


class Tree(HTMLParser):
    """Builds a tree of the body, dropping anything in SKIP entirely."""

    VOID = {"br", "hr", "img", "meta", "link", "input", "source"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.stack = [self.root]
        self.skip_depth = 0
        self.in_body = False

    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.in_body = True
            return
        if self.skip_depth:
            if tag not in self.VOID:
                self.skip_depth += 1
            return
        if tag in SKIP:
            self.skip_depth = 1
            return
        if not self.in_body:
            return
        node = Node(tag, {k: (v or "") for k, v in attrs})
        self.stack[-1].kids.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        if tag == "body":
            self.in_body = False
            return
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag in self.VOID or not self.in_body:
            return
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.skip_depth or not self.in_body or not data.strip():
            return
        self.stack[-1].kids.append(Node("#text", text=data))


def md_escape(s):
    # Only the characters that would change meaning mid-sentence. Deliberately not
    # aggressive: over-escaping makes the markdown twin unpleasant to read, and a
    # reader — human or agent — is the point.
    return s.replace("|", "\\|")


def rel_md(href, from_rel):
    """Rewrite an internal .html link to its .md twin. This is the rule that keeps a
    traversing agent on the markdown surface: it arrives at one .md and every link it
    finds is another .md."""
    if re.match(r"^(https?:|mailto:|data:|//|#)", href):
        return href
    path, _, frag = href.partition("#")
    if path.endswith(".html"):
        path = path[:-len("html")] + "md"
    return path + ("#" + frag if frag else "")


def inline(node, from_rel):
    """Render inline content. Returns a string with no newlines."""
    if node.tag == "#text":
        return md_escape(re.sub(r"\s+", " ", node.text))
    inner = "".join(inline(k, from_rel) for k in node.kids)
    t = node.tag
    if t in ("b", "strong"):
        return f"**{inner.strip()}**" if inner.strip() else ""
    if t in ("em", "i"):
        return f"*{inner.strip()}*" if inner.strip() else ""
    if t == "code":
        return f"`{inner.strip()}`"
    if t == "br":
        return " "
    if t == "img":
        # An image is carried into the twin as a markdown image, same relative path:
        # the .md sits next to the .html, so the src resolves identically.
        src = node.attrs.get("src", "")
        alt = " ".join(node.attrs.get("alt", "").split())
        return f"![{alt}]({src})" if src else ""
    if t == "a":
        href = node.attrs.get("href", "")
        text = inner.strip()
        if not text:
            return ""
        return f"[{text}]({rel_md(href, from_rel)})"
    return inner


def cell(node, from_rel):
    return " ".join("".join(inline(k, from_rel) for k in node.kids).split()).strip()


# Anything not listed here is inline, and a RUN of inline siblings has to be
# emitted as one paragraph rather than one block each. Rendering them separately
# is what turned "<blockquote>text <b>emphasis</b> text</blockquote>" into three
# stacked block quotes — correct-looking HTML, unreadable markdown.
INLINE_TAGS = {"#text", "a", "b", "strong", "em", "i", "code", "span", "br", "small", "sup", "sub", "img"}


def render_children(node, from_rel, out, depth=0):
    """Render a container's children, grouping consecutive inline siblings into one
    paragraph and recursing into the block ones."""
    run = []

    def flush():
        if not run:
            return
        text = " ".join("".join(run).split()).strip()
        run.clear()
        if text:
            out.append(text)

    for k in node.kids:
        # A card is a block whatever tag carries it — and it is usually carried by
        # <a>, which is otherwise inline. Checking the class first is what stops a
        # linked card being swallowed into the surrounding paragraph as one long
        # link label.
        if k.tag in INLINE_TAGS and "card" not in k.cls():
            run.append(inline(k, from_rel))
        else:
            flush()
            render(k, from_rel, out, depth)
    flush()


def render_card(node, from_rel, out, depth=0):
    """A card: an eyebrow <span class="tag">, a heading, a paragraph, and — when the
    card is itself a link — a "Read →" affordance. Rendered as a small titled block
    so the markdown keeps the grouping the layout expresses visually."""
    label = next((" ".join(inline(k, from_rel).split()).strip()
                  for k in node.kids if k.tag == "span" and "tag" in k.cls()), "")
    href = node.attrs.get("href")
    body = Node("div")
    # The eyebrow is emitted as the label and the "go" chevron is pure navigation;
    # neither belongs in the flow.
    body.kids = [k for k in node.kids
                 if not (k.tag == "span" and ("tag" in k.cls() or "go" in k.cls()))]
    buf = []
    render_children(body, from_rel, buf, depth)
    blocks = [b for b in buf if b.strip()]
    if not blocks:
        return
    # Promote the card's heading to a linked heading when the whole card is a link,
    # so a reader of the markdown can still follow where the card pointed.
    head = blocks[0]
    if head.startswith("#"):
        hashes, _, text = head.partition(" ")
        if href:
            text = f"[{text}]({rel_md(href, from_rel)})"
        blocks[0] = f"{hashes} {text}"
    elif href:
        blocks[0] = f"[{head}]({rel_md(href, from_rel)})"
    if label:
        blocks.insert(1 if blocks[0].startswith("#") else 0, f"*{label}*")
    out.extend(blocks)


def render(node, from_rel, out, depth=0):
    """Walk the tree emitting markdown blocks into `out`."""
    t = node.tag

    # A card is a self-contained unit and it is written BOTH as <div class="card">
    # and as <a class="card" href="..."> — the linked form being the common one. So
    # dispatch on the class before the tag, or the anchor branch below flattens the
    # whole card (heading, body, affordance) into a single link label.
    if "card" in node.cls():
        render_card(node, from_rel, out, depth)
        return

    if t in ("h1", "h2", "h3", "h4", "h5", "h6"):
        text = " ".join(inline(node, from_rel).split()).strip()
        if text:
            out.append("#" * int(t[1]) + " " + text)
        return

    if t == "p":
        text = " ".join(inline(node, from_rel).split()).strip()
        if text:
            # The card "Read →" affordances are navigation, not prose; the link
            # itself is already emitted by the card's own heading.
            out.append(text)
        return

    if t == "blockquote":
        buf = []
        render_children(node, from_rel, buf, depth)
        body = "\n\n".join(b for b in buf if b.strip())
        if body:
            out.append("\n".join("> " + line if line else ">" for line in body.split("\n")))
        return

    if t == "pre":
        raw = "".join(_flatten_text(k) for k in node.kids).strip("\n")
        if raw.strip():
            out.append("```\n" + raw + "\n```")
        return

    if t in ("ul", "ol"):
        marker = (lambda i: "- ") if t == "ul" else (lambda i: f"{i}. ")
        items = []
        n = 0
        for k in node.kids:
            if k.tag != "li":
                continue
            n += 1
            buf = []
            render_children(k, from_rel, buf, depth + 1)
            body = "\n\n".join(b for b in buf if b.strip())
            if body:
                pad = " " * len(marker(n))
                lines = body.split("\n")
                items.append(marker(n) + lines[0] + "".join("\n" + (pad + l if l else "")
                                                            for l in lines[1:]))
        if items:
            out.append("\n".join(items))
        return

    if t == "table":
        rows = []
        head = None
        for tr in _find(node, "tr"):
            cells = [cell(c, from_rel) for c in tr.kids if c.tag in ("th", "td")]
            if not cells:
                continue
            if head is None and any(c.tag == "th" for c in tr.kids):
                head = cells
            else:
                rows.append(cells)
        if head is None and rows:
            head = [""] * len(rows[0])
        if head:
            width = max([len(head)] + [len(r) for r in rows]) if rows else len(head)
            head = head + [""] * (width - len(head))
            lines = ["| " + " | ".join(head) + " |",
                     "|" + "|".join(["---"] * width) + "|"]
            for r in rows:
                r = r + [""] * (width - len(r))
                lines.append("| " + " | ".join(r) + " |")
            out.append("\n".join(lines))
        return

    if t in ("div", "section", "header", "main", "thead", "tbody", "#root", "span", "figure", "figcaption"):
        # A .card is a self-contained unit whose <span class="tag"> is its label.
        classes = node.cls()
        if "note" in classes or "warnbox" in classes or "evbox" in classes:
            buf = []
            render_children(node, from_rel, buf, depth)
            body = "\n\n".join(b for b in buf if b.strip())
            if body:
                out.append("\n".join("> " + l if l else ">" for l in body.split("\n")))
            return
        if "crumb" in classes:
            return
        render_children(node, from_rel, out, depth)
        return

    if t == "#text":
        text = " ".join(md_escape(node.text).split()).strip()
        if text:
            out.append(text)
        return

    if t == "a":
        # A bare anchor at block level (a .cta, say) — emit it as a line.
        text = inline(node, from_rel).strip()
        if text:
            out.append(text)
        return

    render_children(node, from_rel, out, depth)


def _flatten_text(node):
    if node.tag == "#text":
        return node.text
    return "".join(_flatten_text(k) for k in node.kids)


def _find(node, tag, out=None):
    out = [] if out is None else out
    for k in node.kids:
        if k.tag == tag:
            out.append(k)
        else:
            _find(k, tag, out)
    return out


def page_title(source):
    m = re.search(r"<title>(.*?)</title>", source, re.S)
    return html.unescape(m.group(1)).strip() if m else ""


def page_description(source):
    m = re.search(r'<meta name="description" content="([^"]*)"', source)
    return html.unescape(m.group(1)).strip() if m else ""


def to_markdown(path):
    rel = path.relative_to(ROOT).as_posix()
    source = path.read_text()
    tree = Tree()
    tree.feed(source)
    out = []
    render(tree.root, rel, out)
    body = "\n\n".join(b for b in out if b.strip())
    body = re.sub(r"\n{3,}", "\n\n", body)

    desc = page_description(source)
    head = [
        f"<!-- generated from {rel} by admin/build/gen_markdown.py — do not edit by hand -->",
        f"*[open-source.sgit.ai](/index.md) · site {VERSION} · "
        f"canonical: https://{HOST}/{rel}*",
    ]
    if desc:
        head.append(f"> {desc}")
    return "\n\n".join(head) + "\n\n---\n\n" + body + "\n\n---\n\n*" + LICENCE + "*\n"


def html_pages():
    pages = []
    for p in sorted(ROOT.rglob("*.html")):
        if ".git" in p.parts:
            continue
        pages.append(p)
    rank = {name: i for i, name in enumerate(ORDER)}
    return sorted(pages, key=lambda p: (rank.get(p.relative_to(ROOT).as_posix(), 10_000),
                                        p.relative_to(ROOT).as_posix()))


def build_llms_txt(pages, twins):
    """llms.txt, written to be SELF-SUFFICIENT. The agent-access finding is that a
    link inside a fetched document does not count as having been seen, so a bare
    list of links is the failure mode. Each entry carries enough of the claim to be
    useful without following anything."""
    lines = [
        f"# open-source.sgit.ai",
        "",
        f"> Open source as a strategy rather than a charity: the position, the practice,",
        f"> and a history checked against its sources. Part of the sgit.ai network.",
        "",
        f"Site version: {VERSION}",
        f"Canonical host: https://{HOST}/",
        "Author: Dinis Cruz — https://www.linkedin.com/in/diniscruz — founder of The Cyber",
        "Boardroom, MyFeeds.ai and the sgit.ai network; former OWASP Board member.",
        "All content CC BY 4.0 unless noted. Code under the repository licence.",
        "",
        "## How to read this site as an agent",
        "",
        "Every page has a markdown twin at the same path with the extension swapped:",
        f"https://{HOST}/views/index.html is also https://{HOST}/views/index.md — and the",
        "links inside the markdown point at markdown, so you never have to parse HTML and",
        "never leave the markdown surface once you arrive.",
        "",
        f"If your fetcher cannot follow links at all, take https://{HOST}/llms-full.txt:",
        "it is every page on this site concatenated into a single file.",
        "",
        "## The thesis, stated so you do not have to fetch anything",
        "",
        '"the power of open source is not for the community, it is not because it is nice',
        'for others, and it is not to give back."',
        "",
        '"open source is not free, somebody is always paying for it. What you get from open',
        'source is freedom, that is different... We play the game of empowering the user and',
        'being the reputable source of trust. We are selling trust."',
        "",
        "The site's best original claim: survivability is not a property of the licence file,",
        "it is a property of the copyright and trademark structure. Every catalogued",
        "relicensing between 2018 and 2024 followed the same legal pattern — a single",
        "corporate copyright holder, having aggregated contributor copyright via a CLA,",
        "exercised the right to change terms going forward. Distributed-copyright projects",
        "could not be moved the same way, because no single party had standing.",
        "",
        "## Pages",
        "",
    ]
    for p in pages:
        rel = p.relative_to(ROOT).as_posix()
        source = p.read_text()
        title = page_title(source)
        desc = page_description(source)
        lines.append(f"- [{title}](https://{HOST}/{rel[:-len('html')] + 'md'}): {desc}")
    lines += [
        "",
        "## Source documents",
        "",
        "The briefs this site was built from are published verbatim under briefs/, and are",
        "the source of truth for anything the pages summarise. The commissioning brief pack",
        "is briefs/00__brief.md through briefs/09__source-manifest.csv.",
        "",
    ]
    return "\n".join(lines)


def build_llms_full(pages, twins):
    parts = [
        f"# open-source.sgit.ai — every page, one file",
        "",
        f"Site version: {VERSION}. Generated from the HTML by admin/build/gen_markdown.py.",
        f"Canonical host: https://{HOST}/ — every section below is one page of the site.",
        "This file exists so an agent that cannot follow links still gets the whole site.",
        "All content CC BY 4.0 unless noted.",
        "",
    ]
    for p in pages:
        rel = p.relative_to(ROOT).as_posix()
        parts.append("=" * 78)
        parts.append(f"PAGE: /{rel}  (markdown twin: /{rel[:-len('html')] + 'md'})")
        parts.append("=" * 78)
        parts.append("")
        parts.append(twins[rel])
        parts.append("")
    return "\n".join(parts)


def main():
    pages = html_pages()
    written = []
    twins = {}
    for p in pages:
        rel = p.relative_to(ROOT).as_posix()
        md = to_markdown(p)
        twins[rel] = md
        target = p.with_suffix(".md")
        if not target.exists() or target.read_text() != md:
            target.write_text(md)
            written.append(target.relative_to(ROOT).as_posix())

    for name, text in (("llms.txt", build_llms_txt(pages, twins)),
                       ("llms-full.txt", build_llms_full(pages, twins))):
        target = ROOT / name
        if not target.exists() or target.read_text() != text:
            target.write_text(text)
            written.append(name)

    print(f"gen_markdown: {len(pages)} page(s) -> twins + llms.txt + llms-full.txt; "
          f"{len(written)} file(s) updated")
    for w in written:
        print(f"  · {w}")


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        sys.stdout = None
