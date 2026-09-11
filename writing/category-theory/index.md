# Categorical and arithmetic foundations

Categorical and arithmetic foundations support the lattice research code, its Sage implementation, and its Lean formalization.

The three parts are a single chain, and each one is used by the next.

**Foundations** fixes the setting: higher categories and universes, the categorical constructions, truncation and the classifiers that both limits and monoidal structure are stated with, limits and colimits, loops and suspension, and what an identification and an equality are.

**Algebraic structure** builds algebra on that setting: categories presented by operations, monoidal structure and the internal algebraic objects it carries, modules and base change, generating families and presentations, joins meets and closure, the distinguished functors, elements and containment, and generic elements with their hypotheses and localization.

**Forms, lattices, and Witt theory** is one dependency chain in its own order.
A bilinear or quadratic form comes first, then forms on the underlying module of an algebra, then a lattice and its discriminant form, then isometries and arithmetic invariants, then Coxeter systems.
The hyperbolic form and the Witt class follow, then the stable category of modules with duality the Witt class lives in, and finally the morphisms and the chain complexes built over that category.

**Authoring and reference** holds the mathematical language style guide and the sources the framework draws on.

## The category and functor diagram

The diagram below is the framework at a glance: the sequence of categories, functors and
invariant maps running from modules, through the form categories, to integral lattices
and on to the discriminant and genus invariants. Every arrow is labelled by its functor
or map. The discriminant construction is drawn on category cores, and the genus is the
fibre of the displayed map on isometry classes over the image of a lattice class.

A category, functor or map shown here refers to its mathematical definition in the
chapters above; the GraphViz identifier is only its implementation label. The editable
source is [`category-graph.dot`](category-graph.dot), and `just graph` re-renders the
interactive view from it.

```{=html}
<iframe src="category-graph.html" title="Interactive category and functor diagram"
        style="width:100%;height:78vh;border:1px solid var(--bs-border-color,#e5e7eb);border-radius:8px"
        loading="lazy"></iframe>
```

[Open the diagram fullscreen](category-graph.html). Scroll to zoom and drag to pan.

The exhaustive Sage runtime hierarchy is recorded separately in the
[SageMath category framework reference](https://github.com/dzackgarza/research/blob/main/docs/sage-inventory/Sage-Category-Framework-Inventory.md),
which is implementation reference rather than part of this book.
