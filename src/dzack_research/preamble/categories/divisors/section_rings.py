r"""Section rings of represented divisors and projective line bundles."""

from sage.misc.cachefunc import cached_method
from sage.rings.integer_ring import ZZ as SageZZ

from dzack_research.preamble.categories.algebras.graded_algebras import GradedAlgebras
from dzack_research.preamble.categories.algebras.semigroup_algebras import (
    AffineSemigroupAlgebras,
)
from dzack_research.preamble.categories.modules.pure.modules import BilinearMap
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    OwnedIntegralDomains,
    _engine_element,
    _own_ring,
)
from dzack_research.preamble.categories.sets.set_categories import NN


class SectionRings(OwnedCategoryOverBaseRing):
    r"""Section rings \(R(X, L) = \bigoplus_{n \ge 0} H^0(X, L^{\otimes n})\).

    An object is a nonnegatively graded algebra presented as an affine
    semigroup algebra.  The algebra levels consume the presentation; this
    level adds the scheme \(X\) and the line bundle \(L\) the ring is stated
    on, given either as \(L\) itself or as a Cartier divisor \(D\) with
    \(L = \mathcal{O}_X(D)\).
    """

    def super_categories(self):
        return [GradedAlgebras(self.base_ring(), NN)]

    @classmethod
    def _repr_object_names(cls):
        return "section rings"

    def _call_(self, source, divisor=None):
        r"""\(R(X, L)\) for a line bundle ``source``, or \(R(X, \mathcal{O}_X(D))\) for a scheme ``source`` and a divisor."""
        match divisor:
            case None:
                return _line_bundle_section_ring(self, source)
            case _:
                return _toric_divisor_section_ring(self, source, divisor)

    class ParentMethods:
        def __init__(
            self,
            section_scheme,
            section_line_bundle=None,
            section_divisor=None,
            **rest,
        ) -> None:
            assert (section_line_bundle is None) != (section_divisor is None), (
                "a section ring is stated on one line bundle or on one divisor"
            )
            self._section_scheme = section_scheme
            self._section_line_bundle = section_line_bundle
            self._section_divisor = section_divisor
            super().__init__(**rest)

        def section_scheme(self):
            r"""The scheme \(X\) whose sections form this ring."""
            return self._section_scheme

        def section_divisor(self):
            r"""The divisor \(D\) with \(L = \mathcal{O}_X(D)\), when the ring was stated on a divisor."""
            assert self._section_divisor is not None, (
                "this section ring was stated on a line bundle, not a divisor"
            )
            return self._section_divisor

        def section_line_bundle(self):
            r"""The line bundle \(L\), when the ring was stated on a line bundle."""
            assert self._section_line_bundle is not None, (
                "this section ring was stated on a divisor, not a line bundle"
            )
            return self._section_line_bundle

        @cached_method
        def section_semigroup_generators(self):
            return self.affine_semigroup_generator_coordinates()

        def generator_degree(self, label):
            point = self.section_semigroup_generators()[label]
            final_position = int(point.cardinality().finite_value()) - 1
            return NN(int(point[final_position]))

        def homogeneous_degree(self, element):
            r"""Return the nonnegative degree of one homogeneous section-ring element."""
            element = self(element)
            assert element != self.zero(), "zero has no selected homogeneous section-ring degree"
            presentation = self.presentation_ring()
            representative = self.lift_to_presentation(element)
            backend = _engine_element(presentation, representative)
            labels = tuple(self.algebra_generating_set())
            degrees = []
            for exponents, coefficient in backend.dict().items():
                if not coefficient:
                    continue
                degree = 0
                for position, exponent in enumerate(exponents):
                    degree += int(exponent) * int(self.generator_degree(labels[position]))
                degrees.append(degree)
            selected = degrees[0]
            assert all(degree == selected for degree in degrees[1:]), (
                "the section-ring element is not homogeneous"
            )
            return NN(selected)

        @cached_method
        def graded_piece(self, degree):
            r"""The section module \(H^0(X, L^{\otimes n})\) in nonnegative degree ``n``."""
            degree = NN(degree)
            match self._section_line_bundle:
                case None:
                    divisor = self.section_divisor()
                    integers = divisor.parent().base_ring()
                    return self.section_scheme().divisor_section_space(
                        integers(int(degree)) * divisor
                    )
                case bundle:
                    return bundle.tensor_power(int(degree)).global_sections()

        def section_multiplication(self, left_degree, right_degree):
            r"""Multiply sections in two graded pieces of a projective line-bundle ring."""
            self.section_line_bundle()
            left_degree = NN(left_degree)
            right_degree = NN(right_degree)
            left = self.graded_piece(left_degree)
            right = self.graded_piece(right_degree)
            target = self.graded_piece(NN(int(left_degree) + int(right_degree)))
            left_exponents = _section_exponent_data(left)
            right_exponents = _section_exponent_data(right)
            target_exponents = _section_exponent_data(target)
            target_by_exponents = {
                exponents: monomial for monomial, exponents in target_exponents.items()
            }

            def product(left_monomial, right_monomial):
                exponents = tuple(
                    a + b
                    for a, b in zip(
                        left_exponents[left_monomial],
                        right_exponents[right_monomial],
                        strict=True,
                    )
                )
                return target.module_generator(target_by_exponents[exponents])

            return BilinearMap(left, right, target, product)

        @cached_method
        def homogeneous_component_map(self, degree):
            r"""Return the map ``H^0(X,L^n) -> R(L)`` into the degree-``n`` component."""
            bundle = self.section_line_bundle()
            degree = NN(degree)
            piece = self.graded_piece(degree)
            count = int(degree)
            degree_one = bundle.global_sections()
            degree_one_exponents = _section_exponent_data(degree_one)
            generator_by_exponents = {
                tuple(exponents): label
                for label, exponents in zip(
                    self.algebra_generating_set(),
                    (
                        degree_one_exponents[label]
                        for label in degree_one.module_generating_set()
                    ),
                    strict=True,
                )
            }
            base_degree, block_widths = _line_bundle_section_data(bundle)
            base_degree = tuple(int(value) for value in base_degree)
            block_widths = tuple(int(value) for value in block_widths)
            piece_exponents = _section_exponent_data(piece)

            def basis_image(label):
                if count == 0:
                    return self.one()
                parts = _split_section_exponents(
                    piece_exponents[label],
                    base_degree,
                    block_widths,
                    count,
                )
                value = self.one()
                for exponents in parts:
                    value *= self.algebra_generator(generator_by_exponents[exponents])
                return value

            target_module = self.underlying_module()
            return piece.module_category().Mor(piece, target_module)(
                {
                    label: target_module(basis_image(label))
                    for label in piece.module_generating_set()
                }
            )

        def homogeneous_component_element(self, degree, section):
            r"""Return one homogeneous section as the corresponding section-ring element."""
            return self(self.homogeneous_component_map(degree)(section))


def _section_exponent_data(section_space):
    r"""The flat exponent vector of each framing monomial of a polynomial section space."""
    from dzack_research.preamble.categories.divisors.linear_systems import (
        HomogeneousPolynomialSectionSpaces,
        MultihomogeneousPolynomialSectionSpaces,
    )

    ring = section_space.base_ring()
    labels = tuple(section_space.module_generating_set())
    match section_space:
        case _ if section_space in MultihomogeneousPolynomialSectionSpaces(ring):
            return {
                monomial: tuple(
                    int(value)
                    for block in section_space.monomial_exponents(monomial)
                    for value in block
                )
                for monomial in labels
            }
        case _ if section_space in HomogeneousPolynomialSectionSpaces(ring):
            return {
                monomial: tuple(
                    int(value) for value in section_space.monomial_exponents(monomial)
                )
                for monomial in labels
            }
        case _:
            assert False, (
                "exponent data is read from a homogeneous or multihomogeneous polynomial "
                "section space; this section module is neither"
            )


def _split_block(exponents, part_total, count):
    remaining = list(exponents)
    parts = []
    for _ in range(count):
        need = int(part_total)
        part = []
        for position, available in enumerate(remaining):
            take = min(int(available), need)
            part.append(take)
            remaining[position] -= take
            need -= take
        assert need == 0, "a homogeneous exponent block has the wrong total degree"
        parts.append(tuple(part))
    assert not any(remaining), "homogeneous exponent splitting left a nonzero remainder"
    return tuple(parts)


def _split_section_exponents(exponents, base_degree, block_widths, count):
    r"""Split a degree-``count`` monomial into ``count`` degree-one monomials.

    Each projective factor is one independent exponent block.  A block of total
    degree ``count*d_i`` is split into ``count`` blocks of degree ``d_i``; the
    corresponding pieces are then concatenated factorwise.  This is a selected
    factorization in the affine semigroup.  Different choices represent the
    same section-ring element by the toric relations.
    """
    exponents = tuple(int(value) for value in exponents)
    base_degree = tuple(int(value) for value in base_degree)
    block_widths = tuple(int(value) for value in block_widths)
    count = int(count)
    assert len(base_degree) == len(block_widths), (
        "section exponent blocks and multidegree have different lengths"
    )
    assert len(exponents) == sum(block_widths), (
        "section exponent vector has the wrong number of coordinates"
    )
    if count == 0:
        assert not any(exponents), "degree-zero section exponents must vanish"
        return ()

    split_blocks = []
    offset = 0
    for degree, width in zip(base_degree, block_widths, strict=True):
        block = exponents[offset : offset + width]
        assert sum(block) == count * degree, "a section exponent block has the wrong total degree"
        split_blocks.append(_split_block(block, degree, count))
        offset += width

    return tuple(
        tuple(
            exponent
            for block_parts in split_blocks
            for exponent in block_parts[position]
        )
        for position in range(count)
    )


def _line_bundle_section_data(bundle):
    r"""The degree and the coordinate width of each projective factor of ``bundle``.

    Both are read off the degree-one section space of the bundle, which is a
    homogeneous polynomial space on a projective space or a multihomogeneous
    one on a product of projective spaces.
    """
    from dzack_research.preamble.categories.divisors.linear_systems import (
        HomogeneousPolynomialSectionSpaces,
        MultihomogeneousPolynomialSectionSpaces,
    )

    integers = _own_ring(SageZZ)
    sections = bundle.global_sections()
    ring = sections.base_ring()
    match sections:
        case _ if sections in HomogeneousPolynomialSectionSpaces(ring):
            width = int(sections.homogeneous_coordinate_ring().algebra_generating_set().cardinality())
            return (integers(sections.homogeneous_degree()),), (width,)
        case _ if sections in MultihomogeneousPolynomialSectionSpaces(ring):
            multidegree = sections.multidegree()
            labels = tuple(multidegree.index_set())
            degrees = tuple(multidegree[label] for label in labels)
            widths = tuple(
                stop - start
                for start, stop in (
                    sections.coordinate_block(position) for position in range(len(labels))
                )
            )
            return degrees, widths
        case _:
            assert False, (
                "the represented line-bundle section ring is stated on projective and "
                "multiprojective O(d), whose sections are polynomial section spaces"
            )


def _line_bundle_section_ring(category, bundle):
    r"""Construct the Veronese/Segre-Veronese section algebra of ``bundle``."""
    assert bundle.scheme().scheme_base_ring() is category.base_ring(), (
        "a line-bundle section ring stays over the bundle's scalar base"
    )
    base_degree, _block_widths = _line_bundle_section_data(bundle)
    assert all(degree >= 0 for degree in base_degree), (
        "the represented projective section-ring presentation requires a nonnegative "
        "line-bundle multidegree"
    )
    degree_one = bundle.global_sections()
    exponent_data = _section_exponent_data(degree_one)
    semigroup_generators = tuple(
        (*exponent_data[label], 1)
        for label in degree_one.module_generating_set()
    )
    assert semigroup_generators, "a nonnegative projective O(d) must have a degree-one section"
    names = tuple(f"s{position}" for position in range(len(semigroup_generators)))
    return AffineSemigroupAlgebras(category.base_ring())(
        semigroup_generators,
        names=names,
        extra_categories=(category,),
        extra_construction_data=(
            ("section_scheme", bundle.scheme()),
            ("section_line_bundle", bundle),
        ),
    )


def _toric_divisor_section_ring(category, scheme, divisor):
    r"""Construct the cone-over-polytope section algebra of a toric Cartier divisor."""
    from sage.geometry.cone import Cone as _SageCone

    from dzack_research.preamble.categories.schemes.toric.fans import _engine_vector

    assert scheme.scheme_base_ring() is category.base_ring(), (
        "a divisor section ring stays over the scheme's scalar base"
    )
    assert scheme.fan().is_complete(), (
        "the supported toric section-ring construction requires a complete fan"
    )
    assert scheme.is_cartier(divisor), "a divisor section ring requires a Cartier divisor"
    assert scheme.is_basepoint_free(divisor), (
        "the supported cone-over-polytope section-ring construction requires a basepoint-free divisor"
    )

    polytope = scheme.divisor_polytope(divisor)
    lattice = polytope.ambient_lattice()
    cone_rays = tuple(
        (*tuple(_engine_vector(lattice, vertex)), 1)
        for vertex in polytope.vertices()
    )
    hilbert_basis = tuple(
        tuple(int(entry) for entry in vector)
        for vector in _SageCone(cone_rays).Hilbert_basis()
    )
    return AffineSemigroupAlgebras(category.base_ring())(
        hilbert_basis,
        names=tuple(f"s{position}" for position in range(len(hilbert_basis))),
        extra_categories=(category, OwnedIntegralDomains()),
        extra_construction_data=(
            ("section_scheme", scheme),
            ("section_divisor", divisor),
        ),
    )


__all__ = ["SectionRings"]
