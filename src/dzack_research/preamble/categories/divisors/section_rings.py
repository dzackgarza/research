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


class _SectionRingConstruction:
    r"""The selected geometric source defining one section ring."""

    def divisor(self):
        raise ValueError("this section ring was selected from a line bundle, not a divisor")

    def line_bundle(self):
        raise ValueError("this section ring was selected from a divisor, not a line bundle")


class _LineBundleSectionRingConstruction(_SectionRingConstruction):
    r"""A section ring selected from one projective line bundle."""

    def __init__(self, line_bundle) -> None:
        self._line_bundle = line_bundle

    def section_scheme(self):
        return self.line_bundle().scheme()

    def line_bundle(self):
        return self._line_bundle


class _ToricDivisorSectionRingConstruction(_SectionRingConstruction):
    r"""A section ring selected from one divisor on one toric scheme."""

    def __init__(self, scheme, divisor) -> None:
        self._scheme = scheme
        self._divisor = divisor

    def section_scheme(self):
        return self._scheme

    def divisor(self):
        return self._divisor


class SectionRings(OwnedCategoryOverBaseRing):
    r"""Nonnegatively graded section algebras over the stated coefficient ring."""

    def super_categories(self):
        return [GradedAlgebras(self.base_ring(), NN)]

    @classmethod
    def _repr_object_names(cls):
        return "section rings"

    def _call_(self, source, divisor=None):
        r"""Construct the selected section algebra from a divisor or line bundle."""
        if divisor is None:
            return _line_bundle_section_ring(self, source)
        return _toric_divisor_section_ring(self, source, divisor)

    class ParentMethods:
        def section_ring_construction(self):
            r"""Return the selected geometric datum defining this section ring."""
            return self._section_ring_construction

        def section_scheme(self):
            return self.section_ring_construction().section_scheme()

        def section_divisor(self):
            return self.section_ring_construction().divisor()

        def section_line_bundle(self):
            return self.section_ring_construction().line_bundle()

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
            if element == self.zero():
                raise ValueError("zero has no selected homogeneous section-ring degree")
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
            if not degrees:
                raise ValueError("zero has no selected homogeneous section-ring degree")
            selected = degrees[0]
            if any(degree != selected for degree in degrees[1:]):
                raise ValueError("the section-ring element is not homogeneous")
            return NN(selected)

        @cached_method
        def graded_piece(self, degree):
            r"""Return the actual section module in nonnegative degree ``n``."""
            degree = NN(degree)
            construction = self.section_ring_construction()
            match construction:
                case _LineBundleSectionRingConstruction():
                    return construction.line_bundle().tensor_power(int(degree)).global_sections()
                case _ToricDivisorSectionRingConstruction():
                    divisor = construction.divisor()
                    integers = divisor.parent().base_ring()
                    return construction.section_scheme().divisor_section_space(
                        integers(int(degree)) * divisor
                    )
                case _:
                    raise TypeError("unknown section-ring construction datum")

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
            inclusion = self.homogeneous_component_map(degree)
            module = inclusion.codomain()
            value = inclusion(section)
            realize = getattr(module, "realize", None)
            return self(realize(value) if callable(realize) else value)


def _section_exponent_data(section_space):
    selected = getattr(section_space, "section_space_construction", None)
    if not callable(selected):
        raise NotImplementedError(
            "this section module has no selected polynomial-section presentation"
        )
    construction = selected()
    labels = tuple(section_space.module_generating_set())
    if callable(getattr(section_space, "multidegree", None)):
        return {
            monomial: tuple(
                int(value)
                for block in construction.exponents_of(monomial)
                for value in block
            )
            for monomial in labels
        }
    if callable(getattr(section_space, "homogeneous_degree", None)):
        return {
            monomial: tuple(
                int(value) for value in construction.exponents_of(monomial)
            )
            for monomial in labels
        }
    raise NotImplementedError(
        "this section module is not a represented polynomial section space"
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
        if need != 0:
            raise ArithmeticError("a homogeneous exponent block has the wrong total degree")
        parts.append(tuple(part))
    if any(remaining):
        raise ArithmeticError("homogeneous exponent splitting left a nonzero remainder")
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
    if len(base_degree) != len(block_widths):
        raise ValueError("section exponent blocks and multidegree have different lengths")
    if len(exponents) != sum(block_widths):
        raise ValueError("section exponent vector has the wrong number of coordinates")
    if count == 0:
        if any(exponents):
            raise ArithmeticError("degree-zero section exponents must vanish")
        return ()

    split_blocks = []
    offset = 0
    for degree, width in zip(base_degree, block_widths, strict=True):
        block = exponents[offset : offset + width]
        if sum(block) != count * degree:
            raise ArithmeticError("a section exponent block has the wrong total degree")
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
    from dzack_research.preamble.categories.divisors.invertible_sheaves import (
        ProductProjectiveLineBundle,
        ProjectiveSpaceLineBundle,
    )

    if isinstance(bundle, ProjectiveSpaceLineBundle):
        degree = (_own_ring(SageZZ)(bundle.degree()),)
        widths = (int(bundle.projective_space().relative_dimension()) + 1,)
        return degree, widths
    if isinstance(bundle, ProductProjectiveLineBundle):
        product = bundle.projective_product()
        factors = product.factors()
        labels = tuple(factors.index_set())
        degree = tuple(bundle.multidegree()[label] for label in labels)
        widths = tuple(
            int(factors[label].relative_dimension()) + 1
            for label in labels
        )
        return degree, widths
    raise TypeError(
        "the represented line-bundle section-ring construction supports standard projective and multiprojective O(d) bundles"
    )


def _line_bundle_section_ring(category, bundle):
    r"""Construct the Veronese/Segre-Veronese section algebra of ``bundle``."""
    if bundle.scheme().scheme_base_ring() is not category.base_ring():
        raise ValueError("a line-bundle section ring stays over the bundle's scalar base")
    base_degree, block_widths = _line_bundle_section_data(bundle)
    if any(degree < 0 for degree in base_degree):
        raise NotImplementedError(
            "the represented projective section-ring presentation requires a nonnegative line-bundle multidegree"
        )
    degree_one = bundle.global_sections()
    exponent_data = _section_exponent_data(degree_one)
    basis_labels = tuple(degree_one.module_generating_set())
    generator_exponents = tuple(exponent_data[label] for label in basis_labels)
    semigroup_generators = tuple(
        (*exponents, 1)
        for exponents in generator_exponents
    )
    if not semigroup_generators:
        raise ArithmeticError("a nonnegative projective O(d) must have a degree-one section")
    names = tuple(f"s{position}" for position in range(len(semigroup_generators)))
    return AffineSemigroupAlgebras(category.base_ring())(
        semigroup_generators,
        names=names,
        extra_categories=(category,),
        extra_construction_data=(
            ("_section_ring_construction", _LineBundleSectionRingConstruction(bundle)),
        ),
    )


def _toric_divisor_section_ring(category, scheme, divisor):
    r"""Construct the cone-over-polytope section algebra of a toric Cartier divisor."""
    from sage.geometry.cone import Cone as _SageCone

    from dzack_research.preamble.categories.schemes.toric.fans import _engine_vector
    if scheme.scheme_base_ring() is not category.base_ring():
        raise ValueError("a divisor section ring stays over the scheme's scalar base")
    if not scheme.fan().is_complete():
        raise ValueError("the supported toric section-ring construction requires a complete fan")
    if not scheme.is_cartier(divisor):
        raise ValueError("a divisor section ring requires a Cartier divisor")
    if not scheme.is_basepoint_free(divisor):
        raise ValueError(
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
            ("_section_ring_construction", _ToricDivisorSectionRingConstruction(scheme, divisor)),
        ),
    )


__all__ = ["SectionRings"]
