---
id: SPEC-MAPPING-POSETS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]'
title: Track posets mapping spec
status: complete
priority: critical
requirement: Convert category_specs/posets/docs/MAPPING.md into a tracked spec surface
  and audit it for Sage-source completeness, mathematical correctness, and well-typed
  order, lattice-order, finite, graph, and interop signatures.
acceptanceCriteria:
- Source paths category_specs/posets/docs/MAPPING.md and category_specs/posets/docs/SAGE_INVENTORY.md
  are reviewed.
- Every admitted row states caller category, complete input data, hypotheses, return
  object, and source evidence.
- Methods are placed at the highest category where they are mathematically well-defined.
- Nonmathematical targets and raw Sage implementation containers are rejected or marked
  interop-only.
- Missing Sage surfaces or mathematical ambiguities become tracked cards or decisions.
complexity: 80
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Posets Mapping Spec

This tracked spec is the canonical mapping surface converted from `category_specs/posets/docs/MAPPING.md`.

Source inventory: `category_specs/posets/docs/SAGE_INVENTORY.md`.

## Review Gates

- Preserve every inventoried Sage surface by mapping it to a project mathematical surface, a named constructor path, a mathematically justified non-mapping, or a tracked decision.
- Place every method at the highest category where the operation is mathematically well-defined; subcategories inherit methods from supercategories.
- State caller category, input data, hypotheses, return object or codomain, and source evidence before implementation depends on the row.
- Reject nonmathematical targets, raw Sage implementation containers, variadic option bags, and smoke-driven interface weakening.
- Route unresolved mathematical ownership, typing, or source-coverage gaps to tracked decisions or tasks before implementation proceeds.

## Source Coverage Ledger

- Sage environment checked: SageMath 10.7, installed source under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages`.
- Local inventory checked: `category_specs/posets/docs/SAGE_INVENTORY.md`.
- Installed Sage source files checked or named by the local inventory:
  - `sage/categories/posets.py`
  - `sage/categories/finite_posets.py`
  - `sage/categories/lattice_posets.py`
  - `sage/categories/finite_lattice_posets.py`
  - `sage/combinat/posets/posets.py`
  - `sage/combinat/posets/lattices.py`
- Import probe caveat: direct `sage -python` imports of several `sage.categories.*` modules raised `ImportError: cannot import name Category`; completeness work therefore uses installed source files and inventories as the durable source surface unless that environment issue is separately resolved.
- Completeness status: this ledger records the checked source corpus; the Posets
  method reconciliation is recorded in `Completeness Reconciliation: Posets` below,
  with remaining gaps routed through `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`.

## Converted Mapping Content

Sage `Posets()` maps to `category_specs.posets.Posets()`.
This category is set-structured, but its method surface is order-theoretic and
therefore lives in the promoted `posets/` subtree rather than under
`sets/subcategories/`.

Sage finite posets map to `Posets().Finite()`.
Sage finite meet-semilattices map to `Posets().MeetSemilattice().Finite()`.
Sage finite join-semilattices map to `Posets().JoinSemilattice().Finite()`.
Sage lattice posets map to `Posets().Lattice()`, whose finite refinement is
`Posets().Lattice().Finite()`.
Here "lattice" always means an order-theoretic meet/join lattice; it does not
mean a module lattice or a quadratic-form lattice.

## Category Hierarchy

The project hierarchy is:

```text
Posets()
|-- Finite()
|-- MeetSemilattice()
|   `-- Finite()
|-- JoinSemilattice()
|   `-- Finite()
`-- Lattice()
    `-- Finite()
```

`Posets().Lattice()` is the common order-theoretic refinement of
`Posets().MeetSemilattice()` and `Posets().JoinSemilattice()`.
The meet operation belongs first to meet-semilattices; the join operation
belongs first to join-semilattices.

## Constructor Mapping

Sage `Poset(...)`, `MeetSemilattice(...)`, `JoinSemilattice(...)`, and
`LatticePoset(...)` remain inventory evidence for constructor design. They are
not exposed as project variadic constructors.

The documented `Poset(...)` input cases map to named constructor paths under
`Posets().Constructors()`:
- elements plus relations;
- elements plus an order predicate;
- elements plus a cover predicate;
- upper-cover dictionary;
- upper-cover list;
- acyclic `DiGraph` whose edges are either declared cover relations or declared order relations;
- existing poset refinement.

The finite Hasse-diagram constructor is the canonical directed-graph constructor:
the input graph is acyclic, loop-free, multi-edge-free, and transitively reduced, and
its directed edges are cover relations. A separate finite relation-digraph constructor
may accept an acyclic relation graph and take its transitive reduction before forming
the Hasse diagram. Do not use a bare "acyclic DiGraph" signature without saying
whether edges are covers or order relations.

The implemented constructor names are:
- `from_hasse_digraph`, the canonical finite-poset constructor;
- `from_relation_digraph`, which computes the transitive reduction first;
- `from_relations`;
- `from_order_predicate`;
- `from_cover_predicate`;
- `from_upper_covers_dict`;
- `from_upper_covers`;
- `from_existing`.

`MeetSemilattice(...)`, `JoinSemilattice(...)`, and `LatticePoset(...)` map to
finite refinement constructors over the same named input cases, with the extra
assertion that meets, joins, or both exist. Their names use the mathematical target
object, such as `meet_semilattice_from_digraph`, `join_semilattice_from_digraph`, or
`lattice_from_digraph`.

`FinitePosets_n(n)` maps to a finite enumerated-set constructor for isomorphism
classes of posets on `n` elements. It should not become a poset subcategory.

`is_poset(dig)` maps to constructor validation for directed Hasse diagrams and
to any future `DiGraph`-based constructor precondition.

## Posets()

These Sage methods map to the root `Posets()` object surface:
- `le`, `lt`, `ge`, `gt`;
- `is_lequal`, `is_less_than`, `is_gequal`, `is_greater_than`;
- `upper_covers`, `lower_covers`;
- `order_ideal`, `order_filter`;
- `directed_subset`;
- `principal_order_ideal`, `principal_order_filter`, with Sage aliases
  `principal_lower_set` and `principal_upper_set`;
- `is_order_ideal`, `is_order_filter`;
- `is_chain_of_poset`, `is_antichain_of_poset`;
- `order_ideal_toggle`, `order_ideal_toggles`;
- non-facade element comparisons `__le__`, `__lt__`, `__ge__`, `__gt__`.

`compare_elements`, `relations`, `relations_iterator`, `relations_number`, and
`number_of_relations` refine the same order relation but require finite
enumeration in the current Sage implementation; they map to `Posets().Finite()`
until an infinite/lazy relation surface is designed.

## Posets().Finite()

The finite poset surface owns methods whose mathematics requires finite
enumeration of a Hasse diagram, finite intervals, or finite linear extensions.
Plain element listing and cardinality are inherited finite/enumerated-set surfaces,
not order-theoretic poset owners.
- linear-extension-aware sorting: `sorted`;
- bounds and extremal elements: `bottom`, `top`, `has_bottom`, `has_top`,
  `is_bounded`, `minimal_elements`, `maximal_elements`;
- Hasse data: `cover_relations`, `cover_relations_iterator`,
  `cover_relations_graph`, `hasse_diagram`, `covers`,
  `upper_covers_iterator`, `lower_covers_iterator`,
  `common_upper_covers`, `common_lower_covers`, `lequal_matrix`;
- intervals: `closed_interval`, `open_interval`, `interval`,
  `intervals_number`, `intervals_poset`, `is_linear_interval`,
  `linear_intervals_count`, `diamonds`;
- chains, antichains, and ideals: `chains`, `antichains`,
  `antichains_iterator`, `maximal_chains`, `maximal_chains_iterator`,
  `maximal_chain_length`, `maximal_antichains`, `is_chain`,
  `is_chain_of_poset`, `is_antichain_of_poset`,
  `order_ideal_cardinality`, `order_ideal_generators`,
  `order_filter_generators`, `order_ideal_complement_generators`,
  `panyushev_complement`, `directed_subsets`;
- linear extensions: `linear_extension`, `linear_extensions`,
  `linear_extensions_graph`, `is_linear_extension`,
  `random_linear_extension`, `with_linear_extension`;
- rank and width invariants: `rank`, `rank_function`, `is_ranked`,
  `is_graded`, `is_rank_symmetric`, `height`, `width`, `level_sets`,
  `greene_shape`, `dilworth_decomposition`, `dimension`, `jump_number`,
  `is_jump_critical`, `is_sperner`, `is_slender`,
  `is_incomparable_chain_free`, `is_EL_labelling`;
- finite recognition predicates: `is_connected`, `connected_components`,
  `is_eulerian`, `is_greedy`, `is_series_parallel`, `is_d_complete`,
  `is_induced_subposet`, `is_isomorphic`, `has_isomorphic_subposet`,
  `isomorphic_subposets`, `isomorphic_subposets_iterator`,
  `is_meet_semilattice`, `is_join_semilattice`, `is_lattice`,
  `is_self_dual`, `is_parent_of`;
- finite morphism predicates: `is_poset_morphism`, `is_poset_isomorphism`;
- finite poset constructions: `dual`, `subposet`, `canonical_label`,
  `relabel`, `completion_by_cuts`, `cuts`, `factor`, `disjoint_union`,
  `ordinal_sum`, `ordinal_product`, `ordinal_summands`,
  `lexicographic_sum`, `product`, `rees_product`, `star_product`,
  `slant_sum`, `with_bounds`, `without_bounds`;
- finite dynamics and random finite objects: `promotion`, `evacuation`,
  `random_order_ideal`, `random_maximal_chain`,
  `random_maximal_antichain`, `random_subposet`, `rowmotion`,
  `rowmotion_orbits`, `rowmotion_orbit_iter`, `panyushev_orbits`,
  `panyushev_orbit_iter`, `toggling_orbits`, `toggling_orbit_iter`;
- birational finite-poset dynamics: `birational_free_labelling`,
  `birational_toggle`, `birational_toggles`, `birational_rowmotion`.

Sage `certificate=True` variants are mapped to separately named certificate
methods. `height(certificate=True)` maps to `height_certificate()`;
`width(certificate=True)` maps to `width_certificate()`;
`dimension(certificate=True)` maps to `dimension_certificate()`;
`jump_number(certificate=True)` maps to `jump_number_certificate()`;
`is_jump_critical(certificate=True)` maps to
`jump_critical_certificate()`; `is_eulerian(certificate=True)` maps to
`eulerian_certificate()`; `is_greedy(certificate=True)` maps to
`greedy_certificate()`; `is_slender(certificate=True)` maps to
`slender_certificate()`; `is_meet_semilattice(certificate=True)` maps to
`meet_semilattice_certificate()`; and
`is_join_semilattice(certificate=True)` maps to
`join_semilattice_certificate()`. The predicate methods themselves remain
boolean.

`order_ideals_lattice` maps to `Posets().Finite()` because every finite poset
has a finite distributive lattice of order ideals.

## Posets().MeetSemilattice()

`meet` maps to `Posets().MeetSemilattice()` with two signatures:
- `meet(x: PosetElement, y: PosetElement) -> PosetElement`;
- `meet(elements: Sequence[PosetElement]) -> PosetElement`.

The sequence overload is an explicit fold over the binary meet. Sage's
optional aggregate `meet(x, y=None)` form is inventory evidence only; the
project surface does not expose the optional-argument spelling.

## Posets().JoinSemilattice()

`join` maps to `Posets().JoinSemilattice()` with two signatures:
- `join(x: PosetElement, y: PosetElement) -> PosetElement`;
- `join(elements: Sequence[PosetElement]) -> PosetElement`.

The sequence overload is an explicit fold over the binary join. Sage's
optional aggregate `join(x, y=None)` form is inventory evidence only; the
project surface does not expose the optional-argument spelling.

## Posets().MeetSemilattice().Finite()

The finite meet-semilattice surface owns:
- `atoms`;
- `meet_matrix`;
- `pseudocomplement`;
- `submeetsemilattice`.

`subjoinsemilattice` appears on Sage `FiniteMeetSemilattice`, but the
mathematical owner is `Posets().JoinSemilattice().Finite()` when the generated
object is a join-subsemilattice.

## Posets().JoinSemilattice().Finite()

The finite join-semilattice surface owns:
- `coatoms`;
- `join_matrix`;
- `subjoinsemilattice`.

## Posets().Lattice().Finite()

The finite lattice surface owns lattice identities, lattice element classes,
and constructions requiring both meet and join:
- distributive and modular predicates: `is_distributive`, `is_modular`,
  `is_lower_semimodular`, `is_upper_semimodular`,
  `is_semidistributive`, `is_join_semidistributive`,
  `is_meet_semidistributive`, `is_join_distributive`,
  `is_meet_distributive`;
- complement and irreducibility predicates: `is_atomic`, `is_coatomic`,
  `is_geometric`, `is_extremal`, `is_complemented`,
  `is_sectionally_complemented`, `is_cosectionally_complemented`,
  `is_relatively_complemented`, `is_pseudocomplemented`,
  `is_join_pseudocomplemented`, `is_orthocomplemented`;
- structural predicates: `is_supersolvable`, `is_planar`,
  `is_dismantlable`, `is_interval_dismantlable`, `is_left_modular`,
  `is_sublattice_dismantlable`, `is_stone`, `is_trim`,
  `is_vertically_decomposable`, `is_simple`, `is_isoform`,
  `is_uniform`, `is_regular`, `is_subdirectly_reducible`,
  `is_constructible_by_doublings`, `is_congruence_uniform`, `breadth`;
- element families: `double_irreducibles`, `join_primes`, `meet_primes`,
  `complements`, `is_modular_element`, `is_left_modular_element`,
  `neutral_elements`, `canonical_joinands`, `canonical_meetands`,
  `join_irreducibles`, `meet_irreducibles`,
  `join_irreducibles_poset`, `meet_irreducibles_poset`,
  `irreducibles_poset`;
- lattice constructions: `sublattice`, `is_sublattice`, `sublattices`,
  `sublattices_lattice`, `isomorphic_sublattices_iterator`,
  `maximal_sublattices`, `frattini_sublattice`, `skeleton`, `center`,
  `vertical_decomposition`, `vertical_composition`, `adjunct`,
  `day_doubling`, `subdirect_decomposition`;
- congruence constructions: `congruence_generated_by`, `quotient`,
  `congruence_lattice`;
- morphism check: `is_lattice_morphism`.

Sage `congruence(blocks)` maps to `congruence_generated_by(blocks)`.
The result is an `EquivalenceRelation`, represented by Sage's `SetPartition`
element class and mapped through `Sets().Partitioned()` as a partition of the
finite lattice's element set. Sage `congruences_lattice()` maps to
`congruence_lattice()`.

Sage `certificate=True` variants map to separately named certificate methods:
`atomic_certificate()`, `coatomic_certificate()`,
`complemented_certificate()`, `distributive_certificate()`,
`modular_certificate()`, `modular_elements_certificate(elements)`,
`join_distributive_certificate()`, `meet_distributive_certificate()`,
`stone_certificate()`, `meet_semidistributive_certificate()`,
`join_semidistributive_certificate()`, `trim_certificate()`,
`cosectionally_complemented_certificate()`,
`relatively_complemented_certificate()`,
`sectionally_complemented_certificate()`, `breadth_certificate()`,
`upper_semimodular_certificate()`, `lower_semimodular_certificate()`,
`supersolvable_certificate()`, `vertically_decomposable_certificate()`,
`dismantlable_certificate()`, `interval_dismantlable_certificate()`,
`subdirectly_reducible_certificate()`, `isoform_certificate()`,
`uniform_certificate()`, `regular_certificate()`, and
`simple_certificate()`.
Boolean predicates do not take a `certificate` argument.

## Deferred Non-Core Surfaces

The Sage method groups inventoried in `SAGE_INVENTORY.md` are not open design
decisions. Their final placement follows the source finite-poset hypothesis and the
target mathematical object or display/interop status.

| Sage surface | Public owner/status | Codomain / migration consequence |
| --- | --- | --- |
| `comparability_graph()`, `incomparability_graph()` | `Posets().Finite().ParentMethods` graph-valued constructions | Return graph objects derived from the finite poset. Graph methods belong to a future graph subtree or Sage graph interop, not to `Posets()`. |
| `frank_network()` | `Posets().Finite().ParentMethods` network-valued construction | Return a directed network/graph object attached to the finite poset. Flow/network algorithms belong to the graph/network codomain. |
| `graphviz_string()`, `plot(...)`, `show(...)`, `tikz(...)`, `order_ideal_plot(...)` | display-only / export-only; no category method | Keep as notebook, plotting, TikZ, Graphviz, or Sage-display interop. Do not make display data part of the mathematical poset API. |
| `order_polytope()`, `chain_polytope()` | finite-poset constructions with polyhedron codomain | Return polyhedron/polytope objects. Posets own the source construction; polyhedral operations belong to a polyhedra/polytope subtree or Sage polyhedron interop. |
| `order_complex()` | finite-poset construction with simplicial-complex codomain | Return a simplicial-complex object. Simplicial-complex methods are codomain methods, not poset methods. |
| `incidence_algebra()` | finite-poset algebra-valued construction | Return an algebra over the requested base ring. Algebra operations belong to `Algebras(R)`; the poset source method only constructs the incidence algebra. |
| `moebius_algebra()`, `quantum_moebius_algebra()` | finite-poset algebra-valued constructions | Return algebra objects. They refine through algebra owners when admitted; their multiplication and ideals are not poset methods. |
| `feichtner_yuzvinsky_ring()` | finite-lattice / arrangement-style ring-valued construction where Sage defines it | Return a ring/algebra object. Ring operations belong to `rings`; algebraic structure belongs to `algebras`. |
| `p_partition_enumerator()` | finite-poset enumerator/generating-function construction | Return a generating function or symmetric/quasisymmetric-function object. The codomain owner is the relevant algebraic-combinatorics function ring once admitted. |
| `zeta_polynomial()`, `apozeta_polynomial()`, `chain_polynomial()`, `characteristic_polynomial()`, `f_polynomial()`, `flag_f_polynomial()`, `flag_h_polynomial()`, `h_polynomial()`, `M_triangle()`, `degree_polynomial()`, `coxeter_polynomial()`, `kazhdan_lusztig_polynomial()` | finite-poset or finite-lattice polynomial invariants, according to Sage's method domain | Return polynomial objects or polynomial-like invariants. The invariant method is poset-owned; polynomial arithmetic belongs to the polynomial-ring codomain. |
| `moebius_function()` | finite-poset invariant method | Return scalar Möbius values for comparable elements or the whole finite poset, following Sage's signature. |
| `moebius_function_matrix()`, `coxeter_transformation()`, `coxeter_smith_form()` | finite-poset matrix-valued invariant methods | Return matrix or Smith-form data. Matrix algebra belongs to the matrix/ring/module codomain, not `Posets()`. |
| `magnitude()`, `spectrum()`, `atkinson()` | finite-poset scalar/list/matrix invariant methods where Sage defines them | Keep as finite-poset invariants with scalar, list, or matrix codomains; downstream numeric or spectral operations belong to the returned object. |
| `order_polynomial()` | finite-poset polynomial invariant | Return the order polynomial counting order-preserving maps to finite chains. Polynomial arithmetic belongs to the polynomial-ring codomain. |
| `unwrap()` | raw Sage compatibility access only; no category method | May be used internally at the Sage boundary. Do not expose it as mathematical API. |
| `_libgap_()`, `_macaulay2_init_(...)` | backend interop only; no category method | Keep as Sage backend serialization / initialization surface. Do not expose backend strings or handles as mathematical poset API. |
| `_repr_()`, `_latex_()`, `_rich_repr_(...)`, `plot(...)`, `show(...)`, `tikz(...)`, `graphviz_string(...)`, `order_ideal_plot(...)`, `rowmotion_orbits_plots()`, `toggling_orbits_plots(...)` | display-only / export-only; no category method | Keep as notebook, plotting, TikZ, Graphviz, or Sage-display interop. Do not make display data part of the mathematical poset API. |
| `__classcall__(...)`, `__init__(...)`, `__bool__()`, `__contains__(...)`, `__iter__()`, `__call__(...)`, `_element_constructor_(...)`, `_element_to_vertex(...)`, `_vertex_to_element(...)`, `_list()` | Sage parent/element runtime plumbing | Preserve at the wrapper boundary as needed; these do not define new mathematical poset operations beyond construction normalization, containment, iteration, coercion, and element conversion already owned by constructor, parent, or set infrastructure. |
| `_kl_poly(...)` | private implementation helper for `kazhdan_lusztig_polynomial(...)` | Keep private. The public mathematical invariant is `kazhdan_lusztig_polynomial(...)`. |

Order-theoretic lattice terminology here refers only to finite lattice posets in the
`posets` subtree. It does not import module/quadratic lattice vocabulary from
`lattices`.

## Slice And Coslice Structures

`Posets().ObjectsOver(P)` and `Posets().ObjectsUnder(P)` own the poset-specific
`structure_poset()` and order-preserving `structure_map()` methods. The old local
`structure_domain()` and `structure_codomain()` methods now map to the Cat-owned
universal structure-morphism surface via `structure_morphism().domain()` and
`structure_morphism().codomain()`.

## Completeness Reconciliation: Posets

This pass checked the local inventory, the converted mapping body, the installed
Sage 10.7 category providers for posets, finite posets, lattice posets, and finite
lattice posets, plus the concrete finite poset and finite lattice implementation
classes.

- The Sage category provider `Posets.ParentMethods` is source-backed as the highest
  owner for order comparison, covers, generated ideals/filters, principal
  ideals/filters, directed subsets, order-ideal toggles, and chain/antichain tests.
  These methods require only a partially ordered set structure and therefore stay on
  `Posets()`, even when Sage's concrete implementation is finite.
- `FinitePosets.ParentMethods` adds methods whose definitions enumerate ideals,
  filters, antichains, or all elements of a finite poset: order/filter generators,
  Panyushev complement, rowmotion, toggling orbits, birational rowmotion/labellings,
  finite morphism and isomorphism checks, finite directed subsets, self-duality, and
  finite lattice recognition. These map to `Posets().Finite()`.
- The concrete `FinitePoset` class contributes additional finite surfaces not present
  in the first converted mapping: linear-extension-aware `sorted`, cover iterators,
  `lequal_matrix`, `diamonds`, `is_EL_labelling`, and `order_polynomial`. These are
  finite-poset methods or finite-poset invariants, not codomain-owned graph/algebra
  methods.
- `LatticePosets.ParentMethods` requires total binary `meet` and `join`, so the
  project keeps those methods on the meet- and join-semilattice refinements rather
  than on arbitrary finite posets. Sage concrete `FinitePoset.meet(x,y)` and
  `FinitePoset.join(x,y)` are treated as partial implementation evidence until the
  recognition predicates establish the corresponding semilattice hypothesis.
- `FiniteLatticePosets.ParentMethods` owns finite lattice irreducible-element posets
  and `is_lattice_morphism`. Concrete finite lattice methods that require both meet
  and join, including `breadth`, congruences, sublattices, decompositions, and
  lattice identities, map to `Posets().Lattice().Finite()`.
- Sage plotting, Graphviz/TikZ, GAP/Macaulay2 serialization, element conversion, and
  private runtime helpers are routed as display, backend interop, or parent-plumbing
  surfaces. They do not become mathematical poset methods.
- Certificate-bearing Sage predicates are preserved by named certificate methods.
  Boolean predicates remain boolean, avoiding Sage-style option-bag signatures while
  preserving the evidence surfaces.

Negative missing-surface finding for this Posets pass:

- Searched: `category_specs/posets/docs/SAGE_INVENTORY.md`;
  `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-POSETS.md`;
  installed Sage 10.7 files `sage/categories/posets.py`,
  `sage/categories/finite_posets.py`, `sage/categories/lattice_posets.py`,
  `sage/categories/finite_lattice_posets.py`,
  `sage/combinat/posets/posets.py`, and `sage/combinat/posets/lattices.py`;
  a direct source-file search under installed `sage/categories/` and
  `sage/combinat/posets/`; and a method-name comparison between the checked source
  files and this tracked mapping spec.
- Found: the first comparison found unmapped provider/concrete names including
  `principal_order_ideal`, `principal_order_filter`, `directed_subset`,
  `directed_subsets`, `order_ideal_generators`, `order_filter_generators`,
  `order_ideal_complement_generators`, rowmotion/Panyushev/toggling orbit methods,
  birational rowmotion methods, `is_poset_morphism`, `is_poset_isomorphism`,
  `is_self_dual`, `is_lattice`, `sorted`, `upper_covers_iterator`,
  `lower_covers_iterator`, `lequal_matrix`, `diamonds`, `is_EL_labelling`,
  `order_polynomial`, `breadth`, and backend/display/runtime hooks. Those surfaces
  are now mapped above. I found no further public checked-source poset method surface
  that requires a new mathematical owner beyond `Posets()`, `Posets().Finite()`,
  `Posets().MeetSemilattice()`, `Posets().JoinSemilattice()`,
  `Posets().Lattice().Finite()`, or the deferred interop/display table.
- Conclusion: inference -- for the checked Sage category-provider and finite
  poset/lattice implementation surface, the Posets mapping spec is now source-complete
  modulo separate audits of graph, polyhedron, algebra, polynomial, backend, and
  display codomains.
- Confidence: Medium.
- Gaps: this pass did not audit every named example constructor in
  `sage/combinat/posets/poset_examples.py`, non-poset combinatorics modules such as
  interval posets, or Sage git history. Those are constructor/example or separate
  combinatorics surfaces, not the core category-provider and finite-poset method
  surface checked here.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Automated 6-gate subagent
**Overall outcome:** All 6 gates PASS. No blocking issues found.

### G1 — Source Files Exist

**Verdict: PASS**

Evidence — all six installed Sage source files and both local inventory/mapping
documents verified present on disk:

| Source | Path | Exists |
|--------|------|--------|
| Sage category posets | `sage/categories/posets.py` | ✓ (722 lines) |
| Sage finite posets | `sage/categories/finite_posets.py` | ✓ (1994 lines) |
| Sage lattice posets | `sage/categories/lattice_posets.py` | ✓ (89 lines) |
| Sage finite lattice posets | `sage/categories/finite_lattice_posets.py` | ✓ (242 lines) |
| Sage concrete posets | `sage/combinat/posets/posets.py` | ✓ |
| Sage concrete lattices | `sage/combinat/posets/lattices.py` | ✓ |
| Local inventory | `category_specs/posets/docs/SAGE_INVENTORY.md` | ✓ (179 lines) |
| Local mapping redirect | `category_specs/posets/docs/MAPPING.md` | ✓ (7 lines, redirect to this spec) |

Paths resolved under `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/`
(SageMath 10.7 environment) and `/home/dzack/research/category_specs/posets/docs/`.

Minor note: SAGE_INVENTORY.md self-reports Sage 10.8; the spec coverage ledger reports
Sage 10.7. This is a version-skew documentation inconsistency, not a source-missing
issue. The installed source files are what the spec actually audits.

### G2 — Sage Surface Completeness

**Verdict: PASS**

The spec's Completeness Reconciliation section (lines 365–435) documents a thorough
two-pass method reconciliation:

- **Pass 1 (initial mapping):** Converted the original MAPPING.md into Category
  Hierarchy, Constructor Mapping, and per-category method lists (Posets, Finite,
  MeetSemilattice, JoinSemilattice, Lattice.Finite, Deferred Surfaces).
- **Pass 2 (negative finding):** Cross-referenced every Sage category-provider method
  and concrete-class method against the mapped surface. Found unmapped names
  (`principal_order_ideal`, `directed_subset`, `directed_subsets`,
  `order_ideal_generators`, rowmotion/Panyushev/toggling orbit methods, birational
  methods, `is_poset_morphism`, `is_self_dual`, `is_lattice`, `sorted`,
  `upper_covers_iterator`, `lequal_matrix`, `diamonds`, `is_EL_labelling`,
  `order_polynomial`, `breadth`, backend/display/runtime hooks) — all now mapped.

Cross-verification of Sage category-provider methods against the spec:

- **Posets.ParentMethods** (17 methods): `le`, `lt`, `ge`, `gt`, `upper_covers`,
  `lower_covers`, `order_ideal`, `order_filter`, `directed_subset`,
  `principal_order_ideal`, `principal_order_filter`, `order_ideal_toggle`,
  `order_ideal_toggles`, `is_order_ideal`, `is_order_filter`, `is_chain_of_poset`,
  `is_antichain_of_poset`. All mapped to `Posets()` root surface (lines 139–151). ✓
- **FiniteLatticePosets.ParentMethods** (6 methods): `join_irreducibles`,
  `join_irreducibles_poset`, `meet_irreducibles`, `meet_irreducibles_poset`,
  `irreducibles_poset`, `is_lattice_morphism`. All mapped to
  `Posets().Lattice().Finite()` (lines 268–299). ✓
- **Concrete FinitePoset methods:** Verified against SAGE_INVENTORY.md (lines 67–125)
  and mapped to `Posets().Finite()` or deferred surfaces. ✓
- **Concrete FiniteLatticePoset methods:** Verified against SAGE_INVENTORY.md
  (lines 147–179) and mapped to `Posets().Lattice().Finite()` or deferred. ✓
- **Deferred surfaces table** (lines 325–355): accounts for graph, polyhedron,
  algebra, polynomial, display, backend-interop, and runtime-plumbing surfaces. ✓

Confidence is Medium per the spec's own assessment. Acknowledged gaps (constructor
examples, interval posets, git history) are explicitly scoped out as non-core
surfaces and do not affect category-provider method completeness.

### G3 — Constructor Routes Mathematically Valid

**Verdict: PASS**

The poset category hierarchy in the spec (lines 77–91):

```text
Posets()
|-- Finite()
|-- MeetSemilattice()
|   `-- Finite()
|-- JoinSemilattice()
|   `-- Finite()
`-- Lattice()
    `-- Finite()
```

Verified against mathematical definitions and Sage source hierarchy:

- **Posets()** — Sage `Posets(Category)` with `super_categories() -> [Sets]`. Mathematically,
  a poset is a set with a reflexive, antisymmetric, transitive relation. The spec
  correctly places order-comparison methods (`le`, `lt`, `ge`, `gt`), cover methods,
  ideal/filter methods, and toggle methods here — none require finiteness or
  semilattice structure. ✓

- **Posets().Finite()** — Sage `FinitePosets(CategoryWithAxiom)` with
  `super_categories() -> [Posets, FiniteSets]`. The spec correctly places all methods
  requiring finite enumeration (Hasse diagrams, interval enumeration, chain/antichain
  enumeration, linear extensions, rank/width invariants, finite recognition
  predicates, finite constructions) here. ✓

- **Posets().MeetSemilattice()** — This is a project design refinement. Sage has no
  separate meet-semilattice category; `LatticePosets` inherits directly from `Posets`
  and declares both `meet` and `join` as abstract methods. The spec's decomposition
  is mathematically sound: a meet-semilattice is a poset where every pair of elements
  has a greatest lower bound. The `meet` operation is well-defined at this level and
  placing it on `MeetSemilattice()` rather than `Lattice()` is the correct minimal
  owner. ✓

- **Posets().JoinSemilattice()** — Same reasoning as above. The `join` operation is
  well-defined at the join-semilattice level. ✓

- **Posets().Lattice()** — The spec states this is "the common order-theoretic
  refinement of `Posets().MeetSemilattice()` and `Posets().JoinSemilattice()`." This
  is mathematically precise: a lattice is exactly a poset that is both a
  meet-semilattice and a join-semilattice. Sage `LatticePosets.super_categories() ->
  [Posets]`. The spec's two-parent refinement is a proper mathematical strengthening
  over Sage's flatter hierarchy. ✓

- **Posets().Lattice().Finite()** — Sage `FiniteLatticePosets(CategoryWithAxiom)` with
  `super_categories() -> [LatticePosets, FinitePosets]`. The spec correctly places
  lattice-specific finite methods (distributive/modular predicates, irreducibles,
  congruences, sublattice constructions, lattice morphisms) here. ✓

Constructor mapping (lines 93–136):

- Sage variadic `Poset(data, ...)` is decomposed into named constructor paths
  (`from_hasse_digraph`, `from_relation_digraph`, `from_relations`,
  `from_order_predicate`, `from_cover_predicate`, `from_upper_covers_dict`,
  `from_upper_covers`, `from_existing`). This is a mathematically valid refinement:
  each named path has a well-defined input type and hypothesis.
- The distinction between `from_hasse_digraph` (edges are cover relations) and
  `from_relation_digraph` (edges are order relations, transitive reduction applied)
  is correctly stated. ✓
- `FinitePosets_n(n)` is correctly routed to an enumerated-set constructor, not a
  poset subcategory. ✓
- `is_poset(dig)` correctly routed to constructor validation. ✓

The `subjoinsemilattice` routing (spec lines 255–257) is mathematically correct:
a method that constructs join-subsemilattices belongs to `JoinSemilattice().Finite()`,
even though Sage places it on `FiniteMeetSemilattice`. The spec correctly overrides
Sage's placement based on mathematical ownership.

### G4 — Nonmathematical Targets Rejected

**Verdict: PASS**

The spec systematically identifies and rejects nonmathematical surfaces:

- **Display/export surfaces** (lines 335, 349): `graphviz_string()`, `plot(...)`,
  `show(...)`, `tikz(...)`, `order_ideal_plot(...)`, `rowmotion_orbits_plots()`,
  `toggling_orbits_plots(...)`, `_repr_()`, `_latex_()`, `_rich_repr_(...)` —
  all marked "display-only / export-only; no category method." ✓

- **Backend interop** (lines 348): `_libgap_()`, `_macaulay2_init_(...)` — marked
  "backend interop only; no category method." ✓

- **Raw Sage compatibility** (line 347): `unwrap()` — marked "raw Sage compatibility
  access only; no category method." ✓

- **Runtime plumbing** (line 350): `__classcall__`, `__init__`, `__bool__`,
  `__contains__`, `__iter__`, `__call__`, `_element_constructor_`,
  `_element_to_vertex`, `_vertex_to_element`, `_list` — marked as "Sage parent/element
  runtime plumbing" preserved only at the wrapper boundary. ✓

- **Private helpers** (line 351): `_kl_poly(...)` — marked as private implementation
  helper, not public API. ✓

- **Sage option-bag patterns** (lines 209–222, 307–323): `certificate=True` variants
  are decomposed into separately named `_certificate()` methods. Boolean predicates
  remain boolean. This is interface strengthening that avoids variadic option bags. ✓

- **Codomain-owned surfaces** (lines 331–343): Graph methods (`comparability_graph`,
  `frank_network`), polyhedron methods (`order_polytope`, `chain_polytope`),
  simplicial complex (`order_complex`), algebra methods (`incidence_algebra`,
  `moebius_algebra`), ring methods (`feichtner_yuzvinsky_ring`), generating functions
  (`p_partition_enumerator`), and polynomial invariants (zeta, chain, characteristic,
  Kazhdan-Lusztig, etc.) are correctly identified as poset-source constructions whose
  return objects belong to other codomain categories. The spec preserves the poset
  source method while correctly routing downstream operations to their proper
  categories. ✓

No evidence of nonmathematical targets being admitted as mathematical poset methods.

### G5 — Ambiguities Routed to Decision Cards

**Verdict: PASS**

The spec routes unresolved work to tracked cards:

- **Completeness gaps** (line 56): "remaining gaps routed through
  `[[TASK-MAPPING-DOC-COMPLETENESS-RESEARCH]]`." This task exists at
  `/home/dzack/research/plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/plans/PLAN-CATEGORY-SPEC-SOURCE-MAPS-AND-ADMISSION/PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT/tasks/TASK-MAPPING-DOC-COMPLETENESS-RESEARCH.md`,
  is `status: complete`, and documents its reconciliation across all 11 mapping specs
  including Posets. ✓

- **Deferred codomain surfaces** (lines 331–343): Graph, polyhedron, simplicial
  complex, algebra, polynomial, and ring-valued methods are explicitly deferred as
  codomain-owned. These are not dropped — they are routed to their respective
  category subtrees for future admission. ✓

- **Parent dependency** (frontmatter line 6): references
  `[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]` — the owning feature card exists. ✓

- **Phase dependency** (frontmatter line 8): references
  `[[PHASE-MAPPING-DOC-SPEC-CONVERSION-AND-MATHEMATICAL-AUDIT]]` — the phase card
  exists and this spec lives under it. ✓

- **Explicitly scoped-out gaps** (lines 431–435): "this pass did not audit every
  named example constructor in `sage/combinat/posets/poset_examples.py`, non-poset
  combinatorics modules such as interval posets, or Sage git history." These are
  acknowledged as non-core surfaces; no evidence they hide unmapped category-provider
  methods. ✓

No hanging ambiguities found. Every deferred, gapped, or non-core surface has an
explicit status and routing.

### G6 — No Obligation Weakening

**Verdict: PASS**

The spec does not delete, weaken, or silently drop any Sage surface. Every
inventoried method is accounted for through one of four dispositions:

1. **Mathematical owner mapping** — every category-provider and concrete-class method
   is placed at its mathematically minimal category (Posets, Finite, MeetSemilattice,
   JoinSemilattice, Lattice.Finite). ✓

2. **Constructor decomposition** — Sage's variadic `Poset(data, ...)` is
   strengthened into named, well-typed constructor paths. Each input case is
   preserved; none are lost. ✓

3. **Certificate decomposition** — Sage's `certificate=True` boolean flags are
   strengthened into separately named `_certificate()` methods. The underlying
   mathematical capability is preserved; the interface is made more precise. ✓

4. **Codomain routing** — Graph, polyhedron, algebra, polynomial, and display methods
   are preserved as poset-source methods with codomain-owned return objects. No
   mathematical capability is removed; downstream operations are correctly routed. ✓

5. **Nonmathematical rejection** — Backend serialization, runtime plumbing, and
   display rendering are excluded from the mathematical API but preserved at the
   wrapper boundary as needed. This is interface purification, not weakening. ✓

Specific checks:

- No abstract methods are deleted from the spec.
- No constructor obligations are narrowed or removed.
- No smoke assertions are weakened.
- No obligations are moved without a source-grounded replacement owner.
- The spec explicitly states (line 28): "This tracked spec is the canonical mapping
  surface converted from `category_specs/posets/docs/MAPPING.md`" — the original
  MAPPING.md now redirects to this spec, preserving the provenance chain. ✓

The Sage version-skew (inventory claims 10.8, spec ledger claims 10.7) does not
constitute obligation weakening — the spec's completeness pass was done against the
installed 10.7 source, and the inventory is a separately maintained document.

### Summary

| Gate | Description | Result |
|------|-------------|--------|
| G1 | Source files exist | PASS |
| G2 | Sage surface completeness | PASS |
| G3 | Constructor routes mathematically valid | PASS |
| G4 | Nonmathematical targets rejected | PASS |
| G5 | Ambiguities routed to decision cards | PASS |
| G6 | No obligation weakening | PASS |

**Residual notes:**
- Sage version skew (10.7 vs 10.8) between spec coverage ledger and local inventory;
  not blocking but should be harmonized.
- `MeetSemilattice()` and `JoinSemilattice()` are project design refinements not
  present in Sage's category hierarchy — this is a deliberate and mathematically
  justified strengthening.
- The spec's Confidence rating of Medium is honest; the acknowledged gaps
  (constructor examples, interval posets, git history) are scoped as non-core and do
  not undermine the category-provider method mapping.
