r"""AT21 toric ADE admission and branch sections use the live divisor/polytope owners."""


from dzack_research.preamble.all import ADELogPairs, QQ, ToricLogPairs


def _vertices(polytope):
    return {
        tuple(int(coordinate) for coordinate in vertex)
        for vertex in polytope.vertices()
    }




def test_branch_divisor_is_twice_the_complement_and_full_section_has_newton_polygon_q() -> None:
    pair = ADELogPairs(QQ).at21("D", 4)

    assert pair in ToricLogPairs(QQ)
    assert pair.category() is ToricLogPairs(QQ)
    assert pair.log_scheme() is pair.base_pair().log_scheme()
    assert pair.boundary_divisor() == pair.base_pair().blue_divisor()
    assert pair.branch_divisor_class() == 2 * pair.complementary_divisor()
    section = pair.full_newton_branch_section()
    assert _vertices(pair.branch_newton_polygon(section)) == _vertices(pair.polygon())
    branch = pair.branch_subscheme(section)
    assert branch.inclusion().codomain() is pair.scheme()


def test_table_five_e8_specialization_retains_the_source_exponent_support() -> None:
    pair = ADELogPairs(QQ).at21("E", 8)
    generic = pair.source_normal_form_section(constant=1)
    singular = pair.source_normal_form_section(constant=0)

    assert _vertices(pair.branch_newton_polygon(generic)) == _vertices(pair.polygon())
    singular_vertices = _vertices(pair.branch_newton_polygon(singular))
    assert singular_vertices == {(2, 2), (0, 3), (5, 0)}
