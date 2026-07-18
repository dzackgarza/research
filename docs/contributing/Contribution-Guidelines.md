# Contribution Guidelines

Forward-facing workflow for contributing to the Lean/Sage alignment work.
Doctrine lives in [Categorical Presentation Principles](Categorical-Presentation-Principles.md) and [Settled Mathematical Rulings](../framework/Settled-Mathematical-Rulings.md); architecture in the [Lean–Sage Integration Model](../lean/Lean-Sage-Integration-Model.md); vocabulary in the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md).
Each rule below guards one or more entries in the [Design Hazard Ledger](Design-Hazard-Ledger.md) (cited as H*n*).

## Derive first, admit declarations second {#sec-cg-derive-first-admit-declarations-second}

Derive the standard mathematical presentation for your area *before* touching declarations, then decide which existing declarations implement it, which are presentations, and which should be deleted.
Never start from an existing declaration and search for mathematics to justify it (H1). A checked identification with upstream mathematics is not admission: a proof that a local declaration agrees with a standard one is evidence it is redundant or misplaced, and the right-to-exist question is settled before any identification is proved (H2).

## Introducing any name is the checkpoint {#sec-cg-introducing-any-name-is-the-checkpoint}

Before any field, method, type, or category is introduced, state:

- its **typed signature** — functor, natural transformation, object property, invariant on the core, or n-ary operation with typed source (style guide [P2](Mathematical-Language-Style-Guide.md#p2));

- its **mathematical home** — the category it is defined on, with structured objects reaching it through canonical functors, never re-declaring it;

- its **relation kind** to existing mathematics — identity, definitional equality, equivalence, isomorphism, forgetful image, chosen presentation, property, ingredient, or example.
  These are not fungible.

Chosen data (bases, enumerations, coordinates, presentations) are evaluation witnesses, never object structure, homes, or categories (H3). Worked examples are instances of the general construction, never vocabulary (H5).

## Author from the dictionary, not freehand {#sec-cg-author-from-the-dictionary-not-freehand}

Every category, functor, and subcategory you introduce must be the image of a named upstream construction — a Mathlib declaration or a textbook/nLab/Stacks citation — under the artifact's explicit dictionary, and the dictionary is what you author; diagrams and derived structure are generated from it.
Grounding is a generation constraint, not a post-hoc audit (H8, H9). Concretely:

- **Locate first, at lemma granularity.** Search the pinned Mathlib checkout before defining any construction, equivalence, or lemma; compositional expressions (a full subcategory cut by a property, a category of elements, a transported functor) count as existing (H4).

- **Declare at the lowest level.** A declared item provably generable one level down — a composite, whiskering, induced functor, witnessed implication, truncation — is a defect regardless of correctness (H10, H11). Properties are declared once, at the terminal category through which they factor; everywhere else they are pullbacks.

- **Name every section.** Any consumer of non-propositional structure references a named lift (`RMod^(⊗)`, never "the monoidal structure") (H12).

- **Keep artifacts as checked data.** Ratified presentations are machine-checkable data; revisions edit the data and regenerate.
  Prose re-derivation is how ratified structure silently disappears (H9).

## Route through the integration model {#sec-cg-route-through-the-integration-model}

Classify every notion before implementing (details in the [Integration Model](../lean/Lean-Sage-Integration-Model.md)):

- **(A)** Mathlib provides it → wrap and declare its seat; the DSL never holds definitions.

- **(B)** Mathlib lacks it → honest `ForMathlib/` contribution (Mathlib-only imports, upstream target named per declaration, self-contained files preferred), then loop back to (A).

- **(C)** user-approved only → kernel-checked statements with `sorry`d proofs, isolated in the Synthetic layer, each entry queued for formalization.
  Never an unassigned "later" (H15).

Any proof-shaped claim — naturality, limits, route agreement, free/transitive action — gets its statement in Lean; Sage keeps executable conformance only.

## Recording a gap {#sec-cg-recording-a-gap}

A `pending`/no-analog row is a negative claim about Mathlib and is admissible only with search evidence: what was searched, the nearest upstream notions found and *distinguished*, confidence, remaining gaps.
An unsearched row is a TODO, not a gap.
Gaps are enumerated per operation, never grouped; a pending row is honest, a wrong alias is poison.
Every registry report names the most-canonical outstanding gap, and a falsified row means re-deriving the population under the corrected model, never repairing the row (H6).

## Corrections reset, they do not patch {#sec-cg-corrections-reset-they-do-not-patch}

A mathematical-level correction invalidates downstream classifications and edits until the presentation is re-derived — treat the counterexample as evidence about the classifier, not the row (H7). Green builds stay semantically quarantined until the *definitions*, not merely the propositions, are reviewed.
After repeated corrections or forced stops, escalate to specification review and tighter supervision — never conclude that more autonomy is safer (H15).

## Never defer a foundational defect {#sec-cg-never-defer-a-foundational-defect}

Do not postpone a foundational problem because the remaining tasks are mechanical: exporting a malformed foundation multiplies the damage.
Fix or surface it before continuing (H15).

## Lean authoring rules {#sec-cg-lean-authoring-rules}

1. **The pinned checkout is the naming authority — for reviewers too.** Every name/namespace/convention claim, from agents and automated reviewers alike, is verified against the pinned Mathlib checkout before acting; a "Mathlib convention" claim contradicting building usage is presumptively stale (H14).

2. **Prove by bundled transport.** When a datum lifts to a bundled structure (`LinearEquiv`, `Iso`, `Equiv`), derive properties from its API in one word — never componentwise re-proofs.

3. **Mathlib names are anchors, not prose** (style guide [P1b](Mathematical-Language-Style-Guide.md#p1b)): code-formatted in identification columns only.

4. **Cop-outs stay visible.** `sorry`/`admit`, extra axioms, `native_decide`, `unsafe`/`implemented_by`, `partial def` are enumerated by the tree-wide report; the hard gate applies outside the Synthetic layer.

## Prose rules {#sec-cg-prose-rules}

All mathematical prose — issue bodies, plan cards, docstrings, manifest text — follows the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md): corpus-only vocabulary auditable by a working mathematician (H13), one term one type, typed notation, implementation vocabulary quarantined to the implementation map.
Run the guide's audit hooks before shipping any prose artifact.
