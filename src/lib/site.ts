/**
 * Global site configuration for Andy's World.
 * Edit these values rather than hard-coding them in components.
 */
export const site = {
  name: "Andy's World",
  tagline: 'Design & Technology · innovation · physics · making',
  author: 'Andrés Forero',
  role: 'Head of Design & Technology — Marymount School, Medellín',
  description:
    "Student-facing Design & Technology lessons by Andrés Forero — organised by grade, term and week.",

  /**
   * Link out to Andy's separate exam-grader project.
   * Currently the preview build; swap for the production URL when confirmed.
   */
  examsUrl: 'https://workwebsitesmixed.github.io/exam-grader-v2-preview/',
  examsLabel: 'Exams',
} as const;
