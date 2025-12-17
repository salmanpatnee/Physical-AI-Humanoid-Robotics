import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import sidebars from './sidebars';

function getModuleLinks() {
  // Hardcoded module links for reliability
  // These link to the first chapter of each module
  // Note: Docusaurus strips number prefixes from filenames when generating URLs
  return [
    {
      label: 'The Robotic Nervous System',
      to: '/docs/module1-robotic-nervous-system/focus-middleware-for-robot-control',
    },
    {
      label: 'The Digital Twin',
      to: '/docs/module2-the-digital-twin/focus-physics-simulation-and-world-building',
    },
    {
      label: 'The AI-Robot Brain',
      to: '/docs/module3-ai-robot-brain/focus-advanced-perception-and-synthetic-data',
    },
    {
      label: 'Vision-Language-Action',
      to: '/docs/module4-vision-language-action/focus-the-convergence-of-llms-and-robotics',
    },
  ];
}

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Teaching Physical AI & Humanoid Robotics Course',
  tagline: 'Physical AI, ROS2, Isaac Sim, VLA — coursebook',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  // Use Vercel URL in production, localhost for development
  url: process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : 'http://localhost:3000',
  // Set the /<baseUrl>/ pathname under which your site is served
  // Root path for Vercel, subdirectory for GitHub Pages if needed
  baseUrl: process.env.VERCEL ? '/' : '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'salmanpatnee', // Usually your GitHub org/user name.
  projectName: 'Physical-AI-Humanoid-Robotics', // Usually your repo name.

  onBrokenLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
          // Useful options to enforce blogging best practices
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    './src/plugins/chapter-validation',
    './src/plugins/chatbot-config',
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'dark',
      disableSwitch: false,
      respectPrefersColorScheme: false,
    },
    navbar: {
      title: 'Physical AI Humanoid Robotics',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'bookSidebar',
          position: 'left',
          label: 'Book',
        },
        // {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learn',
          items: [
            ...getModuleLinks(),
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Discussions',
              href: 'https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics/discussions',
            },
            {
              label: 'Issues',
              href: 'https://github.com/salmanpatnee/Physical-AI-Humanoid-Robotics/issues',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI Humanoid Robotics. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
