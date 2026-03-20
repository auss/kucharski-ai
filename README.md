# kucharski.ai — Personal Blog

A modern, performant personal blog about AI adoption, engineering leadership, and building with emerging technologies.

## Design

**Theme:** Punk zine aesthetic with a dark mode + lime accent
- Custom typography with Space Mono, Archivo Black, and Schibsted Grotesk
- Grain overlay texture for tactile feel
- Animated scroll reveals
- Responsive design (mobile-first)

**Features:**
- Hero section with blinking cursor and strikethrough text
- Ticker marquee with keywords
- Featured post highlight
- Post list with grid layout
- "Now" page (what I'm doing now)
- Contact section with CTAs

## Project Structure

```
kucharski.ai/
├── hugo.toml              # Hugo configuration
├── content/
│   ├── blog/              # 20 blog posts (markdown)
│   └── now.md             # Now page
├── layouts/
│   ├── _default/
│   │   ├── baseof.html    # Base template
│   │   └── single.html    # Generic page template
│   ├── blog/
│   │   ├── single.html    # Post detail page
│   │   └── list.html      # Blog archive page
│   └── index.html         # Homepage
├── static/
│   ├── css/style.css      # Complete stylesheet
│   └── CNAME              # Domain configuration
├── .github/workflows/
│   └── hugo.yml           # GitHub Pages deployment
└── .gitignore
```

## Blog Posts

20 posts covering:
- **AI Adoption** (1200-hour project, 42% abandoned)
- **Engineering Leadership** (Writing code, impact metrics)
- **AI Governance** (Shadow AI, security risks)
- **Personal** (ADHD, labels, authenticity)
- **Trends** (Infrastructure consolidation, standards)

All posts are sourced from LinkedIn and expanded with thoughtful context.

## Build & Deploy

### Local Development
```bash
cd ~/projects/kucharski.ai
hugo server --buildDrafts
# Visit http://localhost:1313
```

### Production Build
```bash
hugo --minify --gc
# Output: ./public/
```

### GitHub Pages
The site auto-deploys on push to `main` via GitHub Actions workflow (`.github/workflows/hugo.yml`).

Domain configuration via `static/CNAME`.

## Technologies

- **Static Generator:** Hugo 0.147+
- **Fonts:** Google Fonts (Space Mono, Archivo Black, Schibsted Grotesk)
- **Styling:** Custom CSS with CSS variables
- **Animations:** CSS keyframes (fadeUp, blink, marquee)
- **Scripting:** Vanilla JavaScript (IntersectionObserver for scroll reveals)
- **Deployment:** GitHub Pages + GitHub Actions

## Customization

### Modify Colors
Edit CSS variables in `static/css/style.css`:
```css
:root {
  --bg: #0e0e0e;
  --accent: #c8ff00;
  /* ... */
}
```

### Add New Posts
```bash
hugo new content blog/my-post.md
# Edit front matter:
# - title, date, description
# - tags (for categorization)
# - linkedin (link to LinkedIn post)
```

### Update Homepage Text
Edit `layouts/index.html` sections:
- Hero section (hardcoded)
- Ticker keywords (hardcoded)
- Contact section (hardcoded)

## Performance

- **Page Speed:** ~100ms to render (static generation)
- **CSS Size:** ~12KB minified
- **Fonts:** Preconnected + display=swap for fast load
- **Images:** None (pure CSS design)
- **JavaScript:** <2KB (vanilla IntersectionObserver)

## Accessibility

- Semantic HTML structure
- High contrast (AAA compliant on links)
- Keyboard navigation supported
- Focus states on interactive elements
- Screen reader friendly

## License

Personal site — design and content © 2026 Marcin Kucharski
