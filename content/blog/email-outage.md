---
title: "Two days. That's how long email system wasn't working."
slug: "two-days-thats-how-long-email-system-wasnt-working"
date: 2025-11-08
description: "An outage that revealed what we depend on."
tags: ["product"]
linkedin: "https://www.linkedin.com/feed/update/urn:li:activity:7376940643052408832/"
image: "/images/blog/email-outage.png"
---

Another time, systems degraded slowly over several days. Performance dropped, errors accumulated. The signals were there—in logs, in system outputs—but nobody connected the dots. We only acted once the system collapsed and downtime forced our hand.

And then there was the logging mess. Thousands of entries captured everything except what mattered. No meaningful checkpoints, no way to reconstruct what really happened. When issues hit, connecting the dots was nearly impossible.

The pattern across all these failures was the same: they weren’t technical problems. They were organizational blind spots—policies never communicated, logging without strategy, and a habit of waiting until failure before paying attention.

And that’s exactly where AI could have helped. Not as a silver bullet, but as a set of very practical tools that reduce the risk of these blind spots:
→ Policy awareness
AI could continuously scan security rules, tickets, and documentation changes. When a new policy—like password rotation—was introduced, it would map which accounts were affected and proactively notify the right owners. Instead of learning from clients that our system broke, we’d get an early warning and fix it before anyone noticed.

→ Signal amplification
Raw logs already contained the story of system degradation, but buried under volume. AI could learn which error patterns historically led to downtime and raise an alert the moment those same trends appeared again. Instead of acting only after collapse, we’d have the chance to address issues days earlier.

→ Meaningful logging strategies
AI could analyze past incidents and point out what was missing: “If you had captured variable X or state Y, you would have solved this in minutes instead of hours.” Over time, this builds a logging strategy that isn’t based on guesswork but on evidence.

→ Cross-signal correlation
Problems don’t announce themselves in one place. A few support tickets, a subtle rise in error logs, a dip in performance metrics—all are weak signals on their own. AI can correlate these streams, showing the bigger picture: this combination usually precedes a major incident. That’s the difference between clients calling us and us calling clients.

What’s important here is perspective. AI won’t run systems for us, and it won’t eliminate human responsibility. But it can take over the part we’re consistently bad at—spotting weak signals in oceans of noise, connecting dots across silos, and making sure policy changes don’t silently blow up production.

How do you see AI reshaping observability in your organization? If this resonates, maybe you’d like to talk about your case?
