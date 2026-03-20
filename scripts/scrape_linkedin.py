#!/usr/bin/env python3
"""Scrape LinkedIn posts and articles for kucharski.ai blog content."""

import json
import os
import re
import time
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

BLOG_DIR = Path(__file__).parent.parent / "content" / "blog"
OUTPUT_DIR = Path(__file__).parent.parent / "scraped_content"
IMAGES_DIR = OUTPUT_DIR / "images"


def get_posts():
    """Read all blog posts and extract LinkedIn URLs."""
    posts = []
    for md_file in sorted(BLOG_DIR.glob("*.md")):
        if md_file.name == "_index.md":
            continue
        content = md_file.read_text()
        linkedin_match = re.search(r'linkedin:\s*"([^"]+)"', content)
        title_match = re.search(r'title:\s*"([^"]+)"', content)
        date_match = re.search(r'date:\s*(\S+)', content)
        tags_match = re.search(r'tags:\s*\[([^\]]+)\]', content)

        if linkedin_match:
            url = linkedin_match.group(1)
            post_type = "pulse" if "/pulse/" in url else "feed"
            posts.append({
                "slug": md_file.stem,
                "file": str(md_file),
                "title": title_match.group(1) if title_match else md_file.stem,
                "date": date_match.group(1) if date_match else "unknown",
                "tags": tags_match.group(1) if tags_match else "",
                "linkedin_url": url,
                "type": post_type,
            })
    return posts


def fetch_page(url):
    """Fetch a LinkedIn page with proper headers."""
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def extract_pulse_article(html):
    """Extract content from a LinkedIn Pulse/Newsletter article."""
    soup = BeautifulSoup(html, "html.parser")

    # Get title
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(strip=True)

    # Get article paragraphs
    article = soup.find("article")
    paragraphs = []
    if article:
        for el in article.find_all(["p", "h2", "h3", "h4", "li", "blockquote"]):
            text = el.get_text(strip=True)
            if not text or len(text) < 3:
                continue
            # Skip non-content elements
            if any(skip in text.lower() for skip in [
                "report this", "sign in", "cookie", "join now",
                "published", "followers", "like", "comment"
            ]):
                continue
            if el.name.startswith("h"):
                level = int(el.name[1])
                paragraphs.append(f"\n{'#' * level} {text}\n")
            elif el.name == "li":
                paragraphs.append(f"- {text}")
            elif el.name == "blockquote":
                paragraphs.append(f"> {text}")
            else:
                paragraphs.append(text)

    # Get images
    images = extract_images(soup)

    return {
        "title": title,
        "content": "\n\n".join(paragraphs),
        "images": images,
    }


def extract_feed_post(html):
    """Extract content from a LinkedIn feed post."""
    soup = BeautifulSoup(html, "html.parser")

    # Method 1: Get from meta description (usually truncated)
    desc = soup.find("meta", {"name": "description"})
    meta_text = desc.get("content", "") if desc else ""

    # Method 2: Get from the main post paragraph
    # LinkedIn feed posts put full content in a <p> tag with data-test-id or specific class
    full_text = ""
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > len(full_text) and len(text) > 200:
            # Filter out comments and other noise
            if not any(skip in text.lower() for skip in [
                "cookie", "sign in", "join now", "report this"
            ]):
                full_text = text

    # Method 3: JSON-LD
    for script in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(script.string)
            if isinstance(data, dict):
                article_body = data.get("articleBody", "")
                if len(article_body) > len(full_text):
                    full_text = article_body
        except (json.JSONDecodeError, TypeError):
            pass

    # Use the longest version
    content = full_text if len(full_text) > len(meta_text) else meta_text

    # Format: add paragraph breaks at logical points
    # LinkedIn posts use double newlines for paragraphs
    content = content.replace("\n\n", "\n\n")

    images = extract_images(soup)

    return {
        "title": "",  # Feed posts use the blog's existing title
        "content": content,
        "images": images,
    }


def extract_images(soup):
    """Extract image URLs from LinkedIn page."""
    images = []

    # OG image (main post image)
    og_img = soup.find("meta", {"property": "og:image"})
    if og_img and og_img.get("content"):
        images.append({
            "url": og_img["content"],
            "type": "og_image",
        })

    # Article images
    article = soup.find("article")
    if article:
        for img in article.find_all("img"):
            src = img.get("src", img.get("data-src", ""))
            if src and "licdn.com" in src and "profile" not in src:
                images.append({
                    "url": src,
                    "type": "article_image",
                })

    return images


def download_image(url, save_path):
    """Download an image from URL."""
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
            save_path.write_bytes(data)
            return True
    except Exception as e:
        print(f"  ⚠️  Failed to download image: {e}")
        return False


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    posts = get_posts()
    print(f"Found {len(posts)} posts to scrape")
    print(f"  Pulse articles: {sum(1 for p in posts if p['type'] == 'pulse')}")
    print(f"  Feed posts: {sum(1 for p in posts if p['type'] == 'feed')}")
    print()

    results = []

    for i, post in enumerate(posts, 1):
        print(f"[{i}/{len(posts)}] {post['slug']} ({post['type']})")
        print(f"  URL: {post['linkedin_url']}")

        try:
            html = fetch_page(post["linkedin_url"])
            time.sleep(2)  # Rate limiting

            if post["type"] == "pulse":
                extracted = extract_pulse_article(html)
            else:
                extracted = extract_feed_post(html)

            content_len = len(extracted["content"])
            print(f"  ✅ Content: {content_len} chars, {len(extracted['images'])} images")

            # Download images
            for j, img in enumerate(extracted["images"]):
                ext = "jpg" if "jpeg" in img["url"].lower() or "jpg" in img["url"].lower() else "png"
                img_filename = f"{post['slug']}_{img['type']}_{j}.{ext}"
                img_path = IMAGES_DIR / img_filename
                if download_image(img["url"], img_path):
                    img["local_path"] = str(img_path)
                    print(f"  📷 Saved: {img_filename}")

            # Save extracted content
            result = {**post, **extracted}
            results.append(result)

            # Save individual markdown file
            md_path = OUTPUT_DIR / f"{post['slug']}.md"
            md_content = f"""---
title: "{post['title']}"
date: {post['date']}
tags: [{post['tags']}]
linkedin: "{post['linkedin_url']}"
type: {post['type']}
scraped_chars: {content_len}
---

{extracted['content']}
"""
            md_path.write_text(md_content)

        except Exception as e:
            print(f"  ❌ Error: {e}")
            results.append({**post, "content": "", "images": [], "error": str(e)})

    # Save summary
    summary_path = OUTPUT_DIR / "scrape_summary.json"
    summary = {
        "total": len(results),
        "successful": sum(1 for r in results if r.get("content")),
        "failed": sum(1 for r in results if not r.get("content")),
        "posts": [{
            "slug": r["slug"],
            "type": r["type"],
            "chars": len(r.get("content", "")),
            "images": len(r.get("images", [])),
            "error": r.get("error"),
        } for r in results],
    }
    summary_path.write_text(json.dumps(summary, indent=2))

    print(f"\n{'='*50}")
    print(f"DONE: {summary['successful']}/{summary['total']} posts scraped")
    print(f"Failed: {summary['failed']}")
    print(f"Output: {OUTPUT_DIR}")
    print(f"Images: {IMAGES_DIR}")


if __name__ == "__main__":
    main()
