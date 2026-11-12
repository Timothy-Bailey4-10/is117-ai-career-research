# AI Career Research

🌐 **Live site:** https://timothy-bailey4-10.github.io/is117-ai-career-research/

A concise guide to in-demand AI jobs, centered on the **Forward Deployed Engineer (FDE)** and the roles around it: Applied AI Engineer, Solutions Engineer, AI Engineer, Agent Engineer, and more.

Built with [VitePress](https://vitepress.dev) and deployed automatically to GitHub Pages.

## What's inside

| Page | What it covers |
|---|---|
| [Forward Deployed Engineer](https://timothy-bailey4-10.github.io/is117-ai-career-research/roles/forward-deployed-engineer) | The main guide: work, pay, interviews, how to break in |
| [Similar roles](https://timothy-bailey4-10.github.io/is117-ai-career-research/roles/) | FDE family + builder roles, side by side |
| [Find the jobs](https://timothy-bailey4-10.github.io/is117-ai-career-research/job-search) | Search terms, where to look, posting checklist |
| [AI Engineer](https://timothy-bailey4-10.github.io/is117-ai-career-research/roles/ai-engineer) | Building products on top of LLMs |
| [Agent Engineer](https://timothy-bailey4-10.github.io/is117-ai-career-research/roles/agent-engineer) | Tool-using AI agents |
| [Skills in demand](https://timothy-bailey4-10.github.io/is117-ai-career-research/skills) | What job postings actually ask for |
| [Student roadmap](https://timothy-bailey4-10.github.io/is117-ai-career-research/roadmap) | Four stages from foundations to internships |

## Run it on your computer

```bash
npm install          # install VitePress
npm run docs:dev     # open http://localhost:5173/is117-ai-career-research/
```

## Project layout

```
ai-career-research/
├── .github/workflows/deploy.yml   ← builds + publishes to GitHub Pages
├── docs/
│   ├── .vitepress/config.mts      ← site title, menu, sidebar
│   ├── index.md                   ← home page
│   ├── roles/                     ← one page per job title
│   ├── skills.md
│   ├── roadmap.md
│   └── sources.md
└── package.json
```

## Add a new role

1. Create `docs/roles/your-role-name.md`.
2. Add it to the `sidebar` in `docs/.vitepress/config.mts`.
3. Commit and push to `main` — the site updates in about a minute.

## How deployment works

Every push to `main` runs the **Deploy VitePress site to Pages** workflow in the Actions tab. It builds the site and publishes it to the live link above.

---

Research compiled November 2026. Pay figures are reported ranges — always check the live job posting.
