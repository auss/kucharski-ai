---
title: "AI Weekly #6: 85% Customize Agents, 25% Ship Them"
slug: "ai-weekly-6-85-customize-agents-25-ship-them"
date: 2026-01-23
description: "85% customize their agents. Only 25% actually ship them."
tags: ["ai-weekly", "ai-adoption"]
linkedin: "https://www.linkedin.com/pulse/85-problem-enterprise-ai-stuck-between-ambition-marcin-kucharski-rzxkf"
image: "/images/blog/newsletter-6.png"
faq:
  - question: "Why can 85% of enterprises customize agents but only 25% ship them to production?"
    answer: "The pilot-to-production conversion rate sits at 21-25% across surveys, with the primary blocker being security governance, not model performance. Three high-profile exploits in January 2026 (Gemini Calendar prompt injection, Cursor IDE arbitrary code execution, Claude Code session hijacking) killed deployment plans for enterprises that spent months on pilots. The gap is the Security Development Lifecycle running slower than agent deployment cycles."
  - question: "What are the main security risks preventing agent production deployment?"
    answer: "Prompt injection attacks hide malicious instructions in calendar events, code comments, email subjects, and filenames that exfiltrate data or escalate privileges. Cursor IDE's CVE-2026-22708 showed arbitrary code execution through workspace configuration files. Claude Code faced session hijacking via crafted HTML comments. Enterprise security teams lack AI-aware threat models in design, development, testing, and deployment phases—security reviews happen after pilots, creating technical debt faster than features ship."
  - question: "How can enterprises move agents from pilots to production faster?"
    answer: "Instrument agents like microservices using observability platforms: 72% of enterprises now manage agent lifecycle with health checks, distributed tracing, and anomaly detection. Treat autonomous agents with the same rigor as APIs. Red team agents for prompt injection before production. Build security into pilot design, not after. Defensive use cases (ITOps, cybersecurity, data processing) ship faster because workflows are instrumented, data is structured, and hallucination risk is lower than generative use cases."
  - question: "Which agent deployment strategies deliver highest ROI and fastest time-to-production?"
    answer: "Vertical agents targeting specific workflows (Microsoft Board Agents, AWS Nova Sonic, Hippocratic AI) outperform horizontal platforms. 44% of enterprises expect highest ROI from agentic AI in ITOps and system monitoring, 27% in cybersecurity, 25% in data processing. These defensive use cases deliver faster ROI than generative use cases (sales content, legal contracts) because agents parse logs and flag anomalies with ground truth validation. Vertical wins over horizontal when domain workflows require compliance and audit trails."
---

**TL;DR:** 85% customize agents, 25% ship them. The gap isn't technology—it's governance. Security exploits (Gemini Calendar, Cursor IDE, Claude Code) blocked deployment plans in January 2026. The solution: instrument agents like microservices (72% of enterprises now do this), red team for prompt injection, and prioritize vertical agents for defensive use cases (ITOps 44% ROI, cybersecurity 27%) that ship faster than generative ones.

85% of enterprises are customizing AI agents for their business needs.

Only 25% have moved those agents to production.

This is the largest governance gap in technology history, and it's running at machine speed. Deloitte's 2026 State of AI report shows 74% of companies are increasing AI budgets, Dynatrace found 50% stuck in proof-of-concept mode, and NVIDIA's finance survey confirms 65% overall adoption but just 21% deployed agents in production.

And the best part: The companies solving this aren't building better AI. They're building better control planes.

### The Ambition Layer Is Exploding

85% of companies expect to tailor agents to fit their business processes, role hierarchies, and domain vocabularies. Microsoft's Board Agents launched in January 2026 with FP&A triangulation architecture designed specifically for CFOs: one agent reads Board decks, another scans earnings transcripts, a third triangulates scenarios. AWS Nova Sonic delivers sub-second response latency with 1.09s time-to-first-audio, optimized for real-time enterprise workflows. Hippocratic AI raised to a $3.5 billion valuation building non-diagnostic patient-facing agents that handle administrative tasks human nurses hate.

This is vertical specialization at scale, with 42% of enterprises using or assessing agentic AI according to NVIDIA's survey. The problem moves from technology readiness to governance readiness.

### The Reality Layer Is Collapsing

The Security Development Lifecycle gap is crushing production plans. Turn of 2025 and 2026 brought three high-profile exploits: The Gemini Calendar prompt injection let attackers exfiltrate calendar data by hiding instructions in event descriptions, Cursor IDE's CVE-2026-22708 exposed arbitrary code execution through malicious workspace files, and Claude Code faced session hijacking through crafted HTML comments in codebases. These aren't theoretical risks. They're production blockers that killed deployment plans for enterprises that spent months on pilots.

Meanwhile, OpenAI reported 320x year-over-year growth in reasoning tokens, with enterprises burning through context windows faster than governance can audit them. The pilot-to-production conversion rate sits at 21-25% across surveys, and the primary blocker isn't model performance. It's identity, access control, and audit trails running at speeds compliance teams can't match.

### The Solution Layer Is Emerging

The companies moving to production aren't waiting for perfect security (which is not possible in AI era). They're building agent control planes.

Observability platforms became the unexpected winners. Dynatrace reports 72% of enterprises now use observability tools to manage agent lifecycle, treating autonomous agents like microservices with instrumentation, health checks, and distributed tracing. Google's Universal Commerce Protocol introduced the Trust Triangle architecture: Model Context Protocol for tool discovery, Agent-to-Agent Protocol for workflow coordination, and Agent Protocol 2 for identity verification. Shopify and Walmart are building integrations that let AI transact without exposing credentials.

Instead of chasing perfect agents, we're moving toward governed agents. Dynatrace found 44% of agentic AI projects deliver highest ROI in ITOps and system monitoring, 27% in cybersecurity, and 25% in data processing. These aren't sexy use cases. They're defensive use cases where control matters more than creativity.

And that's exactly why they're shipping to production.

## This Week in Enterprise AI

### 1. Vertical Agents Are Outperforming Horizontal Platforms

![](/images/blog/newsletter-6_inline_1.png)

Microsoft Board Agents launched in January 2026 with architecture designed for CFOs, not general knowledge workers. One agent reads Board presentation decks, another scans earnings call transcripts, a third triangulates financial scenarios by cross-referencing both. AWS Nova Sonic benchmarked at 1.09s time-to-first-audio, beating competitors for real-time workflows that can't tolerate LLM lag. Hippocratic AI raised to a $3.5 billion valuation building non-diagnostic patient-facing agents that handle scheduling, insurance verification, and appointment reminders. Siemens Industrial Copilot automates PLM, CAD, and supply chain tasks specific to manufacturing.

Gartner predicted in August 2025 that 40% of enterprise applications would embed agents by end of 2026. We're on track. The pattern is clear: vertical wins over horizontal when domain-specific workflows require compliance, audit trails, and integration with legacy systems that horizontal platforms can't touch.

### 2. Google's Universal Commerce Protocol Introduces the Trust Triangle

Google Developers Blog detailed UCP's architecture in January 2026, and it's not a checkout play. The Trust Triangle combines three protocols: Model Context Protocol for tool discovery, Agent-to-Agent Protocol for workflow coordination, and Agent Protocol 2 for identity verification. Shopify, Walmart, and Instacart are building integrations that let AI agents complete transactions without exposing user credentials or payment details.

Early feedback from partners shows UCP reduces integration complexity compared to traditional REST APIs, but privacy concerns linger. Google's protocol could centralize control despite open standard claims, raising antitrust questions. The technical architecture works, but the market power question remains open.

### 3. Security Exploits Are Blocking Production Deployments

![](/images/blog/newsletter-6_inline_2.png)

End of 2025 and beginning of 2026 brought three high-profile AI security incidents that killed deployment plans:

The Gemini Calendar prompt injection exploit let attackers hide instructions in calendar event descriptions that exfiltrated sensitive meeting data when Gemini processed the calendar. Miggo Security reported the vulnerability in January 2026, and enterprises running Gemini pilots pulled agents from production immediately.

Cursor IDE's CVE-2026-22708 exposed arbitrary code execution through malicious workspace configuration files. An attacker could craft a .cursorrules file that executes on IDE startup, compromising developer machines. GitHub Copilot faced similar risks with workspace trust boundaries.

Claude Code session hijacking used crafted HTML comments in codebases to inject instructions that redirected agents to exfiltrate code or modify files. The attack vector exploited context injection through comments that looked benign but carried malicious prompts.

Security incidents targeting AI systems surged in Q4 2025, with enterprises struggling to integrate AI-aware security checks across the full SDLC. The pilot-to-production gap isn't a technology problem. It's a security governance problem.

### 4. Observability Platforms Become Agent Control Towers

![](/images/blog/newsletter-6_inline_3.png)

72% of enterprises now use observability platforms to manage agent lifecycle, treating autonomous agents like microservices with instrumentation, health checks, and distributed tracing.

Observability platforms adapted to monitor agent behavior with instrumentation for health checks, distributed tracing, and anomaly detection when agents deviate from expected patterns. This infrastructure approach solves the visibility gap that compliance teams flagged as the primary blocker to production deployment.

The shift mirrors how enterprises scaled microservices in 2015-2018. You can't manage what you can't measure, and agents executing thousands of decisions per hour need instrumentation just like APIs. Observability platforms provide the audit trail compliance needs, the performance metrics engineering needs, and the cost transparency finance needs.

This explains why 44% of high-ROI agent projects land in ITOps and system monitoring. The teams already running observability platforms are shipping agents faster because they're reusing existing control infrastructure instead of building governance from scratch.

### 5. Humans& Raises $480M Seed at $4.48B Valuation on Human-Centric Thesis

Humans& announced a $480 million seed round in January 2026 at a $4.48 billion post-money valuation, with investors including NVIDIA, Jeff Bezos's family office, and GV. The startup builds AI that augments human decision-making rather than replacing it, targeting long-horizon tasks where reinforcement learning achieves 85% accuracy but humans provide judgment on edge cases.

This is a market shift away from full automation toward human-AI teams. Workera launched similar products in December 2025 focused on upskilling workers alongside AI rather than displacing them. The funding reflects backlash against AGI hype and a pivot toward practical augmentation that enterprises can deploy without layoffs.

McKinsey's State of AI (November 2025) found high performers are more than 3x as likely to pursue transformative AI use cases instead of incremental automation. The human-centric approach reduces resistance, accelerates adoption, and delivers ROI in months instead of years.

### 6. ChatGPT Go at $8/Month with Ads Creates Shadow IT Compliance Risk

OpenAI launched ChatGPT Go in January 2026 at $8 per month with ads, positioning between Free (limited) and Plus ($20, no ads). OpenAI reported 8x message volume growth year-over-year and 320x growth in reasoning tokens, driven by o3 and o1 adoption in enterprises. The ad-supported Go tier addresses accessibility but creates shadow IT risk: employees subscribe personally, paste proprietary data into prompts, and OpenAI's ad partners potentially access training data.

The monetization shift shows pricing stabilization around enterprise value. Google and AWS made similar moves in October 2025, adjusting per-token pricing to reflect compute costs. ChatGPT Go's $8 price point targets prosumers who won't pay $20 but need more than Free tier limits.

The compliance risk is real. Ad-supported tiers with unclear data retention policies create exposure for enterprises that don't govern personal AI subscriptions. CISOs should audit ChatGPT Go subscriptions the same way they audit personal Dropbox or Gmail usage that touches corporate data.

### 7. ITOps ROI Dominates Because Defensive Wins Ship Faster

![](/images/blog/newsletter-6_inline_4.png)

Here's what most people miss: The highest ROI for agentic AI isn't in sales, marketing, or customer support. It's in ITOps and system monitoring.

Dynatrace found 44% of enterprises expect highest ROI from agentic AI in ITOps and system monitoring, 27% in cybersecurity, and 25% in data processing and reporting. These aren't glamorous use cases. They're defensive use cases where agents monitor logs, detect anomalies, remediate incidents, and generate reports. McKinsey confirmed 56% of companies see value in software engineering automation, and 51% in customer support, but ITOps delivers faster time-to-value because the workflows are already instrumented, the data is already structured, and the risk of hallucination is lower.

Defensive AI ships to production because it's easier to govern. An agent that parses logs and flags anomalies can be validated with ground truth. An agent that generates sales copy or drafts legal contracts requires human review at scale, which kills ROI. The 44% ITOps stat explains why companies stuck at 25% production deployment are prioritizing observability platforms over generative content tools.

The infrastructure bet is clear. The creativity bet? Not so much.

## What To Do Monday Morning

### 1. Audit Your Pilot-to-Production Conversion Rate

Pull the list of AI pilots launched in 2025. How many moved to production? If your conversion rate is below 25%, the blocker isn't technology. It's governance. Snyk's data shows only 29% integrated AI-aware security into SDLC. Start there: design, development, testing, deployment. If security reviews happen after pilot completion, you're building technical debt faster than you're shipping features.

### 2. Instrument Your Agents Like Microservices

72% of enterprises use observability platforms to manage agent lifecycle. If you're running agents in production, instrument them: log every request, track token consumption, measure latency distributions, detect anomalies when behavior deviates. Treat agents like APIs with health checks, distributed tracing, and audit logs. You can't govern what you can't measure.

### 3. Red Team Your Agents for Prompt Injection

Run adversarial testing on every agent before production. Gemini Calendar, Cursor IDE, and Claude Code all shipped exploits in January 2026 because prompt injection wasn't part of the threat model. Hire a red team or use tools like Microsoft Security Copilot to fuzz inputs. Test: Can an attacker hide instructions in calendar events, code comments, email subjects, or file names that exfiltrate data or escalate privileges? If yes, fix before deploying.

### 4. Evaluate Vertical Agents for High-ROI Use Cases

Dynatrace's 44% ITOps ROI and 27% cybersecurity ROI point to defensive use cases shipping faster than generative use cases. Microsoft Board Agents, AWS Nova Sonic, Hippocratic AI, and Siemens Industrial Copilot all target specific workflows with compliance built in. Evaluate vertical agents for your industry before building custom agents on horizontal platforms. Time-to-production matters more than flexibility when pilots are stuck at 50%.

### 5. Audit ChatGPT Go and Shadow IT for Data Leakage

ChatGPT Go launched at $8/month with ads. Employees are subscribing personally and pasting proprietary code, customer lists, and financial data into prompts. Audit your org for personal ChatGPT Plus, Go, and Free subscriptions the same way you audit Dropbox or Gmail. Tools like Microsoft Defender for Cloud Apps and Netskope can detect ChatGPT usage and flag high-risk prompts. Block or govern before a breach.

## 6. Calculate Your Reasoning Token Burn Rate

OpenAI reported 320x growth in reasoning tokens year-over-year, driven by o3 and o1 adoption. If your agents use reasoning-heavy models, calculate your monthly token burn rate and compare it to budget. Reasoning tokens cost more than completion tokens, and 320x growth means costs are compounding faster than most finance teams forecasted. Optimize prompts, cache reasoning chains, or switch to smaller models for low-risk tasks before costs spiral.

---

## Frequently Asked Questions

### Why can 85% of enterprises customize agents but only 25% ship them to production?
The pilot-to-production conversion rate sits at 21-25% across surveys, with the primary blocker being security governance, not model performance. Three high-profile exploits in January 2026 (Gemini Calendar prompt injection, Cursor IDE arbitrary code execution, Claude Code session hijacking) killed deployment plans for enterprises that spent months on pilots. The gap is the Security Development Lifecycle running slower than agent deployment cycles.

### What are the main security risks preventing agent production deployment?
Prompt injection attacks hide malicious instructions in calendar events, code comments, email subjects, and filenames that exfiltrate data or escalate privileges. Cursor IDE's CVE-2026-22708 showed arbitrary code execution through workspace configuration files. Claude Code faced session hijacking via crafted HTML comments. Enterprise security teams lack AI-aware threat models in design, development, testing, and deployment phases—security reviews happen after pilots, creating technical debt faster than features ship.

### How can enterprises move agents from pilots to production faster?
Instrument agents like microservices using observability platforms: 72% of enterprises now manage agent lifecycle with health checks, distributed tracing, and anomaly detection. Treat autonomous agents with the same rigor as APIs. Red team agents for prompt injection before production. Build security into pilot design, not after. Defensive use cases (ITOps, cybersecurity, data processing) ship faster because workflows are instrumented, data is structured, and hallucination risk is lower than generative use cases.

### Which agent deployment strategies deliver highest ROI and fastest time-to-production?
Vertical agents targeting specific workflows (Microsoft Board Agents, AWS Nova Sonic, Hippocratic AI) outperform horizontal platforms. 44% of enterprises expect highest ROI from agentic AI in ITOps and system monitoring, 27% in cybersecurity, 25% in data processing. These defensive use cases deliver faster ROI than generative use cases (sales content, legal contracts) because agents parse logs and flag anomalies with ground truth validation. Vertical wins over horizontal when domain workflows require compliance and audit trails.
