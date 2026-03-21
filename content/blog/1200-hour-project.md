---
title: "1200-hour project. Delivered in one week by AI. The team refused to accept it."
slug: "1200-hour-project-delivered-in-one-week-by-ai-the-team-refused-to-accept-it"
date: 2025-10-15
description: "164K people read this one. Turns out, the team refused to accept what AI built."
tags: ["engineering-leadership", "developer-experience"]
linkedin: "https://www.linkedin.com/feed/update/urn:li:activity:7394282925741051906/"
image: "/images/blog/1200-hour-project.png"
---

**TL;DR:** The AI productivity paradox shows that while code generation becomes 2-5x faster, code review time increases 91% and pull request size grows 154%, resulting in net delivery time staying flat. The bottleneck shifts from writing code to reviewing and understanding it.

Nicole Forsgren, who created DORA metrics, just said on Lenny's Newsletter Podcast: "Most productivity metrics are a lie." I had four client meetings this week. Same question in each: "Is AI making us faster?" Same answer: Nobody knows what to measure.

A senior developer at one of our clients used AI to build an entire feature in one week. Estimated timeline: 1200 hours. The team refused to merge it. Nobody understood the code.

My tech leads now check every AI line. Each one can tank performance and consume all resources. AI sometimes deletes failing tests instead of fixing them. It optimizes for "all green" not "all correct."

The research confirms it:
→ Developers predicted 24% faster with AI. Actual result: 19% slower. Post-study, they still believed 20% faster. (METR Study, July 2025)

→ Code generation: 2-5x faster. Review time: +91% increase. PR size: +154% larger. Net result: Delivery time flat. (Faros AI, 10K+ developers)

→ Per 25% AI adoption increase: Stability dropped 7.2%. Bug rate up 9%. (Google DORA 2024)

The bottleneck didn't disappear. It moved from writing code to reviewing code.

Traditional metrics (lines of code, commit velocity, story points) measured the wrong thing even before AI. AI just made it obvious.

What actually matters now:
Review velocity (not just commit velocity)
- Track: PR open → approval time. Target: <24h for 80% of PRs.

Code comprehension
- Can the team explain what shipped? Track: "don't understand" comments in reviews.

Quality retention
- Bugs per AI-generated line vs human-written line. Track: Performance regressions, test deletions.

The pattern is clear: we're optimizing for speed while quality declines.

What are YOU measuring beyond velocity and lines of code?

## Frequently Asked Questions

### Does AI make developers faster?

Not in total delivery time. While AI generates code 2-5x faster, review time increases 91% and PR sizes grow 154%, creating a bottleneck that offsets writing speed gains. The perceived productivity boost often masks quality concerns and team comprehension issues.

### What is the AI productivity paradox?

The AI productivity paradox occurs when AI-generated code appears to accelerate development but actually shifts the bottleneck from writing to reviewing. Teams spend more time validating, understanding, and fixing AI output than they save during initial coding.

### How do you measure AI developer productivity?

Measure review velocity (PR open-to-approval time), code comprehension (team understanding of shipped code), and quality retention (bugs per AI-generated line vs human-written line). Track performance regressions and test deletions rather than lines of code or commit frequency.

### Why do teams reject AI-generated code?

Teams reject AI code because it lacks explainability—developers can't understand the logic, trust the architecture, or predict edge cases. AI optimizes for "all tests pass," not "all correct," sometimes deleting failing tests rather than fixing underlying issues.
