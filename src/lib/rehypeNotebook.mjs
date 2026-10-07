/**
 * rehype plugin: mark every table in a lesson as "notebook content".
 *
 * Students are told that everything in a bordered table, a Formula box or the
 * Key terms goes into their notebook. Markdown tables are plain <table> elements
 * with no component behind them, so there is nowhere to hang a label in the MDX.
 * This plugin wraps each one in
 *
 *   <div class="nb nb-table"><p class="nb-tag">✎ Copy into your notebook</p><table>…</table></div>
 *
 * and the styles for `.nb` and `.nb-tag` live in src/styles/global.css. The Formula
 * and KeyTerms components render the same tag themselves.
 *
 * It only touches lessons (files under /content/lessons/): the other collections
 * (sessions, blocks, skills) have their own look and are left alone. It walks the
 * tree by hand instead of using unist-util-visit so it adds no dependency.
 */

/** Build the label paragraph: a hidden-from-screen-readers pencil, then the words. */
const tag = () => ({
  type: 'element',
  tagName: 'p',
  properties: { className: ['nb-tag'] },
  children: [
    {
      type: 'element',
      tagName: 'span',
      properties: { ariaHidden: 'true' },
      children: [{ type: 'text', value: '✎' }],
    },
    { type: 'element', tagName: 'span', properties: {}, children: [{ type: 'text', value: 'Copy into your notebook' }] },
  ],
});

/** Replace each <table> child with a labelled wrapper, recursing into everything else. */
function wrap(node) {
  if (!node.children) return;
  node.children = node.children.map((child) => {
    if (child.type === 'element' && child.tagName === 'table') {
      return {
        type: 'element',
        tagName: 'div',
        properties: { className: ['nb', 'nb-table'] },
        children: [tag(), child],
      };
    }
    wrap(child);
    return child;
  });
}

export default function rehypeNotebook() {
  return (tree, file) => {
    // Astro gives the absolute source path; normalise slashes so this also works on Windows.
    const path = String(file?.path ?? file?.history?.[0] ?? '').replace(/\\/g, '/');
    if (!path.includes('/content/lessons/')) return;
    wrap(tree);
  };
}
