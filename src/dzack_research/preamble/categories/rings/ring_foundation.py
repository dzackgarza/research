"""Owned scalar hierarchy and the boundary to Sage computation rings."""

from functools import wraps

from sage.all import (
    ComplexField as _SageComplexField,
    FractionField as _SageFractionField,
    GF as _SageGF,
    PolynomialRing as _SagePolynomialRing,
    PowerSeriesRing as _SagePowerSeriesRing,
    Qp as _SageQp,
    RealField as _SageRealField,
    Zmod as _SageZmod,
    Zp as _SageZp,
    LaurentPolynomialRing as _SageLaurentPolynomialRing,
)
from sage.categories.category import Category
from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.principal_ideal_domains import PrincipalIdealDomains as SagePrincipalIdealDomains
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.ring import Ring
from sage.structure.element import Element, RingElement
from sage.structure.parent import Parent
from sage.structure.richcmp import richcmp
from sage.structure.sage_object import SageObject
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
    CategoricalHomset,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    AdditiveMonoids,
    Monoids,
    Semigroups,
)
from dzack_research.preamble.refine import refine


class RingMorphism(Morphism):
    r"""A unital ring morphism in the owned ring category."""

    def __init__(self, parent, function, *, engine_morphism=None) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError("a ring morphism requires an exact element map")
        self._function = function
        self._engine_morphism = engine_morphism

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def _engine_morphism_crossing(self):
        r"""Return the private engine realization when one was selected."""
        if self._engine_morphism is None:
            raise NotImplementedError("this ring morphism has no selected engine realization")
        return self._engine_morphism

    def __mul__(self, other):
        if not isinstance(other, RingMorphism) or other.codomain() is not self.domain():
            return NotImplemented
        return ring_homset(other.domain(), self.codomain()).elementwise(
            lambda element: self(other(element)),
        )

    def compose(self, before):
        result = self * before
        if result is NotImplemented:
            raise ValueError("the ring morphisms are not composable")
        return result

    def is_identity(self) -> bool:
        if self.domain() is not self.codomain():
            return False
        selected = getattr(self, "_preamble_is_identity", None)
        if selected is not None:
            return bool(selected)
        if self._engine_morphism is not None:
            try:
                return bool(self._engine_morphism.is_identity())
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
        return False



class RingHomset(CategoricalHomset):
    r"""The owned set ``Hom_Ring(A,B)``."""

    Element = RingMorphism

    def __init__(self, hom_family, domain, codomain) -> None:
        CategoricalHomset.__init__(self, hom_family, domain, codomain)

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def is_endomorphism_set(self):
        return self.domain() is self.codomain()

    def _element_constructor_(self, datum):
        if isinstance(datum, RingMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError("the ring morphism has the wrong source or target")
            if datum.parent() is self:
                return datum
            return self.elementwise(datum)
        if isinstance(datum, Map):
            source_engine = _engine_ring(self.domain())
            target_engine = _engine_ring(self.codomain())
            if _engine_ring(datum.domain()) is not source_engine:
                raise ValueError("the engine ring map has the wrong domain")
            if _engine_ring(datum.codomain()) is not target_engine:
                raise ValueError("the engine ring map has the wrong codomain")
            return self.element_class(
                self,
                lambda element: target_engine(datum(source_engine(element))),
                engine_morphism=datum,
            )
        if callable(datum):
            return self.elementwise(datum)
        raise TypeError("a ring morphism is supplied by an exact map or engine morphism")

    def elementwise(self, function):
        return self.element_class(self, function)

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError("identity is defined only on a ring endomorphism Hom-set")
        identity = self.elementwise(lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def _repr_(self):
        return f"Mor_Ring({self.domain()}, {self.codomain()})"


class RingHomCategoryConstruction(HomCategoryConstruction):
    r"""The owned family ``(A,B) |-> Hom_Ring(A,B)``."""

    def fixed_category_class(self):
        return RingHomset


def ring_homset(domain, codomain) -> RingHomset:
    r"""Return the canonical owned ``Hom_Ring(domain,codomain)`` object."""
    return OwnedRings().Mor(domain, codomain)


def ring_morphism(domain, codomain, function, *, engine_morphism=None) -> RingMorphism:
    r"""Construct one owned ring morphism with an optional engine realization."""
    return RingMorphism(
        ring_homset(domain, codomain),
        function,
        engine_morphism=engine_morphism,
    )

class PredicateSubrings(OwnedCategory):
    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def ambient_ring(self):
            return self._ambient_ring

        def defining_predicate(self):
            return self._predicate

        def __contains__(self, element):
            if element not in self._ambient_ring:
                return False
            answer = self._predicate(element)
            if answer is True or answer is False:
                return answer
            raise NotImplementedError(
                f"membership in {self} is not decided for {element}"
            )

        def _element_constructor_(self, element):
            try:
                candidate = self._ambient_ring(element)
            except (TypeError, ValueError):
                raise ValueError(
                    f"{element} is not in the ambient ring {self._ambient_ring}"
                ) from None
            if candidate not in self:
                raise ValueError(f"{candidate} does not satisfy {self._description}")
            return candidate

        def one(self):
            return self._one

        def zero(self):
            return self._zero

        def inclusion(self):
            return ring_morphism(
                self,
                self._ambient_ring,
                lambda element: element,
            )

        def _repr_(self):
            return f"{{z in {self._ambient_ring} : {self._description}}}"


class _PredicateSubringParent(Parent):
    def __init__(self, ambient_ring, predicate, description, category):
        if ambient_ring not in SageRings() and ambient_ring not in OwnedRings():
            raise TypeError(f"{ambient_ring} is not a ring")
        self._ambient_ring = ambient_ring
        self._predicate = predicate
        self._description = description
        self._one = ambient_ring.one()
        self._zero = ambient_ring.zero()
        Parent.__init__(self, facade=ambient_ring, category=category)
        refine(self, category)

    def __call__(self, element):
        r"""Construct an element of the predicate subring directly."""
        return self._element_constructor_(element)

    def _element_constructor_(self, element):
        try:
            candidate = self._ambient_ring(element)
        except (TypeError, ValueError):
            raise ValueError(f"{element} is not in the ambient ring {self._ambient_ring}") from None
        if candidate not in self:
            raise ValueError(f"{candidate} does not satisfy {self._description}")
        return candidate

    def __contains__(self, element):
        try:
            candidate = self._ambient_ring(element)
        except (TypeError, ValueError):
            return False
        answer = self._predicate(candidate)
        if answer is True or answer is False:
            return answer
        raise NotImplementedError(
            f"membership in {self} is not decided for {candidate}"
        )


def predicate_subring(ambient_ring, predicate, description, category=None):
    placement = PredicateSubrings()
    if category is not None:
        placement = Category.join((placement, category))
    return _PredicateSubringParent(
        ambient_ring,
        predicate,
        description,
        placement,
    )

class OwnedSemirings(OwnedCategory):
    """Semirings on the owned operation spine."""

    def super_categories(self):
        return [Monoids(), AdditiveMonoids()]


class OwnedRngs(OwnedCategory):
    """Rngs on the owned operation spine."""

    def super_categories(self):
        return [Semigroups(), AdditiveGroups()]


class OwnedRings(CategoryPacketMethods, OwnedCategory):
    """Unital rings whose notebook-facing ring interface is owned here."""

    _HomCategory = RingHomCategoryConstruction

    def super_categories(self):
        return [OwnedSemirings(), OwnedRngs()]

    def mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a ring Hom requires two owned rings")
        return ring_homset(domain, codomain)

    class ParentMethods:
        def Mor(self, codomain, category=None):
            rings = OwnedRings()
            if category is None or (
                isinstance(category, OwnedCategory) and category.is_subcategory(rings)
            ):
                return rings.Mor(self, codomain)
            # A Sage category here is not a mathematical request: it is Sage's
            # coercion machinery asking for somewhere to keep a conversion map,
            # naming its own `SetsWithPartialMaps`.  `SageHom` would check that
            # this owned ring lies in that Sage category, which it does not and
            # need not (`ARC-00`).  Build the homset directly at the engine
            # boundary instead, without the membership check.
            from sage.categories.homset import Homset

            return Homset(self, codomain, category=category, check=False)

        def _Hom_(self, codomain, category=None):
            rings = OwnedRings()
            if codomain not in rings:
                raise TypeError("a ring Hom requires two owned rings")
            if category is not None and not category.is_subcategory(rings):
                raise TypeError("this is not a ring homset category")
            return ring_homset(self, codomain)

        def cardinality(self):
            r"""Return the exact represented cardinal of the underlying set."""
            from dzack_research.preamble.categories.sets.set_categories import (
                CountablyInfiniteSets,
                FiniteSets,
                UncountableSets,
            )
            from dzack_research.preamble.categories.sets.cardinals import (
                aleph0,
                cardinal,
                continuum,
            )

            category = self.category()
            if category.is_subcategory(FiniteSets()):
                from sage.rings.integer_ring import ZZ as SageZZ
                integers = _own_ring(SageZZ)
                return cardinal(
                    integers._from_engine_element(
                        SageZZ(_engine_ring(self).cardinality())
                    )
                )
            if category.is_subcategory(CountablyInfiniteSets()):
                return aleph0
            if category.is_subcategory(UncountableSets()):
                return continuum
            raise NotImplementedError(
                f"the exact cardinality of the underlying set of {self} is not represented"
            )

        def _has_selected_exact_coefficient_presentation(self) -> bool:
            r"""Return whether this ring carries a nontrivial selected exact presentation.

            Module algorithms use this capability without knowing which higher
            mathematical structure supplied the presentation.
            """
            return False

        def _exact_coefficient_presentation_ring(self):
            r"""Return the owned ring in which coefficient computations are lifted."""
            return self

        def _exact_coefficient_presentation_relations(self):
            r"""Return the selected coefficient relations in the computation ring."""
            from dzack_research.preamble.categories.sets.finite_ordered_sets import (
                finite_ordered_set,
            )

            return finite_ordered_set(())

        def _lift_coefficient_to_presentation(self, value):
            return self(value)

        def _descend_coefficient_from_presentation(self, value):
            return self(value)

        def is_central(self, element):
            r"""Return whether ``element`` is central when this is decidable here."""
            if element not in self:
                return False
            if self in OwnedCommutativeRings():
                return True
            from dzack_research.preamble.categories.algebras.algebras import (
                FramedAlgebras,
            )

            if self not in FramedAlgebras(self.base_ring()):
                raise NotImplementedError(
                    f"{self} has no chosen algebra generating set from which "
                    "centrality can be decided"
                )
            return all(
                element * self.algebra_generator(label)
                == self.algebra_generator(label) * element
                for label in self.algebra_generating_set()
            )

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):
            r"""Return the canonical ring map \(R\to Z(R)\) when it is the identity."""
            if self not in OwnedCommutativeRings():
                raise TypeError(
                    f"{self} is noncommutative, so the identity does not land "
                    "in its center"
                )
            center = self.ring_center()
            return ring_morphism(self, center, lambda scalar: scalar)

        def algebra_structure_morphism(self):
            r"""The structure morphism of this ring as an algebra over itself.

            For a commutative ring this is the identity \(R\to R\).
            """
            return self._ring_morphism_defining_algebra_structure()

        @cached_method
        def ring_center(self):
            r"""Return the centre ``Z(R)`` as a predicate-defined subring."""
            if self in OwnedCommutativeRings():
                return self
            return predicate_subring(
                self,
                self.is_central,
                "z commutes with every element",
                OwnedCommutativeRings(),
            )

        def fraction_field(self):
            r"""Return the fraction field through the computation ring."""
            if self in OwnedFields():
                return self
            return _own_ring(_engine_ring(self).fraction_field())

class OwnedCommutativeRings(OwnedCategory):
    r"""Commutative unital rings in the owned mathematical graph."""

    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def is_commutative(self):
            return True


class OwnedOrderedRings(OwnedCategory):
    r"""Totally ordered rings in the owned scalar hierarchy."""

    def super_categories(self):
        return [OwnedRings()]

    class ElementMethods:
        def __abs__(self):
            zero = self.parent().zero()
            return self if self >= zero else -self


class OwnedIntegralDomains(OwnedCategory):
    r"""Commutative rings without zero divisors."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_integral_domain(self, *args, **kwargs):
            return True


class OwnedPrincipalIdealDomains(OwnedCategory):
    r"""Principal ideal domains in the owned ring hierarchy."""

    def super_categories(self):
        return [OwnedIntegralDomains(), OwnedNoetherianRings()]


def _engine_krull_dimension(ring):
    engine = _engine_ring(ring)
    method = getattr(engine, "krull_dimension", None)
    if method is None:
        raise NotImplementedError(f"Krull dimension of {ring} has no active backend")
    return method()


class OwnedNoetherianRings(OwnedCategory):
    r"""Noetherian commutative rings."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_noetherian(self):
            return True

        def krull_dimension(self):
            return _engine_krull_dimension(self)


class OwnedArtinianRings(OwnedCategory):
    r"""Artinian commutative rings."""

    def super_categories(self):
        return [OwnedNoetherianRings()]

    class ParentMethods:
        def is_artinian(self):
            return True


class OwnedLocalRings(OwnedCategory):
    r"""Commutative rings equipped with their unique maximal ideal."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_local(self):
            return True

        def maximal_ideal(self):
            return self._preamble_maximal_ideal

        def residue_field(self):
            return self._preamble_residue_field

        def residue_map(self):
            r"""Return the represented local quotient map ``R -> kappa(m)``."""
            morphism = getattr(self, "_preamble_residue_map", None)
            if morphism is not None:
                return morphism
            if self.residue_field() is self:
                return ring_homset(self, self).identity()
            raise NotImplementedError(f"the residue map of {self} is not represented")

        def fraction_field(self):
            represented = getattr(self, "_preamble_fraction_field", None)
            if represented is not None:
                return represented
            return super().fraction_field()


class OwnedAdicallyCompleteRings(OwnedCategory):
    r"""Commutative rings represented as complete for a chosen adic topology."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_adically_complete(self):
            return True

        def ideal_of_definition(self):
            return self._preamble_ideal_of_definition


class OwnedCompleteLocalRings(OwnedCategory):
    r"""Local rings complete for the represented maximal-ideal/adic topology."""

    def super_categories(self):
        return [OwnedLocalRings(), OwnedAdicallyCompleteRings()]

class OwnedDivisionRings(OwnedCategory):
    def super_categories(self):
        return [OwnedRings()]


class OwnedFields(OwnedCategory):
    def super_categories(self):
        return [
            OwnedDivisionRings(),
            OwnedIntegralDomains(),
            OwnedPrincipalIdealDomains(),
            OwnedNoetherianRings(),
            OwnedArtinianRings(),
            OwnedLocalRings(),
        ]

    class ParentMethods:
        def maximal_ideal(self):
            return _engine_ring(self).ideal(0)

        def residue_field(self):
            return self

        def residue_map(self):
            return ring_homset(self, self).identity()


class OwnedOrders(OwnedCategory):
    r"""Orders in number fields as a ring-theoretic property category."""

    def super_categories(self):
        return [
            OwnedIntegralDomains(),
            OwnedNoetherianRings(),
        ]

    class ParentMethods:
        def cardinality(self):
            from dzack_research.preamble.categories.sets.cardinals import aleph0

            return aleph0

        def is_maximal(self) -> bool:
            r"""Return whether this is the maximal order of its fraction field."""
            engine = _engine_ring(self)
            if engine is SageZZ:
                return True
            return bool(engine.is_maximal())


class PrimeFields(OwnedCategory):
    r"""Prime fields \(\mathbf F_p\)."""

    def super_categories(self):
        return [OwnedFields()]


class OwnedCategoryOverBaseRing(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""A category over a ring, normalized to the session's owned ring."""

    @staticmethod
    def __classcall__(cls, base_ring, *args, **kwargs):
        base_ring = _owned_ring(base_ring)
        return OwnedParameterizedCategory.__classcall__(
            cls,
            base_ring,
            *args,
            **kwargs,
        )

    def base_ring(self):
        return self.base()

    def __contains__(self, candidate) -> bool:
        try:
            return self in candidate.category().all_super_categories(proper=False)
        except (AttributeError, TypeError, ValueError):
            return False


class _OwnedRingElement(RingElement):
    r"""An element of an owned ring with a private backend realization."""

    def __init__(self, parent, backend_value) -> None:
        RingElement.__init__(self, parent)
        self._backend_value = backend_value

    def _backend(self):
        r"""Return the private backend value for boundary code in this module."""
        return self._backend_value

    def _add_(self, other):
        parent = self.parent()
        return parent._from_engine_element(self._backend() + other._backend())

    def __add__(self, other):
        try:
            other = self.parent()(other)
        except (TypeError, ValueError):
            return NotImplemented
        return self._add_(other)

    __radd__ = __add__

    def __sub__(self, other):
        try:
            other = self.parent()(other)
        except (TypeError, ValueError):
            return NotImplemented
        return self._add_(-other)

    def __rsub__(self, other):
        try:
            other = self.parent()(other)
        except (TypeError, ValueError):
            return NotImplemented
        return other._add_(-self)

    def _mul_(self, other):
        parent = self.parent()
        return parent._from_engine_element(self._backend() * other._backend())

    def __mul__(self, other):
        other_parent = getattr(other, "parent", lambda: None)()
        if other_parent is not None and other_parent is not self.parent():
            try:
                if other_parent.base_ring() is self.parent():
                    return other_parent.scalar_multiple(self, other)
            except (AttributeError, TypeError, ValueError):
                return NotImplemented
        try:
            other = self.parent()(other)
        except (TypeError, ValueError):
            return NotImplemented
        return self._mul_(other)

    def __rmul__(self, other):
        try:
            other = self.parent()(other)
        except (TypeError, ValueError):
            return NotImplemented
        return self._mul_(other)

    def _neg_(self):
        return self.parent()._from_engine_element(-self._backend())

    def _richcmp_(self, other, op):
        if not isinstance(other, _OwnedRingElement) or other.parent() is not self.parent():
            try:
                other = self.parent()(other)
            except (TypeError, ValueError):
                return NotImplemented
        return richcmp(self._backend(), other._backend(), op)

    def __eq__(self, other):
        try:
            other = self.parent()(other)
        except (TypeError, ValueError):
            return False
        return bool(self._backend() == other._backend())

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((id(self.parent()), self._backend()))

    def __bool__(self):
        return bool(self._backend())

    def __int__(self):
        return int(self._backend())

    def __index__(self):
        return int(self._backend())

    def __float__(self):
        return float(self._backend())

    def __complex__(self):
        return complex(self._backend())

    def _repr_(self):
        return repr(self._backend())

    def _latex_(self):
        return str(latex(self._backend()))

    def is_zero(self):
        return bool(self._backend() == self.parent()._engine.zero())

    def is_one(self):
        return bool(self._backend() == self.parent()._engine.one())

    def is_unit(self):
        return bool(self._backend().is_unit())

    def inverse_of_unit(self):
        if not self.is_unit():
            raise ZeroDivisionError(f"{self} is not a unit")
        return self.parent()._from_engine_element(self._backend() ** -1)

    def __invert__(self):
        return self.parent()._from_engine_element(~self._backend())

    def __truediv__(self, other):
        other = self.parent()(other)
        value = self._backend() / other._backend()
        value_parent = getattr(value, "parent", lambda: None)()
        if value_parent is self.parent()._engine:
            return self.parent()._from_engine_element(value)
        if value_parent in SageRings():
            return _own_ring(value_parent)._from_engine_element(value)
        return value

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            try:
                modulus = self.parent()(modulus)
            except (TypeError, ValueError):
                return NotImplemented
            value = pow(self._backend(), exponent, modulus._backend())
        else:
            try:
                exponent = exponent.__index__()
            except AttributeError:
                return NotImplemented
            value = self._backend() ** exponent
        value_parent = getattr(value, "parent", lambda: None)()
        if value_parent is self.parent()._engine:
            return self.parent()._from_engine_element(value)
        if value_parent in SageRings():
            return _own_ring(value_parent)._from_engine_element(value)
        return value

    def __rtruediv__(self, other):
        try:
            numerator = self.parent()(other)
        except (TypeError, ValueError):
            return NotImplemented
        return numerator.__truediv__(self)

    def __floordiv__(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend() // other._backend())

    def __mod__(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend() % other._backend())

    def quo_rem(self, other):
        other = self.parent()(other)
        quotient, remainder = self._backend().quo_rem(other._backend())
        return (
            self.parent()._from_engine_element(quotient),
            self.parent()._from_engine_element(remainder),
        )

    def divides(self, other):
        other = self.parent()(other)
        return bool(self._backend().divides(other._backend()))

    def gcd(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend().gcd(other._backend()))

    def lcm(self, other):
        other = self.parent()(other)
        return self.parent()._from_engine_element(self._backend().lcm(other._backend()))

    def valuation(self, prime):
        prime = self.parent()(prime)
        integers = _own_ring(SageZZ)
        return integers._from_engine_element(
            SageZZ(self._backend().valuation(prime._backend()))
        )

    def prime_divisors(self):
        return tuple(
            self.parent()._from_engine_element(prime)
            for prime in self._backend().prime_divisors()
        )

    def is_prime(self):
        return bool(self._backend().is_prime())

    def factorial(self):
        return self.parent()._from_engine_element(self._backend().factorial())

    def is_square(self):
        return bool(self._backend().is_square())

    def sqrt(self):
        value = self._backend().sqrt()
        parent = getattr(value, "parent", lambda: None)()
        if parent in SageRings():
            return _own_ring(parent)._from_engine_element(value)
        return value

    def numerator(self):
        value = self._backend().numerator()
        parent = value.parent()
        return _own_ring(parent)._from_engine_element(value)

    def denominator(self):
        value = self._backend().denominator()
        parent = value.parent()
        return _own_ring(parent)._from_engine_element(value)

    def additive_order(self):
        value = self._backend().additive_order()
        return _own_ring(SageZZ)._from_engine_element(SageZZ(value))

    def multiplicative_order(self):
        value = self._backend().multiplicative_order()
        return _own_ring(SageZZ)._from_engine_element(SageZZ(value))

    def degree(self):
        value = self._backend().degree()
        return _own_ring(SageZZ)._from_engine_element(SageZZ(value))

    def trace(self):
        value = self._backend().trace()
        parent = getattr(value, "parent", lambda: None)()
        return _own_ring(parent)._from_engine_element(value) if parent in SageRings() else value

    def norm(self):
        value = self._backend().norm()
        parent = getattr(value, "parent", lambda: None)()
        return _own_ring(parent)._from_engine_element(value) if parent in SageRings() else value

    def minpoly(self):
        polynomial = self._backend().minpoly()
        return _own_ring(polynomial.parent())._from_engine_element(polynomial)


class _OwnedRingParent(UniqueRepresentation, Parent):
    r"""An owned ring parent with one private computational realization.

    The parent and its elements belong to the preamble universe.  ``engine``
    is implementation state only; raw backend elements enter through
    ``_from_engine_element`` and leave through ``_engine_element``.
    """

    Element = _OwnedRingElement

    def __init__(self, engine: Ring) -> None:
        self._engine = engine
        Parent.__init__(self, category=_owned_ring_category(engine))
        refine(self, self.category())

    def _from_engine_element(self, value):
        if getattr(value, "parent", lambda: None)() is not self._engine:
            value = self._engine(value)
        return self.element_class(self, value)

    def _engine_element(self, value):
        value = self(value)
        return value._backend()

    def __call__(self, value):
        r"""Construct an owned ring element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        parent = getattr(value, "parent", lambda: None)()
        if parent is self:
            return value
        if parent is not None:
            try:
                if parent in OwnedRings():
                    return self._from_engine_element(
                        self._engine(_engine_element(parent, value))
                    )
            except (TypeError, ValueError, AttributeError):
                pass
            if parent in SageRings() or parent is self._engine:
                raise TypeError(
                    "raw backend ring elements are not accepted by the public preamble API"
                )
        if isinstance(value, SageObject):
            raise TypeError(
                "raw backend objects are not accepted by the public preamble API"
            )
        return self._from_engine_element(self._engine(value))

    def __contains__(self, value) -> bool:
        return isinstance(value, self.element_class) and value.parent() is self

    def zero(self):
        return self._from_engine_element(self._engine.zero())

    def one(self):
        return self._from_engine_element(self._engine.one())

    def multiplicative_generator(self):
        generator = getattr(self._engine, "multiplicative_generator", None)
        if generator is None:
            raise AttributeError(f"{self} has no represented multiplicative generator")
        return self._from_engine_element(generator())

    def an_element(self):
        return self._from_engine_element(self._engine.an_element())

    def characteristic(self):
        integers = _own_ring(SageZZ)
        return integers._from_engine_element(SageZZ(self._engine.characteristic()))

    def is_exact(self):
        return self._engine.is_exact()

    def is_field(self, *args, **kwargs):
        return self._engine.is_field(*args, **kwargs)

    def is_commutative(self):
        return self._engine.is_commutative()

    def is_integral_domain(self, *args, **kwargs):
        return self._engine.is_integral_domain(*args, **kwargs)

    def is_finite(self):
        return self._engine.is_finite()

    def base_ring(self):
        base = self._engine.base_ring()
        if base is self._engine:
            return self
        return _own_ring(base) if base in SageRings() else base

    def variable_names(self):
        return self._engine.variable_names()

    def _first_ngens(self, n):
        return tuple(self._from_engine_element(value) for value in self._engine.gens()[:n])

    def _repr_(self):
        return repr(self._engine)

    def _latex_(self):
        return str(latex(self._engine))

def _owned_ring_category(engine: Ring) -> Category:
    """Return the strongest owned ring category witnessed by ``engine``."""
    category = engine.category()
    extra = []
    if category.is_subcategory(SageCommutativeRings()):
        extra.append(OwnedCommutativeRings())
    if category.is_subcategory(SageIntegralDomains()):
        extra.append(OwnedIntegralDomains())
    if engine is SageZZ or engine is SageQQ:
        extra.append(OwnedOrderedRings())
    if category.is_subcategory(SagePrincipalIdealDomains()):
        extra.append(OwnedPrincipalIdealDomains())
    try:
        noetherian = engine.is_noetherian()
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        noetherian = engine is SageZZ
    if noetherian is True or engine is SageZZ:
        extra.append(OwnedNoetherianRings())
    if category.is_subcategory(SageFields()):
        placement = OwnedFields()
    elif category.is_subcategory(SageDivisionRings()):
        placement = OwnedDivisionRings()
    else:
        placement = OwnedRings()
    joined = Category.join((placement, _owned_ring_size(engine), *extra))
    match engine:
        case SageNumberFieldOrder():
            return Category.join((joined, OwnedOrders()))
        case _:
            return joined


def _owned_ring_size(engine):
    r"""Return the exact Set-cardinality placement known from the engine kind."""
    from sage.categories.number_fields import NumberFields
    from sage.categories.sets_cat import Sets as SageSets
    from sage.rings.qqbar import QQbar as SageQQbar
    from dzack_research.preamble.categories.sets.set_categories import (
        CountablyInfiniteSets,
        FiniteSets,
        Sets,
        UncountableSets,
    )

    if engine.category().is_subcategory(SageSets().Finite()):
        return FiniteSets()
    if not engine.is_exact():
        return UncountableSets()
    if engine is SageZZ or engine is SageQQ or engine in NumberFields() or engine is SageQQbar:
        return CountablyInfiniteSets()
    return Sets()


def _own_if_ring(result):
    return _own_ring(result) if result in SageRings() else result


@cached_function
def _owned_engine_ring(engine: Ring) -> _OwnedRingParent:
    return _OwnedRingParent(engine)


def _own_ring(ring):
    r"""Private backend adapter: build the preamble ring represented by ``ring``."""
    if ring in OwnedRings():
        owned = ring
    else:
        if ring not in SageRings():
            raise TypeError(f"{ring} is not a ring")
        owned = _owned_engine_ring(ring)
    return owned


def _owned_ring(ring):
    r"""Return ``ring`` after asserting it already belongs to the preamble universe."""
    if ring not in OwnedRings():
        raise TypeError("this API expects a preamble ring")
    return ring


def _engine_ring(ring):
    r"""Return the Sage computation parent behind an owned ring."""
    represented = getattr(ring, "_preamble_engine_ring", None)
    if represented is not None:
        ring = represented
    # An owned view can stand over another owned view: an algebra view over a
    # ring view, say.  One unwrap would then still hand back an owned parent,
    # which is not an engine object at all, so the descent continues to the
    # Sage parent underneath.
    while True:
        if isinstance(ring, _OwnedRingParent):
            ring = ring._engine
            continue
        if isinstance(ring, _PredicateSubringParent):
            ring = ring._ambient_ring
            continue
        return ring


def _engine_element(ring, element):
    r"""Return the private computation-engine realization of ``element``.

    ``_engine_ring(R)`` identifies a currently selected CAS realization of the
    owned ring ``R``.  This companion crossing converts an element of the
    *owned* ring into that engine without asking the engine's coercion graph to
    know about the owned parent.  Quotients, localizations, completions, and
    future Julia/OSCAR-backed rings can therefore keep one public mathematical
    parent while changing computational realizations independently.
    """
    owned = _own_ring(ring)
    if isinstance(owned, _PredicateSubringParent):
        return _engine_element(owned._ambient_ring, owned(element))
    if getattr(element, "parent", lambda: None)() is owned:
        backend = getattr(element, "_backend", None)
        if callable(backend):
            return backend()
    converter = getattr(owned, "_engine_element", None)
    if converter is not None:
        return converter(element)
    engine = _engine_ring(owned)
    if engine is owned:
        return owned(element)
    return engine(element)


def _owning_constructor(constructor):
    @wraps(constructor)
    def construct(*args, **kwargs):
        result = constructor(*args, **kwargs)
        return _own_ring(result) if result in SageRings() else result

    return construct


def _constructor_over_ring(constructor):
    @wraps(constructor)
    def construct(base_ring, *args, **kwargs):
        result = constructor(_engine_ring(base_ring), *args, **kwargs)
        return _own_ring(result) if result in SageRings() else result

    return construct


def GF(*args, **kwargs):
    engine = _SageGF(*args, **kwargs)
    field = _own_ring(engine)
    if engine.degree() == 1:
        refine(field, PrimeFields())
    return field


FiniteField = GF


def PrimeField(characteristic):
    return GF(characteristic)


def Zmod(*args, **kwargs):
    return _own_ring(_SageZmod(*args, **kwargs))


IntegerModRing = Zmod
Integers = Zmod


def Qp(*args, **kwargs):
    return _own_ring(_SageQp(*args, **kwargs))


def RealField(*args, **kwargs):
    return _own_ring(_SageRealField(*args, **kwargs))


def ComplexField(*args, **kwargs):
    return _own_ring(_SageComplexField(*args, **kwargs))


Rings = OwnedRings
OrderedRings = OwnedOrderedRings
DivisionRings = OwnedDivisionRings
Fields = OwnedFields
CommutativeRings = OwnedCommutativeRings
IntegralDomains = OwnedIntegralDomains
PrincipalIdealDomains = OwnedPrincipalIdealDomains
NoetherianRings = OwnedNoetherianRings
ArtinianRings = OwnedArtinianRings
LocalRings = OwnedLocalRings
AdicallyCompleteRings = OwnedAdicallyCompleteRings
CompleteLocalRings = OwnedCompleteLocalRings
