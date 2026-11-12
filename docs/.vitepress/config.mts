import { defineConfig } from 'vitepress'

// The site is served from https://timothy-bailey4-10.github.io/is117-ai-career-research/
// so every link needs the repo name as its base path.
export default defineConfig({
  base: '/is117-ai-career-research/',
  title: 'AI Career Research',
  description: 'A concise guide to Forward Deployed Engineer and other in-demand AI jobs.',
  lastUpdated: true,
  cleanUrls: true,

  head: [
    ['meta', { name: 'theme-color', content: '#6d4aff' }]
  ],

  themeConfig: {
    nav: [
      { text: 'FDE', link: '/roles/forward-deployed-engineer' },
      { text: 'Similar roles', link: '/roles/' },
      { text: 'Skills', link: '/skills' },
      { text: 'Find jobs', link: '/job-search' },
      { text: 'Roadmap', link: '/roadmap' }
    ],

    sidebar: [
      {
        text: 'Forward Deployed Engineer',
        items: [
          { text: 'FDE guide', link: '/roles/forward-deployed-engineer' },
          { text: 'Skills required', link: '/skills' },
          { text: 'Find the jobs', link: '/job-search' }
        ]
      },
      {
        text: 'Similar roles',
        items: [
          { text: 'Compare all roles', link: '/roles/' },
          { text: 'AI Engineer', link: '/roles/ai-engineer' },
          { text: 'Agent Engineer', link: '/roles/agent-engineer' },
          { text: 'AI Evaluation Engineer', link: '/roles/ai-evaluation-engineer' },
          { text: 'AI Operations (LLMOps)', link: '/roles/ai-operations' }
        ]
      },
      {
        text: 'Other AI roles',
        collapsed: true,
        items: [
          { text: 'AI Product Manager', link: '/roles/ai-product-manager' },
          { text: 'AI Trainer', link: '/roles/ai-trainer' },
          { text: 'AI Trust & Safety', link: '/roles/ai-trust-safety' }
        ]
      },
      {
        text: 'Getting there',
        items: [
          { text: 'Student roadmap', link: '/roadmap' },
          { text: 'Sources', link: '/sources' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Timothy-Bailey4-10/is117-ai-career-research' }
    ],

    search: { provider: 'local' },

    editLink: {
      pattern: 'https://github.com/Timothy-Bailey4-10/is117-ai-career-research/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },

    footer: {
      message: 'Research compiled November 2026. Pay figures are reported ranges — always check the live job posting.',
      copyright: '© 2026 Timothy Bailey'
    }
  }
})
