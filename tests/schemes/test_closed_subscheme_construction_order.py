from dzack_research.preamble.all import ClosedEmbeddings, ProjectiveSpaces, QQ, Schemes


def test_projective_closed_subscheme_is_a_scheme_before_its_inclusion_is_built() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x", "y"))
    x, y = line.gens()

    point = line.closed_subscheme(x - y)

    assert point in Schemes(QQ)
    assert point in ClosedEmbeddings(line)
    assert point.inclusion().domain() is point
    assert point.inclusion().codomain() is line
