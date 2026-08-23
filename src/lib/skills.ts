/**
 * SKILLS enrichment registry — parallel to curriculum.ts/courses.ts but for
 * the optional, ungraded near-peer TA / advanced-enrichment strand.
 *
 * ~18 advanced Grade 11 (Systems & Control) students, 45 min/week before
 * their regular slot. Each card previews and deepens that week's regular
 * G11 topic 1:1, then trains the group to TA it in the regular class.
 *
 * Card content (goals, preview, deepen, taste beyond, TA prep, challenge,
 * run sheet) lives in the `skills` content collection, one .mdx per card.
 * This file holds only what isn't derivable from that content: which terms
 * exist, their framing copy, and which G11 term/week each maps into.
 */

export type SkillsTermId = '1' | '2' | '3' | 'revision';

export interface SkillsTermInfo {
  id: SkillsTermId;
  label: string;
  /** Short status line shown on the /skills landing card. */
  eyebrow: string;
  /** One-sentence card blurb on the /skills landing page. */
  blurb: string;
  /** "At a glance" framing paragraph shown at the top of the term page. */
  intro: string;
  /** The near-peer tutoring model paragraph, shown once per term page. */
  taModel: string;
  /** Which G11 term these cards map their `mapsToWeek` into. */
  targetGradeTerm: number;
  status: 'active' | 'planned';
}

export const SKILLS_TERMS: SkillsTermInfo[] = [
  {
    id: '1',
    label: 'Term 1',
    eyebrow: '8 sessions · SK1–SK8',
    blurb: 'Structures, materials, the project circuit, exam technique, specification, sketching and idea generation — previewed before W3–W10.',
    intro:
      'SKILLS starts at Week 3 this term — Weeks 1–2 (brief framing, sketching fundamentals) run only in the regular class this year. Each of the 8 sessions previews and deepens that week\'s regular Term 1 topic, then prepares the 18 to TA it; 2 further slots sit as unscheduled buffer for any week that has to be skipped. Because the group arrives at SK1 having only had the regular W1–W2 classes and no project decided yet, SK1 doubles as the point where each student\'s own project gets locked down — a real user and a real load, not a placeholder. The high-leverage weeks are W3 (structures end-to-end — the TA must range across all four sub-topics, and the project-lock check happens here), W6 (electronics — circuit building), W7 (exam technique — mark-scheme analysis), W9 (3D sketching + annotation), and W10 (idea generation + Paper 1 project mock).',
    taModel:
      'Having previewed the topic, each SKILLS student joins that week\'s regular class as a near-peer tutor: circulating, prompting and checking the other students\' work using the tutoring cue on their card. The rule they are taught is ask, don\'t tell — guide a peer to the answer with a question rather than handing it over.',
    targetGradeTerm: 1,
    status: 'active',
  },
  {
    id: '2',
    label: 'Term 2',
    eyebrow: 'Not yet written',
    blurb: 'Design development, working drawings, manufacture and CAD — mapped to Term 2.',
    intro: '',
    taModel: '',
    targetGradeTerm: 2,
    status: 'planned',
  },
  {
    id: '3',
    label: 'Term 3',
    eyebrow: 'Not yet written',
    blurb: 'Bench-TA support for assembly, electronics and testing under the technician.',
    intro: '',
    taModel: '',
    targetGradeTerm: 3,
    status: 'planned',
  },
  {
    id: 'revision',
    label: 'Revision',
    eyebrow: 'Not yet written',
    blurb: 'Peer revision-group leadership alongside top-band exam mastery.',
    intro: '',
    taModel: '',
    targetGradeTerm: 3,
    status: 'planned',
  },
];

export function getSkillsTerm(id: string): SkillsTermInfo | undefined {
  return SKILLS_TERMS.find((t) => t.id === id);
}
