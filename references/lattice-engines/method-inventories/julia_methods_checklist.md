# Julia Method Test Gap Checklist

Tracks Julia-relevant methods documented in `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (sections 1-4).
Check a box when there is at least one `method:` tagged test covering that method.

---

## 1. Indefinite.jl

### Methods

- [x] ``INDEF_FORM_TestEquivalence(Q1, Q2)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_indefinite_jl.py::test_1_indef_form_test_equivalence_two_equivalent_forms]
- [x] ``INDEF_FORM_AutomorphismGroup(Q)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_indefinite_jl.py::test_2_indef_form_automorphism_group_hyperbolic_plane]
- [x] ``INDEF_FORM_GetOrbitRepresentative(Q, C)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_indefinite_jl.py::test_3_indef_form_get_orbit_representative_isotropic_vectors]
- [x] ``INDEF_FORM_GetOrbit_IsotropicKplane(Q, k)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_indefinite_jl.py::test_4_indef_form_get_orbit_isotropic_kplane]
- [x] ``INDEF_FORM_GetOrbit_IsotropicKflag(Q, k)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_indefinite_jl.py::test_5_indef_form_get_orbit_isotropic_kflag]
### Definiteness

### References

## 2. Hecke.jl (via Oscar)

### 2.1 Types

### 2.2 Quadratic and hermitian spaces

- [ ] ``quadratic_space(K, n)` / `quadratic_space(K, G)``
- [x] ``hermitian_space(E, n)` / `hermitian_space(E, G)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_1_hermitian_space_construct_from_gram]
- [ ] ``rank(V)` / `dim(V)``
- [ ] ``gram_matrix(V)` / `gram_matrix(V, M)``
- [ ] ``det(V)` / `discriminant(V)``
- [x] ``diagonal(V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadspace_with_isom.py::test_11_diagonal_signature_tuple_positive_definite_space]
- [x] ``diagonal_with_transform(V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_2_diagonal_with_transform_returns_diagonal_and_matrix]
- [x] ``orthogonal_basis(V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_3_orthogonal_basis_returns_orthogonal_vectors]
- [ ] ``signature_tuple(V)``
- [x] ``is_regular(V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_4_is_regular_nondegenerate_space]
- [x] ``is_quadratic(V)` / `is_hermitian(V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_5_is_quadratic_type_check]
- [ ] ``is_positive_definite(V)` / `is_negative_definite(V)` / `is_definite(V)``
- [ ] ``hasse_invariant(V, p)` / `witt_invariant(V, p)``
- [x] ``invariants(V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_6_invariants_returns_rational_invariants]
- [ ] ``is_isometric(V, W)` / `is_isometric(V, W, p)``
- [x] ``is_locally_represented_by(U, V, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_7_is_locally_represented_by_a1_by_a2]
- [x] ``is_represented_by(U, V)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_8_is_represented_by_rank_1_in_rank_2]
- [x] ``inner_product(V, v, w)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_9_inner_product_on_space]
- [x] ``orthogonal_complement(V, M)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_10_orthogonal_complement_on_space]
- [x] ``orthogonal_projection(V, M)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_11_orthogonal_projection_on_space]
- [x] ``is_isotropic(V, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_12_is_isotropic_at_prime]
- [x] ``is_locally_hyperbolic(V, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_13_is_locally_hyperbolic_hermitian_space]
- [x] ``restrict_scalars(V, K, α)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadratic_spaces.py::test_14_restrict_scalars]
- [ ] ``direct_sum(V, W)` / `direct_product` / `biproduct``
### 2.3 Construction

- [ ] ``integer_lattice(; gram=G)``
- [ ] ``integer_lattice(B; gram=G)``
- [ ] ``lattice(V, B)``
- [ ] ``quadratic_lattice(K, gens; gram=M)``
- [x] ``hermitian_lattice(E, gens; gram=M)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_1_hermitian_lattice_construct_over_gaussian_integers]
- [ ] ``root_lattice(:A, n)` / `(:D, n)` / `(:E, n)` / `(:I, n)``
- [ ] ``hyperbolic_plane_lattice(n)``
- [x] ``leech_lattice()`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_construction.py::test_9_leech_lattice_rank_24_even_unimodular]
- [x] ``k3_lattice()`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_construction.py::test_10_k3_lattice_rank_22_signature_3_19]
- [x] ``mukai_lattice()`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_construction.py::test_13_mukai_lattice_rank_24_indefinite]
- [x] ``hyperkaehler_lattice(:K3, n=3)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_construction.py::test_14_hyperkaehler_lattice_k3_type]
- [ ] ``rescale(L, r)``
### 2.4 Intrinsic data

- [ ] ``gram_matrix(L)``
- [ ] ``basis_matrix(L)``
- [ ] ``ambient_space(L)``
- [ ] ``rational_span(L)``
- [ ] ``rank(L)``
- [ ] ``degree(L)``
- [ ] ``signature_tuple(L)``
  - Caveat: in current Hecke docs this returns `(n_positive, n_zero, n_negative)`, not a 2-tuple.
- [ ] ``det(L)``
- [ ] ``discriminant(L)``
- [ ] ``scale(L)``
- [ ] ``norm(L)``
- [ ] ``is_positive_definite(L)``
- [ ] ``is_negative_definite(L)``
- [ ] ``is_definite(L)``
- [ ] ``is_even(L)``
- [ ] ``is_integral(L)``
- [ ] ``is_unimodular(L)``
- [ ] ``is_primary(L, p)``
- [ ] ``is_primary_with_prime(L)``
- [ ] ``is_elementary(L, p)``
- [ ] ``is_elementary_with_prime(L)``
### 2.5 Reduction

- [ ] ``lll(L::ZZLat; same_ambient::Bool=true, redo::Bool=false, ctx::LLLContext=...)``
  - Caveat: `redo=true` forces recomputation even if result is cached; Lovász parameters are passed via `ctx`; runs on indefinite lattices but "shortness" is relative to a majorant.
### 2.6 Vector enumeration

- [ ] ``short_vectors(L, lb, ub)``
- [x] ``short_vectors_iterator(L, lb, ub)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_enumeration.py::test_9_short_vectors_iterator_lazy_enumeration]
- [ ] ``shortest_vectors(L)``
- [ ] ``close_vectors(L::ZZLat, v::Vector, [lb,] ub; check::Bool=false)``
  - Caveat: **`check` defaults to `false`** (not `true`); with `check=false` it runs on indefinite lattices but distances can be negative/zero (result ill-posed); returns `Vector{Tuple{Vector{Int}, QQFieldElem}}`.
- [x] ``short_vectors_affine(S, v, α, d)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_vinberg.py::test_3_short_vectors_affine_affine_enumeration]
- [x] ``vectors_of_square_and_divisibility(L, n, d)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_enumeration.py::test_10_vectors_of_square_and_divisibility]
- [x] ``enumerate_quadratic_triples(L, ...)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_enumeration.py::test_11_enumerate_quadratic_triples]
- [ ] ``minimum(L)``
- [ ] ``kissing_number(L)``
### 2.7 Genus and classification

#### ZZGenus methods

- [x] ``genus(L::ZZLat)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_1_genus_compute_genus_of_a2]
- [x] ``genus(A::MatElem)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_2_genus_from_gram_matrix]
- [x] ``genus(L, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_3_genus_local_genus_at_prime]
- [x] ``integer_genera(sig::Tuple{Int, Int}, det::RationalUnion; even::Bool=true, kwargs...)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_22_integer_genera_enumerate_genus_symbols]
  - Caveat: upstream constrains determinant sign by signature (`det` has sign `(-1)^{s_-}` for `sig=(s_+, s_-)`) and parity (`det ∈ 2ZZ` for `even=true`, `det ∈ ZZ` for `even=false`).
- [x] ``direct_sum(G1::ZZGenus, G2::ZZGenus)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_20_direct_sum_genus_direct_sum]
- [ ] ``representative(gen)``
- [ ] ``representatives(gen)``
- [ ] ``mass(gen)``
- [x] ``dim(gen)` / `rank(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_7_dim_genus_dimension_equals_rank]
- [x] ``signature(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_8_signature_genus_signature]
- [ ] ``det(gen)``
- [x] ``iseven(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_9_iseven_genus_evenness]
- [x] ``is_definite(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_10_is_definite_genus_definiteness]
- [ ] ``level(gen)``
- [x] ``scale(gen)` / `norm(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_12_scale_genus_scale]
- [ ] ``primes(gen)``
- [x] ``is_integral(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_15_is_integral_genus_integrality]
- [ ] ``local_symbol(gen, p)``
- [x] ``quadratic_space(gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_17_quadratic_space_genus_quadratic_space]
- [ ] ``rational_representative(gen)``
- [x] ``rescale(gen, a)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_19_rescale_genus_rescaling]
- [ ] ``represents(G1, G2)``
#### ZZLocalGenus methods

- [x] ``prime(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_25_prime_local_genus_prime]
- [x] ``iseven(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_26_iseven_local_genus_evenness]
- [x] ``symbol(S, scale)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_37_symbol_local_genus_jordan_block_invariants]
- [x] ``hasse_invariant(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_27_hasse_invariant_local_genus_hasse_invariant]
- [x] ``det(S)` / `dim(S)` / `rank(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_28_det_local_genus_determinant]
- [x] ``excess(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_30_excess_local_genus_excess]
- [x] ``signature(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_31_signature_local_genus_signature]
- [x] ``oddity(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_32_oddity_local_genus_2_adic_oddity]
- [x] ``scale(S)` / `norm(S)` / `level(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_39_scale_local_genus_scale]
- [x] ``representative(S)` / `gram_matrix(S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_33_representative_local_genus_representative]
- [x] ``rescale(S, a)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_35_rescale_local_genus_rescaling]
- [x] ``direct_sum(S1, S2)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_36_direct_sum_local_genus_direct_sum]
- [x] ``represents(S1, S2)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzgenus.py::test_42_represents_local_genus_representation]
#### Discriminant group and classification

- [ ] ``discriminant_group(L)``
- [ ] ``genus_representatives(L)``
- [ ] ``Hecke.quadratic_lattice_database()``
### 2.8 Automorphism and isometry

- [ ] ``automorphism_group_generators(L::AbstractLat; ambient_representation::Bool=true, depth::Int=-1, bacher_depth::Int=0)``
  - Caveat: upstream requires `is_definite(L)` — supports **both positive and negative definite** lattices; not restricted to positive definite only; `ambient_representation=true` returns generators in ambient-space coordinates.
- [ ] ``automorphism_group_order(L::AbstractLat; depth::Int=-1, bacher_depth::Int=0)``
  - Caveat: upstream requires `is_definite(L)` — supports **both positive and negative definite** lattices; not restricted to positive definite only.
- [ ] ``is_isometric(L1, L2)``
  - Caveat: upstream requires `is_definite(L1)` and `is_definite(L2)` — supports **both positive and negative definite** lattices; uses LLL to rescale ND to PD before comparison.
- [ ] ``is_isometric_with_isometry(L1, L2)``
  - Caveat: upstream requires `is_definite(L1)` and `is_definite(L2)`; documents tuple return `(isometric::Bool, f)` with `(false, zero_matrix(QQ, 0, 0))` on failure, and kwargs `depth=3`, `bacher_depth=5`, `ambient_representation=true`.
- [x] ``is_locally_isometric(L1, L2, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_automorphism.py::test_9_is_locally_isometric_same_lattice_at_prime_2]
- [ ] ``is_rationally_isometric(L1, L2)``
- [ ] ``hasse_invariant(L, p)``
- [ ] ``witt_invariant(L, p)``
### 2.9 Module operations and embeddings

- [ ] ``direct_sum(L1, L2)``
- [ ] ``direct_product(L1, L2)``
- [ ] ``biproduct(L1, L2)``
- [ ] ``intersect(L1, L2)``
- [x] ``+(L1, L2)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_18_lattice_sum_in_common_ambient]
- [x] ``*(n, L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_19_scalar_multiple_of_lattice]
- [ ] ``lattice_in_same_ambient_space(L, B)``
- [ ] ``orthogonal_submodule(L, S)``
- [ ] ``dual(L)``
- [ ] ``is_sublattice(L, S)``
- [x] ``is_sublattice_with_relations(L, S)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_20_is_sublattice_with_relations]
- [ ] ``is_primitive(L, S)``
- [ ] ``primitive_closure(L, S)``
- [x] ``divisibility(L, v)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_21_divisibility_of_vector]
- [x] ``in(v, L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_22_vector_membership_test]
- [x] ``irreducible_components(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_23_irreducible_components_of_direct_sum]
#### Overlattices and embeddings

- [x] ``glue_map(L, S, gen_imgs)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_1_glue_map_construct_glue_map]
- [x] ``overlattice(glue_map)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_2_overlattice_build_from_glue]
- [ ] ``primitive_extension(L1, L2, glue_map)``
- [x] ``local_modification(M, L, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_3_local_modification_at_prime]
  - Caveat: upstream assumes `M` is `Z_p`-maximal and `L` is isomorphic to `M` over `Q_p`.
- [ ] ``maximal_integral_lattice(L)``
- [ ] ``is_maximal_integral(L)``
- [x] ``is_maximal(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_4_is_maximal_test_maximality]
- [x] ``embed(L, gen)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_5_embed_lattice_into_genus]
- [x] ``embed_in_unimodular(L, ...)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_6_embed_in_unimodular]
  - Caveat: upstream notes this currently works only for even lattices.
#### Endomorphism-based sublattices

- [ ] ``kernel_lattice(L, f)``
- [x] ``invariant_lattice(::ZZLat, ::MatGroup)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_40_invariant_lattice_fixed_sublattice]
- [x] ``coinvariant_lattice(::ZZLat, ::MatGroup)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_41_coinvariant_lattice_orthogonal_complement_of_fixed]
- [x] ``invariant_coinvariant_pair(::ZZLat, ::Union{QQMatrix, Vector{QQMatrix}, MatGroup})`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_44_invariant_coinvariant_pair_rank_sum_equals_full_rank]
#### Root lattice recognition

- [x] ``root_lattice_recognition(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_13_root_lattice_recognition_identifies_a2]
- [x] ``root_lattice_recognition_fundamental(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_7_root_lattice_recognition_fundamental]
- [x] ``ADE_type(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_14_ade_type_identifies_root_type]
- [x] ``coxeter_number(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_15_coxeter_number_a2_coxeter_number_is_3]
- [x] ``highest_root(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_module_ops.py::test_16_highest_root_a2_highest_root]
### 2.10 Vinberg's algorithm

- [ ] ``vinberg_algorithm(Q::ZZMatrix, ub; v0, root_lengths, direction_vector)``
- [ ] ``vinberg_algorithm(S::ZZLat, ub; v0, root_lengths, direction_vector)``
### 2.11 Discriminant groups (`TorQuadModule`)

- [x] ``torsion_quadratic_module(M, N)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_1_torsion_quadratic_module_construct_from_cover_and_relations]
- [x] ``torsion_quadratic_module(q::QQMatrix)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_1_torsion_quadratic_module_construct_from_cover_and_relations]
- [x] ``abelian_group(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_3_abelian_group_underlying_abstract_group]
- [x] ``cover(T)` / `relations(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_4_cover_cover_lattice_of_torquadmodule]
- [x] ``gram_matrix_bilinear(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_6_gram_matrix_bilinear_bilinear_gram_over_q_z]
- [x] ``gram_matrix_quadratic(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_7_gram_matrix_quadratic_quadratic_gram_over_q_2z]
- [x] ``value_module(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_25_value_module_bilinear]
- [x] ``value_module_quadratic_form(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_26_value_module_quadratic_form]
- [x] ``modulus_bilinear_form(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_8_modulus_bilinear_form_modulus_of_bilinear_form]
- [x] ``modulus_quadratic_form(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_9_modulus_quadratic_form_modulus_of_quadratic_form]
- [x] ``quadratic_product(a)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_27_quadratic_product_element]
- [ ] ``inner_product(a, b)``
- [x] ``lift(a)` / `representative(a)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_29_lift_element_to_cover]
- [ ] ``orthogonal_submodule(T, S)``
- [x] ``is_isometric_with_isometry(T, U)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_22_is_isometric_with_isometry_torquadmodule_isometry_test]
  - Caveat: upstream documents tuple return `(Bool, map)` with `(false, 0)` on failure, with preconditions: equal quadratic-form moduli (or prior rescaling) and semiregular decomposition checks.
- [x] ``is_anti_isometric_with_anti_isometry(T, U)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_23_is_anti_isometric_with_anti_isometry_anti_isometry_test]
  - Caveat: upstream documents tuple return `(Bool, anti_map)` with `(false, 0)` on failure and the same modulus/rescale + semiregular preconditions.
- [x] ``is_degenerate(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_10_is_degenerate_a2_discriminant_group_is_non_degenerate]
- [x] ``is_semi_regular(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_11_is_semi_regular_a2_discriminant_group]
- [x] ``radical_bilinear(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_12_radical_bilinear_radical_of_bilinear_form]
- [x] ``radical_quadratic(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_13_radical_quadratic_radical_of_quadratic_form]
- [x] ``normal_form(T; partial=false)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_14_normal_form_normal_form_of_torquadmodule]
- [x] ``brown_invariant(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_15_brown_invariant_mod_8_invariant]
- [x] ``snf(T)` / `is_snf(T)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_17_is_snf_check_if_already_in_snf]
- [x] ``rescale(T, k)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_18_rescale_rescaled_torquadmodule]
- [x] ``genus(T, sig_pair)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_19_genus_genus_from_discriminant_form_and_signature]
- [x] ``is_genus(T, sig_pair)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_20_is_genus_check_genus_existence]
- [x] ``direct_sum(T1, T2)` / `direct_product` / `biproduct`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_21_direct_sum_torquadmodule_direct_sum]
- [x] ``submodules(T::TorQuadModule; order::Int, index::Int, subtype::Vector{Int}, quotype::Vector{Int})`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_24_submodules_enumerate_submodules]
  - Caveat: upstream docs expose four keyword filters: `order` (by cardinality), `index` (by index in `T`), `subtype` (by abelian-group invariants of submodule), `quotype` (by abelian-group invariants of quotient).
- [x] ``stable_submodules(T::TorQuadModule, act::Vector{TorQuadModuleMap}; quotype::Vector{Int})`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_31_stable_submodules]
  - Caveat: upstream requires `act` to be a `Vector{TorQuadModuleMap}`; only `quotype` is documented as keyword filter for the isometry-stable surface.
### 2.12 Hermitian lattices (`HermLat` / `QuadLat`)

- [x] ``base_field(L)` / `base_ring(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_2_base_field_returns_number_field]
- [x] ``fixed_field(L)` / `fixed_ring(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_3_fixed_field_returns_fixed_field_under_involution]
- [x] ``involution(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_10_involution_of_hermitian_form]
- [x] ``pseudo_matrix(L)` / `pseudo_basis(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_4_pseudo_matrix_returns_pseudo_matrix_representation]
- [x] ``coefficient_ideals(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_12_coefficient_ideals_of_pseudo_basis]
- [x] ``absolute_basis(L)` / `absolute_basis_matrix(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_13_absolute_basis_z_basis]
- [x] ``generators(L)` / `gram_matrix_of_generators(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_14_generators_hermitian_lattice]
- [x] ``local_basis_matrix(L, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_16_local_basis_matrix_at_prime]
- [x] ``jordan_decomposition(L, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_6_jordan_decomposition_at_a_prime]
- [ ] ``is_isotropic(L, p)``
- [x] ``is_modular(L)` / `is_modular(L, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_18_is_modular_hermitian_lattice]
- [x] ``can_scale_totally_positive(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_19_can_scale_totally_positive]
- [x] ``volume(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_lattices.py::test_20_volume_of_hermitian_lattice]
- [x] ``is_maximal_integral(L)` / `is_maximal(L)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_overlattices.py::test_4_is_maximal_test_maximality]
### 2.13 Quadratic spaces with isometry (`QuadSpaceWithIsom`)

- [ ] ``quadratic_space_with_isometry(V, f; check)``
  - Caveat: current upstream pages contain conflicting default wording for `check`; pass it explicitly when contract fidelity matters.
- [ ] ``quadratic_space_with_isometry(V; neg=false)``
- [x] ``space(Vf)` / `isometry(Vf)` / `order_of_isometry(Vf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadspace_with_isom.py::test_3_space_extract_space_from_quadspacewithisom]
  - Caveat: upstream documents `order_of_isometry(Vf) = PosInf` for infinite order; for rank-zero spaces, upstream uses `-1`.
- [ ] ``rank(Vf)` / `dim(Vf)` / `gram_matrix(Vf)` / `det(Vf)` / `discriminant(Vf)``
- [x] ``diagonal(Vf)` / `signature_tuple(Vf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_quadspace_with_isom.py::test_11_diagonal_signature_tuple_positive_definite_space]
- [ ] ``is_definite(Vf)` / `is_positive_definite(Vf)` / `is_negative_definite(Vf)``
- [ ] ``characteristic_polynomial(Vf)` / `minimal_polynomial(Vf)``
- [ ] ``^(Vf, n)``
- [ ] ``direct_sum(Vf::Union{QuadSpaceWithIsom, Vector{QuadSpaceWithIsom}}...)``
- [ ] ``rescale(Vf, a)``
- [ ] ``rational_spinor_norm(Vf; b)``
### 2.14 Lattices with isometry (`ZZLatWithIsom`)

#### Construction

- [ ] ``integer_lattice_with_isometry(L, f; check, ambient_representation)``
  - Caveat: upstream distinguishes matrix representation via `ambient_representation` (ambient-space basis vs fixed basis of `L`).
- [ ] ``integer_lattice_with_isometry(L; neg=false)``
- [ ] ``lattice(Vf::QuadSpaceWithIsom)``
- [ ] ``lattice(Vf::QuadSpaceWithIsom, B)``
- [ ] ``lattice_in_same_ambient_space(Lf, B)``
#### Accessors

- [ ] ``isometry(Lf)``
- [x] ``ambient_isometry(Lf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_9_ambient_isometry_isometry_on_ambient_space_preserves_gram]
- [ ] ``ambient_space(Lf)``
- [ ] ``lattice(Lf)``
- [ ] ``basis_matrix(Lf)``
- [ ] ``order_of_isometry(Lf)``
  - Caveat: upstream `latwithisom` defines this as the order of lattice isometry `f`, documented as a divisor of the ambient isometry order; both finite- and infinite-order isometries are supported.
- [ ] ``characteristic_polynomial(Lf)` / `minimal_polynomial(Lf)``
#### Attributes

- [ ] ``rank(Lf)`` / ``degree(Lf)``
- [ ] ``gram_matrix(Lf)`` / ``det(Lf)`` / ``discriminant(Lf)``
- [ ] ``signature_tuple(Lf)``
  - Caveat: this is the lattice signature tuple inherited from the underlying `L`, distinct from eigenspace-signature data returned by `signatures(Lf)`.
- [ ] ``rational_span(Lf)``
- [ ] ``genus(Lf)``
- [ ] ``minimum(Lf)``
  - Caveat: inherits the positive-definite requirement of the underlying lattice minimum routine.
- [ ] ``scale(Lf)`` / ``norm(Lf)``
- [ ] ``is_even(Lf)`` / ``is_integral(Lf)`` / ``is_unimodular(Lf)``
- [ ] ``is_primary(Lf, p)`` / ``is_primary_with_prime(Lf)``
- [ ] ``is_elementary(Lf, p)`` / ``is_elementary_with_prime(Lf)``
- [ ] ``is_positive_definite(Lf)`` / ``is_negative_definite(Lf)`` / ``is_definite(Lf)``

#### Type classification

- [x] ``type(Lf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_46_type_type_of_lattice_with_isometry]
- [x] ``is_of_type(Lf, t)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_47_is_of_type_roundtrip_with_type_lf]
- [x] ``is_of_same_type(Lf, Mg)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_48_is_of_same_type_same_vs_different_isometries]
- [x] ``is_of_hermitian_type(Lf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_49_is_of_hermitian_type_a2_with_negation]
- [x] ``hermitian_structure(Lf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_50_hermitian_structure_roundtrip_hermitian_rank]
- [x] ``trace_lattice_with_isometry(H)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_51_trace_lattice_with_isometry_roundtrip_from_hermitian]
- [x] ``trace_lattice_with_isometry(H, res)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_51_trace_lattice_with_isometry_roundtrip_from_hermitian]
- [x] ``is_hermitian(t::Dict)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_57_is_hermitian_type_dict_check]
#### Operations

- [ ] ``^(Lf, n)``
- [ ] ``direct_sum(Lf::Union{ZZLatWithIsom, Vector{ZZLatWithIsom}}...)``
- [ ] ``dual(Lf)``
- [ ] ``lll(Lf)``
- [ ] ``rescale(Lf, a)``
- [ ] ``orthogonal_submodule(Lf, B)``
#### Kernel sublattices

- [ ] ``kernel_lattice(Lf::ZZLatWithIsom, p::Union{ZZPolyRingElem, QQPolyRingElem})``
  - Caveat: upstream computes the kernel of the polynomial `p(f)` as a sublattice of `L` equipped with the induced action of `f`; such sublattices are primitive in `L` since `L` is non-degenerate.
- [ ] ``kernel_lattice(Lf::ZZLatWithIsom, l::Integer)``
  - Caveat: upstream computes the kernel of `f^l - 1`; also primitive in `L` by non-degeneracy.
- [x] ``invariant_lattice(Lf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_40_invariant_lattice_fixed_sublattice]
- [x] ``coinvariant_lattice(Lf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_41_coinvariant_lattice_orthogonal_complement_of_fixed]
- [x] ``invariant_coinvariant_pair(Lf::ZZLatWithIsom)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_44_invariant_coinvariant_pair_rank_sum_equals_full_rank]
  - Caveat: upstream return is `(ZZLatWithIsom, ZZLatWithIsom)` — invariant sublattice and coinvariant sublattice simultaneously.
#### Discriminant groups

- [ ] ``discriminant_group(Lf::ZZLatWithIsom)``
  - Caveat: upstream return is `(TorQuadModule, AutomorphismGroupElem)` — the discriminant module plus the element of `O(D_L)` induced by `f` (not just a module).
- [ ] ``discriminant_group(::Type{TorQuadModuleWithIsom}, Lf::ZZLatWithIsom; ambient_representation::Bool=true)``
  - Caveat: the type argument is `::Type{TorQuadModuleWithIsom}` (not a positional value); `ambient_representation` controls the coordinate basis for the induced action.
- [x] ``image_centralizer_in_Oq(Lf::ZZLatWithIsom)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_54_image_centralizer_in_oq_returns_group_and_homomorphism]
  - Caveat: upstream return is `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`. Hermitian Miranda-Morrison theory (used to compute this image in the general case) is only available for even lattices; definite lattices, ±identity isometries, and Euler-totient-rank cases bypass Miranda-Morrison without this restriction.
- [ ] ``image_in_Oq(Lf)``
  - Caveat: upstream documents this as the general Miranda-Morrison image of π: O(L) → O(D_L), available for both definite and indefinite lattices (distinct from `image_centralizer_in_Oq`).
- [x] ``discriminant_representation(L::ZZLat, G::MatGroup; ambient_representation::Bool=true, full::Bool=true, check::Bool=true)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom.py::test_53_discriminant_representation_returns_homomorphism]
  - Caveat: upstream return is `GAPGroupHomomorphism`; `full::Bool=true` controls whether full discriminant-group representation is computed; `check::Bool=true` validates input.
#### Spinor norm

- [ ] ``signatures(Lf::ZZLatWithIsom)``
  - Caveat: upstream constrains this to hermitian-type lattices with isometry whose minimal polynomial is irreducible and cyclotomic; returns `Dict{Int, Tuple{Int, Int}}`.
- [ ] ``rational_spinor_norm(Lf::ZZLatWithIsom; b::Int=-1)``
  - Caveat: `b` defaults to `-1` (not unset); computes spinor norm of the isometry with respect to the form `b·Φ`; returns `QQFieldElem`.
#### Enumeration

- [ ] ``enumerate_classes_of_lattices_with_isometry(::Union{ZZGenus, ZZLat}, ::Int)``
- [x] ``representatives_of_hermitian_type(::Union{ZZLat, ZZGenus}, ::Union{ZZPolyRingElem, QQPolyRingElem}, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_3_representatives_of_hermitian_type_a2_genus_order_2]
- [x] ``representatives_of_hermitian_type(::Union{ZZGenus, ZZLat}, ::Int, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_3_representatives_of_hermitian_type_a2_genus_order_2]
- [x] ``admissible_triples(::ZZGenus, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_4_admissible_triples_small_genus]
- [x] ``is_admissible_triple(::ZZGenus, ::ZZGenus, ::ZZGenus, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_5_is_admissible_triple_roundtrip_from_admissible_triples]
- [x] ``splitting(::ZZLatWithIsom, ::Int, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_7_splitting_generic_splitting]
- [x] ``splitting_of_hermitian_type(::ZZLatWithIsom, ::Int, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_6_splitting_of_hermitian_type_a2_negation]
- [x] ``splitting_of_prime_power(::ZZLatWithIsom, ::Int, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_8_splitting_of_prime_power_small_example]
- [x] ``splitting_of_pure_mixed_prime_power(::ZZLatWithIsom, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_9_splitting_of_pure_mixed_prime_power_small_example]
- [x] ``splitting_of_mixed_prime_power(::ZZLatWithIsom, ::Int, ::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_zzlat_with_isom_enumeration.py::test_10_splitting_of_mixed_prime_power_small_example]
### 2.15 Primitive embeddings

- [ ] ``primitive_embeddings(L, M)``
- [ ] ``primitive_embeddings(G::ZZGenus, M)``
- [x] ``primitive_embeddings(q::TorQuadModule, sig, M)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_primitive_embeddings.py::test_4_primitive_embeddings_via_torquadmodule]
- [ ] ``primitive_extensions(M, N)``
- [ ] ``equivariant_primitive_extensions(Mf::ZZLatWithIsom, Nf::ZZLatWithIsom; glue_only=false)``
- [x] ``admissible_equivariant_primitive_extensions(Mf, Nf, gen, poly, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_equivariant_primitive_extensions.py::test_3_admissible_equivariant_primitive_extensions_from_admissible_triple]
### 2.16 Hermitian genera

- [x] ``genus(L::HermLat)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_1_genus_global_genus_of_hermitian_lattice]
- [x] ``genus(L::HermLat, p)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_2_genus_local_genus_of_hermitian_lattice]
- [x] ``hermitian_genera(E::NumField, rank::Int, signatures::Vector{Tuple{Int, Int}}, determinant::Vector{QQFieldElem}; min_scale::Int=(determinant[1] != 0 ? 0 : -3), max_scale::Int=(determinant[1] != 0 ? 0 : 3), kwargs...)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_9_hermitian_genera_enumerate]
  - Caveat: upstream requires `E` imaginary quadratic, `rank > 0`, and same-sign determinants (positive for even rank, negative for odd rank).
- [x] ``hermitian_local_genera(E::NumField, p::AbsNumFieldOrderIdeal, rank::Int, determinant::QQFieldElem, min_scale::Int, max_scale::Int)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_10_hermitian_local_genera_enumerate]
- [x] ``representative(G)` / `representatives(G)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_3_representative_hermitian_genus_representative]
- [ ] ``mass(L)``
- [x] ``rank(G)` / `primes(G)` / `signatures(G)` / `is_integral(G)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_6_rank_hermitian_genus_rank]
- [x] ``scale(G)` / `norm(G)` / `local_symbols(G)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_13_local_symbols_hermitian_genus]
- [ ] ``direct_sum(G1, G2)` / `rescale(G, a)``
- [x] ``is_ramified(g)` / `is_split(g)` / `is_inert(g)` / `is_dyadic(g)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_hermitian_genera.py::test_16_is_ramified_local_genus]
### 2.17 Isometry group actions on lattices

- [ ] ``is_isometry(::Hecke.QuadSpace, ::QQMatrix)`` / ``is_isometry(::ZZLat, ::QQMatrix)``
- [x] ``is_isometry_list(::Hecke.QuadSpace, ::Vector{QQMatrix})`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_is_isometry_list_recognizes_true_and_false_cases]
- [x] ``is_isometry_group(::Hecke.QuadSpace, ::MatGroup)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_is_isometry_group_true_for_orthogonal_group]
  - Caveat: upstream `fingrpact` docs describe these check helpers as non-exported utilities for input validation.
- [x] ``is_stable_isometry(::ZZLatWithIsom)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_is_stable_isometry_identity_stabilizes_sublattice]
- [x] ``is_special_isometry(::ZZLatWithIsom)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_is_special_isometry_distinguishes_det_sign]
- [x] ``special_orthogonal_group(::ZZLat)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_special_orthogonal_group_is_isometry_group]
- [x] ``stable_orthogonal_group(::ZZLat)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_stable_orthogonal_group_stabilizes_sublattice]
- [x] ``stabilizer_discriminant_subgroup(...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_stabilizer_discriminant_subgroup_refines_group_order]
- [x] ``stabilizer_in_orthogonal_group(...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_stabilizer_in_orthogonal_group_refines_orthogonal_group]
- [x] ``pointwise_stabilizer_in_orthogonal_group(...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_pointwise_stabilizer_in_orthogonal_group_nested_in_setwise]
- [x] ``setwise_stabilizer_in_orthogonal_group(...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_setwise_stabilizer_in_orthogonal_group_refines_full_group]
- [x] ``pointwise_stabilizer_orthogonal_complement_in_orthogonal_group(...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_pointwise_stabilizer_orthogonal_complement_refines_group]
- [x] ``stabilizer_in_diagonal_action(...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_stabilizer_in_diagonal_action_produces_finite_group]
  - Caveat: current upstream `fingrpact` docs list these runtime names but do not expose typed dispatch signatures for this stabilizer family.
- [x] ``maximal_extension(::ZZLat, ::ZZLat, ::MatGroup)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_maximal_extension_contains_input_group]
- [x] ``saturation(::ZZLat, ::MatGroup, ::MatGroup)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_isometry_actions.py::test_4_saturation_primitive_closure_in_lattice]
  - Caveat: upstream presents this explicit saturation computation for finite ambient group input.
- [x] ``saturation(::ZZLat, ::MatGroup)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_isometry_actions.py::test_4_saturation_primitive_closure_in_lattice]
  - Caveat: upstream states this form is available when the coinvariant lattice is definite or rank 2.
- [x] ``is_saturated_with_saturation(...)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_isometry_actions.py::test_5_is_saturated_with_saturation_test_and_compute]
  - Caveat: upstream states availability when the coinvariant lattice is definite.
- [x] ``extend_to_ambient_space(::ZZLat, ...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_extend_to_ambient_space_identity_round_trip]
  - Caveat: upstream positions this as matrix-representation conversion from lattice-basis coordinates to ambient-space coordinates for collections of isometries.
- [x] ``restrict_to_lattice(::ZZLat, ...)`` [test: tests/julia_pytest/test_quadform_and_isom_static.py::test_restrict_to_lattice_inverse_of_extension_on_identity]
  - Caveat: upstream positions this as the inverse conversion, restricting ambient-space matrix representation back to lattice-basis coordinates.
### 2.18 Torsion quadratic modules with isometry (`TorQuadModuleWithIsom`)

- [ ] ``TorQuadModuleWithIsom``
- [ ] ``underlying_module(Tf)``
- [x] ``torsion_quadratic_module(Tf)`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_1_torsion_quadratic_module_construct_from_cover_and_relations]
- [ ] ``isometry(Tf)``
- [ ] ``order_of_isometry(Tf)``
  - Caveat: upstream states this is finite-order data cached after first computation; order is not precomputed on object construction.
- [ ] ``torsion_quadratic_module_with_isometry(T::TorQuadModule, [f::U]; check::Bool=true)``
  - Caveat: upstream stable docs document `U` as any of `AutomorphismGroupElem{TorQuadModule}`, `TorQuadModuleMap`, `FinGenAbGroupHom`, `ZZMatrix`, or `MatGroupElem{QQFieldElem, QQMatrix}`; omitting `f` uses the identity; `check=true` validates compatibility.
- [ ] ``torsion_quadratic_module_with_isometry(q::QQMatrix, [f::ZZMatrix]; check::Bool=true)``
  - Caveat: omitting `f` uses the identity; `check=true` validates matrix data as a torsion quadratic module with isometry.
- [ ] ``sub(Tf::TorQuadModuleWithIsom, gene::Vector{TorQuadModuleElem})``
  - Caveat: upstream requires the generated submodule to be stable under the fixed isometry; returns `(TorQuadModuleWithIsom, TorQuadModuleMap)`.
- [ ] ``primary_part(Tf::TorQuadModuleWithIsom, m::IntegerUnion)``
  - Caveat: upstream returns `(TorQuadModuleWithIsom, TorQuadModuleMap)` with induced isometry action.
- [ ] ``orthogonal_submodule(Tf::TorQuadModuleWithIsom, S::TorQuadModule; check::Bool=true)``
  - Caveat: upstream requires `S` to be stable under the fixed isometry (`check=true` enforces this); returns `(TorQuadModuleWithIsom, TorQuadModuleMap)`.
- [x] ``submodules(::TorQuadModuleWithIsom; quotype::Vector{Int}=Int[])`` [test: tests/julia_pytest/migrated_julia_doc/test_migrated_torquadmodule.py::test_24_submodules_enumerate_submodules]
  - Caveat: current upstream docs expose `quotype` filtering on this surface; accepted selector values are restricted to `0,1,2,3`.
- [ ] ``automorphism_group_with_inclusion(Tf::TorQuadModuleWithIsom)``
  - Caveat: upstream identifies this with automorphisms in `O(T)` commuting with the fixed isometry; returns `(AutomorphismGroup{TorQuadModule}, GAPGroupHomomorphism)`.
- [ ] ``automorphism_group(Tf::TorQuadModuleWithMap)``
  - Caveat: upstream method list typesets `TorQuadModuleWithMap` at this signature location; surrounding page context is `TorQuadModuleWithIsom` — treat as a documentation typesetting inconsistency.
- [ ] ``is_isomorphic_with_map(Tf, Sg)``
  - Caveat: upstream return contract is `(true, map)` on success and `(false, 0)` on failure.
- [ ] ``is_anti_isomorphic_with_map(Tf, Sg)``
  - Caveat: upstream return contract is `(true, anti_map)` on success and `(false, 0)` on failure.
### References

### Definiteness summary

## 3. Oscar.jl

### Integration points

- [ ] ``Oscar.ZZLat``
- [ ] ``Oscar.to_oscar(obj)``
- [ ] `Lattice databases`
- [ ] ``lll`, `short_vectors`, `close_vectors``
- [ ] `Discriminant groups`
- [ ] `Intersection forms`
- [ ] `Polyhedral integration`
### References

- [ ] `using Oscar`
## 4. Nemo.jl

### 4.1 LLL reduction

- [ ] ``lll(B::ZZMatrix, ctx::LLLContext)``
- [ ] ``lll_with_transform(B)``
- [ ] ``lll_gram(G)``
- [ ] ``lll_gram_with_transform(G)``
- [ ] `lll(B)`
### 4.2 Hermite Normal Form

- [ ] ``hnf(X)` / `AbstractAlgebra.hnf(X)``
- [ ] ``hnf_with_transform(X)``
### 4.3 Smith Normal Form

- [ ] ``snf(X)` / `AbstractAlgebra.snf(X)``
- [ ] ``snf_with_transform(X)``
### 4.4 Other

- [ ] `Echelon form`
- [ ] `Saturation`
### Interaction with Hecke

### References

## 5. LLLplus.jl

### 5.1 Reduction and search

- [ ] ``lll(B)``
- [ ] ``seysen(B)``
- [ ] ``hkz(B)``
- [ ] ``brun(B)``
- [ ] ``cvp(Q, R, y)``
  - Caveat: upstream examples use Euclidean/QR workflows on real matrices; no indefinite-form contract is documented.

### 5.2 Utility workflows

- [ ] ``subsetsum(...)``
- [ ] ``integerfeasibility(...)``
- [ ] ``rationalapprox(...)``

### Definiteness summary

- LLLplus algorithms are documented for Euclidean (positive-definite) workflows; indefinite arithmetic-form classification is out of scope.

### References

- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (section 5)
- `https://github.com/chrisvwx/LLLplus.jl`
- `https://chrisvwx.github.io/LLLplus.jl/dev/`

## 6. LatticeAlgorithms.jl

### 6.1 Core methods

- [ ] ``lll(M)``
- [ ] ``islllreduced(B)``
- [ ] ``kz(M)``
- [ ] ``closest_point(x, M)``
- [ ] ``closest_point_Dn(x)``
- [ ] ``Dn(n)``
- [ ] ``distance(M)``
- [ ] ``distances(M)``
  - Caveat: upstream positions these routines in GKP/CVP Euclidean settings; no indefinite-form classification API is documented.

### Definiteness summary

- LatticeAlgorithms.jl routines are used in positive-definite Euclidean decoding/reduction workflows.

### References

- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (section 6)
- `https://github.com/QuantumSavory/LatticeAlgorithms.jl`
- `https://github.com/amazon-science/lattice-algorithms`

## 7. Minor Julia Lattice Packages

### 7.1 LatticeBasisReduction.jl

- [ ] ``lll(B::AbstractMatrix{<:Integer}; delta=0.99, eta=0.51)``
- [ ] ``lll!(B::Matrix{BigFloat}; delta=0.99, eta=0.51)``
- [ ] ``islllreduced(B::AbstractMatrix{BigFloat}; delta=0.99, eta=0.51)``
  - Caveat: package exports `lll`; `lll!` and `islllreduced` are documented API surfaces but non-exported.

### 7.2 MinkowskiReduction.jl

- [ ] ``minkReduce(B::AbstractMatrix{<:Integer}; stable=true)``
- [ ] ``deviousMat(n::Int64, m::Int64)``
  - Caveat: upstream documents testing only for low ranks (`n <= 7`) and Euclidean workflows.

### References

- `docs/julia/oscar_jl/lattice/julia_lattice_methods_reference.md` (section 7)
- `https://github.com/MGBoom/LatticeBasisReduction.jl`
- `https://mgboom.github.io/LatticeBasisReduction.jl/stable/API/`
- `https://github.com/glwhart/MinkowskiReduction.jl`
- `https://github.com/glwhart/MinkowskiReduction.jl/blob/master/README.md`

Last updated: 2026-02-18
