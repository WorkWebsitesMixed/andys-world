/**
 * The structural backbone of the site: Grade → Term → Week.
 *
 * This describes the *architecture* (which grades/terms/weeks exist and their
 * status). Actual lesson titles and content live in the `lessons` content
 * collection (src/content/lessons) and are looked up by grade/term/week.
 */

export type GradeStatus = 'active' | 'placeholder';

/**
 * Route keys that resolve to a grade-scoped page via routes[key](gradeId).
 * Extend this union when new per-grade reference pages are added.
 */
export type HubRouteKey = 'igcse' | 'project' | 'paper1' | 'paper4';

/** "Start here" banner shown at the top of a grade landing page. */
export interface GradeHub {
  routeKey: HubRouteKey;
  /** Short label above the title, e.g. "Start here". */
  eyebrow: string;
  /** Banner heading, e.g. "Your IGCSE". */
  title: string;
  /** One-sentence description of what the hub page covers. */
  blurb: string;
}

export interface GradeInfo {
  id: number;
  name: string;
  /** Short subject label shown on cards. */
  subject: string;
  /** One-line description for the grade landing page. */
  blurb: string;
  status: GradeStatus;
  /** Optional hub-page banner. When set, renders a prominent link at the top of the grade landing. */
  hub?: GradeHub;
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
    hub: {
      routeKey: 'igcse',
      eyebrow: 'Start here',
      title: 'Your IGCSE',
      blurb:
        'How your grade works — Paper 1, Paper 4 and your year-long project. Read this once, and come back whenever a lesson mentions a paper or a criterion.',
    },
  },
  {
    id: 12,
    name: 'Grade 12',
    subject: 'ICT & Programming',
    blurb: 'IGCSE ICT exam preparation and an introduction to programming.',
    status: 'active',
  },
];

export const TERMS = [1, 2, 3] as const;
export type TermId = (typeof TERMS)[number];

export const WEEKS_PER_TERM = 10;

/** Per-grade, per-term week-count overrides (when a term runs longer than 10 weeks). */
const WEEKS_OVERRIDE: Partial<Record<number, Partial<Record<TermId, number>>>> = {
  12: { 1: 12 },
};

export function weeksForTerm(term: number, grade?: number): number[] {
  const override = grade !== undefined ? WEEKS_OVERRIDE[grade]?.[term as TermId] : undefined;
  const count = override ?? WEEKS_PER_TERM;
  return Array.from({ length: count }, (_, i) => i + 1);
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
    1: {
      title: 'Exam Prep & LaTeX',
      blurb:
        'Block A: IGCSE ICT Papers 1–3 exam preparation (7 weeks). Block B: LaTeX for Chemistry lab reports in Overleaf (5 weeks).',
    },
    2: { title: 'Term 2', blurb: 'Not yet planned — coming later.', planned: false },
    3: { title: 'Introduction to Programming', blurb: 'A first course in programming.' },
  },
};

export function getTermFocus(grade: number | string, term: number): TermFocus | undefined {
  return TERM_FOCUS[Number(grade)]?.[term as TermId];
}
