# Skills Required

What you need to get hired as a **Forward Deployed Engineer** and in the roles around it, and how to prove each skill.

## What FDE postings ask for

From Bloomberry's analysis of ~1,000 FDE job postings (2026). Click a percentage to see its source sentence:

<div class="bars">
  <div class="bar"><span>Python</span><div class="track"><div class="fill" style="width:66%"></div></div><span class="pct">66% {{b_python}}</span></div>
  <div class="bar"><span>AI agents</span><div class="track"><div class="fill" style="width:35%"></div></div><span class="pct">35% {{b_agents}}</span></div>
  <div class="bar"><span>TypeScript</span><div class="track"><div class="fill" style="width:35%"></div></div><span class="pct">35% {{b_ts}}</span></div>
  <div class="bar"><span>AWS</span><div class="track"><div class="fill" style="width:32%"></div></div><span class="pct">32% {{b_cloud}}</span></div>
  <div class="bar"><span>LLM experience</span><div class="track"><div class="fill" style="width:31%"></div></div><span class="pct">31% {{b_llm}}</span></div>
  <div class="bar"><span>GCP</span><div class="track"><div class="fill" style="width:22%"></div></div><span class="pct">22% {{b_cloud}}</span></div>
  <div class="bar"><span>Azure</span><div class="track"><div class="fill" style="width:18%"></div></div><span class="pct">18% {{b_cloud}}</span></div>
</div>

A separate review of 14 active FDE postings (August 2026) found the most common requirements were **production coding, stakeholder communication, customer discovery, AI or agent development, integrations, and adoption ownership** {{ik_req}}.

## FDE skills checklist

### Technical

| Skill | Evidence it's required | How to prove it* |
|---|---|---|
| **Production coding** (Python / TypeScript) | 12 of 14 postings {{ik_req}} · Python 66% {{b_python}} | A public repo with a deployed app |
| **APIs & integrations** | "The common thread is integration work" {{m_int}} | A project that pulls from a real third-party API |
| **LLMs & agents** | AI agents 35%, LLM experience 31% {{b_agents}} | An agent that completes a real task end-to-end |
| **Evals** | Recur in the better-specified postings {{m_evals}} | An eval dataset and failure categories in your README {{ik_proj}} |
| **Cloud** | AWS 32%, GCP 22%, Azure 18% {{b_cloud}} | Your project running at a public URL |

### People (what makes an FDE different)

| Skill | Evidence it's required | How to prove it* |
|---|---|---|
| **Customer discovery & scoping** | OpenAI lists discovery and technical scoping {{m_disc}} | A write-up of the user problem you solved |
| **Stakeholder communication** | Among the most common requirements {{ik_req}} | A 5-minute demo video and a one-page summary |
| **Owning adoption** | Success measured through production adoption {{m_adopt}} | Usage numbers from your real users |
| **Handling ambiguity** | Tested in the case-study interview stage {{ph_loop}} | Your project's "v1 vs later" scoping decisions |

<small>*"How to prove it" is this site's advice, not taken from a source.</small>

## Skills by role

How much each similar role relies on each skill area. **This is this site's own summary of the role descriptions, not survey data.**

| Skill | FDE | Applied AI Eng. | Solutions Eng. | AI Engineer | Agent Engineer | AI Eval Eng. |
|---|---|---|---|---|---|---|
| Production coding | ●●● | ●●● | ●● | ●●● | ●●● | ●● |
| APIs & integrations | ●●● | ●●● | ●● | ●● | ●●● | ● |
| LLMs & agents | ●●● | ●●● | ●● | ●●● | ●●● | ●● |
| Evals | ●● | ●●● | ● | ●● | ●● | ●●● |
| Customer communication | ●●● | ●●● | ●●● | ● | ● | ● |
| Demos & presenting | ●●● | ●● | ●●● | ● | ● | ● |

<small>●●● core · ●● expected · ● nice to have</small>

## One project that covers almost everything

Build **one AI agent for a real user** (a club, small business, or professor):

1. **Discover**: interview them and write down the workflow
2. **Build**: an agent in Python or TypeScript that calls their real tools or data
3. **Deploy**: put it at a public URL on AWS or similar
4. **Measure**: write an evaluation dataset, success criteria, and failure categories {{ik_proj}}
5. **Present**: record a 5-minute demo and write a one-page summary
