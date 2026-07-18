# Lattice Research — Wiki

Durable narrative for the lattice-category project.
Live execution state is the GitHub [issue tree](https://github.com/dzackgarza/research/issues/46); this wiki is the readable projection and the "why."

## Map

- **[Roadmap](Roadmap.md)** — the two work buckets (Sage parity vs Fork/extension), the milestone map, the guiding philosophy, and the user-story proof.

- **[Mathematical Lexicon](contributing/Mathematical-Lexicon.md)** — the expandable glossary of mathematical objects, constructions, and return contracts used by the project.

- **[SageMath Category Framework Reference](sage/Sage-Category-Framework-Inventory.md)** — the categories, the 51-axiom registry (with owning sites), and the 17 functorial constructions; full source-linked catalogue in [Sage Category Classes](sage/Sage-Category-Classes.md).
  Informing data (source audit, runtime dumps) is tracked in-repo and linked from the page's provenance section.

### Contributing

- **[Contribution Guidelines](contributing/Contribution-Guidelines.md)** — the workflow: derive first, the naming checkpoint, dictionary-first authoring, the A/B/C routing summary, gap recording, correction handling, Lean and prose rules.
  Start here.

- **[Mathematical Language Style Guide](contributing/Mathematical-Language-Style-Guide.md)** — normative vocabulary rules (final edition): audience-relative grounding, the Class A/B/C admissibility taxonomy, the replacement dictionary, audit hooks.

- **[Design Hazard Ledger](contributing/Design-Hazard-Ledger.md)** — recorded hazards with mechanism and standing guard; every guideline traces to at least one entry.

### Doctrine (distilled from the #251 record; later rulings supersede earlier ones)

- **[Mathematical Definitions](framework/Mathematical-Definitions.md)** — the dependency tree of the program's objects, stated as definitions in real MathJax: module categories, axioms as subcategories and the transport rule, the form presheaves and their categories of elements, polarization, the derived arithmetic categories, the discriminant construction, isometry groupoids, genus, constructors.
  The spine the rulings seat under.

- **[Categorical Presentation Principles](contributing/Categorical-Presentation-Principles.md)** — the calculus: classify/factor/lift, property vs structure computed off classifiers, ownership as factorization, generation discipline, named sections, level check.

- **[Settled Mathematical Rulings](framework/Settled-Mathematical-Rulings.md)** — the closed choices, each seated under its definition: nondegenerate vs unimodular, the W-valued form and polarization, the discriminant construction and exact-sequence package, O as an instance of Aut, cardinality/index/genus rulings, relation kinds — each with its supersession trail.

- **[Lean–Sage Integration Model](lean/Lean-Sage-Integration-Model.md)** — layering, the A/B/C routing model, ForMathlib contract, registry semantics, cop-out visibility.

**Interactive:** the [generating graph](generating-graph.html) — the pan/zoom canvas of the category-and-functor graph from the research#251 record.

More pages (user stories, feature doctrine, proof burdens) will be linked here as they land.
