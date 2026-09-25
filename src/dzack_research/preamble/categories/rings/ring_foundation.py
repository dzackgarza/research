"""Owned scalar hierarchy and the boundary to Sage computation rings."""

from abc import ABCMeta
from collections.abc import Mapping
from functools import wraps

from sage.all import (
    GF as _SageGF,
)
from sage.all import (
    ComplexField as _SageComplexField,
)
from sage.all import (
    Qp as _SageQp,
)
from sage.all import (
    RealField as _SageRealField,
)
from sage.all import (
    Zmod as _SageZmod,
)
from sage.arith.misc import (
    euler_phi as _engine_euler_phi,
)
from sage.arith.misc import (
    number_of_divisors as _engine_number_of_divisors,
)
from sage.categories.category import Category
from sage.categories.category_with_axiom import all_axioms
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.map import Map
from sage.categories.morphism import Morphism, SetMorphism
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.categories.principal_ideal_domains import (
    PrincipalIdealDomains as SagePrincipalIdealDomains,
)
from sage.categories.quotient_fields import QuotientFields as SageQuotientFields
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.misc.lazy_attribute import lazy_attribute
from sage.misc.repr import repr_lincomb
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.polynomial.multi_polynomial_ring_base import MPolynomialRing_base
from sage.rings.polynomial.polynomial_quotient_ring import PolynomialQuotientRing_generic
from sage.rings.polynomial.polynomial_ring import PolynomialRing_generic
from sage.rings.quotient_ring import QuotientRing_generic
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.ring import Ring
from sage.structure.element import CommutativeRingElement, RingElement, parent as element_parent
from sage.structure.parent import Parent
from sage.misc.unknown import Unknown
from sage.rings.qqbar import AA as SageAA
from sage.rings.finite_rings.finite_field_constructor import GF as SageGF
from sage.structure.richcmp import op_EQ, op_GE, op_GT, op_LE, op_LT, op_NE, richcmp
from sage.structure.sage_object import SageObject
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.abstract_categories.mor_categories import (
    CategoricalMor,
    CategoryPacketMethods,
    MorCategoryConstruction,
)
from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.rings.semirings import (
    OwnedRngs,
    OwnedSemirings,
    RingMorCategoryConstruction,
)
from dzack_research.preamble.categories import sets as owned_sets
from dzack_research.preamble.owned_category_bases import CategoryWithAxiom
from dzack_research.preamble.refine import realize_owned_category


class _OwnedRingBootstrapParent(metaclass=ABCMeta):
    r"""Declared parent types admitted while their owned ring category is built.

    This is a construction-time type contract only. Category membership is
    the mathematical classification once Parent initialization finishes; this
    virtual base exists solely for the self-referential interval before that
    membership can be asked without circularity.
    """


if "Noetherian" not in all_axioms:
    all_axioms.add("Noetherian")
if "Artinian" not in all_axioms:
    all_axioms.add("Artinian")
if "Local" not in all_axioms:
    all_axioms.add("Local")
if "PrincipalIdeals" not in all_axioms:
    all_axioms.add("PrincipalIdeals")
if "Prime" not in all_axioms:
    all_axioms.add("Prime")


class RingMorphism(Morphism):
    r"""A unital ring morphism in the owned ring category."""

    def __init__(self, parent, function, *, engine_morphism=None) -> None:
        Morphism.__init__(self, parent)
        if not callable(function):
            raise TypeError(
                f"a ring morphism {self.domain()} -> {self.codomain()} needs a map on elements, but "
                f"{function!r} is not callable"
            )
        self._function = function
        self._engine_morphism = engine_morphism
        self._preamble_is_identity = False

    def __call__(self, element):
        return self._call_(element)

    def _call_(self, element):
        return self.codomain()(self._function(self.domain()(element)))

    def _engine_morphism_crossing(self):
        r"""Return the private engine realization when one was selected.

        Protected ring-morphism realization endpoint under OWN-05--07. The
        representation is exposed only through the owner dispatcher below;
        ordinary mathematical consumers use this morphism itself.
        """
        assert self._engine_morphism is not None, (
            f"cannot compute with the ring morphism {self}: it has no computer-algebra model"
        )
        return self._engine_morphism

    def __mul__(self, other):
        # Any ring morphism composes here, including one whose Mor is a
        # subcategory's (a number-field embedding is a ring morphism).
        if not _is_ring_map_into(other, self.domain()):
            return NotImplemented
        if self.is_identity():
            return other
        if other.is_identity():
            return self
        return _ring_composite(self, other)

    def compose(self, before):
        result = self * before
        if result is NotImplemented:
            raise ValueError(
                f"cannot compose {self} after {before}: {before} ends at {before.codomain()}, but {self} "
                f"starts at {self.domain()}"
            )
        return result

    def as_algebra(self):
        r"""Return the codomain viewed as the algebra defined by this structure map."""
        from dzack_research.preamble.categories.algebras.algebras import _own_algebra

        return _own_algebra(self)

    def is_group_algebra_augmentation(self) -> bool:
        r"""Return whether this map is the represented augmentation ``R[G] -> R``."""
        from dzack_research.preamble.categories.functors.group_actions import (
            _is_augmentation_of_group_algebra,
        )

        return _is_augmentation_of_group_algebra(self)

    def is_group_algebra_subgroup_inclusion(self) -> bool:
        r"""Return whether this map is induced by a represented subgroup inclusion."""
        from dzack_research.preamble.categories.functors.group_induction import (
            _is_group_algebra_map_of_subgroup_inclusion,
        )

        return _is_group_algebra_map_of_subgroup_inclusion(self)

    def is_identity(self) -> bool:
        if self.domain() is not self.codomain():
            return False
        if self._preamble_is_identity:
            return True
        return self._engine_is_identity()

    def _engine_is_identity(self) -> bool:
        r"""Ask only the selected private engine realization about identity."""
        if self._engine_morphism is None:
            return False
        return bool(self._engine_morphism.is_identity())

    def _richcmp_(self, other, op):
        r"""Decide equality from represented universal/construction data.

        Sage's generic morphism comparison asks the domain for backend
        generators.  Owned localizations deliberately do not expose such a
        backend presentation: a map out of ``S^-1 R`` is determined instead by
        its restriction along ``R -> S^-1 R``.  Quotients are determined by
        precomposition with their quotient projection, while a framed algebra
        is determined by its scalar restriction and selected algebra-generator
        images.  These are the mathematical determining families owned by the
        corresponding constructors, so equality belongs here rather than at a
        downstream scheme/descent consumer.
        """
        if op not in (op_EQ, op_NE):
            return NotImplemented
        if element_parent(other) is not self.parent():
            return op == op_NE
        equal = _ring_morphisms_equal(self, other)
        from sage.misc.unknown import Unknown

        return equal if op == op_EQ else (Unknown if equal is Unknown else not equal)

    def extension_of_ideal(self, ideal):
        r"""Return ``I S``, the ideal of the codomain generated by the images of ``I``.

        The extension of an ideal along ``f: R -> S`` is generated by the
        images of any generating set of ``I``, because the ideal they generate
        already contains every image.  So this needs nothing of ``f`` beyond
        its values, and the localization of an ideal is the case where ``f``
        inverts a submonoid.
        """

        domain = self.domain()
        assert ideal.ring() is domain, (
            f"cannot extend {ideal} along {self}: it is an ideal of {ideal.ring()}, not of {domain}"
        )
        codomain = self.codomain()
        from dzack_research.preamble.categories.rings.commutative_algebra import (
            AdicCompletions,
        )

        if codomain in AdicCompletions() and domain in OwnedRings().Noetherian():
            from dzack_research.preamble.categories.rings.commutative_ideals import (
                _flat_extension_commutative_ideal,
            )

            return _flat_extension_commutative_ideal(ideal, self)
        return codomain.ideal(*(self(generator) for generator in ideal.ideal_generators()))

    def contraction_of_ideal(self, ideal):
        r"""Return ``f^{-1}(J)``, the contraction of an ideal of the codomain.

        Along a quotient map ``R -> R/I`` the preimage of ``J`` is generated by
        ``I`` together with lifts of generators of ``J``: an element lands in
        ``J`` exactly when it differs from such a lift by something in ``I``.
        That is the case a closed subscheme is written in, and taking ``J`` to
        be zero recovers the kernel.

        A general morphism has no such description, and computing the preimage
        needs elimination in a selected engine realization, which an owned
        morphism given elementwise does not carry.
        """

        from dzack_research.preamble.categories.rings.commutative_algebra import (
            QuotientRings,
        )

        domain = self.domain()
        codomain = self.codomain()
        assert ideal.ring() is codomain, (
            f"cannot contract {ideal} along {self}: it is an ideal of {ideal.ring()}, not of {codomain}"
        )
        assert (
            codomain in QuotientRings()
            and codomain.quotient_source() is domain
        ), (
            f"cannot contract {ideal} along {self}: contraction is computed here only when {codomain} is "
            f"a quotient of {domain} and {self} is its quotient map"
        )
        return domain.ideal(
            *codomain.defining_ideal().ideal_generators(),
            *(generator.lift() for generator in ideal.ideal_generators()),
        )

    def kernel(self):
        r"""Return the kernel ideal ``f^{-1}(0)`` of this ring morphism.

        A ring morphism ``R -> End_R(M)`` is the scalar action that makes ``M``
        an ``R``-module, and ``rho(r) = 0`` says exactly that ``r`` kills
        ``M``, so its kernel is ``Ann_R(M)``.  The module is the endomorphism
        Mor-object's own domain, so nothing has to be carried on the morphism
        for it to be found.
        """
        from dzack_research.preamble.categories.group.additive_mors import (
            AdditiveEndomorphismRings,
        )
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        codomain = self.codomain()
        if codomain in AdditiveEndomorphismRings(codomain.base_ring()):
            module = codomain.domain()
            if (
                module is codomain.codomain()
                and module in Modules(self.domain())
                and module.scalar_action() is self
            ):
                return module.annihilator()
            assert (
                module is codomain.codomain()
                and module in Modules(self.domain())
                and module.scalar_action() is self
            ), (
                f"cannot compute the kernel of {self}: the kernel of a map into End({module}) is computed "
                f"here only when {self} is the scalar action of {self.domain()} on {module}"
            )
        return self.contraction_of_ideal(codomain.ideal(codomain.zero()))


def _selected_engine_ring_morphism(morphism):
    r"""Return a retained private ring-map realization, or None.

    Protected ring-morphism contract under OWN-05--07. The permitted external
    caller role is a computation adapter that must preserve the exact native
    coefficient map selected when this owned ring morphism was built; scheme
    coordinate pullback is such an adapter. The raw map may be used only inside
    that adapter and mathematical values are raised through owned endpoints.
    Reconstructible maps need no crossing and return None here.
    """
    if element_parent(morphism) is not OwnedRings().Mor(
        morphism.domain(), morphism.codomain()
    ):
        return None
    return morphism._engine_morphism


class RingMor(CategoricalMor):
    r"""The owned set ``Hom_Ring(A,B)``."""

    Element = RingMorphism

    def __init__(self, mor_family, domain, codomain) -> None:
        CategoricalMor.__init__(self, mor_family, domain, codomain)

    def __call__(self, datum):
        return self._element_constructor_(datum)

    def is_endomorphism_set(self):
        return self.domain() is self.codomain()

    def _element_constructor_(self, datum):
        if isinstance(datum, RingMorphism):
            if datum.domain() is not self.domain() or datum.codomain() is not self.codomain():
                raise ValueError(
                    f"cannot view {datum} as an element of Mor({self.domain()}, {self.codomain()}): it is a "
                    f"morphism {datum.domain()} -> {datum.codomain()}"
                )
            if datum.parent() is self:
                return datum
            return self.elementwise(datum)
        if isinstance(datum, Mapping):
            from dzack_research.preamble.categories.algebras.algebras import (
                _engine_algebra_morphism_from_generator_images,
            )

            engine_morphism = _engine_algebra_morphism_from_generator_images(
                self.domain(),
                self.codomain(),
                datum,
            )
            return self._element_constructor_(engine_morphism)
        if isinstance(datum, Map):
            source_engine = _engine_ring(self.domain())
            target_engine = _engine_ring(self.codomain())

            def engine_endpoint(ring):
                # An engine map has Sage rings as endpoints; an owned map's
                # endpoints are lowered to their engines.
                return _engine_ring(ring) if ring in OwnedRings() else ring

            if engine_endpoint(datum.domain()) is not source_engine:
                raise ValueError(
                    f"cannot view {datum} as an element of Mor({self.domain()}, {self.codomain()}): its domain "
                    f"is {datum.domain()}"
                )
            if engine_endpoint(datum.codomain()) is not target_engine:
                raise ValueError(
                    f"cannot view {datum} as an element of Mor({self.domain()}, {self.codomain()}): its codomain "
                    f"is {datum.codomain()}"
                )
            return self.element_class(
                self,
                lambda element: _owned_engine_element(self.codomain(),
                    datum(_engine_element(self.domain(), element))
                ),
                engine_morphism=datum,
            )
        if callable(datum):
            return self.elementwise(datum)
        raise TypeError(
            f"cannot build a ring morphism {self.domain()} -> {self.codomain()} from {datum!r}: give "
            "the images of the ring generators or a map on elements"
        )

    def elementwise(self, function):
        return self.element_class(self, function)

    def _elementwise_with_engine(self, function, engine_morphism):
        r"""Construct an elementwise map retaining one private engine realization."""
        return self.element_class(
            self,
            function,
            engine_morphism=engine_morphism,
        )

    def identity(self):
        if self.domain() is not self.codomain():
            raise ValueError(
                f"the identity morphism exists only on Mor(R, R), but this is Mor({self.domain()}, {self.codomain()})"
            )
        identity = self.elementwise(lambda element: element)
        identity._preamble_is_identity = True
        return identity

    def _repr_(self):
        return f"Mor_Ring({self.domain()}, {self.codomain()})"


def _is_ring_map_into(candidate, target) -> bool:
    r"""Whether ``candidate`` is a ring morphism ending at ``target``.

    Composition is asked of an arbitrary right operand, so this is the one
    site that decides whether it is a map at all (Sage's ``Map`` protocol).
    """
    return (
        isinstance(candidate, Map)
        and candidate.codomain() is target
        and candidate.domain() in OwnedRings()
    )


def _ring_composite(second, first):
    r"""``second o first`` in the category of rings, evaluated elementwise.

    Every specialized ring morphism (field embeddings, order embeddings) is a
    ring morphism, so any composable pair has this composite; a
    specialization composes on its own data only when both factors are of its
    kind.
    """
    # The composite is a morphism of rings; the domain's own ``Mor`` may be a
    # more structured homset (algebra maps out of a polynomial ring), which
    # the composite need not belong to.
    return _ring_mor_category(first.domain(), second.codomain()).elementwise(
        lambda element: second(first(element)),
    )


def _ring_mor_category(domain, codomain) -> RingMor:
    r"""Build ``Mor_Ring(domain, codomain)`` from its owned Mor family."""
    return RingMorCategoryConstruction(OwnedRings()).Of(domain, codomain)


def _ring_morphism_with_engine(domain, codomain, function, engine_morphism):
    r"""Construct an owned ring morphism retaining one private engine map.

    Protected ring-Mor construction contract under OWN-05--07. Permitted
    external caller roles are commutative-algebra and scheme base-change
    adapters that have already selected an exact engine map realizing the
    supplied owned element function. The raw map is retained by the ring-Mor
    owner and is never mathematical output.
    """
    return domain.Mor(codomain, category=OwnedRings())._elementwise_with_engine(function, engine_morphism)


def _ring_morphisms_equal(left, right):
    r"""Return ``True``, ``False`` or ``Unknown`` from represented determining data."""
    from sage.misc.unknown import Unknown
    if left is right:
        return True
    if left.domain() is not right.domain() or left.codomain() is not right.codomain():
        return False

    domain = left.domain()
    if domain in LocalizationRings():
        source_map = domain.localization_map()
        return _ring_morphisms_equal(left * source_map, right * source_map)

    from dzack_research.preamble.categories.rings.commutative_algebra import (
        QuotientRings,
    )

    if domain in QuotientRings():
        quotient_map = domain.quotient_map()
        return _ring_morphisms_equal(left * quotient_map, right * quotient_map)

    engine = _engine_ring(domain)
    if engine is SageZZ or engine is SageQQ:
        # A unital map out of Z, or out of Q when it exists, is unique.
        return True

    if domain.is_framed_algebra():
        labels = domain.algebra_generating_set()
        if not labels.cardinality().is_finite():
            return Unknown
        if any(
            left(domain.algebra_generator(label)) != right(domain.algebra_generator(label))
            for label in labels
        ):
            return False
        structure_map = domain.algebra_structure_morphism()
        if structure_map.domain() is domain:
            return Unknown
        return _ring_morphisms_equal(
            left * structure_map,
            right * structure_map,
        )

    if left._engine_morphism is not None and right._engine_morphism is not None:
        return bool(left._engine_morphism == right._engine_morphism)
    return Unknown


class PredicateSubrings(OwnedCategory):
    def an_object(self):
        r"""The integers inside the rationals, cut out by integrality."""
        rationals = _own_ring(SageQQ)
        return rationals.predicate_subring(
            lambda element: element.denominator() == 1,
            "z is an integer",
        )

    def super_categories(self):
        return [OwnedRings()]

    class ParentMethods:
        def ambient_ring(self):
            return self._ambient_ring

        def defining_predicate(self):
            return self._predicate

        def __contains__(self, element):
            from sage.structure.element import parent as element_parent

            if element_parent(element) is self:
                return True
            if element not in self._ambient_ring:
                return False
            candidate = self._ambient_ring(element)
            answer = self._predicate(candidate)
            assert answer is True or answer is False, (
                f"cannot decide whether {candidate} lies in {self}: the defining condition "
                f"'{self._description}' is undecided on it"
            )
            return answer

        def _element_constructor_(self, element):
            from sage.structure.element import parent as element_parent

            from dzack_research.preamble.categories.modules.pure.modules import Modules

            source = element_parent(element)
            if source is self:
                return element
            if source is not self and source in Modules(self.base_ring()) and source.unformed_module() is self:
                return source._element_of_unformed_module(element)
            if element not in self._ambient_ring:
                raise ValueError(
                    f"{element} is not in {self}: it is not even an element of the ring {self._ambient_ring} "
                    "this subring lies in"
                )
            candidate = self._ambient_ring(element)
            if candidate not in self:
                raise ValueError(
                    f"{candidate} is not in {self}: it does not satisfy '{self._description}'"
                )
            return self.element_class(self, _engine_element(self._ambient_ring, candidate))

        def one(self):
            return self._one

        def zero(self):
            return self._zero

        def inclusion(self):
            return self.Mor(self._ambient_ring, category=OwnedRings())(self._element_in_larger_ring)

        def _repr_(self):
            return f"{{z in {self._ambient_ring} : {self._description}}}"


class LocalizationRings(OwnedCategory):
    r"""Commutative localizations carrying their selected source and submonoid."""

    class ElementMethods(CommutativeRingElement):
        r"""A represented fraction ``a/s`` in ``S^{-1}R``."""

        def __init__(self, parent, numerator, denominator) -> None:
            self._numerator = parent.localization_source()(numerator)
            self._denominator = parent.localization_source()(denominator)
            super().__init__(parent)

        def numerator(self):
            return self._numerator

        def denominator(self):
            return self._denominator

        def _add_(self, other):
            return self.parent().fraction(
                self.numerator() * other.denominator() + other.numerator() * self.denominator(),
                self.denominator() * other.denominator(),
            )

        def _mul_(self, other):
            return self.parent().fraction(
                self.numerator() * other.numerator(),
                self.denominator() * other.denominator(),
            )

        def __mul__(self, other):
            from sage.structure.element import parent as element_parent
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            other_parent = element_parent(other)
            if other_parent is self.parent():
                return LocalizationRings.ElementMethods._mul_(self, other)
            if other_parent in Modules(self.parent()):
                return other_parent.scalar_multiple(self, other)
            return NotImplemented

        def inverse_of_unit(self):
            r"""Return the inverse of a unit ``a/s``.

            An inverse is ``sb/u`` for any ``b`` in ``R`` and ``u`` in ``S``
            with ``ab = u``.  Which such pair to take is a witness for the
            membership that :meth:`is_unit` decides, and a fraction holds no
            witness, so the pair is read from the selected computation
            realization.  The decision itself is not asked of that realization,
            which is larger than ``S^{-1}R`` whenever it inverts more.
            """
            parent = self.parent()
            match self.is_unit():
                case True:
                    pass
                case False:
                    raise ValueError(f"{self} is not a unit of {parent}")
                case _:
                    raise ValueError(f"cannot decide whether {self} is a unit of {parent}")
            engine = parent._selected_engine_ring()
            represented = parent._engine_element(self)
            inverse = engine(represented) ** -1
            return _owned_engine_element(parent, inverse)

        def is_unit(self):
            r"""Return whether ``a/s`` is invertible in ``S^{-1}R``.

            An inverse is a fraction ``b/t`` with ``ab/st = 1``, and the
            denominator is already a unit, so ``a/s`` is a unit exactly when
            the ideal ``(a)`` meets ``S``.  For ``S`` generated by
            ``f_1, ..., f_r`` a monomial in the ``f_i`` lies in ``(a)`` exactly
            when a power of their product does -- raise every factor to the
            largest exponent the monomial uses -- so the criterion is that
            saturating ``(a)`` by the product gives the unit ideal.

            This is an ideal computation and needs nothing of ``S^{-1}R``,
            which is what lets a localization of a ring with zero divisors
            answer.  It is made in the ring at the bottom of a tower of
            localizations, where the ideals are: ``a/s`` is a unit exactly when
            ``a`` is, so a tower inverts a single family over that ring and the
            question descends to it unchanged.  A prime localization inverts a
            submonoid with no finite generating set and states the criterion
            for it separately.
            """
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                _localization_descent,
                _one_step_inverted_family,
            )

            parent = self.parent()
            source = parent.localization_source()
            structure = parent.localization_submonoid()._structure_data()
            match structure.get("kind"):
                case "prime_complement":
                    prime = structure["prime_ideal"]
                    return not prime.contains_ambient_element(self.numerator())
                case "nonzero_elements":
                    return self.numerator() != source.zero()
                case _:
                    pass
            # Sage's localization decides a unit by its numerator's units, which
            # is exact when numerators lie in the source ring and wrong for a
            # number-field order, whose numerators lie in the field (TRAPS.md).
            if parent._preamble_engine_ring is not None and source not in OwnedOrders():
                engine = parent._selected_engine_ring()
                return bool(engine(parent._engine_element(self)).is_unit())
            bottom, inverted_family = _one_step_inverted_family(
                source, parent.inverted_elements()
            )
            bottom, (numerator,) = _localization_descent(source, (self.numerator(),))
            inverted_product = bottom.one()
            for inverted in inverted_family:
                inverted_product = inverted_product * inverted
            numerator_ideal = bottom.ideal(numerator)
            inverted_ideal = bottom.ideal(inverted_product)
            return numerator_ideal.ideal_saturation(
                inverted_ideal
            ).contains_ambient_element(bottom.one())

        def __truediv__(self, other):
            other = self.parent()(other)
            return self * other.inverse_of_unit()

        def _neg_(self):
            return self.parent().fraction(
                -self.numerator(),
                self.denominator(),
            )

        def _sub_(self, other):
            r"""Subtraction in the additive group of ``S^{-1}R``."""
            return self._add_(-other)

        def equality_status(self, other):
            if other.parent() is not self.parent() or other.parent() is not self.parent():
                return False
            return self.parent()._fraction_equality_status(self, other)

        def _richcmp_(self, other, op):
            from sage.misc.unknown import Unknown

            if op not in (op_EQ, op_NE):
                return NotImplemented
            status = self.equality_status(other)
            return status if op == op_EQ else (Unknown if status is Unknown else not bool(status))

        def _repr_(self):
            if self.denominator() == self.parent().localization_source().one():
                return repr(self.numerator())
            return f"({self.numerator()})/({self.denominator()})"

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        _derived_construction_parameters = frozenset({"base_ring"})

        def inverted_submonoid_meets(self, ideal) -> bool:
            r"""Decide ``I intersect S != empty`` for this localization ``S^-1 R``.

            For a prime complement this means a generator of I lies outside
            the prime.  For the nonzero elements of a domain it means I is
            nonzero.  For finitely generated S, putting f equal to the product
            of its generators gives I intersect S nonempty exactly when
            ``1 in I : f^infinity``: every monomial in these generators divides
            a sufficiently large power of f, and f itself belongs to S.
            """
            from sage.misc.misc_c import prod

            from dzack_research.preamble.categories.rings.commutative_algebra import (
                PrimeLocalizations,
            )

            ring = self.localization_source()
            match self:
                case _ if self in PrimeLocalizations():
                    prime = self.localized_prime()
                    return any(not prime.contains_ambient_element(g) for g in ideal.ideal_generators())
                case _ if self.is_fraction_field_localization():
                    return ideal != ring.ideal(ring.zero())
                case _:
                    element = prod(self.inverted_elements(), ring.one())
                    return ideal.ideal_saturation(ring.ideal(element)).contains_ambient_element(ring.one())

        def __init__(
            self,
            source,
            submonoid,
            _engine_ring=None,
            _engine_source_decoder=None,
            _engine_source_encoder=None,
            *,
            algebra_source=None,
            fraction_field_realization=None,
            **rest,
        ) -> None:
            self._localization_source = source
            self._localization_submonoid = submonoid
            self._localization_engine_source_decoder = _engine_source_decoder
            self._localization_engine_source_encoder = _engine_source_encoder
            self._localization_algebra_source = algebra_source
            self._fraction_field_realization = fraction_field_realization
            self._preamble_engine_ring = _engine_ring
            from dzack_research.preamble.categories.algebras.algebras import Algebras

            algebra = (
                Algebras(self.algebra_base_ring())
                .Associative()
                .Unital()
                .Commutative()
            )
            rest["category"] = Category.join((rest["category"], algebra))
            super().__init__(
                base_ring=self.algebra_base_ring(),
                _engine_product=lambda left, right: LocalizationRings.ElementMethods._mul_(left, right),
                _engine_scalar_action=lambda scalar, element: LocalizationRings.ElementMethods._mul_(self(scalar), self(element)),
                _engine_unit=lambda algebra: LocalizationRings.ParentMethods.one(algebra),
                **rest,
            )

        def algebra_base_ring(self):
            algebra_source = self._localization_algebra_source
            return (
                algebra_source.base_ring()
                if algebra_source is not None
                else self.localization_source().base_ring()
            )

        def _selected_engine_ring(self):
            r"""Return the private realization that computes in this localization.

            Protected contract: the element arithmetic of this category asks its
            parent for the realization that decides invertibility.
            """
            engine = self._preamble_engine_ring
            assert engine is not None, (
                f"cannot compute in the localization {self}: it has no computer-algebra model"
            )
            return engine

        @cached_method
        def localization_functor(self):
            r"""Return the canonical module-localization functor along this ring localization."""
            from dzack_research.preamble.categories.functors.module_localization import (
                ModuleLocalizationFunctor,
            )

            return ModuleLocalizationFunctor(self)

        def localize_module(self, module):
            r"""Return ``S^{-1}M`` through this localization's canonical functor."""

            if module.base_ring() is not self.localization_source():
                raise ValueError(
                    f"cannot localize {module} at {self}: it is a module over {module.base_ring()}, but the "
                    f"localization is of {self.localization_source()}"
                )
            return self.localization_functor()(module)

        def _valid_denominator(self, denominator) -> bool:
            source = self.localization_source()
            if denominator == source.one():
                return True
            structure = self.localization_submonoid()._structure_data()
            match structure.get("kind"):
                case "prime_complement":
                    prime = structure["prime_ideal"]
                    return not prime.contains_ambient_element(denominator)
                case "nonzero_elements":
                    return denominator != source.zero()
                case _:
                    return bool(self.localization_map()(denominator).is_unit())

        def fraction(self, numerator, denominator=None):
            r"""Construct ``a/s`` after admitting ``s`` through the selected submonoid.

            Arithmetic and private engine crossings use this same constructor.
            There is no trusted spelling that can manufacture a localization
            element with a denominator outside the represented saturation of
            the selected multiplicative system.
            """
            source = self.localization_source()
            numerator = source(numerator)
            denominator = source.one() if denominator is None else source(denominator)
            match self._valid_denominator(denominator):
                case True:
                    pass
                case False:
                    raise ValueError(
                        f"{numerator}/{denominator} is not an element of {self}: the denominator {denominator} is "
                        "not in the multiplicative set being inverted"
                    )
            return self.element_class(self, numerator, denominator)

        def _element_constructor_(self, value):
            from sage.structure.element import parent as element_parent

            from dzack_research.preamble.categories.modules.pure.modules import Modules

            source = element_parent(value)
            if source is not self and source in Modules(self.base_ring()) and source.unformed_module() is self:
                return source._element_of_unformed_module(value)
            if source is self:
                return value
            if isinstance(value, tuple) and len(value) == 2:
                return self.fraction(value[0], value[1])
            return self.fraction(value)

        def __call__(self, value):
            return self._element_constructor_(value)

        def __contains__(self, value) -> bool:
            if element_parent(value) is self:
                return True
            source = self.localization_source()
            if isinstance(value, tuple) and len(value) == 2:
                numerator, denominator = value
                if numerator not in source or denominator not in source:
                    return False
                return self._valid_denominator(source(denominator))
            parent = element_parent(value)
            match parent:
                case _ if (
                    parent is not source
                    and parent in OwnedRings()
                    and self._preamble_engine_ring is not None
                    and self._localization_engine_source_decoder is None
                ):
                    # An element of a larger ring, such as 1/4 in QQ for
                    # ZZ[1/2], is in S^-1 A exactly when it is some a/s; the
                    # engine localization decides that on its own fractions.
                    return _engine_element(parent, value) in self._preamble_engine_ring
                case _:
                    return value in source

        def _from_engine_element(self, value):
            engine = self._preamble_engine_ring
            assert engine is not None, (
                f"cannot convert {value} into the localization {self}: it has no computer-algebra model"
            )
            represented = engine(value)
            source = self.localization_source()
            source_engine = _engine_ring(source)
            decoder = self._localization_engine_source_decoder
            if decoder is not None:
                return self.fraction(
                    decoder(represented.numerator()),
                    decoder(represented.denominator()),
                )

            # A localization of a quotient is realized privately by the
            # standard finite presentation
            # ``P[u_i]/(I, u_i f_i - 1)``.  Decode a polynomial representative
            # by sending the original variables through ``P -> P/I`` and each
            # auxiliary variable to the represented inverse of its selected
            # denominator.  This is exactly the universal localization map.
            if isinstance(engine, QuotientRing_generic) and isinstance(
                source_engine, QuotientRing_generic
            ):
                engine_cover = engine.cover_ring()
                source_cover = source_engine.cover_ring()
                source_names = tuple(source_cover.variable_names())
                inverted = tuple(self.inverted_elements())
                engine_names = tuple(engine_cover.variable_names())
                if (
                    engine_names[: len(source_names)] == source_names
                    and len(engine_names) == len(source_names) + len(inverted)
                    and all(
                        name.startswith("localization_inverse_")
                        for name in engine_names[len(source_names) :]
                    )
                ):
                    result = self.zero()
                    for exponents, coefficient in represented.lift().dict().items():
                        source_monomial = source_cover(coefficient)
                        for position, exponent in enumerate(exponents[: len(source_names)]):
                            source_monomial *= source_cover.gen(position) ** int(exponent)
                        term = self.fraction(
                            _owned_engine_element(source, source_engine(source_monomial))
                        )
                        for position, exponent in enumerate(exponents[len(source_names) :]):
                            if exponent:
                                term *= self.fraction(
                                    source.one(),
                                    inverted[position],
                                ) ** int(exponent)
                        result += term
                    return result
            return self.fraction(
                _owned_engine_element(source, source_engine(represented.numerator())),
                _owned_engine_element(source, source_engine(represented.denominator())),
            )

        def _engine_element(self, value):
            engine = self._preamble_engine_ring
            assert engine is not None, (
                f"cannot compute with {value} in the localization {self}: it has no computer-algebra model"
            )
            element = self(value)
            encoder = self._localization_engine_source_encoder
            if encoder is not None:
                return encoder(element.numerator()) / encoder(element.denominator())
            numerator = _engine_element(self.localization_source(), element.numerator())
            denominator = _engine_element(self.localization_source(), element.denominator())
            source_engine = _engine_ring(self.localization_source())
            source_map = engine.coerce_map_from(source_engine)
            if source_map is not None:
                return source_map(numerator) / source_map(denominator)
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                QuotientRings,
            )

            assert self.localization_source() in QuotientRings(), (
                "a localization engine without a source coercion is represented here "
                "only for a quotient source with canonical polynomial lifts"
            )
            return engine(numerator.lift()) / engine(denominator.lift())

        def zero(self):
            return self.fraction(self.localization_source().zero())

        def one(self):
            return self.fraction(self.localization_source().one())

        def _fraction_equality_status(self, left, right):
            from sage.misc.unknown import Unknown

            source = self.localization_source()
            left_product = left.numerator() * right.denominator()
            right_product = right.numerator() * left.denominator()
            # Use the owned additive operations rather than Python subtraction.
            # In particular, represented quotient classes implement addition and
            # negation directly, while Sage's inherited binary-subtraction
            # dispatch need not recognize their common owned parent.
            difference = source(left_product + (-right_product))
            if difference == source.zero():
                return True

            if source in OwnedRings().Commutative().NoZeroDivisors():
                return False

            structure = self.localization_submonoid()._structure_data()
            if structure.get("kind") == "prime_complement":
                prime = structure.get("prime_ideal")
                if prime is None:
                    return Unknown
                annihilator = source.ideal(source.zero()).colon(
                    source.ideal(difference)
                )
                return any(
                    not prime.contains_ambient_element(generator)
                    for generator in annihilator.ideal_generators()
                )

            from dzack_research.preamble.categories.rings.commutative_algebra import (
                QuotientRings,
            )

            if source in QuotientRings():
                source_ring = source.quotient_source()
                representative = source_ring(difference.lift())
                lifted_generators = tuple(
                    source_ring(generator.lift())
                    for generator in self.localization_submonoid().monoid_generators()
                )
                if not lifted_generators:
                    return False
                product = source_ring.one()
                for generator in lifted_generators:
                    product *= generator
                saturated = source.defining_ideal().saturation(
                    source_ring.ideal(product)
                )
                return saturated.contains_ambient_element(representative)

            # A selected exact coefficient presentation A = P/I contains the
            # same data needed for localization equality as an explicit
            # QuotientRing object.  For a finitely generated multiplicative set
            # S = <f_1,...,f_r>, a class d vanishes in S^{-1}A exactly when its
            # lift to P belongs to I : (f_1 ... f_r)^∞.  Indeed, a monomial in
            # the f_i kills d iff a sufficiently large common power of their
            # product kills d, and conversely every such common power lies in S.
            has_presentation = source._has_selected_exact_coefficient_presentation()
            if has_presentation:
                presentation_ring = source._exact_coefficient_presentation_ring()
                representative = presentation_ring(
                    source._lift_coefficient_to_presentation(difference)
                )
                lifted_generators = tuple(
                    presentation_ring(
                        source._lift_coefficient_to_presentation(generator)
                    )
                    for generator in self.localization_submonoid().monoid_generators()
                )
                if not lifted_generators:
                    return False
                product = presentation_ring.one()
                for generator in lifted_generators:
                    product *= generator
                relations = tuple(
                    presentation_ring(relation)
                    for relation in source._exact_coefficient_presentation_relations()
                )
                defining_ideal = presentation_ring.ideal(
                    *(relations or (presentation_ring.zero(),))
                )
                saturated = defining_ideal.saturation(
                    presentation_ring.ideal(product)
                )
                return saturated.contains_ambient_element(representative)

            if source in owned_sets.FiniteSets():
                generators = tuple(self.localization_submonoid().monoid_generators())
                pending = [difference]
                seen = []
                while pending:
                    current = pending.pop()
                    if current == source.zero():
                        return True
                    if any(current == old for old in seen):
                        continue
                    seen.append(current)
                    pending.extend(
                        source(generator * current) for generator in generators
                    )
                return False
            return Unknown

        def _repr_(self):
            return f"Localization of {self.localization_source()} at {self.localization_submonoid()}"

        def localization_source(self):
            return self._localization_source

        def localization_submonoid(self):
            return self._localization_submonoid

        def is_fraction_field_localization(self) -> bool:
            r"""Whether this localizes a domain at all of its nonzero elements."""
            return (
                self.localization_submonoid()._structure_data().get("kind")
                == "nonzero_elements"
            )

        def fraction_field_realization(self):
            r"""Return the canonical owned field privately realizing this localization."""
            if not self.is_fraction_field_localization():
                raise ValueError(
                    f"{self} is not the fraction field of {self.localization_source()}: it does not invert "
                    "all nonzero elements"
                )
            field = self._fraction_field_realization
            if field is None:
                raise ArithmeticError(
                    f"{self} inverts all nonzero elements of {self.localization_source()}, but its fraction field "
                    "was not constructed"
                )
            return field

        @cached_method
        def fraction_field_comparison(self):
            r"""Return the canonical map ``(R-{0})^-1 R -> Frac(R)``."""
            if not self.is_fraction_field_localization():
                raise ValueError(
                    f"there is no map {self} -> Frac(R): {self} is not the localization of "
                    f"{self.localization_source()} at all nonzero elements"
                )
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                _canonical_map,
            )

            source_to_field = _canonical_map(
                self.localization_source(), self.fraction_field_realization()
            )

            def image(element):
                fraction = self(element)
                numerator = source_to_field(fraction.numerator())
                denominator = source_to_field(fraction.denominator())
                return numerator * denominator.inverse_of_unit()

            return self.Mor(self.fraction_field_realization())(image)

        @cached_method
        def fraction_field_comparison_inverse(self):
            r"""Return the inverse ``Frac(R) -> (R-{0})^-1 R``."""
            if not self.is_fraction_field_localization():
                raise ValueError(
                    f"there is no map Frac(R) -> {self}: {self} is not the localization of "
                    f"{self.localization_source()} at all nonzero elements"
                )
            field = self.fraction_field_realization()
            return field.Mor(self)(
                lambda element: self._from_engine_element(_engine_element(field, element)),
            )

        def inverted_elements(self):
            return self.localization_submonoid().monoid_generators()

        def inverted_element(self):
            r"""Return the one element ``f`` this localization inverts.

            Localizing at a single ``f`` is the distinguished open ``D(f)``, and
            there every represented denominator is a power of ``f``, so a
            fraction is read as ``a/f^n``.  A localization at several elements
            inverts every monomial in them, so a denominator is described by one
            exponent per inverted element rather than by a single natural
            number; that reading is not stated here.
            """
            inverted = self.inverted_elements()
            match inverted.cardinality() == 1:
                case True:
                    pass
                case False:
                    raise ValueError(
                        f"{self} inverts {inverted.cardinality()} elements, but the inverted element is defined only "
                        "for a localization R[1/f] at a single element f"
                    )
            return inverted[0]

        def induced_morphism(self, morphism):
            r"""Return the unique ``S^{-1}R -> T`` extending ``g: R -> T``.

            Localization is universal among ring maps out of ``R`` that invert
            ``S``.  So when ``g`` carries ``S`` into the units exactly one map
            out of ``S^{-1}R`` composes with the localization map to give
            ``g``, and it sends ``a/s`` to ``g(a)g(s)^{-1}``.  Which
            representative of a fraction is used does not matter: ``a/f`` and
            ``af/f^2`` have the same image, so the map is defined on the
            fraction and not on a chosen presentation of it.

            Both terms come from the fraction itself, which a localization
            built from a numerator and a denominator, so the source ring is
            asked for nothing beyond the two elements it already holds.

            The hypothesis is one statement about a generating set: a monomial
            in elements carried to units is carried to a unit, so it suffices
            on generators.  The complement of a prime has no finite generating
            set, and there the hypothesis is asked of each denominator the map
            meets, which is where inverting it is what the map has to do.

            A transition map of a toric atlas is such a map: the pullback to a
            face localization is a ring morphism out of the source that carries
            the inverted character to a unit.  So is the residue map
            ``R_p -> kappa(p)``, which extends ``R -> kappa(p)``.
            """
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                PrimeLocalizations,
            )

            source = self.localization_source()
            match morphism.domain() is source:
                case True:
                    pass
                case False:
                    raise ValueError(
                        f"a map out of {self} is induced from a ring morphism out of {source}, but {morphism} starts "
                        f"at {morphism.domain()}"
                    )
            match self in PrimeLocalizations():
                case True:
                    pass
                case False:
                    for inverted in self.inverted_elements():
                        match morphism(inverted).is_unit():
                            case True:
                                pass
                            case False:
                                raise ValueError(
                                    f"{morphism} does not carry {inverted} to a unit, so it does not "
                                    f"factor through {self}"
                                )
                            case _:
                                raise ValueError(
                                    f"it is undecided whether {morphism} sends {inverted} to a unit, so it is not known to "
                                    f"factor through {self}"
                                )

            def image(element):
                fraction = self(element)
                return morphism(fraction.numerator()) * morphism(
                    fraction.denominator()
                ).inverse_of_unit()

            engine_source = _engine_ring(source)
            engine_target = _engine_ring(morphism.codomain())
            engine_localization = self._selected_engine_ring()
            source_generators = tuple(engine_source.gens())
            localization_generators = tuple(engine_localization.gens())
            engine_morphism = None
            if len(source_generators) == len(localization_generators):
                engine_images = [
                    _engine_element(
                        morphism.codomain(),
                        morphism(_owned_engine_element(source, generator)),
                    )
                    for generator in source_generators
                ]
                engine_morphism = engine_localization.hom(
                    engine_images,
                    engine_target,
                )

            return self.Mor(morphism.codomain(), category=OwnedRings())._elementwise_with_engine(
                image,
                engine_morphism,
            )

        @cached_method
        def localization_map(self):
            r"""Return the canonical map ``R -> S^-1 R`` derived from this localization datum."""
            source = self.localization_source()
            return source.Mor(self, category=OwnedRings())(
                lambda element: self.fraction(element),
            )

        def restriction_to(self, target):
            r"""Return the unique map ``S^{-1}R -> T^{-1}R`` commuting with the maps from ``R``.

            Localization is universal among ring maps out of ``R`` that invert
            ``S``.  So whenever ``T^{-1}R`` already inverts every element of
            ``S``, exactly one map ``S^{-1}R -> T^{-1}R`` respects the two maps
            from ``R``, and it sends ``a/s`` to ``a`` times the inverse of ``s``.
            Uniqueness is what makes these maps compose: for ``S`` inside ``T``
            inside ``U`` the composite of the two restrictions is the single
            restriction from ``S`` to ``U``.

            On spectra this is the inclusion of distinguished opens
            ``D(fg) <= D(f)``, so sheaf restriction on an affine scheme is this
            map and nothing further.  Taking ``T`` to be the complement of a
            prime gives the map from a section to its germ.

            The same open arises the other way, by localizing the chart
            ``S^{-1}R`` itself at ``g``.  Then the target's source is this ring
            rather than ``R``, and the map over it is that localization's own
            map, which the two constructions of ``D(fg)`` share.

            Between two prime localizations the containment ``S <= T`` is
            ``R \\ q <= R \\ p``, that is ``p <= q``, so ``R_q -> R_p`` exists
            exactly when ``p`` specializes to ``q``: the germ at a point maps
            to the germ at any point whose closure contains it.  Neither
            complement has a finite generating set, so the containment is
            decided on the primes rather than on inverted elements.
            """

            from dzack_research.preamble.categories.rings.commutative_algebra import (
                PrimeLocalizations,
            )

            match target in LocalizationRings():
                case True:
                    pass
                case False:
                    raise TypeError(
                        f"a map {self} -> {target} over {self.localization_source()} needs a localization of that ring "
                        f"as target, but {target} is not a localization"
                    )
            if target.localization_source() is self:
                # The overlap was built by localizing this chart, so the map
                # over it is that localization's own map: it is already the
                # unique map out of this ring inverting what the target adds.
                return target.localization_map()
            match target.localization_source() is self.localization_source():
                case True:
                    pass
                case False:
                    raise ValueError(
                        f"{self} and {target} localize different rings, so no map over the source exists"
                    )
            if self in PrimeLocalizations():
                match target in PrimeLocalizations():
                    case True:
                        pass
                    case False:
                        raise ValueError(
                            f"{self} inverts the complement of the prime {self.localized_prime()}, which has no finite "
                            f"generating set, so a map to {target} is constructed only when {target} is also a localization "
                            "at a prime"
                        )
                match all(
                    self.localized_prime().contains_ambient_element(generator)
                    for generator in target.localized_prime().ideal_generators()
                ):
                    case True:
                        pass
                    case False:
                        raise ValueError(
                            f"{target.localized_prime()} is not contained in {self.localized_prime()}, "
                            f"so {target} does not invert everything {self} inverts and the universal "
                            "property of localization gives no map between them"
                        )
            else:
                for inverted in self.inverted_elements():
                    match target(inverted).is_unit():
                        case True:
                            pass
                        case False:
                            raise ValueError(
                                f"{target} does not invert {inverted}, so the universal "
                                f"property of localization gives no map from {self}"
                            )
                        case _:
                            raise ValueError(
                                f"invertibility of {inverted} in {target} is unresolved, so the "
                                f"universal property of localization does not admit a map from {self}"
                            )

            def image(element):
                numerator = target(element.numerator())
                denominator = target(element.denominator())
                return numerator * denominator.inverse_of_unit()

            return self.Mor(target)(image)

        def localization_fraction_data(self, element):
            r"""Return one represented fraction ``(r,s)`` for ``element=r/s``."""
            value = self(element)
            source = self.localization_source()
            return source(value.numerator()), source(value.denominator())


class _PredicateSubringParent(Parent):
    @lazy_attribute
    def Element(self):
        return _PredicateSubringElement

    def __init__(self, ambient_ring, predicate, description, category):
        if ambient_ring not in SageRings() and ambient_ring not in OwnedRings():
            raise TypeError(f"{ambient_ring} is not a ring")
        ambient_ring = _own_ring(ambient_ring)
        self._ambient_ring = ambient_ring
        self._predicate = predicate
        self._description = description
        commutative_rings = OwnedRings().Commutative()
        self._preamble_is_commutative = category.is_subcategory(commutative_rings) or ambient_ring.is_commutative() is True
        self._one = ambient_ring.one()
        self._zero = ambient_ring.zero()
        base = self if self._preamble_is_commutative else _own_ring(SageZZ)
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        algebra = Algebras(base).Associative().Unital()
        placements = [category]
        match self._preamble_is_commutative:
            case True:
                from dzack_research.preamble.categories.modules.pure.modules import (
                    FinitelyGeneratedFreeModules,
                )

                placements.extend((
                    algebra.Commutative(),
                    FinitelyGeneratedFreeModules(self),
                ))
            case False:
                placements.append(algebra)
        Parent.__init__(self, base=base, category=Category.join(tuple(placements)))
        realize_owned_category(self)
        # A predicate-subring datum asserts closure and the ring constants.
        # Refute a decided false constant, but do not treat an undecided
        # predicate as false. Constants are supplied by those defining laws.
        assert predicate(self._one) is not False and predicate(self._zero) is not False, (
            f"the subset of {ambient_ring} defined by '{description}' is not a unital subring: "
            "the condition fails on 0 or on 1"
        )
        self._one = self.element_class(self, _engine_element(ambient_ring, self._one))
        self._zero = self.element_class(self, _engine_element(ambient_ring, self._zero))
        from dzack_research.preamble.categories.algebras.algebras import (
            _algebra_from_native_ring,
        )

        _algebra_from_native_ring(self, lambda left, right: self(left * right), self._one,
            lambda scalar, element: self(self(scalar) * self(element)))

    def is_commutative(self):
        if self._preamble_is_commutative:
            return True
        from sage.misc.unknown import Unknown

        return Unknown

    def __call__(self, element):
        r"""Construct an element of the predicate subring directly."""
        return self._element_constructor_(element)

    def _element_constructor_(self, element):
        return PredicateSubrings.ParentMethods._element_constructor_(self, element)

    def _from_engine_element(self, element):
        r"""Cross a computation in the larger ring back into this subring."""
        candidate = _owned_engine_element(self._ambient_ring, element)
        if (candidate == self._ambient_ring.zero()) is True:
            return self._zero
        if (candidate == self._ambient_ring.one()) is True:
            return self._one
        return self(candidate)

    def _element_in_larger_ring(self, element):
        r"""Raise this subring's stored computation in its exact larger ring."""
        native = self._engine_element(element)
        return _owned_engine_element(self._ambient_ring, native)

    def _engine_element(self, element):
        return self(element)._backend()

    def _selected_engine_ring(self):
        r"""Return the ambient ring's selected computation realization."""
        return _engine_ring(self._ambient_ring)

    def __contains__(self, element):
        return PredicateSubrings.ParentMethods.__contains__(self, element)


_OwnedRingBootstrapParent.register(_PredicateSubringParent)


def _predicate_subring(ambient_ring, predicate, description, category=None):
    placement = PredicateSubrings()
    if category is not None:
        placement = Category.join((placement, category))
    return _PredicateSubringParent(
        ambient_ring,
        predicate,
        description,
        placement,
    )


class LocalRingConstruction:
    r"""The selected maximal ideal and residue quotient data of a local ring."""

    def __init__(self, maximal_ideal, residue_field, residue_map=None) -> None:
        self._maximal_ideal = maximal_ideal
        self._residue_field = residue_field
        self._residue_map = residue_map

    def maximal_ideal(self):
        return self._maximal_ideal

    def residue_field(self):
        return self._residue_field

    def residue_map(self):
        return self._residue_map


def _install_local_ring_construction(ring, maximal_ideal, residue_field, residue_map=None):
    r"""Install the selected local-ring quotient datum on ``ring`` exactly once."""
    if maximal_ideal.ring() is not ring:
        raise ValueError(
            f"cannot make {ring} a local ring with maximal ideal {maximal_ideal}: that is an ideal of "
            f"{maximal_ideal.ring()}"
        )
    if residue_map is not None:
        if residue_map.domain() is not ring or residue_map.codomain() is not residue_field:
            raise ValueError(
                f"the residue map of the local ring {ring} must be {ring} -> {residue_field}, but {residue_map} "
                f"is a map {residue_map.domain()} -> {residue_map.codomain()}"
            )
    construction = LocalRingConstruction(maximal_ideal, residue_field, residue_map)
    existing = ring._selected_local_ring_construction()
    if existing is not None:
        if (
            existing.maximal_ideal() is not maximal_ideal
            or existing.residue_field() is not residue_field
            or existing.residue_map() is not residue_map
        ):
            raise ValueError(
                f"{ring} is already a local ring with maximal ideal {existing.maximal_ideal()} and residue field "
                f"{existing.residue_field()}; it cannot also have maximal ideal {maximal_ideal} and residue field "
                f"{residue_field}"
            )
        return ring
    ring._local_ring_construction = construction
    return ring


class OwnedRings(CategoryPacketMethods, OwnedCategory):
    """Unital rings whose notebook-facing ring interface is owned here."""

    _MorCategory = RingMorCategoryConstruction

    def an_object(self):
        r"""The integers, the initial object of this category."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedSemirings(), OwnedRngs()]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError(
                f"a ring morphism needs a ring as domain and codomain, but got {domain} and {codomain}"
            )
        return _ring_mor_category(domain, codomain)

    # Functors out of rings, sited on their domain.

    def unit_group(self):
        r"""``R |-> R^x : Ring -> Grp``."""
        return UnitGroupFunctor()

    def center_functor(self):
        r"""Return ``Z : Core(Ring) -> CRing``."""
        return RingCenterFunctor()

    class SubcategoryMethods:
        def Division(self):
            r"""Return this category with the axiom that every nonzero element is a unit."""
            return self._with_axiom("Division")

        def NoZeroDivisors(self):
            r"""Return this category with the axiom ``xy = 0  =>  x = 0 or y = 0``."""
            return self._with_axiom("NoZeroDivisors")

        def Noetherian(self):
            r"""Return this category with the ascending chain condition on ideals."""
            return self._with_axiom("Noetherian")

        def Artinian(self):
            r"""Return this category with the descending chain condition on ideals."""
            return self._with_axiom("Artinian")

    class Division(CategoryWithAxiom):
        r"""Division rings: every nonzero element is a unit."""

        @classmethod
        def _repr_object_names(cls):
            return "division rings"

        def an_object(self):
            r"""The field of two elements."""
            return GF(2)

        def extra_super_categories(self):
            return [OwnedRings().NoZeroDivisors()]

        class Commutative(CategoryWithAxiom):
            r"""Fields, spelled as Sage spells them: ``DivisionRings().Commutative()``."""

            class _MorCategory(MorCategoryConstruction):
                def fixed_category_class(self):
                    from dzack_research.preamble.categories.rings.field_morphisms import (
                        _ExactFieldMor,
                    )

                    return _ExactFieldMor

            @classmethod
            def _repr_object_names(cls):
                return "fields"

            def an_object(self):
                r"""The field of two elements."""
                return GF(2)

            def extra_super_categories(self):
                r"""The ideals of a field are ``0`` and the field."""
                return [
                    OwnedRings().Commutative().PrincipalIdeals(),
                    OwnedRings().Artinian(),
                    OwnedRings().Commutative().Local(),
                ]

            class SubcategoryMethods:
                def Prime(self):
                    r"""Return this category with the axiom of having no proper subfield."""
                    return self._with_axiom("Prime")

            class Prime(CategoryWithAxiom):
                r"""Prime fields: \(\mathbf F_p\) and \(\mathbb Q\), the fields with no proper subfield."""

                @classmethod
                def _repr_object_names(cls):
                    return "prime fields"

                def an_object(self):
                    r"""The field of two elements."""
                    return GF(2)

            class ParentMethods:
                def krull_dimension(self):
                    r"""``0``: the only prime ideal of a field is ``(0)``."""
                    return _own_ring(SageZZ).zero()

                def field_generators(self):
                    r"""Return exact elements which determine a unital map out of this field."""
                    from dzack_research.preamble.categories.rings.field_morphisms import (
                        _field_generators,
                    )

                    return _field_generators(self)

                def exact_morphisms_to(self, codomain):
                    r"""Return the exact-field morphism object from this field to ``codomain``."""
                    return OwnedFields().MorCategory().Of(self, codomain)

                def exact_embeddings(self, codomain):
                    r"""Return the exact embeddings of this field into ``codomain``."""
                    from dzack_research.preamble.categories.rings.field_morphisms import (
                        _exact_embeddings,
                    )

                    return _exact_embeddings(self, codomain)

                def first_exact_embedding(self, codomain):
                    r"""Choose the first exact embedding into ``codomain`` in deterministic order."""
                    embeddings = self.exact_embeddings(codomain)
                    if embeddings.cardinality() == 0:
                        raise ValueError(f"{self} has no embedding into {codomain}")
                    return embeddings[0]

                def maximal_ideal(self):
                    r"""Return the zero ideal, the unique maximal ideal of a field."""
                    return self.ideal(self.zero())

                def residue_field(self):
                    return self

                def residue_map(self):
                    return self.Mor(self).identity()

                def absolute_galois_group(self):
                    r"""Return the absolute Galois group ``G_K`` of this field ``K``.

                    The group is the existing profinite owner; this field method is
                    only the mathematical construction site and creates no parallel
                    realization.
                    """
                    from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
                        AbsoluteGaloisGroup,
                    )

                    return AbsoluteGaloisGroup(self)

    class NoZeroDivisors(CategoryWithAxiom):
        r"""Domains: rings in which ``xy = 0`` forces ``x = 0`` or ``y = 0``."""

        @classmethod
        def _repr_object_names(cls):
            return "domains"

        def an_object(self):
            r"""The integers."""
            return _own_ring(SageZZ)

        class Commutative(CategoryWithAxiom):
            r"""Integral domains, spelled as Sage spells them: ``Domains().Commutative()``."""

            @classmethod
            def _repr_object_names(cls):
                return "integral domains"

            def an_object(self):
                r"""The integers."""
                return _own_ring(SageZZ)

            class ParentMethods:
                def is_integral_domain(self, *args, **kwargs):
                    return True

                def fractional_ideal(self, *module_generators):
                    r"""Return the fractional ideal spanned by the stated elements of ``Frac(self)``."""
                    from dzack_research.preamble.categories.modules.fractional_ideals import (
                        _fractional_ideal,
                    )

                    if len(module_generators) == 1 and isinstance(
                        module_generators[0], (tuple, list)
                    ):
                        module_generators = tuple(module_generators[0])
                    return _fractional_ideal(self, tuple(module_generators))

                @cached_method
                def nonzero_multiplicative_submonoid(self):
                    r"""Return ``R - {0}``, the multiplicative submonoid defining ``Frac(R)``."""
                    from dzack_research.preamble.categories.rings.commutative_algebra import (
                        _nonzero_element_submonoid,
                    )

                    return _nonzero_element_submonoid(self)

                @cached_method
                def fraction_field_localization(self):
                    r"""Return the represented localization ``(R-{0})^-1 R``."""
                    from dzack_research.preamble.categories.rings.commutative_algebra import (
                        _localization_at_submonoid,
                    )

                    if self in OwnedRings().Division().Commutative():
                        return self
                    return _localization_at_submonoid(
                        self,
                        self.nonzero_multiplicative_submonoid(),
                    )

                @cached_method
                def fraction_field_map(self):
                    r"""Return the localization map ``R -> Frac(R)``.

                    This is the localization of ``R`` at its nonzero elements, so it is
                    injective exactly because ``R`` is a domain.  Scalar extension along
                    it is the generic fibre: a module dies under it exactly on its
                    torsion, and an ideal extends along it to the unit ideal exactly
                    when it is nonzero.
                    """
                    if self in OwnedRings().Division().Commutative():
                        return self.Mor(self).identity()
                    localization = self.fraction_field_localization()
                    return (
                        localization.fraction_field_comparison()
                        * localization.localization_map()
                    )

    class Noetherian(CategoryWithAxiom):
        r"""Noetherian rings: the ascending chain condition on ideals."""

        @classmethod
        def _repr_object_names(cls):
            return "noetherian rings"

        def an_object(self):
            r"""The integers."""
            return _own_ring(SageZZ)

        class ParentMethods:
            def is_noetherian(self):
                return True

    class Artinian(CategoryWithAxiom):
        r"""Artinian rings: the descending chain condition on ideals."""

        @classmethod
        def _repr_object_names(cls):
            return "artinian rings"

        def an_object(self):
            r"""The field of two elements: a field is artinian."""
            return GF(2)

        def extra_super_categories(self):
            r"""Hopkins–Levitzki: an artinian ring is noetherian."""
            return [OwnedRings().Noetherian()]

        class ParentMethods:
            def is_artinian(self):
                return True

    class Commutative(CategoryWithAxiom):
        r"""Commutative unital rings in the owned mathematical graph."""

        @classmethod
        def _repr_object_names(cls):
            return "commutative rings"

        def an_object(self):
            r"""The integers."""
            return _own_ring(SageZZ)

        class SubcategoryMethods:
            def Local(self):
                r"""Return this category with the axiom of a unique maximal ideal."""
                return self._with_axiom("Local")

            def PrincipalIdeals(self):
                r"""Return this category with the axiom that every ideal is principal."""
                return self._with_axiom("PrincipalIdeals")

        class Local(CategoryWithAxiom):
            r"""Local rings: one maximal ideal."""

            @classmethod
            def _repr_object_names(cls):
                return "local rings"

            def an_object(self):
                r"""The integers localized at the prime (2)."""
                return _own_ring(SageZZ).localize_at_prime(2)

            class SubcategoryMethods:
                def Complete(self):
                    r"""Return the complete-local refinement."""
                    return self._with_axiom("Complete")

            class ParentMethods:
                def is_local(self):
                    return True

                def local_ring_construction(self):
                    construction = self._selected_local_ring_construction()
                    assert construction is not None, (
                        f"{self} is in the category of local rings that are not fields, but its maximal ideal and "
                        "residue field are missing"
                    )
                    return construction

                def maximal_ideal(self):
                    return self.local_ring_construction().maximal_ideal()

                def residue_field(self):
                    return self.local_ring_construction().residue_field()

                def residue_map(self):
                    r"""Return the selected local quotient map ``R -> kappa(m)``."""
                    selected = self.local_ring_construction().residue_map()
                    assert selected is not None, (
                        f"the residue map R -> R/m of the local ring {self} is missing"
                    )
                    return selected

            class Complete(CategoryWithAxiom):
                r"""Complete local rings: complete and separated for the maximal-ideal topology."""

                @classmethod
                def _repr_object_names(cls):
                    return "complete local rings"

                def an_object(self):
                    r"""The 2-adic integers: complete, and local because (2) is maximal."""
                    return _own_ring(SageZZ).adic_completion(2)

                def extra_super_categories(self):
                    r"""The maximal ideal is the ideal of definition, so the datum is determined."""
                    return [OwnedAdicallyCompleteRings()]

        class PrincipalIdeals(CategoryWithAxiom):
            r"""Principal ideal rings: every ideal is principal (Mathlib's ``IsPrincipalIdealRing``)."""

            @classmethod
            def _repr_object_names(cls):
                return "principal ideal rings"

            def an_object(self):
                r"""The integers."""
                return _own_ring(SageZZ)

            def extra_super_categories(self):
                r"""A principal ideal is finitely generated."""
                return [OwnedRings().Noetherian()]

        class ParentMethods:
            def is_commutative(self):
                return True

            def krull_dimension(self):
                return _engine_krull_dimension(self)

            def as_algebra_over(self, base_ring):
                base = _own_ring(base_ring)
                from dzack_research.preamble.categories.algebras.algebras import (
                    Algebras,
                )

                selected = Algebras(base).Associative().Unital().Commutative()
                match (self.base_ring() is base, self in selected):
                    case (True, True):
                        return self
                    case _:
                        pass
                engine = _engine_ring(self)
                if not engine.has_coerce_map_from(_engine_ring(base)):
                    raise ValueError(
                        f"{self} is not an algebra over {base}: there is no canonical ring morphism {base} -> {self}"
                    )
                match base is self:
                    case True:
                        structure_map = self.Mor(self).identity()
                    case False:
                        structure_map = base.Mor(self)(
                            engine.coerce_map_from(_engine_ring(base))
                        )
                return structure_map.as_algebra()

            def affine_spectrum(self, base_ring=None):
                r"""Return the affine scheme represented by this commutative ring or algebra."""
                from dzack_research.preamble.categories.schemes.schemes import (
                    _affine_spectrum,
                )

                return _affine_spectrum(self, base_ring=base_ring)

            def as_ZZ_algebra(self):
                return self.as_algebra_over(_own_ring(SageZZ))

            def ideal(self, *generators):
                r"""Return the ideal of this ring generated by the elements given.

                In a localization every denominator is a unit, so
                ``(a_1/s_1, ..., a_r/s_r)`` is the extension of the source ideal
                ``(a_1, ..., a_r)`` along ``R -> S^{-1}R``.  Saying it that way
                is what makes the result an ideal like any other: it arrives as
                a submodule of the regular module of ``S^{-1}R``, carrying the
                sum, product, intersection, colon, contraction and membership
                operations, and it asks the source for a numerator rather than a
                fraction field, so a localization of a ring that has none is
                built the same way.
                """
                from dzack_research.preamble.categories.rings.commutative_ideals import (
                    _commutative_ideal,
                )

                if len(generators) == 1 and isinstance(generators[0], (tuple, list)):
                    generators = tuple(generators[0])
                if self in LocalizationRings():
                    source = self.localization_source()
                    numerators = tuple(
                        self.localization_fraction_data(generator)[0]
                        for generator in generators
                    )
                    return source.ideal(*numerators).extension_to_localization(self)
                return _commutative_ideal(self, tuple(generators))

            def quotient_ring(self, ideal):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    _owned_ideal,
                    _quotient_ring,
                )

                return _quotient_ring(self, _owned_ideal(self, ideal))

            def localization(self, *elements):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    _localization,
                )

                return _localization(self, *elements)

            def localize_at_prime(self, prime):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    _prime_localization_from_input,
                )

                return _prime_localization_from_input(self, prime)

            def residue_field_at(self, ideal):
                r"""Return the residue field ``R/m`` at a represented maximal ideal ``m``."""
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    _residue_field_at,
                )

                return _residue_field_at(self, ideal)

            def dual_numbers(self, name="epsilon"):
                r"""Return ``self[epsilon]/(epsilon^2)``."""
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    _dual_numbers,
                )

                return _dual_numbers(self, name=name)

            def adic_completion(self, ideal, precision=20):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    AdicCompletions,
                )

                return AdicCompletions()(self, ideal, precision=precision)

            @cached_method
            def spectrum(self):
                from dzack_research.preamble.categories.rings.commutative_algebra import (
                    PrimeSpectra,
                    _PrimeSpectrumTopologyData,
                )
                from dzack_research.preamble.owned_category import _object_of

                return _object_of(
                    PrimeSpectra(),
                    ring=self,
                    topology_data=_PrimeSpectrumTopologyData(self),
                )

            def total_quotient_ring(self):
                r"""Return ``Q(R) = S^{-1}R`` for ``S`` the regular elements of ``R``.

                Inverting every non-zerodivisor is the largest localization that
                stays injective on ``R``, which is what a Cartier divisor and a
                rational function are stated in.  Over an integral domain the
                regular elements are exactly the nonzero ones, so ``Q(R)`` is
                the fraction field.
                """

                assert self in OwnedRings().Commutative().NoZeroDivisors(), (
                    f"the total quotient ring of {self} is computed here only for an integral domain, where it is "
                    f"Frac(R), but {self} is not known to be an integral domain"
                )
                return self.fraction_field()

        class ElementMethods:
            def is_regular(self) -> bool:
                r"""Return whether this scalar is a non-zerodivisor.

                Multiplication by ``r`` is injective exactly when nothing
                nonzero is killed by it, that is when the colon ideal
                ``(0 : r)`` is zero.  Over a domain that reduces to being
                nonzero, which is a theorem about domains rather than a second
                definition.
                """

                ring = self.parent()
                if ring in OwnedRings().Commutative().NoZeroDivisors():
                    return not self.is_zero()
                zero_ideal = ring.ideal(ring.zero())
                return zero_ideal.colon(ring.ideal(self)) == zero_ideal

    class ParentMethods:
        def _selected_local_ring_construction(self):
            r"""Return an installed local-ring datum, or ``None``.

            Protected ring-construction contract under OWN-05. Ordinary local
            rings such as fields and prime localizations compute their residue
            data through their mathematical owners and therefore return
            ``None`` here. Native/adically completed/dual-number parents that
            retain a selected maximal-ideal quotient override this endpoint.
            """
            return None

        def _selected_engine_ring(self):
            r"""Return the private computation parent selected for this ring.

            Protected ring-realization contract under OWN-05--07.  The only
            permitted callers are the ring owner's lowering/raising dispatchers
            and ring-local computation adapters after a mathematical operation
            has already been selected.  A ring with no separate foreign
            realization computes in its owned parent itself; engine-backed
            constructions override this method at their construction owner.
            Raw computation parents never leave those adapters.
            """
            return self

        def _engine_element(self, element):
            r"""Lower an owned element for a self-realized ring adapter."""
            return self(element)

        def _from_engine_element(self, element):
            r"""Raise a self-realized computation value into this ring."""
            return self(element)

        def _fresh_free_module_on(self, labels, **options):
            r"""Return the free ``R``-module on ``labels``, for this ring ``R``.

            A ring that is also a free module over a smaller base -- a number
            field over the rationals, an order over the integers -- is still
            the ring its modules are over here; the free modules over the
            smaller base are asked of that base.
            """
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                _fresh_free_module_on,
            )

            return _fresh_free_module_on(
                self,
                labels,
                **options,
            )

        def free_module(self, rank_or_index_set):
            r"""Return the canonical free module over this ring on the stated labels."""
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                _module_generating_set,
                _owned_free_module_on,
            )

            return _owned_free_module_on(
                self,
                _module_generating_set(rank_or_index_set),
            )

        def polynomial_ring(self, *args, **kwargs):
            r"""Return the polynomial ring over this ring with the stated variables."""
            from dzack_research.preamble.categories.algebras.free_algebras import (
                _polynomial_ring,
            )

            return _polynomial_ring(self, *args, **kwargs)

        def laurent_polynomial_ring(self, *args, **kwargs):
            r"""Return the Laurent polynomial ring over this ring with the stated variables."""
            from dzack_research.preamble.categories.algebras.free_algebras import (
                _laurent_polynomial_ring,
            )

            return _laurent_polynomial_ring(self, *args, **kwargs)

        def power_series_ring(self, *args, **kwargs):
            r"""Return the formal power-series ring over this ring."""
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                FormalPowerSeriesRings,
            )

            return FormalPowerSeriesRings(self)(*args, **kwargs)

        def matrix_space(self, nrows, ncols=None):
            r"""Return the finite matrix Mor over this ring, as an algebra when square."""
            from dzack_research.preamble.categories.algebras.algebras import (
                _require_matrix_algebra,
            )
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                _matrix_space,
            )

            return _require_matrix_algebra(_matrix_space(self, nrows, ncols))

        def formal_spectrum(self, ideal_of_definition):
            r"""Return ``Spf(self, ideal_of_definition)``."""
            from dzack_research.preamble.categories.schemes.formal_schemes import (
                FormalSpectrum,
            )

            return FormalSpectrum(self, ideal_of_definition)

        def cyclic_cover_presentation(self, branch_coefficient, degree):
            r"""Return ``self[z]/(z^degree - branch_coefficient)``."""
            from dzack_research.preamble.categories.algebras.cyclic_cover_algebras import (
                _cyclic_cover_presentation,
            )

            return _cyclic_cover_presentation(self, branch_coefficient, degree)

        def __pow__(self, exponent):
            r"""Return the free module ``R^n`` through the owned module constructor."""

            return self.free_module(exponent)

        @cached_method
        def unit_group(self):
            r"""Return ``self^×``, the group of units of this ring."""
            return _unit_group(self)

        @cached_method
        def regular_module(self):
            r"""Return ``{}_R R``, the rank-one left regular module.

            The ring remains the scalar object; the module is the canonical
            free rank-one object on which ``r`` acts by left multiplication.
            If this ring already carries that canonical finite-free module
            structure, the regular module is the ring itself; otherwise it is
            the canonical rank-one based free module over this ring.
            """
            from dzack_research.preamble.categories.modules.pure.modules import (
                FinitelyGeneratedFreeModules,
            )

            if self in FinitelyGeneratedFreeModules(self):
                return self
            return self.free_module(1)

        def __getitem__(self, names):
            r"""Use standard polynomial/algebraic adjunction syntax on an owned ring."""
            from dzack_research.preamble.categories.algebras.group_algebras import (
                _group_algebra,
            )
            from dzack_research.preamble.categories.group.groups import OwnedGroups

            match names:
                case str():
                    return self.polynomial_ring(names)
                case _ if names in OwnedGroups():
                    return _group_algebra(self, names)
                case tuple() if all(isinstance(part, str) for part in names):
                    return self.polynomial_ring(names)
                case list():
                    result = _own_if_ring(_engine_ring(self)[names])
                case _ if names in self:
                    return self
                case _:
                    result = _own_if_ring(_engine_ring(self)[names])

            if result not in OwnedRings():
                return result
            return result

        def predicate_subring(self, predicate, description, category=None):
            r"""Return the represented subring of elements satisfying ``predicate``."""
            return _predicate_subring(self, predicate, description, category)

        def Mor(self, codomain, category=None):
            rings = OwnedRings()
            if category is None or (isinstance(category, OwnedCategory) and category.is_subcategory(rings)):
                return rings.Mor(self, codomain)
            # A Sage category here is not a mathematical request: it is Sage's
            # coercion machinery asking for somewhere to keep a conversion map,
            # naming its own `SetsWithPartialMaps`.  `SageHom` would check that
            # this owned ring lies in that Sage category, which it does not and
            # need not (`ARC-00`).  Build the Mor directly at the engine
            # boundary instead, without the membership check.
            from sage.categories.homset import Homset as SageHomset

            return SageHomset(self, codomain, category=category, check=False)

        def _Hom_(self, codomain, category=None):
            rings = OwnedRings()
            if codomain not in rings:
                raise TypeError(
                    f"Mor({self}, {codomain}) in the category of rings needs a ring as codomain, but {codomain} is not a ring"
                )
            if category is not None and not category.is_subcategory(rings):
                raise TypeError(
                    f"{category} is not a subcategory of rings, so Mor({self}, {codomain}) cannot be formed in it"
                )
            return rings.Mor(self, codomain)

        def cardinality(self):
            r"""Return the exact represented cardinal of the underlying set."""
            from dzack_research.preamble.categories.sets.cardinals import (
                aleph0,
                cardinal,
                continuum,
            )

            category = self.category()
            if category.is_subcategory(owned_sets.FiniteSets()):
                from sage.rings.integer_ring import ZZ as SageZZ

                integers = _own_ring(SageZZ)
                return cardinal(_owned_engine_element(integers, SageZZ(_engine_ring(self).cardinality())))
            if category.is_subcategory(owned_sets.CountablyInfiniteSets()):
                return aleph0
            if category.is_subcategory(owned_sets.UncountableSets()):
                return continuum
            # No size placement on the ring: its underlying set may still be
            # constructed at a lower level, as M_n(R) is the free module R^(n^2).
            return super().cardinality()

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

            return owned_sets.finite_ordered_set(())

        def _lift_coefficient_to_presentation(self, value):
            return self(value)

        def _descend_coefficient_from_presentation(self, value):
            return self(value)

        def is_central(self, element):
            r"""Return whether ``element`` is central in the foundational ring regimes."""
            if element not in self:
                return False
            assert self in OwnedRings().Commutative(), (
                f"cannot decide whether {element} is central in {self}: centrality is computed here only in "
                "a commutative ring"
            )
            return True

        @cached_method
        def ring_center(self):
            r"""Return the centre ``Z(R)`` as a predicate-defined subring."""
            if self in OwnedRings().Commutative():
                return self
            return self.predicate_subring(
                self.is_central,
                "z commutes with every element",
                OwnedRings().Commutative(),
            )

        def fraction_field(self):
            r"""Return the fraction field through its nonzero-element localization."""
            if self in OwnedRings().Division().Commutative():
                return self
            if self not in OwnedRings().Commutative().NoZeroDivisors():
                raise ValueError(
                    f"{self} is not an integral domain, so it has no fraction field; "
                    "inverting its regular elements is the total quotient-ring construction"
                )
            return self.fraction_field_localization().fraction_field_realization()


class OwnedOrderedRings(OwnedCategory):
    r"""Rings with a chosen total order compatible with the operations.

    A ring can support several orders (a real quadratic field has two), so
    the order is a chosen datum.
    """

    def an_object(self):
        r"""The integers with their usual order."""
        return _own_ring(SageZZ)

    def super_categories(self):
        return [OwnedRings()]

    class ElementMethods:
        def __abs__(self):
            zero = self.parent().zero()
            return self if self >= zero else -self


def OwnedIntegralDomains():
    r"""``OwnedRings().Commutative().NoZeroDivisors()``, the session name for integral domains."""
    return OwnedRings().Commutative().NoZeroDivisors()


def OwnedPrincipalIdealDomains():
    r"""``OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals()``, the session name for PIDs."""
    return OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals()


def _engine_krull_dimension(ring):
    return _krull_dimension_of_engine(_engine_ring(ring))


def _krull_dimension_of_engine(engine):
    r"""The Krull dimension of a Sage computation ring, as an owned integer.

    ``OWN-06`` adapter.  Sage answers ``krull_dimension`` itself on every
    engine but one: the generic quotient ``S/I`` of a multivariate polynomial
    ring falls to the ``CommutativeRings`` default, which raises.  There
    ``dim S/I = dim I``, the dimension Singular computes for ``I`` (TRAPS.md).
    A quotient of a principal ideal domain ``D/(d)`` -- ``Zmod(n)`` is one, over
    ``ZZ`` -- has dimension zero for ``d != 0`` and the dimension of ``D`` for
    ``d = 0``.  A univariate quotient ``K[x]/(f)`` answers its own.
    """
    match engine:
        case PolynomialQuotientRing_generic():
            dimension = engine.krull_dimension()
        case QuotientRing_generic():
            cover = engine.cover_ring()
            defining = engine.defining_ideal()
            match cover in SagePrincipalIdealDomains(), defining.is_zero():
                case (True, True):
                    dimension = cover.krull_dimension()
                case (True, False):
                    dimension = SageZZ.zero()
                case _:
                    dimension = defining.dimension()
        case _:
            dimension = engine.krull_dimension()
    return _owned_engine_element(SageZZ, SageZZ(dimension))


def OwnedNoetherianRings():
    r"""``OwnedRings().Commutative().Noetherian()``, the session name for Noetherian rings."""
    return OwnedRings().Commutative().Noetherian()


def OwnedArtinianRings():
    r"""``OwnedRings().Commutative().Artinian()``, the session name for Artinian rings."""
    return OwnedRings().Commutative().Artinian()


def OwnedLocalRings():
    r"""``OwnedRings().Commutative().Local()``, the session name for local rings."""
    return OwnedRings().Commutative().Local()


class OwnedAdicallyCompleteRings(OwnedCategory):
    r"""Commutative rings with a chosen ideal of definition for which they are adically complete.

    The ideal is a chosen datum: every ring is complete for its zero ideal.
    """

    def an_object(self):
        r"""The 2-adic integers, complete for the ideal (2)."""
        return _own_ring(SageZZ).adic_completion(2)

    def super_categories(self):
        return [OwnedRings().Commutative()]

    class ParentMethods:
        def is_adically_complete(self):
            return True

        def ideal_of_definition(self):
            return self._adic_defining_ideal


def OwnedCompleteLocalRings():
    r"""``OwnedRings().Commutative().Local().Complete()``, the session name for complete local rings."""
    return OwnedRings().Commutative().Local().Complete()


def OwnedDivisionRings():
    r"""``OwnedRings().Division()``, the session name for division rings."""
    return OwnedRings().Division()


def OwnedFields():
    r"""``OwnedRings().Division().Commutative()``, the session name for fields."""
    return OwnedRings().Division().Commutative()


class OwnedOrders(OwnedCategory):
    r"""Orders: integral domains finitely generated as ``ZZ``-modules (Neukirch I §12).

    The number field is ``Frac(O) = O (x) QQ``, determined by the ring, and
    the category is the intersection of its two declared supercategories:
    finite generation is the module axiom on the ring as a ``ZZ``-algebra.
    The class is the home of the operations of orders (their embeddings, the
    adjunction with number fields, maximality); it adds no condition.
    """

    def an_object(self):
        r"""The integers, the ring of integers of the rationals."""
        return _own_ring(SageZZ)

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras

        return [
            Algebras(_owned_integers()).Associative().Unital().Commutative().FinitelyGenerated(),
            OwnedRings().Commutative().NoZeroDivisors().Noetherian(),
        ]

    def fraction_field_adjunction(self):
        r"""Return ``Frac -| O`` from orders to number fields."""
        from dzack_research.preamble.categories.functors.orders_number_fields import (
            _order_number_field_adjunction,
        )

        return _order_number_field_adjunction()

    @cached_method(key=lambda self, domain, codomain: (id(domain), id(codomain)))
    def Mor(self, domain, codomain):
        r"""Return the exact embedding Mor between two represented orders."""
        if domain not in self or codomain not in self:
            raise TypeError(
                f"an embedding of orders needs an order as domain and codomain, but got {domain} and {codomain}"
            )
        from dzack_research.preamble.categories.rings.embeddings import OrderMor

        return OrderMor(domain, codomain)

    class ParentMethods:
        def Mor(self, codomain, category=None):
            orders = OwnedOrders()
            if codomain in orders and (
                category is None
                or (
                    isinstance(category, OwnedCategory)
                    and category.is_subcategory(orders)
                )
            ):
                return orders.Mor(self, codomain)
            return super().Mor(codomain, category=category)

        def _Hom_(self, codomain, category=None):
            orders = OwnedOrders()
            if codomain in orders and (
                category is None
                or (
                    isinstance(category, OwnedCategory)
                    and category.is_subcategory(orders)
                )
            ):
                return orders.Mor(self, codomain)
            return super()._Hom_(codomain, category=category)

        def is_maximal(self) -> bool:
            r"""Return whether this is the maximal order of its fraction field."""
            engine = _engine_ring(self)
            if engine is SageZZ:
                return True
            return bool(engine.is_maximal())


def PrimeFields():
    r"""``OwnedRings().Division().Commutative().Prime()``, the session name for prime fields."""
    return OwnedRings().Division().Commutative().Prime()


@cached_function
def _unit_group(ring):
    r"""Return \(R^\times\), the group of units of the owned ring ``ring``.

    A ring is a monoid under multiplication, and its invertible elements are a
    submonoid: the identity is invertible, and a product of invertibles is
    invertible.  That submonoid is a group, because every one of its elements
    has an inverse by the very predicate that admitted it, so the group law is
    the ring's multiplication and nothing is chosen.

    Invertibility is asked of the ring element.  A ring whose elements do not
    decide it has no represented unit group, and that absence is a gap on the
    element interface rather than a second construction here.
    """
    from dzack_research.preamble.categories.group.groups import OwnedGroups

    assert ring in OwnedRings(), (
        f"the unit group R^* needs a ring R of this session, but {ring!r} is not one"
    )
    units = ring.predicate_submonoid(
        lambda element: element.is_unit(),
        f"{ring}^×",
        placements=(OwnedGroups(),),
    )
    return units


class UnitGroupFunctor(Functor):
    r"""\(R\mapsto R^\times\) and \(f\mapsto f|_{R^\times}\), from rings to groups.

    A ring morphism carries a unit to a unit: from \(rs = 1\) it gives
    \(f(r)f(s) = 1\), so the restriction is defined with no further data, and
    functoriality is the functoriality of restriction.

    Applied to \(\operatorname{End}_{\mathbf C}(X)\) this is
    \(\operatorname{Aut}_{\mathbf C}(X)\): an endomorphism is invertible in the
    endomorphism ring exactly when it is an isomorphism of \(X\).
    """

    def __init__(self) -> None:
        from dzack_research.preamble.categories.group.groups import OwnedGroups

        super().__init__(OwnedRings(), OwnedGroups())

    def _apply_object(self, ring):
        return ring.unit_group()

    def _apply_morphism(self, morphism):
        source = self.object_image(morphism.domain())
        target = self.object_image(morphism.codomain())
        return SetMorphism(
            source.Mor(target),
            lambda unit: target(morphism(unit)),
        )

    def _repr_(self):
        return "Unit group functor"


def _center_transport_of_ring_isomorphism(morphism):
    r"""Restrict one ring isomorphism direction to represented centers."""
    source = morphism.domain()
    target = morphism.codomain()
    source_center = source.ring_center()
    target_center = target.ring_center()

    def ambient_source(element):
        if source_center is source:
            return source(element)
        return source_center.inclusion()(element)

    return source_center.Mor(target_center)(
        lambda element: target_center(morphism(ambient_source(element))),
    )


class RingCenterFunctor(Functor):
    r"""The ring center functor on the maximal subgroupoid of owned rings.

    A general ring morphism need not preserve centers.  An isomorphism does:
    if ``f : R -> S`` is invertible, ``z`` commutes with every element of
    ``R``, and ``s in S``, then writing ``s=f(r)`` gives
    ``f(z)s=f(zr)=f(rz)=sf(z)``.  Thus the center construction is functorial
    exactly on the core without a generator or surjectivity heuristic.
    """

    def __init__(self) -> None:
        core = OwnedRings().Core()
        super().__init__(core, CommutativeRings())

    def _apply_object(self, ring):
        return ring.ring_center()

    def _apply_morphism(self, isomorphism):
        return _center_transport_of_ring_isomorphism(isomorphism.forward())

    def _repr_(self):
        return "Ring center functor Core(Ring) -> CRing"


class OwnedCategoryOverBaseRing(CategoryPacketMethods, OwnedParameterizedCategory):
    r"""A category over a ring, normalized to the session's owned ring."""

    def parameter_category(self):
        r"""Return the mathematical domain of the base-ring parameter."""
        return OwnedRings()

    @classmethod
    def an_instance(cls):
        r"""Return this category over the rational numbers.

        Sage's ``Category_over_base.an_instance`` (category_types.py) returns
        ``cls(QQ)``; here ``QQ`` is the owned rational field.
        """
        return cls(_own_ring(SageQQ))

    @staticmethod
    def __classcall__(cls, base_ring, *args, **kwargs):
        # During construction of an engine-backed owned ring, ``self`` already
        # exists and already carries its engine, but ``Parent.__init__`` has not
        # yet installed its category.  A self-referential placement such as
        # ``Algebras(R).Associative().Unital().Commutative()`` must therefore accept that constructing
        # parent directly rather than asking category membership of an object
        # whose category is precisely what is being built.
        match base_ring:
            case _OwnedRingBootstrapParent():
                pass
            case _:
                base_ring = _owned_ring(base_ring)
        return OwnedParameterizedCategory.__classcall__(
            cls,
            base_ring,
            *args,
            **kwargs,
        )

    def __init__(self, base_ring) -> None:
        match base_ring:
            case _OwnedRingBootstrapParent():
                # The host type is itself the owned-ring construction.  During
                # its bootstrap the category being built is precisely what
                # will establish ``base_ring in OwnedRings()``; asking that
                # membership here would make the declaration depend on its
                # own result.  Fix the parameter and construct the category
                # without re-asking the theorem under construction.
                self._owned_parameter = base_ring
                OwnedCategory.__init__(self)
            case _:
                OwnedParameterizedCategory.__init__(self, base_ring)

    def base_ring(self):
        return self.base()

def _cross_engine_ring_value(value):
    r"""Cross a private engine-ring value back into the owned universe when possible."""
    parent = element_parent(value)
    if parent in SageRings():
        return _owned_engine_element(parent, value)
    return value


class OwnedFactorization(SageObject):
    r"""A finite factorization retaining its unit and factor multiplicities."""

    def __init__(self, parent, unit, factors) -> None:
        self._parent = parent
        self._unit = _owned_engine_element(parent, unit)
        engine_pairs = tuple(factors)
        owned_factors = tuple(
            _owned_engine_element(parent, factor) for factor, _multiplicity in engine_pairs
        )
        indices = owned_sets.finite_ordered_set(owned_factors)
        multiplicities = {
            factor: _owned_engine_element(SageZZ, SageZZ(multiplicity))
            for factor, (_engine_factor, multiplicity) in zip(
                owned_factors, engine_pairs, strict=True
            )
        }
        self._factors = owned_sets.finite_indexed_family(
            indices,
            multiplicities.__getitem__,
            name=f"Factor multiplicities in {parent}",
        )

    def parent_ring(self):
        return self._parent

    def unit(self):
        return self._unit

    def factor_multiplicities(self):
        return self._factors

    def cardinality(self):
        return self._factors.cardinality()

    def items(self):
        return self._factors.items()

    def reconstruct(self):
        product = self.unit()
        for factor, multiplicity in self.items():
            product = product * factor ** int(multiplicity)
        return product

    def _repr_(self):
        return f"Factorization of an element of {self.parent_ring()}"


def _proper_restriction_base_ring(ring):
    r"""Return the next proper scalar base in the represented ring tower.

    A represented ring keeps its distinguished construction base through
    ``base_ring()``.  When that base is the ring itself, the canonical map
    from the initial ring still makes every module or algebra over it a module
    or algebra over ``ZZ``.  The integers are the terminal case and therefore
    have no proper restriction base.

    The engine test is essential while ``ZZ`` itself is being constructed:
    asking ``_own_ring(SageZZ)`` again before its cache entry exists would
    recursively start a second construction of the same parent.
    """
    base = ring.base_ring()
    if base is None:
        return None if _engine_ring(ring) is SageZZ else _own_ring(SageZZ)
    if base is not ring:
        return _owned_ring(base)
    if _engine_ring(ring) is SageZZ:
        return None
    return _own_ring(SageZZ)


def _engine_multiplicative_generator(engine):
    r"""Return the selected engine's multiplicative generator at the private boundary."""
    return engine.multiplicative_generator()



def _owned_monomial_text(variable_names, exponent):
    # A univariate polynomial keys its terms by an integer exponent, a
    # multivariate one by an exponent vector (Sage's ETuple).
    match len(variable_names):
        case 1:
            powers = (exponent,)
        case _:
            powers = tuple(exponent)
    factors = []
    for variable, power in zip(variable_names, powers, strict=False):
        power = int(power)
        if power == 0:
            continue
        factors.append(variable if power == 1 else f"{variable}^{power}")
    return "*".join(factors) or "1"


def _owned_polynomial_text(parent, backend_value) -> str:
    base = parent.base_ring()
    variables = tuple(parent.variable_names())
    terms = []
    for exponent, coefficient in backend_value.dict().items():
        owned_coefficient = _owned_engine_element(base, coefficient)
        terms.append((exponent, owned_coefficient))
    if not terms:
        return "0"
    return repr_lincomb(
        terms,
        repr_monomial=lambda exponent: _owned_monomial_text(variables, exponent),
        strip_one=True,
    )


def _owned_ring_element_text(element) -> str:
    parent = element.parent()
    engine = parent._engine
    value = element._backend()
    if engine is SageZZ:
        return str(int(value))
    if engine is SageQQ:
        numerator = int(value.numerator())
        denominator = int(value.denominator())
        return str(numerator) if denominator == 1 else f"{numerator}/{denominator}"
    if isinstance(engine, (PolynomialRing_generic, MPolynomialRing_base)):
        return _owned_polynomial_text(parent, value)
    kind = parent._preamble_ring_display_kind
    if kind == "modular":
        return f"[{int(value.lift())}]"
    if kind == "real":
        return repr(float(value))
    if kind == "complex":
        return repr(complex(value))
    if parent._preamble_is_number_field():
        polynomial = value.polynomial()
        owned_parent = _own_ring(polynomial.parent())
        return repr(_owned_engine_element(owned_parent, polynomial))
    if parent._preamble_is_number_field_order():
        coefficients = tuple(value.list())
        owned = tuple(_cross_engine_ring_value(coefficient) for coefficient in coefficients)
        return f"coordinates {owned} in {parent}"
    if kind == "padic":
        valuation = value.valuation()
        precision = value.precision_absolute()
        residue = value.residue()
        return (
            f"p-adic element with residue {int(residue)}, "
            f"valuation {valuation}, precision {precision}"
        )
    if isinstance(engine, QuotientRing_generic) and isinstance(
        engine.cover_ring(), (PolynomialRing_generic, MPolynomialRing_base)
    ):
        cover = _own_ring(engine.cover_ring())
        return f"[{_owned_polynomial_text(cover, value.lift())}]"
    return f"element of {parent}"


class _OwnedRingElement(RingElement):
    r"""An element of an owned ring with a private backend realization."""

    def __init__(self, parent, backend_value) -> None:
        RingElement.__init__(self, parent)
        self._backend_value = backend_value

    def _backend(self):
        r"""Return the private backend value for boundary code in this module."""
        return self._backend_value

    def _operator_operand(self, value):
        r"""``value`` in this ring along the canonical map, or ``NotImplemented`` for Python dispatch.

        When the canonical map runs from this ring into the other operand's ring
        and not back, the operation lives in the other ring, and
        ``NotImplemented`` lets Python ask the other operand: ``2 * q.one()``
        for a quotient ``q`` of ``QQ[x,y]`` is an element of ``q``, not the
        integer that the lift of ``1`` would convert to.  Otherwise the value
        is read in this ring when it is one of its elements.
        """
        ring = self.parent()
        other_parent = element_parent(value)
        if (
            other_parent is not ring
            and other_parent in OwnedRings()
            and _engine_ring(other_parent).has_coerce_map_from(_engine_ring(ring))
            and not _engine_ring(ring).has_coerce_map_from(_engine_ring(other_parent))
        ):
            return NotImplemented
        if value not in ring:
            return NotImplemented
        return ring(value)
    def _add_(self, other):
        parent = self.parent()
        return _owned_engine_element(parent, self._backend() + other._backend())

    def __add__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return self._add_(other)

    __radd__ = __add__

    def __sub__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return self._add_(-other)

    def __rsub__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return other._add_(-self)

    def _mul_(self, other):
        parent = self.parent()
        return _owned_engine_element(parent, self._backend() * other._backend())

    def _lmul_(self, scalar):
        r"""``r * a`` for ``r`` in the ring this ring is presented over: the engine's own action.

        The engine presents this ring over its base, so ``r`` enters through
        the engine's map from its base and multiplies ``a`` there.  The algebra
        root derives ``algebra_structure_morphism`` from this action as
        ``r |-> rho(r)(1)``, so the action is never read back from it.
        """
        parent = self.parent()
        return parent(parent.base_ring()(scalar)) * self

    def __mul__(self, other):
        r"""``r x`` for a scalar of this ring and an element over it.

        A module over this ring registers the action of this ring on its
        elements, and the host's coercion model finds that action for ``r*m``.
        It finds it only when this method defers, and this method cannot defer
        whenever this ring can convert the other element: the line below would
        then multiply in this ring and answer in it, so ``3`` times the identity
        of the Gaussian field would be the rational three rather than the
        Gaussian three.  A number field, a polynomial ring and every other
        algebra over this ring holds such elements -- the ones this ring already
        names.

        So the scalar action is taken here, on the element's own parent, before
        the conversion is tried.  It is the same operation the registered action
        performs, reached on the one route the coercion model does not see.
        """
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        other_parent = element_parent(other)
        if other_parent is not self.parent() and other_parent in Modules(self.parent()):
            return other_parent.scalar_multiple(self, other)
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return _OwnedRingElement._mul_(self, other)

    def __rmul__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return _OwnedRingElement._mul_(other, self)

    def _neg_(self):
        return _owned_engine_element(self.parent(), -self._backend())

    def _richcmp_(self, other, op):
        if element_parent(other) is not self.parent():
            other = self._operator_operand(other)
            if other is NotImplemented:
                return NotImplemented
        return richcmp(self._backend(), other._backend(), op)

    def _ordered_comparison(self, other, op):
        if self.parent() not in OwnedOrderedRings():
            return NotImplemented
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return bool(richcmp(self._backend(), other._backend(), op))

    def __lt__(self, other):
        return self._ordered_comparison(other, op_LT)

    def __le__(self, other):
        return self._ordered_comparison(other, op_LE)

    def __gt__(self, other):
        return self._ordered_comparison(other, op_GT)

    def __ge__(self, other):
        return self._ordered_comparison(other, op_GE)

    def __eq__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            # Not this ring's decision: a cardinal, say, knows whether it
            # equals a natural number of the ring, so Python asks it next.
            return NotImplemented
        return bool(self._backend() == other._backend())

    def __ne__(self, other):
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented
        return not equal

    def __hash__(self):
        # Equal elements hash equally: ``__eq__`` identifies this element with
        # the literal it converts from, so the hash is the value's, as for
        # Sage's own elements (``hash(Integer(1)) == hash(1)``).
        return hash(self._backend())

    def __bool__(self):
        return bool(self._backend())

    def __int__(self):
        return int(self._backend())

    def __float__(self):
        return float(self._backend())

    def __complex__(self):
        return complex(self._backend())

    def _repr_(self):
        return _owned_ring_element_text(self)

    def _latex_(self):
        text = _owned_ring_element_text(self).replace("_", r"\_")
        return rf"\text{{{text}}}"

    def is_zero(self):
        return bool(self._backend() == self.parent()._engine.zero())

    def is_one(self):
        return bool(self._backend() == self.parent()._engine.one())

    def is_unit(self):
        return bool(self._backend().is_unit())

    def inverse_of_unit(self):
        if not self.is_unit():
            raise ZeroDivisionError(f"{self} is not a unit")
        return _owned_engine_element(self.parent(), self._backend() ** -1)

    def __invert__(self):
        return _owned_engine_element(self.parent(), ~self._backend())

    def __mod__(self, other):
        r"""The remainder of Euclidean division by ``other``, as the engine ring computes it."""
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return _owned_engine_element(self.parent(), self._backend() % other._backend())

    def __rmod__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        return _owned_engine_element(self.parent(), other._backend() % self._backend())

    def __truediv__(self, other):
        other = self._operator_operand(other)
        if other is NotImplemented:
            return NotImplemented
        value = self._backend() / other._backend()
        value_parent = element_parent(value)
        if value_parent is self.parent()._engine:
            return _owned_engine_element(self.parent(), value)
        if value_parent in SageRings():
            return _owned_engine_element(value_parent, value)
        return value

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            modulus = self._operator_operand(modulus)
            if modulus is NotImplemented:
                return NotImplemented
            value = pow(self._backend(), exponent, modulus._backend())
        else:
            try:
                exponent = exponent.__index__()
            except AttributeError:
                return NotImplemented
            value = self._backend() ** exponent
        value_parent = element_parent(value)
        if value_parent is self.parent()._engine:
            return _owned_engine_element(self.parent(), value)
        if value_parent in SageRings():
            return _owned_engine_element(value_parent, value)
        return value

    def __rtruediv__(self, other):
        numerator = self._operator_operand(other)
        if numerator is NotImplemented:
            return NotImplemented
        return numerator.__truediv__(self)

    def __floordiv__(self, other):
        other = self.parent()(other)
        return _owned_engine_element(self.parent(), self._backend() // other._backend())

    def quo_rem(self, other):
        other = self.parent()(other)
        quotient, remainder = self._backend().quo_rem(other._backend())
        ring = self.parent()
        product = owned_sets.Sets().product((ring, ring))
        return product((
            _owned_engine_element(ring, quotient),
            _owned_engine_element(ring, remainder),
        ))

    def divides(self, other):
        other = self.parent()(other)
        return bool(self._backend().divides(other._backend()))

    def gcd(self, other):
        other = self.parent()(other)
        return _owned_engine_element(self.parent(), self._backend().gcd(other._backend()))

    def xgcd(self, other):
        r"""Return ``(g,s,t)`` with ``g = s*self + t*other`` in this ring."""
        other = self.parent()(other)
        gcd, left, right = self._backend().xgcd(other._backend())
        ring = self.parent()
        product = owned_sets.Sets().product((ring, ring, ring))
        return product((
            _owned_engine_element(ring, gcd),
            _owned_engine_element(ring, left),
            _owned_engine_element(ring, right),
        ))

    def lcm(self, other):
        other = self.parent()(other)
        return _owned_engine_element(self.parent(), self._backend().lcm(other._backend()))

    def valuation(self, prime):
        prime = self.parent()(prime)
        integers = _own_ring(SageZZ)
        return _owned_engine_element(integers, SageZZ(self._backend().valuation(prime._backend())))

    def prime_divisors(self):
        r"""Return the distinct prime divisors as an owned finite ordered set."""
        return owned_sets.finite_ordered_set(
            tuple(
                _owned_engine_element(self.parent(), prime)
                for prime in self._backend().prime_divisors()
            )
        )

    def is_prime(self):
        return bool(self._backend().is_prime())

    def divisors(self):
        r"""Return the positive divisors as an owned finite ordered set."""
        return owned_sets.finite_ordered_set(
            tuple(
                _owned_engine_element(self.parent(), divisor)
                for divisor in self._backend().divisors()
            )
        )

    def euler_phi(self):
        r"""Return Euler's totient as an owned nonnegative integer."""
        integers = _own_ring(SageZZ)
        return _owned_engine_element(integers, SageZZ(_engine_euler_phi(self._backend())))

    def number_of_divisors(self):
        r"""Return the number of positive divisors as an owned integer."""
        integers = _own_ring(SageZZ)
        return _owned_engine_element(integers,
            SageZZ(_engine_number_of_divisors(self._backend()))
        )

    def factor(self):
        r"""Return the engine factorization crossed into owned factors and multiplicities."""
        factorization = self._backend().factor()
        return OwnedFactorization(
            self.parent(),
            factorization.unit(),
            tuple(factorization),
        )

    def is_irreducible(self):
        return bool(self._backend().is_irreducible())

    def roots(self, ring=None):
        r"""Return the finite family of roots indexed by the roots themselves."""
        if ring is None:
            backend_roots = tuple(self._backend().roots())
        else:
            ring = _owned_ring(ring)
            backend_roots = tuple(self._backend().roots(_engine_ring(ring)))
        if ring is None:
            owned_pairs = tuple(
                (
                    _cross_engine_ring_value(root),
                    _owned_engine_element(SageZZ, SageZZ(multiplicity)),
                )
                for root, multiplicity in backend_roots
            )
        else:
            owned_pairs = tuple(
                (
                    _owned_engine_element(ring, root),
                    _owned_engine_element(SageZZ, SageZZ(multiplicity)),
                )
                for root, multiplicity in backend_roots
            )
        indices = owned_sets.finite_ordered_set(tuple(root for root, _multiplicity in owned_pairs))
        multiplicities = dict(owned_pairs)
        return owned_sets.finite_indexed_family(
            indices,
            multiplicities.__getitem__,
            name=f"Roots of {self}",
        )

    def discriminant(self):
        return _cross_engine_ring_value(self._backend().discriminant())

    def resultant(self, other):
        other = self.parent()(other)
        return _cross_engine_ring_value(self._backend().resultant(other._backend()))

    def splitting_field(self):
        r"""Return the owned splitting field of this polynomial.

        Sage requires a presentation name even though the splitting field is
        the mathematical output.  Keep that choice private, then refine the
        crossed ring through the number-field owner so field operations such
        as ``degree`` remain available.
        """
        from dzack_research.preamble.categories.rings.number_fields import (
            _own_number_field,
        )

        return _own_number_field(self._backend().splitting_field("a"))

    def factorial(self):
        return _owned_engine_element(self.parent(), self._backend().factorial())

    def binomial(self, m):
        r"""The binomial coefficient of this element over the natural number ``m``."""
        return _owned_engine_element(self.parent(), self._backend().binomial(int(m)))

    def is_square(self):
        return bool(self._backend().is_square())

    def sqrt(self):
        return _cross_engine_ring_value(self._backend().sqrt())

    def numerator(self):
        value = self._backend().numerator()
        parent = value.parent()
        return _owned_engine_element(parent, value)

    def denominator(self):
        value = self._backend().denominator()
        parent = value.parent()
        return _owned_engine_element(parent, value)

    def additive_order(self):
        value = self._backend().additive_order()
        return _owned_engine_element(SageZZ, SageZZ(value))

    def multiplicative_order(self):
        value = self._backend().multiplicative_order()
        return _owned_engine_element(SageZZ, SageZZ(value))

    def degree(self):
        value = self._backend().degree()
        return _owned_engine_element(SageZZ, SageZZ(value))

    def trace(self):
        return _cross_engine_ring_value(self._backend().trace())

    def norm(self):
        return _cross_engine_ring_value(self._backend().norm())

    def minpoly(self):
        polynomial = self._backend().minpoly()
        return _owned_engine_element(polynomial.parent(), polynomial)


class _PredicateSubringElement(_OwnedRingElement):
    r"""The shared native scalar realization with this subring as its parent.

    Computation may use the larger ring, but results re-enter the predicate
    subring. A unit of the larger ring is a unit here exactly when its inverse
    lies here; field arithmetic must not classify every nonzero subring
    element as a unit.
    """

    def _repr_(self):
        return repr(self.parent().inclusion()(self))

    def _latex_(self):

        return latex(self.parent().inclusion()(self))

    def __call__(self, *arguments, **options):
        r"""Apply this element when its ambient ring element is itself callable.

        A predicate subring changes the parent that records membership; it does
        not erase operations intrinsic to the selected ambient element. This is
        needed, for example, for central elements of an endomorphism ring, whose
        ambient elements are morphisms and therefore evaluate on module
        elements. Non-callable ambient elements retain ordinary Python's
        TypeError behavior.
        """
        ambient = self.parent().inclusion()(self)
        if not callable(ambient):
            raise TypeError(f"{ambient!r} is not callable")
        return ambient(*arguments, **options)

    def is_zero(self):
        return self == self.parent().zero()

    def is_one(self):
        return self == self.parent().one()

    def is_unit(self):
        if (self == self.parent().one()) is True or (self == -self.parent().one()) is True:
            return True
        value = self.parent().inclusion()(self)
        decision = value.is_unit()
        if decision is False:
            return False
        assert decision is True, (
            f"cannot decide whether {self} is a unit: it is undecided whether its image {value} is a unit "
            f"in {value.parent()}"
        )
        return value.inverse_of_unit() in self.parent()


class _OwnedIntegerElement(_OwnedRingElement):
    r"""An integer engine value implementing Python's exact index protocol.

    ``__index__`` is not a truncating conversion from an arbitrary ring.
    The private ring engine selects this element realization only for ZZ;
    sets and other consumers then use the native protocol without importing
    the ring constructor or inspecting its engine.
    """

    def __index__(self) -> int:
        return int(self)


class _OwnedRingParent(UniqueRepresentation, Parent):
    r"""An owned ring parent with one private computational realization.

    The parent and its elements belong to the preamble universe.  ``engine``
    is implementation state only; raw backend elements enter through
    ``_from_engine_element`` and leave through ``_engine_element``.
    """

    _native_module_basis = None


    @lazy_attribute
    def Element(self):
        r"""The engine-specific element realization consumed by Sage Parent.

        ``sage/structure/parent.pyx:Parent.element_class`` reads ``self.Element``
        and combines it with the category's element methods.  This native
        representation boundary supplies exact indexing only for integers;
        it does not change the mathematical category of either ring.
        """
        match self._engine:
            case _ if self._engine is SageZZ:
                return _OwnedIntegerElement
            case _:
                return _OwnedRingElement

    def __init__(self, engine: Ring, *, base=None, category=None) -> None:
        r"""Construct over the scalar ring the level above declares.

        ``base`` is that ring.  A level sitting over a ring states its own base
        when it constructs through the level below -- the algebra level does --
        and carrying it to the host here is what makes the module level's
        ``base_ring()`` an answer of the construction rather than state a leaf
        restates.

        A ring the preamble adopts has no level above it to declare one, so it
        declares its own: the ring the engine presents it over, and itself when
        the engine presents it over nothing smaller, since a ring is free of
        rank one over its own scalars.  That is the same question the placement
        asks in order to read this ring as an algebra, and asking it here is
        what lets the module level's construction step -- registering the
        scalar action -- run on this route with nothing left to guess.
        """
        canonical_native = base is None and category is None
        self._engine = engine
        self._preamble_ring_display = None
        self._preamble_ring_display_kind = None
        self._local_ring_construction = None
        integer_bootstrap = canonical_native and engine is SageZZ
        # ``OwnedOrders`` is declared using ``Algebras(ZZ)``.  The canonical
        # integer object therefore has to be the parameter of that category
        # while its own initial placement is being assembled.  Seed only this
        # initial-object identity before category construction; every other
        # native ring keeps the ordinary post-Parent interning below.
        if integer_bootstrap:
            _owned_engine_ring.set_cache(self, engine)
            _owned_integers.set_cache(self)
        try:
            if base is None:
                scalars = _engine_scalar_ring(engine)
                base = self if scalars is None else _own_ring(scalars)
                category_base = None if scalars is None else base
            else:
                base = _own_ring(base)
                category_base = base
            placement = _owned_ring_category(
                engine,
                scalar_base=category_base,
                owned_ring=self,
            )
            if category is not None:
                from dzack_research.preamble.owned_category import owned_category_join

                placement = owned_category_join((placement, category))
            Parent.__init__(self, base=base, category=placement)
            realize_owned_category(self)

            # The primitive owned ring now exists as a Parent.  Cache every
            # canonical native ring before its regular module/algebra datum is
            # constructed so those owners reuse this exact scalar object.
            if canonical_native and not integer_bootstrap:
                _owned_engine_ring.set_cache(self, engine)

            _install_engine_selected_ring_data(self, engine)

            from dzack_research.preamble.categories.algebras.algebras import (
                _algebra_from_native_ring,
            )

            _algebra_from_native_ring(self, lambda left, right: left * right,
                self._from_engine_element(engine.one()), self._native_scalar_action,
                module_basis=self._native_module_basis)
        except BaseException:
            # A failed constructor cannot leave its incomplete owned ring in
            # the canonical cache. Remove only this exact object's entries.
            if canonical_native:
                key = _owned_engine_ring.get_key(engine)
                if _owned_engine_ring.cache.get(key) is self:
                    del _owned_engine_ring.cache[key]
                if engine is SageZZ:
                    key = _owned_integers.get_key()
                    if _owned_integers.cache.get(key) is self:
                        del _owned_integers.cache[key]
            raise



    def _native_scalar_action(self, scalar, element):
        r"""The native coefficient embedding before its module action is constructed."""
        element = self(element)
        return element._lmul_(self.base_ring()(scalar))

    def _from_engine_element(self, value):
        if element_parent(value) is not self._engine:
            value = self._engine(value)
        return self.element_class(self, value)

    def _engine_element(self, value):
        value = self(value)
        return value._backend()

    def _selected_engine_ring(self):
        r"""Return this native ring's selected private Sage realization."""
        return self._engine

    def _selected_local_ring_construction(self):
        r"""Return this native ring's selected local quotient datum, if any."""
        return self._local_ring_construction

    def __call__(self, value):
        r"""Construct an owned ring element without Sage coercion discovery."""
        return self._element_constructor_(value)

    def _element_constructor_(self, value):
        parent = element_parent(value)
        if parent is self:
            return value
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        if parent in Modules(self.base_ring()) and parent.unformed_module() is self:
            return parent._element_of_unformed_module(value)
        if parent is not None:
            if parent in OwnedRings():
                return self._from_engine_element(
                    self._engine(_engine_element(parent, value))
                )
            from dzack_research.preamble.categories.sets.set_categories import NN

            if parent is NN:
                return self._from_engine_element(self._engine(int(value)))
            if parent in SageRings() or parent is self._engine:
                raise TypeError(
                    f"cannot convert {value!r} into {self}: it is a raw Sage element of {parent}; construct it "
                    "from a ring of this session"
                )
        if isinstance(value, SageObject):
            raise TypeError(
                f"cannot convert {value!r} into {self}: it is a raw Sage object; construct it from an object "
                "of this session"
            )
        return self._from_engine_element(self._engine(value))

    def __contains__(self, value) -> bool:
        r"""Decide whether ``value`` represents an element of this ring.

        Sage distinguishes set membership from ``is_parent_of``: membership
        asks whether the value lies in the represented set, not whether this
        exact parent already owns its current representation.  Keep that
        distinction while making the admissible routes explicit.  Owned ring
        elements are lowered at the ring adapter and the selected Sage ring
        decides membership of the represented value; raw Sage elements remain
        outside the public owned universe.
        """
        source = element_parent(value)
        if source is self:
            return True
        # Sage's parent() of a value outside Sage (a Cartan type, a list) is
        # its Python class, which no category can be asked about.
        if not isinstance(source, Parent):
            return value in self._engine
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        if source in Modules(self.base_ring()) and source.unformed_module() is self:
            return True
        if source in OwnedRings():
            # An element on which the canonical map lands is in this ring.
            # Sage's FreeAlgebra answers `2 in F` False although F(2) is its
            # scalar two (TRAPS.md), so the coercion is asked first.
            represented = _engine_element(source, value)
            return self._engine.has_coerce_map_from(_engine_ring(source)) or represented in self._engine
        from dzack_research.preamble.categories.sets.set_categories import NN

        if source is NN:
            return True
        if source in SageRings() or isinstance(value, SageObject):
            return False
        return value in self._engine

    def _coerce_map_from_(self, source):
        r"""The owned rings that coerce into this one: those whose engine ring coerces into this ring's.

        A coercion is the canonical ring morphism, and the owned rings
        realize their engine rings, so the canonical morphisms between them
        are the engine's: \(\mathbb{Z}\to\mathbb{Q}\), \(R\to R[x]\),
        \(\mathcal{O}_K\to K\).  Sage builds the map from this ring's element
        constructor, which reads the source element through its engine.
        """
        match source:
            case _ if source in OwnedRings():
                return self._engine.has_coerce_map_from(_engine_ring(source))
            case _:
                return None

    def zero(self):
        return self._from_engine_element(self._engine.zero())

    def one(self):
        return self._from_engine_element(self._engine.one())

    def multiplicative_generator(self):
        return self._from_engine_element(_engine_multiplicative_generator(self._engine))

    def an_element(self):
        return self._from_engine_element(self._engine.an_element())

    def characteristic(self):
        integers = _own_ring(SageZZ)
        return _owned_engine_element(integers, SageZZ(self._engine.characteristic()))

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

    def _preamble_is_number_field_order(self):
        return self._engine is SageZZ or isinstance(self._engine, SageNumberFieldOrder)

    def is_projective(self) -> bool:
        r"""Projectivity as a module over the base ring.

        A ring is free of rank one over itself, a number-field order is
        free of finite rank over the integers (its integral basis), and a
        ring constructed with a native module basis over its base ring (a
        free algebra on its words) is free on that basis.  This is asked
        while the regular module is admitted into its free placement, so it
        is read from the construction's basis rather than that placement.
        """
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FramedFreeModules,
        )
        from dzack_research.preamble.categories.modules.pure.modules import Modules

        if self.base_ring() is self or self._preamble_is_number_field_order():
            return True
        presentation = Modules.ParentMethods._native_module_presentation(self)
        basis = None if presentation is None else presentation.module_basis()
        if basis is not None and basis.source() in FramedFreeModules(self.base_ring()):
            return True
        raise AssertionError(
            f"cannot decide whether {self} is projective as a module over {self.base_ring()}"
        )

    def _preamble_is_number_field(self):
        return self._engine in SageNumberFields()

    def _preamble_has_chosen_primitive_element(self):
        return self._engine in SageNumberFields() and self._engine is not SageQQ

    def base_ring(self):
        r"""Return the scalar ring this ring's construction declared."""
        return self.base()

    def variable_names(self):
        return self._engine.variable_names()

    def _first_ngens(self, n):
        return tuple(self._from_engine_element(value) for value in self._engine.gens()[:n])

    def elements(self):
        r"""Return all elements when this ring is finite, as an owned ordered set."""
        if self not in owned_sets.FiniteSets():
            raise ValueError(
                f"elements() lists the elements of a finite ring, but {self} is not known to be finite"
            )
        return owned_sets.finite_ordered_set(
            tuple(self._from_engine_element(element) for element in self._engine.list())
        )

    def _repr_(self):
        display = self._preamble_ring_display
        if display is not None:
            return display
        if self._engine is SageZZ:
            return "Integer Ring"
        if self._engine is SageQQ:
            return "Rational Field"
        if isinstance(self._engine, (PolynomialRing_generic, MPolynomialRing_base)):
            variables = ", ".join(self.variable_names())
            return f"Polynomial ring {self.base_ring()}[{variables}]"
        if self._preamble_is_number_field():
            return (
                f"Number field over {self.base_ring()} with defining polynomial "
                f"{self.defining_polynomial()}"
            )
        if self._preamble_is_number_field_order():
            rank = self.module_rank()
            names = tuple(self.variable_names())
            generator_text = f" generated by {', '.join(names)}" if names else ""
            return f"Order of rank {rank} over Integer Ring{generator_text}"
        if self in owned_sets.FiniteSets():
            size = self.cardinality()
            kind = "Field" if self in OwnedRings().Division().Commutative() else "Ring"
            return f"Finite {kind.lower()} with {size} elements"
        base = self.base_ring()
        return f"Ring over {base}" if base is not self else f"Ring in {self.category()}"

    def _latex_(self):
        text = self._repr_().replace("_", r"\_")
        return rf"\text{{{text}}}"


_OwnedRingBootstrapParent.register(_OwnedRingParent)


def _engine_scalar_ring(engine: Ring):
    r"""Return the owned ring over which ``engine`` presents this ring.

    The answer is ``None`` for a ring the engine presents over itself, which is
    every ring free of rank one over its own scalars -- ``ZZ``, ``QQ``, a
    finite field.  A number field over the rationals or a p-adic ring over the
    integers presents over a smaller ring, and that ring is the scalars its
    module structure is over.  The placement below and the construction that
    threads the scalars to the host both ask this one question.
    """
    base = engine.base_ring()
    if base is engine or base not in SageRings():
        return None
    return _own_ring(base)


def _integer_mod_local_prime(engine):
    r"""Return the unique residue characteristic of ``ZZ/nZZ`` when it is local."""
    match engine:
        case IntegerModRing_generic():
            modulus = SageZZ(engine.characteristic())
            factors = tuple(modulus.factor())
            match factors:
                case ((prime, _exponent),):
                    return SageZZ(prime)
                case _:
                    return None
        case _:
            return None


def _is_integral_multivariate_ideal(engine_ideal) -> bool:
    r"""Whether ``engine_ideal`` lives in ``ZZ[x_1, ..., x_n]``, where Sage's own ``is_prime`` and ``is_maximal`` raise."""
    ring = engine_ideal.ring()
    return isinstance(ring, MPolynomialRing_base) and ring.base_ring() is SageZZ


def _integral_polynomial_ideal_is_prime(engine_ideal) -> bool:
    r"""Primality of ``I`` in ``ZZ[x_1, ..., x_n]``.

    ``OWN-06`` adapter.  Sage's ``is_prime`` raises over ``ZZ`` (TRAPS.md);
    Singular's ``minAssZ`` (``primdecint.lib``) gives the minimal primes of
    ``I``, and a proper ``I`` is prime exactly when it is its only minimal
    prime.
    """
    from sage.libs.singular.function import lib as singular_lib, singular_function

    ring = engine_ideal.ring()
    if engine_ideal.is_one():
        return False
    singular_lib("primdecint.lib")
    minimal_primes = singular_function("minAssZ")(engine_ideal)
    return len(minimal_primes) == 1 and ring.ideal(minimal_primes[0]) == engine_ideal


def _integral_polynomial_ideal_is_maximal(engine_ideal) -> bool:
    r"""Maximality of ``I`` in ``ZZ[x_1, ..., x_n]``.

    ``OWN-06`` adapter.  ``ZZ`` is a Jacobson ring, so a field that is a
    finitely generated ``ZZ``-algebra is finite: ``I`` is maximal exactly
    when ``I cap ZZ = (p)`` for a prime ``p`` and the image of ``I`` in
    ``F_p[x_1, ..., x_n]`` is maximal, which Zariski's lemma decides there
    (prime, with quotient of dimension zero).  ``I cap ZZ`` is read off the
    constants of a Groebner basis over ``ZZ``.
    """
    ring = engine_ideal.ring()
    constants = tuple(g for g in engine_ideal.groebner_basis() if g.degree() <= 0)
    match constants:
        case (constant,):
            characteristic = SageZZ(constant).abs()
        case _:
            return False
    if not characteristic.is_prime():
        return False
    reduction = engine_ideal.change_ring(ring.change_ring(SageGF(characteristic)))
    return bool(reduction.is_prime() and reduction.dimension() == 0)


def _engine_field_decision(engine):
    r"""Return the engine's exact field decision when represented.

    ``OWN-06`` adapter.  ``S/I`` is a field exactly when ``I`` is maximal.
    For a multivariate polynomial ring ``S`` over a field Sage's
    ``is_maximal`` raises (TRAPS.md), so Zariski's lemma decides it: ``I`` is
    maximal exactly when it is prime and ``S/I`` has Krull dimension zero.
    """
    match engine:
        case _ if engine in SageFields():
            return True
        case QuotientRing_generic() if isinstance(engine.cover_ring(), MPolynomialRing_base) and (
            engine.cover_ring().base_ring() is SageAA
        ):
            # Singular has no algebraic-real coefficients and Sage has no
            # other primality route over AA (TRAPS.md): undecided.
            return Unknown
        case QuotientRing_generic() if isinstance(engine.cover_ring(), MPolynomialRing_base) and bool(
            engine.cover_ring().base_ring().is_field()
        ):
            defining = engine.defining_ideal()
            return bool(defining.is_prime() and defining.dimension() == 0)
        case QuotientRing_generic() if _is_integral_multivariate_ideal(engine.defining_ideal()):
            return _integral_polynomial_ideal_is_maximal(engine.defining_ideal())
        case QuotientRing_generic() if isinstance(engine.cover_ring(), MPolynomialRing_base) and isinstance(
            engine.cover_ring().base_ring(), IntegerModRing_generic
        ):
            # (Z/n)[x]/I = Z[x]/(n, I), so the integral test decides it.
            cover = engine.cover_ring()
            modulus = SageZZ(cover.base_ring().characteristic())
            integral = cover.change_ring(SageZZ)
            lifted = integral.ideal(
                (integral(modulus), *(integral(generator.change_ring(SageZZ)) for generator in engine.defining_ideal().gens()))
            )
            return _integral_polynomial_ideal_is_maximal(lifted)
        case _:
            return engine.is_field()


def _owned_ring_category(engine: Ring, *, scalar_base=None, owned_ring=None) -> Category:
    from dzack_research.preamble.owned_category import owned_category_join

    r"""Return the strongest owned ring category witnessed by ``engine``.

    ``scalar_base`` is the owned base already selected by the constructor.
    Re-reading an engine scalar parent here can create a second owned view of
    the same mathematical base and hence two distinct parameterized algebra
    categories.
    """
    category = engine.category()
    extra = []
    commutative = engine.is_commutative() is True
    match owned_ring:
        case None:
            algebra_base = scalar_base
        case _:
            match scalar_base:
                case None:
                    algebra_base = owned_ring
                case _:
                    algebra_base = scalar_base
    match algebra_base:
        case None:
            pass
        case _:
            # The selected scalar object is part of the ring constructor.
            # Record its ordinary algebra/module structure in the initial
            # placement; the native algebra owner below supplies the
            # multiplication and unit data.
            from dzack_research.preamble.categories.algebras.algebras import Algebras

            algebra = Algebras(algebra_base).Associative().Unital()
            match commutative:
                case True:
                    extra.append(algebra.Commutative())
                case False:
                    extra.append(algebra)
    match commutative:
        case True:
            extra.append(OwnedRings().Commutative())
        case False:
            pass
    match (scalar_base is None, owned_ring is not None):
        case (True, True):
            # Every ring is the rank-one free module over itself.  Fix that
            # placement before Parent construction; the native module owner
            # fixes the selected unit framing before this constructor returns.
            from dzack_research.preamble.categories.modules.pure.modules import (
                FinitelyGeneratedFreeModules,
            )

            extra.append(FinitelyGeneratedFreeModules(owned_ring))
        case _:
            pass
    match owned_ring:
        case _ if owned_ring is not None and owned_ring._native_module_basis is not None:
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FramedFreeModules,
            )

            native_source = owned_ring._native_module_basis.source()
            native_free = FramedFreeModules(algebra_base)
            if native_source.module_generating_set().cardinality().is_finite():
                native_free = native_free.FinitelyGenerated()
            extra.append(native_free)
        case _:
            pass
    if engine in SageIntegralDomains():
        extra.append(OwnedRings().Commutative().NoZeroDivisors())
    if engine is SageZZ or engine is SageQQ:
        extra.append(OwnedOrderedRings())
    field_decision = _engine_field_decision(engine)
    match field_decision:
        case True:
            # A prime field is QQ or F_p.  A field realized as Zmod(n) is F_p
            # (GF(p) is an IntegerModRing_generic, GF(p^k) for k > 1 is not);
            # Sage's generic quotients have no is_finite to ask instead.
            match engine is SageQQ or isinstance(engine, IntegerModRing_generic):
                case True:
                    extra.append(PrimeFields())
                case False:
                    pass
        case _:
            pass
    if category.is_subcategory(SagePrincipalIdealDomains()):
        extra.append(OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals())
    elif (
        isinstance(engine, SageNumberFieldOrder)
        and engine.is_maximal()
        and engine.class_number() == 1
    ):
        # A maximal order is Dedekind, hence is a PID exactly when its
        # ideal class group is trivial.  Sage does not place number-field
        # orders in its PrincipalIdealDomains category, so retain this
        # theorem at the owned boundary where the class number is exact.
        extra.append(OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals())
    noetherian = engine.is_noetherian()
    if noetherian is True:
        extra.append(OwnedRings().Noetherian())
    match field_decision:
        case True:
            placement = OwnedRings().Division().Commutative()
        case _:
            match category.is_subcategory(SageDivisionRings()):
                case True:
                    placement = OwnedRings().Division()
                case False:
                    placement = OwnedRings()
    size = _owned_ring_size(engine)
    match size.is_subcategory(owned_sets.FiniteSets()):
        case True:
            extra.append(OwnedRings().Artinian())
        case False:
            pass
    local_prime = _integer_mod_local_prime(engine)
    match (local_prime is not None, field_decision is not True):
        case (True, True):
            extra.append(OwnedRings().Commutative().Local())
        case _:
            pass
    match engine in SageNumberFields():
        case True:
            from dzack_research.preamble.categories.rings.number_fields import (
                NumberFieldsWithChosenPrimitiveElement,
                OwnedNumberFields,
            )

            extra.append(OwnedNumberFields())
            match engine is SageQQ:
                case True:
                    pass
                case False:
                    extra.append(NumberFieldsWithChosenPrimitiveElement())
        case False:
            pass
    match engine is SageZZ or isinstance(engine, SageNumberFieldOrder):
        case True:
            from dzack_research.preamble.categories.rings.number_fields import (
                OrdersWithChosenIntegralBasis,
            )

            extra.append(OrdersWithChosenIntegralBasis())
        case False:
            pass
    joined = owned_category_join((placement, size, *extra))
    if engine is SageZZ or (
        isinstance(engine, SageNumberFieldOrder)
        and (scalar_base is None or _engine_ring(scalar_base) is SageZZ)
    ):
        return owned_category_join((joined, OwnedOrders()))
    return joined


def _install_engine_selected_ring_data(ring, engine) -> None:
    r"""Fix constructor data required by exact initial ring placement."""
    match engine:
        case IntegerModRing_generic() if _engine_field_decision(engine) is not True:
            prime = _integer_mod_local_prime(engine)
            match prime:
                case None:
                    pass
                case _:
                    from dzack_research.preamble.categories.rings.commutative_algebra import (
                        GeneratedIdealView,
                    )

                    residue = GF(prime)
                    maximal_ideal = GeneratedIdealView(ring, (ring(int(prime)),))
                    residue_map = ring.Mor(residue)(
                        lambda element: residue(
                            SageZZ(_engine_element(ring, element).lift())
                        )
                    )
                    _install_local_ring_construction(
                        ring,
                        maximal_ideal,
                        residue,
                        residue_map,
                    )
        case SageNumberFieldOrder() if engine is not SageZZ:
            from dzack_research.preamble.categories.modules.pure.modules import (
                _fix_selected_module_framing,
            )

            integers = _own_ring(SageZZ)
            labels = owned_sets.finite_ordered_set(range(int(engine.rank())))
            source = integers.free_module(labels)
            _fix_selected_module_framing(
                ring,
                integers,
                labels,
                lambda label: _owned_engine_element(ring,
                    engine.basis()[labels.ranking_map()(label)]
                ),
                source,
            )
        case _:
            pass


def _owned_ring_size(engine):
    r"""Return the exact Set-cardinality placement known from the engine kind."""
    from sage.categories.number_fields import NumberFields
    from sage.categories.sets_cat import Sets as SageSets
    from sage.rings.qqbar import AA as SageAA
    from sage.rings.qqbar import QQbar as SageQQbar

    if engine.category().is_subcategory(SageSets().Finite()):
        return owned_sets.FiniteSets()
    if not engine.is_exact():
        return owned_sets.UncountableSets()
    if (
        engine is SageZZ
        or engine is SageQQ
        or engine in NumberFields()
        or isinstance(engine, SageNumberFieldOrder)
        or engine is SageAA
        or engine is SageQQbar
    ):
        return owned_sets.CountablyInfiniteSets()
    if isinstance(engine, (PolynomialRing_generic, MPolynomialRing_base)):
        coefficient_size = _owned_ring_size(engine.base_ring())
        if engine.ngens() == 0:
            return coefficient_size
        if coefficient_size.is_subcategory(owned_sets.FiniteSets()) or coefficient_size.is_subcategory(owned_sets.CountablyInfiniteSets()):
            return owned_sets.CountablyInfiniteSets()
    if engine.category().is_subcategory(SageQuotientFields()):
        source_size = _owned_ring_size(engine.ring())
        if source_size.is_subcategory(owned_sets.FiniteSets()) or source_size.is_subcategory(owned_sets.CountablyInfiniteSets()):
            return owned_sets.CountablyInfiniteSets()
    return owned_sets.Sets()


def _own_if_ring(result):
    return _own_ring(result) if result in SageRings() else result


@cached_function
def _owned_engine_ring(engine: Ring) -> _OwnedRingParent:
    r"""Adopt the engine through the construction that supplies its module.

    Polynomial and free associative engines present the free algebra on
    their native variables over their coefficient ring.  They therefore
    take the same monomial-module construction as the public free functor,
    rather than a bare native ring later labelled as a free algebra.
    """
    from sage.algebras.free_algebra import FreeAlgebra_generic

    match engine:
        case PolynomialRing_generic() | MPolynomialRing_base():
            flavor = "symmetric"
        case FreeAlgebra_generic():
            flavor = "tensor"
        case _:
            return _OwnedRingParent(engine)
    from dzack_research.preamble.categories.algebras.free_algebras import (
        _native_free_algebra,
    )

    base = _own_ring(engine.base_ring())
    return _native_free_algebra(
        engine, base.free_module(tuple(engine.variable_names())), flavor,
    )


def _own_ring(ring):
    r"""Private backend adapter: build the preamble ring represented by ``ring``.

    One engine has one owned view.  Number-field, order and ordinary algebra
    placement are fixed by that constructor before the parent is exposed;
    selected residue and integral-basis data are installed in the same
    construction.  Thus ``ZZ.base_ring() is ZZ`` and every morphism
    ``R[G] -> R`` finds one common base ring.
    """
    if ring in OwnedRings():
        return ring
    if ring not in SageRings():
        raise TypeError(f"{ring} is not a ring")
    if ring is SageZZ:
        return _owned_integers()
    return _owned_engine_ring(ring)


def _set_owned_ring_display(ring, display, *, kind=None):
    r"""Install presentation metadata at the owned ring boundary.

    Protected ring-storage contract under OWN-05. Ring and algebra
    constructors may select human-readable display metadata, but they do not
    write the ring parent's private storage directly. This owner dispatcher
    returns the same owned ring after installing only presentation metadata;
    it changes no mathematical category or realization.
    """
    owned = _own_ring(ring)
    owned._preamble_ring_display = str(display)
    if kind is not None:
        owned._preamble_ring_display_kind = str(kind)
    return owned


@cached_function
def _owned_integers() -> _OwnedRingParent:
    r"""The canonical owned integers, including their initial order placement."""
    return _owned_engine_ring(SageZZ)


def _owned_ring(ring):
    r"""Return ``ring`` after asserting it already belongs to the preamble universe."""
    if ring not in OwnedRings():
        raise TypeError(f"expected a ring of this session, but {ring!r} is not one")
    return ring


def _engine_ring(ring):
    r"""Return the selected private computation parent behind an owned ring.

    This is the designated dispatcher for the protected ring-realization
    contract declared on :class:`OwnedRings.ParentMethods`.  It performs no
    representation probing: each construction owner states its realization.
    """
    return _own_ring(ring)._selected_engine_ring()


def _engine_quotient_cover_ideal(ring, engine_ideal):
    r"""Lift an ideal of a selected quotient engine to its cover ring.

    If the computation parent of ``ring`` is ``S/J``, then an ideal generated
    by classes ``f_i`` is represented upstairs by ``J + (\tilde f_i)``.  This
    private crossing is the exact backend datum needed by Singular operations
    that work over ``S`` but not over Sage's generic quotient-ring parent.
    """
    engine = _engine_ring(ring)
    cover = engine.cover_ring()
    defining = engine.defining_ideal()
    lifted = tuple(engine(generator).lift() for generator in engine_ideal.gens())
    return cover.ideal(tuple(defining.gens()) + lifted)


def _engine_element(ring, element):
    r"""Return the private computation-engine realization of ``element``.

    ``_engine_ring(R)`` identifies a currently selected CAS realization of the
    owned ring ``R``.  This companion crossing converts an element of the
    *owned* ring into that engine without asking the engine's coercion graph to
    know about the owned parent.  Quotients, localizations, completions, and
    future Julia/OSCAR-backed rings can therefore keep one public mathematical
    parent while changing computational realizations independently.
    """
    return _own_ring(ring)._engine_element(element)


def _owned_engine_element(ring, engine_element):
    r"""Raise one private computation result into the owned ring.

    Protected ring-realization contract (OWN-05--07).  Implementers are the
    ring parents' private ``_from_engine_element`` methods; callers are only
    computation adapters that have already selected this ring's realization
    and must immediately return to the owned mathematical parent.  Raw engine
    elements do not leave that adapter.  This is the raising companion to
    :func:`_engine_element`, so every ring realization has one lowering and
    one raising dispatcher.
    """
    return _own_ring(ring)._from_engine_element(engine_element)


def _engine_numeral(ring, value):
    r"""Cross an ingress numeral to the selected private Sage ring.

    Constructor arguments can arrive as Python numerals, owned ring elements,
    or raw Sage ring elements from backend code.  Public owned-ring coercion
    deliberately rejects the last case; this private constructor boundary is
    precisely where all three spellings are normalized before entering Sage.
    """

    owned = _own_ring(ring)
    engine = _engine_ring(owned)
    parent = element_parent(value)
    if parent in OwnedRings():
        value = _engine_element(parent, value)
    elif parent not in SageRings() and isinstance(value, SageObject):
        raise TypeError(
            f"cannot read {value!r} as an element of {ring}: its parent {parent!r} is not a ring"
        )
    return engine(value)


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


def _lowered_integer_arguments(args):
    r"""The arguments of an engine ring constructor, with the session's integers lowered to Python ``int``.

    Sage's constructors neither contain nor convert the owned integers
    (TRAPS.md); every other argument, such as a generator name, passes as given.
    """
    integers = _owned_integers()
    return tuple(int(argument) if argument in integers else argument for argument in args)


def GF(*args, **kwargs):
    engine = _SageGF(*_lowered_integer_arguments(args), **kwargs)
    field = _own_ring(engine)
    _set_owned_ring_display(field, f"GF({engine.order()})", kind="finite_field")
    return field


FiniteField = GF


def PrimeField(characteristic):
    return GF(characteristic)


def Zmod(*args, **kwargs):
    r"""Return ``ZZ/nZZ`` with its exact finite-ring refinements."""
    engine = _SageZmod(*_lowered_integer_arguments(args), **kwargs)
    ring = _own_ring(engine)
    if engine is SageZZ:
        return ring
    modulus = SageZZ(engine.characteristic())
    _set_owned_ring_display(ring, f"ZZ/{modulus}ZZ", kind="modular")

    return ring


IntegerModRing = Zmod
Integers = Zmod


def Qp(*args, **kwargs):
    engine = _SageQp(*args, **kwargs)
    ring = _own_ring(engine)
    _set_owned_ring_display(
        ring,
        f"Q_{engine.prime()} with precision {engine.precision_cap()}",
        kind="padic",
    )
    return ring


def RealField(*args, **kwargs):
    engine = _SageRealField(*args, **kwargs)
    ring = _own_ring(engine)
    _set_owned_ring_display(
        ring,
        f"Real field with {engine.precision()} bits precision",
        kind="real",
    )
    return ring


def ComplexField(*args, **kwargs):
    engine = _SageComplexField(*args, **kwargs)
    ring = _own_ring(engine)
    _set_owned_ring_display(
        ring,
        f"Complex field with {engine.precision()} bits precision",
        kind="complex",
    )
    return ring


Rings = OwnedRings
OrderedRings = OwnedOrderedRings
DivisionRings = OwnedDivisionRings
Fields = OwnedFields
IntegralDomains = OwnedIntegralDomains
PrincipalIdealDomains = OwnedPrincipalIdealDomains
NoetherianRings = OwnedNoetherianRings
ArtinianRings = OwnedArtinianRings
LocalRings = OwnedLocalRings
AdicallyCompleteRings = OwnedAdicallyCompleteRings
CompleteLocalRings = OwnedCompleteLocalRings
Orders = OwnedOrders


def binomial(x, m):
    r"""The binomial coefficient \(\binom{x}{m}\), for a natural number \(m\)."""
    return x.binomial(m)


def CommutativeRings():
    r"""The category of commutative unital rings.

    The session name for ``OwnedRings().Commutative()``: commutativity is an
    axiom on the operation, and this is the category it cuts out.
    """
    return OwnedRings().Commutative()


OwnedCommutativeRings = CommutativeRings


def _enumerated_ring_elements(ring):
    r"""Finite scalar enumeration at the native ring boundary, or ``None``.

    The finite-linearity callers use owned values.  Only this ring adapter
    accesses the computation ring's iterator and converts its outputs.
    """
    match ring:
        case _ if ring in owned_sets.FiniteSets():
            engine = _engine_ring(ring)
            return tuple(_owned_engine_element(ring, engine(value)) for value in engine)
        case _:
            return None
