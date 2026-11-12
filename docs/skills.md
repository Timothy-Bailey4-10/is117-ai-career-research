# Skills Required

What you need to get hired as a **Forward Deployed Engineer** and in the roles around it, and how to prove each skill.

## What FDE postings ask for

From Bloomberry's analysis of ~1,000 FDE job postings (2026):

<div class="bars">
  <div class="bar"><span>Python</span><div class="track"><div class="fill" style="width:66%"></div></div><span class="pct">66%</span></div>
  <div class="bar"><span>AI agents</span><div class="track"><div class="fill" style="width:35%"></div></div><span class="pct">35%</span></div>
  <div class="bar"><span>TypeScript</span><div class="track"><div class="fill" style="width:35%"></div></div><span class="pct">35%</span></div>
  <div class="bar"><span>AWS</span><div class="track"><div class="fill" style="width:32%"></div></div><span class="pct">32%</span></div>
  <div class="bar"><span>LLM experience</span><div class="track"><div class="fill" style="width:31%"></div></div><span class="pct">31%</span></div>
  <div class="bar"><span>GCP</span><div class="track"><div class="fill" style="width:22%"></div></div><span class="pct">22%</span></div>
  <div class="bar"><span>Azure</span><div class="track"><div class="fill" style="width:18%"></div></div><span class="pct">18%</span></div>
</div>

A separate review of FDE postings found the most common non-language requirements to be **production coding, stakeholder communication, customer discovery, AI/agent development, integrations, and owning adoption**.

## FDE skills checklist

### Technical (must-have)

| Skill | What it means in practice | How to prove it |
|---|---|---|
| **Production coding** | Python and/or TypeScript you'd be comfortable shipping, with tests | A public repo with a real deployed app |
| **APIs & integrations** | REST and webhooks, auth (OAuth, API keys), connecting to CRMs and databases | Project that pulls from a real third-party API |
| **SQL & data wrangling** | Cleaning messy exports and building simple pipelines | Notebook or script that turns raw data into usable inputs |
| **LLM apps** | Prompting, structured outputs, RAG (embeddings + vector DB) | A RAG app over real documents |
| **Agents & tool use** | Model calls tools, takes multi-step actions, hands off to humans | An agent that completes a real task end-to-end |
| **Evals** | Test sets, metrics, and regression checks for AI output | An eval report in your project README |
| **Cloud & deploy** | One cloud (AWS is most common), Docker, environment config | Your project running at a public URL |

### People (what makes an FDE different from other engineers)

| Skill | What it means in practice | How to prove it |
|---|---|---|
| **Customer discovery** | Asking questions until you understand the real workflow | A write-up of the user problem you solved |
| **Communication** | Explaining trade-offs to non-engineers, writing clear docs | A 5-minute demo video + one-page summary |
| **Ownership** | Debugging production issues with little guidance | A story about something that broke and how you fixed it |
| **Scoping** | Turning a vague request into a buildable plan | Your project's "v1 vs later" decisions |

## Skills by role

How much each similar role relies on each skill area:

| Skill | FDE | Applied AI Eng. | Solutions Eng. | AI Engineer | Agent Engineer | AI Eval Eng. |
|---|---|---|---|---|---|---|
| Production coding | ●●● | ●●● | ●● | ●●● | ●●● | ●● |
| APIs & integrations | ●●● | ●●● | ●● | ●● | ●●● | ● |
| LLM apps / RAG | ●●● | ●●● | ●● | ●●● | ●●● | ●● |
| Agents & tool use | ●●● | ●●● | ●● | ●● | ●●● | ●● |
| Evals | ●● | ●●● | ● | ●● | ●● | ●●● |
| Cloud & deploy | ●● | ●● | ●● | ●●● | ●● | ● |
| Customer communication | ●●● | ●●● | ●●● | ● | ● | ● |
| Demos & presenting | ●●● | ●● | ●●● | ● | ● | ● |

<small>●●● core requirement · ●● expected · ● nice to have. Compiled from the role guides on this site.</small>

## One project that covers almost everything

Build **one AI agent for a real user** (a club, small business, or professor):

1. **Discover**: interview them and write down the workflow (*customer discovery*)
2. **Build**: an agent in Python or TypeScript that calls their real tools or data (*coding, APIs, agents, RAG*)
3. **Deploy**: put it at a public URL on AWS or similar (*cloud*)
4. **Measure**: write 20–50 test cases and report the pass rate (*evals*)
5. **Present**: record a 5-minute demo and write a one-page summary (*communication*)

That single project lets you answer most FDE interview rounds with a real story.

<small>Sources: Bloomberry, *I analyzed 1,000 FDE jobs* (2026); Masai School and Interview Kickstart FDE posting analyses. See [Sources](/sources).</small>
