/**
 * Build an internal href that respects the configured `base` path
 * (e.g. "/andys-world"). Always use this for site-internal links so the
 * project deploys correctly to GitHub Pages.
 *
 *   url()                 -> "/andys-world/"
 *   url('grade/11')       -> "/andys-world/grade/11"
 *   url('/grade/11')      -> "/andys-world/grade/11"
 */
const BASE = import.meta.env.BASE_URL; // e.g. "/andys-world/" (trailing slash)

export function url(path: string = ''): string {
  const joined = `${BASE}/${path}`.replace(/\/{2,}/g, '/');
  // keep a single trailing slash only for the root
  if (path === '' || path === '/') return joined.endsWith('/') ? joined : `${joined}/`;
  return joined.replace(/\/$/, '');
}

/** Convenience builders for the grade → term → week hierarchy. */
export const routes = {
  home: () => url(),
  grade: (g: number | string) => url(`grade/${g}`),
  term: (g: number | string, t: number | string) => url(`grade/${g}/term/${t}`),
  week: (g: number | string, t: number | string, w: number | string) =>
    url(`grade/${g}/term/${t}/week/${w}`),
  igcse: (g: number | string) => url(`grade/${g}/igcse`),
  project: (g: number | string) => url(`grade/${g}/project`),
  paper1: (g: number | string) => url(`grade/${g}/paper-1`),
  paper4: (g: number | string) => url(`grade/${g}/paper-4`),

  /** Extracurricular courses: course → sprint → week. */
  extracurricular: () => url('extracurricular'),
  course: (c: string) => url(`course/${c}`),
  sprint: (c: string, s: number | string) => url(`course/${c}/sprint/${s}`),
  session: (c: string, s: number | string, w: number | string) =>
    url(`course/${c}/sprint/${s}/week/${w}`),
};
