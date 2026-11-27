# Posets Mapping

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
- acyclic `DiGraph`;
- existing poset refinement.

The acyclic `DiGraph` constructor is the canonical constructor. Other
documented Sage input cases are non-variadic adaptations that route through the
same finite poset construction surface or through existing-poset refinement.

The implemented constructor names are:
- `from_digraph`, the canonical finite-poset constructor;
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
enumeration of a Hasse diagram, finite intervals, or finite linear extensions:
- element listing and cardinality: `list`, `cardinality`;
- bounds and extremal elements: `bottom`, `top`, `has_bottom`, `has_top`,
  `is_bounded`, `minimal_elements`, `maximal_elements`;
- Hasse data: `cover_relations`, `cover_relations_iterator`,
  `cover_relations_graph`, `hasse_diagram`, `covers`,
  `common_upper_covers`, `common_lower_covers`;
- intervals: `closed_interval`, `open_interval`, `interval`,
  `intervals_number`, `intervals_poset`, `is_linear_interval`,
  `linear_intervals_count`;
- chains, antichains, and ideals: `chains`, `antichains`,
  `antichains_iterator`, `maximal_chains`, `maximal_chains_iterator`,
  `maximal_chain_length`, `maximal_antichains`, `is_chain`,
  `is_chain_of_poset`, `is_antichain_of_poset`,
  `order_ideal_cardinality`;
- linear extensions: `linear_extension`, `linear_extensions`,
  `linear_extensions_graph`, `is_linear_extension`,
  `random_linear_extension`, `with_linear_extension`;
- rank and width invariants: `rank`, `rank_function`, `is_ranked`,
  `is_graded`, `is_rank_symmetric`, `height`, `width`, `level_sets`,
  `greene_shape`, `dilworth_decomposition`, `dimension`, `jump_number`,
  `is_jump_critical`, `is_sperner`, `is_slender`,
  `is_incomparable_chain_free`;
- finite recognition predicates: `is_connected`, `connected_components`,
  `is_eulerian`, `is_greedy`, `is_series_parallel`, `is_d_complete`,
  `is_induced_subposet`, `is_isomorphic`, `has_isomorphic_subposet`,
  `isomorphic_subposets`, `isomorphic_subposets_iterator`,
  `is_meet_semilattice`, `is_join_semilattice`, `is_parent_of`;
- finite poset constructions: `dual`, `subposet`, `canonical_label`,
  `relabel`, `completion_by_cuts`, `cuts`, `factor`, `disjoint_union`,
  `ordinal_sum`, `ordinal_product`, `ordinal_summands`,
  `lexicographic_sum`, `product`, `rees_product`, `star_product`,
  `slant_sum`, `with_bounds`, `without_bounds`;
- finite dynamics and random finite objects: `promotion`, `evacuation`,
  `random_order_ideal`, `random_maximal_chain`,
  `random_maximal_antichain`, `random_subposet`.

Sage `certificate=True` variants are mapped to separately named certificate
methods. `height(certificate=True)` maps to `height_certificate()`;
`width(certificate=True)` maps to `width_certificate()`;
`is_meet_semilattice(certificate=True)` maps to
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
  `is_constructible_by_doublings`, `is_congruence_uniform`;
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
`modular_certificate()`, and `modular_elements_certificate(elements)`.
Boolean predicates do not take a `certificate` argument.

## Deferred Non-Core Surfaces

The following Sage method groups are inventoried for later mapping. They are
not open design decisions; ownership follows the target mathematical object or
display/interop status:
- graph, plotting, and TikZ views: `comparability_graph`,
  `incomparability_graph`, `frank_network`, `graphviz_string`, `plot`,
  `show`, `tikz`;
- polytope and order-complex constructions: `order_polytope`,
  `chain_polytope`, `order_complex`;
- algebra surfaces: `incidence_algebra`, `p_partition_enumerator`,
  `moebius_algebra`, `quantum_moebius_algebra`,
  `feichtner_yuzvinsky_ring`;
- polynomial and Coxeter invariants: `zeta_polynomial`,
  `apozeta_polynomial`, `chain_polynomial`, `characteristic_polynomial`,
  `f_polynomial`, `flag_f_polynomial`, `flag_h_polynomial`,
  `h_polynomial`, `M_triangle`, `degree_polynomial`,
  `coxeter_polynomial`, `coxeter_transformation`, `coxeter_smith_form`,
  `kazhdan_lusztig_polynomial`, `moebius_function`,
  `moebius_function_matrix`, `magnitude`, `spectrum`, `atkinson`;
- display helpers and raw Sage compatibility accessors: `order_ideal_plot`,
  `unwrap`.

## Slice And Coslice Structures

`Posets().ObjectsOver(P)` and `Posets().ObjectsUnder(P)` own the poset-specific
`structure_poset()` and order-preserving `structure_map()` methods. The old local
`structure_domain()` and `structure_codomain()` methods now map to the Cat-owned
universal structure-morphism surface via `structure_morphism().domain()` and
`structure_morphism().codomain()`.
