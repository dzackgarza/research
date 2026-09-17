r"""A chosen lattice polytope owns its toric polarization and zero divisors."""

from dzack_research.preamble.all import QQ, LatticePolygons


def test_polytope_reconstructs_its_polarizing_divisor_and_character_section_zero_scheme() -> None:
    polygon = LatticePolygons()(((0, 0), (2, 0), (0, 2)))
    surface = polygon.toric_variety(QQ)
    divisor = surface.polarizing_divisor()
    recovered = surface.divisor_polytope(divisor)

    assert {
        tuple(int(coordinate) for coordinate in vertex)
        for vertex in recovered.vertices()
    } == {
        tuple(int(coordinate) for coordinate in vertex)
        for vertex in polygon.vertices()
    }

    sections = surface.divisor_section_space(divisor)
    section = sections.linear_combination(
        {label: QQ.one() for label in sections.module_generating_set()}
    )
    line_bundle = surface.invertible_sheaf_of_divisor(divisor)
    compatible = surface.compatible_divisor_section(
        divisor,
        section,
        line_bundle=line_bundle,
    )
    zero = surface.zero_subscheme_of_divisor_section(
        divisor,
        section,
        line_bundle=line_bundle,
    )

    assert compatible.parent() is line_bundle.compatible_sections()
    assert compatible == sum(
        (
            surface.compatible_divisor_section(
                divisor, sections.module_generator(label), line_bundle=line_bundle
            )
            for label in sections.module_generating_set()
        ),
        line_bundle.compatible_sections().zero(),
    )
    assert zero.inclusion().codomain() is surface
    assert zero._preamble_defining_toric_section == section
    assert zero._preamble_defining_toric_divisor == divisor
