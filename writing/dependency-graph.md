---
unit: reference
---

# Dependency graph {#sec-dependency-graph}

Each numbered block is a node. An arrow from $a$ to $b$ means that the statement of $a$, or its proof, cites $b$. So the references are the whole record of what a block uses, and a result used without a reference is missing from this graph.

An arrow is one of two kinds.

- A **uses** arrow, drawn solid, joins two blocks of the logical development: theorems, propositions, lemmas, corollaries, observations, claims, conjectures, definitions, constructions, notations, conventions and assumptions. The statement or proof of $a$ takes $b$ as a premise.
- A **mentions** arrow, drawn dashed, has an example, remark, note, warning, exercise, problem or question at one end. These blocks illustrate or point, or they ask for work that the text does not do. None of them is a premise, so the arrow records a reference and not a dependency.

Each block kind belongs to one side, for the following reason.

| Kind | Side | Reason |
|---|---|---|
| theorem, proposition, lemma, corollary | logical | a stated result with a proof; later results rest on it |
| observation | logical | a stated fact with its proof, so it can be a premise like a lemma |
| claim | logical | a stated result inside a proof, used by the rest of that proof |
| conjecture | logical | a result can be proved conditionally on it |
| definition, construction | logical | it introduces an object that later blocks use |
| notation, convention | logical | it fixes the meaning of symbols that later blocks use |
| assumption | logical | it is a hypothesis of the blocks that cite it |
| example | commentary | it illustrates a result and establishes nothing used later |
| remark, note, warning | commentary | it points to or comments on the development |
| exercise, problem | commentary | it asks for work that the text does not do, so it cannot be a premise |
| question | commentary | it asks whether something holds; it states no fact |

The dependency checker stops with an error on a block kind that is not in this table.

A result of another work is also a node, drawn grey and named by the work's bibliography key and the result: a block that cites `[@AEGS25, Lem. 3.9]` has an arrow to the node "AEGS25 Lem. 3.9". "Theorem 2" and "Thm. 2" name one node. A result taken from a paper is a premise, so the arrow from a block of the logical development is a uses arrow; from a commentary block it is a mentions arrow. Such a result cites nothing in the book, so each chain of uses stops at a definition, at a block with no citations, or at the literature.

A citation of a whole work, as `[@Vin75]`, or of a chapter, a section or a page of one, names no result. It says where something comes from, or it summarizes the work, so it makes no arrow. In a proof it is an **unlocated citation** on the findings list: if the proof rests on one result of the work, the citation names that result, and if it only says where the argument comes from, the attribution goes in the statement or the text around the block.

Only uses arrows can make a definition or a proof circular. So the check for circular definitions and proofs reads the uses arrows only, and a remark and the theorem it discusses can cite each other.

A book editor can run `just book-catalogue --book-tasks` to find passages that need review. An **uncited use** flags a term listed in a declaration's `defines` attribute when its paragraph has no citation to a defining block. Read the passage to identify the intended sense. Cite the definition there, or mark a different sense with a span such as `[right adjoints]{.other-sense}`. A citation in the statement does not identify the premise of a later proof step.

Review the mathematics in each chapter as well. A formula can use a result without repeating any of its terminology. Give each separately used definition or result a label and state its hypotheses. Cite it at the step that uses it. For example, @lem:coble-canonical-boundary-degree uses both additivity and invariance under linear equivalence to compute the canonical degree. Its proof cites both intersection lemmas at the equality they justify.

Run `just book-catalogue` to export the declarations in prerequisite order. Add a block ID to export that declaration with its prerequisites and their source passages.

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
  const href = n => n.chapter.replace(/\.md$/, ".html") + (n.kind === "reference" ? "#ref-" + n.work : "#" + n.id);
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
      ...graph.edges.map(e => ({ data: { id: e.source + "->" + e.target, source: e.source, target: e.target, relation: e.relation } })),
    ],
    style: [
      { selector: "node", style: { label: "data(name)", "font-size": 10, color: style.color,
          "background-color": "#6c8ebf", width: 12, height: 12, "text-valign": "bottom" } },
      { selector: 'node[kind = "definition"]', style: { "background-color": "#82b366" } },
      { selector: 'node[kind = "theorem"], node[kind = "proposition"], node[kind = "lemma"], node[kind = "corollary"]',
        style: { "background-color": "#b85450" } },
      { selector: 'node[kind = "reference"]', style: { "background-color": "#999", shape: "round-rectangle" } },
      { selector: "node.focus", style: { width: 20, height: 20, "border-width": 3, "border-color": style.color } },
      { selector: "edge", style: { width: 1, "curve-style": "bezier", "target-arrow-shape": "triangle",
          "line-color": "#666", "target-arrow-color": "#666" } },
      { selector: 'edge[relation = "mentions"]', style: { "line-style": "dashed",
          "line-color": "#aaa", "target-arrow-color": "#aaa", "target-arrow-shape": "vee" } },
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
  const kindName = { "dangling": "reference to no block", "cycle": "circular uses",
    "orphan-proof": "proof of no block", "duplicate-id": "id defined twice",
    "missing-id": "block without an id", "uncited-term": "uncited use",
    "parse-warning": "pandoc warning", "unlocated-citation": "unlocated citation" };
  const counts = {};
  for (const f of findings) counts[f.kind] = (counts[f.kind] || 0) + 1;
  box.querySelector("summary").textContent = findings.length === 0 ? "0 findings"
    : `${findings.length} findings: ` + Object.entries(counts).map(([k, n]) => `${n} ${kindName[k] || k}`).join(", ");
  for (const f of findings) {
    const li = document.createElement("li");
    li.append(`${kindName[f.kind] || f.kind} in ${f.chapter}: `);
    if (f.kind === "uncited-term") li.append(`“${f.detail}” in`);
    else if (f.kind === "unlocated-citation") li.append(`[${f.detail}] in`);
    else if (f.detail) li.append(f.detail);
    f.blocks.forEach((id, i) => {
      if (f.kind === "uncited-term" && i === 1) li.append(", defined in");
      const n = nodes.get(id);
      if (!n) { li.append(` @${id}`); return; }
      const a = document.createElement("a"); a.href = href(n); a.textContent = name(n);
      li.append(" ", a);
    });
    box.querySelector("ul").append(li);
  }
})();
</script>
```
