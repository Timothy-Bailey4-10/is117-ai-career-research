import { defineConfig } from 'vitepress'

// The site is served from https://timothybailey4-10.github.io/ai-career-research/
// so every link needs the repo name as its base path.
export default defineConfig({
  base: '/ai-career-research/',
  title: 'AI Career Research',
  description: 'A field guide to the new jobs in the AI industry — what they are, what they pay, and how to break in.',
  lastUpdated: true,
  cleanUrls: true,

  head: [
    ['meta', { name: 'theme-color', content: '#6d4aff' }]
  ],

  themeConfig: {
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Roles', link: '/roles/' },
      { text: 'Skills', link: '/skills' },
      { text: 'Roadmap', link: '/roadmap' },
      { text: 'Sources', link: '/sources' }
    ],

    sidebar: [
      {
        text: 'Start here',
        items: [
          { text: 'Overview', link: '/roles/' },
          { text: 'Compare all roles', link: '/roles/#compare-the-roles' }
        ]
      },
      {
        text: 'Building AI',
        items: [
          { text: 'AI Engineer', link: '/roles/ai-engineer' },
          { text: 'Forward Deployed Engineer', link: '/roles/forward-deployed-engineer' },
          { text: 'Agent Engineer', link: '/roles/agent-engineer' },
          { text: 'AI Evaluation Engineer', link: '/roles/ai-evaluation-engineer' },
          { text: 'AI Operations (LLMOps)', link: '/roles/ai-operations' }
        ]
      },
      {
        text: 'Shaping AI',
        items: [
          { text: 'AI Product Manager', link: '/roles/ai-product-manager' },
          { text: 'AI Trainer', link: '/roles/ai-trainer' },
          { text: 'AI Trust & Safety', link: '/roles/ai-trust-safety' }
        ]
      },
      {
        text: 'Getting there',
        items: [
          { text: 'Skills in demand', link: '/skills' },
          { text: 'Student roadmap', link: '/roadmap' },
          { text: 'Sources', link: '/sources' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/TimothyBailey4-10/ai-career-research' }
    ],

    search: { provider: 'local' },

    editLink: {
      pattern: 'https://github.com/TimothyBailey4-10/ai-career-research/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },

    footer: {
      message: 'Research compiled November 2026. Pay figures are reported ranges — always check the live job posting.',
      copyright: '© 2026 Timothy Bailey'
    }
  }
})
