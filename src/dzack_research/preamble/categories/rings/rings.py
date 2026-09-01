"""Owned scalar hierarchy and the boundary to Sage computation rings."""

from functools import wraps

from sage.all import (
    ComplexField as _SageComplexField,
    CyclotomicField as _SageCyclotomicField,
    FractionField as _SageFractionField,
    GF as _SageGF,
    MatrixSpace as _SageMatrixSpace,
    NumberField as _SageNumberField,
    PolynomialRing as _SagePolynomialRing,
    PowerSeriesRing as _SagePowerSeriesRing,
    Qp as _SageQp,
    QuadraticField as _SageQuadraticField,
    RealField as _SageRealField,
    Zmod as _SageZmod,
    Zp as _SageZp,
    LaurentPolynomialRing as _SageLaurentPolynomialRing,
)
from sage.categories.category import Category
from sage.categories.category_types import Category_over_base_ring
from sage.categories.commutative_rings import CommutativeRings as SageCommutativeRings
from sage.categories.division_rings import DivisionRings as SageDivisionRings
from sage.categories.fields import Fields as SageFields
from sage.categories.finite_fields import FiniteFields as SageFiniteFields
from sage.categories.integral_domains import IntegralDomains as SageIntegralDomains
from sage.categories.number_fields import NumberFields as SageNumberFields
from sage.categories.rings import Rings as SageRings
from sage.categories.rngs import Rngs as SageRngs
from sage.categories.semirings import Semirings as SageSemirings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.latex import latex
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ
from sage.rings.ring import Ring
from sage.structure.parent import Parent
from sage.structure.unique_representation import UniqueRepresentation

from dzack_research.preamble.categories.group.magmas import (
    AdditiveGroups,
    AdditiveMonoids,
    Monoids,
    Semigroups,
)
from dzack_research.preamble.refine import refine


class OwnedSemirings(Category):
    """Semirings on the owned operation spine."""

    def super_categories(self):
        return [SageSemirings(), Monoids(), AdditiveMonoids()]


class OwnedRngs(Category):
    """Rngs on the owned operation spine."""

    def super_categories(self):
        return [SageRngs(), Semigroups(), AdditiveGroups()]


class OwnedRings(Category):
    """Unital rings whose notebook-facing ring interface is owned here."""

    def super_categories(self):
        return [SageRings(), OwnedSemirings(), OwnedRngs()]

    class ParentMethods:
        def __getitem__(self, names):
            r"""Adjoin names as a polynomial ring, or algebraic integers as an extension.

            Variable names produce a polynomial ring: ``ZZ["x"]`` is
            \(\mathbb{Z}[x]\).  An algebraic integer produces the
            extension Sage would: ``ZZ[I]`` is the Gaussian integers,
            ``QQ[I]`` is \(\mathbb{Q}(i)\), and ``ZZ[sqrt(2)]`` is the
            order \(\mathbb{Z}[\sqrt{2}]\).
            """
            match names:
                case str():
                    return PolynomialRing(self, names)
                case list():
                    return _own_if_ring(engine_ring(self)[names])
                case tuple() if all(isinstance(part, str) for part in names):
                    return PolynomialRing(self, names)
                case _ if names in self:
                    return self
                case _:
                    return _own_if_ring(engine_ring(self)[names])

        def cardinality(self):
            r"""Return the exact represented cardinal of the underlying set."""
            from dzack_research.preamble.categories.sets import (
                CountablyInfiniteSets,
                FiniteSets,
                UncountableSets,
                aleph0,
                cardinal,
                continuum,
            )

            category = self.category()
            if category.is_subcategory(FiniteSets()):
                return cardinal(engine_ring(self).cardinality())
            if category.is_subcategory(CountablyInfiniteSets()):
                return aleph0
            if category.is_subcategory(UncountableSets()):
                return continuum
            raise NotImplementedError(
                f"the exact cardinality of the underlying set of {self} is not represented"
            )

        def __pow__(self, exponent):
            r"""Return the free module on the specified basis/index set."""
            from dzack_research.preamble.categories.modules import FreeModule

            return FreeModule(self, exponent)

        def __truediv__(self, divisor):
            r"""Delegate parent quotients to the computation ring and re-own the result."""
            result = engine_ring(self) / engine_ring(divisor)
            from sage.groups.additive_abelian.qmodnz import QmodnZ

            if isinstance(result, QmodnZ):
                from dzack_research.preamble.categories.modules.framed.fraction_field_quotients import (
                    refine_fraction_field_quotient,
                )

                return refine_fraction_field_quotient(result)
            return own_ring(result) if result in SageRings() else result

        def is_central(self, element):
            r"""Return whether ``element`` is central when this is decidable here."""
            if element not in self:
                return False
            if self in SageCommutativeRings():
                return True
            from dzack_research.preamble.categories.algebras.algebras import (
                finite_algebra_generators,
            )

            try:
                generators = finite_algebra_generators(self)
            except NotImplementedError as error:
                raise NotImplementedError(
                    f"{self} supplies no finite algebra generating set from which "
                    "centrality can be decided"
                ) from error
            return all(
                element * generator == generator * element
                for generator in generators
            )

        @cached_method
        def _ring_morphism_defining_algebra_structure(self):
            r"""Return the canonical ring map \(R\to Z(R)\) when it is the identity."""
            from sage.categories.homset import Hom
            from sage.categories.morphism import SetMorphism

            if self not in SageCommutativeRings():
                raise TypeError(
                    f"{self} is noncommutative, so the identity does not land "
                    "in its center"
                )
            center = self.ring_center()
            return SetMorphism(Hom(self, center, SageRings()), lambda scalar: scalar)

        def algebra_structure_morphism(self):
            r"""The structure morphism of this ring as an algebra over itself.

            For a commutative ring this is the identity \(R\to R\).
            """
            return self._ring_morphism_defining_algebra_structure()

        @cached_method
        def ring_center(self):
            r"""Return the centre ``Z(R)`` as a predicate-defined subring."""
            if self in SageCommutativeRings():
                return self
            from dzack_research.preamble.categories.rings.predicate_subrings import (
                predicate_subring,
            )

            return predicate_subring(
                self,
                self.is_central,
                "z commutes with every element",
                SageCommutativeRings(),
            )

        def fraction_field(self):
            r"""Return the fraction field through the computation ring."""
            if self in SageFields():
                return self
            return own_ring(engine_ring(self).fraction_field())

        def ideal(self, *module_generators):
            r"""Return an owned ideal where the active module adapter applies.

            Other rings retain their native Sage ideal construction rather
            than being forced through the current ``ZZ``/number-order module
            adapter.
            """
            if engine_ring(self) is SageZZ:
                from dzack_research.preamble.categories.modules.fractional_ideals import (
                    Ideal,
                )

                return Ideal(self, module_generators)
            return engine_ring(self).ideal(*module_generators)

        def fractional_ideal(self, *module_generators):
            r"""Return the owned ``ZZ`` fractional ideal, otherwise delegate."""
            engine = engine_ring(self)
            if engine is SageZZ:
                from dzack_research.preamble.categories.modules.fractional_ideals import (
                    FractionalIdeal,
                )

                return FractionalIdeal(self, module_generators)
            try:
                method = engine.fractional_ideal
            except AttributeError as error:
                raise AttributeError(
                    f"{self} has no fractional-ideal constructor"
                ) from error
            return method(*module_generators)


class OwnedCommutativeRings(Category):
    r"""Commutative unital rings in the owned mathematical graph."""

    def super_categories(self):
        return [OwnedRings(), SageCommutativeRings()]

    class ParentMethods:
        def is_commutative(self):
            return True

        def as_algebra_over(self, base_ring):
            r"""Return this ring with its canonical algebra structure over ``base_ring``."""
            base = own_ring(base_ring)
            engine = engine_ring(self)
            if not engine.has_coerce_map_from(engine_ring(base)):
                raise ValueError(f"{self} has no represented canonical algebra structure over {base}")
            from dzack_research.preamble.categories.algebras.algebras import refine_algebra

            return refine_algebra(self, base)

        def as_ZZ_algebra(self):
            return self.as_algebra_over(own_ring(SageZZ))

        def quotient_ring(self, ideal):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                QuotientRing,
            )

            return QuotientRing(self, ideal)

        def localization(self, *elements):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                Localization,
            )

            return Localization(self, *elements)

        def localize_at_prime(self, prime):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                PrimeLocalization,
            )

            return PrimeLocalization(self, prime)

        def adic_completion(self, ideal, precision=20):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                AdicCompletion,
            )

            return AdicCompletion(self, ideal, precision=precision)

        @cached_method
        def spectrum(self):
            from dzack_research.preamble.categories.rings.prime_spectrum import (
                PrimeSpectrum,
            )

            return PrimeSpectrum(self)


class OwnedIntegralDomains(Category):
    r"""Commutative rings without zero divisors."""

    def super_categories(self):
        return [OwnedCommutativeRings(), SageIntegralDomains()]

    class ParentMethods:
        def is_integral_domain(self, *args, **kwargs):
            return True


class OwnedNoetherianRings(Category):
    r"""Noetherian commutative rings."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_noetherian(self):
            return True

        def krull_dimension(self):
            engine = engine_ring(self)
            method = getattr(engine, "krull_dimension", None)
            if method is None:
                raise NotImplementedError(f"Krull dimension of {self} has no active backend")
            return method()


class OwnedArtinianRings(Category):
    r"""Artinian commutative rings."""

    def super_categories(self):
        return [OwnedNoetherianRings()]

    class ParentMethods:
        def is_artinian(self):
            return True


class OwnedLocalRings(Category):
    r"""Commutative rings equipped with their unique maximal ideal."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_local(self):
            return True

        def maximal_ideal(self):
            ideal = getattr(self, "_preamble_maximal_ideal", None)
            if ideal is None:
                raise NotImplementedError(f"the maximal ideal of {self} is not represented")
            return ideal

        def residue_field(self):
            residue = getattr(self, "_preamble_residue_field", None)
            if residue is None:
                raise NotImplementedError(f"the residue field of {self} is not represented")
            return residue

        def fraction_field(self):
            represented = getattr(self, "_preamble_fraction_field", None)
            if represented is not None:
                return represented
            return super().fraction_field()


class OwnedAdicallyCompleteRings(Category):
    r"""Commutative rings represented as complete for a chosen adic topology."""

    def super_categories(self):
        return [OwnedCommutativeRings()]

    class ParentMethods:
        def is_adically_complete(self):
            return True

        def ideal_of_definition(self):
            ideal = getattr(self, "_preamble_ideal_of_definition", None)
            if ideal is None:
                raise NotImplementedError(f"the ideal of definition of {self} is not represented")
            return ideal

        def completion_source(self):
            source = getattr(self, "_preamble_completion_source", None)
            if source is None:
                raise NotImplementedError(f"{self} is not represented as a completion of a source ring")
            return source


class OwnedCompleteLocalRings(Category):
    r"""Local rings complete for the represented maximal-ideal/adic topology."""

    def super_categories(self):
        return [OwnedLocalRings(), OwnedAdicallyCompleteRings()]

class OwnedDivisionRings(Category):
    def super_categories(self):
        return [SageDivisionRings(), OwnedRings()]


class OwnedFields(Category):
    def super_categories(self):
        return [
            SageFields(),
            OwnedDivisionRings(),
            OwnedIntegralDomains(),
            OwnedNoetherianRings(),
            OwnedArtinianRings(),
            OwnedLocalRings(),
        ]

    class ParentMethods:
        def maximal_ideal(self):
            return engine_ring(self).ideal(0)

        def residue_field(self):
            return self


class OwnedOrders(Category):
    r"""Orders in number fields.

    An order is a finite-rank \(\mathbb{Z}\)-subalgebra of a number
    field, hence infinite as a set.
    """

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.framed.finitely_generated.finitely_generated_free_modules import (
            FinitelyGeneratedFreeModules,
        )

        return [
            OwnedRings(),
            OwnedIntegralDomains(),
            OwnedNoetherianRings(),
            Algebras(own_ring(SageZZ)),
            FinitelyGeneratedFreeModules(own_ring(SageZZ)),
        ]

    class ParentMethods:
        def base_ring(self):
            return own_ring(SageZZ)

        def _Hom_(self, codomain, category=None):
            if codomain not in OwnedOrders():
                raise TypeError("an order embedding must land in an order")
            if category is not None and not category.is_subcategory(OwnedOrders()):
                raise TypeError("this is not an order-embedding category")
            from dzack_research.preamble.categories.rings.embeddings import order_homset

            return order_homset(self, codomain)

        def ideal(self, *module_generators):
            r"""Return the integral ideal generated by the stated order elements."""
            from dzack_research.preamble.categories.modules.fractional_ideals import (
                Ideal,
            )

            return Ideal(self, module_generators)

        def fractional_ideal(self, *module_generators):
            r"""Return the fractional ideal generated in the fraction field."""
            from dzack_research.preamble.categories.modules.fractional_ideals import (
                FractionalIdeal,
            )

            return FractionalIdeal(self, module_generators)

        def base_change(self, ring_map):
            r"""Return the algebra scalar extension of this order.

            In particular, ``QQ tensor_ZZ O`` is the number field containing
            ``O``.  The order is also a finite free ``ZZ``-module, but scalar
            extension here retains its algebra structure rather than selecting
            the weaker module-only construction inherited from free modules.
            """
            if engine_ring(ring_map.domain()) is not SageZZ:
                raise ValueError("an order is a ZZ-algebra, so scalar extension starts at ZZ")
            target = engine_ring(ring_map.codomain())
            if target is SageZZ:
                return self
            if target is SageQQ:
                field = own_ring(engine_ring(self).fraction_field())
                return field.as_algebra()
            raise NotImplementedError(
                "the active order algebra-base-change adapter currently constructs ZZ -> ZZ and ZZ -> QQ"
            )

        def cardinality(self):
            from dzack_research.preamble.categories.sets import aleph0

            return aleph0

        def integral_basis(self):
            r"""Return the selected ``ZZ``-basis of this order."""
            return self.module_generators()

        @cached_method
        def module_generating_set(self):
            from dzack_research.preamble.categories.sets import finite_ordered_set

            engine = engine_ring(self)
            if engine is SageZZ:
                return finite_ordered_set((0,))
            return finite_ordered_set(range(int(engine.rank())))

        def module_generator(self, label):
            labels = self.module_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a module-generator label")
            engine = engine_ring(self)
            if engine is SageZZ:
                return self(SageZZ.one())
            return self(engine.basis()[labels.position(label)])

        @cached_method
        def module_generators(self):
            from dzack_research.preamble.categories.sets import finite_ordered_set

            return finite_ordered_set(
                self.module_generator(label) for label in self.module_generating_set()
            )

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
                FreeModuleOn,
            )
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
                framing_morphism,
            )

            source = FreeModuleOn(self.base_ring(), self.module_generating_set())
            return framing_morphism(source, self, self.module_generator)

        def rank(self):
            engine = engine_ring(self)
            return SageZZ.one() if engine is SageZZ else SageZZ(engine.rank())


class PrimeFields(Category):
    r"""Prime fields \(\mathbf F_p\)."""

    def super_categories(self):
        return [SageFiniteFields(), OwnedFields()]


from dzack_research.preamble.categories.abstract_categories.hom_categories import (  # noqa: E402
    CategoryPacketMethods,
)


class OwnedCategoryOverBaseRing(CategoryPacketMethods, Category_over_base_ring):
    r"""A category over a ring, normalized to the session's owned ring."""

    @staticmethod
    def __classcall__(cls, base_ring, *args, **kwargs):
        return Category_over_base_ring.__classcall__(
            cls,
            owned_ring_view(base_ring),
            *args,
            **kwargs,
        )


class OwnedRingView(UniqueRepresentation, Parent):
    r"""The session-facing ring whose Sage parent is its computation engine.

    Elements remain the engine's elements.  The owned object is the ring
    parent: it supplies the uniform category surface while algorithms can
    explicitly cross to :func:`engine_ring` when they require Sage's concrete
    implementation class.
    """

    def __init__(self, engine: Ring) -> None:
        self._engine = engine
        Parent.__init__(
            self,
            facade=engine,
            category=_owned_ring_category(engine),
        )
        refine(self, self.category())

    def engine(self) -> Ring:
        return self._engine

    def _element_constructor_(self, value):
        return self._engine(value)

    def __contains__(self, value) -> bool:
        try:
            self._engine(value)
        except (TypeError, ValueError):
            return False
        return True

    def zero(self):
        return self._engine.zero()

    def one(self):
        return self._engine.one()

    def characteristic(self):
        return self._engine.characteristic()

    def is_exact(self):
        return self._engine.is_exact()

    def is_field(self, *args, **kwargs):
        return self._engine.is_field(*args, **kwargs)

    def is_commutative(self):
        return self._engine.is_commutative()

    def is_integral_domain(self, *args, **kwargs):
        method = self._engine.is_integral_domain
        return method(*args, **kwargs)

    def is_finite(self):
        return self._engine.is_finite()

    def base_ring(self):
        base = self._engine.base_ring()
        if base is self._engine:
            return self
        return own_ring(base) if base in SageRings() else base

    def variable_names(self):
        return self._engine.variable_names()

    def _first_ngens(self, n):
        r"""Return the distinguished variables needed by Sage's naming syntax."""
        return tuple(self._engine.gens()[:n])

    def _coerce_map_from_(self, source):
        computation_source = engine_ring(source)
        if computation_source is self._engine:
            return True
        return True if self._engine.has_coerce_map_from(computation_source) else None

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
    joined = Category.join((category, placement, _owned_ring_size(engine), *extra))
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
    from dzack_research.preamble.categories.sets import (
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
    return own_ring(result) if result in SageRings() else result


@cached_function
def _owned_engine_ring(engine: Ring) -> OwnedRingView:
    return OwnedRingView(engine)


def _refine_canonical_self_module_and_algebra(ring):
    r"""Install the canonical ``R``-module and ``R``-algebra structures on ``R``.

    This applies when the owned ring's currently selected scalar base is the
    ring itself.  The important point is identity of the mathematical object:
    no rank-one module copy and no second algebra parent is constructed.

    The guard is also an import-cycle guard.  ``own_ring`` is used while the
    module/algebra category modules themselves are imported; in that phase the
    refinement is simply deferred until the next lookup of the interned ring.
    """
    if ring.__dict__.get("_preamble_self_structures_done", False):
        return ring
    if ring.__dict__.get("_preamble_self_structures_in_progress", False):
        return ring

    ring._preamble_self_structures_in_progress = True
    try:
        if not ring.is_commutative():
            return ring
        # Before this refinement ``OwnedRingView.base_ring`` delegates to the
        # engine.  Rings such as QQ, ZZ, and prime fields are canonically based
        # on themselves.  A polynomial ring already carries a different chosen
        # algebra/module base and must not have that structure silently changed.
        if ring.base_ring() is not ring:
            return ring

        try:
            from dzack_research.preamble.categories.algebras import (
                CommutativeAlgebras,
                FramedAlgebras,
            )
            from dzack_research.preamble.categories.modules import (
                FinitelyGeneratedFreeModules,
            )
            from dzack_research.preamble.categories.sets import finite_ordered_set
        except ImportError:
            return ring

        module_labels = finite_ordered_set((0,))
        ring._preamble_base_ring = ring
        ring._preamble_module_generating_set = module_labels
        ring._preamble_module_generator_values = {0: ring.one()}
        ring._preamble_module_coordinate_function = lambda element: (ring(element),)

        # As an algebra over itself the scalar image already generates all of
        # R, so the selected algebra generating set is empty.
        ring._preamble_algebra_base_ring = ring
        ring._preamble_algebra_generating_set = finite_ordered_set(())
        ring._preamble_algebra_generator_values = {}

        refine(
            ring,
            [
                FinitelyGeneratedFreeModules(ring),
                FramedAlgebras(ring),
                CommutativeAlgebras(ring),
            ],
        )
        ring._preamble_self_structures_done = True
        return ring
    finally:
        ring._preamble_self_structures_in_progress = False


def own_ring(ring):
    r"""Return the owned form of a ring without changing its elements."""
    if ring in OwnedRings():
        owned = ring
    else:
        if ring not in SageRings():
            raise TypeError(f"{ring} is not a ring")
        owned = _owned_engine_ring(ring)
    if engine_ring(owned) in SageNumberFields():
        from dzack_research.preamble.categories.rings.number_fields import (
            _refine_number_field_view,
        )

        owned = _refine_number_field_view(owned)
    return _refine_canonical_self_module_and_algebra(owned)


def owned_ring_view(ring):
    return own_ring(ring)


def engine_ring(ring):
    r"""Return the Sage computation parent behind an owned ring."""
    match ring:
        case OwnedRingView():
            return ring.engine()
        case _:
            return ring


def _owning_constructor(constructor):
    @wraps(constructor)
    def construct(*args, **kwargs):
        result = constructor(*args, **kwargs)
        return own_ring(result) if result in SageRings() else result

    return construct


def _constructor_over_ring(constructor):
    @wraps(constructor)
    def construct(base_ring, *args, **kwargs):
        result = constructor(engine_ring(base_ring), *args, **kwargs)
        return own_ring(result) if result in SageRings() else result

    return construct


def GF(*args, **kwargs):
    engine = _SageGF(*args, **kwargs)
    field = own_ring(engine)
    if engine.degree() == 1:
        refine(field, PrimeFields())
    return field


FiniteField = GF


def PrimeField(characteristic):
    return GF(characteristic)


def Zmod(*args, **kwargs):
    return own_ring(_SageZmod(*args, **kwargs))


IntegerModRing = Zmod
Integers = Zmod


def Zp(*args, **kwargs):
    result = own_ring(_SageZp(*args, **kwargs))
    prime = SageZZ(args[0] if args else kwargs.get("p"))
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        GeneratedIdealView,
    )

    refine(
        result,
        [
            OwnedNoetherianRings(),
            OwnedCompleteLocalRings(),
        ],
    )
    result._preamble_ideal_of_definition = SageZZ.ideal(prime)
    result._preamble_maximal_ideal = GeneratedIdealView(
        result,
        (result(engine_ring(result).uniformizer()),),
        source_ideal=SageZZ.ideal(prime),
    )
    result._preamble_residue_field = GF(prime)
    result._preamble_completion_source = own_ring(SageZZ)
    return result


def Qp(*args, **kwargs):
    return own_ring(_SageQp(*args, **kwargs))


def RealField(*args, **kwargs):
    return own_ring(_SageRealField(*args, **kwargs))


def ComplexField(*args, **kwargs):
    return own_ring(_SageComplexField(*args, **kwargs))


def CyclotomicField(*args, **kwargs):
    return own_ring(_SageCyclotomicField(*args, **kwargs))


def QuadraticField(*args, **kwargs):
    return own_ring(_SageQuadraticField(*args, **kwargs))


def NumberField(*args, **kwargs):
    return own_ring(_SageNumberField(*args, **kwargs))


def PolynomialRing(base_ring, *args, **kwargs):
    result = own_ring(_SagePolynomialRing(engine_ring(base_ring), *args, **kwargs))
    try:
        from dzack_research.preamble.categories.algebras.algebras import refine_algebra

        labels = tuple(engine_ring(result).variable_names())
        algebra = refine_algebra(result, base_ring, labels)
        if own_ring(base_ring) in OwnedNoetherianRings():
            refine(algebra, OwnedNoetherianRings())
        return algebra
    except ImportError:
        return result


def LaurentPolynomialRing(base_ring, *args, **kwargs):
    result = own_ring(
        _SageLaurentPolynomialRing(engine_ring(base_ring), *args, **kwargs)
    )
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    labels = tuple(engine_ring(result).variable_names())
    algebra = refine_algebra(result, base_ring, labels)
    if own_ring(base_ring) in OwnedNoetherianRings():
        refine(algebra, OwnedNoetherianRings())
    return algebra


def PowerSeriesRing(base_ring, *args, **kwargs):
    result = own_ring(_SagePowerSeriesRing(engine_ring(base_ring), *args, **kwargs))
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    labels = tuple(engine_ring(result).variable_names())
    algebra = refine_algebra(result, base_ring, labels)
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        refine_power_series_ring,
    )

    return refine_power_series_ring(algebra, base_ring)


def FractionField(ring, *args, **kwargs):
    result = own_ring(_SageFractionField(engine_ring(ring), *args, **kwargs))
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    return refine_algebra(result, ring)


def MatrixSpace(base_ring, *args, **kwargs):
    result = _SageMatrixSpace(engine_ring(base_ring), *args, **kwargs)
    if result not in SageRings():
        return result
    result = own_ring(result)
    from dzack_research.preamble.categories.algebras.algebras import refine_algebra

    return refine_algebra(result, base_ring)


def ring_constructor_surface() -> dict[str, object]:
    r"""Return the ring constructors that a preamble session owns."""
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        AdicCompletion,
        DualNumbers,
        Localization,
        PrimeLocalization,
        QuotientRing,
        ResidueField,
    )

    return {
        "AdicCompletion": AdicCompletion,
        "DualNumbers": DualNumbers,
        "GF": GF,
        "FiniteField": FiniteField,
        "PrimeField": PrimeField,
        "Zmod": Zmod,
        "IntegerModRing": IntegerModRing,
        "Integers": Integers,
        "Zp": Zp,
        "Qp": Qp,
        "RealField": RealField,
        "ComplexField": ComplexField,
        "CyclotomicField": CyclotomicField,
        "QuadraticField": QuadraticField,
        "NumberField": NumberField,
        "PolynomialRing": PolynomialRing,
        "LaurentPolynomialRing": LaurentPolynomialRing,
        "PowerSeriesRing": PowerSeriesRing,
        "FractionField": FractionField,
        "Localization": Localization,
        "PrimeLocalization": PrimeLocalization,
        "QuotientRing": QuotientRing,
        "ResidueField": ResidueField,
        "MatrixSpace": MatrixSpace,
    }


@cached_function
def session_ring_objects() -> dict[str, Parent]:
    r"""Return the standard session names under their owned ring parents."""
    from sage.all import AA as SageAA
    from sage.all import CC as SageCC
    from sage.all import CDF as SageCDF
    from sage.all import QQ as SageQQ
    from sage.all import QQbar as SageQQbar
    from sage.all import RDF as SageRDF
    from sage.all import ZZ as SageZZ

    from dzack_research.preamble.rings.real import RR

    # RR is already an owned mathematical field, rather than a view of Sage's
    # MPFR parent.  It joins the same owned category graph in place.
    refine(RR, OwnedFields())
    return {
        "ZZ": own_ring(SageZZ),
        "QQ": own_ring(SageQQ),
        "AA": own_ring(SageAA),
        "QQbar": own_ring(SageQQbar),
        "RR": RR,
        "RDF": own_ring(SageRDF),
        "CDF": own_ring(SageCDF),
        "CC": own_ring(SageCC),
    }


def install_session_rings(scope: dict) -> None:
    r"""Restore the owned scalar names and ring constructors in ``scope``."""
    scope.update(session_ring_objects())
    scope.update(ring_constructor_surface())


Rings = OwnedRings
DivisionRings = OwnedDivisionRings
Fields = OwnedFields
CommutativeRings = OwnedCommutativeRings
IntegralDomains = OwnedIntegralDomains
NoetherianRings = OwnedNoetherianRings
ArtinianRings = OwnedArtinianRings
LocalRings = OwnedLocalRings
AdicallyCompleteRings = OwnedAdicallyCompleteRings
CompleteLocalRings = OwnedCompleteLocalRings
