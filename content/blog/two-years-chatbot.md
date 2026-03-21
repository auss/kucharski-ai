---
title: "Two years ago, building a production chatbot meant months of work."
slug: "two-years-ago-building-a-production-chatbot-meant-months-of-work"
date: 2025-11-12
description: "Two years ago this took months. Now it takes a weekend. What happened."
tags: ["developer-experience"]
linkedin: "https://www.linkedin.com/feed/update/urn:li:activity:7381960574244573184/"
image: "/images/blog/two-years-chatbot.png"
---

Everyone knows you shouldn't use production data for testing. And everyone does it anyway.

When we researched the product definition for GoMask we heard of this happening everywhere. Fintech, healthcare, e-commerce, SaaS. Different industries, different stacks, exact same problem.

The official process is always some version of request sanitised data from the data team, wait three days, get a snapshot that's already weeks out of date, discover it doesn't have the edge cases you need, spend hours debugging only to realise the issue only exists in prod anyway.

So teams take the quiet path. SSH into production, grab what they need, debug with real customer data, hope compliance doesn't dig too deep in the next audit.

Mock data isn't realistic enough to debug with. Snapshots go stale. Manual masking takes forever and usually breaks something. None of it works for modern development.

The gap between policy and reality gets worse as you scale. At 20 engineers everyone knows everyone and can quietly look the other way. At 200 engineers you've got a compliance nightmare hiding in plain sight and nobody wants to be the one to call it out.

Interestingly, nobody actually wants this outcome. Engineering wants to do things properly but needs speed. Security wants control but knows the official process creates bottlenecks. Compliance wants documentation but understands that impossible processes just drive behaviour underground.

It's an organisational problem wearing a technical disguise.

The teams that fix this properly do two things. They treat test data infrastructure as critical as CI/CD rather than a someday project. And they give teams self-serve access with compliance built in from the start rather than bolted on after.

This is why we built GoMask. Schema-aware masking that preserves relationships. AI-powered synthetic data for edge cases. Built for CI/CD. Compliance ready from day one.

It's available now and has a free plan: https://gomask.ai/
