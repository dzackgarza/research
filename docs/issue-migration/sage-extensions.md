# Preamble issue programme: migration to `dzackgarza/sage-extensions`

Every row of the former `TODO.md` described work on what is now the `sage-extensions`
library, tracked in this repository. This file records the factoring, the evidence for it,
and the issue bodies to post upstream. Nothing here is this repository's work.

## Why this is not `research` work

Three checks, each reproducible from the tree:

1. **The preamble is a shim here.** `src/dzack_research/preamble/` is two files and about
   12 KB. `all.py` is `from sage_extensions.all import *` plus a session-module
   registration; `__init__.py` is a docstring. The categories, modules, algebras, schemes,
   lattices and engines that the issue bodies cite are not in this tree.

2. **The cited paths do not resolve here.** Issue #482 (`lattice-mor-stays-in-the-preamble`)
   cites `src/dzack_research/preamble/categories/lattices.py:1444` as the site that violates
   the rule. That path does not exist in this repository; the file is
   `sage_extensions/categories/lattices.py`, and at the retained pin its line 1444 is inside
   `_indefinite_binary_representation`, not `Mor`. The issue is not merely filed against the
   wrong repository --- its evidence has drifted out of date as well, so it cannot be settled
   from the text it carries.

3. **The library is an external dependency.** `pyproject.toml` declares
   `sage-extensions @ git+https://github.com/dzackgarza/sage-extensions`, alongside
   `sage-categories`, `pandoc-config`, `sage-julia-bridge` and `vinal`. This repository
   consumes the library; it does not build it.

The programme's own text agrees: `TODO.md` opened as "Preamble work issues" and every
milestone reconciles "its complete mathematics with `lean-categories`, its semantic execution
with the `lean-cas-dsl` kernel, and its computations with leaf registrations" --- three
repositories, none of them this one.

Scale: **134 leaf issues** under **7 cluster parents**.

## The seven clusters

| Former `TODO.md` section | `research` issue | Leaves | Proposed `sage-extensions` title |
| --- | --- | --- | --- |
| M1 — Shared correctness and daily mathematical constructions | #417 | 52 | Phase: shared correctness and daily mathematical constructions |
| Reusable lattice and group computations | #415 | 2 | Phase: reusable lattice and group computations |
| Specialized port computation and acceptance | #416 | 3 | Phase: specialized port computation and acceptance |
| M4 — Required mathematical expansion | #420 | 49 | Phase: required mathematical expansion |
| M2 — API review and retained core closure | #418 | 15 | Phase: API review and retained core closure |
| M3 — Complete mathematical acceptance | #419 | 7 | Phase: complete mathematical acceptance |
| M5 — Optional research extensions | #421 | 6 | Phase: optional research extensions |

## Issue bodies to post upstream

Each body keeps the source identifiers, so a leaf closed upstream can be traced back to the
`research` issue that named it. Acceptance criteria stay in the existing issue bodies, which
are already written against the library and need no rewriting; the migration is of owner,
not of contract.

### Phase: shared correctness and daily mathematical constructions

```markdown
Migrated from dzackgarza/research#417 (`M1 — Shared correctness and daily mathematical constructions`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #417 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (52):
- `mor-hom-expectation-ruling` (was dzackgarza/research#492)
- `core-property-construction` (was dzackgarza/research#556)
- `division-algebras-are-placed-by-construction` (was dzackgarza/research#451)
- `ring-sizes-follow-construction` (was dzackgarza/research#450)
- `effective-categorical-constructions` (was dzackgarza/research#428)
- `pullbacks-in-every-category` (was dzackgarza/research#514)
- `named-notions-unfolded-population` (was dzackgarza/research#485)
- `modules-over-a-group-algebra-keep-the-module-axioms` (was dzackgarza/research#443)
- `modules-call-on-a-set-is-the-free-module` (was dzackgarza/research#461)
- `cat-declares-the-owned-objects` (was dzackgarza/research#470)
- `arrows-compare-through-richcmp` (was dzackgarza/research#453)
- `an-object-lies-in-several-slices` (was dzackgarza/research#468)
- `module-and-algebra-slice-objects-lie-in-their-slice` (was dzackgarza/research#469)
- `every-arrow-is-an-element-of-its-mor` (was dzackgarza/research#454)
- `objects-of-sets-answer-their-endomorphisms` (was dzackgarza/research#458)
- `maximal-and-prime-ideals-are-presented` (was dzackgarza/research#444)
- `native-rings-are-constructed-not-adopted` (was dzackgarza/research#447)
- `adopted-rings-declare-their-construction-data` (was dzackgarza/research#467)
- `objects-ask-the-mor-of-their-ambient-category` (was dzackgarza/research#435)
- `graded-modules-ask-their-mor-of-the-endpoints` (was dzackgarza/research#457)
- `equivariant-module-maps-give-their-natural-transformation` (was dzackgarza/research#456)
- `restricted-algebras-are-restricted-modules` (was dzackgarza/research#478)
- `internal-mor-inclusion-starts-at-the-mor-module` (was dzackgarza/research#479)
- `restricted-mors-decide-membership-by-their-predicate` (was dzackgarza/research#481)
- `algebra-arrows-are-ring-arrows` (was dzackgarza/research#459)
- `power-algebra-identity` (was dzackgarza/research#460)
- `unital-algebras-supply-their-unit` (was dzackgarza/research#462)
- `derivation-spaces-read-declared-data` (was dzackgarza/research#463)
- `group-resolution-augmentation-terminates` (was dzackgarza/research#464)
- `augmented-algebras-retain-their-defining-data` (was dzackgarza/research#483)
- `finite-galois-stages-answer-as-their-fields` (was dzackgarza/research#484)
- `infinite-index-additive-product-placement` (was dzackgarza/research#430)
- `centres-of-algebras-on-infinitely-generated-modules` (was dzackgarza/research#452)
- `abelian-groups-are-z-modules` (was dzackgarza/research#533)
- `rings-of-integers-are-dedekind-by-construction` (was dzackgarza/research#449)
- `covering-families-cover-their-space` (was dzackgarza/research#471)
- `gluing-accepts-isomorphisms-on-overlaps` (was dzackgarza/research#472)
- `base-change-structure-morphisms-land-in-their-mor` (was dzackgarza/research#473)
- `native-free-algebras-answer-their-variable` (was dzackgarza/research#474)
- `nonaffine-structure-sheaf-coverage` (was dzackgarza/research#499)
- `sheaves-compute-sections-on-opens` (was dzackgarza/research#500)
- `arrow-class-subcategories-admit-their-arrows` (was dzackgarza/research#477)
- `marked-schemes-construct-on-the-owner-route` (was dzackgarza/research#476)
- `symbolic-expressions-are-no-owned-ring` (was dzackgarza/research#446)
- `the-real-line-is-a-smooth-manifold` (was dzackgarza/research#434)
- `function-spaces-are-subobjects-of-mor` (was dzackgarza/research#433)
- `group-categories-defined-by-data` (was dzackgarza/research#432)
- `lattice-mor-stays-in-the-preamble` (was dzackgarza/research#482)
- `brauer-characters-are-maps-on-p-regular-elements` (was dzackgarza/research#480)
- `coxeter-diagrams-construct-from-their-data` (was dzackgarza/research#439)
- `coxeter-diagram-orders-are-owned-posets` (was dzackgarza/research#441)
- `partially-ordered-sets-have-monotone-maps` (was dzackgarza/research#442)
```

### Phase: reusable lattice and group computations

```markdown
Migrated from dzackgarza/research#415 (`Reusable lattice and group computations`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #415 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (2):
- `construction-cost-on-resumed-routes` (was dzackgarza/research#422)
- `port-configurations-cones-and-integral-lifts` (was dzackgarza/research#423)
```

### Phase: specialized port computation and acceptance

```markdown
Migrated from dzackgarza/research#416 (`Specialized port computation and acceptance`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #416 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (3):
- `port-rank-three-isotropic-traversal` (was dzackgarza/research#424)
- `port-nonscalar-component-centralizers` (was dzackgarza/research#425)
- `port-handoff-frozen-acceptance` (was dzackgarza/research#426)
```

### Phase: required mathematical expansion

```markdown
Migrated from dzackgarza/research#420 (`M4 — Required mathematical expansion`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #420 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (49):
- `geometry-stub-operations-compute` (was dzackgarza/research#501)
- `orthogonal-groups-of-direct-sums` (was dzackgarza/research#506)
- `higher-rank-integral-lattice-representation` (was dzackgarza/research#505)
- `lattice-glue-stabilizers` (was dzackgarza/research#515)
- `filtered-objects-and-associated-graded` (was dzackgarza/research#534)
- `filtered-scalar-extension-and-conjugation` (was dzackgarza/research#535)
- `pure-and-mixed-hodge-structures` (was dzackgarza/research#536)
- `hodge-tensors-pairings-and-polarizations` (was dzackgarza/research#537)
- `k3-hodge-and-partner-foundations` (was dzackgarza/research#532)
- `hodge-lattice-isometries` (was dzackgarza/research#538)
- `hodge-isometry-subgroup-computation` (was dzackgarza/research#539)
- `k3-surfaces-and-cohomology` (was dzackgarza/research#540)
- `genus-finiteness-parity-and-classification` (was dzackgarza/research#531)
- `pontryagin-duality` (was dzackgarza/research#512)
- `group-exact-sequences-and-homology` (was dzackgarza/research#513)
- `signed-discriminant-lifting-obstructions` (was dzackgarza/research#542)
- `k3-ample-cones-and-stabilizers` (was dzackgarza/research#541)
- `k3-automorphisms-by-torelli` (was dzackgarza/research#543)
- `k3-fourier-mukai-partner-count` (was dzackgarza/research#545)
- `k3-families-on-threefolds` (was dzackgarza/research#544)
- `k3-brauer-groups-and-classes` (was dzackgarza/research#546)
- `k3-mukai-lattices-and-vectors` (was dzackgarza/research#547)
- `k3-sheaf-moduli-and-caldararu-classes` (was dzackgarza/research#548)
- `discriminant-lagrangian-elements-and-subsets` (was dzackgarza/research#549)
- `complex-realization-is-a-functor` (was dzackgarza/research#527)
- `complete-intersection-hodge-sources` (was dzackgarza/research#528)
- `complete-intersection-hodge-structure` (was dzackgarza/research#529)
- `optional-manifold-tangent-bundles` (was dzackgarza/research#553)
- `simplicial-and-cw-foundations` (was dzackgarza/research#517)
- `integral-affine-polyhedral-p1` (was dzackgarza/research#518)
- `integral-affine-polyhedral-p2` (was dzackgarza/research#519)
- `integral-affine-polyhedral-p3` (was dzackgarza/research#520)
- `integral-affine-polyhedral-p4` (was dzackgarza/research#521)
- `integral-affine-polyhedral-p5` (was dzackgarza/research#522)
- `integral-affine-polyhedral-p6` (was dzackgarza/research#523)
- `modular-form-spaces-with-character` (was dzackgarza/research#502)
- `theta-cusp-form-coordinates` (was dzackgarza/research#503)
- `definite-representation-exceptions` (was dzackgarza/research#504)
- `modular-forms-and-hecke-algebras` (was dzackgarza/research#525)
- `higher-signature-reflection-engine-ruling` (was dzackgarza/research#509)
- `higher-signature-reflection-group-search` (was dzackgarza/research#508)
- `hyperbolic-restricted-reflection-engine-ruling` (was dzackgarza/research#511)
- `hyperbolic-restricted-norm-reflection-groups` (was dzackgarza/research#510)
- `lattice-reflection-groups` (was dzackgarza/research#507)
- `coxeter-group-structure` (was dzackgarza/research#516)
- `coxeter-complexes-and-buildings` (was dzackgarza/research#524)
- `satake-diagrams-present-real-forms` (was dzackgarza/research#526)
- `prime-prolongations-from-p-adic-embeddings` (was dzackgarza/research#466)
- `geometric-cards-store-betti-numbers` (was dzackgarza/research#530)
```

### Phase: API review and retained core closure

```markdown
Migrated from dzackgarza/research#418 (`M2 — API review and retained core closure`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #418 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (15):
- `resolution-truncations-in-the-session` (was dzackgarza/research#465)
- `placement-audit` (was dzackgarza/research#429)
- `engine-wiring-audit` (was dzackgarza/research#431)
- `membership-replaces-dynamic-peeking` (was dzackgarza/research#436)
- `session-objects-are-built-by-their-parents` (was dzackgarza/research#440)
- `literal-sets-route-by-membership` (was dzackgarza/research#475)
- `construction-is-instant` (was dzackgarza/research#437)
- `daily-core-exercises` (was dzackgarza/research#438)
- `architecture-remediation` (was dzackgarza/research#486)
- `core-usability-session` (was dzackgarza/research#487)
- `constructor-discovery` (was dzackgarza/research#491)
- `refactor-audit` (was dzackgarza/research#488)
- `type-paydown` (was dzackgarza/research#489)
- `bloat-audit-loop` (was dzackgarza/research#490)
- `minimal-api-freeze` (was dzackgarza/research#493)
```

### Phase: complete mathematical acceptance

```markdown
Migrated from dzackgarza/research#419 (`M3 — Complete mathematical acceptance`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #419 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (7):
- `triage-long-tail` (was dzackgarza/research#496)
- `suite-compactification` (was dzackgarza/research#494)
- `category-method-coverage-sweep` (was dzackgarza/research#495)
- `suite-within-time-gates` (was dzackgarza/research#497)
- `terminal-session` (was dzackgarza/research#498)
- `resumed-handoff-delivery` (was dzackgarza/research#427)
- `extended-mathematics-session` (was dzackgarza/research#550)
```

### Phase: optional research extensions

```markdown
Migrated from dzackgarza/research#421 (`M5 — Optional research extensions`).

This work operates on the `sage_extensions` tree, not on `research`, whose
`src/dzack_research/preamble/` is a two-file re-export of `sage_extensions.all`.
The parent issue in `research` #421 stays open as a pointer until this cluster closes.

Source identifiers carried by this cluster (6):
- `optional-framed-manifolds` (was dzackgarza/research#551)
- `optional-brauer-manin-obstructions` (was dzackgarza/research#552)
- `optional-random-lattices-of-given-invariants` (was dzackgarza/research#554)
- `optional-moduli-of-stable-curves` (was dzackgarza/research#555)
- `optional-database` (was dzackgarza/research#557)
- `optional-engine` (was dzackgarza/research#558)
```

## Full leaf mapping

Every row, in `TODO.md` order, with the `research` issue that currently carries it.

| Cluster | Source identifier | `research` issue |
| --- | --- | --- |
| M1 | `mor-hom-expectation-ruling` | #492 |
| M1 | `core-property-construction` | #556 |
| M1 | `division-algebras-are-placed-by-construction` | #451 |
| M1 | `ring-sizes-follow-construction` | #450 |
| M1 | `effective-categorical-constructions` | #428 |
| M1 | `pullbacks-in-every-category` | #514 |
| M1 | `named-notions-unfolded-population` | #485 |
| M1 | `modules-over-a-group-algebra-keep-the-module-axioms` | #443 |
| M1 | `modules-call-on-a-set-is-the-free-module` | #461 |
| M1 | `cat-declares-the-owned-objects` | #470 |
| M1 | `arrows-compare-through-richcmp` | #453 |
| M1 | `an-object-lies-in-several-slices` | #468 |
| M1 | `module-and-algebra-slice-objects-lie-in-their-slice` | #469 |
| M1 | `every-arrow-is-an-element-of-its-mor` | #454 |
| M1 | `objects-of-sets-answer-their-endomorphisms` | #458 |
| M1 | `maximal-and-prime-ideals-are-presented` | #444 |
| M1 | `native-rings-are-constructed-not-adopted` | #447 |
| M1 | `adopted-rings-declare-their-construction-data` | #467 |
| M1 | `objects-ask-the-mor-of-their-ambient-category` | #435 |
| M1 | `graded-modules-ask-their-mor-of-the-endpoints` | #457 |
| M1 | `equivariant-module-maps-give-their-natural-transformation` | #456 |
| M1 | `restricted-algebras-are-restricted-modules` | #478 |
| M1 | `internal-mor-inclusion-starts-at-the-mor-module` | #479 |
| M1 | `restricted-mors-decide-membership-by-their-predicate` | #481 |
| M1 | `algebra-arrows-are-ring-arrows` | #459 |
| M1 | `power-algebra-identity` | #460 |
| M1 | `unital-algebras-supply-their-unit` | #462 |
| M1 | `derivation-spaces-read-declared-data` | #463 |
| M1 | `group-resolution-augmentation-terminates` | #464 |
| M1 | `augmented-algebras-retain-their-defining-data` | #483 |
| M1 | `finite-galois-stages-answer-as-their-fields` | #484 |
| M1 | `infinite-index-additive-product-placement` | #430 |
| M1 | `centres-of-algebras-on-infinitely-generated-modules` | #452 |
| M1 | `abelian-groups-are-z-modules` | #533 |
| M1 | `rings-of-integers-are-dedekind-by-construction` | #449 |
| M1 | `covering-families-cover-their-space` | #471 |
| M1 | `gluing-accepts-isomorphisms-on-overlaps` | #472 |
| M1 | `base-change-structure-morphisms-land-in-their-mor` | #473 |
| M1 | `native-free-algebras-answer-their-variable` | #474 |
| M1 | `nonaffine-structure-sheaf-coverage` | #499 |
| M1 | `sheaves-compute-sections-on-opens` | #500 |
| M1 | `arrow-class-subcategories-admit-their-arrows` | #477 |
| M1 | `marked-schemes-construct-on-the-owner-route` | #476 |
| M1 | `symbolic-expressions-are-no-owned-ring` | #446 |
| M1 | `the-real-line-is-a-smooth-manifold` | #434 |
| M1 | `function-spaces-are-subobjects-of-mor` | #433 |
| M1 | `group-categories-defined-by-data` | #432 |
| M1 | `lattice-mor-stays-in-the-preamble` | #482 |
| M1 | `brauer-characters-are-maps-on-p-regular-elements` | #480 |
| M1 | `coxeter-diagrams-construct-from-their-data` | #439 |
| M1 | `coxeter-diagram-orders-are-owned-posets` | #441 |
| M1 | `partially-ordered-sets-have-monotone-maps` | #442 |
| Reusable lattice and group computations | `construction-cost-on-resumed-routes` | #422 |
| Reusable lattice and group computations | `port-configurations-cones-and-integral-lifts` | #423 |
| Specialized port computation and acceptance | `port-rank-three-isotropic-traversal` | #424 |
| Specialized port computation and acceptance | `port-nonscalar-component-centralizers` | #425 |
| Specialized port computation and acceptance | `port-handoff-frozen-acceptance` | #426 |
| M4 | `geometry-stub-operations-compute` | #501 |
| M4 | `orthogonal-groups-of-direct-sums` | #506 |
| M4 | `higher-rank-integral-lattice-representation` | #505 |
| M4 | `lattice-glue-stabilizers` | #515 |
| M4 | `filtered-objects-and-associated-graded` | #534 |
| M4 | `filtered-scalar-extension-and-conjugation` | #535 |
| M4 | `pure-and-mixed-hodge-structures` | #536 |
| M4 | `hodge-tensors-pairings-and-polarizations` | #537 |
| M4 | `k3-hodge-and-partner-foundations` | #532 |
| M4 | `hodge-lattice-isometries` | #538 |
| M4 | `hodge-isometry-subgroup-computation` | #539 |
| M4 | `k3-surfaces-and-cohomology` | #540 |
| M4 | `genus-finiteness-parity-and-classification` | #531 |
| M4 | `pontryagin-duality` | #512 |
| M4 | `group-exact-sequences-and-homology` | #513 |
| M4 | `signed-discriminant-lifting-obstructions` | #542 |
| M4 | `k3-ample-cones-and-stabilizers` | #541 |
| M4 | `k3-automorphisms-by-torelli` | #543 |
| M4 | `k3-fourier-mukai-partner-count` | #545 |
| M4 | `k3-families-on-threefolds` | #544 |
| M4 | `k3-brauer-groups-and-classes` | #546 |
| M4 | `k3-mukai-lattices-and-vectors` | #547 |
| M4 | `k3-sheaf-moduli-and-caldararu-classes` | #548 |
| M4 | `discriminant-lagrangian-elements-and-subsets` | #549 |
| M4 | `complex-realization-is-a-functor` | #527 |
| M4 | `complete-intersection-hodge-sources` | #528 |
| M4 | `complete-intersection-hodge-structure` | #529 |
| M4 | `optional-manifold-tangent-bundles` | #553 |
| M4 | `simplicial-and-cw-foundations` | #517 |
| M4 | `integral-affine-polyhedral-p1` | #518 |
| M4 | `integral-affine-polyhedral-p2` | #519 |
| M4 | `integral-affine-polyhedral-p3` | #520 |
| M4 | `integral-affine-polyhedral-p4` | #521 |
| M4 | `integral-affine-polyhedral-p5` | #522 |
| M4 | `integral-affine-polyhedral-p6` | #523 |
| M4 | `modular-form-spaces-with-character` | #502 |
| M4 | `theta-cusp-form-coordinates` | #503 |
| M4 | `definite-representation-exceptions` | #504 |
| M4 | `modular-forms-and-hecke-algebras` | #525 |
| M4 | `higher-signature-reflection-engine-ruling` | #509 |
| M4 | `higher-signature-reflection-group-search` | #508 |
| M4 | `hyperbolic-restricted-reflection-engine-ruling` | #511 |
| M4 | `hyperbolic-restricted-norm-reflection-groups` | #510 |
| M4 | `lattice-reflection-groups` | #507 |
| M4 | `coxeter-group-structure` | #516 |
| M4 | `coxeter-complexes-and-buildings` | #524 |
| M4 | `satake-diagrams-present-real-forms` | #526 |
| M4 | `prime-prolongations-from-p-adic-embeddings` | #466 |
| M4 | `geometric-cards-store-betti-numbers` | #530 |
| M2 | `resolution-truncations-in-the-session` | #465 |
| M2 | `placement-audit` | #429 |
| M2 | `engine-wiring-audit` | #431 |
| M2 | `membership-replaces-dynamic-peeking` | #436 |
| M2 | `session-objects-are-built-by-their-parents` | #440 |
| M2 | `literal-sets-route-by-membership` | #475 |
| M2 | `construction-is-instant` | #437 |
| M2 | `daily-core-exercises` | #438 |
| M2 | `architecture-remediation` | #486 |
| M2 | `core-usability-session` | #487 |
| M2 | `constructor-discovery` | #491 |
| M2 | `refactor-audit` | #488 |
| M2 | `type-paydown` | #489 |
| M2 | `bloat-audit-loop` | #490 |
| M2 | `minimal-api-freeze` | #493 |
| M3 | `triage-long-tail` | #496 |
| M3 | `suite-compactification` | #494 |
| M3 | `category-method-coverage-sweep` | #495 |
| M3 | `suite-within-time-gates` | #497 |
| M3 | `terminal-session` | #498 |
| M3 | `resumed-handoff-delivery` | #427 |
| M3 | `extended-mathematics-session` | #550 |
| M5 | `optional-framed-manifolds` | #551 |
| M5 | `optional-brauer-manin-obstructions` | #552 |
| M5 | `optional-random-lattices-of-given-invariants` | #554 |
| M5 | `optional-moduli-of-stable-curves` | #555 |
| M5 | `optional-database` | #557 |
| M5 | `optional-engine` | #558 |

