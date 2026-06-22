# Andy's World — project handoff

> Hand-off for a **fresh session** opened in this folder
> (`/home/andresforero/Documents/Marymount/andys-world/`). The site is **built and
> live**; this document is the current state, architecture, and what remains.

## 0. Status — BUILT & LIVE 🚀
- **Live site:** https://workwebsitesmixed.github.io/andys-world/
- **Repo:** `WorkWebsitesMixed/andys-world` (public; default branch `main`).
- **Deploy:** every push to `main` triggers `.github/workflows/deploy.yml` (Astro
  build → GitHub Pages). No manual step. First shipped 2026-06-21.
- **Build check:** `npm run build` (runs `astro check` + build) — keep it at
  **0 errors / 0 warnings / 0 hints**. `npm run dev` to preview locally.

## 1. What it is
A **student-facing** teaching website for **Andrés Forero** ("Andy's World"),
Head of Design & Technology at **Marymount School, Medellín**. Hosts D&T class
lessons organised **Grade (10/11/12) → Term (1/2/3) → Week (1–10) → Class**. It is
Andy's own brand (not Marymount-branded). Replaces an old hand-coded site.

## 2. Stack & architecture
- **Astro 6** static site, **MDX content collections**, deployed to GitHub Pages.
- **Project page** (GitHub Pages): `astro.config.mjs` sets `site` =
  `https://WorkWebsitesMixed.github.io`, `base` = `/andys-world`. **Never hard-code
  the base** — use `src/lib/url.ts` (`url()`, `routes.*`).
- **Content model:** one `.mdx` per class in `src/content/lessons/`. **Routing is
  derived from frontmatter** (`grade`/`term`/`week`), not file path. Schema in
  `src/content.config.ts`. Convention: `grade-<n>/t<term>-w<week>.mdx`.
- **Nav is generated** from the lessons collection + `src/lib/curriculum.ts`
  (grades, terms, 10 weeks/term, per-term focus for placeholder grades).
- A missing week renders a "being prepared" placeholder automatically.
- **Drafts:** `draft: true` hides a lesson in production, shows it in `npm run dev`.

## 3. Design system & UX
- Dark, near-black surface · **electric blue-cyan accent** (`#34e0ff`) · Space
  Grotesk + Inter (self-hosted) · faint physics grid + glow. Tokens in
  `src/styles/global.css`.
- **Display preferences** (header "Aa Display", saved in `localStorage`, applied
  pre-paint): theme **Dark / Light / High-contrast**, text spacing **Normal /
  Roomy**, **Calm mode** (hides grid/glow/motion). New components must look right in
  all three themes.
- **Floating section navigator** (`LessonNav.astro`), scroll-spy, ≥1280px only.
- Accessibility baseline: alt text required on images, WCAG-checked contrast,
  keyboard/`prefers-reduced-motion` support.

## 4. Lesson format & component library
Locked house structure per lesson: lead hook → `Callout type="exam" id="why"`
(wrap first paper mention in `<ExamLink>`) → `KeyTerms` → `Section "The lesson"`
(drop a diagram if a technical concept fits) → `WorkedExample` → `Activity` →
`Support` → `SelfCheck` (3 Qs, each with `hint` + `explain`) → `Section "Homework &
extension"` with `Extension` → `Resources` → `Reflection`.

Components (all auto-available in MDX — **never add imports to lesson files**; see
`src/layouts/LessonLayout.astro` for the map, and **`src/content/lessons/README.md`
for the full authoring guide**):
`Goals` (auto, from frontmatter), `KeyTerms`, `WorkedExample`, `Activity`,
`SelfCheck` (formative only — instant client-side feedback, **nothing stored**;
wrong → hint, correct → explanation + lock), `Resources`, `Reflection`, `Callout`,
`Section`, `Support` (collapsible scaffold), `Extension` (optional stretch),
`Figure` (image + required alt), `WatchSee` (curated external video links),
`ExamLink`, `ProjectExamples`, and theme-aware SVG diagrams in
`src/components/diagrams/` (Triangulation, Forces, Circuit, BeamReactions).

## 5. The coursework brief (CANONICAL — reworked June 2026)
**Open, person-first.** Students design a structural product for **a real person
they know** — no product category prescribed. Constraints are on what it must *do*
and how it's *made*:
- carry a **defined, tested load**;
- a **low-voltage switch-operated circuit** (category bound: choose switch +
  indicator; **no PICs/logic gates/PCBs/motors/sensors**; ~18 Skills-enrichment
  students may use a DC motor with an end-of-Term-2 breadboard checkpoint);
- the **make-palette** (laser sheet, timber/strip, minimal 3D print);
- fit **400 × 400 mm**, ≥150 mm one dimension; a **real finished product**.
Three launch examples (single source of truth, image-ready placeholders, in
`src/lib/project-examples.ts` · rendered by `ProjectExamples.astro`): A musician
rack · **B cyclist gear organiser (the running example in lessons)** · C collector
display. Full brief lives on the **Project
overview** page (`/grade/11/project`); the "Your IGCSE" hub (`/grade/11/igcse`)
explains Paper 1, Paper 4 and the Project.

## 6. What's done
- **Phase 0** foundation/design system · **Phase 1** exemplar · **Phase 2** **all 30
  Grade 11 lessons** (Systems & Control; Terms 1–3 × 10) + the IGCSE hub (Paper 1 /
  Paper 4 / Project pages) + curated diagrams & approved Watch/See videos ·
  **Phase 3** Grade 10 & 12 placeholder structure + authoring README ·
  **Phase 4** shipped to GitHub Pages.
- **Phase 5** architectural refactoring (zero student-facing changes):
  - **P1** MDX lesson files are now fully import-free — `routes.*` replaced by
    `route:` prop on `Resources` items and `<ExamLink>` for inline prose links.
  - **P2** Utility classes `page-narrow`, `lede`, `card-grid` extracted to
    `global.css`; duplicate scoped rules removed from four pages.
  - **P3** `DisclosureBlock.astro` base component; `Support` and `Extension` are
    thin wrappers (~10 lines each).
  - **P4** `GradeInfo.hub` data field in `curriculum.ts` drives the grade hub
    banner; hardcoded `gradeNum === 11` guard removed from `[grade].astro`.
  - **P5** `ProjectExamples` data moved to `src/lib/project-examples.ts`.
  - **P6** `--header-h: 64px` CSS token in `:root`; header height and
    `scroll-margin-top` both reference it.
  - **P7** Inter font switched from the full multi-subset import to a single
    Latin-only `@font-face` block (drops 6 unused subset declarations).
  - **P8** `<link rel="preload">` for Inter in `BaseLayout.astro` using a Vite
    `?url` import so the href matches the content-hashed filename in the CSS.

## 7. Content sources (for populating more lessons)
- **Grade 11 (done):** `../Curriculum/LaTeX_sources/Term{1,2,3}.tex` (each
  `\section{Week N}` → the `W (90 min)` lesson; ignore `B` bonus sessions),
  context in `../Curriculum/PLANNING_HANDOFF_Grade11_2027.md`, textbook
  `../Curriculum/Book.pdf` (Collins, image-only).
- **Grade 10 (Materials) — to populate:** `../Curriculum/Curriculum_2028-2030_Materials/`.
- **Grade 12 (ICT/Programming) — user-populated:** T1 IGCSE ICT review, T2 empty,
  T3 Programming. Structure/labels already stubbed in `curriculum.ts`.
- Old site to mine for images/quizzes: `../D&T Classes/D-T-Classes/` (+ `img/`).

## 8. Open items / next steps
1. **Grader URL:** `examsUrl` in `src/lib/site.ts` points at the grader **preview**
   (`https://workwebsitesmixed.github.io/exam-grader-v2-preview/`) — swap for the
   production URL when available.
2. **Populate Grade 10 & Grade 12** lessons (architecture + README ready).
3. **Media:** curated only — SVG diagrams (authored) for technical concepts; photos
   only where real-world needed; Watch/See = web-searched candidates the user
   approves (never auto-search, never fabricate URLs). Term 2 had videos added;
   Term 2/3 more can be sourced on request.
4. **CI nicety:** deploy workflow actions log a "Node 20 deprecated" warning — bump
   `actions/checkout`, `setup-node`, `upload-pages-artifact` versions sometime.

## 9. Working style (the user's established preference)
**Discuss before implementing** on significant decisions: propose + recommend, get
an explicit go-ahead, then build; review phase-by-phase. The user likes
conversational discussion over multiple-choice prompts. Honest reality-checks are
valued over yes-man agreement.
