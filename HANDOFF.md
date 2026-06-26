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
- **Textbook links (2026-06-23):** `../Curriculum/Book.pdf` (Collins IGCSE D&T,
  375 pp, image-only) split into 27 section PDFs with ghostscript (PDF page =
  book page − 1 throughout). Hosted on Google Drive (anyone-with-link; not in
  repo — copyright). 58 `href` fields added to `type: "Textbook"` resource items
  across all 29 G11 lesson MDX files. Each `📘 Textbook` entry now links directly
  to the relevant section extract. §1.5 + §1.6 share one bundled file.
  Extracts kept at `../textbook-extracts/` locally for re-use.
- **G11 T2 + T3 rewrite (2026-06-25):** All 30 G11 lessons (T2 W1–10, T3 W1–10)
  rewritten to match the canonical LaTeX schemes of work at
  `../Curriculum/Grade11_SchemeOfWork/Term{2,3}.tex`. The LaTeX source is the
  ground truth for G11; earlier MDX files had drifted. T3 W11–W20 are
  `sessionType: bonus` — shown on the term page as a separate "Bonus sessions"
  block (see `bonusWeekStart` in `curriculum.ts`).
- **Grade 12 T1 (2026-06-25):** 12 lessons authored from scratch (T1 W1–12).
  Week count override: `WEEKS_OVERRIDE[12][1] = 12` in `curriculum.ts`.
- **Grade 10 fully populated (2026-06-25):** All 30 lessons written from
  LaTeX sources at `../Curriculum/2027/10th/LaTeX_sources/Term{1,2,3}.tex`.
  - T1 (10 lessons): Design communication, mechanisms, electronics (Firefighter Barbie).
  - T2 (10 lessons): Materials, making, OnShape CAD (Desk Organizer). Three
    graded moments: M1 Paper 1 (c)(d)(e) W7; M2 folder W8; M3 partial Paper 3 W10.
  - T3 (10 lessons): Commercial manufacturing, reverse-engineering (Water Bottle).
    M1 analysis package W6; M2 design+plan package W9; M3 full Paper 3 mock W9.
  - **G10 does not use `ExamLink`** (Paper 3 not in the route map) — exam refs
    are plain text inside `Callout` or `Section`.
  - **G10 does not use `route:` on Resources** — the Resources component hardcodes
    grade 11 in `routes[r.route](11)`. All G10 textbook links use `href:` instead.
- **Textbook links comprehensive pass (2026-06-25):** 110 changes across 57
  files (G10 T1–T3, G11 T1–T3, G12 T1). All `type: "Textbook"` items that have a
  Drive PDF now carry `href: "https://drive.google.com/open?id=..."`. Existing
  `file/d/ID/view?usp=sharing` hrefs normalised to `open?id=` format.
  Sections with no Drive PDF (§2.6 CAD, §3.8–3.9, §3.11–3.13, §5.1–5.2 etc.)
  remain as plain text labels — add hrefs when those PDFs are uploaded.

## 7. Content sources (for populating more lessons)
- **Grade 11 (done):** `../Curriculum/Grade11_SchemeOfWork/Term{1,2,3}.tex`
  (each `\section{Week N}` → 90-min lesson; `\section{Bonus N}` → bonus session
  with `sessionType: bonus` in frontmatter). Context in
  `../Curriculum/PLANNING_HANDOFF_Grade11_2027.md`.
- **Grade 10 (done):** `../Curriculum/2027/10th/LaTeX_sources/Term{1,2,3}.tex`
  — three projects: Firefighter Barbie (T1), Desk Organizer (T2), Water Bottle
  reverse-engineering (T3). IGCSE 0445 D&T, Materials option; Papers 1 and 3
  (no Paper 4; no ExamLink; no Resources `route:` — use `href:` only).
- **Grade 12 T1 (done):** 12 lessons, 12-week term override.
  T2 and T3 still empty — not yet planned.
- **Textbook:** `../Curriculum/Book.pdf` (Collins IGCSE D&T, 375 pp, image-only).
  Section PDFs on Google Drive — see Section 6 for link format and which sections
  still need PDFs. Drive links map: see the user's canonical list in the most
  recent session notes, or grep `open?id=` in any lesson file for the 28 covered IDs.
- Old site to mine for images/quizzes: `../D&T Classes/D-T-Classes/` (+ `img/`).

## 7b. Extracurricular courses (added 2026-06-26)
- **Python Programming** course added at `/course/python/` with 4 sprints × 27 weeks.
- Architecture: new `sessions` content collection (`src/content/sessions/python/*.mdx`),
  `src/lib/courses.ts` (parallel to `curriculum.ts`), new route builders in `url.ts`.
- Nav: "Extracurricular" link added to header (violet, `--accent-2`), links to `/extracurricular` index.
- Session pages: lighter structure — sprint tag, week number, payoff, learning goals, code files.
- **`CodeFile.astro`** component: Shiki syntax highlighting (`github-dark` theme), no line numbers,
  **Copy button** (clipboard API copies `pre.textContent` — zero line numbers in paste),
  **Download .py** button (links to `public/python/filename`).
- All `.py` files + `sample_grades.csv` + `sample_notes.txt` live in `public/python/` (served as
  static downloads) and are read at build time via `fs.readFileSync` in the week page.
- **Mechatronics** course added at `/course/mechatronics/` — 6 blocks × 60 classes across 30 weeks.
  - Block structure (not sprint/week): `CourseInfo` is now a discriminated union `{ structure: 'sprint' | 'block' }`.
  - New `blocks` content collection (`src/content/blocks/mechatronics/block-1a.mdx` → `block-2d.mdx`).
  - Route: `/course/mechatronics/block/[blockId]` — one rich page per block with C++ code, tables, copy buttons.
  - Copy buttons on fenced code blocks injected by a client-side script in the block page (no line numbers).
  - Block 2B shows all three tracks (Pet Feeder / Smart Locker / Vending Machine) on one URL.
  - `src/pages/course/[courseId]/block/[blockId].astro` — new block page with prev/next navigation.
  - Source of truth for content: `../Curriculum/mechatronics_course/*.tex` files.

## 8. Open items / next steps
1. **Grader URL:** `examsUrl` in `src/lib/site.ts` points at the grader **preview**
   (`https://workwebsitesmixed.github.io/exam-grader-v2-preview/`) — swap for the
   production URL when available.
2. **Grade 12 T2 + T3** — not yet planned or authored. Placeholder stubs show
   already. Awaiting Andy's curriculum plan for those terms.
3. **Remaining textbook Drive links** — 29 `type: "Textbook"` items across G10 and
   G11 still have no `href` because no Drive PDF was provided for those sections:
   §1.7, §2.4, §2.5, **§2.6 CAD**, §3.8 Finishing, **§3.9** Manufacturing,
   **§3.11** Scale of production, **§3.12** Polymer processes, **§3.13** Metal
   processes, §5.1, §5.2. Upload those PDFs to Drive, share the `open?id=` URL,
   and run the same `patch_links.py` pattern (or share links and I'll patch inline).
4. **Media:** curated only — SVG diagrams (authored) for technical concepts; photos
   only where real-world needed; Watch/See = web-searched candidates the user
   approves (never auto-search, never fabricate URLs).
5. **CI nicety:** deploy workflow actions log a "Node 20 deprecated" warning — bump
   `actions/checkout`, `setup-node`, `upload-pages-artifact` versions sometime.

## 9. Working style (the user's established preference)
**Discuss before implementing** on significant decisions: propose + recommend, get
an explicit go-ahead, then build; review phase-by-phase. The user likes
conversational discussion over multiple-choice prompts. Honest reality-checks are
valued over yes-man agreement.
