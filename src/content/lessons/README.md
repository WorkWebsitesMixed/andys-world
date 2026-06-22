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
`<ExamLink to="paper1|paper4|project|igcse">…</ExamLink>` (Grade 11 reference pages).

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
