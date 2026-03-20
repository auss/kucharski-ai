# Deployment Guide

## GitHub Pages Setup

This site is configured to deploy to GitHub Pages automatically on every push to `main`.

### Initial Setup (One-time)

1. **Create a GitHub repository** at `github.com/yourusername/kucharski.ai`

2. **Push the code:**
   ```bash
   cd ~/projects/kucharski.ai
   git remote add origin https://github.com/yourusername/kucharski.ai.git
   git branch -M main
   git push -u origin main
   ```

3. **Configure GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `/ (root)`
   - Click Save

4. **Enable Actions:**
   - Go to Settings → Actions → General
   - Allow GitHub Actions
   - Workflow permissions: Read and write permissions

### Domain Configuration

1. **Point domain to GitHub Pages:**
   ```
   kucharski.ai → CNAME → yourusername.github.io
   ```
   Or use A records:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

2. **GitHub will auto-detect CNAME file** from `static/CNAME`

3. **HTTPS will be auto-enabled** (after domain propagates)

### Automatic Deployment Workflow

Every push to `main` triggers:

1. `.github/workflows/hugo.yml` runs
2. Installs Hugo 0.147
3. Builds site with `hugo --minify --gc`
4. Uploads artifacts to GitHub Pages
5. Site live at `https://kucharski.ai` (or your domain)

**Status Check:**
- Go to Actions tab in GitHub
- See build logs and deployment status

## Manual Deployment (Alternative)

If not using GitHub Pages:

### To Netlify
```bash
hugo --minify --gc
# Upload public/ folder to Netlify

# Or:
npm install -g netlify-cli
netlify deploy --prod
```

### To Vercel
```bash
hugo --minify --gc
vercel --prod
```

### To Any Hosting
```bash
hugo --minify --gc
# Upload public/ to your web server via FTP/SCP
```

## Local Preview Before Push

```bash
hugo server --buildDrafts
# Visit http://localhost:1313
# Make changes, site auto-reloads
# Press Ctrl+C to stop
```

## Build Verification

```bash
# Clean build
rm -rf public resources
hugo --minify --gc

# Check output
ls -lh public/
du -sh public/

# Validate HTML
npm install -g html-validate
html-validate public/index.html
```

## Troubleshooting

### Build Fails
```bash
# Check Hugo version (need 0.100+)
hugo version

# Verbose output
hugo -v

# Check for errors in content
hugo --enableWebsiteMode
```

### Site Doesn't Show Posts
- Check `content/blog/` has .md files
- Verify YAML front matter is valid
- Check `layouts/index.html` references correct path

### CSS Not Loading
- Check `static/css/style.css` exists
- Verify `baseURL` in `hugo.toml` matches domain
- Clear browser cache

### Domain Not Working
- Verify DNS points to GitHub Pages IPs
- Check CNAME file at `static/CNAME`
- Wait 5-10 minutes for DNS propagation

## Monitoring

### Google Analytics
Add to `layouts/_default/baseof.html`:
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_ID');
</script>
```

### Lighthouse CI
Add to workflow:
```yaml
- name: Run Lighthouse CI
  uses: treosh/lighthouse-ci-action@v9
  with:
    uploadArtifacts: true
```

## Maintenance

### Regular Backups
```bash
cd ~/projects
tar -czf kucharski.ai-backup-$(date +%Y%m%d).tar.gz kucharski.ai/
```

### Monitor Build Times
```bash
# Check Actions tab in GitHub
# Target: < 30 seconds
```

### Keep Hugo Updated
```bash
brew upgrade hugo
hugo version
```

## Security

### Secrets Management
- No secrets stored in `hugo.toml`
- Use environment variables for sensitive config
- GitHub Secrets for API keys (if needed)

### Content Security
- No user-generated content
- All changes via git (auditable)
- Branch protection on `main` (optional)

## Performance Optimization

Current metrics:
- Build time: ~50ms
- CSS size: ~12KB
- Total page size: ~25KB
- Lighthouse: 100/100

To maintain:
1. Keep images minimal (use CSS)
2. Avoid heavy JavaScript
3. Use preload/prefetch wisely
4. Monitor bundle size

---

**Ready to deploy?** Follow Initial Setup steps above, then run `git push` and watch it deploy!
