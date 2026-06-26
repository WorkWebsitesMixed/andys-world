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

/**
 * The `sessions` collection. One .mdx file = one extracurricular class session.
 * Routing is derived from courseId/sprint/week frontmatter.
 * Convention: src/content/sessions/<courseId>/s<sprint>-w<week>.mdx
 */
const sessions = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/sessions' }),
  schema: z.object({
    courseId: z.string(),
    sprint: z.number().int().min(1),
    week: z.number().int().min(1),
    title: z.string(),
    /** Short topic tag shown on sprint overview cards. */
    topic: z.string(),
    /** The main concept or technique introduced this session. */
    coreSkill: z.string(),
    /** One sentence: what the student builds or achieves by the end. */
    payoff: z.string(),
    learningGoals: z.array(z.string()),
    /** Python files shipped with this session (served from /python/). */
    files: z
      .array(
        z.object({
          filename: z.string(),
          label: z.string(),
        }),
      )
      .default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { lessons, sessions };
