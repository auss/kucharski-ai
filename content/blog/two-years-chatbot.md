---
title: "Two years ago, building a production chatbot meant months of work."
slug: "two-years-ago-building-a-production-chatbot-meant-months-of-work"
date: 2025-11-12
description: "Two years ago this took months. Now it takes a weekend. What happened."
tags: ["developer-experience"]
linkedin: "https://www.linkedin.com/feed/update/urn:li:activity:7381960574244573184/"
image: "/images/blog/two-years-chatbot.png"
faq:
  - question: "Why do teams use production data for testing instead of following official data policies?"
    answer: "Official processes require requesting sanitized data from the data team, waiting 3+ days, receiving snapshots that are weeks out of date, discovering they lack needed edge cases, spending hours debugging only to realize the issue exists only in production. The gap between policy and reality grows as organizations scale: at 20 engineers, everyone knows each other and can quietly look the way; at 200 engineers, compliance discovers a shadow practice that seemed invisible. Engineering wants speed, security wants control, compliance wants documentation—but the official process serves none well."
  - question: "What is the core organizational problem with test data infrastructure?"
    answer: "It's not technical—it's organizational. Test data infrastructure is treated as a 'someday project' rather than critical infrastructure like CI/CD. Teams lack self-serve access to compliant test data. The result: a policy-reality gap where teams bypass security via unauthorized production access. The solution requires two things: treat test data as critical infrastructure (same priority as CI/CD), and give teams self-serve access with compliance built in from the start, not bolted on after discovery."
  - question: "What are the hidden costs of shadow IT practices like unauthorized production data access?"
    answer: "At 20 engineers, side effects are invisible. At 200 engineers, it becomes a compliance nightmare. Unauthorized production access creates audit risk, exposes customer data to uncontrolled debugging, violates compliance requirements (SOC 2, HIPAA, PCI-DSS in regulated industries), and provides no audit trail. When audits happen, organizations face penalties and must scramble to implement proper data governance retroactively."
  - question: "How can organizations fix the test data gap without slowing development?"
    answer: "Schema-aware masking preserves data relationships while removing PII. AI-powered synthetic data handles edge cases. Built-in CI/CD integration gives teams instant self-serve access. Compliance-ready from day one means no post-deployment retrofitting. Organizations that treat test data infrastructure as critical (not a 'someday project') eliminate the policy-reality gap and enable fast, compliant development."
---

**TL;DR:** Official test data process: request, wait 3 days, get outdated snapshots missing edge cases. Reality: teams access production directly, violating compliance. The gap widens at scale. Solution: treat test data as critical infrastructure (not 'someday'), provide self-serve access with schema-aware masking and AI-powered synthetic data, build compliance in from day one. Teams get speed; audits pass.

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

---

## Frequently Asked Questions

### Why do teams use production data for testing instead of following official data policies?
Official processes require requesting sanitized data from the data team, waiting 3+ days, receiving snapshots that are weeks out of date, discovering they lack needed edge cases, spending hours debugging only to realize the issue exists only in production. The gap between policy and reality grows as organizations scale: at 20 engineers, everyone knows each other and can quietly look the way; at 200 engineers, compliance discovers a shadow practice that seemed invisible. Engineering wants speed, security wants control, compliance wants documentation—but the official process serves none well.

### What is the core organizational problem with test data infrastructure?
It's not technical—it's organizational. Test data infrastructure is treated as a "someday project" rather than critical infrastructure like CI/CD. Teams lack self-serve access to compliant test data. The result: a policy-reality gap where teams bypass security via unauthorized production access. The solution requires two things: treat test data as critical infrastructure (same priority as CI/CD), and give teams self-serve access with compliance built in from the start, not bolted on after discovery.

### What are the hidden costs of shadow IT practices like unauthorized production data access?
At 20 engineers, side effects are invisible. At 200 engineers, it becomes a compliance nightmare. Unauthorized production access creates audit risk, exposes customer data to uncontrolled debugging, violates compliance requirements (SOC 2, HIPAA, PCI-DSS in regulated industries), and provides no audit trail. When audits happen, organizations face penalties and must scramble to implement proper data governance retroactively.

### How can organizations fix the test data gap without slowing development?
Schema-aware masking preserves data relationships while removing PII. AI-powered synthetic data handles edge cases. Built-in CI/CD integration gives teams instant self-serve access. Compliance-ready from day one means no post-deployment retrofitting. Organizations that treat test data infrastructure as critical (not a "someday project") eliminate the policy-reality gap and enable fast, compliant development.
