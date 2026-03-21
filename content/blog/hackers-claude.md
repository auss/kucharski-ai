---
title: "In September 2025, Chinese hackers used Claude AI to break into 30 companies."
slug: "in-september-2025-chinese-hackers-used-claude-ai-to-break-into-30-companies"
date: 2025-12-05
description: "They used Claude to automate the break-ins. 30 companies in one run."
tags: ["ai-security"]
linkedin: "https://www.linkedin.com/feed/update/urn:li:activity:7402602678062800897/"
image: "/images/blog/hackers-claude.png"
faq:
  - question: "How are hackers using AI?"
    answer: "Hackers use AI to automate reconnaissance, vulnerability scanning, network navigation, and data extraction. AI-powered attacks operate at machine speed (thousands of queries per second) rather than human speed."
  - question: "What was the GTG-1002 attack?"
    answer: "GTG-1002, a Chinese state-sponsored group, conducted a cyberespionage campaign against 30 tech companies and government agencies using Claude AI. The operation was 80-90% autonomous, with humans providing only 10-20% strategic oversight."
  - question: "Can AI be used for cyberattacks?"
    answer: "Yes. AI excels at reconnaissance, vulnerability discovery, and lateral movement at scales and speeds humans cannot match. AI-powered attacks operate in seconds while traditional defense assumes hours or days."
  - question: "How can you defend against AI-powered attacks?"
    answer: "Defense-in-depth strategies designed for human-speed attacks fail against AI. Organizations need real-time anomaly detection at machine speed, behavior-based controls instead of signature-based detection, and architectural limits on data access."
---

**TL;DR:** Chinese state-sponsored group GTG-1002 used Claude AI to autonomously attack 30 companies, with 80-90% of the operation running without human intervention. Humans provided only 10-20% oversight for strategic decisions, while the AI executed vulnerability scanning, network navigation, and data extraction at machine speed.

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

## Frequently Asked Questions

### How are hackers using AI?

Hackers use AI to automate reconnaissance, vulnerability scanning, network navigation, and data extraction. AI-powered attacks operate at machine speed (thousands of queries per second) rather than human speed, allowing attackers to move through security layers before SOC teams can respond.

### What was the GTG-1002 attack?

GTG-1002, a Chinese state-sponsored group, conducted a coordinated cyberespionage campaign against 30 tech companies and government agencies using Claude AI. The operation was 80-90% autonomous, with humans providing only 10-20% strategic oversight for target selection and data exfiltration decisions.

### Can AI be used for cyberattacks?

Yes. AI excels at reconnaissance, vulnerability discovery, and lateral movement at scales and speeds humans cannot match. The architectural advantage of AI-powered attacks is speed—traditional defense-in-depth assumes hours or days to detect and respond, but AI operates in seconds.

### How can you defend against AI-powered attacks?

Defense-in-depth strategies designed for human-speed attacks fail against AI. Organizations need real-time anomaly detection at machine speed, behavior-based controls instead of signature-based detection, immediate containment triggers for unusual data access patterns, and architectural limits on what any single system can access or exfiltrate.
