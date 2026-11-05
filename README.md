# AI Career Research

🌐 **Live site:** https://timothybailey4-10.github.io/ai-career-research/

A field guide to the new jobs in the AI industry — **Forward Deployed Engineer, AI Engineer, Agent Engineer, AI Evaluation Engineer**, and more. Each role page covers what the job is, what a week looks like, the skills employers ask for, reported pay, and concrete first steps for students.

Built with [VitePress](https://vitepress.dev) and deployed automatically to GitHub Pages.

## What's inside

| Page | What it covers |
|---|---|
| [Roles overview](https://timothybailey4-10.github.io/ai-career-research/roles/) | How the roles connect + side-by-side comparison |
| [Forward Deployed Engineer](https://timothybailey4-10.github.io/ai-career-research/roles/forward-deployed-engineer) | Embedding with customers to ship AI |
| [AI Engineer](https://timothybailey4-10.github.io/ai-career-research/roles/ai-engineer) | Building products on top of LLMs |
| [Agent Engineer](https://timothybailey4-10.github.io/ai-career-research/roles/agent-engineer) | Tool-using AI agents |
| [Skills in demand](https://timothybailey4-10.github.io/ai-career-research/skills) | What job postings actually ask for |
| [Student roadmap](https://timothybailey4-10.github.io/ai-career-research/roadmap) | Four stages from foundations to internships |

## Run it on your computer

```bash
npm install          # install VitePress
npm run docs:dev     # open http://localhost:5173/ai-career-research/
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
