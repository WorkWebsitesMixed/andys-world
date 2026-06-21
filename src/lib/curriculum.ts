/**
 * The structural backbone of the site: Grade → Term → Week.
 *
 * This describes the *architecture* (which grades/terms/weeks exist and their
 * status). Actual lesson titles and content live in the `lessons` content
 * collection (src/content/lessons) and are looked up by grade/term/week.
 */

export type GradeStatus = 'active' | 'placeholder';

export interface GradeInfo {
  id: number;
  name: string;
  /** Short subject label shown on cards. */
  subject: string;
  /** One-line description for the grade landing page. */
  blurb: string;
  status: GradeStatus;
}

export const GRADES: GradeInfo[] = [
  {
    id: 10,
    name: 'Grade 10',
    subject: 'Materials',
    blurb: 'The Materials cohort — properties, processes and sustainable design.',
    status: 'placeholder',
  },
  {
    id: 11,
    name: 'Grade 11',
    subject: 'Systems & Control',
    blurb:
      'Systems & Control with Structures as the coursework focus — the IGCSE route we are teaching in full.',
    status: 'active',
  },
  {
    id: 12,
    name: 'Grade 12',
    subject: 'ICT & Programming',
    blurb: 'IGCSE ICT review and an introduction to programming.',
    status: 'placeholder',
  },
];

export const TERMS = [1, 2, 3] as const;
export type TermId = (typeof TERMS)[number];

/** Every term runs 10 weeks. In Term 3, Week 10 is a "Project Review". */
export const WEEKS_PER_TERM = 10;

export function weeksForTerm(_term: number): number[] {
  return Array.from({ length: WEEKS_PER_TERM }, (_, i) => i + 1);
}

export function termLabel(term: number): string {
  return `Term ${term}`;
}

/** Default week heading used before a lesson is authored for that slot. */
export function defaultWeekTitle(_term: number, week: number): string {
  return `Week ${week}`;
}

export function getGrade(id: number | string): GradeInfo | undefined {
  return GRADES.find((g) => g.id === Number(id));
}

/** Optional focus for a term on a placeholder grade (so stubs show their scope). */
export interface TermFocus {
  /** Overrides the plain "Term N" focus label on cards. */
  title?: string;
  /** One-line description of what the term will cover. */
  blurb: string;
  /** false = deliberately empty / not yet planned. */
  planned?: boolean;
}

/**
 * Per-grade, per-term focus for the placeholder grades. Active grades (with
 * authored lessons) derive their structure from the lessons themselves.
 */
export const TERM_FOCUS: Record<number, Partial<Record<TermId, TermFocus>>> = {
  12: {
    1: { title: 'IGCSE ICT Review', blurb: 'Reviewing the core IGCSE ICT topics.' },
    2: { title: 'Term 2', blurb: 'Not yet planned — coming later.', planned: false },
    3: { title: 'Introduction to Programming', blurb: 'A first course in programming.' },
  },
};

export function getTermFocus(grade: number | string, term: number): TermFocus | undefined {
  return TERM_FOCUS[Number(grade)]?.[term as TermId];
}
