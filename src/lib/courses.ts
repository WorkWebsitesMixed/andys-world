/**
 * Extracurricular course registry — parallel to curriculum.ts but for
 * after-school courses that are not tied to a specific grade.
 *
 * Two structural patterns:
 *   'sprint' — Course → Sprint → Week (Python: individual session pages)
 *   'block'  — Course → Block (Mechatronics: one rich page per block)
 */

export interface SprintInfo {
  id: number;
  name: string;
  /** Week numbers that belong to this sprint (global, 1-based across the course). */
  weeks: number[];
  /** CSS colour for sprint accent badges. */
  color: string;
}

export interface BlockInfo {
  id: string;
  /** Short display label, e.g. "Block 1A". */
  label: string;
  name: string;
  weekRange: [number, number];
  classRange: [number, number];
  /** CSS colour for block accent badges. */
  color: string;
  /** One sentence: what the student builds and demos at the end. */
  deliverable: string;
}

export type CourseInfo =
  | {
      id: string;
      name: string;
      tagline: string;
      blurb: string;
      structure: 'sprint';
      sprints: SprintInfo[];
    }
  | {
      id: string;
      name: string;
      tagline: string;
      blurb: string;
      structure: 'block';
      blocks: BlockInfo[];
    };

export const COURSES: CourseInfo[] = [
  {
    id: 'python',
    name: 'Python Programming',
    tagline: 'From zero to your own AI-powered tool in 27 weeks.',
    blurb:
      'A project-driven introduction to Python for students who want to build real things — games, AI assistants, automation tools. No lectures; code from session one.',
    structure: 'sprint',
    sprints: [
      { id: 1, name: 'The Game Lab',       weeks: [1,2,3,4,5,6,7],       color: '#10783c' },
      { id: 2, name: 'The AI Lab',         weeks: [8,9,10,11,12,13,14],   color: '#5a32a0' },
      { id: 3, name: 'The Automation Lab', weeks: [15,16,17,18,19,20,21], color: '#be5a0a' },
      { id: 4, name: 'The Final Showcase', weeks: [22,23,24,25,26,27],    color: '#966400' },
    ],
  },
  {
    id: 'mechatronics',
    name: 'Mechatronics',
    tagline: 'ESP32 · C++ · 3D Printing · IoT — 30 weeks, 60 classes.',
    blurb:
      'A two-phase practical engineering programme. Phase 1: build and race real RC vehicles. Phase 2: build internet-connected devices that solve real problems — culminating in an individual smart safe with a three-stage puzzle.',
    structure: 'block',
    blocks: [
      {
        id: '1a',
        label: 'Block 1A',
        name: 'Da Vinci Paddle Boat',
        weekRange: [1, 5],
        classRange: [1, 10],
        color: '#005aa0',
        deliverable: 'A single-motor RC paddle boat that races on a lake, controlled by a Bluetooth gamepad.',
      },
      {
        id: '1b',
        label: 'Block 1B',
        name: 'RoboJam Adaptation',
        weekRange: [6, 10],
        classRange: [11, 20],
        color: '#a01e1e',
        deliverable: 'Two competition-ready RC robots — Disk Derby (20×20 cm) and Path Attack Pro (15×15 cm) — raced on Competition Day.',
      },
      {
        id: '2a',
        label: 'Block 2A',
        name: 'IoT Mini-Builds',
        weekRange: [11, 14],
        classRange: [21, 28],
        color: '#10783c',
        deliverable: 'Three standalone IoT devices: a Telegram alert bot, a web-controlled mood lamp, and an auto plant waterer.',
      },
      {
        id: '2b',
        label: 'Block 2B',
        name: 'Level-2 IoT Project',
        weekRange: [15, 20],
        classRange: [29, 40],
        color: '#006e8c',
        deliverable: 'One fully assembled, cloud-connected device chosen by class vote: Smart Pet Feeder, Smart Locker, or IoT Vending Machine.',
      },
      {
        id: '2c',
        label: 'Block 2C',
        name: 'Crack-the-Code Safe',
        weekRange: [21, 28],
        classRange: [41, 56],
        color: '#5a32a0',
        deliverable: 'Individual 3D-printed smart safe with three sequential puzzle stages, Telegram hints, and an hourly-changing NTP-synced access code.',
      },
      {
        id: '2d',
        label: 'Block 2D',
        name: 'Demo Day',
        weekRange: [29, 30],
        classRange: [57, 60],
        color: '#966400',
        deliverable: 'Public demo event for parents, peers, and school administration — each student presents her safe and earlier portfolio projects.',
      },
    ],
  },
];

export function getCourse(id: string): CourseInfo | undefined {
  return COURSES.find((c) => c.id === id);
}

/** Sprint-based helpers */
export function getSprint(course: CourseInfo, sprintId: number): SprintInfo | undefined {
  if (course.structure !== 'sprint') return undefined;
  return course.sprints.find((s) => s.id === sprintId);
}

export function getSprintForWeek(course: CourseInfo, week: number): SprintInfo | undefined {
  if (course.structure !== 'sprint') return undefined;
  return course.sprints.find((s) => s.weeks.includes(week));
}

/** Block-based helpers */
export function getBlock(course: CourseInfo, blockId: string): BlockInfo | undefined {
  if (course.structure !== 'block') return undefined;
  return course.blocks.find((b) => b.id === blockId);
}
