#!/usr/bin/env python3
"""Update Hugo blog posts with scraped LinkedIn content."""

import re
import shutil
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "content" / "blog"
SCRAPED_DIR = Path(__file__).parent.parent / "scraped_content"
IMAGES_SRC = SCRAPED_DIR / "images"
IMAGES_DST = Path(__file__).parent.parent / "static" / "images" / "blog"


def clean_feed_post(text):
    """Clean feed post content: remove hashtags, fix formatting."""
    # Remove trailing hashtag block (e.g. "#Engineering... | 242 comments on LinkedIn")
    text = re.sub(r'\n\n#\w+.*$', '', text, flags=re.DOTALL)
    # Remove "| N comments on LinkedIn" suffix
    text = re.sub(r'\s*\|\s*\d+\s*comments?\s*on\s*LinkedIn\s*$', '', text)
    # Remove leading duplicate of the title (first line often repeats)
    lines = text.strip().split('\n')
    return '\n'.join(lines).strip()


def clean_pulse_article(text):
    """Clean Pulse article content: remove LinkedIn noise, fix formatting."""
    # Remove "### Marcin Kucharski" byline
    text = re.sub(r'###\s*Marcin Kucharski\s*\n', '', text)
    # Remove "## Recommended by LinkedIn" section
    text = re.sub(r'\n+##\s*Recommended by LinkedIn\s*\n+', '\n\n', text)
    # Fix stuck-together words from LinkedIn HTML parsing
    stuck_patterns = [
        (r'isActive Engagement', 'is Active Engagement'),
        (r'isPassive Acceptance', 'is Passive Acceptance'),
        (r'ofthinkingwith', 'of thinking with'),
        (r'ofgenerating', 'of generating'),
    ]
    for pattern, replacement in stuck_patterns:
        text = text.replace(pattern, replacement)
    # Remove leading/trailing whitespace from paragraphs
    paragraphs = text.split('\n\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]
    return '\n\n'.join(paragraphs)


def get_image_for_post(slug):
    """Find the OG image for a post."""
    img_path = IMAGES_SRC / f"{slug}_og_image_0.png"
    if img_path.exists():
        return img_path
    return None


def update_post(slug):
    """Update a single Hugo blog post with scraped content."""
    blog_file = BLOG_DIR / f"{slug}.md"
    scraped_file = SCRAPED_DIR / f"{slug}.md"

    if not blog_file.exists() or not scraped_file.exists():
        return False, "File not found"

    # Read original front matter
    original = blog_file.read_text()
    fm_match = re.match(r'^---\n(.*?)\n---\n', original, re.DOTALL)
    if not fm_match:
        return False, "No front matter"

    front_matter = fm_match.group(1)

    # Read scraped content
    scraped = scraped_file.read_text()
    scraped_fm = re.match(r'^---\n(.*?)\n---\n', scraped, re.DOTALL)
    if not scraped_fm:
        return False, "No scraped front matter"

    scraped_type = "feed"
    for line in scraped_fm.group(1).split('\n'):
        if line.startswith('type:'):
            scraped_type = line.split(':')[1].strip()

    # Extract body content (after front matter)
    body = scraped[scraped_fm.end():].strip()

    # Clean content based on type
    if scraped_type == "pulse":
        body = clean_pulse_article(body)
    else:
        body = clean_feed_post(body)

    # Remove first line if it duplicates the title
    title_match = re.search(r'title:\s*"([^"]+)"', front_matter)
    if title_match:
        title = title_match.group(1)
        first_line = body.split('\n')[0].strip()
        # Check if first line is similar to title (ignoring case/punctuation)
        title_clean = re.sub(r'[^a-zA-Z0-9\s]', '', title.lower())
        first_clean = re.sub(r'[^a-zA-Z0-9\s]', '', first_line.lower())
        if title_clean and first_clean and (
            title_clean in first_clean or first_clean in title_clean
            or title_clean[:50] == first_clean[:50]
        ):
            body = '\n'.join(body.split('\n')[1:]).strip()

    # Copy image to Hugo static dir
    img_path = get_image_for_post(slug)
    if img_path:
        IMAGES_DST.mkdir(parents=True, exist_ok=True)
        dst = IMAGES_DST / f"{slug}.png"
        shutil.copy2(img_path, dst)
        # Add image to front matter if not present
        if 'image:' not in front_matter:
            front_matter += f'\nimage: "/images/blog/{slug}.png"'

    # Remove linkedin redirect line from front matter (keep linkedin URL for reference)
    # Build updated file
    updated = f"---\n{front_matter}\n---\n\n{body}\n"

    blog_file.write_text(updated)
    return True, f"{len(body)} chars"


def main():
    IMAGES_DST.mkdir(parents=True, exist_ok=True)

    posts = sorted([f.stem for f in SCRAPED_DIR.glob("*.md") if f.stem != "scrape_summary"])
    print(f"Updating {len(posts)} blog posts...\n")

    success = 0
    for slug in posts:
        ok, msg = update_post(slug)
        status = "✅" if ok else "❌"
        print(f"  {status} {slug}: {msg}")
        if ok:
            success += 1

    print(f"\nDone: {success}/{len(posts)} updated")
    print(f"Images copied to: {IMAGES_DST}")


if __name__ == "__main__":
    main()
