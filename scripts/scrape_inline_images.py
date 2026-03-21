#!/usr/bin/env python3
"""Scrape inline images from LinkedIn Pulse articles and update blog posts."""

import os
import re
import time
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

BLOG_DIR = Path(__file__).parent.parent / "content" / "blog"
IMAGES_DIR = Path(__file__).parent.parent / "static" / "images" / "blog"

# Pulse articles only (feed posts don't have inline images)
PULSE_POSTS = {
    "ai-standards": "https://www.linkedin.com/pulse/week-ai-got-standards-marcin-kucharski-x4zyf",
    "ai-weekly-2": "https://www.linkedin.com/pulse/ai-adoption-paradox-88-deployed-only-6-ready-marcin-kucharski-l6gkf",
    "ai-weekly-4": "https://www.linkedin.com/pulse/why-your-2026-ai-roadmap-just-hit-physical-wall-marcin-kucharski-93uxf",
    "ai-weekly-7": "https://www.linkedin.com/pulse/when-investment-velocity-meets-governance-collapse-marcin-kucharski-e6n0f",
    "doomprompting": "https://www.linkedin.com/pulse/doomprompting-how-i-traded-one-addiction-another-marcin-kucharski-b8qaf",
    "multi-provider-era": "https://www.linkedin.com/pulse/multi-provider-ai-era-just-started-most-ctos-arent-ready-kucharski-widwf",
    "newsletter-5": "https://www.linkedin.com/pulse/10-billion-infrastructure-boom-meets-95-roi-failure-marcin-kucharski-sipuf",
    "newsletter-6": "https://www.linkedin.com/pulse/85-problem-enterprise-ai-stuck-between-ambition-marcin-kucharski-rzxkf",
}


def fetch_page(url):
    """Fetch a LinkedIn page."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def download_image(url, save_path):
    """Download an image."""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            save_path.write_bytes(resp.read())
            return True
    except Exception as e:
        print(f"    ⚠️  Download failed: {e}")
        return False


def extract_article_with_images(html, slug):
    """Extract article content preserving image positions."""
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article")
    if not article:
        return None, []

    # Walk through article elements in order
    content_parts = []
    images_downloaded = []
    img_counter = 0

    # Get the main content container - usually after the cover image and author info
    # We process all direct children and nested elements
    for el in article.descendants:
        if el.name == "img":
            src = el.get("src", el.get("data-src", el.get("data-delayed-url", "")))
            cls = " ".join(el.get("class", []))

            # Skip profile pics, icons, cover image (already handled as featured)
            if "profile" in src or "logo" in src:
                continue
            if "cover_image" in src:
                continue
            if "rounded-[50%]" in cls or "w-6" in cls:
                continue

            # This is an inline content image
            if "article-inline_image" in src:
                img_counter += 1
                ext = "jpg" if "jpeg" in src.lower() else "png"
                filename = f"{slug}_inline_{img_counter}.{ext}"
                local_path = IMAGES_DIR / filename

                if download_image(src, local_path):
                    images_downloaded.append(filename)
                    content_parts.append(f"\n\n![](/images/blog/{filename})\n\n")
                    print(f"    📷 Inline image {img_counter}: {filename}")

        elif el.name in ("p", "h2", "h3", "h4", "blockquote", "li"):
            text = el.get_text(strip=True)
            if not text or len(text) < 3:
                continue

            # Skip noise
            if any(skip in text.lower() for skip in [
                "report this", "sign in", "cookie", "join now",
                "published", "followers", "recommended by linkedin"
            ]):
                continue

            # Skip if this element is inside another element we'll process
            # (avoid double-counting)
            parent = el.parent
            if parent and parent.name in ("p", "h2", "h3", "h4", "blockquote", "li"):
                continue

            if el.name.startswith("h"):
                level = int(el.name[1])
                content_parts.append(f"\n{'#' * level} {text}\n")
            elif el.name == "li":
                content_parts.append(f"- {text}")
            elif el.name == "blockquote":
                content_parts.append(f"> {text}")
            else:
                content_parts.append(text)

    return content_parts, images_downloaded


def clean_content(parts, slug):
    """Clean and join content parts."""
    text = "\n\n".join(parts)

    # Remove author byline
    text = re.sub(r'###?\s*Marcin Kucharski\s*\n', '', text)
    # Fix stuck words
    stuck = [
        ("isActive Engagement", "is Active Engagement"),
        ("isPassive Acceptance", "is Passive Acceptance"),
        ("ofthinkingwith", "of thinking with"),
        ("ofgenerating", "of generating"),
    ]
    for pattern, replacement in stuck:
        text = text.replace(pattern, replacement)

    # Clean multiple blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def update_blog_post(slug, new_content):
    """Update the Hugo blog post with new content including inline images."""
    blog_file = BLOG_DIR / f"{slug}.md"
    if not blog_file.exists():
        return False

    original = blog_file.read_text()
    fm_match = re.match(r'^(---\n.*?\n---)\n', original, re.DOTALL)
    if not fm_match:
        return False

    front_matter = fm_match.group(1)
    updated = f"{front_matter}\n\n{new_content}\n"
    blog_file.write_text(updated)
    return True


def main():
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Processing {len(PULSE_POSTS)} Pulse articles for inline images...\n")

    for slug, url in sorted(PULSE_POSTS.items()):
        print(f"📄 {slug}")
        print(f"   {url}")

        try:
            html = fetch_page(url)
            time.sleep(2)

            parts, images = extract_article_with_images(html, slug)
            if parts is None:
                print("   ❌ No article found")
                continue

            content = clean_content(parts, slug)
            char_count = len(content)
            print(f"   ✅ Content: {char_count} chars, {len(images)} inline images")

            if update_blog_post(slug, content):
                print(f"   📝 Blog post updated")
            else:
                print(f"   ⚠️  Could not update blog post")

        except Exception as e:
            print(f"   ❌ Error: {e}")

        print()

    # Summary
    inline_imgs = list(IMAGES_DIR.glob("*_inline_*.png")) + list(IMAGES_DIR.glob("*_inline_*.jpg"))
    print(f"{'='*50}")
    print(f"DONE: {len(inline_imgs)} inline images downloaded")
    print(f"Location: {IMAGES_DIR}")


if __name__ == "__main__":
    main()
