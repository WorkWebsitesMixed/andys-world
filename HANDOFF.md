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
- **Light is the default theme (changed 2026-08-04).** Soft blue-grey page
  (`--bg: #eef1f6`) with white cards · **deep cyan accent** (`#0a7488`, ≥4.5:1 on
  white) · Space Grotesk + Inter (self-hosted) · faint physics grid + glow. Tokens in
  `src/styles/global.css`.
- **Token structure:** `:root` holds the **light** palette; `:root[data-theme='dark']`
  and `:root[data-theme='contrast']` override it. There is deliberately **no
  `[data-theme='light']` block** — a stored `light` preference falls through to
  `:root`. The near-black surface + `#34e0ff` electric cyan is now the *dark* theme.
- **Feedback colours (`--ok`/`--warn`/`--bad`) are defined per theme** and must stay
  that way. The dark values drop to ~1.5:1 on white; the light values are each ≥5:1.
  If you add a theme, define all three.
- **Display preferences** (header "Aa Display", saved in `localStorage`, applied
  pre-paint): theme **Light / Dark / High-contrast**, text spacing **Normal /
  Roomy**, **Calm mode** (hides grid/glow/motion). New components must look right in
  all three themes.
- **Lesson sections are numbered.** `.lesson-body` sets `counter-reset: sec` and
  `Section.astro` increments it, so every `<Section>` in a lesson is numbered 1..n
  down the page (all the house-structure components render a `<Section>`). Sections
  are divided by a `border-top` spanning the column — a boundary *between* sections,
  not an underline on the heading. Section `h2` is 1.55rem against a 1.05rem `h3`;
  keep that gap, a student reported the old 1.3/1.25 step was unreadable as hierarchy.
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
wrong → hint, correct → explanation + lock — hardcodes `id="self-check"` in its
internal `<Section>`, so **only one per page**), `Resources`, `Reflection`,
`Callout`, `Section`, `Support` (collapsible scaffold), `Extension` (optional
stretch), `WatchSee` (curated external video links), `ExamLink`, `WeekLink`
(inline link to another week's page — e.g. a main session ↔ its paired B
session), `ProjectExamples`.
- **`Figure`** (image + required alt) — `src` resolves through `url()`, so pass a
  path relative to `public/`, e.g. `src="images/tools/pillar-drill.jpg"`, no base
  prefix needed. Optional `credit`/`creditHref` render a linked attribution line
  under the caption — use for any openly-licensed photo (see §6 real-photo note).
- **`MoreImages`** (`term` prop) — a "see more real photos of X" link. Currently
  points at **Google Images** (`google.com/search?...&tbm=isch`), a deliberate,
  informed choice by Andy (2026-08-07) after Wikimedia's `Special:MediaSearch`
  returned empty for several multi-word queries even though Commons has matching
  content — its relevance matching doesn't handle compound tool/joint names well.
  Known tradeoff: unlike a Commons search, results aren't licence-filtered or
  moderated by us.
- **Theme-aware SVG diagrams** in `src/components/diagrams/` (12 as of
  2026-08-06): `TriangulationDiagram`, `ForcesDiagram`, `CircuitDiagram`,
  `BeamReactionsDiagram`, `StructureTypesDiagram`, `StructuralJointsDiagram`,
  `MotionTypesDiagram`, `SliderCrankDiagram`, `CamDiagram`,
  `TransistorSwitchDiagram`, `GearTrainDiagram`, `InjectionMouldingDiagram`,
  `BlowVacuumFormingDiagram`, `MetalProcessesDiagram`, `CharpyTestDiagram`,
  `QCGaugesDiagram`. Same pattern for a new one: inline `<svg>` in a
  `<figure class="diagram">`, `title`/`desc` for a11y, CSS vars only
  (`var(--text)`, `var(--accent)`, etc.) so it recolours per theme automatically.

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
  `sessionType: 'b'` (renamed from `'bonus'` 2026-08-06 — see below) — shown on
  the term page as a separate "B sessions" block (`bSessionStart()` in
  `curriculum.ts`).
- **Grade 12 T1 (2026-06-25):** 12 lessons authored from scratch (T1 W1–12).
  Week count override: `WEEKS_OVERRIDE[12][1] = 12` (later 24 — see below) in
  `curriculum.ts`.
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

- **Textbook link audit & repair (2026-08-04):** all 139 `type: "Textbook"` items re-checked
  against the actual Drive files. 53 edits across 34 lesson files; build stayed 0/0/0.
  - **Dead link fixed:** the §1.8 Drive ID in 10 lessons was 32 chars (a dropped `E`). Correct ID
    is `1LALQ16ljZjug0gE7WVoN2HaEERnwFK-4`. Recovered via
    `curl "https://drive.google.com/embeddedfolderview?id=13ILaFGNhBhK1Ol2k_OUVbGOYx7tpiBxW"`,
    which returns plain HTML listing all 27 filenames + IDs with no auth. **Use that trick again**
    if a link breaks — the MCP Drive connector is on the personal account and cannot see these files
    (owned by `andres.forero@marymount.edu.co`), though `get_file_metadata` on a known ID works.
  - **Wrong file fixed:** four §4.4.4/.5/.7 refs in `g10/t1-w8`, `t1-w9` pointed at
    `s4-4-electronics`; repointed to `s4-4-3-switches`. Their page numbers were already correct.
  - **~30 page numbers corrected** against verified section-start pages (see the vault note for the
    full § → page table). Extracts are at `../Curriculum/2027/textbook-extracts/`.
  - **Known defect:** `s1-3-making.pdf` starts at printed p. 36, but §1.3 opens on p. 35 — that page
    is the last page of `s1-2-design-ideas.pdf`. Labels cite p. 36 deliberately. A corrected
    re-split is ready at `../Curriculum/2027/textbook-extracts/s1-3-making-FIXED.pdf`; if it is
    uploaded in place, flip the 7 §1.3 labels to p. 35.
  - `s4-2-4-structural-members.pdf` (§4.2.4, pp. 242–244) is on Drive as
    `1Gef_9F-ldqFU3wRb5XPN1_FYC2yuFzaS` but is not linked from any lesson.
  - Note: **PDF pages are image-only.** To find where a section starts, render with `pdftoppm` and
    read the page-top strips — `pdftotext` returns nothing.
  - **The 29 previously-unlinked refs are now linked too.** They were never a missing-PDF
    problem: they cited section numbers from a *different edition*. Remapped per-lesson —
    "§2.6 CAD" → §1.6 Use of technology (p. 63), "§5.2 Mechanisms" → §4.3 (p. 265),
    "§3.12/§3.13" → §3.9 Shaping (p. 204), "§2.5 Finishing" → §3.11 Finishes (p. 222),
    "§2.4 Adhesives" → §3.10 Joining and assembly (p. 210). Two "§3.11 Scale of production"
    references were **dropped** — this edition has no such section (chapter 3 ends at §3.11
    Finishes; chapter 5 is one unnumbered chapter, "The Project", p. 346, so no §5.1/§5.2).
    `g10/t3-w4` and `t3-w5` deliberately carry **both** §1.7 (p. 72) and §1.8 (p. 78) for
    product analysis — Andy will pick one later. Full table: vault note §4b.

- **Maths rendering (2026-08-04):** `remark-math` + `rehype-katex` wired into
  `astro.config.mjs`; maths compiles to static MathML + HTML at build time (no client JS,
  screen-reader accessible). `katex/dist/katex.min.css` is imported by **`LessonLayout`,
  not `BaseLayout`** — only lesson pages carry the stylesheet.
  - **`Formula.astro`** — the house component for calculations. Renders
    equation → substitution → result on labelled rows, result row in the accent wash,
    all three left-aligned on a shared baseline (that's the Paper 4 mark-scheme method).
    Props: `name?`, `equation` (required), `substitution?`, `result?`, `note?`. It calls
    `katex.renderToString` directly, since MDX props are not markdown and `$…$` would not
    be processed there. Verified in dark, light and high-contrast.
  - Inline `$…$` / display `$$…$$` work in lesson prose. Authoring rules and TeX
    conventions are in `src/content/lessons/README.md` under **Maths**.
  - Converted so far: `g11/t1-w3`, `t1-w6`, `t2-w10`, `g10/t1-w8`, `t1-w9` (12 formulas).
  - **Watch out:** `g12/t1-w1` and `t1-w7` use `$` for Excel absolute references. Those are
    all inside backticks/code fences/JS prop strings, which remark-math ignores — but never
    write a bare `$B$2` in prose or it will be parsed as maths.

- **Section separation + light-default (2026-08-04):** section `h2` step, `border-top`
  boundary rule, section numbering via CSS counter, light made the default theme
  (dark/high-contrast still one click away). Fixed a real defect on the way in: light
  never redefined `--ok`/`--warn`/`--bad`, so quiz feedback was near-invisible on white.

- **G12 B-session curriculum + bonus→B rename (2026-08-06):** G12 has a second,
  mandatory 45-min weekly class (the "B session") alongside the 90-min main class —
  same mechanism G11 T3 already used (extra week numbers appended after the main
  block via `WEEKS_OVERRIDE`/`B_SESSION_START` in `curriculum.ts`). Both were
  mislabelled "Bonus" (implying optional); renamed site-wide to "B" —
  `sessionType: 'bonus' → 'b'`, `BONUS_START → B_SESSION_START`,
  `bonusWeekStart() → bSessionStart()`, UI pill "Bonus B*n*" → "B*n*".
  - `WEEKS_OVERRIDE[12][1]` 12 → **24** (12 W sessions + 12 B sessions).
  - **B1–B7** (weeks 13–19): restored to full 45-min lessons from `Term1.tex`'s
    Socratic scripts — previously compressed into a duplicate "Theory" section
    inside each `t1-w1..w7.mdx`; that duplicate is now a one-line `<Callout>`
    pointer to the paired B session via `<WeekLink>`.
  - **B8–B12** (weeks 20–24): no scheme existed for this slot (`Term1.tex` says
    "Block B: W only"). Design decision, not restoration — mirrors what the W8–W12
    Chemistry-lab-report unit already proves LaTeX is good at (`mhchem`,
    `graphicx`, `booktabs`, `biblatex`: structured multi-page documents with
    tables/figures/citations) rather than a CV-building idea that was tried and
    dropped (a hand-built LaTeX CV template couldn't beat Andy's own Canva CV on
    one-page visual design — see the vault note for the full comparison). Students
    write a report in their own field (most are Medicine/Management-bound, a
    minority Engineering), reusing the Chemistry report's LaTeX skeleton rather
    than three separate templates.
  - Added **`WeekLink.astro`** (mirrors `ExamLink`'s pattern) for W↔B cross-links.

- **Structures/mechanics/manufacturing diagrams + real tool photos (2026-08-06/07):**
  audited G10/G11 for missing visuals — found 4 diagram components already built
  and registered but **used in zero lessons**. Built 12 total (see §4) and wired
  them into their actual teaching lessons; also sourced, downloaded and hosted 16
  openly-licensed real photos of workshop tools/equipment from Wikimedia Commons
  (`public/images/tools/`, credits in `public/images/tools/CREDITS.md`, attribution
  rendered live via `Figure`'s `credit`/`creditHref`). Verify a Commons candidate
  visually before committing to a lesson — two initial picks were wrong at a glance
  (an industrial sheet-metal laser rig for what should read as a desktop laser
  cutter; a sash-clamp search returning irrelevant scanned book pages — "bar clamp"
  found the real thing). `junior-hacksaw.jpg` was sourced but never placed — the
  term isn't actually used anywhere in the G10/G11 content, so it wasn't forced in.

- **Firefighter Barbie façade guide (2026-08-10):** `facade_guide.html`
  (self-contained dimensioned-drawing/assembly guide for the teacher-made 13
  Ember Lane façade, generated from `facade.py` — source at
  `../class_materials/10th_grade/firefighter_barbie_facade/`) hosted at
  `public/g10/firefighter-barbie/facade_guide.html` and linked as a `Resources`
  item in G10 T1 **W1** (handed out as the fixed constraint), **W2** (dimensioned
  drawings for orthographic projection), and **W10** (install/assembly
  reference) — matches the weeks the guide's own README calls out. Extended
  `Resources.astro`'s `href` to resolve relative (`public/`-rooted) paths through
  `url()`, mirroring `Figure`'s `src` handling, so a lesson can link a static
  file without an MDX import.

## 7. Content sources (for populating more lessons)
- **Grade 11 (done):** `../Curriculum/Grade11_SchemeOfWork/Term{1,2,3}.tex`
  (each `\section{Week N}` → 90-min lesson; `\section{Bonus N}` → B session
  with `sessionType: 'b'` in frontmatter). Context in
  `../Curriculum/PLANNING_HANDOFF_Grade11_2027.md`.
- **Grade 10 (done):** `../Curriculum/2027/10th/LaTeX_sources/Term{1,2,3}.tex`
  — three projects: Firefighter Barbie (T1), Desk Organizer (T2), Water Bottle
  reverse-engineering (T3). IGCSE 0445 D&T, Materials option; Papers 1 and 3
  (no Paper 4; no ExamLink; no Resources `route:` — use `href:` only).
- **Grade 12 T1 (done):** 24 weeks (12 W main sessions + 12 B sessions,
  `WEEKS_OVERRIDE[12][1] = 24`), from `../Curriculum/2027/12th/LaTeX_sources/Term1.tex`.
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
1. **Grader URL — DONE (2026-08-10).** `examsUrl` in `src/lib/site.ts` now points at the
   production grader (`exam-grader/grader.html?src=...` Apps Script endpoint), not the preview.
2. **Grade 12 T2 + T3** — not yet planned or authored. Placeholder stubs show
   already. Awaiting Andy's curriculum plan for those terms.
3. **Textbook links — COMPLETE (2026-08-04).** All 137 `type: "Textbook"` items resolve to
   the right file at a page inside it: 0 dead, 0 out-of-range, 0 unlinked. Nothing left to
   upload — the 27 extracts cover the whole book (printed 8–376).
4. **Media:** SVG diagrams (authored) for technical concepts where a schematic
   teaches best; real photos (Wikimedia Commons, openly licensed, credited — see §6)
   for physical tools/equipment a student has zero background with; Watch/See =
   web-searched candidates the user approves (never auto-search, never fabricate
   URLs). Never fabricate a photo of a real person or claim a generated image is
   real. **G10/G11 audit done (2026-08-06/07)** — structures, mechanics, circuits,
   manufacturing processes and testing equipment all now have a diagram or photo;
   materials (MDF/acrylic/plywood/etc.) were deliberately deprioritised since
   students handle them physically most weeks. Not yet audited: G12.
5. **CI nicety:** deploy workflow actions log a "Node 20 deprecated" warning — bump
   `actions/checkout`, `setup-node`, `upload-pages-artifact` versions sometime.
6. **About page — built, NOT pushed.** `src/pages/about.astro`, `public/about/`,
   the footer link (`Footer.astro`) and the `about` route (`url.ts`) are complete
   and committed-ready but deliberately held out of every push so far — Andy
   wants to decide separately when it goes live. Check `git status` before
   assuming a "push everything" instruction includes it; ask if unclear.
7. **GitHub Actions/Pages outages happen and look like your fault.** Hit one
   2026-08-06: `git push` succeeded but the deploy workflow failed at job setup
   ("Service Unavailable" resolving action images) and later hung in "waiting"
   indefinitely — not a code problem. Check
   `curl -s https://www.githubstatus.com/api/v2/summary.json` before assuming a
   broken push or a broken workflow; retrying mid-outage just repeats the same
   failure. A `git push` succeeding does **not** mean the Pages deploy ran —
   they're separate steps; check `gh run list` too.
8. **MDX bare `{...}` outside a code span breaks the build.** Hit this twice —
   once from `Table~\ref{...}` in prose, once from a `<style>` block with real
   CSS braces (`{ display: grid; }`). MDX parses any `{...}` in body content as a
   JS expression, code fences and inline `` `code` `` spans excepted. Wrap
   LaTeX-ish snippets in backticks; for layout, use inline `style="..."`
   attributes on a `<div>` instead of a `<style>` block in lesson MDX.

## 9. Working style (the user's established preference)
**Discuss before implementing** on significant decisions: propose + recommend, get
an explicit go-ahead, then build; review phase-by-phase. The user likes
conversational discussion over multiple-choice prompts. Honest reality-checks are
valued over yes-man agreement.
