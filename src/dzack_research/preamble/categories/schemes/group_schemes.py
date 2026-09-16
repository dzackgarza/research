r"""Affine group schemes and their actions over an affine base.

A group scheme over ``S`` is a scheme ``G/S`` with multiplication, unit, and
inverse scheme morphisms satisfying the group diagrams.  An action on ``X/S``
is a morphism ``G x_S X -> X`` satisfying the associativity and unit diagrams;
equivariant morphisms are exactly the scheme maps for which the usual action
square commutes.  This is the scheme-valued notion of Stacks Project, Tags
022S and 022Z.  It is intentionally distinct from ``GObjects(G, Schemes(R))``:
the latter is an action of an abstract group through a functor ``BG -> Sch_R``.
"""

from sage.categories.morphism import Morphism
from sage.misc.classcall_metaclass import typecall
from sage.structure.parent import Parent

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalHomset,
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import OwnedCategory
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedCategoryOverBaseRing,
    _own_ring,
)
from dzack_research.preamble.categories.schemes.schemes import (
    AffineSchemes,
    ProductSchemes,
    Schemes,
    _affine_morphism_from_pullback,
)


def _product_has_factors(product, factors) -> bool:
    if product not in ProductSchemes(factors[0].scheme_base_ring()):
        return False
    actual = tuple(product.factors())
    return len(actual) == len(factors) and all(
        left is right for left, right in zip(actual, factors, strict=True)
    )


def _map_to_product(product, legs):
    return product.from_product_cone(tuple(legs))


class AffineGroupSchemeHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return AffineGroupSchemeHomset


class AffineGroupSchemes(OwnedCategoryOverBaseRing):
    r"""Affine group schemes over ``Spec(R)``, represented by their structure maps."""

    def super_categories(self):
        return [AffineSchemes(self.base_ring())]

    def _repr_object_names(self):
        return f"affine group schemes over {self.base_ring()}"

    def _call_(self, scheme, multiplication, unit, inverse):
        return AffineGroupScheme(
            self,
            scheme,
            multiplication,
            unit,
            inverse,
        )

    def roots_of_unity(self, degree: int):
        r"""Return the affine group scheme ``mu_degree`` over this base."""
        return _roots_of_unity_group_scheme(self.base_ring(), degree)

    def an_object(self):
        return self.roots_of_unity(1)

    _HomCategory = AffineGroupSchemeHomCategoryConstruction


class AffineGroupScheme(Parent):
    r"""One affine group scheme with actual scheme-theoretic structure morphisms."""

    def __init__(self, category, scheme, multiplication, unit, inverse) -> None:
        self._scheme = scheme
        self._multiplication = multiplication
        self._unit = unit
        self._inverse = inverse
        base = category.base_ring()
        if scheme not in AffineSchemes(base):
            raise TypeError("an affine group scheme requires an affine scheme over its base")
        square = multiplication.domain()
        if not _product_has_factors(square, (scheme, scheme)) or multiplication.codomain() is not scheme:
            raise ValueError("group multiplication must be a morphism G x_S G -> G")
        if unit.codomain() is not scheme:
            raise ValueError("the group-scheme unit must land in G")
        if inverse.domain() is not scheme or inverse.codomain() is not scheme:
            raise ValueError("the group-scheme inverse must be a morphism G -> G")
        if unit.domain() is not scheme.base_scheme():
            raise ValueError("the group-scheme unit must start at the represented base scheme")
        self._verify_group_diagrams()
        Parent.__init__(self, category=category)

    def scheme(self):
        return self._scheme

    underlying_scheme = scheme

    def base_ring(self):
        return self.category().base_ring()

    def base_scheme(self):
        return self.unit_morphism().domain()

    def multiplication(self):
        return self._multiplication

    def unit_morphism(self):
        return self._unit

    def inverse_morphism(self):
        return self._inverse

    def _verify_group_diagrams(self) -> None:
        group = self.scheme()
        multiplication = self.multiplication()
        square = multiplication.domain()
        triple = group.scheme_category().product((group, group, group))
        first, second, third = triple.projections()

        first_pair = _map_to_product(square, (first, second))
        second_pair = _map_to_product(square, (second, third))
        first_product = multiplication * first_pair
        second_product = multiplication * second_pair
        multiply_first = multiplication * _map_to_product(square, (first_product, third))
        multiply_second = multiplication * _map_to_product(square, (first, second_product))
        if multiply_first != multiply_second:
            raise ValueError("group-scheme multiplication is not associative")

        identity = group.categorical_identity_morphism()
        structure = group.structure_morphism()
        unit_on_group = self.unit_morphism() * structure
        left_unit = multiplication * _map_to_product(square, (unit_on_group, identity))
        right_unit = multiplication * _map_to_product(square, (identity, unit_on_group))
        if left_unit != identity or right_unit != identity:
            raise ValueError("group-scheme multiplication does not satisfy the unit laws")

        inverse = self.inverse_morphism()
        target_unit = unit_on_group
        left_inverse = multiplication * _map_to_product(square, (inverse, identity))
        right_inverse = multiplication * _map_to_product(square, (identity, inverse))
        if left_inverse != target_unit or right_inverse != target_unit:
            raise ValueError("group-scheme inverse does not satisfy the inverse laws")

    def actions(self):
        return AffineGroupSchemeActions(self)

    def Mor(self, target):
        return self.category().Mor(self, target)

    def _repr_(self):
        return f"Affine group scheme on {self.scheme()}"


class AffineGroupSchemeMorphism(Morphism):
    r"""A scheme morphism preserving affine group-scheme multiplication."""

    def __init__(self, parent, arrow) -> None:
        Morphism.__init__(self, parent)
        self._arrow = arrow

    def underlying_arrow(self):
        return self._arrow

    def __mul__(self, other):
        if not isinstance(other, AffineGroupSchemeMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            self.underlying_arrow() * other.underlying_arrow()
        )

    def _repr_(self):
        return f"Group-scheme morphism from {self.domain()} to {self.codomain()}"


class AffineGroupSchemeHomset(CategoricalHomset):
    r"""Morphisms of affine group schemes over one represented base."""

    Element = AffineGroupSchemeMorphism

    def _element_constructor_(self, arrow):
        source = self.domain()
        target = self.codomain()
        schemes = Schemes(source.base_ring())
        arrow = schemes.Mor(source.scheme(), target.scheme())(arrow)

        source_square = source.multiplication().domain()
        target_square = target.multiplication().domain()
        first, second = source_square.projections()
        arrow_times_arrow = _map_to_product(
            target_square,
            (arrow * first, arrow * second),
        )
        if arrow * source.multiplication() != target.multiplication() * arrow_times_arrow:
            raise ValueError("the scheme morphism does not preserve group-scheme multiplication")
        if arrow * source.unit_morphism() != target.unit_morphism():
            raise ValueError("the scheme morphism does not preserve the group-scheme unit")
        if arrow * source.inverse_morphism() != target.inverse_morphism() * arrow:
            raise ValueError("the scheme morphism does not preserve the group-scheme inverse")
        return self.element_class(self, arrow)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to a group-scheme endomorphism Hom")
        return self(self.domain().scheme().categorical_identity_morphism())


_ACTION_CATEGORIES = {}


class AffineGroupSchemeActionHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return AffineGroupSchemeActionHomset


class AffineGroupSchemeActions(CategoryPacketMethods, OwnedCategory):
    r"""Affine schemes over the same base with an action of one affine group scheme."""

    @staticmethod
    def __classcall__(cls, group_scheme):
        key = id(group_scheme)
        cached = _ACTION_CATEGORIES.get(key)
        if cached is not None and cached.group_scheme() is group_scheme:
            return cached
        category = typecall(cls, group_scheme)
        _ACTION_CATEGORIES[key] = category
        return category

    def __init__(self, group_scheme) -> None:
        self._group_scheme = group_scheme
        OwnedCategory.__init__(self)

    def group_scheme(self):
        return self._group_scheme

    def super_categories(self):
        return [AffineSchemes(self.group_scheme().base_ring())]

    def _repr_object_names(self):
        return f"affine schemes acted on by {self.group_scheme()}"

    def _call_(self, scheme, action_morphism):
        return AffineGroupSchemeAction(self, scheme, action_morphism)

    def an_object(self):
        group = self.group_scheme()
        base = group.base_scheme()
        product = base.scheme_category().product((group.scheme(), base))
        action = product.projection(1)
        return self(base, action)

    _HomCategory = AffineGroupSchemeActionHomCategoryConstruction


class AffineGroupSchemeAction(Parent):
    r"""An affine ``G``-scheme represented by ``a: G x_S X -> X``."""

    def __init__(self, category, scheme, action_morphism) -> None:
        self._scheme = scheme
        self._action_morphism = action_morphism
        group = category.group_scheme()
        self._group_scheme = group
        base = group.base_ring()
        if scheme not in AffineSchemes(base):
            raise TypeError("an affine group-scheme action requires an affine scheme over the group base")
        if scheme.base_scheme() is not group.base_scheme():
            raise ValueError("the group scheme and acted scheme must have the same represented base")
        product = action_morphism.domain()
        if not _product_has_factors(product, (group.scheme(), scheme)):
            raise ValueError("a group-scheme action must have domain G x_S X")
        if action_morphism.codomain() is not scheme:
            raise ValueError("a group-scheme action must land in X")
        self._verify_action_diagrams()
        Parent.__init__(self, category=category)

    def scheme(self):
        return self._scheme

    underlying_scheme = scheme

    def group_scheme(self):
        return self._group_scheme

    def action_morphism(self):
        return self._action_morphism

    def _verify_action_diagrams(self) -> None:
        group = self.group_scheme()
        group_scheme = group.scheme()
        scheme = self.scheme()
        action = self.action_morphism()
        group_times_scheme = action.domain()
        triple = group_scheme.scheme_category().product((group_scheme, group_scheme, scheme))
        first, second, point = triple.projections()

        group_square = group.multiplication().domain()
        multiplied = group.multiplication() * _map_to_product(
            group_square,
            (first, second),
        )
        via_multiplication = action * _map_to_product(
            group_times_scheme,
            (multiplied, point),
        )
        inner_action = action * _map_to_product(
            group_times_scheme,
            (second, point),
        )
        via_action = action * _map_to_product(
            group_times_scheme,
            (first, inner_action),
        )
        if via_multiplication != via_action:
            raise ValueError("the group-scheme action is not associative")

        identity = scheme.categorical_identity_morphism()
        unit_on_scheme = group.unit_morphism() * scheme.structure_morphism()
        via_unit = action * _map_to_product(
            group_times_scheme,
            (unit_on_scheme, identity),
        )
        if via_unit != identity:
            raise ValueError("the group-scheme unit does not act as the identity")

    def Mor(self, target):
        return self.category().Mor(self, target)

    def _repr_(self):
        return f"{self.scheme()} with action of {self.group_scheme()}"


class AffineGroupSchemeEquivariantMorphism(Morphism):
    r"""A scheme morphism commuting with one affine group-scheme action."""

    def __init__(self, parent, arrow) -> None:
        Morphism.__init__(self, parent)
        self._arrow = arrow

    def underlying_arrow(self):
        return self._arrow

    def __mul__(self, other):
        if not isinstance(other, AffineGroupSchemeEquivariantMorphism):
            return NotImplemented
        if other.codomain() is not self.domain():
            return NotImplemented
        return other.domain().Mor(self.codomain())(
            self.underlying_arrow() * other.underlying_arrow()
        )

    def _repr_(self):
        return f"Equivariant morphism from {self.domain()} to {self.codomain()}"


class AffineGroupSchemeActionHomset(CategoricalHomset):
    r"""Equivariant morphisms between two actions of the same affine group scheme."""

    Element = AffineGroupSchemeEquivariantMorphism

    def __init__(self, family, domain, codomain) -> None:
        if domain.group_scheme() is not codomain.group_scheme():
            raise ValueError("an equivariant Hom requires one common acting group scheme")
        CategoricalHomset.__init__(self, family, domain, codomain)

    def _element_constructor_(self, arrow):
        source = self.domain().scheme()
        target = self.codomain().scheme()
        schemes = Schemes(self.domain().group_scheme().base_ring())
        arrow = schemes.Mor(source, target)(arrow)
        self.domain().group_scheme().scheme()
        source_product = self.domain().action_morphism().domain()
        target_product = self.codomain().action_morphism().domain()
        group_leg = source_product.projection(0)
        point_leg = source_product.projection(1)
        identity_times_arrow = _map_to_product(
            target_product,
            (group_leg, arrow * point_leg),
        )
        after_source_action = arrow * self.domain().action_morphism()
        before_target_action = self.codomain().action_morphism() * identity_times_arrow
        if after_source_action != before_target_action:
            raise ValueError("the scheme morphism is not equivariant for the group-scheme actions")
        return self.element_class(self, arrow)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity belongs to an equivariant endomorphism Hom")
        return self(self.domain().scheme().categorical_identity_morphism())


def _roots_of_unity_group_scheme(base_ring, degree: int):
    r"""Return ``mu_degree = Spec(R[u]/(u^degree - 1))`` over ``Spec(R)``.

    The construction is valid over every represented commutative base ring;
    no primitive root of unity and no invertibility hypothesis on ``degree`` is
    imposed.  The multiplication, unit, and inverse are the actual scheme maps
    dual to ``u |-> u_1 u_2``, ``u |-> 1``, and ``u |-> u^(degree-1)``.
    """
    if degree < 1:
        raise ValueError("mu_n requires n >= 1")
    base = _own_ring(base_ring)
    presentation = base.polynomial_ring("u")
    u_presentation = presentation.algebra_generator("u")
    algebra = (presentation).quotient_by_relations((u_presentation**degree - presentation.one(),),
    )
    u = algebra.algebra_generator("u")
    scheme = (algebra).affine_spectrum(base_ring=base)
    square = scheme.scheme_category().product((scheme, scheme))
    square_algebra = square.coordinate_algebra()
    first_pullback = square.projection(0).coordinate_algebra_morphism()
    second_pullback = square.projection(1).coordinate_algebra_morphism()
    multiplication_pullback = algebra.Mor(square_algebra)(
        {"u": first_pullback(u) * second_pullback(u)}
    )
    multiplication = _affine_morphism_from_pullback(
        square,
        scheme,
        multiplication_pullback,
    )

    base_scheme = scheme.structure_morphism().codomain()
    unit_pullback = algebra.Mor(base)({"u": base.one()})
    unit = _affine_morphism_from_pullback(base_scheme, scheme, unit_pullback)
    inverse_pullback = algebra.Mor(algebra)({"u": u ** (degree - 1)})
    inverse = _affine_morphism_from_pullback(scheme, scheme, inverse_pullback)
    return AffineGroupSchemes(base)(scheme, multiplication, unit, inverse)
