from dzack_research.preamble.all import (
    ZZ,
    Embeddings,
    Involutions,
    Lattices,
    NamedLattices,
    signature_orthogonal_sums,
)


def test_named_surface_lattices_have_their_expected_signatures_and_ranks() -> None:
    assert NamedLattices.Tco.rank() == 11
    assert NamedLattices.Tco.signature_pair() == (2, 9)
    assert NamedLattices.TEn.rank() == 12
    assert NamedLattices.TEn.signature_pair() == (2, 10)
    assert NamedLattices.TdP.rank() == 20
    assert NamedLattices.TdP.signature_pair() == (2, 18)
    assert NamedLattices.LK3.rank() == 22
    assert NamedLattices.LK3.signature_pair() == (3, 19)
    assert Lattices.TEn is NamedLattices.TEn
    assert Lattices.TdP is NamedLattices.TdP
    assert Lattices.LK3 is NamedLattices.LK3


def test_named_embedding_chain_is_form_preserving_and_injective() -> None:
    chain = (
        Embeddings.TCo_into_TEn,
        Embeddings.TEn_into_TdP,
        Embeddings.TdP_into_LK3,
    )
    for embedding in chain:
        assert embedding.is_injective()
        for left in embedding.domain().module_generators():
            for right in embedding.domain().module_generators():
                assert left.b(right) == embedding(left).b(embedding(right))


def test_tco_generator_maps_diagonally_into_the_first_hyperbolic_plane() -> None:
    source = tuple(NamedLattices.Tco.module_generators())
    target = tuple(NamedLattices.TEn.module_generators())
    assert Embeddings.TCo_into_TEn(source[0]) == target[0] + target[1]


def test_e8_2_maps_diagonally_into_the_two_e8_blocks_of_tdp() -> None:
    source = tuple(NamedLattices.TEn.module_generators())
    target = tuple(NamedLattices.TdP.module_generators())
    for index in range(8):
        assert Embeddings.TEn_into_TdP(source[4 + index]) == target[4 + index] + target[12 + index]


def test_named_k3_automorphisms_are_nontrivial_involutions() -> None:
    generators = tuple(NamedLattices.LK3.module_generators())
    for involution in (Involutions.I_dP, Involutions.I_En, Involutions.I_Nik):
        assert all(involution(involution(generator)).to_tuple() == generator.to_tuple() for generator in generators)
        assert any(involution(generator).to_tuple() != generator.to_tuple() for generator in generators)


def test_catalogue_coinvariant_embeddings_are_formed_orthogonal_complements() -> None:
    pairs = (
        (Involutions.I_dP, Embeddings.TdP_into_LK3),
        (Involutions.I_En, Embeddings.TEn_into_LK3),
    )
    for involution, expected in pairs:
        invariant = involution.invariant_lattice()
        formed_coinvariants = involution.formed_coinvariants()
        assert invariant.rank() + formed_coinvariants.rank() == 22
        assert formed_coinvariants.inclusion() == expected


def test_named_invariant_and_formed_coinvariant_lattices_are_exact() -> None:
    triples = (
        (Involutions.I_dP, NamedLattices.Sdp, NamedLattices.TdP),
        (Involutions.I_En, NamedLattices.SEn, NamedLattices.TEn),
        (Involutions.I_Nik, NamedLattices.LpNik, NamedLattices.LmNik),
    )
    for involution, expected_plus, expected_minus in triples:
        actual_plus = involution.invariant_lattice().inclusion().domain()
        actual_minus = involution.formed_coinvariants().inclusion().domain()
        for actual, expected in (
            (actual_plus, expected_plus),
            (actual_minus, expected_minus),
        ):
            assert actual.gram_tensor().is_equal_tensor(expected.gram_tensor())
            witness = actual.Isom(expected).an_element()
            assert expected.gram_tensor().pullback(witness.tensor()).is_equal_tensor(
                actual.gram_tensor()
            )


def test_remaining_named_embeddings_are_primitive_and_form_preserving() -> None:
    for embedding in (
        Embeddings.E8_2_into_TdP,
        Embeddings.U_E8_2_into_TEn,
    ):
        assert embedding.is_primitive()
        for left in embedding.domain().module_generators():
            for right in embedding.domain().module_generators():
                assert left.b(right) == embedding(left).b(embedding(right))


def test_signature_block_search_enumerates_multisets_not_subsets() -> None:
    candidates = signature_orthogonal_sums((0, 4), (NamedLattices.A1, NamedLattices.D4))
    assert len(candidates) == 2
    assert all(candidate.signature_pair() == (0, 4) for candidate in candidates)


def test_indecomposable_registry_names_the_live_direct_sum_factors() -> None:
    lattice = NamedLattices.A1 + Lattices(ZZ)("A2") + NamedLattices.U_2
    assert lattice.is_decomposable()
    assert lattice.decomposition().summands() == lattice.biproduct_factors()
    assert lattice.decomposition_names() == ("I_{0,1}(2)", "A_{2}", "U(2)")


def test_bogachev_kolpakov_specimens_are_exact_ternary_lattices() -> None:
    assert NamedLattices.BogachevKolpakovNonReflective.signature_pair() == (1, 2)
    assert NamedLattices.BogachevKolpakovWithoutRoots.signature_pair() == (1, 2)
