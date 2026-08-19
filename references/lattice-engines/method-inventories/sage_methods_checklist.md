# Sage Method Checklist

Tracks Sage-relevant methods from the Sage docs set.

---

## Module: sage.modules.free_quadratic_module

- [ ] `FreeQuadraticModule(R, n, inner_product_matrix)`
  - Caveat: supports degenerate and asymmetric pairings; do not assume symmetric Gram semantics.
- [ ] `FreeModule(ZZ, n, inner_product_matrix=G)`
- [ ] `VectorSpace(QQ, n, inner_product_matrix=M)`
- [x] `inner_product_matrix()` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_inner_product_matrix_returns_ambient_form]
  - Caveat: ambient form matrix, not submodule Gram matrix.
- [x] `gram_matrix()` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_gram_matrix_on_submodule_basis]
  - Caveat: for submodules this is basis-dependent (`B*A*B^T`).
- [ ] `determinant()`
- [ ] `discriminant()`
  - Caveat: discriminant convention differs from `IntegralLattice.discriminant()`.
- [x] `ambient_module()` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_ambient_module_is_self_for_ambient]
- [x] `ambient_vector_space()` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_ambient_vector_space_keeps_dimension]
- [x] `span(gens, check=True, already_echelonized=False)` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_span_and_span_of_basis_agree_on_rank]
- [x] `span_of_basis(basis, check=True, already_echelonized=False)` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_span_of_basis_rank_two_on_independent_basis]

## Module: sage.modules.free_module_integer (IntegerLattice)

- [ ] `IntegerLattice(basis, lll_reduce=True)`
  - Caveat: Euclidean embedding model (`Gram = B*B^T`), not arbitrary-form lattice constructor.
- [ ] `LLL()`
- [ ] `BKZ(*args, **kwds)`
- [x] `HKZ()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_hkz_preserves_rank]
- [x] `shortest_vector()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_shortest_vector_has_expected_norm_rank_one]
- [x] `closest_vector(target)` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_closest_vector_exact_rank_one]
- [x] `approximate_closest_vector(target)` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_approximate_closest_vector_returns_lattice_vector]
  - Caveat: heuristic, not exact CVP guarantee.
- [x] `babai(target, *args, **kwds)` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_babai_returns_lattice_vector_rank_one]
- [x] `volume()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_volume_square_matches_discriminant]
- [ ] `discriminant()`
- [x] `is_unimodular()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_is_unimodular_false_for_scaled_basis]
- [x] `reduced_basis` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_reduced_basis_preserves_discriminant_after_lll]
- [x] `update_reduced_basis()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_update_reduced_basis_sets_attribute]
- [x] `voronoi_cell()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_voronoi_cell_has_vertices]
- [x] `voronoi_relevant_vectors()` [test: tests/sage_doc/test_integerlattice_static.py::test_integerlattice_voronoi_relevant_vectors_nonempty]

## Module: sage.modules.free_quadratic_module_integer_symmetric (IntegralLattice)

- [ ] `IntegralLattice(data, basis=None)`
  - Caveat: requires non-degenerate symmetric form.
- [ ] `IntegralLatticeDirectSum(Lattices, return_embeddings=False)`
- [ ] `IntegralLatticeGluing(Lattices, glue, return_embeddings=False)`
- [x] `gram_matrix()` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_gram_matrix_on_submodule_basis]
- [ ] `basis_matrix()`
- [x] `inner_product_matrix()` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_inner_product_matrix_returns_ambient_form]
- [ ] `rank()`
- [x] `degree()` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_degree_matches_rank_for_nondegenerate_example]
- [ ] `determinant()`
- [ ] `signature()`
- [ ] `signature_pair()`
- [ ] `is_even()`
- [ ] `is_positive_definite()`
- [ ] `is_negative_definite()`
- [ ] `is_definite()`
- [x] `dual_lattice()` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_dual_lattice_contains_scaled_basis]
- [x] `discriminant_group(s=0)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_discriminant_group_has_expected_order_rank_one]
- [ ] `direct_sum(M)`
- [x] `sublattice(basis)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_sublattice_rank_from_single_generator]
- [x] `overlattice(gens)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_overlattice_contains_original_rank]
- [x] `maximal_overlattice(p=None)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_maximal_overlattice_evenness_constraint_at_two]
- [x] `orthogonal_complement(M)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_orthogonal_complement_dimension]
- [ ] `is_primitive(M)`
- [x] `tensor_product(other, discard_basis=False)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_tensor_product_rank_multiplies]
- [ ] `twist(s, discard_basis=False)`
- [ ] `LLL()`
- [ ] `lll()`
  - Caveat: `IntegralLattice.lll()/LLL()` returns a new lattice object; `IntegerLattice.LLL()` returns a reduced basis matrix and updates `reduced_basis` on the object.
- [x] `short_vectors(n, **kwargs)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_short_vectors_contains_minimal_vector]
- [x] `enumerate_short_vectors()` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_enumerate_short_vectors_iterator_nonempty]
  - Caveat: returned vectors are not necessarily ordered strictly by length.
- [x] `enumerate_close_vectors(target)` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_enumerate_close_vectors_returns_candidate]
  - Caveat: returned vectors are not necessarily ordered strictly by distance to the target.
- [x] `minimum()` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_minimum_extremes_by_signature]
- [x] `maximum()` [test: tests/sage_doc/test_integrallattice_static.py::test_integrallattice_maximum_extremes_by_signature]
- [ ] `orthogonal_group(gens=None, is_finite=None)`
  - Caveat: docs state generator computation is currently only for definite lattices; indefinite example raises `NotImplementedError`.
- [ ] `genus()`
- [ ] `quadratic_form()`
- [ ] `local_modification(M, G, p, check=True)`

## Module: sage.quadratic_forms.quadratic_form (QuadraticForm)

- [ ] `QuadraticForm(R, n, entries)`
- [ ] `QuadraticForm(p)`
- [ ] `QuadraticForm(R, M)`
- [ ] `QuadraticForm(M)`
- [ ] `DiagonalQuadraticForm(R, diag)`
- [ ] `quadratic_form_from_invariants(F, rk, det, P, sminus)`
- [ ] `QuadraticForm.from_polynomial(poly)`
- [ ] `dim()`
- [ ] `base_ring()`
- [ ] `coefficients()`
- [ ] `det()`
- [x] `Gram_det()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_Gram_det_scales_det_by_power_of_two]
  - Caveat: do not conflate Hessian determinant and Gram determinant.
- [ ] `matrix()`
- [x] `Hessian_matrix()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_Hessian_matrix_matches_matrix_method]
- [x] `Gram_matrix()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_Gram_matrix_half_of_matrix]
  - Caveat: Hessian and Gram normalization differ.
- [x] `Gram_matrix_rational()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_Gram_matrix_rational_has_expected_entries]
- [x] `has_integral_Gram_matrix()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_has_integral_gram_matrix_true_for_integer_form]
- [ ] `polynomial(names='x')`
- [x] `bilinear_map(v, w)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_bilinear_map_polarization_identity]
- [ ] `__call__(v)`
- [x] `hasse_invariant(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_hasse_invariant_comparison_with_omeara]
- [x] `hasse_invariant__OMeara(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_hasse_invariant_omeara_sign_value]
- [ ] `signature()`
- [x] `signature_vector()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_signature_vector_counts_eigenvalue_signs]
- [x] `anisotropic_primes()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_anisotropic_primes_contains_three]
- [x] `is_isotropic(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_isotropic_true_at_two]
- [x] `is_anisotropic(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_anisotropic_and_is_isotropic_complement_at_prime]
- [x] `is_hyperbolic(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_hyperbolic_false_at_two_for_example]
- [x] `rational_diagonal_form()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_rational_diagonal_form_preserves_rank]
- [ ] `is_positive_definite()`
- [ ] `is_negative_definite()`
- [ ] `is_definite()`
- [ ] `is_indefinite()`
- [x] `compute_definiteness()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_compute_definiteness_sets_consistent_string]
- [x] `compute_definiteness_string_by_determinants()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_compute_definiteness_string_expected_value]
- [ ] `level()`
- [x] `level_ideal()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_level_ideal_matches_level_generator]
- [ ] `is_primitive()`
- [ ] `primitive()`
- [x] `adjoint_primitive()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_adjoint_primitive_is_primitive]
- [ ] `change_ring(R)`
- [ ] `lll()`
- [x] `minkowski_reduction()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_minkowski_reduction_preserves_discriminant]
- [x] `minkowski_reduction_for_4vars__SP()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_minkowski_reduction_for_4vars_sp_preserves_discriminant]
- [x] `reduced_binary_form()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_reduced_binary_form_preserves_discriminant]
- [x] `reduced_binary_form1()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_reduced_binary_form1_on_binary_input_preserves_discriminant]
- [x] `reduced_ternary_form__Dickson()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_reduced_ternary_form_Dickson_notimplemented_here]
- [x] `theta_series(var, prec)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_theta_series_leading_coefficient_one]
  - Caveat: implemented via PARI `qfrep` (`theta_by_pari`), and `qfrep` is defined for positive-definite forms.
- [x] `theta_by_cholesky(q_prec)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_theta_by_cholesky_starts_with_one_constant_term]
- [x] `theta_by_pari(prec)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_theta_by_pari_starts_with_one_constant_term]
- [x] `theta_series_degree_2(prec)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_theta_series_degree_2_has_constant_term_one]
- [x] `short_vector_list_up_to_length(n)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_short_vector_list_up_to_length_zero_contains_none]
  - Caveat: docs show non-positive-definite input raises `ValueError: Quadratic form must be positive definite in order to enumerate short vectors`.
- [x] `short_primitive_vector_list_up_to_length(n)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_short_primitive_vector_list_subset_of_short_vectors]
- [x] `automorphism_group()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_automorphism_group_order_matches_automorphisms_list]
- [ ] `automorphisms()`
- [ ] `number_of_automorphisms()`
- [x] `is_globally_equivalent_to(other)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_globally_equivalent_to_reflexive_and_detects_change]
- [x] `is_locally_equivalent_to(other, p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_locally_equivalent_to_reflexive_and_detects_change]
- [x] `is_rationally_isometric(other)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_rationally_isometric_detects_discriminant_change]
- [x] `global_genus_symbol()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_global_genus_symbol_determinant_matches]
- [x] `local_genus_symbol(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_genus_symbol_returns_symbol]
- [x] `local_normal_form(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_normal_form_preserves_discriminant_at_two]
  - Caveat: upstream warning states this currently only works for quadratic forms defined over `ZZ`.
- [x] `jordan_blocks_by_scale_and_unimodular(p, safe_flag=True)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_jordan_blocks_by_scale_and_unimodular_nonempty]
  - Caveat: upstream notes Jordan decomposition into smaller blocks is not unique.
- [x] `jordan_blocks_in_unimodular_list_by_scale_power(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_jordan_blocks_unimodular_list_nonempty]
  - Caveat: upstream states this is defined for integer-valued forms; for `p = 2`, indexing works correctly only when the form has an integer Gram matrix.
- [x] `has_equivalent_Jordan_decomposition_at_prime(other, p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_has_equivalent_jordan_decomposition_at_prime_detects_change]
- [x] `genera(sig_pair, det, ...)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_genera_nonempty_for_signature_and_det]
- [x] `mass__by_Siegel_densities()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_mass_by_siegel_densities_positive]
- [x] `conway_mass()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_conway_mass_positive]
- [x] `conway_standard_mass()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_conway_standard_mass_positive]
- [x] `siegel_product()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_siegel_product_raises_for_nonsquare_root_rationality]
- [x] `local_density(p, m)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_density_agrees_with_congruence_at_sample]
  - Caveat: upstream notes this routine internally puts the form in local normal form (a required precondition for density computations).
- [x] `local_primitive_density(p, m)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_primitive_density_agrees_with_congruence]
  - Caveat: upstream notes this routine internally puts the form in local normal form (a required precondition for primitive density computations).
- [x] `local_density_congruence(p, m, Zvec=None, NZvec=None)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_density_congruence_matches_local_density]
  - Caveat: upstream assumes the form is block diagonal and `p`-integral; `Zvec` and `NZvec` are non-repeating index lists in `range(self.dim())` (or `None`).
- [x] `local_primitive_density_congruence(p, m, Zvec=None, NZvec=None)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_primitive_density_congruence_zero_at_sample]
  - Caveat: upstream assumes the form is block diagonal and `p`-integral; `Zvec` and `NZvec` are non-repeating index lists in `range(self.dim())` (or `None`). Upstream also notes this routine is included for consistency and not used internally.
- [x] `local_good_density_congruence(p, m, Zvec=None, NZvec=None)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_good_density_even_odd_helpers_on_sample]
  - Caveat: upstream assumes the form is block diagonal and `p`-integral; `Zvec` and `NZvec` are non-repeating index lists in `range(self.dim())` (or `None`).
- [x] `local_bad_density_congruence(p, m, Zvec=None, NZvec=None)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_bad_density_equals_sum_of_I_and_II]
  - Caveat: upstream assumes the form is block diagonal and `p`-integral; `Zvec` and `NZvec` are non-repeating index lists in `range(self.dim())` (or `None`).
- [x] `local_badI_density_congruence(p, m, Zvec=None, NZvec=None)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_badI_density_congruence_zero_at_sample]
  - Caveat: upstream assumes the form is block diagonal and `p`-integral; `Zvec` and `NZvec` are non-repeating index lists in `range(self.dim())` (or `None`).
- [x] `local_badII_density_congruence(p, m, Zvec=None, NZvec=None)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_badII_density_congruence_zero_at_sample]
  - Caveat: upstream assumes the form is block diagonal and `p`-integral; `Zvec` and `NZvec` are non-repeating index lists in `range(self.dim())` (or `None`).
- [x] `local_representation_conditions(...)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_representation_conditions_mentions_exception_prime]
- [x] `is_locally_universal_at_prime(p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_locally_universal_at_prime_true_sample]
- [x] `is_locally_universal_at_all_primes()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_universality_methods_detect_nonuniversal_case]
- [x] `is_locally_universal_at_all_places()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_locally_universal_at_all_places_false_example]
- [x] `is_locally_represented_number(m)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_local_representation_methods_agree_on_sample]
- [x] `is_locally_represented_number_at_place(m, p)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_is_locally_represented_number_at_place_true_sample]
- [x] `solve(n)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_solve_over_qq_returns_exact_value]
- [ ] `find_p_neighbor_from_vec(p, v)`
- [x] `neighbor_iteration(p, ...)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_neighbor_iteration_returns_seed_under_class_limit]
- [ ] `disc()`
- [ ] `content()`
- [ ] `adjoint()`
- [x] `antiadjoint()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_antiadjoint_inverts_adjoint]
- [ ] `reciprocal()`
- [ ] `omega()`
- [ ] `delta()`
- [ ] `xi()`
- [ ] `xi_rec()`
- [x] `clifford_invariant()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_clifford_invariant_is_hilbert_symbol_value]
- [x] `clifford_conductor()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_clifford_conductor_positive]
- [x] `hasse_conductor()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_hasse_conductor_positive]
- [x] `representation_number_list(B)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_representation_number_list_constant_term_one]
- [x] `representation_vector_list(B)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_representation_vector_list_contains_zero_vector_for_zero]
  - Caveat: docs state this only works for positive-definite quadratic forms.
- [x] `swap_variables(i, j)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_swap_variables_preserves_discriminant]
- [x] `multiply_variable(i, s)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_multiply_variable_by_zero_forces_zero_coefficient]
- [x] `divide_variable(i, s)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_divide_variable_by_one_is_identity]
- [x] `add_symmetric(i, j, s)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_add_symmetric_changes_selected_coefficients]
- [x] `extract_variables(v)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_extract_variables_dimension_matches_selection]
- [ ] `scale_by_factor(s)`

## Module: sage.quadratic_forms.genera.genus

- [ ] `Genus(A, factored_determinant=None)`
- [ ] `LocalGenusSymbol(A, p)`
- [x] `genera(sig_pair, determinant, max_scale=None, even=False)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_genera_nonempty_for_signature_and_det]
- [ ] `is_GlobalGenus(G)`
- [ ] `p_adic_symbol(A, p, val)`
- [ ] `two_adic_symbol(A, val)`
- [ ] `is_2_adic_genus(symbol)`
- [x] `signature_pair_of_matrix(A)` [test: tests/sage_doc/test_genus_static.py::test_genus_signature_pair_of_matrix_alias]
- [ ] `is_even_matrix(A)`
- [ ] `canonical_2_adic_reduction(symbol)`
- [ ] `canonical_2_adic_compartments(symbol)`
- [ ] `canonical_2_adic_trains(symbol)`
- [ ] `basis_complement(B)`
- [ ] `split_odd(A)`
- [ ] `trace_diag_mod_8(A)`
- [ ] `prime()`
- [ ] `is_even()`
- [ ] `symbol_tuple_list()`
- [ ] `canonical_symbol()`
- [ ] `number_of_blocks()`
- [ ] `determinant()`
- [ ] `det()`
- [x] `dimension()` [test: tests/sage_doc/test_genus_static.py::test_genus_dimension_matches_representative_size]
- [ ] `dim()`
- [ ] `rank()`
- [ ] `excess()`
- [x] `scale()` [test: tests/sage_doc/test_genus_static.py::test_genus_scale_and_norm_are_positive]
- [ ] `norm()`
- [ ] `level()`
- [ ] `direct_sum(other)`
- [x] `gram_matrix(check=True)` [test: tests/sage_doc/test_freequadraticmodule_static.py::test_freequadraticmodule_gram_matrix_on_submodule_basis]
- [x] `mass()` [test: tests/sage_doc/test_genus_static.py::test_genus_mass_positive_rational]
- [ ] `automorphous_numbers()`
- [ ] `trains()`
- [ ] `compartments()`
- [ ] `signature_pair()`
- [ ] `signature()`
- [x] `local_symbols()` [test: tests/sage_doc/test_genus_static.py::test_genus_local_symbols_nonempty_for_nonsingular_example]
- [x] `local_symbol(p)` [test: tests/sage_doc/test_genus_static.py::test_genus_local_symbol_returns_prime_data]
- [x] `discriminant_form()` [test: tests/sage_doc/test_genus_static.py::test_genus_discriminant_form_cardinality_matches_abs_determinant]
- [x] `rational_representative()` [test: tests/sage_doc/test_genus_static.py::test_genus_rational_representative_shape]
- [x] `representative()` [test: tests/sage_doc/test_genus_static.py::test_genus_representative_preserves_dimension]
- [x] `representatives(backend=None, algorithm=None)` [test: tests/sage_doc/test_genus_static.py::test_genus_representatives_returns_nonempty_same_rank_matrices]
- [x] `spinor_generators(proper)` [test: tests/sage_doc/test_genus_static.py::test_genus_spinor_generators_nonempty_for_proper_and_improper]
- [x] `spinor_generators()` [test: tests/sage_doc/test_genus_static.py::test_genus_spinor_generators_nonempty_for_proper_and_improper]

## Module: sage.modules.torsion_quadratic_module

- [ ] `TorsionQuadraticModule(V, W, gens=None, modulus=None, modulus_qf=None, check=True)`
- [ ] `TorsionQuadraticForm(q)`
- [ ] `gens()`
- [x] `gram_matrix_bilinear()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_gram_matrix_bilinear_is_square]
- [x] `gram_matrix_quadratic()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_gram_matrix_quadratic_has_same_shape_as_bilinear]
- [x] `value_module()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_value_modules_are_defined]
- [x] `value_module_qf()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_value_module_qf_defined]
- [x] `order()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_order_equals_cardinality_for_finite_module]
- [x] `invariants()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_invariants_rank_one_even_lattice]
- [ ] `direct_sum(other)`
- [ ] `twist(s)`
- [ ] `submodule(gens)`
- [x] `submodule_with_gens(gens)` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_submodule_with_gens_cardinality_bound]
- [x] `orthogonal_submodule_to(S)` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_orthogonal_submodule_to_self_is_nonempty]
  - Caveat: method name is `orthogonal_submodule_to`, not `orthogonal_submodule`.
- [x] `primary_part(m)` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_primary_part_of_two_group_is_itself]
- [x] `all_submodules()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_all_submodules_nonempty]
- [ ] `quotient(W)`
- [x] `normal_form(partial=False)` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_normal_form_returns_module]
- [x] `brown_invariant()` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_brown_invariant_is_defined_mod_8]
- [ ] `genus(signature_pair)`
- [x] `is_genus(signature_pair, even=True)` [test: tests/sage_doc/test_torsionquadraticmodule_static.py::test_tqm_is_genus_true_exactly_for_valid_signature_example]
  - Caveat: upstream `is_genus` docs include TODO `implement the same for odd lattices`; treat `even=False` as incomplete even though odd-lattice examples exist for `genus(signature_pair)`.
- [ ] `orthogonal_group(gens=None, check=False)`

## Module: sage.quadratic_forms.binary_qf

- [ ] `BinaryQF(a, b=None, c=None)`
- [ ] `discriminant()`
  - Caveat: distinct from `determinant()`/`det()` (Gram determinant normalization differs).
- [ ] `determinant()`
- [ ] `det()`
- [x] `is_equivalent(other)` [test: tests/sage_doc/test_binaryqf_static.py::test_binaryqf_is_equivalent_reflexive]
- [ ] `is_indefinite()`
- [x] `is_reduced()` [test: tests/sage_doc/test_binaryqf_static.py::test_binaryqf_is_reduced_on_simple_posdef_example]
- [x] `reduced_form()` [test: tests/sage_doc/test_binaryqf_static.py::test_binaryqf_reduced_form_preserves_discriminant]
- [x] `cycle()` [test: tests/sage_doc/test_binaryqf_static.py::test_binaryqf_cycle_contains_equivalent_forms]
- [x] `small_prime_value()` [test: tests/sage_doc/test_binaryqf_static.py::test_binaryqf_small_prime_value_is_represented]

## Module: sage.quadratic_forms.ternary_qf

- [ ] `TernaryQF(coeffs)`
- [ ] `disc()`
- [ ] `content()`
- [ ] `adjoint()`
- [ ] `omega()`
- [ ] `delta()`
- [x] `level__Tornaria()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_level_Tornaria_is_positive]
- [ ] `is_definite()`
- [x] `is_reduced()` [test: tests/sage_doc/test_binaryqf_static.py::test_binaryqf_is_reduced_on_simple_posdef_example]
- [x] `reduced_ternary_form__Dickson()` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_reduced_ternary_form_Dickson_notimplemented_here]
- [ ] `automorphisms()`
- [ ] `number_of_automorphisms()`
- [x] `representation_number_list(B)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_representation_number_list_constant_term_one]
- [x] `representation_vector_list(B)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_representation_vector_list_contains_zero_vector_for_zero]
- [x] `theta_series(var, prec)` [test: tests/sage_doc/test_quadraticform_static.py::test_quadraticform_theta_series_leading_coefficient_one]

## Module: sage.combinat.root_system

- [ ] `RootSystem(type)`
- [x] `root_lattice()` [test: tests/sage_doc/test_rootsystem_static.py::test_rootsystem_cartan_type_rank_matches_lattice_dimension]
  - Caveat: combinatorial root lattice API, not `IntegralLattice` API.
- [ ] `weight_lattice()`
- [ ] `root_space()`
- [ ] `weight_space()`
- [ ] `ambient_lattice()`
- [ ] `ambient_space()`
- [ ] `simple_roots()`
- [ ] `simple_coroots()`
- [x] `positive_roots()` [test: tests/sage_doc/test_rootsystem_static.py::test_rootsystem_positive_roots_count_matches_type_a2]
- [x] `highest_root()` [test: tests/sage_doc/test_rootsystem_static.py::test_rootsystem_highest_root_is_positive]
- [ ] `fundamental_weights()`
- [ ] `rho()`
- [x] `scalar(...)` [test: tests/sage_doc/test_rootsystem_static.py::test_rootsystem_simple_root_scalar_recovers_cartan_entry]
  - Caveat: Cartan pairing semantics; do not treat as Euclidean inner product.
- [ ] `inner_product(...)`

## Module: sage.rings.number_field / ideals (Bridge Methods)

- [x] `integral_basis()` [test: tests/sage_doc/test_numberfield_bridge_static.py::test_numberfield_integral_basis_has_field_degree_length]
- [ ] `basis()`
- [x] `free_module()` [test: tests/sage_doc/test_numberfield_bridge_static.py::test_numberfield_ideal_free_module_has_expected_rank]
  - Caveat: returns bare module; no stored metric/Gram.
- [x] `trace()` [test: tests/sage_doc/test_numberfield_bridge_static.py::test_numberfield_element_trace_matches_conjugate_sum]
- [x] `minkowski_embedding(prec=...)` [test: tests/sage_doc/test_numberfield_bridge_static.py::test_numberfield_minkowski_embedding_matrix_has_degree_rows]
  - Caveat: floating approximation; not canonical exact Gram source.
- [ ] `discriminant()`
- [ ] `signature()`

## Archived out-of-scope toric/polyhedral surfaces

- Sage toric/fan/polytope checklist sections were moved out of active bilinear-form lattice scope and archived at:
  `docs/archive/scope_violations/sage_methods_checklist_toric_sections_2026-02-18.md`.

Last updated: 2026-02-18
