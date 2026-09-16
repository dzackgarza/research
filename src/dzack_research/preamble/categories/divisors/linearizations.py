r"""Linearizations of projective line bundles under represented group actions.

A ``G``-linearization of a line bundle ``L`` over a ``G``-scheme is additional
data: isomorphisms ``lambda_g : g^*L -> L`` satisfying the cocycle.  Preserving
the isomorphism class of ``L`` does not select these maps.  For the standard
``O(d)`` on projective space, a projective-coordinate action canonically
identifies ``g^*O(d)`` with ``O(d)``; multiplying that identification by a
character gives the familiar character twists.

The induced *left* action on global sections is

``g . s = lambda_g((g^{-1})^* s)``.

The inverse is essential: pullback is contravariant.  The resulting section
space is constructed as the existing module over the group algebra, so
invariants and isotypic components are those of the common group-module owner.
"""

from sage.misc.cachefunc import cached_function, cached_method
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
from dzack_research.preamble.categories.group.g_objects import GObjects
from dzack_research.preamble.categories.group.groups import OwnedGroups
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.schemes.schemes import (
    Schemes,
    _affine_morphism_from_pullback,
)
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.indexed_families import (
    finite_indexed_family,
    indexed_family,
)


class _ProjectiveLineBundleLinearizationIsomorphism(SageObject):
    r"""One selected ``lambda_g : g^*L -> L`` in the standard ``O(d)`` model."""

    def __init__(self, linearization, group_element) -> None:
        self._linearization = linearization
        self._group_element = linearization.acting_group()(group_element)

    def linearization(self):
        return self._linearization

    def group_element(self):
        return self._group_element

    def pullback_morphism(self):
        return self.linearization().scheme_action_of(self.group_element())

    def domain(self):
        r"""The canonically identified pullback ``g^*L``."""
        return self.linearization().line_bundle()

    def codomain(self):
        return self.linearization().line_bundle()

    def scalar(self):
        return self.linearization().character_value(self.group_element())

    def inverse(self):
        return self.linearization().linearization_isomorphism(
            self.group_element().inverse()
        )

    def _repr_(self):
        return (
            f"Linearization isomorphism for {self.group_element()} on "
            f"{self.linearization().line_bundle()} with scalar {self.scalar()}"
        )


class _EigensectionDivisorConstruction(SageObject):
    r"""The selected eigensection datum defining one invariant zero divisor."""

    def __init__(self, linearization, section, character) -> None:
        self._linearization = linearization
        self._section = section
        self._character = character

    def linearization(self):
        return self._linearization

    def section(self):
        return self._section

    def character(self):
        return self._character


class _ProductProjectiveCoordinateActionConstruction(SageObject):
    r"""The coordinate weights and affine-chart arrows defining one product action."""

    def __init__(self, coordinate_weights, local_automorphisms) -> None:
        self._coordinate_weights = coordinate_weights
        self._local_automorphisms = local_automorphisms

    def coordinate_weights(self):
        return self._coordinate_weights

    def local_automorphisms(self):
        return self._local_automorphisms

    def local_automorphism(self, chart_index):
        return self.local_automorphisms()[chart_index]


class _ProjectiveLineBundleLinearization(SageObject):
    r"""A character-twisted linearization of ``O(d)`` under a projective action."""

    def __init__(self, line_bundle, scheme_action_functor, character) -> None:
        from dzack_research.preamble.categories.divisors.invertible_sheaves import (
            ProjectiveSpaceLineBundle,
        )

        if not isinstance(line_bundle, ProjectiveSpaceLineBundle):
            raise TypeError("this linearization owner currently represents projective-space O(d)")
        scheme = line_bundle.projective_space()
        base = scheme.scheme_base_ring()
        if not isinstance(scheme_action_functor, GroupActionFunctor):
            raise TypeError("a projective linearization requires an actual BG -> Schemes action functor")
        group = scheme_action_functor.group()
        if scheme_action_functor.codomain() != Schemes(base):
            raise ValueError("the projective action functor has the wrong scheme category")
        if scheme_action_functor.underlying_object() is not scheme:
            raise ValueError("the projective action functor acts on a different scheme")
        assert group.is_finite() is True, (
            "character-twist validation is represented here for a finite acting group"
        )

        self._line_bundle = line_bundle
        self._scheme_action_functor = scheme_action_functor
        self._group = group
        self._character = character
        self._validate_character()

    def line_bundle(self):
        return self._line_bundle

    underlying_line_bundle = line_bundle

    def projective_space(self):
        return self.line_bundle().projective_space()

    def section_scheme(self):
        return self.projective_space()

    def acting_group(self):
        return self._group

    def scheme_action_functor(self):
        return self._scheme_action_functor

    @cached_method
    def acted_scheme(self):
        r"""Return the generic ``G``-object represented by the scheme action functor."""
        return GObjects(
            self.acting_group(),
            Schemes(self.section_scheme().scheme_base_ring()),
        )(self.scheme_action_functor())

    def character_value(self, group_element):
        base = self.section_scheme().scheme_base_ring()
        value = base(self._character(self.acting_group()(group_element)))
        if not value.is_unit():
            raise ValueError("a linearization character takes values in scalar units")
        return value

    def _validate_character(self) -> None:
        group = self.acting_group()
        base = self.section_scheme().scheme_base_ring()
        if self.character_value(group.one()) != base.one():
            raise ValueError("a linearization character sends the identity to one")
        elements = tuple(group)
        for left in elements:
            for right in elements:
                if self.character_value(left * right) != self.character_value(left) * self.character_value(right):
                    raise ValueError("the selected linearization twist is not a character")

    def scheme_action_of(self, group_element):
        group_element = self.acting_group()(group_element)
        action = self.scheme_action_functor()
        point = action.domain().an_object()
        arrow = action.domain().Mor(point, point)(group_element)
        return action(arrow)

    @cached_method
    def linearization_isomorphism(self, group_element):
        return _ProjectiveLineBundleLinearizationIsomorphism(self, group_element)

    def cocycle_holds(self, left, right) -> bool:
        r"""Check the character part of ``lambda_{gh}=lambda_g o g^*lambda_h``.

        The untwisted ``O(d)`` lift is functorial pullback of homogeneous
        coordinates.  Hence the only additional cocycle condition for a twist
        is multiplicativity of its scalar character, which is recorded here.
        """
        left = self.acting_group()(left)
        right = self.acting_group()(right)
        return self.character_value(left * right) == (
            self.character_value(left) * self.character_value(right)
        )

    @cached_method
    def section_action_of(self, group_element):
        r"""Return ``s |-> chi(g) (g^-1)^*s`` on ``H^0(P,O(d))``."""
        group_element = self.acting_group()(group_element)
        sections = self.line_bundle().global_sections()
        inverse_action = self.scheme_action_of(group_element.inverse())
        pullback = sections.pullback_by_projective_automorphism(inverse_action)
        scalar = self.character_value(group_element)
        return sections.Mor(sections).elementwise(
            lambda section: sections.scalar_multiple(scalar, pullback(section)),
            verify_linearity=False,
        )

    @cached_method
    def section_group_module(self):
        r"""Return the actual module over ``R[G]`` induced by this linearization."""
        base = self.section_scheme().scheme_base_ring()
        group_algebra = OwnedGroups().group_algebra(base)(self.acting_group())
        sections = self.line_bundle().global_sections()
        return Modules(group_algebra)(
            sections,
            lambda group_element, section: self.section_action_of(group_element)(section),
        )

    def invariant_sections(self):
        return self.section_group_module().module_invariants()

    def isotypic_decomposition(self):
        return self.section_group_module().isotypic_decomposition()

    @cached_method
    def coherent_cohomology_group_module(self, degree):
        r"""Return the induced ``G``-action on represented ``H^degree(P,O(d))``.

        For ``d >= 0`` on projective space, the represented global-section
        module is ``H^0``.  On a projective line the only other coherent
        cohomology group is ``H^1``, which vanishes in this nonnegative regime;
        its zero module carries the unique trivial action.  Negative-degree
        nonzero higher cohomology is left to the later general projective
        cohomology owner rather than inferred from a dimension formula here.
        """
        degree = int(degree)
        if degree < 0:
            raise ValueError("a coherent cohomology degree is nonnegative")
        supported_h1 = (
            int(self.projective_space().relative_dimension()) == 1
            and degree == 1
            and self.line_bundle().degree() >= 0
        )
        assert degree == 0 or supported_h1, (
            "coherent cohomology actions are represented here on H^0 and on the vanishing H^1 "
            "of nonnegative O(d) on P^1"
        )
        if degree == 0:
            return self.section_group_module()
        base = self.section_scheme().scheme_base_ring()
        zero = base._fresh_free_module_on(finite_ordered_set(()))
        return Modules(base).trivial_action(self.acting_group())(zero)

    def equivariant_section_restriction(self, divisor):
        r"""Restrict sections equivariantly to an invariant eigensection divisor.

        The underlying map is the exact image-valued section restriction.  The
        divisor is invariant because it is the zero locus of an eigensection,
        so its restriction kernel is stable.  Acting on a target section means
        choosing any source preimage, acting there, and restricting again;
        stability of the kernel makes that independent of the preimage.
        """
        if not self.is_eigensection_divisor(divisor):
            raise ValueError("equivariant restriction here requires an invariant eigensection divisor of this linearization")
        restriction = self.line_bundle().restriction_map(divisor)
        source = self.section_group_module()
        target_unacted = restriction.codomain()
        group_algebra = source.group_algebra()

        def target_action(group_element, element):
            preimage = restriction.preimage(element)
            return restriction(
                self.section_action_of(group_element)(preimage)
            )

        target = Modules(group_algebra)(target_unacted, target_action)
        images = {
            label: target.equip_action_morphism()(
                restriction(source.unacted_module().module_generator(label))
            )
            for label in source.module_generating_set()
        }
        return source.Mor(target)(images)

    def is_eigensection(self, section, character) -> bool:
        sections = self.line_bundle().global_sections()
        section = sections(section)
        base = sections.base_ring()
        return all(
            self.section_action_of(group_element)(section)
            == sections.scalar_multiple(base(character(group_element)), section)
            for group_element in self.acting_group()
        )

    def eigensection_divisor(self, section, character):
        r"""Return the invariant zero divisor of a selected eigensection."""
        sections = self.line_bundle().global_sections()
        section = sections(section)
        if not self.is_eigensection(section, character):
            raise ValueError("the selected section does not transform through this character")
        polynomial = sections.homogeneous_polynomial(section)
        divisor = self.projective_space().closed_subscheme(polynomial)
        divisor._preamble_eigensection_divisor_construction = (
            _EigensectionDivisorConstruction(self, section, character)
        )
        return divisor

    def eigensection_divisor_construction(self, divisor):
        r"""Return the selected eigensection datum defining ``divisor`` for this lift."""
        construction = getattr(
            divisor,
            "_preamble_eigensection_divisor_construction",
            None,
        )
        if (
            not isinstance(construction, _EigensectionDivisorConstruction)
            or construction.linearization() is not self
        ):
            raise ValueError(
                "this divisor was not constructed from an eigensection of this linearization"
            )
        return construction

    def is_eigensection_divisor(self, divisor) -> bool:
        r"""Return whether ``divisor`` was constructed from an eigensection of this lift."""
        try:
            self.eigensection_divisor_construction(divisor)
        except ValueError:
            return False
        return True

    @staticmethod
    def _normalized_projective_coordinates(point):
        coordinates = tuple(point.point_coordinates())
        base = point.codomain().scheme_base_ring()
        pivot = next(
            (coordinate for coordinate in coordinates if coordinate != base.zero()),
            None,
        )
        if pivot is None:
            raise ValueError("projective point coordinates cannot all vanish")
        inverse = pivot.inverse_of_unit()
        return tuple(coordinate * inverse for coordinate in coordinates)

    def point_is_fixed(self, point) -> bool:
        if point.codomain() is not self.projective_space():
            raise ValueError("fixed-point evaluation requires a point of the acted projective space")
        selected = self._normalized_projective_coordinates(point)
        for group_element in self.acting_group():
            image = self.scheme_action_of(group_element).image_of_point(point)
            if self._normalized_projective_coordinates(image) != selected:
                return False
        return True

    @cached_method
    def fixed_point_fiber_evaluation(self, point):
        r"""Return the equivariant evaluation ``H^0(P,L) -> L|_p`` at a fixed point."""
        if not self.point_is_fixed(point):
            raise ValueError("equivariant fiber evaluation requires a fixed point")
        source = self.section_group_module()
        sections = source.unacted_module()
        evaluation = self.line_bundle().jet_evaluation(point, 1)
        fiber = evaluation.codomain()
        base = fiber.base_ring()
        group_algebra = source.group_algebra()
        target = Modules(group_algebra)(
            fiber,
            lambda group_element, vector: fiber.scalar_multiple(
                self.character_value(group_element),
                vector,
            ),
        )
        images = {
            label: target.equip_action_morphism()(
                evaluation(sections.module_generator(label))
            )
            for label in source.module_generating_set()
        }
        return source.Mor(target)(images)

    def twist(self, character):
        return type(self)(
            self.line_bundle(),
            self.scheme_action_functor(),
            lambda group_element: self.character_value(group_element)
            * self.section_scheme().scheme_base_ring()(character(group_element)),
        )

    def _repr_(self) -> str:
        return f"Linearization of {self.line_bundle()} by {self.acting_group()}"



class _ProductProjectiveLineBundleLinearization(_ProjectiveLineBundleLinearization):
    r"""A C2 coordinate linearization of ``O(d_1,...,d_r)`` on a projective product.

    The scheme action stores the scalar weight of every homogeneous coordinate.
    The induced action on a monomial section is the product of those weights to
    its exponent vector, followed by the selected character twist.  Thus the
    eigenspace decomposition is obtained from the represented action on the
    common group-module owner rather than from a dimension formula.
    """

    def __init__(self, line_bundle, scheme_action_functor, character) -> None:
        from dzack_research.preamble.categories.divisors.invertible_sheaves import (
            ProductProjectiveLineBundle,
        )

        if not isinstance(line_bundle, ProductProjectiveLineBundle):
            raise TypeError("this linearization requires multiprojective O(d_1,...,d_r)")
        scheme = line_bundle.projective_product()
        base = scheme.scheme_base_ring()
        if not isinstance(scheme_action_functor, GroupActionFunctor):
            raise TypeError("a multiprojective linearization requires an actual BG -> Schemes action functor")
        group = scheme_action_functor.group()
        if scheme_action_functor.codomain() != Schemes(base):
            raise ValueError("the multiprojective action functor has the wrong scheme category")
        if scheme_action_functor.underlying_object() is not scheme:
            raise ValueError("the multiprojective action functor acts on a different scheme")
        assert int(group.order()) == 2, (
            "the represented coordinate-weight specialization is the C2 action"
        )
        construction = getattr(
            scheme_action_functor,
            "_preamble_product_projective_coordinate_action_construction",
            None,
        )
        if not isinstance(construction, _ProductProjectiveCoordinateActionConstruction):
            raise ValueError("the product action must retain its coordinate construction data")
        weights = construction.coordinate_weights()
        if weights is None or weights.index_set() is not scheme.factors().index_set():
            raise ValueError("the product action must retain coordinate weights on the exact factor index set")
        self._line_bundle = line_bundle
        self._scheme_action_functor = scheme_action_functor
        self._coordinate_action_construction = construction
        self._group = group
        self._character = character
        self._validate_character()

    def projective_product(self):
        return self.line_bundle().projective_product()

    def section_scheme(self):
        return self.projective_product()

    def coordinate_action_construction(self):
        return self._coordinate_action_construction

    def coordinate_weights(self):
        return self.coordinate_action_construction().coordinate_weights()

    def local_chart_automorphism(self, group_element, chart_index):
        group_element = self.acting_group()(group_element)
        atlas = self.projective_product().standard_affine_atlas()
        chart_index = atlas.normalize_chart_index(chart_index)
        if group_element == self.acting_group().one():
            return atlas.chart(chart_index).categorical_identity_morphism()
        return self.coordinate_action_construction().local_automorphism(chart_index)

    def local_jacobian_scalar(self, group_element, chart_index):
        r"""Return the determinant of the diagonal action on affine chart coordinates."""
        group_element = self.acting_group()(group_element)
        base = self.section_scheme().scheme_base_ring()
        if group_element == self.acting_group().one():
            return base.one()
        atlas = self.projective_product().standard_affine_atlas()
        chart_index = atlas.normalize_chart_index(chart_index)
        choice = chart_index
        factors = self.projective_product().factors()
        labels = tuple(factors.index_set())
        result = base.one()
        for position, label in enumerate(labels):
            selected = choice[position]
            weights = self.coordinate_weights()[label]
            other = 1 - int(selected)
            result *= base(weights[other]) * base(weights[selected]).inverse_of_unit()
        return result

    @cached_method
    def section_action_of(self, group_element):
        group_element = self.acting_group()(group_element)
        sections = self.line_bundle().global_sections()
        base = sections.base_ring()
        scalar_twist = self.character_value(group_element)
        if group_element == self.acting_group().one():
            return sections.Mor(sections).elementwise(
                lambda section: sections.scalar_multiple(scalar_twist, section),
                verify_linearity=False,
            )
        exponents = sections._preamble_multihomogeneous_exponents
        factor_labels = tuple(self.projective_product().factors().index_set())
        weights = self.coordinate_weights()
        images = {}
        for monomial in sections.module_generating_set():
            weight = base.one()
            for factor_label, block in zip(factor_labels, exponents[monomial], strict=True):
                factor_weights = weights[factor_label]
                for coordinate_weight, exponent in zip(factor_weights, block, strict=True):
                    if exponent:
                        weight *= base(coordinate_weight) ** int(exponent)
            images[monomial] = sections.scalar_multiple(
                scalar_twist * weight,
                sections.module_generator(monomial),
            )
        return sections.Mor(sections)(images)

    def coherent_cohomology_group_module(self, degree):
        r"""Return the represented action on ``H^0`` of this multiprojective line bundle."""
        degree = int(degree)
        if degree < 0:
            raise ValueError("a coherent cohomology degree is nonnegative")
        assert degree == 0, (
            "higher multiprojective coherent cohomology actions belong to the general product-projective cohomology owner"
        )
        return self.section_group_module()


@cached_function(
    key=lambda projective_product, group=None: (
        id(projective_product),
        id(OwnedGroups().C(2) if group is None else group),
    )
)
def _c2_diagonal_product_projective_action(projective_product, group=None):
    r"""Return the diagonal sign action ``[x0:x1] |-> [x0:-x1]`` on every P1 factor."""
    base = projective_product.scheme_base_ring()
    factors = projective_product.factors()
    indices = factors.index_set()
    for label in indices:
        if int(factors[label].relative_dimension()) != 1:
            raise TypeError("the diagonal sign action is represented here on products of projective lines")
    group = OwnedGroups().C(2) if group is None else group
    if int(group.order()) != 2:
        raise ValueError("the diagonal sign action requires a group of order two")
    weights = finite_indexed_family(
        indices,
        lambda _label: (base.one(), -base.one()),
        name="Homogeneous coordinate weights of the diagonal sign action",
    )
    factor_automorphisms = {}
    for label in indices:
        factor = factors[label]
        ring = factor.O(1).global_sections().homogeneous_coordinate_ring()
        coordinate_labels = tuple(ring.algebra_generating_set())
        coordinates = tuple(ring.algebra_generator(name) for name in coordinate_labels)
        factor_automorphisms[label] = factor.projective_morphism_from_coordinates(
            factor,
            (coordinates[0], -coordinates[1]),
        )
    nontrivial = projective_product.from_product_cone(
        indexed_family(
            indices,
            lambda label: factor_automorphisms[label] * projective_product.projection(label),
            name="Factor legs of the diagonal sign involution",
        )
    )
    atlas = projective_product.standard_affine_atlas()
    positions = {label: position for position, label in enumerate(tuple(indices))}
    local_automorphisms = {}
    for choice in atlas.chart_indices():
        chart = atlas.chart(choice)
        local_factors = chart.factors()
        local_factor_automorphisms = {}
        for label in indices:
            factor_chart = local_factors[label]
            algebra = factor_chart.coordinate_algebra()
            coordinate_label = next(iter(algebra.algebra_generating_set()))
            coordinate = algebra.algebra_generator(coordinate_label)
            selected = int(choice[positions[label]])
            other = 1 - selected
            factor_weights = weights[label]
            scalar = base(factor_weights[other]) * base(factor_weights[selected]).inverse_of_unit()
            local_factor_automorphisms[label] = _affine_morphism_from_pullback(
                factor_chart,
                factor_chart,
                algebra.Mor(algebra)({coordinate_label: algebra(scalar) * coordinate}),
            )
        local_automorphisms[choice] = chart.from_product_cone(
            indexed_family(
                indices,
                lambda label, chart=chart: (
                    local_factor_automorphisms[label] * chart.projection(label)
                ),
                name="Affine factor legs of the diagonal sign involution",
            )
        )

    identity = projective_product.categorical_identity_morphism()
    action = GroupActionFunctor(
        group,
        Schemes(base),
        projective_product,
        lambda element: identity if element == group.one() else nontrivial,
    )
    action._preamble_product_projective_coordinate_action_construction = (
        _ProductProjectiveCoordinateActionConstruction(
            weights,
            finite_indexed_family(
                atlas.chart_index_set(),
                lambda index: local_automorphisms[index],
                name="Affine-chart automorphisms of the diagonal sign action",
            ),
        )
    )
    return action



@cached_function(key=lambda projective_line, group=None: (id(projective_line), id(OwnedGroups().C(2) if group is None else group)))
def _projective_line_coordinate_swap_action(projective_line, group=None):
    r"""Return the ``C2`` action on ``P^1`` interchanging its two coordinates."""
    base = projective_line.scheme_base_ring()
    if int(projective_line.relative_dimension()) != 1:
        raise TypeError("the coordinate-swap action is defined on a projective line")
    group = OwnedGroups().C(2) if group is None else group
    if int(group.order()) != 2:
        raise ValueError("the coordinate-swap action requires a group of order two")
    ring = projective_line.O(1).global_sections().homogeneous_coordinate_ring()
    labels = tuple(ring.algebra_generating_set())
    if len(labels) != 2:
        raise ArithmeticError("a projective line has two homogeneous coordinates")
    left = ring.algebra_generator(labels[0])
    right = ring.algebra_generator(labels[1])
    identity = projective_line.projective_morphism_from_coordinates(
        projective_line,
        (left, right),
    )
    swap = projective_line.projective_morphism_from_coordinates(
        projective_line,
        (right, left),
    )
    return GroupActionFunctor(
        group,
        Schemes(base),
        projective_line,
        lambda group_element: identity if group_element == group.one() else swap,
    )



__all__ = []
