# The category graph

The planning-stage **manifest** of the intended category hierarchy: nodes are categories, edges the preferred forgetful/inclusion functors, and the boxes are the towers of @sec-base-graph — sets & bedrock, the magma tower, rings, modules, forms, and the $\mathbf{Cat}_1$ meta layer.
It records the names and relationships the [Lean–Sage Integration Model](Lean-Sage-Integration-Model.md) is built against; at this stage it is hand-authored, and later Lean implementations are checked for conformance to it.

The source of truth is a GraphViz manifest, [`category-graph.dot`](category-graph.dot) — a plain-text, machine-parseable record of the nodes, clusters, and edges.
`just graph` renders it (`dot -Tsvg`) and injects the result into the pan/zoom view below; the SVG is derived output, so edits happen in the `.dot`. Later, a Lean → manifest exporter can emit the same file from the CatDSL declarations ([#251](https://github.com/dzackgarza/research/issues/251)), closing the loop from Lean source to graph.

```{=html}
<iframe src="category-graph.html" title="Interactive category and functor graph"
        style="width:100%;height:78vh;border:1px solid var(--bs-border-color,#e5e7eb);border-radius:8px"
        loading="lazy"></iframe>
```

[Open the graph fullscreen](category-graph.html) &middot; scroll to zoom, drag to pan.
