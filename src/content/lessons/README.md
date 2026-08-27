# Authoring lessons

One `.mdx` file = one class. **Routing comes from the frontmatter** (`grade` /
`term` / `week`), not the file path — but the convention is:

```
src/content/lessons/grade-<n>/t<term>-w<week>.mdx
e.g. grade-12/t1-w1.mdx
```

A placeholder week (no file yet) renders a "this lesson is being prepared" page
automatically, so you can fill terms in any order.

## Frontmatter (all required except `draft`)

```yaml
---
grade: 12            # 10 | 11 | 12
term: 1              # 1 | 2 | 3
week: 1              # 1–10
title: "Lesson title"
topic: "Short tag"   # shown on the week card
learningGoal: "…"    # completes "By the end of this class I will …"
selGoal: "…"         # the social/emotional goal, same stem
draft: false         # true = hidden in production, visible in `npm run dev`
---
```

The two goals are rendered for you from the frontmatter — don't repeat them in the
body. Write the body in the order below.

## Components available in any lesson (no import needed)

Content blocks (each renders its own titled section):
`<KeyTerms terms={[{term,definition}]} />` ·
`<WorkedExample title="…"> …ordered list… </WorkedExample>` ·
`<Activity title="…" time="…" grouping="…" materials={[…]}> … </Activity>` ·
`<SelfCheck questions={[{q,options,answer,hint,explain}]} />` (answer = 0-based index;
give **both** a `hint` shown on a wrong answer and an `explain` shown when correct) ·
`<Resources items={[{label,href?,type?}]} />` ·
`<Reflection prompt="…" />`

Helpers:
`<Callout type="info|tip|warn|exam" title="…" id?="…"> … </Callout>` (give an exam
callout `id="why"` to put it in the side navigator) ·
`<Section title="…" id="…"> … </Section>` (free prose section) ·
`<Support title="Need a hand?"> … </Support>` (collapsible scaffold) ·
`<Extension title="Go deeper"> … </Extension>` (optional stretch) ·
`<Figure src="…" alt="…" caption="…" />` (alt text required) ·
`<WatchSee items={[{label,href,kind?,note?}]} />` (curated external video links) ·
`<ExamLink to="paper1|paper4|project|igcse">…</ExamLink>` (Grade 11 reference pages) ·
`<Formula … />` (see below).

## Maths

Never write an equation as plain prose (`Stress = Force / Area`) — it reads as text and
does not match the exam paper or the textbook.

**Inside a sentence**, use `$…$`: "the factor of safety $\text{FoS} = 4.0$ means…".
**On its own line**, use `$$…$$`. Both are rendered to static MathML + HTML at build
time, so there is no client-side JavaScript and screen readers get real maths.

**For a calculation, use `<Formula>`** — it lays the work out the way the mark scheme
wants it, one stage per line:

```mdx
<Formula
  name="Factor of safety"
  equation="\text{FoS} = \frac{\text{Failure Load}}{\text{Working Load}}"
  substitution="\text{FoS} = \frac{200\ \text{N}}{50\ \text{N}}"
  result="\text{FoS} = 4.0"
  note="A FoS of 4 is a comfortable margin for a domestic shelf."
/>
```

Only `equation` is required — drop `substitution`/`result` to state a formula in the
abstract. Paper 4 Section B gives method marks for the rearranged formula and the
substituted values, so show all three stages whenever there are numbers.

**Define every term.** A formula that introduces a new quantity must carry `terms`,
which renders a "where …" list under the working — the way a textbook and a mark
scheme both present it. `symbol` is TeX without delimiters so it matches the
equation exactly; `unit` is optional but include it unless the quantity genuinely
has none (write `"no unit"` for a ratio like FoS).

```mdx
<Formula
  name="Stress"
  equation="\text{Stress} = \frac{\text{Force}}{\text{Area}}"
  terms={[
    { symbol: "\\text{Stress}", meaning: "the share of the load carried by each square millimetre of cross-section", unit: "N/mm² (= MPa)" },
    { symbol: "\\text{Force}", meaning: "the load pushing or pulling on the member", unit: "N" },
    { symbol: "\\text{Area}", meaning: "the cross-sectional area carrying that load", unit: "mm²" },
  ]}
/>
```

Repeat instances of the same formula inside a `<WorkedExample>` may omit `terms` —
the symbols are already defined higher up the page, and repeating them three times
is noise. Every symbol must be defined *somewhere* on its page.

**Where you'll see this.** A new concept or formula should be followed by a
`<Callout type="info" title="Where you'll see this">` giving two or three places a
student meets it outside school — a door handle for moments, a stiletto heel for
stress, a lift capacity plate for factor of safety. Concrete and everyday beats
impressive: the test is whether they could go and look at it today.

Conventions: `\text{…}` for words and units so they are upright, `\ ` for the thin gap
before a unit (`200\ \text{N}`), `\times` for multiplication (never a letter `x`),
`\frac{}{}` for division, and `{,}` for a thousands separator (`80{,}000`).

Use `\frac` inside a sentence and reserve `\dfrac` for a fraction that stands on its own
line — `\dfrac` forces a full-size fraction, which makes surrounding lines sit unevenly.

Note for Grade 12 Excel lessons: `$` for absolute references is safe inside backticks
or a code fence, which is where it already lives. Do not write a bare `$B$2` in prose —
it would be parsed as maths.

**Never import anything in lesson files** — all components and route helpers are injected automatically.
For inline links to the exam hub pages, use `<ExamLink to="project|paper1|paper4|igcse">`.
For Resources items that point to internal pages, use `route:` instead of `href:`:
`{ label: "The Project", route: "project", type: "Link" }` — no import needed.

## House structure (the locked lesson pattern)

1. A short lead hook (renders as the lede).
2. `<Callout type="exam" title="Why this matters" id="why">` — link the first exam mention with `<ExamLink>`.
3. `<KeyTerms … />`
4. `<Section title="The lesson" …>` with `###` sub-sections (drop a diagram if one fits).
5. `<WorkedExample … />`
6. `<Activity … />`
7. `<Support … />`
8. `<SelfCheck … />`
9. `<Section title="Homework & extension" …>` containing the homework + an `<Extension>`.
10. `<Resources … />`
11. `<Reflection prompt="…" />`

Grade 11 is the worked reference — copy any `grade-11/*.mdx` file as a starting point.
