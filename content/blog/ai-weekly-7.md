---
title: "AI Weekly #7: When Investment Velocity Meets Governance Collapse"
slug: "ai-weekly-7-when-investment-velocity-meets-governance-collapse"
date: 2026-02-13
description: "AI spending is accelerating. Governance isn't keeping up."
tags: ["ai-weekly", "ai-adoption"]
linkedin: "https://www.linkedin.com/pulse/when-investment-velocity-meets-governance-collapse-marcin-kucharski-e6n0f"
image: "/images/blog/ai-weekly-7.png"
---

Madhu Gottumukkala, acting director of CISA, uploaded sensitive government documents to public ChatGPT in August 2025.

Universal Music Group filed a $3 billion lawsuit against Anthropic over 20,000+ songs, escalating 40x from their October 2023 suit that covered 500 songs and $75 million in damages. The complaint names CEO Dario Amodei personally and claims Anthropic torrented pirated tracks from LibGen to avoid licensing fees.

Investment velocity is off the charts. Governance? Collapsing in real time.

### The Governance Gap Is Structural

If the person responsible for protecting America's critical infrastructure can't follow basic AI security policy, technical controls need to replace trust. Automated sensors caught the CISA breach in August, alerts fired across DHS systems, but the incident didn't surface publicly until January 2026-six months later-raising questions about who reviews these alerts and what happened to accountability in between.

The $3 billion Anthropic lawsuit creates the "poisoned tree" problem for enterprises. If a court rules Claude was trained illegally, do companies using Claude inherit liability when the model generates copyrighted material? Most vendor indemnification clauses don't cover this scenario. Your procurement team should be reading those contracts right now.

### The Infrastructure Layer Is Racing Ahead

Meta's capex guidance shocked Wall Street, which expected around $110 billion. Zuckerberg said the company will experience "major AI acceleration" in 2026 as it races to catch up after falling behind Google, OpenAI, and Anthropic. Microsoft's Maia 200 uses standard Ethernet for cluster scaling instead of expensive Infiniband, lowering total cost of ownership for massive deployments. Azure's AI business grew 175% year-over-year to $13 billion annual run rate.

Google's AlphaGenome targets the 98% of human DNA that doesn't code for proteins but controls gene activity. Since the API launched seven months ago, nearly 3,000 scientists across 160 countries have used it for cancer and genetic disease research, logging 1 million API calls per day.

### The Control Layer Is Emerging

The companies shipping agents aren't waiting for perfect governance. They're building Zero Trust architectures where every agent is a monitored high-risk user. They're deploying Institutional Memory Layers (RAG 2.0 systems that retrieve business context and historical precedents, not just documents). They're prioritizing defensive use cases first: ITOps, security, data processing. Domains where outputs validate against ground truth without human review bottlenecks that kill ROI.

Governable agents matter more than more agents.

## This Week in Enterprise AI

### 1. The CISA Breach: When Leadership Breaks Policy

![](/images/blog/ai-weekly-7_inline_1.png)

The week's most uncomfortable revelation came from inside the US government. Madhu Gottumukkala, acting director of CISA, uploaded sensitive documents to public ChatGPT in August 2025. The documents were marked "For Official Use Only" (not classified, but not meant for public AI platforms).

Automated sensors caught it immediately, multiple alerts fired, but turns out the story didn't break until January 2026-six months later-raising questions about who reviews these alerts and what happened to accountability.

Gottumukkala requested special ChatGPT access when he joined CISA in May, despite the tool being blocked for most DHS employees. CISA's response emphasized "controls were in place" and use was "short-term and limited." The damage to credibility is done regardless.

The message to every enterprise: policy without enforcement is theater. If the person responsible for protecting America's critical infrastructure can't follow AI security basics, technical controls need to replace trust. Air-gap sensitive systems, monitor every query, and remember-your CISO might be your biggest Shadow AI risk.

### 2. Anthropic's $3 Billion Legal Time Bomb

![](/images/blog/ai-weekly-7_inline_2.png)

Universal Music Group, Concord, and ABKCO filed what could be one of the largest non-class action copyright cases in US history against Anthropic. They're seeking over $3 billion in damages, alleging infringement of 20,000+ songs.

The lawsuit claims Anthropic "torrented an enormous number of unauthorized copies" from illegal shadow libraries like LibGen to avoid licensing fees. It names CEO Dario Amodei and co-founder Benjamin Mann as defendants.

This is a dramatic escalation. The publishers' October 2023 suit covered 500 works with $75 million in potential damages. The new filing is 40x larger. It comes months after Anthropic paid $1.5 billion to authors in a separate settlement over pirated books.

The enterprise question is existential: if a court rules Claude was trained illegally, do companies using Claude inherit liability when outputs reproduce copyrighted material? This is the "poisoned tree" doctrine applied to AI.

Your procurement teams should audit indemnification clauses now. Does Microsoft, Google, or Anthropic cover your legal costs if their model generates infringing content for your business? Most contracts don't. A $3 billion judgment changes the risk calculation overnight.

### 3. Meta's $135 Billion Bet

![](/images/blog/ai-weekly-7_inline_3.png)

Meta delivered strong Q4 2025 earnings on January 28: $59.9 billion revenue, $8.88 EPS, both beating estimates. Capital expenditure will climb to $115-135 billion in 2026, nearly double the $72.2 billion spent in 2025.

Wall Street expected around $110 billion. Meta blew past that. The market responded with a 10% stock surge, signaling investors believe Meta's advertising business can fund the moonshot.

Zuckerberg said the company will experience "major AI acceleration" in 2026 as it races to catch up after falling behind Google, OpenAI, and Anthropic. Rumors suggest "Avocado," a closed-source Llama successor, is planned for spring 2026. If Meta abandons open-source AI, the $135 billion investment needs to generate revenue.

The implication for CTOs: the barrier to entry for frontier AI just doubled. If you're not Meta, Microsoft, or Google, your strategy is integration, not competition.

### 4. Microsoft's Custom Silicon: Maia 200

![](/images/blog/ai-weekly-7_inline_4.png)

Microsoft unveiled Maia 200 on January 26. Built on TSMC's 3nm process with 140 billion transistors and 216GB of HBM3e memory. Claims 10+ petaFLOPS in FP4, 5 petaFLOPS in FP8. Microsoft says it delivers 3x the FP4 performance of Amazon's Trainium and 30% better economics than current Azure infrastructure.

The strategy: break free from Nvidia's pricing power. By designing custom silicon for AI inference, Microsoft controls cost and supply chain for Azure's most profitable workloads. Maia 200 uses standard Ethernet for cluster scaling instead of expensive Infiniband, lowering total cost of ownership for massive deployments.

Azure's AI business grew 175% year-over-year to $13 billion annual run rate. Microsoft now controls the full stack: silicon, cloud infrastructure, and model deployment.

For enterprises, this means Azure's AI pricing will get more competitive in 2026. It also means multi-cloud AI strategies need to account for vendor-specific silicon that may lock workloads to platforms.

### 5. AlphaGenome: Decoding the Dark 98%

![](/images/blog/ai-weekly-7_inline_5.png)

Trained on human and mouse genomes, AlphaGenome predicts gene expression, chromatin accessibility, histone modifications, and transcription factor binding. In 25 of 26 evaluations, it matched or beat the best available models for variant effect prediction.

Since the API launched seven months ago, nearly 3,000 scientists across 160 countries have used it for cancer and genetic disease research. It logs 1 million API calls per day.

Google isn't selling AlphaGenome at per-token pricing. They're building partnerships with healthcare companies to monetize insights.

## Bottom Line for You

### This week's action items:

1. **Indemnification Audit** — Review AI vendor contracts. Does Microsoft, Google, or Anthropic cover your legal costs if their model generates copyright-infringing content? The $3 billion Anthropic lawsuit made this clause business-critical.

2. **Zero Trust for AI** — Treat every AI agent as a high-risk user. Monitor all API calls, database writes, external integrations. If the CISA director can't be trusted with ChatGPT, neither can your employees.

3. **Institutional Memory Layer** — Build RAG 2.0 systems that retrieve business context and decision precedents, not just documents. Your agents need to understand "why we don't do that" before autonomously executing "technically correct" actions.

4. **Agent Control Plane** — Create a central registry of deployed agents. Map permissions, dependencies, trigger conditions to prevent cascading chaos when one agent's action spawns unintended downstream consequences.

Is your governance architecture ready, or are you the next CISA headline?
