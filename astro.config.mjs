// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// Andy's World deploys as a GitHub Pages *project* site:
//   https://WorkWebsitesMixed.github.io/andys-world
// so `site` is the user/org domain and `base` is the repo path.
// Internal links must go through src/lib/url.ts so the base path is applied.
export default defineConfig({
  site: 'https://WorkWebsitesMixed.github.io',
  base: '/andys-world',
  trailingSlash: 'ignore',
  integrations: [mdx(), sitemap()],
  // Maths in lesson prose: `$...$` inline, `$$...$$` display. Rendered to static
  // MathML + HTML at build time — no client-side JS. The KaTeX stylesheet is loaded
  // by LessonLayout only, so non-lesson pages don't pay for it.
  // For the equation → substitution → result pattern, use <Formula> instead.
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [[rehypeKatex, { throwOnError: false, strict: false }]],
  },
});
