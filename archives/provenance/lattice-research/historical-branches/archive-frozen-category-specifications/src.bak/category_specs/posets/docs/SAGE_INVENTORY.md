# Sage Poset Inventory

Sources read:
- Sage 10.8 combinatorics reference, `sage.combinat.posets.posets`
- Sage 10.8 combinatorics reference, `sage.combinat.posets.lattices`
- Local Sage category module names under `sage/categories`

Sage exposes category-level order theory through `sage.categories.posets.Posets`, `sage.categories.finite_posets.FinitePosets`, `sage.categories.lattice_posets.LatticePosets`, and `sage.categories.finite_lattice_posets.FiniteLatticePosets`. The documented concrete combinatorics classes are `sage.combinat.posets.posets.FinitePoset`, `sage.combinat.posets.lattices.FiniteMeetSemilattice`, `sage.combinat.posets.lattices.FiniteJoinSemilattice`, and `sage.combinat.posets.lattices.FiniteLatticePoset`.

## Category Method Providers

`Posets.ParentMethods` requires `le` and exposes derived order comparisons, covers, ideals, filters, chains, antichains, and order-ideal toggles.

`FinitePosets` refines finite enumerated posets.
The concrete `FinitePoset` class documents finite Hasse-diagram operations, intervals, top and bottom predicates, chain and antichain enumerators, linear extensions, subposets, products and sums, rank and width invariants, graph views, polytopes, incidence algebras, and several combinatorial polynomials.

`LatticePosets.ParentMethods` requires `meet` and `join`. `FiniteLatticePosets.ParentMethods` exposes irreducible-element posets and finite lattice morphism checks.

## Constructors

`Poset(data=None, element_labels=None, cover_relations=False, linear_extension=False, category=None, facade=None, key=None)` constructs a `FinitePoset`. The documented `data` cases are:
- elements plus relations `(E, R)`;
- elements plus a comparison or cover predicate `(E, f)`;
- a dictionary of upper covers;
- a list or tuple of upper covers;
- an acyclic loop-free `DiGraph`;
- an existing poset, returned as itself.

The constructor also documents optional element labels, cover-relation mode, default linear-extension control, facade and non-facade element behavior, and a unique-representation `key`.

`MeetSemilattice(data=None, *args, **options)` constructs a finite meet-semilattice by passing data through `Poset()` and checking that meets exist.

`JoinSemilattice(data=None, *args, **options)` constructs a finite join-semilattice by passing data through `Poset()` and checking that joins exist.

`LatticePoset(data=None, *args, **options)` constructs a finite lattice by passing data through `Poset()` and checking both semilattice conditions.

`FinitePosets_n(n)` is the finite enumerated set of all posets on `n` elements up to isomorphism.
Its documented method is `cardinality(from_iterator=False)`.

`is_poset(dig)` returns whether a directed graph is acyclic and transitively reduced.

## FinitePoset Surface

The documented `FinitePoset` methods are:

- Order comparisons and relations: `le`, `lt`, `ge`, `gt`, `is_lequal`, `is_less_than`, `is_gequal`, `is_greater_than`, `compare_elements`, `relations`, `relations_iterator`, `relations_number`, `number_of_relations`, `lequal_matrix`, `covers`.
- Covers and Hasse data: `cover_relations`, `cover_relations_iterator`, `cover_relations_graph`, `hasse_diagram`, `upper_covers`, `upper_covers_iterator`, `lower_covers`, `lower_covers_iterator`, `common_upper_covers`, `common_lower_covers`.
- Bounds and extremal elements: `bottom`, `top`, `has_bottom`, `has_top`, `is_bounded`, `minimal_elements`, `maximal_elements`, `with_bounds`, `without_bounds`.
- Intervals: `closed_interval`, `open_interval`, `interval`, `intervals_number`, `intervals_poset`, `is_linear_interval`, `linear_intervals_count`.
- Chains, antichains, and order ideals: `chains`, `antichains`, `antichains_iterator`, `maximal_chains`, `maximal_chains_iterator`, `maximal_chain_length`, `maximal_antichains`, `is_chain`, `is_chain_of_poset`, `is_antichain_of_poset`, `order_ideal`, `order_filter`, `order_ideal_cardinality`, `order_ideal_plot`, `random_order_ideal`, `random_maximal_chain`, `random_maximal_antichain`.
- Linear extensions and dynamics: `linear_extension`, `linear_extensions`, `linear_extensions_graph`, `is_linear_extension`, `random_linear_extension`, `with_linear_extension`, `promotion`, `evacuation`.
- Rank and width invariants: `rank`, `rank_function`, `is_ranked`, `is_graded`, `is_rank_symmetric`, `height`, `width`, `level_sets`, `greene_shape`, `dilworth_decomposition`, `dimension`, `jump_number`, `is_jump_critical`, `is_sperner`, `is_slender`, `is_incomparable_chain_free`.
- Poset predicates and recognition: `is_connected`, `connected_components`, `is_chain`, `is_eulerian`, `is_greedy`, `is_series_parallel`, `is_d_complete`, `is_induced_subposet`, `is_isomorphic`, `has_isomorphic_subposet`, `isomorphic_subposets`, `isomorphic_subposets_iterator`, `is_meet_semilattice`, `is_join_semilattice`, `is_parent_of`.
- Constructions: `dual`, `subposet`, `canonical_label`, `relabel`, `completion_by_cuts`, `cuts`, `factor`, `disjoint_union`, `ordinal_sum`, `ordinal_product`, `ordinal_summands`, `lexicographic_sum`, `product`, `rees_product`, `star_product`, `slant_sum`.
- Graphs, polytopes, complexes, and display: `comparability_graph`, `incomparability_graph`, `frank_network`, `order_complex`, `order_polytope`, `chain_polytope`, `graphviz_string`, `plot`, `show`, `tikz`.
- Polynomial and matrix invariants: `zeta_polynomial`, `apozeta_polynomial`, `chain_polynomial`, `characteristic_polynomial`, `f_polynomial`, `flag_f_polynomial`, `flag_h_polynomial`, `h_polynomial`, `M_triangle`, `degree_polynomial`, `coxeter_polynomial`, `coxeter_transformation`, `coxeter_smith_form`, `kazhdan_lusztig_polynomial`, `moebius_function`, `moebius_function_matrix`, `magnitude`, `spectrum`, `atkinson`.
- Algebraic constructions: `incidence_algebra`, `p_partition_enumerator`.
- Enumeration and element access: `cardinality`, `list`, `unwrap`, `random_subposet`, `diamonds`.

The concrete class also documents `join(x, y)` and `meet(x, y)` on finite posets; the recognition methods `is_join_semilattice` and `is_meet_semilattice` determine whether these operations are total.

## Finite Semilattice Surface

`FiniteMeetSemilattice` documents:
- `atoms`;
- `meet`;
- `meet_matrix`;
- `pseudocomplement`;
- `submeetsemilattice`;
- `subjoinsemilattice`.

`FiniteJoinSemilattice` documents:
- `coatoms`;
- `join`;
- `join_matrix`.

## FiniteLatticePoset Surface

`FiniteLatticePoset` documents:
- Lattice predicates: `is_distributive`, `is_modular`, `is_lower_semimodular`, `is_upper_semimodular`, `is_semidistributive`, `is_join_semidistributive`, `is_meet_semidistributive`, `is_join_distributive`, `is_meet_distributive`, `is_atomic`, `is_coatomic`, `is_geometric`, `is_extremal`, `is_complemented`, `is_sectionally_complemented`, `is_cosectionally_complemented`, `is_relatively_complemented`, `is_pseudocomplemented`, `is_join_pseudocomplemented`, `is_orthocomplemented`, `is_supersolvable`, `is_planar`, `is_dismantlable`, `is_interval_dismantlable`, `is_left_modular`, `is_sublattice_dismantlable`, `is_stone`, `is_trim`, `is_vertically_decomposable`, `is_simple`, `is_isoform`, `is_uniform`, `is_regular`, `is_subdirectly_reducible`, `is_constructible_by_doublings`, `is_congruence_uniform`.
- Element classes and element predicates: `atoms`, `coatoms`, `double_irreducibles`, `join_primes`, `meet_primes`, `complements`, `pseudocomplement`, `is_modular_element`, `is_left_modular_element`, `neutral_elements`, `canonical_joinands`, `canonical_meetands`.
- Sublattice and semilattice constructions: `sublattice`, `submeetsemilattice`, `subjoinsemilattice`, `is_sublattice`, `sublattices`, `sublattices_lattice`, `isomorphic_sublattices_iterator`, `maximal_sublattices`, `frattini_sublattice`, `skeleton`, `center`, `vertical_decomposition`, `vertical_composition`, `adjunct`, `day_doubling`, `subdirect_decomposition`.
- Congruence constructions: `congruence`, `quotient`, `congruences_lattice`.
- Algebraic constructions: `moebius_algebra`, `quantum_moebius_algebra`, `feichtner_yuzvinsky_ring`.
