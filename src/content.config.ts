import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

/**
 * The `lessons` collection. One .mdx file = one class.
 *
 * Routing is derived from the `grade`/`term`/`week` frontmatter (not the file
 * path), so files can be organised however is convenient on disk. The
 * convention is src/content/lessons/grade-<n>/t<term>-w<week>.mdx.
 *
 * Frontmatter mirrors §3 of the rebuild brief.
 */
const lessons = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/lessons' }),
  schema: z.object({
    grade: z.number().int(),
    term: z.number().int().min(1).max(3),
    week: z.number().int().min(1).max(20),
    sessionType: z.enum(['main', 'bonus']).default('main'),
    title: z.string(),
    /** Single topic tag, e.g. "Structures". */
    topic: z.string(),
    /** "By the end of this class I will…" — cognitive goal (Mager ABCD). */
    learningGoal: z.string(),
    /** "By the end of this class I will…" — social/emotional goal. */
    selGoal: z.string(),
    /** Hidden from navigation and excluded from production builds when true. */
    draft: z.boolean().default(false),
  }),
});

export const collections = { lessons };
