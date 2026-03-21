#!/usr/bin/env python3
"""Fix formatting issues in scraped LinkedIn content."""

import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "content" / "blog"


def fix_stuck_words(text):
    """Fix words stuck together from LinkedIn HTML parsing."""
    # Pattern: lowercase letter immediately followed by uppercase (camelCase-like joins)
    # e.g. "Groupfiled" → "Group filed", "againstAnthropicover" → "against Anthropic over"
    # Be careful not to break intentional camelCase like "ChatGPT", "AlphaGenome"

    known_fixes = {
        "Groupfiled": "Group filed",
        "againstAnthropicover": "against Anthropic over",
        "isActive Engagement": "is Active Engagement",
        "isPassive Acceptance": "is Passive Acceptance",
        "ofthinkingwith": "of thinking with",
        "ofgenerating": "of generating",
        "1.Indemnification Audit-": "1. **Indemnification Audit** —",
        "2.Zero Trust for AI-": "2. **Zero Trust for AI** —",
        "3.Institutional Memory Layer-": "3. **Institutional Memory Layer** —",
        "4.Agent Control Plane-": "4. **Agent Control Plane** —",
    }
    for old, new in known_fixes.items():
        text = text.replace(old, new)

    return text


def fix_missing_headings(text):
    """Convert numbered section titles that should be headings."""
    # Pattern: line starting with "N. Title" that isn't already a heading or list item
    # These are subheadings from LinkedIn articles that got parsed as plain text
    lines = text.split('\n')
    fixed_lines = []

    for line in lines:
        stripped = line.strip()
        # Match patterns like "4. Microsoft's Custom Silicon: Maia 200"
        # but NOT "1. Some action item text that continues..."
        heading_match = re.match(r'^(\d+)\.\s+([A-Z][^.]{10,80})$', stripped)
        if heading_match and not stripped.startswith('###'):
            num = heading_match.group(1)
            title = heading_match.group(2)
            # Only convert if it looks like a section heading (short, title-case-ish)
            word_count = len(title.split())
            if word_count <= 12:
                fixed_lines.append(f'### {num}. {title}')
                continue

        # Also fix "- Microsoft's Custom Silicon: Maia 200" list items that should be headings
        li_heading = re.match(r'^- ([A-Z][^.]{10,80})$', stripped)
        if li_heading:
            title = li_heading.group(1)
            if len(title.split()) <= 12 and ':' in title:
                fixed_lines.append(f'### {title}')
                continue

        fixed_lines.append(line)

    return '\n'.join(fixed_lines)


def fix_numbered_lists(text):
    """Fix numbered lists with stuck formatting like '1.Item- Description'."""
    # Fix "N.Title- description" → "N. **Title** — description"
    text = re.sub(
        r'^(\d+)\.(\w)',
        lambda m: f'{m.group(1)}. {m.group(2)}',
        text,
        flags=re.MULTILINE
    )
    return text


def fix_post(filepath):
    """Fix formatting in a single blog post."""
    content = filepath.read_text()

    # Split front matter and body
    fm_match = re.match(r'^(---\n.*?\n---)\n(.*)$', content, re.DOTALL)
    if not fm_match:
        return False, "No front matter"

    front_matter = fm_match.group(1)
    body = fm_match.group(2)
    original_body = body

    # Apply fixes
    body = fix_stuck_words(body)
    body = fix_missing_headings(body)
    body = fix_numbered_lists(body)

    if body == original_body:
        return False, "No changes needed"

    filepath.write_text(f"{front_matter}\n{body}")

    # Count changes
    changes = sum(1 for a, b in zip(original_body.split('\n'), body.split('\n')) if a != b)
    return True, f"{changes} lines fixed"


def main():
    print("Fixing formatting in blog posts...\n")

    fixed = 0
    for md in sorted(BLOG_DIR.glob("*.md")):
        if md.name == "_index.md":
            continue

        ok, msg = fix_post(md)
        if ok:
            print(f"  ✅ {md.stem}: {msg}")
            fixed += 1

    print(f"\nFixed {fixed} posts")


if __name__ == "__main__":
    main()
