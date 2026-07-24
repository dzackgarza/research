# Categorical Presentation — Principles

Distilled from the ratified record on [#251](https://github.com/dzackgarza/research/issues/251) (2026-07-16/17). That record is a progression: later rulings supersede earlier artifacts, and this page carries only the surviving form, with supersession noted where a ruling replaced an earlier one.
Execution artifacts (per-method mappings, generated graphs, the quarry ledger) remain on the issue and its PRs; vocabulary is governed by the [Mathematical Language Style Guide](Mathematical-Language-Style-Guide.md).

## The master principle: propositions become morphisms one level up {#sec-master-principle}

A predicate asserted about a thing at level *n* is replaced by a morphism at level *n*+1, and the assertion becomes a factorization.
A bare declaration ("C is abelian", "this group is finite", "O(L) preserves b") is inert prose — checkable only by a human re-reading it — whereas a morphism is subject to a calculus: it composes, pulls back, whiskers, and satisfies commutativity conditions, so "is this claim consistent with the others?"
becomes "does this diagram commute?"
— a mechanical question.
The whole framework is three moves — **classify, factor, lift** — applied uniformly at every level.

## Classifiers; property / structure / stuff is computed, never declared {#sec-classifiers}

The stuff / structure / property trichotomy and its computation from the classifier `ι_A : S_A → Cat` are @def-property-structure-stuff in the [Mathematical Framework](../framework/Mathematical-Framework.md).
As an authoring rule it is *computed, never declared*: full + replete ⇒ property ("C has A" a proposition, uniqueness of the lift discharged once from fullness); faithful-not-full ⇒ structure (each lift a separate theorem-with-witness); general ⇒ stuff.
A proof that C has A is a lift of the point `1 → Cat` selecting C through `ι_A` (the source is the terminal category, not a one-object full subcategory).
Properties of categories (HasInitial, HasKernels, HasCokernels, HasFiniteProducts) get replete full subcategories of **Cat**; genuine structure (monoidal, preadditive/abelian in Mathlib's packaging) gets a forgetful 2-functor (`MonCat → Cat`), never a subcategory inclusion.
Conflating the two cases was identified as the most consequential language error in the record.

**Formation conventions.** Pullbacks along classifiers are pseudo-pullbacks unless the leg is an isofibration; replete full inclusions are isofibrations, so for properties strict = pseudo.
Every property-defined subcategory is replete (closed under isomorphism); a predicate not invariant under isomorphism may not define a subcategory.
Conservativity is the minimal requirement on "axiomatic" forgetfuls: axioms may cut objects and add data, but must not create isomorphisms.

## Ownership and transport are factorization, not doctrine {#sec-ownership-and-transport}

The transport mechanism — a property `P` at `C` descends along a forgetful `U : C → B` iff it factors through `U`, and is then the pullback `C_P = U^{-1}(B_Q)` — is @def-transport-property.
As an authoring rule it is a definition, not a rule with exceptions: **a property is declared once, at the terminal category through which it factors, and everywhere else it is the pullback** (Mathlib anchor: `ObjectProperty.inverseImage` / `FullSubcategory`). Failure of factorization is the counterexample, stated once: ℤ is finitely generated as a group but not as a monoid, so finite generation does not factor through the monoid forgetful.

The entire derived corpus of subcategories (finite sets, finite abelian groups, finite commutative rings, f.g. free modules, the lattice and discriminant-form categories) is the set of instances of one pullback square.
A manually-declared subcategory that is derivable is a defect — extensional correctness does not excuse hand-instantiation.

## Present, don't enumerate {#sec-present-dont-enumerate}

Declared 1-cells are **adjacent forgetfuls only**; every other functor is generated — a composite, an inverse image, a Grothendieck construction, or induced/whiskered — and is marked generated.
Relations (agreement of alternative composites, distinguished factorizations) are imposed as identifications of composites: named natural isomorphisms, not extra edges.
Two consequences: minimality becomes theorem-shaped (an edge is illegal iff it is a composite of others — checkable), and coherence data becomes visible as a relation between paths instead of vanishing into a direct edge.
The ring diamond (additive vs multiplicative underlying-set composites) is the standing example: drawing the composite hid it; the presentation exposes it, and dropping the multiplicative forgetful makes unit groups unreachable.

Parameterized families are declared at presheaf level, valued in R-Mod when their comparison identities require it (e.g. `polar ∘ diag = 2` does not parse for Set-valued presheaves); element categories, projections, and induced functors (pushforward in the value module, diag, polar, base change) are generated from presheaf-level natural transformations.

## Level 2: comparisons are 2-cells, theorems are lifts {#sec-level-2}

The relationships the project kept needing have no home at level 1; refusing level 2 forces faking them (e.g. `O(L) ↪ Aut(L)` drawn as an edge between fake objects).
In **Cat** as a 2-category:

- **Comparisons between constructions are 2-cells**, usually generated by whiskering: the projection π induces `Aut ⇒ Aut ∘ π`; the discriminant functor induces `O(−) ⇒ O(disc(−))` — components generated, never drawn.

- **Theorems are lifts**: "O(−) lands in finitely presented groups on the definite locus" is a lift of a composite through a replete full inclusion, with a citation as witness.
  A landing refinement is never graph data.

- **Parameters are indices**: a parameter is a variable in a functor category, so its coherence is automatic rather than legislated.

Truncation is content, not decoration: set-level and groupoid-level constructions are not interchanged, and π₀ does not commute with homotopy pullbacks (see the genus ruling in [Settled Mathematical Rulings](../framework/Settled-Mathematical-Rulings.md)).

## Name every section {#sec-name-every-section}

When a classifier is not full, lifts are choices and may be many (R-Mod is monoidal under ⊗ and under ⊕ — genuinely distinct points of the fiber).
Every lift is a separate named theorem row (`RMod^(⊗)`, `RMod^(⊕)`), and every consumer of structure references the named lift, never "the" structure.
An unnamed structure-reference is a defect (lift ambiguity), detectable by grep — it is precisely the drift vector by which one session proves something about ⊕ while a later session silently consumes it for ⊗. Property-level references are exempt because contractibility of the fiber makes them unambiguous.
The subscript goes on the *lift*, never on the classifier: one classifier, many named sections; a classifier node per structure is generator-proliferation one level up.

## Generation discipline {#sec-generation-discipline}

The positive criterion that replaced the growing defect-class list:

> Every category, functor, and subcategory in an artifact must be the image of a named upstream construction (Mathlib declaration or textbook / nLab / Stacks citation) under a small explicit dictionary — and the dictionary **is** the artifact; the diagram is derived from it.

Anything not in the dictionary's image is wrong *by definition*, with no per-defect-class litigation.
Grounding is a **generation constraint, not a post-hoc audit**: generate the artifact as a dictionary from project nouns to standard names and derive the diagram, because generate-then-audit guarantees drift (generation is unconstrained; auditing is lossy across sessions).
In the standard framework the recurring defects are not audited — they are *inexpressible*.

The single per-entry audit question: **is this item at the lowest level at which it is generated?** A declared item provably the image of something one level down — a composite, a whiskering, an induced functor, an implication with witness, a truncation — is a defect, whether the error inflates the level (a set-level construction promoted to a homotopy pullback) or deflates it (a theorem demoted to a definition by nesting one property-cut inside another; implication posets among properties are generated by theorem edges with witnesses, never encoded by nesting definitions).

**Artifacts live as checked data, never as prose to be re-derived per session.** Prose has no diff; regeneration from prose silently deletes ratified structure that no audit rule flags, and vocabulary that exists only in context can be audited for internal consistency but never for correctness against literature.
The presentation is therefore maintained as machine-checked data with standard vocabulary.

The hazards these disciplines guard against — with the mechanism by which each one occurs — are catalogued in the [Design Hazard Ledger](Design-Hazard-Ledger.md); the authoring workflow that applies them is the [Contribution Guidelines](Contribution-Guidelines.md).

## The principles, named {#sec-principles-named}

The disciplines above and their object-level consequences are named for reference; each is developed in the section or ruling cited.

**Meta-conventions — how mathematics is registered here.**

- **M1 — Lowest generating level.** Every item sits at the lowest categorical level at which it is generated; over-leveling and under-leveling are one defect.
  The master audit (Generation discipline, above; [Settled Rulings A1](../framework/Settled-Mathematical-Rulings.md#master-rulings)).

- **M2 — Propositions become morphisms one level up.** A predicate becomes a lift; its class (property / structure / stuff) is *computed* from the classifier, and the vocabulary must respect the computed class (the master principle and the classifier section, above).

- **M3 — Auditability is audience-relative.** A term is admissible iff the working algebraist can detect its misuse; foreign-discipline vocabulary is worse than coinage ([Style Guide P1 / Class A](Mathematical-Language-Style-Guide.md)).

- **M4 — The artifact is the dictionary; the diagram is its image.** Generate-then-audit is forbidden; the registered object is checked data, never prose to be re-derived (Generation discipline, above).

- **M5 — Naming scales with non-fullness.** Where a classifier is full, reference without naming is sound; where it is not, every consumer names its section (Name every section, above).

- **H1 — Homological presentation** *(peer of M1).* A property is defined by the exact sequence it sits in and the invariants that sequence exposes, not by a condition on a single map ([Settled Rulings A5](../framework/Settled-Mathematical-Rulings.md#master-rulings)).

**Object-conventions — what the mathematics is.**

- **O1 — One primitive per family, parametrized.** Right modules are $\mathrm{Mod}_{R^{\mathrm{op}}}$; $O(L)$ is $\operatorname{Aut}(L)$; $\mathbf{Ab}$ is the $\mathbb{Z}$-fiber.
  First-class treatment of a generic's instance is a defect ([Settled Rulings A2](../framework/Settled-Mathematical-Rulings.md#master-rulings)).

- **O2 — The datum of a form is the $W$-valued form**, never the map to a dual (that is derived polarization) (@sec-forms).

- **O3 — Predicates own at their factoring node; transport is pullback.** The domain of transport is properties of underlying data; finite generation is the boundary counterexample (Ownership and transport, above; [Settled Rulings A3](../framework/Settled-Mathematical-Rulings.md#master-rulings)).

- **O4 — Implications are witnessed theorem edges, not nested definitions** (Level 2, above).

- **O5 — Everything up to equivalence**; strict category-equalities are forbidden and each canonical equivalence carries a named witness ([Settled Rulings A4](../framework/Settled-Mathematical-Rulings.md#master-rulings)).

- **O6 — Truncation level is content and must be stated** (Level 2, above; the genus ruling).
