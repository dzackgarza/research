# Preamble issue programme: migration to `dzackgarza/sage-extensions`

Every row of the former `TODO.md` described work on what is now the `sage-extensions`
library, tracked in this repository. This file records the factoring, the evidence for it,
and where each work unit lives now. Nothing here is this repository's work.

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

## Clusters and their phases

Executed 2026-11-04. Each open leaf was transferred (`gh issue transfer`) to `sage-extensions`, detached from its research milestone, and attached under the phase below in its research sibling order; the handoff-delivery leaves were absorbed verbatim into the port issues that own them. The research milestone stays open as the cross-repository roadmap node and routes to its phase with an `itree-contract` fence.

| `research` milestone | `sage-extensions` phase | Transferred leaves |
| --- | --- | --- |
| [#417](https://github.com/dzackgarza/research/issues/417) M1 — Daily mathematical work | [#21](https://github.com/dzackgarza/sage-extensions/issues/21) | 71 |
| [#415](https://github.com/dzackgarza/research/issues/415) Immediate priority repairs | [#44](https://github.com/dzackgarza/sage-extensions/issues/44) | 16 |
| [#416](https://github.com/dzackgarza/research/issues/416) Resumed handoff delivery | absorbed verbatim into [sage-indefinite-port#15](https://github.com/dzackgarza/sage-indefinite-port/issues/15), [#18](https://github.com/dzackgarza/sage-indefinite-port/issues/18) and [#33](https://github.com/dzackgarza/sage-indefinite-port/issues/33) | 3 |
| [#420](https://github.com/dzackgarza/research/issues/420) M4 — Required mathematical expansion | [#22](https://github.com/dzackgarza/sage-extensions/issues/22) | 60 |
| [#418](https://github.com/dzackgarza/research/issues/418) M2 — Auditable minimal API | [#23](https://github.com/dzackgarza/sage-extensions/issues/23) | 19 |
| [#419](https://github.com/dzackgarza/research/issues/419) M3 — Compact mathematical test suite | [#24](https://github.com/dzackgarza/sage-extensions/issues/24) | 10 |
| [#421](https://github.com/dzackgarza/research/issues/421) M5 — Optional research extensions | [#25](https://github.com/dzackgarza/sage-extensions/issues/25) | 9 |

## Full leaf mapping

Every row, in former `TODO.md` order. A `research` number without a current issue was already closed before the transfer, or stays in `research`.

| Cluster | Source identifier | `research` issue | Current issue |
| --- | --- | --- | --- |
| M1 | `mor-hom-expectation-ruling` | [#492](https://github.com/dzackgarza/research/issues/492) |  |
| M1 | `core-property-construction` | [#556](https://github.com/dzackgarza/research/issues/556) | [sage-extensions#27](https://github.com/dzackgarza/sage-extensions/issues/27) |
| M1 | `division-algebras-are-placed-by-construction` | [#451](https://github.com/dzackgarza/research/issues/451) | [sage-extensions#35](https://github.com/dzackgarza/sage-extensions/issues/35) |
| M1 | `ring-sizes-follow-construction` | [#450](https://github.com/dzackgarza/research/issues/450) | [sage-extensions#36](https://github.com/dzackgarza/sage-extensions/issues/36) |
| M1 | `effective-categorical-constructions` | [#428](https://github.com/dzackgarza/research/issues/428) | [sage-extensions#32](https://github.com/dzackgarza/sage-extensions/issues/32) |
| M1 | `pullbacks-in-every-category` | [#514](https://github.com/dzackgarza/research/issues/514) | [sage-extensions#33](https://github.com/dzackgarza/sage-extensions/issues/33) |
| M1 | `named-notions-unfolded-population` | [#485](https://github.com/dzackgarza/research/issues/485) | [sage-extensions#34](https://github.com/dzackgarza/sage-extensions/issues/34) |
| M1 | `modules-over-a-group-algebra-keep-the-module-axioms` | [#443](https://github.com/dzackgarza/research/issues/443) | [sage-extensions#37](https://github.com/dzackgarza/sage-extensions/issues/37) |
| M1 | `modules-call-on-a-set-is-the-free-module` | [#461](https://github.com/dzackgarza/research/issues/461) | [sage-extensions#38](https://github.com/dzackgarza/sage-extensions/issues/38) |
| M1 | `cat-declares-the-owned-objects` | [#470](https://github.com/dzackgarza/research/issues/470) | [sage-extensions#28](https://github.com/dzackgarza/sage-extensions/issues/28) |
| M1 | `arrows-compare-through-richcmp` | [#453](https://github.com/dzackgarza/research/issues/453) | [sage-extensions#121](https://github.com/dzackgarza/sage-extensions/issues/121) |
| M1 | `an-object-lies-in-several-slices` | [#468](https://github.com/dzackgarza/research/issues/468) | [sage-extensions#30](https://github.com/dzackgarza/sage-extensions/issues/30) |
| M1 | `module-and-algebra-slice-objects-lie-in-their-slice` | [#469](https://github.com/dzackgarza/research/issues/469) | [sage-extensions#31](https://github.com/dzackgarza/sage-extensions/issues/31) |
| M1 | `every-arrow-is-an-element-of-its-mor` | [#454](https://github.com/dzackgarza/research/issues/454) | [sage-extensions#29](https://github.com/dzackgarza/sage-extensions/issues/29) |
| M1 | `objects-of-sets-answer-their-endomorphisms` | [#458](https://github.com/dzackgarza/research/issues/458) | [sage-extensions#40](https://github.com/dzackgarza/sage-extensions/issues/40) |
| M1 | `maximal-and-prime-ideals-are-presented` | [#444](https://github.com/dzackgarza/research/issues/444) |  |
| M1 | `native-rings-are-constructed-not-adopted` | [#447](https://github.com/dzackgarza/research/issues/447) |  |
| M1 | `adopted-rings-declare-their-construction-data` | [#467](https://github.com/dzackgarza/research/issues/467) |  |
| M1 | `objects-ask-the-mor-of-their-ambient-category` | [#435](https://github.com/dzackgarza/research/issues/435) | [sage-extensions#39](https://github.com/dzackgarza/sage-extensions/issues/39) |
| M1 | `graded-modules-ask-their-mor-of-the-endpoints` | [#457](https://github.com/dzackgarza/research/issues/457) | [sage-extensions#41](https://github.com/dzackgarza/sage-extensions/issues/41) |
| M1 | `equivariant-module-maps-give-their-natural-transformation` | [#456](https://github.com/dzackgarza/research/issues/456) | [sage-extensions#42](https://github.com/dzackgarza/sage-extensions/issues/42) |
| M1 | `restricted-algebras-are-restricted-modules` | [#478](https://github.com/dzackgarza/research/issues/478) | [sage-extensions#43](https://github.com/dzackgarza/sage-extensions/issues/43) |
| M1 | `internal-mor-inclusion-starts-at-the-mor-module` | [#479](https://github.com/dzackgarza/research/issues/479) | [sage-extensions#46](https://github.com/dzackgarza/sage-extensions/issues/46) |
| M1 | `restricted-mors-decide-membership-by-their-predicate` | [#481](https://github.com/dzackgarza/research/issues/481) | [sage-extensions#47](https://github.com/dzackgarza/sage-extensions/issues/47) |
| M1 | `algebra-arrows-are-ring-arrows` | [#459](https://github.com/dzackgarza/research/issues/459) | [sage-extensions#48](https://github.com/dzackgarza/sage-extensions/issues/48) |
| M1 | `power-algebra-identity` | [#460](https://github.com/dzackgarza/research/issues/460) | [sage-extensions#49](https://github.com/dzackgarza/sage-extensions/issues/49) |
| M1 | `unital-algebras-supply-their-unit` | [#462](https://github.com/dzackgarza/research/issues/462) | [sage-extensions#50](https://github.com/dzackgarza/sage-extensions/issues/50) |
| M1 | `derivation-spaces-read-declared-data` | [#463](https://github.com/dzackgarza/research/issues/463) | [sage-extensions#52](https://github.com/dzackgarza/sage-extensions/issues/52) |
| M1 | `group-resolution-augmentation-terminates` | [#464](https://github.com/dzackgarza/research/issues/464) | [sage-extensions#54](https://github.com/dzackgarza/sage-extensions/issues/54) |
| M1 | `augmented-algebras-retain-their-defining-data` | [#483](https://github.com/dzackgarza/research/issues/483) | [sage-extensions#56](https://github.com/dzackgarza/sage-extensions/issues/56) |
| M1 | `finite-galois-stages-answer-as-their-fields` | [#484](https://github.com/dzackgarza/research/issues/484) | [sage-extensions#59](https://github.com/dzackgarza/sage-extensions/issues/59) |
| M1 | `infinite-index-additive-product-placement` | [#430](https://github.com/dzackgarza/research/issues/430) | [sage-extensions#62](https://github.com/dzackgarza/sage-extensions/issues/62) |
| M1 | `centres-of-algebras-on-infinitely-generated-modules` | [#452](https://github.com/dzackgarza/research/issues/452) | [sage-extensions#64](https://github.com/dzackgarza/sage-extensions/issues/64) |
| M1 | `abelian-groups-are-z-modules` | [#533](https://github.com/dzackgarza/research/issues/533) | [sage-extensions#66](https://github.com/dzackgarza/sage-extensions/issues/66) |
| M1 | `rings-of-integers-are-dedekind-by-construction` | [#449](https://github.com/dzackgarza/research/issues/449) |  |
| M1 | `covering-families-cover-their-space` | [#471](https://github.com/dzackgarza/research/issues/471) | [sage-extensions#68](https://github.com/dzackgarza/sage-extensions/issues/68) |
| M1 | `gluing-accepts-isomorphisms-on-overlaps` | [#472](https://github.com/dzackgarza/research/issues/472) | [sage-extensions#70](https://github.com/dzackgarza/sage-extensions/issues/70) |
| M1 | `base-change-structure-morphisms-land-in-their-mor` | [#473](https://github.com/dzackgarza/research/issues/473) | [sage-extensions#74](https://github.com/dzackgarza/sage-extensions/issues/74) |
| M1 | `native-free-algebras-answer-their-variable` | [#474](https://github.com/dzackgarza/research/issues/474) | [sage-extensions#77](https://github.com/dzackgarza/sage-extensions/issues/77) |
| M1 | `nonaffine-structure-sheaf-coverage` | [#499](https://github.com/dzackgarza/research/issues/499) | [sage-extensions#80](https://github.com/dzackgarza/sage-extensions/issues/80) |
| M1 | `sheaves-compute-sections-on-opens` | [#500](https://github.com/dzackgarza/research/issues/500) | [sage-extensions#83](https://github.com/dzackgarza/sage-extensions/issues/83) |
| M1 | `arrow-class-subcategories-admit-their-arrows` | [#477](https://github.com/dzackgarza/research/issues/477) | [sage-extensions#86](https://github.com/dzackgarza/sage-extensions/issues/86) |
| M1 | `marked-schemes-construct-on-the-owner-route` | [#476](https://github.com/dzackgarza/research/issues/476) | [sage-extensions#89](https://github.com/dzackgarza/sage-extensions/issues/89) |
| M1 | `symbolic-expressions-are-no-owned-ring` | [#446](https://github.com/dzackgarza/research/issues/446) | [sage-extensions#93](https://github.com/dzackgarza/sage-extensions/issues/93) |
| M1 | `the-real-line-is-a-smooth-manifold` | [#434](https://github.com/dzackgarza/research/issues/434) | [sage-extensions#97](https://github.com/dzackgarza/sage-extensions/issues/97) |
| M1 | `function-spaces-are-subobjects-of-mor` | [#433](https://github.com/dzackgarza/research/issues/433) | [sage-extensions#101](https://github.com/dzackgarza/sage-extensions/issues/101) |
| M1 | `group-categories-defined-by-data` | [#432](https://github.com/dzackgarza/research/issues/432) | [sage-extensions#104](https://github.com/dzackgarza/sage-extensions/issues/104) |
| M1 | `lattice-mor-stays-in-the-preamble` | [#482](https://github.com/dzackgarza/research/issues/482) | [sage-extensions#107](https://github.com/dzackgarza/sage-extensions/issues/107) |
| M1 | `brauer-characters-are-maps-on-p-regular-elements` | [#480](https://github.com/dzackgarza/research/issues/480) | [sage-extensions#110](https://github.com/dzackgarza/sage-extensions/issues/110) |
| M1 | `coxeter-diagrams-construct-from-their-data` | [#439](https://github.com/dzackgarza/research/issues/439) | [sage-extensions#113](https://github.com/dzackgarza/sage-extensions/issues/113) |
| M1 | `coxeter-diagram-orders-are-owned-posets` | [#441](https://github.com/dzackgarza/research/issues/441) | [sage-extensions#116](https://github.com/dzackgarza/sage-extensions/issues/116) |
| M1 | `partially-ordered-sets-have-monotone-maps` | [#442](https://github.com/dzackgarza/research/issues/442) | [sage-extensions#118](https://github.com/dzackgarza/sage-extensions/issues/118) |
| M4 | `geometry-stub-operations-compute` | [#501](https://github.com/dzackgarza/research/issues/501) | [sage-extensions#200](https://github.com/dzackgarza/sage-extensions/issues/200) |
| M4 | `orthogonal-groups-of-direct-sums` | [#506](https://github.com/dzackgarza/research/issues/506) | [sage-extensions#130](https://github.com/dzackgarza/sage-extensions/issues/130) |
| M4 | `higher-rank-integral-lattice-representation` | [#505](https://github.com/dzackgarza/research/issues/505) | [sage-extensions#127](https://github.com/dzackgarza/sage-extensions/issues/127) |
| M4 | `lattice-glue-stabilizers` | [#515](https://github.com/dzackgarza/research/issues/515) | [sage-extensions#136](https://github.com/dzackgarza/sage-extensions/issues/136) |
| M4 | `filtered-objects-and-associated-graded` | [#534](https://github.com/dzackgarza/research/issues/534) | [sage-extensions#142](https://github.com/dzackgarza/sage-extensions/issues/142) |
| M4 | `filtered-scalar-extension-and-conjugation` | [#535](https://github.com/dzackgarza/research/issues/535) | [sage-extensions#145](https://github.com/dzackgarza/sage-extensions/issues/145) |
| M4 | `pure-and-mixed-hodge-structures` | [#536](https://github.com/dzackgarza/research/issues/536) | [sage-extensions#148](https://github.com/dzackgarza/sage-extensions/issues/148) |
| M4 | `hodge-tensors-pairings-and-polarizations` | [#537](https://github.com/dzackgarza/research/issues/537) | [sage-extensions#151](https://github.com/dzackgarza/sage-extensions/issues/151) |
| M4 | `k3-hodge-and-partner-foundations` | [#532](https://github.com/dzackgarza/research/issues/532) | [sage-extensions#139](https://github.com/dzackgarza/sage-extensions/issues/139) |
| M4 | `hodge-lattice-isometries` | [#538](https://github.com/dzackgarza/research/issues/538) | [sage-extensions#154](https://github.com/dzackgarza/sage-extensions/issues/154) |
| M4 | `hodge-isometry-subgroup-computation` | [#539](https://github.com/dzackgarza/research/issues/539) | [sage-extensions#157](https://github.com/dzackgarza/sage-extensions/issues/157) |
| M4 | `k3-surfaces-and-cohomology` | [#540](https://github.com/dzackgarza/research/issues/540) | [sage-extensions#169](https://github.com/dzackgarza/sage-extensions/issues/169) |
| M4 | `genus-finiteness-parity-and-classification` | [#531](https://github.com/dzackgarza/research/issues/531) | [sage-extensions#124](https://github.com/dzackgarza/sage-extensions/issues/124) |
| M4 | `pontryagin-duality` | [#512](https://github.com/dzackgarza/research/issues/512) | [sage-extensions#171](https://github.com/dzackgarza/sage-extensions/issues/171) |
| M4 | `group-exact-sequences-and-homology` | [#513](https://github.com/dzackgarza/research/issues/513) | [sage-extensions#174](https://github.com/dzackgarza/sage-extensions/issues/174) |
| M4 | `signed-discriminant-lifting-obstructions` | [#542](https://github.com/dzackgarza/research/issues/542) | [sage-extensions#177](https://github.com/dzackgarza/sage-extensions/issues/177) |
| M4 | `k3-ample-cones-and-stabilizers` | [#541](https://github.com/dzackgarza/research/issues/541) | [sage-extensions#179](https://github.com/dzackgarza/sage-extensions/issues/179) |
| M4 | `k3-automorphisms-by-torelli` | [#543](https://github.com/dzackgarza/research/issues/543) | [sage-extensions#182](https://github.com/dzackgarza/sage-extensions/issues/182) |
| M4 | `k3-fourier-mukai-partner-count` | [#545](https://github.com/dzackgarza/research/issues/545) | [sage-extensions#185](https://github.com/dzackgarza/sage-extensions/issues/185) |
| M4 | `k3-families-on-threefolds` | [#544](https://github.com/dzackgarza/research/issues/544) | [sage-extensions#188](https://github.com/dzackgarza/sage-extensions/issues/188) |
| M4 | `k3-brauer-groups-and-classes` | [#546](https://github.com/dzackgarza/research/issues/546) | [sage-extensions#190](https://github.com/dzackgarza/sage-extensions/issues/190) |
| M4 | `k3-mukai-lattices-and-vectors` | [#547](https://github.com/dzackgarza/research/issues/547) | [sage-extensions#193](https://github.com/dzackgarza/sage-extensions/issues/193) |
| M4 | `k3-sheaf-moduli-and-caldararu-classes` | [#548](https://github.com/dzackgarza/research/issues/548) | [sage-extensions#196](https://github.com/dzackgarza/sage-extensions/issues/196) |
| M4 | `discriminant-lagrangian-elements-and-subsets` | [#549](https://github.com/dzackgarza/research/issues/549) | [sage-extensions#197](https://github.com/dzackgarza/sage-extensions/issues/197) |
| M4 | `complex-realization-is-a-functor` | [#527](https://github.com/dzackgarza/research/issues/527) | [sage-extensions#160](https://github.com/dzackgarza/sage-extensions/issues/160) |
| M4 | `complete-intersection-hodge-sources` | [#528](https://github.com/dzackgarza/research/issues/528) | [sage-extensions#163](https://github.com/dzackgarza/sage-extensions/issues/163) |
| M4 | `complete-intersection-hodge-structure` | [#529](https://github.com/dzackgarza/research/issues/529) | [sage-extensions#166](https://github.com/dzackgarza/sage-extensions/issues/166) |
| M4 | `optional-manifold-tangent-bundles` | [#553](https://github.com/dzackgarza/research/issues/553) | [sage-extensions#198](https://github.com/dzackgarza/sage-extensions/issues/198) |
| M4 | `simplicial-and-cw-foundations` | [#517](https://github.com/dzackgarza/research/issues/517) | [sage-extensions#199](https://github.com/dzackgarza/sage-extensions/issues/199) |
| M4 | `integral-affine-polyhedral-p1` | [#518](https://github.com/dzackgarza/research/issues/518) | [sage-extensions#201](https://github.com/dzackgarza/sage-extensions/issues/201) |
| M4 | `integral-affine-polyhedral-p2` | [#519](https://github.com/dzackgarza/research/issues/519) | [sage-extensions#202](https://github.com/dzackgarza/sage-extensions/issues/202) |
| M4 | `integral-affine-polyhedral-p3` | [#520](https://github.com/dzackgarza/research/issues/520) | [sage-extensions#203](https://github.com/dzackgarza/sage-extensions/issues/203) |
| M4 | `integral-affine-polyhedral-p4` | [#521](https://github.com/dzackgarza/research/issues/521) | [sage-extensions#204](https://github.com/dzackgarza/sage-extensions/issues/204) |
| M4 | `integral-affine-polyhedral-p5` | [#522](https://github.com/dzackgarza/research/issues/522) | [sage-extensions#205](https://github.com/dzackgarza/sage-extensions/issues/205) |
| M4 | `integral-affine-polyhedral-p6` | [#523](https://github.com/dzackgarza/research/issues/523) | [sage-extensions#206](https://github.com/dzackgarza/sage-extensions/issues/206) |
| M4 | `modular-form-spaces-with-character` | [#502](https://github.com/dzackgarza/research/issues/502) | [sage-extensions#207](https://github.com/dzackgarza/sage-extensions/issues/207) |
| M4 | `theta-cusp-form-coordinates` | [#503](https://github.com/dzackgarza/research/issues/503) | [sage-extensions#208](https://github.com/dzackgarza/sage-extensions/issues/208) |
| M4 | `definite-representation-exceptions` | [#504](https://github.com/dzackgarza/research/issues/504) | [sage-extensions#209](https://github.com/dzackgarza/sage-extensions/issues/209) |
| M4 | `modular-forms-and-hecke-algebras` | [#525](https://github.com/dzackgarza/research/issues/525) | [sage-extensions#210](https://github.com/dzackgarza/sage-extensions/issues/210) |
| M4 | `higher-signature-reflection-engine-ruling` | [#509](https://github.com/dzackgarza/research/issues/509) | [sage-extensions#211](https://github.com/dzackgarza/sage-extensions/issues/211) |
| M4 | `higher-signature-reflection-group-search` | [#508](https://github.com/dzackgarza/research/issues/508) | [sage-extensions#212](https://github.com/dzackgarza/sage-extensions/issues/212) |
| M4 | `hyperbolic-restricted-reflection-engine-ruling` | [#511](https://github.com/dzackgarza/research/issues/511) | [sage-extensions#213](https://github.com/dzackgarza/sage-extensions/issues/213) |
| M4 | `hyperbolic-restricted-norm-reflection-groups` | [#510](https://github.com/dzackgarza/research/issues/510) | [sage-extensions#214](https://github.com/dzackgarza/sage-extensions/issues/214) |
| M4 | `lattice-reflection-groups` | [#507](https://github.com/dzackgarza/research/issues/507) | [sage-extensions#215](https://github.com/dzackgarza/sage-extensions/issues/215) |
| M4 | `coxeter-group-structure` | [#516](https://github.com/dzackgarza/research/issues/516) | [sage-extensions#133](https://github.com/dzackgarza/sage-extensions/issues/133) |
| M4 | `coxeter-complexes-and-buildings` | [#524](https://github.com/dzackgarza/research/issues/524) | [sage-extensions#216](https://github.com/dzackgarza/sage-extensions/issues/216) |
| M4 | `satake-diagrams-present-real-forms` | [#526](https://github.com/dzackgarza/research/issues/526) | [sage-extensions#217](https://github.com/dzackgarza/sage-extensions/issues/217) |
| M4 | `prime-prolongations-from-p-adic-embeddings` | [#466](https://github.com/dzackgarza/research/issues/466) | [sage-extensions#218](https://github.com/dzackgarza/sage-extensions/issues/218) |
| M4 | `geometric-cards-store-betti-numbers` | [#530](https://github.com/dzackgarza/research/issues/530) | [sage-extensions#219](https://github.com/dzackgarza/sage-extensions/issues/219) |
| M2 | `resolution-truncations-in-the-session` | [#465](https://github.com/dzackgarza/research/issues/465) | [sage-extensions#220](https://github.com/dzackgarza/sage-extensions/issues/220) |
| M2 | `placement-audit` | [#429](https://github.com/dzackgarza/research/issues/429) | [sage-extensions#221](https://github.com/dzackgarza/sage-extensions/issues/221) |
| M2 | `engine-wiring-audit` | [#431](https://github.com/dzackgarza/research/issues/431) | [sage-extensions#222](https://github.com/dzackgarza/sage-extensions/issues/222) |
| M2 | `membership-replaces-dynamic-peeking` | [#436](https://github.com/dzackgarza/research/issues/436) | [sage-extensions#223](https://github.com/dzackgarza/sage-extensions/issues/223) |
| M2 | `session-objects-are-built-by-their-parents` | [#440](https://github.com/dzackgarza/research/issues/440) | [sage-extensions#224](https://github.com/dzackgarza/sage-extensions/issues/224) |
| M2 | `literal-sets-route-by-membership` | [#475](https://github.com/dzackgarza/research/issues/475) | [sage-extensions#225](https://github.com/dzackgarza/sage-extensions/issues/225) |
| M2 | `construction-is-instant` | [#437](https://github.com/dzackgarza/research/issues/437) | [sage-extensions#226](https://github.com/dzackgarza/sage-extensions/issues/226) |
| M2 | `daily-core-exercises` | [#438](https://github.com/dzackgarza/research/issues/438) | [sage-extensions#227](https://github.com/dzackgarza/sage-extensions/issues/227) |
| M2 | `architecture-remediation` | [#486](https://github.com/dzackgarza/research/issues/486) | [sage-extensions#228](https://github.com/dzackgarza/sage-extensions/issues/228) |
| M2 | `core-usability-session` | [#487](https://github.com/dzackgarza/research/issues/487) | [sage-extensions#229](https://github.com/dzackgarza/sage-extensions/issues/229) |
| M2 | `constructor-discovery` | [#491](https://github.com/dzackgarza/research/issues/491) | [sage-extensions#230](https://github.com/dzackgarza/sage-extensions/issues/230) |
| M2 | `refactor-audit` | [#488](https://github.com/dzackgarza/research/issues/488) | [sage-extensions#231](https://github.com/dzackgarza/sage-extensions/issues/231) |
| M2 | `type-paydown` | [#489](https://github.com/dzackgarza/research/issues/489) | [sage-extensions#232](https://github.com/dzackgarza/sage-extensions/issues/232) |
| M2 | `bloat-audit-loop` | [#490](https://github.com/dzackgarza/research/issues/490) | [sage-extensions#233](https://github.com/dzackgarza/sage-extensions/issues/233) |
| M2 | `minimal-api-freeze` | [#493](https://github.com/dzackgarza/research/issues/493) | [sage-extensions#26](https://github.com/dzackgarza/sage-extensions/issues/26) |
| M3 | `triage-long-tail` | [#496](https://github.com/dzackgarza/research/issues/496) | [sage-extensions#234](https://github.com/dzackgarza/sage-extensions/issues/234) |
| M3 | `suite-compactification` | [#494](https://github.com/dzackgarza/research/issues/494) | [sage-extensions#235](https://github.com/dzackgarza/sage-extensions/issues/235) |
| M3 | `category-method-coverage-sweep` | [#495](https://github.com/dzackgarza/research/issues/495) | [sage-extensions#236](https://github.com/dzackgarza/sage-extensions/issues/236) |
| M3 | `suite-within-time-gates` | [#497](https://github.com/dzackgarza/research/issues/497) | [sage-extensions#237](https://github.com/dzackgarza/sage-extensions/issues/237) |
| M3 | `terminal-session` | [#498](https://github.com/dzackgarza/research/issues/498) | [sage-extensions#238](https://github.com/dzackgarza/sage-extensions/issues/238) |
| M3 | `resumed-handoff-delivery` | [#427](https://github.com/dzackgarza/research/issues/427) | [sage-extensions#239](https://github.com/dzackgarza/sage-extensions/issues/239) |
| M3 | `extended-mathematics-session` | [#550](https://github.com/dzackgarza/research/issues/550) | [sage-extensions#240](https://github.com/dzackgarza/sage-extensions/issues/240) |
| M5 | `optional-framed-manifolds` | [#551](https://github.com/dzackgarza/research/issues/551) | [sage-extensions#241](https://github.com/dzackgarza/sage-extensions/issues/241) |
| M5 | `optional-brauer-manin-obstructions` | [#552](https://github.com/dzackgarza/research/issues/552) | [sage-extensions#242](https://github.com/dzackgarza/sage-extensions/issues/242) |
| M5 | `optional-random-lattices-of-given-invariants` | [#554](https://github.com/dzackgarza/research/issues/554) | [sage-extensions#243](https://github.com/dzackgarza/sage-extensions/issues/243) |
| M5 | `optional-moduli-of-stable-curves` | [#555](https://github.com/dzackgarza/research/issues/555) | [sage-extensions#244](https://github.com/dzackgarza/sage-extensions/issues/244) |
| M5 | `optional-database` | [#557](https://github.com/dzackgarza/research/issues/557) | [sage-extensions#245](https://github.com/dzackgarza/sage-extensions/issues/245) |
| M5 | `optional-engine` | [#558](https://github.com/dzackgarza/research/issues/558) | [sage-extensions#246](https://github.com/dzackgarza/sage-extensions/issues/246) |
