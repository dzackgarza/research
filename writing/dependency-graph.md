---
unit: reference
---

# Dependency graph {#sec-dependency-graph}

Each numbered block is a node. An arrow from $a$ to $b$ means that the statement of $a$, or its proof, cites $b$. So the references are the whole record of what a block uses, and a result used without a reference is missing from this graph.

Choose a block to see what it rests on, what rests on it, or both, to a chosen depth. Click a node to move to it; the link under the graph opens the block in its chapter. The render builds the graph from the chapter sources. The same graph is in [GraphML](dependency-graph/dependency-graph.graphml), [DOT](dependency-graph/dependency-graph.dot) and [node-link JSON](dependency-graph/dependency-graph.json).

```{=html}
<div class="depgraph">
  <div class="depgraph-controls">
    <input id="depgraph-search" list="depgraph-blocks" placeholder="Theorem 3.10, def:universe, a title ..." autocomplete="off">
    <datalist id="depgraph-blocks"></datalist>
    <label><input type="radio" name="depgraph-dir" value="uses" checked> rests on</label>
    <label><input type="radio" name="depgraph-dir" value="usedby"> rests on it</label>
    <label><input type="radio" name="depgraph-dir" value="both"> both</label>
    <label>depth <select id="depgraph-depth"><option>1</option><option>2</option><option>3</option><option value="0">all</option></select></label>
  </div>
  <div id="depgraph-selected"></div>
  <div id="depgraph-canvas"></div>
  <details id="depgraph-findings"><summary></summary><ul></ul></details>
</div>
<style>
  .depgraph-controls { display: flex; flex-wrap: wrap; gap: .75rem; align-items: center; margin-bottom: .5rem; }
  #depgraph-search { flex: 1 1 18rem; min-width: 0; padding: .3rem .5rem; }
  #depgraph-canvas { height: 70vh; border: 1px solid var(--bs-border-color, #ccc); border-radius: 4px; }
  #depgraph-selected { min-height: 1.5rem; margin-bottom: .5rem; }
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/dagre/0.8.5/dagre.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/cytoscape-dagre@2.5.0/cytoscape-dagre.js"></script>
<script>
(async () => {
  const base = "dependency-graph/";
  const [graph, findings] = await Promise.all([
    fetch(base + "dependency-graph.json").then(r => r.json()),
    fetch(base + "dependency-findings.json").then(r => r.json()),
  ]);
  const name = n => n.label || n.id;
  const href = n => n.chapter.replace(/\.md$/, ".html") + "#" + n.id;
  const nodes = new Map(graph.nodes.map(n => [n.id, n]));

  const list = document.getElementById("depgraph-blocks");
  const byText = new Map();
  for (const n of graph.nodes) {
    const text = `${name(n)} — ${n.title || n.id}`;
    byText.set(text, n.id); byText.set(n.id, n.id); byText.set(name(n), n.id);
    const option = document.createElement("option"); option.value = text; list.append(option);
  }

  const style = getComputedStyle(document.body);
  const cy = cytoscape({
    container: document.getElementById("depgraph-canvas"),
    maxZoom: 1.5,
    elements: [
      ...graph.nodes.map(n => ({ data: { ...n, name: name(n) } })),
      ...graph.edges.map(e => ({ data: { id: e.source + "->" + e.target, source: e.source, target: e.target } })),
    ],
    style: [
      { selector: "node", style: { label: "data(name)", "font-size": 10, color: style.color,
          "background-color": "#6c8ebf", width: 12, height: 12, "text-valign": "bottom" } },
      { selector: 'node[kind = "definition"]', style: { "background-color": "#82b366" } },
      { selector: 'node[kind = "theorem"], node[kind = "proposition"], node[kind = "lemma"], node[kind = "corollary"]',
        style: { "background-color": "#b85450" } },
      { selector: "node.focus", style: { width: 20, height: 20, "border-width": 3, "border-color": style.color } },
      { selector: "edge", style: { width: 1, "curve-style": "bezier", "target-arrow-shape": "triangle",
          "line-color": "#999", "target-arrow-color": "#999" } },
    ],
  });

  const direction = () => document.querySelector('input[name="depgraph-dir"]:checked').value;
  function show(id) {
    const node = cy.getElementById(id);
    if (node.empty()) return;
    const dir = direction();
    const depth = Number(document.getElementById("depgraph-depth").value) || Infinity;
    const reach = step => {
      let found = node, frontier = node;
      for (let d = 0; d < depth && frontier.nonempty(); d++) {
        frontier = step(frontier).nodes().difference(found);
        found = found.union(frontier);
      }
      return found;
    };
    let kept = node;
    if (dir !== "usedby") kept = kept.union(reach(c => c.outgoers()));
    if (dir !== "uses") kept = kept.union(reach(c => c.incomers()));
    const keep = kept.union(kept.edgesWith(kept));
    cy.elements().style("display", "none");
    keep.style("display", "element");
    cy.nodes().removeClass("focus"); node.addClass("focus");
    keep.layout({ name: "dagre", rankDir: "TB", nodeSep: 70, rankSep: 50 }).run();
    const n = nodes.get(id);
    const selected = document.getElementById("depgraph-selected");
    selected.replaceChildren();
    const a = document.createElement("a"); a.href = href(n); a.textContent = name(n);
    selected.append(a, ` ${n.title ? "— " + n.title.replace(/\$([^$]+)\$/g, "\\($1\\)") : ""} (${keep.nodes().length - 1} other blocks)`);
    if (window.MathJax?.typesetPromise) MathJax.typesetPromise([selected]);
  }

  document.getElementById("depgraph-search").addEventListener("change", e => {
    const id = byText.get(e.target.value.trim()); if (id) show(id);
  });
  document.querySelectorAll('input[name="depgraph-dir"], #depgraph-depth').forEach(r => r.addEventListener("change", () => {
    const focus = cy.nodes(".focus"); if (focus.nonempty()) show(focus.id());
  }));
  cy.on("tap", "node", e => show(e.target.id()));
  cy.elements().style("display", "none");

  const box = document.getElementById("depgraph-findings");
  box.querySelector("summary").textContent = `${findings.length} findings: circular definitions or proofs, blocks without ids`;
  for (const f of findings) {
    const li = document.createElement("li");
    li.append(`${f.kind} in ${f.chapter}: `);
    for (const id of f.blocks) {
      const n = nodes.get(id);
      if (!n) { li.append(` @${id}`); continue; }
      const a = document.createElement("a"); a.href = href(n); a.textContent = name(n);
      li.append(" ", a);
    }
    box.querySelector("ul").append(li);
  }
})();
</script>
```
