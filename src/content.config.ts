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
    week: z.number().int().min(1).max(24),
    /** 'b' = a separate, mandatory weekly session distinct from the main class
     *  (e.g. G11 T3's 45-min enrichment block, G12's B sessions) — not optional. */
    sessionType: z.enum(['main', 'b']).default('main'),
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

/**
 * The `blocks` collection. One .mdx file = one block in a block-structured course.
 * Routing: /course/[courseId]/block/[blockId]
 * Convention: src/content/blocks/<courseId>/block-<id>.mdx
 */
const blocks = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/blocks' }),
  schema: z.object({
    courseId: z.string(),
    blockId: z.string(),
    draft: z.boolean().default(false),
  }),
});

/**
 * The `skills` collection. One .mdx file = one 45-min SKILLS enrichment card.
 * SKILLS is the optional, ungraded near-peer TA / advanced-enrichment strand
 * for the Grade 11 (Systems & Control) cohort — each card maps 1:1 to that
 * week's regular G11 topic. Routing: /skills/term/[term]/[code].
 * Convention: src/content/skills/term-<term>/<code>.mdx (e.g. term-1/sk1.mdx).
 */
const skills = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/skills' }),
  schema: z.object({
    term: z.enum(['1', '2', '3', 'revision']),
    /** Card code as used in the source docs, e.g. "SK1", "SR1". */
    code: z.string(),
    /** Position within the term, for ordering and prev/next. */
    order: z.number().int(),
    /** The regular Grade 11 week this card previews (1:1 mapping). */
    mapsToWeek: z.number().int(),
    title: z.string(),
    /** Short tagline shown under the title. */
    hook: z.string(),
    /** Extra flags shown as pills, e.g. "project-lock session", "key TA week". */
    badges: z.array(z.string()).default([]),
    /** "By the end of the session I will…" — go-deeper goal. */
    masteryGoal: z.string(),
    /** "By the end of the session I will…" — TA/leadership prep goal. */
    tutorGoal: z.string(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { lessons, sessions, blocks, skills };
