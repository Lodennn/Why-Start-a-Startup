#!/usr/bin/env python3
"""Builds a single-file, Notion-styled HTML edition of the book from book/chapters/*.md."""
import re
import html
import markdown
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = ROOT / "chapters"
OUT_HTML = Path(__file__).resolve().parent / "index.html"

# (filename stem, part label or None, emoji icon)
STRUCTURE = [
    ("00-preface", None, "👋"),
    ("01-why-start-a-startup", "Part One — Why and What: The Idea", "🚀"),
    ("02-anatomy-of-a-great-idea", "Part One — Why and What: The Idea", "💡"),
    ("03-monopoly-not-competition", "Part One — Why and What: The Idea", "👑"),
    ("04-choosing-a-cofounder", "Part Two — Who: Founders and Team", "🤝"),
    ("05-the-first-ten-hires", "Part Two — Who: Founders and Team", "🧑‍💼"),
    ("06-designing-company-culture", "Part Two — Who: Founders and Team", "🎨"),
    ("07-idea-to-mvp-talking-to-users", "Part Three — What: Building the Product", "🗣️"),
    ("08-building-products-users-love", "Part Three — What: Building the Product", "❤️"),
    ("09-doing-things-that-dont-scale", "Part Three — What: Building the Product", "🏃"),
    ("09b-interlude-hardware-in-a-software-world", "Part Three — What: Building the Product", "🔌"),
    ("10-retention-is-the-root-of-growth", "Part Four — Growth", "📈"),
    ("11-growth-channels-and-tactics", "Part Four — Growth", "🌱"),
    ("12-getting-press", "Part Four — Growth", "📰"),
    ("13-how-to-raise-money", "Part Five — Money", "💰"),
    ("14-pitching-and-fundraising-mechanics", "Part Five — Money", "🎤"),
    ("15-legal-and-financial-mechanics", "Part Five — Money", "⚖️"),
    ("16-selling-first-customer-to-enterprise-deal", "Part Five — Money", "🛒"),
    ("17-execution-focus-speed-momentum", "Part Six — Execution, Leadership, Scale", "⚡"),
    ("18-the-founders-mind-paradox-and-judgment", "Part Six — Execution, Leadership, Scale", "🧠"),
    ("19-how-to-operate", "Part Six — Execution, Leadership, Scale", "🛠️"),
    ("20-how-to-manage", "Part Six — Execution, Leadership, Scale", "👔"),
    ("21-scaling-the-company", "Part Six — Execution, Leadership, Scale", "🏗️"),
    ("22-epilogue-the-long-road", None, "🌅"),
    ("23-appendix-a-cap-table-walkthrough", "Appendices", "📊"),
    ("24-appendix-b-term-sheet-primer", "Appendices", "📄"),
    ("25-appendix-c-unit-economics-formulas", "Appendices", "🧮"),
    ("26-appendix-d-full-pitch-roleplay-transcript", "Appendices", "🎭"),
    ("27-glossary", "Back Matter", "📖"),
    ("28-bibliography", "Back Matter", "📚"),
    ("29-index", "Back Matter", "🔎"),
]

# heading text (lowercased, substring match) -> (emoji, css class)
SECTION_STYLES = [
    ("the core idea", "💡", "callout-blue"),
    ("why it's true", "🔍", "callout-teal"),
    ("common mistakes", "⚠️", "callout-red"),
    ("tradeoffs and edge cases", "⚖️", "callout-purple"),
    ("applying the test", "🧪", "callout-green"),
    ("chapter summary", "✅", "callout-yellow"),
    ("exercises", "📝", "callout-pink"),
    ("further reading", "📚", "callout-gray"),
]

MD = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc", "attr_list"])


def slugify(text):
    return re.sub(r"[^a-z0-9-]", "", re.sub(r"\s+", "-", text.strip().lower()))


def style_for_heading(text):
    low = text.lower()
    for key, emoji, css in SECTION_STYLES:
        if key in low:
            return emoji, css
    return None, None


def wrap_sections(body_html, chapter_slug):
    """Split an H2-delimited chapter body into styled callout <section>s."""
    parts = re.split(r"(<h2[^>]*>.*?</h2>)", body_html, flags=re.DOTALL)
    if len(parts) == 1:
        return body_html

    out = [parts[0]]  # cold open, before first h2
    i = 1
    while i < len(parts):
        heading_html = parts[i]
        content_html = parts[i + 1] if i + 1 < len(parts) else ""
        text = re.sub(r"<[^>]+>", "", heading_html).strip()
        emoji, css = style_for_heading(text)
        anchor = f'{chapter_slug}-{slugify(text)}'
        if css:
            clean_heading = re.sub(r"^<h2[^>]*>", f'<h2 id="{anchor}"><span class="h2-emoji">{emoji}</span> ', heading_html)
            out.append(f'<section class="callout {css}">{clean_heading}{content_html}</section>')
        else:
            clean_heading = re.sub(r"^<h2[^>]*>", f'<h2 id="{anchor}">', heading_html)
            out.append(f"{clean_heading}{content_html}")
        i += 2
    return "".join(out)


def load_chapter(stem):
    text = (CHAPTERS_DIR / f"{stem}.md").read_text()
    MD.reset()
    body = MD.convert(text)
    # Pull the H1 title out for the sidebar / header, then remove it from the body
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.DOTALL)
    title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else stem
    body_wo_h1 = re.sub(r"<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.DOTALL)
    return title, body_wo_h1


def build():
    chapters = []
    for stem, part, emoji in STRUCTURE:
        title, body = load_chapter(stem)
        slug = stem
        body = wrap_sections(body, slug)
        chapters.append({"slug": slug, "part": part, "emoji": emoji, "title": title, "body": body})

    # Sidebar, grouped by part (None = ungrouped top-level entry, e.g. Preface/Epilogue)
    sidebar_html = []
    current_part = "__unset__"
    for ch in chapters:
        if ch["part"] != current_part:
            if ch["part"] is not None:
                sidebar_html.append(f'<div class="sidebar-part">{html.escape(ch["part"])}</div>')
            current_part = ch["part"]
        indent_cls = "sidebar-link" if ch["part"] else "sidebar-link sidebar-link-top"
        sidebar_html.append(
            f'<a class="{indent_cls}" href="#{ch["slug"]}" data-target="{ch["slug"]}" title="{html.escape(ch["title"])}">'
            f'<span class="sidebar-emoji">{ch["emoji"]}</span>'
            f'<span class="sidebar-label">{html.escape(ch["title"])}</span></a>'
        )
    sidebar = "\n".join(sidebar_html)

    # Main content
    sections_html = []
    for ch in chapters:
        sections_html.append(
            f'<article class="chapter" id="{ch["slug"]}">'
            f'<div class="chapter-icon">{ch["emoji"]}</div>'
            f'<h1 class="chapter-title">{html.escape(ch["title"])}</h1>'
            f'{ch["body"]}'
            f"</article>"
        )
    content = "\n".join(sections_html)

    page = TEMPLATE.replace("{{SIDEBAR}}", sidebar).replace("{{CONTENT}}", content)
    OUT_HTML.write_text(page)
    print(f"Wrote {OUT_HTML} ({len(page):,} bytes, {len(chapters)} chapters)")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>How to Start a Startup — The Book</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root{
  --bg:#ffffff; --text:#37352f; --muted:#787774; --sidebar-bg:#fbfaf9; --border:#e9e5e0;
  --blue-bg:#e7f3f8; --blue-text:#1a5c7a; --blue-border:#8ec6de;
  --teal-bg:#e6f4f1; --teal-text:#0f6d5c; --teal-border:#7ecdb8;
  --red-bg:#fdecec; --red-text:#a3342a; --red-border:#e8a6a0;
  --purple-bg:#f3effa; --purple-text:#5b3c94; --purple-border:#c4aeeb;
  --green-bg:#edf6ec; --green-text:#2f7a3a; --green-border:#a9d8a5;
  --yellow-bg:#fdf6e3; --yellow-text:#93720b; --yellow-border:#efd888;
  --pink-bg:#fbebf1; --pink-text:#a3306e; --pink-border:#eeb0cd;
  --gray-bg:#f1f1ef; --gray-text:#5c5b57; --gray-border:#d3d1cb;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  margin:0; display:flex; min-height:100vh;
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  color:var(--text); background:var(--bg); line-height:1.65;
}
/* Sidebar */
nav.sidebar{
  width:300px; flex-shrink:0; background:var(--sidebar-bg); border-right:1px solid var(--border);
  padding:24px 10px; position:sticky; top:0; height:100vh; overflow-y:auto;
}
.sidebar-title{font-weight:700; font-size:15px; padding:4px 10px 16px; color:var(--text);}
.sidebar-part{
  font-size:11px; text-transform:uppercase; letter-spacing:.06em; color:var(--muted);
  margin:18px 10px 6px; font-weight:600;
}
.sidebar-link{
  display:flex; align-items:center; gap:8px; padding:6px 10px; border-radius:6px;
  color:var(--text); text-decoration:none; font-size:13px; min-width:0;
}
.sidebar-link:hover{background:#efece7;}
.sidebar-link.active{background:#e3e1dc; font-weight:600;}
.sidebar-link-top{font-weight:600;}
.sidebar-emoji{font-size:15px; flex:none;}
.sidebar-label{overflow:hidden; text-overflow:ellipsis; white-space:nowrap; min-width:0;}
/* Main content */
main{flex:1; min-width:0; padding:56px 48px 120px; max-width:840px; margin:0 auto;}
.chapter{padding-bottom:64px; margin-bottom:64px; border-bottom:1px dashed var(--border);}
.chapter:last-child{border-bottom:none;}
.chapter-icon{font-size:64px; line-height:1; margin-bottom:8px;}
.chapter-title{font-size:2.1em; font-weight:800; margin:0 0 28px; letter-spacing:-.01em;}
h2{font-size:1.5em; font-weight:750; margin:0 0 14px; display:flex; align-items:center; gap:8px;}
h3{font-size:1.15em; font-weight:700; margin:28px 0 10px; color:#1a5c7a; border-left:3px solid var(--blue-border); padding-left:10px;}
p{margin:0 0 16px;}
strong{color:#2b2926; font-weight:700;}
a{color:#0b6e99;}
ul,ol{padding-left:1.4em; margin:0 0 16px;}
li{margin-bottom:6px;}
li::marker{color:#c48d3a;}
blockquote{
  margin:20px 0; padding:14px 18px; background:#f7f6f3; border-left:4px solid #d9a441;
  border-radius:4px; font-style:italic; color:#4b4a45;
}
blockquote p:last-child{margin-bottom:0;}
code{
  background:#f1f1ef; color:#af5252; padding:2px 6px; border-radius:4px;
  font-family:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace; font-size:.9em;
}
pre{
  background:#2f3437; color:#e3e2e0; padding:18px 20px; border-radius:8px; overflow-x:auto;
  font-family:"SFMono-Regular",Consolas,"Liberation Mono",Menlo,monospace; font-size:.85em;
  line-height:1.5; margin:20px 0;
}
pre code{background:none; color:inherit; padding:0;}
table{border-collapse:collapse; width:100%; margin:20px 0; font-size:.95em;}
th,td{border:1px solid var(--border); padding:8px 12px; text-align:left;}
th{background:#f7f6f3; font-weight:700;}
tr:nth-child(even) td{background:#fbfaf9;}
hr{border:none; border-top:1px solid var(--border); margin:32px 0;}
/* Callout sections */
.callout{
  border-radius:10px; padding:20px 24px 22px; margin:24px 0 32px; border:1px solid transparent;
}
.callout h2{margin-top:0;}
.h2-emoji{font-size:1.1em;}
.callout-blue{background:var(--blue-bg); border-color:var(--blue-border);} .callout-blue h2{color:var(--blue-text);}
.callout-teal{background:var(--teal-bg); border-color:var(--teal-border);} .callout-teal h2{color:var(--teal-text);}
.callout-red{background:var(--red-bg); border-color:var(--red-border);} .callout-red h2{color:var(--red-text);}
.callout-purple{background:var(--purple-bg); border-color:var(--purple-border);} .callout-purple h2{color:var(--purple-text);}
.callout-green{background:var(--green-bg); border-color:var(--green-border);} .callout-green h2{color:var(--green-text);}
.callout-yellow{background:var(--yellow-bg); border-color:var(--yellow-border);} .callout-yellow h2{color:var(--yellow-text);}
.callout-pink{background:var(--pink-bg); border-color:var(--pink-border);} .callout-pink h2{color:var(--pink-text);}
.callout-gray{background:var(--gray-bg); border-color:var(--gray-border);} .callout-gray h2{color:var(--gray-text);}
.callout pre{background:#20242a;}
.callout table th{background:rgba(255,255,255,.6);}
.callout table tr:nth-child(even) td{background:rgba(255,255,255,.4);}
@media (max-width:900px){
  body{flex-direction:column;}
  nav.sidebar{width:100%; height:auto; position:relative; border-right:none; border-bottom:1px solid var(--border);}
  main{padding:32px 20px 80px;}
}
@media print{
  nav.sidebar{display:none;}
  body{display:block;}
  main{max-width:none; padding:0;}
  .chapter{page-break-before:always; border-bottom:none;}
  .chapter:first-child{page-break-before:avoid;}
  * { -webkit-print-color-adjust:exact !important; print-color-adjust:exact !important; }
}
</style>
</head>
<body>
<nav class="sidebar">
  <div class="sidebar-title">📘 How to Start a Startup</div>
  {{SIDEBAR}}
</nav>
<main>
{{CONTENT}}
</main>
<script>
  const links = document.querySelectorAll('.sidebar-link');
  const sections = Array.from(document.querySelectorAll('.chapter'));
  const setActive = (slug) => {
    links.forEach(l => l.classList.toggle('active', l.dataset.target === slug));
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) setActive(e.target.id); });
  }, { rootMargin: '-10% 0px -80% 0px' });
  sections.forEach(s => io.observe(s));
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
