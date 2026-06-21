# Andy's World — website rebuild brief

> Hand-off for a **fresh session** opened in this folder
> (`/home/andresforero/Documents/Marymount/andys-world/`). It is self-contained:
> read it fully, then start at **§7 Build plan, Phase 0**. Confirm the §8 open
> items with the user early.

## 1. What we're building
A **professional personal teaching website for Andrés Forero** ("**Andy's World**") — Design & Technology teacher / HOD at Marymount school, Bogotá. It replaces an old, sprawling hand-coded site. **Built from scratch** with a clean, data-driven architecture. The site hosts student-facing **class lessons** organised by grade → term → week.

This is **not** Marymount-branded — it is Andy's own brand.

## 2. Locked decisions
- **Stack:** **Astro** (static site), authored content in **MDX content collections**, deployed to **GitHub Pages** (brand-new repo = this folder; already `git init`-ed).
- **Identity / look:** name **"Andy's World"**; **dark theme**, **electric cyan** accent; technical sans-serif (suggest **Space Grotesk** headings / **Inter** body); aesthetic = *innovation · physics · technology* — near-black background, thin vector grid, faint circuit/orbit motifs, subtle smooth motion. Formal but cool; fast; responsive.
- **Content model:** `Grade (10/11/12) → Term (1/2/3) → Week (1–10) → Class`. Each class is **one `.mdx` file** (frontmatter + body). Navigation (home → grade → term → week) is generated from the collection.
- **Scope now:** build the **architecture for ALL grades/terms/weeks**, but **populate Grade 11 only**. Grade 10 and Grade 12 get ready-to-fill **placeholder** pages.
- **No grading on this site.** A configurable **"Exams" link** points out to Andy's separate grader project (see §6). In-lesson "Check your understanding" is **formative only** — client-side, instant feedback, **nothing stored, no backend, no grade**.
- **Term 3 = 10 weeks**, where **Week 10 = "Project Review"** (consolidation). (The source plan's Term 3 has 9 taught weeks; week 10 is the added review.)

## 3. The lesson page format (every class follows this)
Frontmatter (per `.mdx`): `grade`, `term`, `week`, `title`, `topic` (tag), `learningGoal`, `selGoal`, `draft` (bool).
Body sections, in order — each a reusable **component** where it makes sense:
1. **Header** — grade · term · week · title · topic (rendered from frontmatter).
2. **Goals** — **two**: a **Learning goal** and an **SEL goal**, both phrased *"By the end of this class I will…"* (Mager ABCD style, carried from the curriculum plan).
3. **Why this matters** — short hook linking the class to the IGCSE exam / coursework.
4. **Key terms** — `<KeyTerms>` (term → definition list).
5. **Lesson content** — the actual teaching: clear sections, examples, diagrams/images.
6. **Worked example** — `<WorkedExample>` step-by-step.
7. **Activity** — `<Activity>` the in-class hands-on task.
8. **Check your understanding** — `<SelfCheck>` formative quiz (client-side only, no storage).
9. **Homework / extension** — optional further practice.
10. **Resources** — `<Resources>` textbook pages, past papers, videos, downloads.
11. **Reflection** — `<Reflection>` one-line metacognition prompt.

Component library to build: `Goals` (dual), `KeyTerms`, `WorkedExample`, `Activity`, `SelfCheck`, `Resources`, `Reflection`, `Callout`, plus layout/nav/card components.

## 4. Content sources (where the lessons come from)
- **Grade 11 (2026–27) = the Systems & Control scheme we built.** Expand each week's *main class* into a full student lesson using the §3 format. Sources:
  - `/home/andresforero/Documents/Marymount/Curriculum/Term1.pdf`, `Term2.pdf`, `Term3.pdf`, `Overview.pdf` (LaTeX sources in `Curriculum/LaTeX_sources/`).
  - Context / philosophy: `Curriculum/PLANNING_HANDOFF_Grade11_2027.md` (S&C route, **Structures** as Paper 4 Section B, the dual cognitive+SEL goals, the framed-structures coursework project, the per-week topics). **Read this for the teaching content and the goal style.**
  - Per-term week topics are listed in those docs (e.g. Term 1: W1 project launch, W2 structures types/rigidity, W3 forces & members, W4 woods & metals, W5 concrete/plastics/composites + sustainability, W6 research→spec, W7 loads/moments/stress/FoS, W8 joining, W9 the project circuit, W10 idea generation). Term 2 and Term 3 likewise.
  - The lessons must be **student-facing** (teach the student), not the teacher run-sheets — rewrite accordingly, keeping the dual goals.
- **Grade 10 (2026–27) = the Materials cohort** — source is `Curriculum_2028-2030_Materials/` (static canonical + physics) plus pending transition bridges. **Leave as placeholders for now** (architecture only; do not populate).
- **Grade 12 = ICT/Programming, populated by the user** — Term 1 *IGCSE ICT review*, Term 2 *empty*, Term 3 *Programming*. **Placeholders only.**
- **Old site to mine for reusable material** (images, quiz content, explanations): `/home/andresforero/Documents/Marymount/D&T Classes/D-T-Classes/` (102 hand-coded HTML pages + `img/`). Archive, don't copy wholesale.
- **SKILLS enrichment** (`Curriculum/Skills_2026-2027/`) is **out of initial scope** — possibly a later separate section.

## 5. Visual / UX targets
- Dark background (near-black), electric-cyan accent, high-contrast readable body text.
- Home → grade landing (10/11/12) → term → week grid → lesson page. Clean cards, breadcrumb nav, prev/next within a term.
- Physics/tech motifs used tastefully (grid, faint circuitry/orbits, glow on the accent, micro-interactions). Must stay legible and professional.
- Mobile-first responsive; fast (static).

## 6. Grader integration (do NOT rebuild grading)
Andy has a separate, robust **exam-grader** project: `/home/andresforero/Documents/Marymount/D&T Classes/exam-grader/` (Google Apps Script JSON API + GitHub Pages frontend, **Claude-graded** IGCSE mocks; see its `handoff.md`). This site only needs a **configurable `examsUrl`** in site config that links students to that grader. Leave it as a placeholder/config value; **ask the user for the exact production URL** (a preview exists at `https://workwebsitesmixed.github.io/exam-grader-v2-preview/`).

## 7. Build plan (phased — review with the user between phases)
- **Phase 0 — foundation:** scaffold Astro; set up the dark + electric-cyan theme, fonts, physics-motif design system, base layout, content-collection **schema** (§3 frontmatter), nav generation, and the **GitHub Pages deploy** (GitHub Actions). Build the **component library** (§3).
- **Phase 1 — exemplar:** build **one fully-worked lesson** (Grade 11 · Term 1 · Week 1) end-to-end to lock the format, components and visual. **Get user sign-off** before scaling.
- **Phase 2 — populate Grade 11:** generate all Grade 11 lessons — Term 1 (10), Term 2 (10), Term 3 (10, incl. Week 10 "Project Review") ≈ **30 lessons**, from the §4 sources. Build term-by-term, Term 1 first for review (mirrors how the curriculum was built).
- **Phase 3 — placeholders:** stub Grade 10 (all terms/weeks) and Grade 12 (T1 ICT review, T2 empty, T3 Programming) so the user can fill them.
- **Phase 4 — ship:** deploy to GitHub Pages; wire the `examsUrl`; archive the old site repo reference.

## 8. Confirm with the user early
1. **GitHub account/repo name** for Pages (and is the deploy to `username.github.io/andys-world` or a custom domain?).
2. The **grader production URL** for `examsUrl`.
3. Repo/folder name is `andys-world` — keep, or rename?
4. Font choice (Space Grotesk/Inter ok?) and whether the cyan should be more blue-cyan or green-cyan.

## 9. Working style (the user's established preference)
**Discuss before implementing** on significant decisions: propose + recommend, get an explicit go-ahead, then build; review phase-by-phase (Term 1 first). The user likes conversational discussion over multiple-choice prompts. Keep the curriculum context in mind — this site is the student-facing face of the plans in `../Curriculum/`.
