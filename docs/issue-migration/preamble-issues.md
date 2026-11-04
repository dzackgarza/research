# Preamble work issues

Implement issue work directly on `main`. Use a branch only when parallel work
requires a separate worktree. The [delivery policy](CONTRIBUTING.md#delivery-workflow)
overrides `itree next`'s generic instruction to open a PR.

The roadmap is [the ordered research issue tree, #46](https://github.com/dzackgarza/research/issues/46); its milestones route to `Phase:` issues under [sage-extensions#14](https://github.com/dzackgarza/sage-extensions/issues/14), which hold the work units (`itree next dzackgarza/sage-extensions`). Order minimizes the work needed to complete the required programme, including rework. Shared correctness and construction, reusable mathematical operations, and required capability normally precede broad reviews and final acceptance. Advance a shared change when it removes or shortens named later repairs; reassess those repairs against their full acceptance after delivery. Performance and workflow repairs move earlier for observed costs on required work. Optional work follows required work.

[AGENTS.md](AGENTS.md#execution-order) states the payoff and dependency rules. Milestone numbers retain their identities; native sibling order determines execution. Task contracts, hypotheses, specimens, acceptance and dependencies live in the issues. This file maps the former source identifiers to their current owners.

[INTENT.md](INTENT.md), [AGENTS.md](AGENTS.md) and [CONTRIBUTING.md](CONTRIBUTING.md) govern implementation. Issue [#414](https://github.com/dzackgarza/research/issues/414) retains the shared execution contract. Terminal acceptance [sage-extensions#238](https://github.com/dzackgarza/sage-extensions/issues/238), including its continuation comments, and required-extension acceptance [sage-extensions#240](https://github.com/dzackgarza/sage-extensions/issues/240) retain their complete obligations.

Concrete repairs extracted from broader surveys are [minimal-prime loci sage-extensions#87](https://github.com/dzackgarza/sage-extensions/issues/87), [indexed-family equality sage-extensions#90](https://github.com/dzackgarza/sage-extensions/issues/90), [Coxeter construction #563](https://github.com/dzackgarza/research/issues/563), and [spinor-generator accumulation #564](https://github.com/dzackgarza/research/issues/564). Their original surveys or inventories depend on these repairs.

## M1 — Shared correctness and daily mathematical constructions

[Issue #417](https://github.com/dzackgarza/research/issues/417) routes to [sage-extensions#21](https://github.com/dzackgarza/sage-extensions/issues/21), which holds the work units.

The required [core migration #384](https://github.com/dzackgarza/research/issues/384) and [property/constructor integration sage-extensions#27](https://github.com/dzackgarza/sage-extensions/issues/27) precede repairs to the transitional runtime they retire. Each layer reconciles its complete mathematics with `lean-categories`, its semantic execution with the `lean-cas-dsl` kernel, and its computations with leaf registrations. The affected issues retain unmet requirements on the final construction. The native tree also places shared finite-action and formed-module computations before their decorated-family consumers.

| Source identifier | Issue |
| --- | --- |
| `mor-hom-expectation-ruling` | [#492](https://github.com/dzackgarza/research/issues/492) |
| `core-property-construction` | [sage-extensions#27](https://github.com/dzackgarza/sage-extensions/issues/27) |
| `division-algebras-are-placed-by-construction` | [sage-extensions#35](https://github.com/dzackgarza/sage-extensions/issues/35) |
| `ring-sizes-follow-construction` | [sage-extensions#36](https://github.com/dzackgarza/sage-extensions/issues/36) |
| `effective-categorical-constructions` | [sage-extensions#32](https://github.com/dzackgarza/sage-extensions/issues/32) |
| `pullbacks-in-every-category` | [sage-extensions#33](https://github.com/dzackgarza/sage-extensions/issues/33) |
| `named-notions-unfolded-population` | [sage-extensions#34](https://github.com/dzackgarza/sage-extensions/issues/34) |
| `modules-over-a-group-algebra-keep-the-module-axioms` | [sage-extensions#37](https://github.com/dzackgarza/sage-extensions/issues/37) |
| `modules-call-on-a-set-is-the-free-module` | [sage-extensions#38](https://github.com/dzackgarza/sage-extensions/issues/38) |
| `cat-declares-the-owned-objects` | [sage-extensions#28](https://github.com/dzackgarza/sage-extensions/issues/28) |
| `arrows-compare-through-richcmp` | [sage-extensions#121](https://github.com/dzackgarza/sage-extensions/issues/121) |
| `an-object-lies-in-several-slices` | [sage-extensions#30](https://github.com/dzackgarza/sage-extensions/issues/30) |
| `module-and-algebra-slice-objects-lie-in-their-slice` | [sage-extensions#31](https://github.com/dzackgarza/sage-extensions/issues/31) |
| `every-arrow-is-an-element-of-its-mor` | [sage-extensions#29](https://github.com/dzackgarza/sage-extensions/issues/29) |
| `objects-of-sets-answer-their-endomorphisms` | [sage-extensions#40](https://github.com/dzackgarza/sage-extensions/issues/40) |
| `maximal-and-prime-ideals-are-presented` | [#444](https://github.com/dzackgarza/research/issues/444) |
| `native-rings-are-constructed-not-adopted` | [#447](https://github.com/dzackgarza/research/issues/447) |
| `adopted-rings-declare-their-construction-data` | [#467](https://github.com/dzackgarza/research/issues/467) |
| `objects-ask-the-mor-of-their-ambient-category` | [sage-extensions#39](https://github.com/dzackgarza/sage-extensions/issues/39) |
| `graded-modules-ask-their-mor-of-the-endpoints` | [sage-extensions#41](https://github.com/dzackgarza/sage-extensions/issues/41) |
| `equivariant-module-maps-give-their-natural-transformation` | [sage-extensions#42](https://github.com/dzackgarza/sage-extensions/issues/42) |
| `restricted-algebras-are-restricted-modules` | [sage-extensions#43](https://github.com/dzackgarza/sage-extensions/issues/43) |
| `internal-mor-inclusion-starts-at-the-mor-module` | [sage-extensions#46](https://github.com/dzackgarza/sage-extensions/issues/46) |
| `restricted-mors-decide-membership-by-their-predicate` | [sage-extensions#47](https://github.com/dzackgarza/sage-extensions/issues/47) |
| `algebra-arrows-are-ring-arrows` | [sage-extensions#48](https://github.com/dzackgarza/sage-extensions/issues/48) |
| `power-algebra-identity` | [sage-extensions#49](https://github.com/dzackgarza/sage-extensions/issues/49) |
| `unital-algebras-supply-their-unit` | [sage-extensions#50](https://github.com/dzackgarza/sage-extensions/issues/50) |
| `derivation-spaces-read-declared-data` | [sage-extensions#52](https://github.com/dzackgarza/sage-extensions/issues/52) |
| `group-resolution-augmentation-terminates` | [sage-extensions#54](https://github.com/dzackgarza/sage-extensions/issues/54) |
| `augmented-algebras-retain-their-defining-data` | [sage-extensions#56](https://github.com/dzackgarza/sage-extensions/issues/56) |
| `finite-galois-stages-answer-as-their-fields` | [sage-extensions#59](https://github.com/dzackgarza/sage-extensions/issues/59) |
| `infinite-index-additive-product-placement` | [sage-extensions#62](https://github.com/dzackgarza/sage-extensions/issues/62) |
| `centres-of-algebras-on-infinitely-generated-modules` | [sage-extensions#64](https://github.com/dzackgarza/sage-extensions/issues/64) |
| `abelian-groups-are-z-modules` | [sage-extensions#66](https://github.com/dzackgarza/sage-extensions/issues/66) |
| `rings-of-integers-are-dedekind-by-construction` | [#449](https://github.com/dzackgarza/research/issues/449) |
| `covering-families-cover-their-space` | [sage-extensions#68](https://github.com/dzackgarza/sage-extensions/issues/68) |
| `gluing-accepts-isomorphisms-on-overlaps` | [sage-extensions#70](https://github.com/dzackgarza/sage-extensions/issues/70) |
| `base-change-structure-morphisms-land-in-their-mor` | [sage-extensions#74](https://github.com/dzackgarza/sage-extensions/issues/74) |
| `native-free-algebras-answer-their-variable` | [sage-extensions#77](https://github.com/dzackgarza/sage-extensions/issues/77) |
| `nonaffine-structure-sheaf-coverage` | [sage-extensions#80](https://github.com/dzackgarza/sage-extensions/issues/80) |
| `sheaves-compute-sections-on-opens` | [sage-extensions#83](https://github.com/dzackgarza/sage-extensions/issues/83) |
| `arrow-class-subcategories-admit-their-arrows` | [sage-extensions#86](https://github.com/dzackgarza/sage-extensions/issues/86) |
| `marked-schemes-construct-on-the-owner-route` | [sage-extensions#89](https://github.com/dzackgarza/sage-extensions/issues/89) |
| `symbolic-expressions-are-no-owned-ring` | [sage-extensions#93](https://github.com/dzackgarza/sage-extensions/issues/93) |
| `the-real-line-is-a-smooth-manifold` | [sage-extensions#97](https://github.com/dzackgarza/sage-extensions/issues/97) |
| `function-spaces-are-subobjects-of-mor` | [sage-extensions#101](https://github.com/dzackgarza/sage-extensions/issues/101) |
| `group-categories-defined-by-data` | [sage-extensions#104](https://github.com/dzackgarza/sage-extensions/issues/104) |
| `lattice-mor-stays-in-the-preamble` | [sage-extensions#107](https://github.com/dzackgarza/sage-extensions/issues/107) |
| `brauer-characters-are-maps-on-p-regular-elements` | [sage-extensions#110](https://github.com/dzackgarza/sage-extensions/issues/110) |
| `coxeter-diagrams-construct-from-their-data` | [sage-extensions#113](https://github.com/dzackgarza/sage-extensions/issues/113) |
| `coxeter-diagram-orders-are-owned-posets` | [sage-extensions#116](https://github.com/dzackgarza/sage-extensions/issues/116) |
| `partially-ordered-sets-have-monotone-maps` | [sage-extensions#118](https://github.com/dzackgarza/sage-extensions/issues/118) |

## Reusable lattice and group computations

[Issue #415](https://github.com/dzackgarza/research/issues/415) routes to [sage-extensions#44](https://github.com/dzackgarza/sage-extensions/issues/44), which holds the work units.

| Source identifier | Issue |
| --- | --- |
| `construction-cost-on-resumed-routes` | [sage-extensions#78](https://github.com/dzackgarza/sage-extensions/issues/78) |
| `port-configurations-cones-and-integral-lifts` | [sage-extensions#81](https://github.com/dzackgarza/sage-extensions/issues/81) |

## Specialized port computation and acceptance

[Issue #416](https://github.com/dzackgarza/research/issues/416)

| Source identifier | Issue |
| --- | --- |
| `port-rank-three-isotropic-traversal` | [sage-indefinite-port#15](https://github.com/dzackgarza/sage-indefinite-port/issues/15) |
| `port-nonscalar-component-centralizers` | [sage-indefinite-port#18](https://github.com/dzackgarza/sage-indefinite-port/issues/18) |
| `port-handoff-frozen-acceptance` | [sage-indefinite-port#33](https://github.com/dzackgarza/sage-indefinite-port/issues/33) |

## M4 — Required mathematical expansion

[Issue #420](https://github.com/dzackgarza/research/issues/420) routes to [sage-extensions#22](https://github.com/dzackgarza/sage-extensions/issues/22), which holds the work units.

| Source identifier | Issue |
| --- | --- |
| `geometry-stub-operations-compute` | [sage-extensions#200](https://github.com/dzackgarza/sage-extensions/issues/200) |
| `orthogonal-groups-of-direct-sums` | [sage-extensions#130](https://github.com/dzackgarza/sage-extensions/issues/130) |
| `higher-rank-integral-lattice-representation` | [sage-extensions#127](https://github.com/dzackgarza/sage-extensions/issues/127) |
| `lattice-glue-stabilizers` | [sage-extensions#136](https://github.com/dzackgarza/sage-extensions/issues/136) |
| `filtered-objects-and-associated-graded` | [sage-extensions#142](https://github.com/dzackgarza/sage-extensions/issues/142) |
| `filtered-scalar-extension-and-conjugation` | [sage-extensions#145](https://github.com/dzackgarza/sage-extensions/issues/145) |
| `pure-and-mixed-hodge-structures` | [sage-extensions#148](https://github.com/dzackgarza/sage-extensions/issues/148) |
| `hodge-tensors-pairings-and-polarizations` | [sage-extensions#151](https://github.com/dzackgarza/sage-extensions/issues/151) |
| `k3-hodge-and-partner-foundations` | [sage-extensions#139](https://github.com/dzackgarza/sage-extensions/issues/139) |
| `hodge-lattice-isometries` | [sage-extensions#154](https://github.com/dzackgarza/sage-extensions/issues/154) |
| `hodge-isometry-subgroup-computation` | [sage-extensions#157](https://github.com/dzackgarza/sage-extensions/issues/157) |
| `k3-surfaces-and-cohomology` | [sage-extensions#169](https://github.com/dzackgarza/sage-extensions/issues/169) |
| `genus-finiteness-parity-and-classification` | [sage-extensions#124](https://github.com/dzackgarza/sage-extensions/issues/124) |
| `pontryagin-duality` | [sage-extensions#171](https://github.com/dzackgarza/sage-extensions/issues/171) |
| `group-exact-sequences-and-homology` | [sage-extensions#174](https://github.com/dzackgarza/sage-extensions/issues/174) |
| `signed-discriminant-lifting-obstructions` | [sage-extensions#177](https://github.com/dzackgarza/sage-extensions/issues/177) |
| `k3-ample-cones-and-stabilizers` | [sage-extensions#179](https://github.com/dzackgarza/sage-extensions/issues/179) |
| `k3-automorphisms-by-torelli` | [sage-extensions#182](https://github.com/dzackgarza/sage-extensions/issues/182) |
| `k3-fourier-mukai-partner-count` | [sage-extensions#185](https://github.com/dzackgarza/sage-extensions/issues/185) |
| `k3-families-on-threefolds` | [sage-extensions#188](https://github.com/dzackgarza/sage-extensions/issues/188) |
| `k3-brauer-groups-and-classes` | [sage-extensions#190](https://github.com/dzackgarza/sage-extensions/issues/190) |
| `k3-mukai-lattices-and-vectors` | [sage-extensions#193](https://github.com/dzackgarza/sage-extensions/issues/193) |
| `k3-sheaf-moduli-and-caldararu-classes` | [sage-extensions#196](https://github.com/dzackgarza/sage-extensions/issues/196) |
| `discriminant-lagrangian-elements-and-subsets` | [sage-extensions#197](https://github.com/dzackgarza/sage-extensions/issues/197) |
| `complex-realization-is-a-functor` | [sage-extensions#160](https://github.com/dzackgarza/sage-extensions/issues/160) |
| `complete-intersection-hodge-sources` | [sage-extensions#163](https://github.com/dzackgarza/sage-extensions/issues/163) |
| `complete-intersection-hodge-structure` | [sage-extensions#166](https://github.com/dzackgarza/sage-extensions/issues/166) |
| `optional-manifold-tangent-bundles` (historical identifier; required by #520) | [sage-extensions#198](https://github.com/dzackgarza/sage-extensions/issues/198) |
| `simplicial-and-cw-foundations` | [sage-extensions#199](https://github.com/dzackgarza/sage-extensions/issues/199) |
| `integral-affine-polyhedral-p1` | [sage-extensions#201](https://github.com/dzackgarza/sage-extensions/issues/201) |
| `integral-affine-polyhedral-p2` | [sage-extensions#202](https://github.com/dzackgarza/sage-extensions/issues/202) |
| `integral-affine-polyhedral-p3` | [sage-extensions#203](https://github.com/dzackgarza/sage-extensions/issues/203) |
| `integral-affine-polyhedral-p4` | [sage-extensions#204](https://github.com/dzackgarza/sage-extensions/issues/204) |
| `integral-affine-polyhedral-p5` | [sage-extensions#205](https://github.com/dzackgarza/sage-extensions/issues/205) |
| `integral-affine-polyhedral-p6` | [sage-extensions#206](https://github.com/dzackgarza/sage-extensions/issues/206) |
| `modular-form-spaces-with-character` | [sage-extensions#207](https://github.com/dzackgarza/sage-extensions/issues/207) |
| `theta-cusp-form-coordinates` | [sage-extensions#208](https://github.com/dzackgarza/sage-extensions/issues/208) |
| `definite-representation-exceptions` | [sage-extensions#209](https://github.com/dzackgarza/sage-extensions/issues/209) |
| `modular-forms-and-hecke-algebras` | [sage-extensions#210](https://github.com/dzackgarza/sage-extensions/issues/210) |
| `higher-signature-reflection-engine-ruling` | [sage-extensions#211](https://github.com/dzackgarza/sage-extensions/issues/211) |
| `higher-signature-reflection-group-search` | [sage-extensions#212](https://github.com/dzackgarza/sage-extensions/issues/212) |
| `hyperbolic-restricted-reflection-engine-ruling` | [sage-extensions#213](https://github.com/dzackgarza/sage-extensions/issues/213) |
| `hyperbolic-restricted-norm-reflection-groups` | [sage-extensions#214](https://github.com/dzackgarza/sage-extensions/issues/214) |
| `lattice-reflection-groups` | [sage-extensions#215](https://github.com/dzackgarza/sage-extensions/issues/215) |
| `coxeter-group-structure` | [sage-extensions#133](https://github.com/dzackgarza/sage-extensions/issues/133) |
| `coxeter-complexes-and-buildings` | [sage-extensions#216](https://github.com/dzackgarza/sage-extensions/issues/216) |
| `satake-diagrams-present-real-forms` | [sage-extensions#217](https://github.com/dzackgarza/sage-extensions/issues/217) |
| `prime-prolongations-from-p-adic-embeddings` | [sage-extensions#218](https://github.com/dzackgarza/sage-extensions/issues/218) |
| `geometric-cards-store-betti-numbers` | [sage-extensions#219](https://github.com/dzackgarza/sage-extensions/issues/219) |

## M2 — API review and retained core closure

[Issue #418](https://github.com/dzackgarza/research/issues/418) routes to [sage-extensions#23](https://github.com/dzackgarza/sage-extensions/issues/23), which holds the work units.

| Source identifier | Issue |
| --- | --- |
| `resolution-truncations-in-the-session` | [sage-extensions#220](https://github.com/dzackgarza/sage-extensions/issues/220) |
| `placement-audit` | [sage-extensions#221](https://github.com/dzackgarza/sage-extensions/issues/221) |
| `engine-wiring-audit` | [sage-extensions#222](https://github.com/dzackgarza/sage-extensions/issues/222) |
| `membership-replaces-dynamic-peeking` | [sage-extensions#223](https://github.com/dzackgarza/sage-extensions/issues/223) |
| `session-objects-are-built-by-their-parents` | [sage-extensions#224](https://github.com/dzackgarza/sage-extensions/issues/224) |
| `literal-sets-route-by-membership` | [sage-extensions#225](https://github.com/dzackgarza/sage-extensions/issues/225) |
| `construction-is-instant` | [sage-extensions#226](https://github.com/dzackgarza/sage-extensions/issues/226) |
| `daily-core-exercises` | [sage-extensions#227](https://github.com/dzackgarza/sage-extensions/issues/227) |
| `architecture-remediation` | [sage-extensions#228](https://github.com/dzackgarza/sage-extensions/issues/228) |
| `core-usability-session` | [sage-extensions#229](https://github.com/dzackgarza/sage-extensions/issues/229) |
| `constructor-discovery` | [sage-extensions#230](https://github.com/dzackgarza/sage-extensions/issues/230) |
| `refactor-audit` | [sage-extensions#231](https://github.com/dzackgarza/sage-extensions/issues/231) |
| `type-paydown` | [sage-extensions#232](https://github.com/dzackgarza/sage-extensions/issues/232) |
| `bloat-audit-loop` | [sage-extensions#233](https://github.com/dzackgarza/sage-extensions/issues/233) |
| `minimal-api-freeze` | [sage-extensions#26](https://github.com/dzackgarza/sage-extensions/issues/26) |

## M3 — Complete mathematical acceptance

[Issue #419](https://github.com/dzackgarza/research/issues/419) routes to [sage-extensions#24](https://github.com/dzackgarza/sage-extensions/issues/24), which holds the work units.

| Source identifier | Issue |
| --- | --- |
| `triage-long-tail` | [sage-extensions#234](https://github.com/dzackgarza/sage-extensions/issues/234) |
| `suite-compactification` | [sage-extensions#235](https://github.com/dzackgarza/sage-extensions/issues/235) |
| `category-method-coverage-sweep` | [sage-extensions#236](https://github.com/dzackgarza/sage-extensions/issues/236) |
| `suite-within-time-gates` | [sage-extensions#237](https://github.com/dzackgarza/sage-extensions/issues/237) |
| `terminal-session` | [sage-extensions#238](https://github.com/dzackgarza/sage-extensions/issues/238) |
| `resumed-handoff-delivery` | [sage-extensions#239](https://github.com/dzackgarza/sage-extensions/issues/239) |
| `extended-mathematics-session` | [sage-extensions#240](https://github.com/dzackgarza/sage-extensions/issues/240) |

## M5 — Optional research extensions

[Issue #421](https://github.com/dzackgarza/research/issues/421) routes to [sage-extensions#25](https://github.com/dzackgarza/sage-extensions/issues/25), which holds the work units.

| Source identifier | Issue |
| --- | --- |
| `optional-framed-manifolds` | [sage-extensions#241](https://github.com/dzackgarza/sage-extensions/issues/241) |
| `optional-brauer-manin-obstructions` | [sage-extensions#242](https://github.com/dzackgarza/sage-extensions/issues/242) |
| `optional-random-lattices-of-given-invariants` | [sage-extensions#243](https://github.com/dzackgarza/sage-extensions/issues/243) |
| `optional-moduli-of-stable-curves` | [sage-extensions#244](https://github.com/dzackgarza/sage-extensions/issues/244) |
| `optional-database` | [sage-extensions#245](https://github.com/dzackgarza/sage-extensions/issues/245) |
| `optional-engine` | [sage-extensions#246](https://github.com/dzackgarza/sage-extensions/issues/246) |
