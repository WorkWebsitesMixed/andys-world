import { getCollection, type CollectionEntry } from 'astro:content';

export type Lesson = CollectionEntry<'lessons'>;

const isProd = import.meta.env.PROD;

/**
 * All published lessons. Drafts are hidden in production builds but visible
 * during local development so work-in-progress can be previewed.
 */
export async function getLessons(): Promise<Lesson[]> {
  const all = await getCollection('lessons');
  return all.filter((l) => !isProd || l.data.draft !== true);
}

/** Find the single lesson for a grade/term/week slot, if one exists. */
export async function getLesson(
  grade: number,
  term: number,
  week: number,
): Promise<Lesson | undefined> {
  const all = await getLessons();
  return all.find(
    (l) => l.data.grade === grade && l.data.term === term && l.data.week === week,
  );
}

/** Lessons for a given grade+term, ordered by week. */
export async function getTermLessons(grade: number, term: number): Promise<Lesson[]> {
  const all = await getLessons();
  return all
    .filter((l) => l.data.grade === grade && l.data.term === term)
    .sort((a, b) => a.data.week - b.data.week);
}

/** Does this grade have any authored lessons yet? */
export async function gradeHasLessons(grade: number): Promise<boolean> {
  const all = await getLessons();
  return all.some((l) => l.data.grade === grade);
}
