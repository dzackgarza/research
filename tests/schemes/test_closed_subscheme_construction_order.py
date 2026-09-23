from dzack_research.preamble.all import ClosedEmbeddings, ProjectiveSpaces, QQ, Schemes


def test_projective_closed_subscheme_is_a_scheme_before_its_inclusion_is_built() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("x", "y"))
    x, y = line.homogeneous_coordinate_generators()

    point = line.closed_subscheme(x - y)

    assert point in Schemes(QQ)
    assert point in ClosedEmbeddings(line)
    assert point.inclusion().domain() is point
    assert point.inclusion().codomain() is line


def test_closed_subscheme_category_and_inclusion_are_order_independent() -> None:
    line = ProjectiveSpaces(QQ)(1, names=("u", "v"))
    u, v = line.homogeneous_coordinate_generators()

    category_first = line.closed_subscheme(u - v)
    placement = category_first.category()
    inclusion = category_first.inclusion()
    assert category_first.category() is placement
    assert category_first.inclusion() is inclusion
    assert inclusion.domain() is category_first
    assert inclusion.codomain() is line

    inclusion_first = line.closed_subscheme(u)
    other_inclusion = inclusion_first.inclusion()
    other_placement = inclusion_first.category()
    assert inclusion_first.inclusion() is other_inclusion
    assert inclusion_first.category() is other_placement
    assert other_inclusion.domain() is inclusion_first
    assert other_inclusion.codomain() is line
    assert other_placement is placement
