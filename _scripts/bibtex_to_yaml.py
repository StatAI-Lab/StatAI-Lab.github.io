#!/usr/bin/env python3
"""
Convert BibTeX files to Jekyll citations.yaml format.
PDF and BibTeX are paired by filename (without extension).
"""

import os
import re

BIB_DIR = "/mnt/d/Git_repo/StatAI-Lab.github.io/assets/bibtex"
PDF_DIR = "/mnt/d/Git_repo/StatAI-Lab.github.io/assets/publications"
OUTPUT_FILE = "/mnt/d/Git_repo/StatAI-Lab.github.io/_data/citations.yaml"


def parse_bibtex(filepath, pdf_base=""):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    entry_type = re.search(r'@(\w+)\{', content, re.IGNORECASE)
    entry_type = entry_type.group(1).lower() if entry_type else ""

    def get(field):
        # Try double-quoted style: field = "..."
        m = re.search(rf'\b{field}\s*=\s*"([^"]*)"', content, re.IGNORECASE)
        if not m:
            # Try brace style: field = {...}
            m = re.search(rf'\b{field}\s*=\s*\{{([^}}]*)\}}', content, re.IGNORECASE)
        return m.group(1).strip() if m else ""

    def get_year():
        m = re.search(r'\byear\s*=\s*["\{]?(\d{4})["\}]?', content, re.IGNORECASE)
        return m.group(1) if m else ""

    title = get("title")
    # Strip outer braces if title is like "{...}"
    title = re.sub(r'^\{([^}]+)\}$', r'\1', title)

    authors_str = get("author")
    authors = []
    for part in re.split(r'\s+and\s+', authors_str, flags=re.IGNORECASE):
        part = part.strip().strip('{}')
        # Handle "Last, First" format
        if ',' in part:
            last, first = part.rsplit(',', 1)
            authors.append(f"{first.strip()} {last.strip()}")
        else:
            authors.append(part.strip())

    year = get_year()

    publisher = get("publisher") or get("journal") or get("booktitle") or ""

    month_str = get("month")
    day_str = get("day") or "01"
    date_str = f"{year}-01-01"
    if month_str:
        month_map = {
            'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04',
            'may': '05', 'jun': '06', 'jul': '07', 'aug': '08',
            'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'
        }
        m = re.search(r'\d+', month_str)
        if m:
            date_str = f"{year}-{month_map.get(m.group().lower()[:3], '01')}-{day_str.zfill(2)}"
        else:
            m2 = re.search(r'(\d{1,2})', month_str)
            if m2:
                date_str = f"{year}-{int(m2.group(1)):02d}-{day_str.zfill(2)}"

    doi_raw = get("doi")
    doi = doi_raw
    if doi and not doi.startswith("http"):
        doi = f"https://doi.org/{doi_raw}"
    link = get("url")
    if link.startswith("10."):
        link = f"https://doi.org/{link}"

    if doi and not link:
        link = doi

    pdf_link = link if link else ""

    buttons = [{"type": "pdf", "text": "PDF", "link": pdf_link}]

    if doi:
        bib_id = f"doi:{doi.split('/')[-1]}" if doi.startswith("http") else f"doi:{doi}"
    else:
        bib_id = f"{entry_type}:{year}"

    return {
        "id": bib_id,
        "title": title,
        "authors": authors,
        "publisher": publisher,
        "date": date_str,
        "link": link,
        "type": "paper",
        "buttons": buttons
    }


def main():
    pdfs = sorted(os.listdir(PDF_DIR))

    lines = []
    lines.append("# ================================================")
    lines.append("# StatAI Lab 论文列表")
    lines.append("# ================================================")
    lines.append("# 自动从 BibTeX 转换生成，PDF 与 BibTeX 按文件名一一对应")
    lines.append("#")
    lines.append("# 每篇论文格式：")
    lines.append("# - id:        唯一标识（用 DOI，如 doi:10.xxxx/xxxxx）")
    lines.append("#   title:     论文标题")
    lines.append("#   authors:   作者列表")
    lines.append("#   publisher: 发表期刊/会议")
    lines.append("#   date:      发表日期，格式 YYYY-MM-DD")
    lines.append("#   link:      论文链接")
    lines.append("#   type:      paper")
    lines.append("# ================================================")
    lines.append("")
    lines.append("# 论文列表")
    lines.append("")

    for pdf_name in pdfs:
        base = os.path.splitext(pdf_name)[0]
        bib_name = base + ".bib"
        bib_path = os.path.join(BIB_DIR, bib_name)

        if not os.path.exists(bib_path):
            print(f"SKIP (no bib): {pdf_name}")
            continue

        c = parse_bibtex(bib_path)

        lines.append(f"- id: {c['id']}")
        lines.append(f"  title: \"{c['title']}\"")
        lines.append("  authors:")
        for a in c['authors']:
            lines.append(f"    - {a}")
        lines.append(f"  publisher: {c['publisher']}")
        lines.append(f"  date: '{c['date']}'")
        if c['link']:
            lines.append(f"  link: {c['link']}")
        lines.append(f"  type: {c['type']}")
        if c['buttons']:
            lines.append("  buttons:")
            for b in c['buttons']:
                lines.append(f"    - type: {b['type']}")
                lines.append(f"      text: {b['text']}")
                lines.append(f"      link: {b['link']}")
        lines.append("")

        print(f"OK: {pdf_name} -> {c['title'][:70]}")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    print(f"\nDone. Written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()