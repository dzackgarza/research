from dzack_research.preamble.all import ZZ, Zp


def test_zp_accepts_the_owned_integer_produced_by_sage_session_preparsing() -> None:
    completion = Zp(ZZ(5))

    assert completion.ideal_of_definition() == ZZ.ideal(ZZ(5))
    assert completion.residue_field().cardinality() == 5
