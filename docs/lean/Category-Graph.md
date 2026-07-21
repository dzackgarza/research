# Category and functor diagram

The diagram displays the sequence of categories, functors, and invariant maps from
modules through form categories and integral lattices to discriminant and genus
invariants. Every arrow is labeled by its functor or map. The discriminant construction
is shown on category cores, and genus is
the fiber of the displayed map on isometry classes over the image of a lattice class.
The exhaustive Sage runtime hierarchy is recorded separately in the
[SageMath category framework reference](../sage/Sage-Category-Framework-Inventory.md).

The editable source is [`category-graph.dot`](category-graph.dot). The command
`just graph` renders the SVG and inserts it into the interactive view below. A displayed
category, functor, or map refers to its mathematical definition in the theory chapters;
the GraphViz identifier is only its implementation label.

```{=html}
<iframe src="category-graph.html" title="Interactive category and functor diagram"
        style="width:100%;height:78vh;border:1px solid var(--bs-border-color,#e5e7eb);border-radius:8px"
        loading="lazy"></iframe>
```

[Open the diagram fullscreen](category-graph.html). Scroll to zoom and drag to pan.
