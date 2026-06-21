// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Andy's World deploys as a GitHub Pages *project* site:
//   https://WorkWebsitesMixed.github.io/andys-world
// so `site` is the user/org domain and `base` is the repo path.
// Internal links must go through src/lib/url.ts so the base path is applied.
export default defineConfig({
  site: 'https://WorkWebsitesMixed.github.io',
  base: '/andys-world',
  trailingSlash: 'ignore',
  integrations: [mdx(), sitemap()],
});
