---
title: "In September 2025, Chinese hackers used Claude AI to break into 30 companies."
slug: "in-september-2025-chinese-hackers-used-claude-ai-to-break-into-30-companies"
date: 2025-12-05
description: "They used Claude to automate the break-ins. 30 companies in one run."
tags: ["ai-security", "cyberattack", "wake-up-call"]
linkedin: "https://www.linkedin.com/feed/update/urn:li:activity:7402602678062800897/"
image: "/images/blog/hackers-claude.png"
---

80% of the attack ran autonomously.

When Anthropic published the details last month, I couldn't stop reading. Not because of the tech they used, but because of what it means for how we think about defense.

Turns out, most of our security strategies assume attackers move at human speed.

That assumption just became obsolete.

Here's what happened:

Chinese state-sponsored group GTG-1002 launched a coordinated cyberespionage campaign. 30 targets - tech companies and government agencies. The weapon? Claude Code from Anthropic.

80-90% of the operation was autonomous:
- Scanned for vulnerabilities
- Navigated networks
- Identified sensitive data
- Extracted it

Humans only provided 10-20% oversight - strategic direction: which targets, which data, when to exfiltrate.

The AI executed at machine speed generating thousands of queries per second.

Traditional SOC response time? Hours.
AI attack cycle? Seconds.

This is what really got me:

Defense-in-depth just failed at the architecture level.

The model assumes layered controls buy you time: Firewall blocks initial access, EDR catches malware, SIEM correlates anomalies, SOC investigates and contains. That works when attackers operate at human speed and trigger obvious alerts.

But autonomous AI? It moved through all those layers before the first alert reached a human analyst. By the time your SOC noticed unusual activity, exfiltration was complete.

The tools didn't fail. The strategic framework did.

And here's what makes this even more interesting:

Humans still made 10-20% of GTG-1002's decisions. Strategic choices: which targets, which data, when to exfiltrate.

That means strategy became MORE important with AI, not less.

When your Board asks "Are we protected from this?", the traditional answer - MFA, EDR, SIEM, SOC - doesn't cut it anymore.

The real question: "Do we have a security architecture designed for AI-orchestrated attacks?"

Most organizations don't. Because most security strategies were written when attackers operated at human speed.


Anthropic's CEO testifies before Congress on December 17. We'll see regulations on AI model access.

But regulation won't redesign your security architecture.

The GTG-1002 attack isn't breaking news anymore. But the strategic question remains:

Does your Board have answers for autonomous AI threats?

Because that question is coming - and "we're evaluating tools" won't be enough.

Sources:
- Anthropic: "Disrupting the first reported AI-orchestrated cyber espionage campaign" (Nov 13, 2025)
- Axios: "Anthropic CEO called to testify before Congress" (Nov 26, 2025)
