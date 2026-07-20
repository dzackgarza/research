# Lattice Research — Wiki

Durable narrative for the lattice-category project.
Live execution state is the GitHub [issue tree](https://github.com/dzackgarza/research/issues/46); this wiki is the readable projection and the "why."

## Map

- **[Roadmap](Roadmap.md)** — the two work buckets (Sage parity vs Fork/extension), the milestone map, the guiding philosophy, and the user-story proof.

- **[Lexicon](contributing/Mathematical-Lexicon.md)** — the expandable glossary of mathematical objects, constructions, and return contracts used by the project.

- **[SageMath Category Framework Reference](sage/Sage-Category-Framework-Inventory.md)** — the categories, the 51-axiom registry (with owning sites), and the 17 functorial constructions; full source-linked catalogue in [Sage Category Classes](sage/Sage-Category-Classes.md).
  Informing data (source audit, runtime dumps) is tracked in-repo and linked from the page's provenance section.

### Contributing

- **[Contribution Guidelines](contributing/Contribution-Guidelines.md)** — the workflow: derive first, the naming checkpoint, dictionary-first authoring, the A/B/C routing summary, gap recording, correction handling, Lean and prose rules.
  Start here.

- **[Language Style Guide](contributing/Mathematical-Language-Style-Guide.md)** — normative vocabulary rules (final edition): audience-relative grounding, the Class A/B/C admissibility taxonomy, the replacement dictionary, audit hooks.

- **[Design Hazard Ledger](contributing/Design-Hazard-Ledger.md)** — recorded hazards with mechanism and standing guard; every guideline traces to at least one entry.

- **[Written Form and Evaluation](contributing/Written-Form-and-Evaluation.md)** — the implementation map from written source to the framework's definitions: source form, parse shapes versus category-owned meaning, the command grammar, evaluation regimes, result status and provenance, separable certification.

### Doctrine (distilled from the #251 record; later rulings supersede earlier ones)

- **[Definitions](framework/Mathematical-Definitions.md)** — the dependency tree of the program's objects, stated as definitions in real MathJax: module categories, axioms as subcategories and the pullback rule, the form presheaves and their categories of elements, polarization, the derived arithmetic categories, the discriminant construction, isometry groupoids, genus, constructors.
  The spine the rulings seat under.

- **[Categorical Presentation Principles](contributing/Categorical-Presentation-Principles.md)** — the calculus: classify/factor/lift, property vs structure computed off classifiers, ownership as factorization, generation discipline, named sections, level check.

- **[Settled Rulings](framework/Settled-Mathematical-Rulings.md)** — the closed choices, each seated under its definition: nondegenerate vs unimodular, the W-valued form and polarization, the discriminant construction and exact-sequence package, O as an instance of Aut, cardinality/index/genus rulings, relation kinds — each with its supersession trail.

- **[Truncation, Classifiers, and Filled Diagrams](framework/Truncation-and-Classifiers.md)** — the general form of the classifier machinery: truncation, element projections as the primitive behind "forgetful," axiom classifiers via classifying pseudofunctors, the trichotomy as fiber truncation, equations as filled-diagram cuts, the operadic coherence tower, and the Set/Cat/∞ stabilization that recovers the strict cases.

- **[Elements and Containment](framework/Elements-and-Containment.md)** — element functors and their corepresenting objects, generalized elements, membership in classifiers as proposition versus fiber, subobjects as carried monomorphisms, underlying containment, embedding existence, well-formedness.

- **[Identification](framework/Identification.md)** — the typed identification claims, the torsor of witnesses, canonical identification by contractible or distinguished comparison, sameness after a functor.

- **[Distinguished Functors](framework/Distinguished-Functors.md)** — distinguished factorizations, the parallel-functor trichotomy, least common category, the statement/construction asymmetry, axioms through functors.

- **[Generic Elements, Hypotheses, and Localization](framework/Generic-Elements.md)** — generic solutions of defining equations, statements with hypotheses, case decomposition without classifier unions, locality by base change and descent.

- **[Lean–Sage Integration Model](lean/Lean-Sage-Integration-Model.md)** — layering, the A/B/C routing model, ForMathlib contract, registry semantics, cop-out visibility.

**Interactive:** [the category graph](lean/Category-Graph.md) — the pan/zoom canvas of the category-and-functor graph, generated from its GraphViz manifest (research#251).

More pages (user stories, feature doctrine, proof burdens) will be linked here as they land.
