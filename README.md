# AI Career Research

### 🌐 [View the site → timothy-bailey4-10.github.io/is117-ai-career-research](https://timothy-bailey4-10.github.io/is117-ai-career-research/)

A concise guide to in-demand AI jobs, centered on the **Forward Deployed Engineer (FDE)** and the roles around it: Applied AI Engineer, Solutions Engineer, AI Engineer, Agent Engineer, and more. Each fact on the FDE pages links to the exact sentence in its source.

Built with [VitePress](https://vitepress.dev) and deployed automatically to GitHub Pages.

## Pages

| Page | What it covers |
|---|---|
| [Forward Deployed Engineer](https://timothy-bailey4-10.github.io/is117-ai-career-research/roles/forward-deployed-engineer) | The main guide: work, pay, who's hiring, interviews, how to break in |
| [Similar roles](https://timothy-bailey4-10.github.io/is117-ai-career-research/roles/) | FDE family and builder roles, side by side |
| [Skills required](https://timothy-bailey4-10.github.io/is117-ai-career-research/skills) | What postings ask for, an FDE skills checklist, and skills by role |
| [Find the jobs](https://timothy-bailey4-10.github.io/is117-ai-career-research/job-search) | Search terms, companies to check, and a posting checklist |
| [Student roadmap](https://timothy-bailey4-10.github.io/is117-ai-career-research/roadmap) | Four stages from foundations to internships |
| [Sources](https://timothy-bailey4-10.github.io/is117-ai-career-research/sources) | Every source and what it supports |

## Run it locally

```bash
npm install
npm run docs:dev     # http://localhost:5173/is117-ai-career-research/
```

## Edit and publish

```bash
# If you edited a cited page, edit its template in scripts/citations/templates/ and regenerate:
python3 scripts/citations/cite.py scripts/citations/templates docs

git add -A
git commit -m "Describe your change"
git push origin main   # the site redeploys in about a minute
```

## Project layout

```
├── .github/workflows/deploy.yml   ← builds and publishes to GitHub Pages
├── docs/
│   ├── .vitepress/config.mts      ← site title, menu, sidebar
│   ├── index.md                   ← home page
│   ├── roles/                     ← one page per job title
│   ├── skills.md · job-search.md · roadmap.md · sources.md
├── scripts/citations/             ← citation templates + verified quote map
└── package.json
```

---

Research compiled November 2026. Pay figures are reported ranges, so always check the live job posting.
