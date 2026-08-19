from __future__ import annotations

import logging
from functools import reduce

from sage.all import ZZ, IntegralLattice, identity_matrix, matrix
from src.backends.isometry_backend import LatticeIsometryBackend
from src.lattices.lattices import DiscriminantGroup, FreeBilinearModule, Lattice


class TestLatticeSemantics:
    NATIVE_LATTICE = type(IntegralLattice("U"))
    PICARD_NEGATIVE_RANK = IntegralLattice("E8").rank() + IntegralLattice("U").rank()
    HYPERBOLIC_RANK = IntegralLattice("U").rank()
    README_EQUIVALENCE_LEFT = (
        (0, 1, 0, 0),
        (1, 0, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, -1),
    )
    README_EQUIVALENCE_RIGHT = (
        (2, 1, 0, 0),
        (1, 0, 0, 0),
        (0, 0, -1, 0),
        (0, 0, 0, -1),
    )
    UPSTREAM_U_I3_LEFT = (
        (0, 1, 0, 0, 0),
        (1, 0, 0, 0, 0),
        (0, 0, -1, 0, 0),
        (0, 0, 0, -1, 0),
        (0, 0, 0, 0, -1),
    )
    UPSTREAM_U_I3_RIGHT = (
        (-3729, 464, -792, -930, 805),
        (464, -58, 99, 116, -99),
        (-792, 99, -169, -198, 169),
        (-930, 116, -198, -232, 201),
        (805, -99, 169, 201, -170),
    )

    @classmethod
    def _native_scaled_hyperbolic_plane(cls, scale):
        native = IntegralLattice(scale * IntegralLattice("U").inner_product_matrix())
        assert native.base_ring() is ZZ
        return native

    @classmethod
    def _wrapped_scaled_hyperbolic_plane(cls, scale):
        wrapped = Lattice.from_gram(cls._native_scaled_hyperbolic_plane(scale).gram_matrix())
        assert wrapped.base_ring() is ZZ
        return wrapped

    @classmethod
    def _wrapped_basis_changed_scaled_hyperbolic_plane(cls, scale):
        native = cls._native_scaled_hyperbolic_plane(scale)
        first_basis_vector, second_basis_vector = tuple(native.basis())
        changed_lattice = cls.NATIVE_LATTICE(
            native.ambient_module(),
            native.submodule((first_basis_vector, first_basis_vector + second_basis_vector)).basis_matrix(),
            native.inner_product_matrix(),
        )
        assert changed_lattice.base_ring() is ZZ
        return Lattice.from_gram(changed_lattice.gram_matrix())

    @classmethod
    def _native_split_scaled_hyperbolic_plane(cls, scale):
        native = cls.NATIVE_LATTICE.direct_sum(
            Lattice.Z().twist(scale),
            Lattice.Z().twist(-scale),
        )
        assert native.base_ring() is ZZ
        return native

    @classmethod
    def _wrapped_split_scaled_hyperbolic_plane(cls, scale):
        wrapped = Lattice.from_gram(cls._native_split_scaled_hyperbolic_plane(scale).gram_matrix())
        assert wrapped.base_ring() is ZZ
        return wrapped

    @classmethod
    def _wrapped_lattice_from_gram_rows(cls, rows):
        rank = len(rows)
        native = cls.NATIVE_LATTICE(
            ZZ**rank,
            identity_matrix(ZZ, rank),
            matrix(ZZ, rows),
        )
        assert native.base_ring() is ZZ
        return Lattice.from_gram(native.gram_matrix())

    @classmethod
    def _native_t_en(cls):
        native = reduce(
            cls.NATIVE_LATTICE.direct_sum,
            (
                IntegralLattice("U"),
                cls._native_scaled_hyperbolic_plane(2),
                IntegralLattice(-2 * IntegralLattice("E8").inner_product_matrix()),
            ),
        )
        assert native.base_ring() is ZZ
        return native

    @classmethod
    def _native_k3(cls):
        native = reduce(
            cls.NATIVE_LATTICE.direct_sum,
            (
                IntegralLattice("U"),
                IntegralLattice("U"),
                IntegralLattice(-IntegralLattice("E8").inner_product_matrix()),
                IntegralLattice(-IntegralLattice("E8").inner_product_matrix()),
            ),
            IntegralLattice("U"),
        )
        assert native.base_ring() is ZZ
        return native

    def test_free_module_and_lattice_element_semantics_are_exact(self) -> None:
        wrapped_module = FreeBilinearModule(ZZ, IntegralLattice("U").inner_product_matrix())
        module_generator = next(iter(wrapped_module.gens()))
        wrapped_lattice = Lattice.U()
        basis_vector = next(iter(wrapped_lattice.basis()))
        assert module_generator.is_isotropic()
        assert basis_vector.divisibility().is_one()
        assert basis_vector.is_primitive()
        assert basis_vector.discriminant_class().is_zero()

    def test_k3_matches_the_literature_model_and_unimodularity(self) -> None:
        wrapped_lattice = Lattice.k3()
        expected = Lattice.U() ** 3 + Lattice.E(8).twist(-1) ** 2
        rank_invariant, a_invariant, delta_invariant = wrapped_lattice.nikulin_invariants()
        assert wrapped_lattice.is_even()
        assert wrapped_lattice.discriminant_group().cardinality().is_one()
        assert wrapped_lattice.discriminant_group().is_p_elementary(2)
        assert wrapped_lattice.is_isometric_to(expected)
        assert not rank_invariant.is_zero()
        assert a_invariant.is_zero()
        assert delta_invariant.is_zero()

    def test_discriminant_group_exposes_two_primary_nikulin_data_on_u_two(self) -> None:
        wrapped_lattice = self._wrapped_scaled_hyperbolic_plane(2)
        wrapped_group = wrapped_lattice.discriminant_group()
        rank_invariant, a_invariant, delta_invariant = wrapped_lattice.nikulin_invariants()
        assert wrapped_group.is_p_elementary(2)
        assert not wrapped_group.is_p_elementary(3)
        assert wrapped_group.p_rank(3).is_zero()
        assert not wrapped_group.p_rank(2).is_zero()
        assert not wrapped_group.nikulin_a().is_zero()
        assert wrapped_group.coparity().is_zero()
        assert wrapped_group.delta().is_zero()
        assert wrapped_lattice.is_isometric_to(self._wrapped_basis_changed_scaled_hyperbolic_plane(2))
        assert not rank_invariant.is_zero()
        assert not a_invariant.is_zero()
        assert delta_invariant.is_zero()

    def test_t_en_sits_in_the_nikulin_domain(self) -> None:
        wrapped_lattice = Lattice.U() + Lattice.U().twist(2) + Lattice.E(8).twist(2)
        rank_invariant, a_invariant, delta_invariant = wrapped_lattice.nikulin_invariants()
        assert wrapped_lattice.is_even()
        assert wrapped_lattice.discriminant_group().is_p_elementary(2)
        assert wrapped_lattice.is_isometric_to(Lattice.U() + Lattice.U().twist(2) + Lattice.E(8).twist(2))
        assert not rank_invariant.is_zero()
        assert not a_invariant.is_zero()
        assert delta_invariant.is_zero()

    def test_rank_mismatch_precludes_isometry(self) -> None:
        assert not Lattice.Z().is_isometric_to(Lattice.U())

    def test_discriminant_group_mismatch_precludes_isometry(self) -> None:
        """
        <2> + <2> and <1> + <4> share rank 2, signature (2, 0), and
        determinant 4, but their discriminant groups differ:
        (Z/2Z)^2 versus Z/4Z.
        """
        from sage.all import diagonal_matrix

        two_two = Lattice.from_gram(diagonal_matrix(ZZ, [2, 2]))
        one_four = Lattice.from_gram(diagonal_matrix(ZZ, [1, 4]))
        assert two_two.rank() == one_four.rank()
        assert two_two.signature_pair() == one_four.signature_pair()
        assert two_two.determinant() == one_four.determinant()
        assert not two_two.discriminant_group().isomorphic_as_groups(one_four.discriminant_group())
        assert not two_two.is_isometric_to(one_four)

    def test_signature_and_nikulin_domain_mismatches_preclude_isometry(self) -> None:
        positive_line = Lattice.Z()
        negative_line = Lattice.A(1)
        nikulin_lattice = self._wrapped_scaled_hyperbolic_plane(2)
        non_nikulin_lattice = self._wrapped_scaled_hyperbolic_plane(3)
        assert not positive_line.is_isometric_to(negative_line)
        assert not nikulin_lattice.is_isometric_to(non_nikulin_lattice)

    def test_isometry_prechecks_rule_out_nonisometric_indefinite_pair(self) -> None:
        left = self._wrapped_scaled_hyperbolic_plane(2)
        right = self._wrapped_split_scaled_hyperbolic_plane(2)
        assert left.rank() == right.rank()
        assert left.signature_pair() == right.signature_pair()
        assert left.determinant() == right.determinant()
        assert left.discriminant_group().isomorphic_as_groups(right.discriminant_group())
        assert not left.discriminant_group().is_isometric_to(right.discriminant_group())
        assert left.is_rationally_isometric_to(right)
        assert not left.is_locally_isometric_to(right, 2)
        assert left.is_locally_isometric_to(right, 3)
        assert left.is_locally_isometric_to(right, 5)
        assert not left.is_in_same_genus_as(right)
        assert not left.is_isometric_to(right)

    def test_nikulin_invariants_warn_but_remain_defined_on_u_three(self, caplog) -> None:
        wrapped_lattice = self._wrapped_scaled_hyperbolic_plane(3)
        with caplog.at_level(logging.WARNING, logger="coble_geometry_foundation"):
            invariants = wrapped_lattice.nikulin_invariants()
        rank_invariant, a_invariant, delta_invariant = invariants
        assert caplog.records
        assert wrapped_lattice.discriminant_group().is_p_elementary(3)
        assert not wrapped_lattice.discriminant_group().is_p_elementary(2)
        assert not rank_invariant.is_zero()
        assert a_invariant.is_zero()
        assert delta_invariant.is_one()

    def test_isometry_uses_the_known_nikulin_route_for_u_two(self) -> None:
        """
        TODO: expose the roughly 75 Nikulin lattices as named constructors and run
        this theorem-backed isometry path across the full literature family.
        """
        left = self._wrapped_scaled_hyperbolic_plane(2)
        right = self._wrapped_basis_changed_scaled_hyperbolic_plane(2)
        left_rank, left_a, left_delta = left.nikulin_invariants()
        right_rank, right_a, right_delta = right.nikulin_invariants()
        assert left.discriminant_group().is_p_elementary(2)
        assert right.discriminant_group().is_p_elementary(2)
        assert not left_rank.is_zero()
        assert not left_a.is_zero()
        assert left_delta.is_zero()
        assert not right_rank.is_zero()
        assert not right_a.is_zero()
        assert right_delta.is_zero()
        assert left.is_isometric_to(right)

    def test_general_indefinite_basis_change_is_detected_as_an_isometry(self) -> None:
        left = self._wrapped_scaled_hyperbolic_plane(3)
        right = self._wrapped_basis_changed_scaled_hyperbolic_plane(3)
        assert left.discriminant_group().is_p_elementary(3)
        assert not left.discriminant_group().is_p_elementary(2)
        assert left.discriminant_group().isomorphic_as_groups(right.discriminant_group())
        assert left.discriminant_group().is_isometric_to(right.discriminant_group())
        assert left.is_rationally_isometric_to(right)
        assert left.is_locally_isometric_to(right, 2)
        assert left.is_locally_isometric_to(right, 3)
        assert left.is_locally_isometric_to(right, 5)
        assert left.is_in_same_genus_as(right)
        assert left.is_isometric_to(right)

    def test_upstream_readme_equivalence_fixture_is_supported(self) -> None:
        """
        Source: `Indefinite.jl` README and the example in `src/Functions.jl`.
        """
        left = self._wrapped_lattice_from_gram_rows(self.README_EQUIVALENCE_LEFT)
        right = self._wrapped_lattice_from_gram_rows(self.README_EQUIVALENCE_RIGHT)
        assert left.rank() == right.rank()
        assert left.signature_pair() == right.signature_pair()
        assert left.is_in_same_genus_as(right)
        assert left.is_isometric_to(right)

    def test_upstream_u_i3_fixture_is_supported(self) -> None:
        """
        Source: `Indefinite.jl` fixtures `TestLor/U_I3_mat1` and `U_I3_mat2`.
        """
        left = self._wrapped_lattice_from_gram_rows(self.UPSTREAM_U_I3_LEFT)
        right = self._wrapped_lattice_from_gram_rows(self.UPSTREAM_U_I3_RIGHT)
        assert left.rank() == right.rank()
        assert left.signature_pair() == right.signature_pair()
        assert left.discriminant_group().isomorphic_as_groups(right.discriminant_group())
        assert left.discriminant_group().is_isometric_to(right.discriminant_group())
        assert left.is_rationally_isometric_to(right)
        assert left.is_in_same_genus_as(right)
        assert left.is_isometric_to(right)

    def test_milnor_husemoller_same_genus_not_isometric(self) -> None:
        """
        Milnor-Husemoller, §II Example 3 p.44.

        L1 = <5> ⊕ <11> and L2 = <1> ⊕ <55> are p-adically isometric for
        every finite prime p (same genus), but not isometric over Z because
        5x² + 11y² = 1 has no integer solutions.
        """
        L1 = Lattice.Z().twist(1) + Lattice.Z().twist(55)
        L2 = Lattice.Z().twist(5) + Lattice.Z().twist(11)
        assert L1.determinant() == L2.determinant()
        assert L1.is_in_same_genus_as(L2)
        assert not L1.is_isometric_to(L2)

    def test_general_indefinite_backend_maps_missing_witness_to_false(self) -> None:
        backend = LatticeIsometryBackend()
        left = self._wrapped_scaled_hyperbolic_plane(3)
        right = self._wrapped_split_scaled_hyperbolic_plane(3)
        assert not backend._compute_general_indefinite_isometry(left, right)

    def test_coble_constructors_and_orthogonal_complements_match_models(
        self,
    ) -> None:
        positive_line = Lattice.Z().twist(2)
        negative_line = Lattice.Z().twist(-2)
        coble_picard = Lattice.coble_picard()
        coble_transcendental = Lattice.coble_transcendental()
        expected_picard = reduce(
            self.NATIVE_LATTICE.direct_sum,
            (negative_line,) * int(self.PICARD_NEGATIVE_RANK),
            positive_line,
        )
        expected_transcendental = reduce(
            self.NATIVE_LATTICE.direct_sum,
            (
                Lattice.Z().twist(2),
                IntegralLattice("U"),
                IntegralLattice(-IntegralLattice("E8").inner_product_matrix()),
            ),
        )
        k3_lattice = Lattice.k3()
        orthogonal_complement = k3_lattice.orthogonal_complement(
            k3_lattice.submodule(tuple(k3_lattice.basis())[: int(self.HYPERBOLIC_RANK)])
        )
        expected_orthogonal = reduce(
            self.NATIVE_LATTICE.direct_sum,
            (
                IntegralLattice("U"),
                IntegralLattice("U"),
                IntegralLattice(-IntegralLattice("E8").inner_product_matrix()),
                IntegralLattice(-IntegralLattice("E8").inner_product_matrix()),
            ),
        )
        assert coble_picard.is_isometric_to(expected_picard)
        assert coble_transcendental.is_isometric_to(expected_transcendental)
        assert orthogonal_complement.is_isometric_to(expected_orthogonal)

    def test_lattice_morphism_contracts_are_exact_on_k3(self) -> None:
        wrapped_lattice = Lattice.k3()
        identity_morphism = wrapped_lattice.hom(wrapped_lattice).element_from_images(tuple(wrapped_lattice.basis()))
        assert identity_morphism.image().is_isometric_to(wrapped_lattice)
        assert identity_morphism.image().perp().rank().is_zero()

    def test_discriminant_group_identity_morphism_is_exact_for_a1_negative(
        self,
    ) -> None:
        wrapped_group = DiscriminantGroup.from_lattice(Lattice.A(1))
        identity_morphism = wrapped_group.hom(wrapped_group).element_from_images(tuple(wrapped_group.gens()))
        zero_morphism = wrapped_group.hom(wrapped_group).element_from_images((wrapped_group.zero(),))
        assert wrapped_group.zero().is_isotropic()
        assert identity_morphism.is_identity()
        assert not zero_morphism.is_identity()
        assert not zero_morphism.is_injective()
        assert not zero_morphism.is_surjective()
        assert identity_morphism.is_injective()
        assert identity_morphism.is_surjective()

    @classmethod
    def _unimodular_shear(cls, gram):
        """Apply a shear P = I + e_0 e_1^T to get a different Gram representation."""
        rank = gram.nrows()
        shear = identity_matrix(ZZ, rank)
        shear[0, 1] = 1
        return shear * gram * shear.transpose()

    def test_e8_is_unique_in_its_genus(self) -> None:
        """
        E8 is the unique even unimodular positive-definite lattice of rank 8.
        A unimodular basis change produces a different Gram matrix for the same
        lattice; the definite isometry engine must recover this.
        """
        standard = Lattice.from_gram(IntegralLattice("E8").gram_matrix())
        sheared_gram = self._unimodular_shear(IntegralLattice("E8").inner_product_matrix())
        sheared = Lattice.from_gram(sheared_gram)
        assert sheared_gram != IntegralLattice("E8").inner_product_matrix()
        assert standard.is_in_same_genus_as(sheared)
        assert standard.is_isometric_to(sheared)

    def test_negative_e8_is_unique_in_its_genus(self) -> None:
        """
        The negative-definite E8 lattice is unique in its genus.
        This exercises the negation branch of the definite isometry engine
        (``_positive_definite_copy`` negates a negative-definite lattice before
        calling Sage's quadratic-form equivalence).
        """
        negative_e8_gram = -IntegralLattice("E8").inner_product_matrix()
        standard = Lattice.from_gram(negative_e8_gram)
        sheared_gram = self._unimodular_shear(negative_e8_gram)
        sheared = Lattice.from_gram(sheared_gram)
        assert sheared_gram != negative_e8_gram
        assert standard.is_in_same_genus_as(sheared)
        assert standard.is_isometric_to(sheared)

    @classmethod
    def _d16_plus(cls):
        """
        Construct D16+, the even unimodular overlattice of D16.

        D16 has discriminant group (Z/2Z)^2 with two isotropic elements.
        Gluing along either one produces D16+, the unique even unimodular
        rank-16 lattice that is not isometric to E8 + E8.
        """
        d16 = IntegralLattice("D16")
        discriminant = d16.discriminant_group()
        isotropic_glue = next(g for g in discriminant if g.q() == 0 and not g.is_zero())
        overlattice = d16.overlattice([isotropic_glue.lift()])
        return IntegralLattice(overlattice.gram_matrix())

    def test_e8_e8_and_d16_plus_are_not_isometric(self) -> None:
        """
        There are exactly two isometry classes of even unimodular
        positive-definite lattices of rank 16: E8 + E8 and D16+. They share
        the same genus but are not isometric.
        """
        e8_e8 = Lattice.from_gram(IntegralLattice("E8").direct_sum(IntegralLattice("E8")).gram_matrix())
        d16_plus = Lattice.from_gram(self._d16_plus().gram_matrix())
        assert e8_e8.rank() == d16_plus.rank()
        assert e8_e8.signature_pair() == d16_plus.signature_pair()
        assert e8_e8.determinant() == d16_plus.determinant()
        assert e8_e8.is_even()
        assert d16_plus.is_even()
        assert e8_e8.is_in_same_genus_as(d16_plus)
        assert not e8_e8.is_isometric_to(d16_plus)

    def test_odd_unimodular_lorentzian_lattice_is_unique(self) -> None:
        """
        I_{1,8} = <1> + <-1>^8 is the unique odd unimodular lattice of
        signature (1, 8). A unimodular shear produces a different Gram matrix
        that the general indefinite backend (Dutour's Indefinite.jl) must
        recognize as isometric.
        """
        from sage.all import diagonal_matrix

        diagonal_gram = diagonal_matrix(ZZ, [1] + [-1] * 8)
        sheared_gram = self._unimodular_shear(diagonal_gram)
        standard = Lattice.from_gram(diagonal_gram)
        sheared = Lattice.from_gram(sheared_gram)
        assert diagonal_gram != sheared_gram
        assert not standard.is_even()
        assert standard.is_in_same_genus_as(sheared)
        assert standard.is_isometric_to(sheared)


class TestCentralizerAndEigenspaceMethods:
    """Tests for invariant_sublattice, coinvariant_sublattice,
    centralizer, and kernel_of_discriminant_action."""

    def test_invariant_sublattice_minus_identity_is_empty(self) -> None:
        """ker(-I - I) = ker(-2I) = 0 over ZZ, so no fixed vectors."""
        L = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        inv = L.invariant_sublattice(iota)
        assert inv.rank() == 0

    def test_coinvariant_sublattice_minus_identity_is_full(self) -> None:
        """Every vector is a (-1)-eigenvector of -I, so coinvariant = full."""
        L = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        coinv = L.coinvariant_sublattice(iota)
        assert coinv.rank() == L.rank()

    def test_coinvariant_sublattice_gram_matches_original(self) -> None:
        """The inner product on L_ι agrees with L (A2 has only ±1 eigs for -I)."""
        L = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        coinv = L.coinvariant_sublattice(iota)
        # Coinvariant of -I has same Gram as L (basis = identity map)
        assert coinv.inner_product_matrix() == L.inner_product_matrix()

    def test_invariant_and_coinvariant_rank_sum_equals_total(self) -> None:
        """For a rank-2 involution on A1+A1, ranks split as 1+1=2."""
        # A1 ⊕ A1 Gram matrix: diag(2, 2)
        gram = matrix(ZZ, [[2, 0], [0, 2]])
        L = Lattice.from_gram(gram)
        iota = matrix(ZZ, [[1, 0], [0, -1]])
        assert iota in L.orthogonal_group()
        inv = L.invariant_sublattice(iota)
        coinv = L.coinvariant_sublattice(iota)
        assert inv.rank() + coinv.rank() == L.rank()
        assert inv.rank() == 1
        assert coinv.rank() == 1

    def test_minus_identity_is_in_centralizer_of_a2(self) -> None:
        """-I commutes with every matrix, so it is in Z_{O(A2)}(-I)."""
        L = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        Z = L.orthogonal_group().centralizer(iota)
        assert iota in Z

    def test_centralizer_of_minus_identity_equals_full_group(self) -> None:
        """-I is central, so Z_{O(A2)}(-I) = O(A2); #gens should be positive."""
        L = Lattice.A(2)
        iota = -identity_matrix(ZZ, 2)
        Z = L.orthogonal_group().centralizer(iota)
        gens = Z.gens()
        assert len(gens) > 0
        O = L.orthogonal_group()
        for g in gens:
            assert g in O

    def test_non_commuting_matrix_not_in_centralizer(self) -> None:
        """A matrix that does not commute with iota is not in Z(iota)."""
        gram = matrix(ZZ, [[2, 0], [0, 2]])
        L = Lattice.from_gram(gram)
        # Involution negating second factor
        iota = matrix(ZZ, [[1, 0], [0, -1]])
        # Swap permutation: commutes only if block sizes are equal here, but
        # the swap does NOT commute with this iota (swap then negate ≠ negate then swap)
        swap = matrix(ZZ, [[0, 1], [1, 0]])
        assert swap in L.orthogonal_group()
        Z = L.orthogonal_group().centralizer(iota)
        # swap * iota != iota * swap: [[0,-1],[1,0]] vs [[0,1],[-1,0]]
        assert swap not in Z

    def test_identity_in_kernel_of_discriminant_action(self) -> None:
        """The identity acts trivially on every discriminant group."""
        L = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        K = L.orthogonal_group().centralizer(iota).kernel_of_discriminant_action()
        assert identity_matrix(ZZ, 2) in K

    def test_minus_identity_not_in_kernel_for_a2(self) -> None:
        """A2 has discriminant group Z/3Z; -I acts nontrivially on it."""
        L = Lattice.from_gram(IntegralLattice("A2").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        K = L.orthogonal_group().centralizer(iota).kernel_of_discriminant_action()
        assert iota not in K

    def test_kernel_of_disc_action_trivial_for_unimodular(self) -> None:
        """U is unimodular (A_L = 0), so every isometry acts trivially on A_L."""
        L = Lattice.from_gram(IntegralLattice("U").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        K = L.orthogonal_group().centralizer(iota).kernel_of_discriminant_action()
        assert iota in K

    def test_intersection_of_centralizer_and_stabilizer(self) -> None:
        """Z(ι) ∩ Stab(v) excludes -I when -I*v ≠ v."""
        L = Lattice.from_gram(IntegralLattice("U").gram_matrix())
        iota = -identity_matrix(ZZ, 2)
        from sage.all import vector

        v = vector(ZZ, [1, 0])
        Z = L.orthogonal_group().centralizer(iota)
        stab = L.orthogonal_group().stabilizer(v)
        combined = Z & stab
        assert identity_matrix(ZZ, 2) in combined
        assert iota not in combined  # -I*v = -v ≠ v
