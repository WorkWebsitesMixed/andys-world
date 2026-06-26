/**
 * Extracurricular course registry — parallel to curriculum.ts but for
 * after-school courses that are not tied to a specific grade.
 * Structure: Course → Sprint → Week (analogous to Grade → Term → Week).
 */

export interface SprintInfo {
  id: number;
  name: string;
  /** Week numbers that belong to this sprint (global, 1-based across the course). */
  weeks: number[];
  /** CSS colour for sprint accent badges. */
  color: string;
}

export interface CourseInfo {
  id: string;
  name: string;
  tagline: string;
  blurb: string;
  sprints: SprintInfo[];
}

export const COURSES: CourseInfo[] = [
  {
    id: 'python',
    name: 'Python Programming',
    tagline: 'From zero to your own AI-powered tool in 27 weeks.',
    blurb:
      'A project-driven introduction to Python for students who want to build real things — games, AI assistants, automation tools. No lectures; code from session one.',
    sprints: [
      { id: 1, name: 'The Game Lab',        weeks: [1,2,3,4,5,6,7],            color: '#10783c' },
      { id: 2, name: 'The AI Lab',          weeks: [8,9,10,11,12,13,14],        color: '#5a32a0' },
      { id: 3, name: 'The Automation Lab',  weeks: [15,16,17,18,19,20,21],      color: '#be5a0a' },
      { id: 4, name: 'The Final Showcase',  weeks: [22,23,24,25,26,27],         color: '#966400' },
    ],
  },
];

export function getCourse(id: string): CourseInfo | undefined {
  return COURSES.find((c) => c.id === id);
}

export function getSprintForWeek(course: CourseInfo, week: number): SprintInfo | undefined {
  return course.sprints.find((s) => s.weeks.includes(week));
}

export function getSprint(course: CourseInfo, sprintId: number): SprintInfo | undefined {
  return course.sprints.find((s) => s.id === sprintId);
}
