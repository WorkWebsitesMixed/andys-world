/**
 * The three cross-category launch examples (person → need → product).
 * Deliberately NOT desk products — they show the pattern without overlapping
 * what students are likely to design. Text cards for now; each is a
 * [PLACEHOLDER] to be replaced with a real image/case study later.
 */

export interface ProjectExample {
  icon: string;
  person: string;
  frustration: string;
  product: string;
  load: string;
  circuit: string;
}

export const PROJECT_EXAMPLES: ProjectExample[] = [
  {
    icon: '🎸',
    person: 'A musician',
    frustration: 'Their instrument and accessories have no safe home between sessions.',
    product: 'A freestanding instrument & cable rack',
    load: 'Instrument weight',
    circuit: '"Session ready" indicator',
  },
  {
    icon: '🚲',
    person: 'A cyclist',
    frustration: 'They lose track of helmet, shoes and tools before a ride.',
    product: 'A helmet, shoes & tool organiser',
    load: 'Gear weight',
    circuit: '"Ready to go" light',
  },
  {
    icon: '🪴',
    person: 'A collector',
    frustration: 'They have no way to display books, plants or figures at height.',
    product: 'A tiered display structure',
    load: 'Collection weight',
    circuit: 'Small spotlight / indicator',
  },
];
