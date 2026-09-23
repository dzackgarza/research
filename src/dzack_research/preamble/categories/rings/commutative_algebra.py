r"""Basic commutative-algebra constructions needed by affine scheme theory."""

from math import factorial

from sage.all import (
    PolynomialRing as _SagePolynomialRing,
)
from sage.all import (
    PowerSeriesRing as _SagePowerSeriesRing,
)
from sage.all import (
    Zp as _SageZp,
)
from sage.categories.rings import Rings as SageRings
from sage.misc.cachefunc import cached_function, cached_method
from sage.misc.unknown import Unknown
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing_generic
from sage.rings.fraction_field import FractionField_generic as SageFractionField
from sage.rings.infinity import Infinity
from sage.rings.integer_ring import ZZ as SageZZ
from sage.structure.element import CommutativeRingElement, Element
from sage.structure.richcmp import op_EQ, op_NE
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.abstract_categories.objects import (
    OwnedCategory,
    OwnedParameterizedCategory,
)
from dzack_research.preamble.categories.abstract_categories.products import (
    InverseSystem,
    PosetCategory,
    SelectedLimitConstruction,
)
from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
    _OwnedAlgebraElement,
    _OwnedAlgebraParent,
    _algebra_structure_morphism,
    _algebra_with_structure,
)
from dzack_research.preamble.categories.algebras.free_algebras import SymmetricAlgebras
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.group.magmas import Monoids
from dzack_research.preamble.categories.rings.ring_foundation import _owned_engine_element
from dzack_research.preamble.categories.rings.ring_foundation import (
    LocalizationRings,
    OwnedAdicallyCompleteRings,
    OwnedCategoryOverBaseRing,
    OwnedRings,
    _engine_element,
    _engine_krull_dimension,
    _engine_quotient_cover_ideal,
    _engine_ring,
    _install_local_ring_construction,
    _own_ring,
    _ring_morphism_with_engine,
)
from dzack_research.preamble.categories.sets.cardinals import aleph0, cardinal
from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set
from dzack_research.preamble.categories.sets.indexed_families import finite_indexed_family
from dzack_research.preamble.categories.sets.set_categories import (
    NN,
    CountablyInfiniteSets,
    FiniteSets,
    PartiallyOrderedSets,
    SetInclusion,
    Sets,
    UncountableSets,
)
from dzack_research.preamble.categories.topological_spaces import TopologicalSpaces
from dzack_research.preamble.owned_category import _object_of
from dzack_research.preamble.owned_category_bases import Category


def _commutative_algebra_with_structure(algebra, base_ring, labels=None, *categories):
    r"""Construct the commutative owned algebra view over ``base_ring``."""
    return _algebra_with_structure(algebra, base_ring, labels, *categories)


class _PrimeSpectrumTopologyData:
    r"""Private topology datum for the Zariski space ``Spec R``."""

    def __init__(self, ring) -> None:
        self._ring = ring

    def ring(self):
        return self._ring

    def open_subsets(self, spectrum):
        return spectrum.power_set().condition_set(
            lambda subset: self.is_open_subset(spectrum, subset)
        )

    def is_open_subset(self, spectrum, subset) -> bool:
        power = spectrum.power_set()
        selected = power(subset)
        match selected:
            case _ if selected == power.bottom():
                return True
            case _ if selected == power.top():
                return True
            case _:
                assert False, (
                    "openness of a nontrivial arbitrary subset of Spec(R) requires "
                    "a represented Zariski-open presentation"
                )


class PrimeSpectra(OwnedCategory):
    r"""The prime spectra \(\operatorname{Spec}R\), ordered by inclusion."""

    def an_object(self):
        r"""\(\operatorname{Spec}\mathbb{Z}\)."""
        from sage.rings.integer_ring import ZZ as SageZZ

        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        return _own_ring(SageZZ).spectrum()

    def super_categories(self):
        return [PartiallyOrderedSets(), TopologicalSpaces()]

    class ElementMethods(Element):
        r"""What a prime point is."""

        def __init__(self, parent, ideal) -> None:
            self._ideal = ideal
            Element.__init__(self, parent)

        def ideal(self):
            return self._ideal

        prime_ideal = ideal

        @cached_method
        def local_ring(self):
            return self.parent().ring().localize_at_prime(self.ideal())

        stalk = local_ring

        @cached_method
        def residue_field(self):
            return self.local_ring().residue_field()

        @cached_method
        def residue_map(self):
            r"""Return the canonical map ``R -> kappa(p)`` attached to this point.

            This is the map whose factorization through ``R_p`` is the residue
            map of the local ring, so it is asked of the local ring rather than
            recomposed from it.
            """
            return self.local_ring().source_residue_map()

        @cached_method
        def residue_degree(self):
            r"""Return the finite degree ``[kappa(p):k]`` of a closed affine point."""
            ring = self.parent().ring()
            source = ring.quotient_source() if ring in QuotientRings() else ring
            base = source.base_ring()
            assert bool(_engine_ring(base).is_field()), (
                "residue degree here is relative to the coefficient field of an affine algebra"
            )
            assert bool(self.ideal().is_maximal()), (
                "a finite residue degree is represented here at a closed point"
            )
            point_engine = _engine_ideal(ring, self.ideal())
            if ring in QuotientRings():
                point_engine = _engine_quotient_cover_ideal(ring, point_engine)
            degree = int(point_engine.vector_space_dimension())
            return _own_ring(SageZZ)(degree)

        @cached_method
        def closure_dimension(self):
            r"""Return ``dim closure({p}) = dim R/p`` for this prime point."""
            return self.parent().ring().quotient_ring(self.ideal()).krull_dimension()

        def generic_local_length(self, ideal):
            r"""Return ``length_{R_p}((R/I)_p)`` at an associated generic point.

            For a ``p``-primary component ``Q`` in a polynomial algebra over a
            field, degree is multiplicative with generic length:

            ``deg(R/Q) = length_{R_p}(R_p/Q_p) * deg(R/p)``.

            The maintained polynomial-ideal Hilbert computation supplies both
            degrees. This is the positive-dimensional analogue of
            :meth:`local_length`, whose vector-space colength computation is
            appropriate only when the local quotient is supported at a closed
            point.
            """
            ring = self.parent().ring()
            if ideal.ring() is not ring:
                raise ValueError(
                    "generic local length requires an ideal of this point's ring"
                )
            source = ring.quotient_source() if ring in QuotientRings() else ring
            assert bool(_engine_ring(source.base_ring()).is_field()), (
                "generic local length here uses the affine-algebra-over-a-field degree formula"
            )

            def cover_ideal(selected):
                backend = _engine_ideal(ring, selected)
                if ring in QuotientRings():
                    backend = _engine_quotient_cover_ideal(ring, backend)
                return backend

            def projective_degree(backend):
                homogeneous = (
                    backend if backend.is_homogeneous() else backend.homogenize()
                )
                polynomial = homogeneous.hilbert_polynomial(algorithm="singular")
                if not polynomial:
                    raise ArithmeticError(
                        "the selected homogenized primary component has zero Hilbert polynomial"
                    )
                return SageZZ(
                    polynomial.leading_coefficient()
                    * factorial(int(polynomial.degree()))
                )

            denominator = projective_degree(cover_ideal(self.ideal()))
            if denominator <= 0:
                raise ArithmeticError(
                    "a prime component must have positive projective degree"
                )
            total = SageZZ.zero()
            for primary in ideal.primary_decomposition():
                if primary.radical() != self.ideal():
                    continue
                numerator = projective_degree(cover_ideal(primary))
                if numerator % denominator:
                    raise ArithmeticError(
                        "primary-component degree is not divisible by its reduced support degree"
                    )
                total += numerator // denominator
            return _own_ring(SageZZ)(total)

        def local_length(self, ideal):
            r"""Return ``length_{R_p}((R/I)_p)`` for a finite local quotient.

            If ``Q`` is the primary component supported at ``p``, then
            ``dim_k(R/Q) = length(R_p/Q_p) [kappa(p):k]``.  The residue-degree
            factor is therefore divided out explicitly, which is essential at
            a nonrational closed point.
            """
            ring = self.parent().ring()
            source = ring.quotient_source() if ring in QuotientRings() else ring
            assert bool(_engine_ring(source.base_ring()).is_field()), (
                "finite local length here uses finite-dimensional residue algebras over a field"
            )
            ideal_engine = _engine_ideal(ring, ideal)
            point_engine = _engine_ideal(ring, self.ideal())
            if ring in QuotientRings():
                ideal_engine = _engine_quotient_cover_ideal(ring, ideal_engine)
                point_engine = _engine_quotient_cover_ideal(ring, point_engine)
            matching = tuple(
                component
                for component in ideal_engine.primary_decomposition()
                if component.radical() == point_engine
            )
            if not matching:
                return _own_ring(SageZZ).zero()
            total_dimension = 0
            for component in matching:
                dimension = component.vector_space_dimension()
                if dimension not in SageZZ:
                    raise ValueError("the selected local quotient does not have finite length")
                total_dimension += int(dimension)
            residue_degree = int(self.residue_degree())
            if total_dimension % residue_degree:
                raise ArithmeticError(
                    "local vector-space dimension is not divisible by the residue-field degree"
                )
            return _own_ring(SageZZ)(total_dimension // residue_degree)

        @cached_method
        def height(self):
            r"""Return the height of this point, the codimension of its closure.

            The height of ``p`` is the dimension of the local ring ``R_p``, and
            in a domain that is finitely generated over a field, or of
            dimension at most one, the dimension formula
            ``height(p) + dim(R/p) = dim(R)`` holds, because such a ring is
            catenary and equidimensional.  So the height is read from two
            dimensions the ring already answers, rather than from a chain of
            primes nobody can enumerate.
            """

            ring = self.parent().ring()
            assert ring in OwnedRings().Commutative().NoZeroDivisors(), (
                f"the dimension formula that computes height here needs {ring} to be "
                "an integral domain"
            )
            finite_type_source = (
                ring.quotient_source()
                if ring in QuotientRings()
                else ring
            )
            assert (
                ring in OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals()
                or finite_type_source.base_ring() in OwnedRings().Division().Commutative()
            ), (
                f"the dimension formula that computes height here needs {ring} to be "
                "a principal ideal domain or finitely generated over a field, which is "
                "what makes it catenary and equidimensional"
            )
            quotient = ring.quotient_ring(self.ideal())
            return ring.krull_dimension() - quotient.krull_dimension()

        @cached_method
        def embedding_dimension(self):
            r"""Return ``dim_kappa(p) pR_p/(pR_p)^2``.

            Nakayama identifies this dimension with the minimal number of
            generators of the maximal ideal of ``R_p``.  The local ideal is an
            actual represented module, so the value is obtained from its
            existing residue-module construction rather than from a separate
            Jacobian formula.
            """
            local = self.local_ring()
            return local.maximal_ideal().minimal_number_of_generators()

        @cached_method
        def is_regular(self) -> bool:
            r"""Return whether the local ring ``R_p`` is regular.

            For a Noetherian local ring, regularity is exactly
            ``edim(R_p) = dim(R_p)``.  Here the first side is the residue
            dimension of the represented maximal ideal and the second is the
            height of ``p`` in the supported catenary affine-domain regime.
            """
            return self.embedding_dimension() == self.height()

        @cached_method
        def is_locally_factorial(self):
            r"""Return local factoriality where it follows from represented regularity.

            Every regular local ring is a unique-factorization domain.  This
            gives an exact positive criterion from the local-ring data already
            represented here.  A singular local ring can still be factorial,
            so failure of regularity is not a negative criterion and is left
            undecided until a divisor-class computation supplies one.
            """
            if self.is_regular():
                return True
            return Unknown

        def order_of_vanishing(self, function):
            r"""Return ``ord_p(f)`` at this height-one point.

            At a height-one prime of a normal domain ``R_p`` is a discrete
            valuation ring, and the order of vanishing is the length of
            ``R_p/(f)``, which is the valuation of ``f``.  Where the prime is
            generated by one element that element is a uniformizer, its powers
            are the powers of the maximal ideal, and the valuation is the
            multiplicity with which it divides ``f``.

            A prime that is not principal has no uniformizer, and its ordinary
            and symbolic powers can differ, so the multiplicity may not be read
            from membership in ``p^n``; that case is not computed here.
            """

            ring = self.parent().ring()
            function = ring(function)
            assert int(self.height()) == 1, (
                "an order of vanishing is stated at a prime of height one, and "
                f"{self.ideal()} has height {self.height()}"
            )
            prime = self.ideal()
            uniformizer = next(
                (
                    generator
                    for generator in prime.ideal_generators()
                    if ring.ideal(generator) == prime
                ),
                None,
            )
            assert uniformizer is not None, (
                "the order of vanishing is read from a uniformizer, so this prime must "
                f"be generated by one of its chosen generators, and {prime} is not"
            )
            assert not function.is_zero(), (
                "the zero function vanishes to infinite order, which is not an integer"
            )
            return function.valuation(uniformizer)

        def specializes_to(self, other) -> bool:
            if other.parent() is not self.parent():
                raise ValueError("specialization compares points of one spectrum")
            ring = self.parent().ring()
            return bool(_engine_ideal(ring, self.ideal()) <= _engine_ideal(ring, other.ideal()))

        def _richcmp_(self, other, op):
            if other.parent() is not self.parent() or other.parent() is not self.parent():
                return NotImplemented
            from sage.structure.richcmp import op_EQ, op_LE, op_LT, op_NE

            ring = self.parent().ring()
            left_ideal = _engine_ideal(ring, self.ideal())
            right_ideal = _engine_ideal(ring, other.ideal())
            if op == op_EQ:
                return left_ideal == right_ideal
            if op == op_NE:
                return left_ideal != right_ideal
            if op == op_LE:
                return self.specializes_to(other)
            if op == op_LT:
                return left_ideal != right_ideal and self.specializes_to(other)
            return NotImplemented

        def __hash__(self):
            r"""Hash the prime ideal equality compares, so a point may key a cache."""
            return hash(_engine_ideal(self.parent().ring(), self.ideal()))

        def _repr_(self):
            return f"Point {self.ideal()} of {self.parent()}"

    class ParentMethods:

        def __init__(self, ring, **rest) -> None:
            self._ring = _own_ring(ring)
            assert self._ring in OwnedRings().Commutative(), (
                "Spec(R) requires a commutative ring"
            )
            super().__init__(**rest)

        def ring(self):
            return self._ring

        def cardinality(self):
            r"""Return the exact number of prime points in supported finite spectra."""
            ring = self.ring()
            engine = _engine_ring(ring)
            assert (
                ring in OwnedRings().Division().Commutative()
                or isinstance(engine, IntegerModRing_generic)
            ), (
                f"exact cardinality of Spec({ring}) is represented only for a field or Z/nZ"
            )
            if ring in OwnedRings().Division().Commutative():
                return cardinal(1)
            modulus = SageZZ(engine.characteristic())
            return cardinal(len(tuple(modulus.prime_divisors())))

        def ringed_space(self):
            r"""Return the affine locally ringed space ``Spec(R)`` this spectrum underlies."""
            return self.ring().affine_spectrum()

        coordinate_ring = ring

        def __call__(self, ideal):
            r"""Construct a prime point directly from its represented ideal."""
            return self._element_constructor_(ideal)

        def _element_constructor_(self, ideal):
            if isinstance(ideal, self.category().ElementType) and ideal.parent() is self:
                return ideal
            candidate = _owned_ideal(self.ring(), ideal)
            if not bool(candidate.is_prime()):
                raise ValueError(f"{candidate} is not a prime ideal of {self.ring()}")
            return self.element_class(self, candidate)

        def __contains__(self, candidate) -> bool:
            if isinstance(candidate, self.category().ElementType):
                return candidate.parent() is self
            ideal = _engine_ideal(self.ring(), candidate)
            return bool(ideal.is_prime())

        def le(self, left, right) -> bool:
            return self._element_constructor_(left).specializes_to(
                self._element_constructor_(right)
            )

        def closed_set(self, ideal):
            return _zariski_closed_subobject(self, _owned_ideal(self.ring(), ideal))

        V = closed_set

        def distinguished_open(self, function):
            return _distinguished_open_subobject(self, function)

        D = distinguished_open

        def generic_point(self):
            engine = _engine_ring(self.ring())
            zero = engine.ideal(0)
            if not bool(zero.is_prime()):
                raise ValueError(f"{self.ring()} is not integral, so Spec has no unique generic point")
            return self._element_constructor_(zero)

        def _repr_(self):
            return f"Spec({self.ring()})"


def _engine_ring_value(ring, value):
    r"""Cross one owned/ordinary ring value to ``ring``'s private engine."""
    source = _own_ring(ring)
    engine = _engine_ring(source)
    parent = getattr(value, "parent", lambda: None)()
    if parent is engine or (parent is not None and parent in SageRings()):
        return engine(value)
    return engine(_engine_element(source, source(value)))


def _engine_ideal(ring, ideal):
    r"""Return the computation-ring ideal represented by ``ideal``.

    Protected commutative-algebra adapter under OWN-06. Representation
    dispatch is confined here; after a representation is selected, a failure
    in that route propagates rather than selecting another route by exception.
    """
    source = _own_ring(ring)
    engine = _engine_ring(source)
    if getattr(ideal, "ring", lambda: None)() is engine:
        return ideal
    from dzack_research.preamble.categories.rings.commutative_ideals import (
        CommutativeIdeals,
        _engine_commutative_ideal,
    )

    if ideal in CommutativeIdeals(source):
        return _engine_commutative_ideal(ideal)
    ideal_generators = getattr(ideal, "ideal_generators", None)
    if ideal_generators is not None:
        return engine.ideal(
            tuple(_engine_element(ring, value) for value in ideal_generators())
        )
    generators = getattr(ideal, "gens", None)
    if generators is not None and not isinstance(ideal, (tuple, list)):
        return engine.ideal(
            tuple(_engine_ring_value(ring, value) for value in generators())
        )
    if isinstance(ideal, (tuple, list)):
        return engine.ideal(tuple(_engine_ring_value(ring, value) for value in ideal))
    return engine.ideal(_engine_ring_value(ring, ideal))


def _engine_coefficient_ring(engine):
    r"""Return an optional coefficient ring of a private engine realization."""
    base_ring = getattr(engine, "base_ring", None)
    return None if base_ring is None else base_ring()


def _owned_ideal(ring, ideal):
    r"""Return an owned ideal unchanged, or raise represented input into one."""
    source = _own_ring(ring)
    from dzack_research.preamble.categories.rings.commutative_ideals import (
        CommutativeIdeals,
    )

    if ideal in CommutativeIdeals(source):
        return ideal
    backend = _engine_ideal(source, ideal)
    engine = _engine_ring(source)
    return source.ideal(
        *(_owned_engine_element(source, engine(generator)) for generator in backend.gens())
    )


def _canonical_map(domain, codomain, engine_map=None):
    source_engine = _engine_ring(domain)
    target_engine = _engine_ring(codomain)
    if engine_map is None and target_engine is not codomain:
        engine_map = target_engine.coerce_map_from(source_engine)

    def image(element):
        source = _engine_element(domain, domain(element))
        value = engine_map(source) if engine_map is not None else source
        return _owned_engine_element(codomain, target_engine(value))


    return _ring_morphism_with_engine(domain, codomain, image, engine_map)




class ZariskiClosedSubobjects(OwnedParameterizedCategory):
    r"""Closed subsets of one prime spectrum, retaining their defining ideal."""

    def parameter_category(self):
        return PrimeSpectra()

    def super_categories(self):
        return [Sets().Subobjects(self.base())]

    class ParentMethods:
        def __init__(self, defining_ideal, **rest):
            self._defining_ideal = defining_ideal
            super().__init__(**rest)

        def defining_ideal(self):
            return self._defining_ideal

        def _repr_(self):
            return f"V({self.defining_ideal()}) in {self.codomain()}"


class DistinguishedOpenSubobjects(OwnedParameterizedCategory):
    r"""Distinguished open subsets of one prime spectrum, retaining ``f``."""

    def parameter_category(self):
        return PrimeSpectra()

    def super_categories(self):
        return [Sets().Subobjects(self.base())]

    class ParentMethods:
        def __init__(self, function, **rest):
            self._function = function
            super().__init__(**rest)

        def function(self):
            return self._function

        def coordinate_ring(self):
            return self.codomain().ring().localization(self.function())

        def _repr_(self):
            return f"D({self.function()}) in {self.codomain()}"


def _zariski_closed_subobject(spectrum, ideal):
    domain = spectrum.condition_set(
        lambda point: bool(
            _engine_ideal(spectrum.ring(), ideal)
            <= _engine_ideal(spectrum.ring(), point.ideal())
        )
    )
    inclusion = SetInclusion(domain, spectrum)
    return Sets().Subobjects(spectrum).object(
        inclusion,
        categories=(ZariskiClosedSubobjects(spectrum),),
        construction_data={"defining_ideal": ideal},
    )


def _distinguished_open_subobject(spectrum, function):
    function = spectrum.ring()(function)
    domain = spectrum.condition_set(
        lambda point: _engine_element(spectrum.ring(), function)
        not in _engine_ideal(spectrum.ring(), point.ideal())
    )
    inclusion = SetInclusion(domain, spectrum)
    return Sets().Subobjects(spectrum).object(
        inclusion,
        categories=(DistinguishedOpenSubobjects(spectrum),),
        construction_data={"function": function},
    )



class QuotientRings(OwnedCategory):
    r"""Commutative quotient rings equipped with their quotient map."""

    class ElementMethods(Element):
        r"""What a class in \(R/I\) is."""

        def __init__(self, parent, representative) -> None:
            self._representative = parent.quotient_source()(representative)
            CommutativeRingElement.__init__(self, parent)

        def lift(self):
            return self._representative

        representative = lift

        def _add_(self, other):
            return self.parent()(self.lift() + other.lift())

        def _mul_(self, other):
            return self.parent()(self.lift() * other.lift())

        def _neg_(self):
            return self.parent()(-self.lift())

        def _sub_(self, other):
            r"""Subtraction in the additive group of ``R/I``."""
            return self._add_(-other)

        def is_unit(self):
            parent = self.parent()
            source = parent.quotient_source()
            unit_ideal = source.ideal(
                *parent.defining_ideal().ideal_generators(),
                self.lift(),
            )
            return unit_ideal.contains_ambient_element(source.one())

        def inverse_of_unit(self):
            parent = self.parent()
            assert parent._preamble_engine_ring is not None, (
                "an explicit inverse representative in this quotient requires the selected quotient computation realization"
            )
            represented = parent._engine_element(self)
            if not represented.is_unit():
                raise ZeroDivisionError(f"{self} is not a unit")
            return parent(represented**-1)

        def __truediv__(self, other):
            return self * self.parent()(other).inverse_of_unit()

        def _richcmp_(self, other, op):
            if other.parent() is not self.parent() or other.parent() is not self.parent():
                return NotImplemented
            if op not in (op_EQ, op_NE):
                return NotImplemented
            equal = self.parent().defining_ideal().contains_ambient_element(
                self.lift() - other.lift()
            )
            return equal if op == op_EQ else not equal

        def _repr_(self):
            return f"{self.lift()} mod {self.parent().defining_ideal()}"

    class ParentMethods:
        _derived_construction_parameters = frozenset({"base_ring"})

        def __init__(
            self,
            source,
            defining_ideal,
            _engine_ring=None,
            **rest,
        ) -> None:
            def quotient_map():
                return source.Mor(self, category=OwnedRings())(
                    lambda element: self(element),
                )

            self._quotient_source = source
            self._quotient_defining_ideal = defining_ideal
            self._quotient_map_factory = quotient_map
            self._preamble_engine_ring = _engine_ring
            super().__init__(
                base_ring=source,
                _engine_product=lambda left, right: QuotientRings.ElementMethods._mul_(left, right),
                _engine_scalar_action=lambda scalar, element: QuotientRings.ElementMethods._mul_(self(scalar), self(element)),
                _engine_unit=lambda algebra: QuotientRings.ParentMethods.one(algebra),
                **rest,
            )

        def _element_constructor_(self, value):
            from sage.structure.element import parent as element_parent
            from dzack_research.preamble.categories.modules.pure.modules import Modules

            source = element_parent(value)
            if source is not self and source in Modules(self.base_ring()) and source.unformed_module() is self:
                return source._element_of_unformed_module(value)
            if isinstance(value, self.category().ElementType) and value.parent() is self:
                return value
            source = self.quotient_source()
            source_engine = _engine_ring(source)
            value_parent = getattr(value, "parent", lambda: None)()
            quotient_engine = self._preamble_engine_ring
            if quotient_engine is not None and value_parent is quotient_engine:
                backend_value = quotient_engine(value)
                lift = getattr(backend_value, "lift", None)
                if lift is None:
                    raise TypeError(
                        "the selected quotient-engine element has no lift to the source ring"
                    )
                value = _owned_engine_element(source, source_engine(lift()))
            elif value_parent in OwnedRings():
                value_engine = _engine_ring(value_parent)
                if value_parent is source or value_engine is source_engine:
                    value = _owned_engine_element(source,
                        source_engine(_engine_element(value_parent, value))
                    )
                elif quotient_engine is not None and value_engine is quotient_engine:
                    backend_value = quotient_engine(_engine_element(value_parent, value))
                    lift = getattr(backend_value, "lift", None)
                    if lift is None:
                        raise TypeError(
                            "the equivalent owned quotient element has no lift to the source ring"
                        )
                    value = _owned_engine_element(source, source_engine(lift()))
            elif value_parent is source_engine:
                value = _owned_engine_element(source, source_engine(value))
            return self.element_class(self, value)

        def __call__(self, value):
            return self._element_constructor_(value)

        def _from_engine_element(self, value):
            r"""Cross one element of the selected quotient engine into this quotient."""
            engine = self._preamble_engine_ring
            assert engine is not None, (
                "crossing from a quotient engine requires this quotient to carry that selected realization"
            )
            return self._element_constructor_(engine(value))

        def _engine_element(self, value):
            engine = self._preamble_engine_ring
            assert engine is not None, (
                "crossing to a quotient engine requires this quotient to carry that selected realization"
            )
            element = self(value)
            source_value = _engine_element(self.quotient_source(), element.lift())
            quotient_map = engine.coerce_map_from(_engine_ring(self.quotient_source()))
            if quotient_map is not None:
                return quotient_map(source_value)
            return engine(source_value)

        def zero(self):
            return self(self.quotient_source().zero())

        def one(self):
            return self(self.quotient_source().one())

        def an_element(self):
            return self.one()

        def is_finite(self):
            if self._preamble_engine_ring is not None:
                return bool(self._preamble_engine_ring.is_finite())
            source_engine = _engine_ring(self.quotient_source())
            if isinstance(source_engine, SageNumberFieldOrder):
                return not _engine_ideal(
                    self.quotient_source(), self.defining_ideal()
                ).is_zero()
            from sage.misc.unknown import Unknown

            return Unknown

        def cardinality(self):
            if self._preamble_engine_ring is not None:
                return cardinal(self._preamble_engine_ring.cardinality())
            source_engine = _engine_ring(self.quotient_source())
            if isinstance(source_engine, SageNumberFieldOrder):
                defining = _engine_ideal(
                    self.quotient_source(), self.defining_ideal()
                )
                if not defining.is_zero():
                    return cardinal(SageZZ(defining.norm()))
            source = self.quotient_source()
            if source in OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals() and source in OwnedRings().Commutative().Local():
                valuations = []
                for generator in self.defining_ideal().ideal_generators():
                    backend = _engine_ring_value(source, generator)
                    if backend == source_engine.zero():
                        continue
                    valuation = getattr(backend, "valuation", None)
                    if valuation is None:
                        valuations = []
                        break
                    valuations.append(int(valuation()))
                if valuations:
                    residue_size = source.residue_field().cardinality()
                    return residue_size ** min(valuations)
            assert False, (
                "cardinality is defined for every quotient ring, but this represented "
                "quotient has no selected exact-cardinality computation"
            )

        def is_field(self):
            if self._preamble_engine_ring is None:
                return False
            return bool(self._preamble_engine_ring.is_field())

        def is_integral_domain(self):
            return bool(self.defining_ideal().is_prime())

        def krull_dimension(self):
            if self._preamble_engine_ring is not None:
                return _engine_krull_dimension(self)
            backend = _engine_ideal(self.quotient_source(), self.defining_ideal())
            return _owned_engine_element(SageZZ, SageZZ(backend.dimension()))

        def _repr_(self):
            return f"{self.quotient_source()} / {self.defining_ideal()}"

        def algebra_base_ring(self):
            return self.quotient_source()

        def quotient_source(self):
            return self._quotient_source

        def defining_ideal(self):
            return self._quotient_defining_ideal

        @cached_method
        def quotient_map(self):
            morphism = self._quotient_map_factory()
            if morphism.domain() is not self.quotient_source():
                raise ValueError("the quotient map has the wrong source ring")
            return morphism

        def localization_comparison(self, localization_ring):
            r"""Return ``S^{-1}(R/I) ~= S^{-1}R/S^{-1}I`` with both maps."""
            return _quotient_localization_comparison(self, localization_ring)

        def completion_comparison(self, source_ideal, *, precision=20):
            r"""Return ``(R/J)^ ~= R^/J R^`` for the selected adic topology.

            Here ``self = R/J`` and ``source_ideal`` is the ideal ``I`` of
            ``R`` whose image defines the topology on ``R/J``.  The supported
            theorem is the finite-module completion theorem over a Noetherian
            source; the comparison is built from the two canonical completion
            maps and the quotient maps rather than from the selected finite
            computation precision.
            """
            return _quotient_completion_comparison(
                self,
                source_ideal,
                precision=precision,
            )

        def characteristic(self):
            source = self.quotient_source()
            source_engine = _engine_ring(source)
            defining = self.defining_ideal()
            if source_engine is SageZZ:
                generators = tuple(defining.ideal_generators())
                generator = abs(
                    SageZZ(generators[0]) if generators else SageZZ.zero()
                )
                return _owned_engine_element(SageZZ, generator)
            coefficient_ring = _engine_coefficient_ring(source_engine)
            if coefficient_ring is not None:
                try:
                    if bool(coefficient_ring.is_field()):
                        return _owned_engine_element(
                            SageZZ,
                            SageZZ(coefficient_ring.characteristic()),
                        )
                except (AttributeError, NotImplementedError, TypeError, ValueError):
                    pass
            try:
                return _owned_engine_element(
                    SageZZ,
                    SageZZ(_engine_ring(self).characteristic()),
                )
            except NotImplementedError as error:
                raise AssertionError(
                    "characteristic of this quotient requires contraction of the defining ideal to the prime subring"
                ) from error

        @cached_method
        def _affine_normalization_data(self):
            r"""Return the selected exact normalization data for this reduced affine ring.

            The public object remains an owned quotient ring.  Singular's
            ``normal.lib`` is only the private engine computing an affine
            presentation of the integral closure, its normalization map,
            conductor, and delta invariant.  No Singular ring, ideal, or map
            crosses this boundary.
            """
            return _affine_reduced_quotient_normalization_data(self)

        @cached_method
        def normalization(self):
            r"""Return the integral closure of this reduced affine ring in its total quotient ring."""
            return self._affine_normalization_data().normalization

        @cached_method
        def normalization_map(self):
            r"""Return the canonical finite birational map ``A -> A^nu``."""
            return self._affine_normalization_data().normalization_map

        def normalization_components(self):
            r"""Return the normalized irreducible components with their maps."""
            return self._affine_normalization_data().components

        def is_reduced(self) -> bool:
            defining = _engine_ideal(self.quotient_source(), self.defining_ideal())
            return defining.radical() == defining

        @cached_method
        def _presentation_minimal_primes(self):
            r"""Return the minimal primes upstairs in the chosen presentation ring."""
            from dzack_research.preamble.categories.rings.commutative_ideals import (
                _from_engine_ideal,
            )

            source = self.quotient_source()
            defining = _engine_ideal(source, self.defining_ideal())
            return finite_ordered_set(
                tuple(
                    _from_engine_ideal(source, prime)
                    for prime in defining.minimal_associated_primes()
                )
            )

        @cached_method
        def minimal_primes(self):
            r"""Return the minimal prime ideals of this quotient ring."""
            return finite_ordered_set(
                tuple(
                    self.ideal(
                        *(self(generator) for generator in prime.ideal_generators())
                    )
                    for prime in self._presentation_minimal_primes()
                )
            )

        @cached_method
        def irreducible_components(self):
            r"""Return the component domains ``R/p`` for the minimal primes ``p``."""
            if not self.is_reduced():
                raise ValueError("irreducible components here require a reduced quotient ring")
            return finite_ordered_set(
                tuple(
                    self.quotient_source().quotient_ring(prime)
                    for prime in self._presentation_minimal_primes()
                )
            )

        @cached_method
        def total_quotient_ring(self):
            r"""Return the total quotient ring of this supported reduced affine quotient."""
            if self in OwnedRings().Commutative().NoZeroDivisors():
                return self.fraction_field()
            assert self.is_reduced(), (
                "the selected total-quotient realization is the product of component fraction fields and therefore requires a reduced affine quotient"
            )
            fields = tuple(
                component.fraction_field() for component in self.irreducible_components()
            )
            return _finite_product_ring(fields)

        @cached_method
        def total_quotient_map(self):
            r"""Return the canonical injection ``A -> Q(A)`` in the supported reduced case."""
            if self in OwnedRings().Commutative().NoZeroDivisors():
                return self.fraction_field_map()
            components = tuple(self.irreducible_components())
            fields = tuple(component.fraction_field() for component in components)
            field_maps = tuple(component.fraction_field_map() for component in components)
            target = self.total_quotient_ring()
            target_engine = _engine_ring(target)

            def image(element):
                lift = element.lift()
                values = tuple(
                    field_map(component(lift))
                    for component, field_map in zip(components, field_maps, strict=True)
                )
                backend = target_engine(
                    tuple(
                        _engine_element(field, value)
                        for field, value in zip(fields, values, strict=True)
                    )
                )
                return _owned_engine_element(target, backend)

            return self.Mor(target)(image)

        @cached_method
        def conductor_ideal(self):
            r"""Return ``(A :_A A^nu)``, the conductor of the normalization."""
            return self._affine_normalization_data().conductor

        @cached_method
        def delta_invariant(self):
            r"""Return ``dim_k(A^nu/A)`` when finite, and infinity otherwise."""
            delta = self._affine_normalization_data().delta
            return Infinity if delta < 0 else delta

        @cached_method
        def is_normal(self) -> bool:
            r"""Return whether this affine domain equals its integral closure."""
            return bool(self._affine_normalization_data().is_normal)

    def super_categories(self):
        return [OwnedRings().Commutative()]


class _AffineReducedQuotientNormalizationData(SageObject):
    r"""Owned-boundary data returned by the private affine-normalization engine."""

    def __init__(
        self,
        normalization,
        normalization_map,
        conductor,
        delta,
        is_normal,
        components,
    ) -> None:
        self.normalization = normalization
        self.normalization_map = normalization_map
        self.conductor = conductor
        self.delta = int(delta)
        self.is_normal = bool(is_normal)
        self.components = components


def _finite_product_ring(factors):
    factors = tuple(factors)
    if not factors:
        raise ValueError("a finite product ring requires at least one factor")
    if len(factors) == 1:
        return factors[0]
    engines = tuple(_engine_ring(factor) for factor in factors)
    return _own_ring(engines[0].cartesian_product(*engines[1:]))


def _affine_reduced_quotient_normalization_data(quotient):
    r"""Cross Singular ``normal.lib`` output back into owned affine algebra data.

    This adapter intentionally uses Sage's persistent Singular interface rather
    than an ad-hoc process or textual file protocol.  ``normal.lib`` computes
    the normalization componentwise for a reduced affine quotient, the
    generator images of every normalization map, the conductor, and ``delta``
    in one exact computation.
    The returned Singular ring is converted by Sage's own ``sage()`` crossing,
    then reconstructed through the source ring's ``quotient_ring`` and ``Mor`` methods.
    """
    source = quotient.quotient_source()
    source_engine = _engine_ring(source)
    if not quotient.is_reduced():
        raise ValueError("normalization here requires a reduced affine quotient")
    assert hasattr(source_engine, "_singular_"), (
        "affine normalization currently requires a polynomial presentation supported by Singular"
    )

    defining_engine = _engine_ideal(source, quotient.defining_ideal())
    from sage.interfaces.singular import singular

    previous_ring = singular.current_ring()
    try:
        source_engine._singular_(singular).set_ring()
        singular.lib("normal.lib")
        defining_singular = defining_engine._singular_(singular)
        normal_data = defining_singular.normal("useRing", "withDelta", "prim")

        normal_rings = normal_data[1]

        # The conductor is an ideal in the original polynomial presentation.
        source_engine._singular_(singular).set_ring()
        conductor_singular = defining_singular.normalConductor(normal_data)
        conductor_engine = conductor_singular.sage(source_engine)
        conductor = source.ideal(
            *(
                _owned_engine_element(source, source_engine(generator))
                for generator in conductor_engine.gens()
            )
        )

        total_delta = int(normal_data[3][2].sage())

        source_quotient_engine = _engine_ring(quotient)
        normalizations = []
        normalization_maps = []
        component_primes = []
        from dzack_research.preamble.categories.rings.commutative_ideals import (
            _from_engine_ideal,
        )

        for position in range(1, len(normal_rings) + 1):
            normal_ring_singular = normal_rings[position]
            normal_ring_singular.set_ring()
            normal_cover_engine = normal_ring_singular.sage()
            normal_ideal_engine = singular("norid").sage(normal_cover_engine)
            normal_map_images_engine = singular("normap").sage(normal_cover_engine)
            normal_cover = _own_ring(normal_cover_engine)
            normal_ideal = normal_cover.ideal(
                *(
                    _owned_engine_element(normal_cover, normal_cover_engine(generator))
                    for generator in normal_ideal_engine.gens()
                )
            )
            component = normal_cover.quotient_ring(normal_ideal)
            target_engine = _engine_ring(component)
            target_images = tuple(
                target_engine(normal_cover_engine(generator))
                for generator in normal_map_images_engine.gens()
            )
            if len(target_images) != source_engine.ngens():
                raise ArithmeticError(
                    "Singular's normalization map did not return one image per source generator"
                )
            source_component_map = source_engine.mor(target_images, target_engine)
            source_prime = _from_engine_ideal(source, source_component_map.kernel())
            component_prime = quotient.ideal(
                *(quotient(generator) for generator in source_prime.ideal_generators())
            )
            engine_component_map = source_quotient_engine.mor(target_images, target_engine)
            def component_image(
                element,
                component=component,
                engine_component_map=engine_component_map,
            ):
                return _owned_engine_element(component,
                    engine_component_map(_engine_element(quotient, element))
                )

            component_map = _ring_morphism_with_engine(
                quotient, component, component_image, engine_component_map
            )
            normalizations.append(component)
            normalization_maps.append(component_map)
            component_primes.append(component_prime)

        normalizations = tuple(normalizations)
        normalization_maps = tuple(normalization_maps)
        component_primes = tuple(component_primes)
        normalization = _finite_product_ring(normalizations)
        if len(normalizations) == 1:
            normalization_map = normalization_maps[0]
        else:
            product_engine = _engine_ring(normalization)

            def into_product(element):
                values = tuple(map_(element) for map_ in normalization_maps)
                backend = product_engine(
                    tuple(
                        _engine_element(component, value)
                        for component, value in zip(normalizations, values, strict=True)
                    )
                )
                return _owned_engine_element(normalization, backend)

            normalization_map = quotient.Mor(normalization)(into_product)

        component_indices = finite_ordered_set(range(len(normalizations)))
        components = finite_indexed_family(
            component_indices,
            lambda position: (
                component_primes[int(position)],
                normalizations[int(position)],
                normalization_maps[int(position)],
            ),
            name=f"Normalized components of {quotient}",
        )

        return _AffineReducedQuotientNormalizationData(
            normalization,
            normalization_map,
            quotient.ideal(*(quotient(generator) for generator in conductor.ideal_generators())),
            total_delta,
            total_delta == 0,
            components,
        )
    finally:
        try:
            previous_ring.set_ring()
        except (AttributeError, TypeError, ValueError):
            pass







class QuotientLocalizationComparison(SageObject):
    r"""The canonical compatibility of quotient and localization."""

    def __init__(
        self,
        source_quotient,
        localization_ring,
        localized_quotient,
        quotient_after_localization,
        forward,
        inverse,
        extended_ideal,
    ) -> None:
        self._source_quotient = source_quotient
        self._localization_ring = localization_ring
        self._localized_quotient = localized_quotient
        self._quotient_after_localization = quotient_after_localization
        self._forward = forward
        self._inverse = inverse
        self._extended_ideal = extended_ideal

    def source_quotient(self):
        return self._source_quotient

    def localization_ring(self):
        return self._localization_ring

    def localized_quotient(self):
        r"""Return ``S^{-1}(R/I)``."""
        return self._localized_quotient

    def quotient_after_localization(self):
        r"""Return ``S^{-1}R/S^{-1}I``."""
        return self._quotient_after_localization

    def extended_ideal(self):
        return self._extended_ideal

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return (
            f"{self.localized_quotient()} ~= "
            f"{self.quotient_after_localization()}"
        )


class QuotientCompletionComparison(SageObject):
    r"""The canonical Noetherian comparison ``(R/J)^ ~= R^/J R^``."""

    def __init__(
        self,
        source_quotient,
        source_ideal,
        source_completion,
        completed_quotient,
        quotient_after_completion,
        extended_defining_ideal,
        forward,
        inverse,
    ) -> None:
        self._source_quotient = source_quotient
        self._source_ideal = source_ideal
        self._source_completion = source_completion
        self._completed_quotient = completed_quotient
        self._quotient_after_completion = quotient_after_completion
        self._extended_defining_ideal = extended_defining_ideal
        self._forward = forward
        self._inverse = inverse

    def source_quotient(self):
        return self._source_quotient

    def source_ideal(self):
        return self._source_ideal

    def source_completion(self):
        return self._source_completion

    def completed_quotient(self):
        r"""Return ``(R/J)^`` completed at the image of ``I``."""
        return self._completed_quotient

    def quotient_after_completion(self):
        r"""Return ``R^ / J R^``."""
        return self._quotient_after_completion

    def extended_defining_ideal(self):
        return self._extended_defining_ideal

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return (
            f"{self.completed_quotient()} ~= "
            f"{self.quotient_after_completion()}"
        )


class MaximalAdicLocalizationCompletionComparison(SageObject):
    r"""The canonical comparison ``R^_m ~= (R_m)^`` for Noetherian ``R``."""

    def __init__(
        self,
        source_completion,
        local_ring,
        local_completion,
        forward,
        inverse,
    ) -> None:
        self._source_completion = source_completion
        self._local_ring = local_ring
        self._local_completion = local_completion
        self._forward = forward
        self._inverse = inverse

    def source_completion(self):
        return self._source_completion

    def local_ring(self):
        return self._local_ring

    def local_completion(self):
        return self._local_completion

    def forward(self):
        return self._forward

    isomorphism = forward

    def inverse(self):
        return self._inverse

    def _repr_(self):
        return f"{self.source_completion()} ~= {self.local_completion()}"






class PrimeLocalizations(OwnedCategory):
    r"""Prime local rings ``R_p`` represented by fractions with denominator outside ``p``."""

    def super_categories(self):
        r"""``R_p`` is the localization at the multiplicative set ``R \ p``."""
        return [LocalizationRings(), OwnedRings().Commutative().Local()]

    class ElementMethods:
        def is_unit(self):
            parent = self.parent()
            return not parent.localized_prime().contains_ambient_element(
                self.numerator()
            )

        def inverse_of_unit(self):
            if not self.is_unit():
                raise ZeroDivisionError(f"{self} is not a unit")
            return self.parent().fraction(
                self.denominator(),
                self.numerator(),
            )

    class ParentMethods:
        def __init__(
            self,
            source,
            submonoid,
            fraction_field=None,
            *,
            engine_ring=None,
            **rest,
        ) -> None:
            self._preamble_fraction_field = fraction_field
            base = source.base_ring()
            algebra_source = (
                source
                if base is not None and source in Algebras(base).Associative().Unital()
                else None
            )
            super().__init__(
                source,
                submonoid,
                _engine_ring=engine_ring,
                algebra_source=algebra_source,
                **rest,
            )

        def fraction_field(self):
            r"""Return ``Frac(R_p)``, which is ``Frac(R)``.

            Localizing does not change the fraction field: ``R -> R_p`` is
            injective for a domain and every nonzero element of ``R_p`` is
            already invertible in ``Frac(R)``.  A ring with zero divisors has
            no fraction field, and neither has its localization.
            """
            represented = self._preamble_fraction_field
            assert represented is not None, (
                f"{self.localization_source()} has zero divisors, so neither it nor {self} "
                "has a fraction field"
            )
            return represented

        @cached_method
        def residue_field(self):
            r"""Return ``kappa(p) = R_p / p R_p``.

            ``R/p`` is a domain because ``p`` is prime, and the classes of
            ``R \\ p`` are exactly its nonzero elements, so inverting them gives
            ``Frac(R/p)`` and killing ``p R_p`` afterwards changes nothing.
            When ``p`` is maximal that fraction field is ``R/p`` itself, which
            is what a closed point of the spectrum has.

            This asks ``R`` for a quotient and a fraction field and never for a
            fraction field of its own, so a reducible or nonreduced ``R``,
            which has none, still has a residue field at every point.
            """
            quotient = self.localization_source().quotient_ring(self.localized_prime())
            if quotient in OwnedRings().Division().Commutative():
                return quotient
            return quotient.fraction_field()

        @cached_method
        def source_residue_map(self):
            r"""Return ``R -> kappa(p)``, the value of a function at this point."""
            quotient = self.localization_source().quotient_ring(self.localized_prime())
            residue = self.residue_field()
            if residue is quotient:
                return quotient.quotient_map()
            return _canonical_map(quotient, residue) * quotient.quotient_map()

        @cached_method
        def residue_map(self):
            r"""Return ``R_p -> kappa(p)``, the quotient by the maximal ideal.

            ``R -> kappa(p)`` carries every ``s`` outside ``p`` to a nonzero
            class of the domain ``R/p``, hence to a unit of its fraction field.
            So it inverts ``R \\ p`` and the universal property of ``R_p``
            factors it uniquely through this ring; that factorization is the
            residue map, and its kernel is ``p R_p``.
            """
            return self.induced_morphism(self.source_residue_map())

        @cached_method
        def maximal_ideal(self):
            r"""Return ``p R_p``, the extension of ``p`` along ``R -> R_p``.

            The maximal ideal of a local ring is its non-units, and ``a/s`` is
            a non-unit of ``R_p`` exactly when ``a`` lies in ``p``, so the
            non-units are the ideal ``p`` generates here.  Constructing it as
            the extension of ``p`` is what gives it the operations of an ideal
            rather than a name and a generating set.
            """
            return self.localized_prime().extension_to_localization(self)

        def localize_module(self, module):
            r"""Return ``R_p tensor_R M`` through the module-localization theory."""

            if module.base_ring() is not self.localization_source():
                raise ValueError("the module has the wrong source ring for this localization")
            return self.localization_functor()(module)

        def localized_prime(self):
            structure = self.localization_submonoid()._structure_data()
            if structure.get("kind") != "prime_complement":
                raise ArithmeticError(
                    "a prime localization must retain a prime-complement localization submonoid"
                )
            prime = structure.get("prime_ideal")
            if prime is None:
                raise ArithmeticError(
                    "a prime-complement localization submonoid must retain its selected prime ideal"
                )
            return prime

        def is_field(self):
            r"""Return whether the maximal ideal ``p R_p`` vanishes."""
            return all(
                self(generator) == self.zero()
                for generator in self.localized_prime().ideal_generators()
            )


class IdealExtensionData(SageObject):
    r"""One ideal extension ``I -> I S`` along a represented ring morphism.

    The extended ideal remains the canonical ideal subobject of the codomain;
    this construction object retains the source ideal and the morphism that
    produced it without making either one part of the ideal's identity.
    """

    def __init__(self, morphism, source_ideal) -> None:
        if source_ideal.ring() is not morphism.domain():
            raise ValueError("an ideal extension starts with an ideal of the morphism domain")
        self._morphism = morphism
        self._source_ideal = source_ideal
        self._extended_ideal = morphism.extension_of_ideal(source_ideal)

    def morphism(self):
        return self._morphism

    extension_map = morphism

    def source_ideal(self):
        return self._source_ideal

    def extended_ideal(self):
        return self._extended_ideal

    def _repr_(self):
        return (
            f"Extension of {self.source_ideal()} along {self.morphism()} "
            f"to {self.extended_ideal()}"
        )


class AdicCompletions(Category):
    r"""Adic completions equipped with source and ideal of definition."""

    def an_object(self):
        r"""The 2-adic completion of the owned integers."""
        from sage.rings.integer_ring import ZZ as SageZZ

        integers = _own_ring(SageZZ)
        return self(integers, integers.ideal(integers(2)), precision=4)

    def super_categories(self):
        return [OwnedAdicallyCompleteRings()]

    def _call_(self, ring, ideal, *, precision=20):
        r"""Construct the adic completion from its authoritative defining datum.

        Public notation and ring methods both route through this category
        constructor.  The private cached constructor receives only owned data,
        so repeated routes to the same ``(R,I,precision)`` return the same
        mathematical parent rather than parallel completion objects.
        """
        source = _own_ring(ring)
        defining = _owned_ideal(source, ideal)
        return _adic_completion_from_owned_data(
            source,
            defining,
            int(precision),
        )

    class ParentMethods:
        def completion_source(self):
            return self._adic_completion_source

        def completion_map(self):
            morphism = self._realized_completion_map
            if morphism is None:
                morphism = self._adic_completion_map_factory()
                if morphism.domain() is not self.completion_source():
                    raise ValueError("the completion map has the wrong source ring")
                self._realized_completion_map = morphism
            return morphism

        def _completion_projection_lift(self):
            r"""Return the retained finite-stage lift used to realize adic projections.

            Protected completion-realization contract. Its callers are this
            completion's projection operation and the prime-localization
            completion constructor, which transports the same retained lift
            through the localization map.
            """
            return self._adic_projection_lift

        @cached_method
        def algebra_structure_morphism(self):
            r"""Return the coefficient structure map without duplicating the completion map.

            For an ordinary adic completion the coefficient ring is its source,
            so the structure map is exactly the canonical completion map.  A
            formal power-series specialization is instead an algebra over the
            coefficient ring below its polynomial completion source and keeps
            that distinct scalar structure.
            """
            if self.algebra_base_ring() is self.completion_source():
                return self.completion_map()
            return _algebra_structure_morphism(self)

        @cached_method
        def ideal_extension(self):
            r"""Return the construction ``I -> I A^`` along the completion map."""
            return IdealExtensionData(
                self.completion_map(),
                self.ideal_of_definition(),
            )

        def extended_ideal(self):
            r"""Return ``I A^``, retaining its extension construction separately."""
            return self.ideal_extension().extended_ideal()

        @cached_method
        def truncation_ideal_extension(self, exponent):
            r"""Return the image ideal of ``I`` in ``A/I^exponent`` with its map."""
            target = self.adic_truncation(exponent)
            return IdealExtensionData(
                target.quotient_map(),
                self.ideal_of_definition(),
            )

        @cached_method
        def completion_map_kernel(self):
            r"""Return ``ker(A -> A^)`` in the represented exact regimes.

            The kernel is ``intersection I^n``.  The zero/nilpotent and
            idempotent cases are exact from the represented ideal arithmetic;
            no injectivity claim is made outside a theorem or one of these
            computations.
            """
            source = self.completion_source()
            represented = self._adic_completion_map_kernel
            if represented is not None:
                return represented
            zero = source.ideal(source.zero())
            defining = self.ideal_of_definition()
            if defining == zero:
                return zero
            square = defining.power(2)
            if square == zero:
                return zero
            if square == defining:
                return defining
            supported_by_krull_intersection = (
                source in OwnedRings().Noetherian()
                and source in OwnedRings().Commutative().NoZeroDivisors()
            )
            assert supported_by_krull_intersection, (
                "the completion-map kernel is intersection I^n; outside the represented exact cases and the Noetherian-domain Krull-intersection theorem, that intersection has no selected exact computation"
            )
            return zero

        def is_adically_separated(self) -> bool:
            r"""Return whether the represented source embeds in this completion."""
            source = self.completion_source()
            return self.completion_map_kernel() == source.ideal(source.zero())

        def is_completion_map_injective(self) -> bool:
            r"""Return injectivity exactly when the represented kernel is known."""
            return self.is_adically_separated()

        def is_flat_over_source(self):
            r"""Return flatness of ``A^`` over ``A`` in the Noetherian regime."""
            if self.completion_source() in OwnedRings().Noetherian():
                return True
            return Unknown

        def computation_precision(self):
            return self._adic_completion_precision

        @cached_method
        def adic_inverse_system(self):
            r"""Return the represented inverse system ``n |-> A/I^(n+1)``."""
            functor = _AdicQuotientInverseSystem(self)
            return functor.system_category().object(functor)

        @cached_method
        def adic_truncation(self, exponent):
            r"""Return the canonical adic quotient ``A / I^exponent``.

            It is not called an Artin quotient without a finite-length
            hypothesis: for example ``QQ[x,y]/(x^n)`` still has positive
            dimension.
            """
            exponent = int(exponent)
            if exponent <= 0:
                raise ValueError("an adic truncation exponent is positive")
            source = self.completion_source()
            defining = self.ideal_of_definition()
            return source.quotient_ring(defining.power(exponent))

        def adic_artin_truncation(self, exponent):
            r"""Return ``A/I^exponent`` after requiring it to be Artinian."""
            quotient = self.adic_truncation(exponent)
            if quotient not in OwnedRings().Artinian():
                raise ValueError(
                    "this adic quotient has not been established to have finite length"
                )
            return quotient

        @cached_method
        def adic_transition_map(self, higher_exponent, lower_exponent):
            r"""Return ``A/I^higher -> A/I^lower`` for ``higher >= lower``."""
            higher_exponent = int(higher_exponent)
            lower_exponent = int(lower_exponent)
            if lower_exponent <= 0 or higher_exponent < lower_exponent:
                raise ValueError("adic transition exponents satisfy higher >= lower > 0")
            higher = self.adic_truncation(higher_exponent)
            lower = self.adic_truncation(lower_exponent)
            lower_projection = lower.quotient_map()
            return higher.Mor(lower)(
                lambda element: lower_projection(element.lift()),
            )

        @cached_method
        def adic_projection(self, exponent):
            r"""Return the canonical projection ``A_hat -> A/I^exponent``."""
            exponent = int(exponent)
            if exponent <= 0:
                raise ValueError("an adic projection exponent is positive")
            target = self.adic_truncation(exponent)
            quotient_map = target.quotient_map()
            projection_lift = self._completion_projection_lift()
            assert projection_lift is not None, (
                "this completion realization must carry a finite-truncation lift before its adic projections are computable"
            )

            def image(element):
                backend = _engine_element(self, self(element))
                return quotient_map(projection_lift(backend, exponent))

            return self.Mor(target)(image)

        def induced_map(self, source_morphism, target_completion):
            r"""Return the continuous map of completions induced by ``source_morphism``.

            This supported topology requires ``f(I) <= J``.  The mathematical
            map is unique by completion; computation on an element uses its
            exact retained source expression and otherwise stays at the
            declared computational frontier.
            """
            if source_morphism.domain() is not self.completion_source():
                raise ValueError("the ring morphism has the wrong source for this completion")
            if source_morphism.codomain() is not target_completion.completion_source():
                raise ValueError("the ring morphism has the wrong target source ring")
            target_ideal = target_completion.ideal_of_definition()
            if any(
                not target_ideal.contains_ambient_element(source_morphism(generator))
                for generator in self.ideal_of_definition().ideal_generators()
            ):
                raise ValueError("the source ideal does not map into the target ideal")
            identity_factory = getattr(source_morphism.parent(), "identity", None)
            if (
                source_morphism.domain() is source_morphism.codomain()
                and callable(identity_factory)
                and source_morphism is identity_factory()
                and target_completion is self
            ):
                return self.Mor(self).identity()

            def image(element):
                selected = self(element)
                source_expression = selected.exact_source_expression()
                if source_expression is None:
                    raise AssertionError(
                        "this continuous completion map needs an exact retained source expression for evaluation"
                    )
                return target_completion.completion_map()(
                    source_morphism(source_expression)
                )

            return self.Mor(target_completion)(image)

        @cached_method
        def maximal_localization_comparison(self):
            r"""Return ``R^_m ~= (R_m)^`` when the ideal of definition is maximal.

            For Noetherian ``R`` completion at a maximal ideal agrees with
            completion after localizing at that maximal ideal.  Both arrows
            are assembled from the localization/completion universal maps;
            this method does not assert any analogous comparison for an
            arbitrary localization.
            """
            source = self.completion_source()
            maximal = self.ideal_of_definition()
            if source not in OwnedRings().Noetherian():
                raise TypeError("the maximal-adic localization comparison requires a Noetherian source")
            if not bool(maximal.is_maximal()):
                raise TypeError("the localization/completion isomorphism here is maximal-adic")
            local = source.localize_at_prime(maximal)
            local_completion = local.adic_completion(
                local.maximal_ideal(),
                precision=self.computation_precision(),
            )
            forward = self.induced_map(local.localization_map(), local_completion)
            local_to_completion = local.induced_morphism(self.completion_map())
            inverse = local_completion.induced_map(local_to_completion, self)
            return MaximalAdicLocalizationCompletionComparison(
                self,
                local,
                local_completion,
                forward,
                inverse,
            )

        @cached_method
        def residue_map(self):
            r"""Return ``A^ -> A/I`` when the adic ideal is maximal."""
            if not bool(self.ideal_of_definition().is_maximal()):
                raise TypeError("a residue map is local data and this adic ideal is not maximal")
            residue = self.residue_field()
            projection = self.adic_projection(1)
            if projection.codomain() is residue:
                return projection
            return _canonical_map(projection.codomain(), residue) * projection

        @cached_method
        def source_residue_map(self):
            r"""Return the comparison ``A -> A^ -> kappa(I)`` for maximal ``I``."""
            return self.residue_map() * self.completion_map()

        @cached_method
        def adic_limit_cone(self):
            r"""Return the canonical cone ``A_hat -> (A/I^n)_n``."""
            system = self.adic_inverse_system()
            diagram = system.functor()
            return system.Cones().cone(
                self,
                lambda index: self.adic_projection(diagram.exponent(index)),
            )

        @cached_method
        def adic_limit_construction(self):
            r"""Return the selected inverse-limit construction defining this completion.

            The represented completion and its cone are exact.  Constructing a
            map into an arbitrary infinite inverse limit from a supplied coherent
            cone is not implemented by the generic finite product/equalizer
            solver; the supported series engine is the selected realization of
            this particular limit.
            """
            system = self.adic_inverse_system()
            diagram = system.functor()
            cone = self.adic_limit_cone()

            def factorizer(supplied_cone):
                assert supplied_cone is cone, (
                    "factorization of a noncanonical cone into this infinite adic limit requires a represented compatible-series construction"
                )
                return self.Mor(self).identity()

            return SelectedLimitConstruction(diagram, cone, factorizer)


class _AdicQuotientInverseSystem(Functor):
    r"""The inverse system ``A/I <- A/I^2 <- ...`` owned by one completion."""

    def __init__(self, completion) -> None:
        self._completion = completion
        self._base_index = PosetCategory(NN)
        self._system_category = InverseSystem(
            self._base_index,
            OwnedRings().Commutative(),
        )
        super().__init__(
            self._system_category.index_category(),
            OwnedRings().Commutative(),
        )

    def completion(self):
        return self._completion

    def base_index_category(self):
        return self._base_index

    def system_category(self):
        return self._system_category

    def exponent(self, index):
        return NN(int(index.underlying_object().value()) + 1)

    def _apply_object(self, index):
        return self.completion().adic_truncation(self.exponent(index))

    def _apply_morphism(self, morphism):
        underlying = morphism.underlying_arrow()
        lower = int(underlying.domain().value()) + 1
        higher = int(underlying.codomain().value()) + 1
        return self.completion().adic_transition_map(higher, lower)


class _AdicCompletionElement(_OwnedAlgebraElement):
    r"""An element of a completion with equality respecting its information model."""

    def __init__(self, parent, backend_value, *, exact_source_expression=None) -> None:
        super().__init__(parent, backend_value)
        self._exact_source_expression = exact_source_expression

    def exact_source_expression(self):
        r"""Return the retained exact source expression, or ``None``.

        A finite computational approximation does not become exact merely by
        living in the completion.  Expressions arriving through the completion
        map, however, still carry their exact source expression, and ordinary
        ring operations preserve that information while both operands have it.
        """
        return self._exact_source_expression

    def _with_source_expression(self, backend_value, source_expression):
        constructor = getattr(self.parent(), "_completion_element", None)
        if constructor is None:
            return _owned_engine_element(self.parent(), backend_value)
        return constructor(backend_value, source_expression=source_expression)

    def _add_(self, other):
        left_source = self.exact_source_expression()
        right_source = other.exact_source_expression()
        source_expression = None
        if left_source is not None and right_source is not None:
            source_expression = left_source + right_source
        return self._with_source_expression(
            self._backend() + other._backend(),
            source_expression,
        )

    def _mul_(self, other):
        left_source = self.exact_source_expression()
        right_source = other.exact_source_expression()
        source_expression = None
        if left_source is not None and right_source is not None:
            source_expression = left_source * right_source
        return self._with_source_expression(
            self._backend() * other._backend(),
            source_expression,
        )

    def _neg_(self):
        source_expression = self.exact_source_expression()
        if source_expression is not None:
            source_expression = -source_expression
        return self._with_source_expression(-self._backend(), source_expression)

    def __pow__(self, exponent, modulus=None):
        if modulus is not None:
            return super().__pow__(exponent, modulus)
        try:
            exponent = exponent.__index__()
        except AttributeError:
            return NotImplemented
        source_expression = self.exact_source_expression()
        if source_expression is not None and exponent >= 0:
            source_expression = source_expression**exponent
        else:
            source_expression = None
        return self._with_source_expression(
            self._backend() ** exponent,
            source_expression,
        )

    def _exact_source_equality_status(self, other):
        left_source = self.exact_source_expression()
        right_source = other.exact_source_expression()
        if left_source is None or right_source is None:
            return None
        difference = left_source - right_source
        if difference == self.parent().completion_source().zero():
            return True
        try:
            kernel = self.parent().completion_map_kernel()
        except NotImplementedError:
            return None
        return bool(kernel.contains_ambient_element(difference))

    @staticmethod
    def _backend_exact_zero_status(difference):
        r"""Return ``True``/``False`` when the backend decides exact zero.

        ``None`` means that the selected finite information agrees with zero
        but does not decide exact zero in the completion.
        """
        exact_zero = getattr(difference, "_is_exact_zero", None)
        if callable(exact_zero) and bool(exact_zero()):
            return True
        inexact_zero = getattr(difference, "_is_inexact_zero", None)
        if callable(inexact_zero) and bool(inexact_zero()):
            return None

        precision = getattr(difference, "precision_absolute", None)
        if callable(precision):
            if bool(difference):
                return False
            return True if precision() is Infinity else None

        return None

    def _completion_equal(self, other) -> bool:
        parent = self.parent()
        try:
            other = parent(other)
        except (TypeError, ValueError):
            return False
        if self is other:
            return True
        left = self._backend()
        right = other._backend()
        source_status = self._exact_source_equality_status(other)
        if source_status is not None:
            return source_status
        mode = parent.completion_arithmetic_mode()
        if mode == "exact_backend":
            return bool(left == right)
        if mode == "exact_lazy":
            options = getattr(left.parent(), "options", None)
            old_secure = None
            if options is not None:
                old_secure = options["secure"]
                options["secure"] = True
            try:
                try:
                    return bool(left == right)
                except ValueError as error:
                    raise AssertionError(
                        "exact equality of these lazy completion elements is undecidable by the selected engine"
                    ) from error
            finally:
                if options is not None:
                    options["secure"] = old_secure
        difference = left - right
        status = self._backend_exact_zero_status(difference)
        if status is True:
            return True
        if status is False:
            return False
        if mode == "finite_approximation" and difference != left.parent().zero():
            return False
        raise AssertionError(
            "finite completion data agree at the selected precision but do not decide exact equality"
        )

    def __eq__(self, other):
        return self._completion_equal(other)

    def __ne__(self, other):
        return not self._completion_equal(other)

    __hash__ = None

    def __bool__(self):
        return not self._completion_equal(self.parent().zero())

    def is_zero(self):
        return self._completion_equal(self.parent().zero())

    def is_one(self):
        return self._completion_equal(self.parent().one())

    def is_unit(self):
        return bool(self._backend().is_unit())

    def inverse_of_unit(self):
        if not self.is_unit():
            raise ZeroDivisionError(f"{self} is not a unit")
        return _owned_engine_element(self.parent(), self._backend() ** -1)

    def precision_absolute(self):
        r"""Return the selected absolute computation precision when represented."""
        precision = getattr(self._backend(), "precision_absolute", None)
        if callable(precision):
            return precision()
        return self.parent().computation_precision()

    def refine_precision(self, precision):
        r"""Refine an exact source image without inventing missing coefficients."""
        source_expression = self.exact_source_expression()
        if source_expression is None:
            raise AssertionError(
                "precision refinement requires an exact retained source expression"
            )
        refined = self.parent().completion_source().adic_completion(
            self.parent().ideal_of_definition(), precision=int(precision)
        )
        return refined.completion_map()(source_expression)


class _AdicCompletionAlgebraParent(_OwnedAlgebraParent):
    r"""An engine-backed adic completion with its defining data fixed at construction."""

    Element = _AdicCompletionElement

    def __init__(
        self,
        engine,
        source,
        defining_ideal,
        precision,
        *,
        engine_map=None,
        completed_ideal_generators=None,
        projection_lift=None,
        arithmetic_mode="finite_precision",
        completion_image=None,
        completion_map_kernel=None,
        algebra_base=None,
        algebra_labels=None,
        formal_parameter_labels=None,
        extra_categories=(),
    ) -> None:
        selected_engine_map = engine_map
        if completion_image is None:
            source_engine = _engine_ring(source)
            if selected_engine_map is None:
                selected_engine_map = engine.coerce_map_from(source_engine)

            def completion_image(element):
                source_value = _engine_element(source, source(element))
                value = (
                    selected_engine_map(source_value)
                    if selected_engine_map is not None
                    else engine(source_value)
                )
                return engine(value)

        def completion_map_factory():
            def completion_map_image(element):
                selected = source(element)
                return self._completion_element(
                    completion_image(selected),
                    source_expression=selected,
                )

            return _ring_morphism_with_engine(
                source, self, completion_map_image, selected_engine_map
            )

        self._adic_completion_source = source
        self._adic_defining_ideal = defining_ideal
        self._adic_completion_precision = int(precision)
        self._adic_projection_lift = projection_lift
        self._adic_arithmetic_mode = arithmetic_mode
        self._adic_completion_map_kernel = completion_map_kernel
        self._adic_completion_map_factory = completion_map_factory
        self._realized_completion_map = None
        match formal_parameter_labels:
            case None:
                self._preamble_formal_parameter_labels = None
            case _:
                self._preamble_formal_parameter_labels = finite_ordered_set(
                    formal_parameter_labels
                )
        placements = [AdicCompletions(), *extra_categories]
        if source in OwnedRings().Noetherian():
            placements.append(OwnedRings().Noetherian())
        formal_base = algebra_base
        match formal_base:
            case None:
                formal_base_is_local = False
                formal_base_is_complete_local = False
            case _:
                formal_base = _own_ring(formal_base)
                formal_base_is_local = (
                    formal_parameter_labels is not None
                    and formal_base in OwnedRings().Commutative().Local()
                )
                formal_base_is_complete_local = (
                    formal_parameter_labels is not None
                    and formal_base in OwnedRings().Commutative().Local().Complete()
                )

        # A formal-power-series specialization knows the quotient by its
        # represented ideal of variables exactly: R[x_1,...,x_n]/(x_1,...,x_n)
        # is R.  Thus that ideal is maximal when the coefficient ring is a
        # field, without asking a backend ideal predicate that may not decide
        # maximality over a general base such as ZZ.  For arbitrary adic
        # completions, preserve an unavailable maximality algorithm as
        # undecided; absence of an algorithm is not evidence that the ideal is
        # nonmaximal.
        if formal_parameter_labels is not None and formal_base is not None:
            defining_ideal_is_maximal = (
                True if formal_base in OwnedRings().Division().Commutative() else None
            )
        else:
            try:
                defining_ideal_is_maximal = bool(defining_ideal.is_maximal())
            except NotImplementedError:
                defining_ideal_is_maximal = None

        match (
            defining_ideal_is_maximal,
            formal_base_is_complete_local,
            formal_base_is_local,
        ):
            case (True, _, _) | (_, True, _):
                placements.append(OwnedRings().Commutative().Local().Complete())
            case (_, _, True):
                placements.append(OwnedRings().Commutative().Local())
            case _:
                pass
        _OwnedAlgebraParent.__init__(
            self,
            engine,
            source if algebra_base is None else algebra_base,
            algebra_labels,
            categories=tuple(placements),
        )
        completion_map = self.completion_map()
        match (formal_base_is_local, defining_ideal_is_maximal):
            case (True, _):
                formal_parameters = tuple(
                    completion_map(
                        source.algebra_generator(label)
                    )
                    for label in self._preamble_formal_parameter_labels
                )
                maximal_ideal = _maximal_ideal_over_local_base(
                    self,
                    formal_base,
                    formal_parameters,
                )
                residue = formal_base.residue_field()
                _install_local_ring_construction(self, maximal_ideal, residue)
            case (_, True):
                maximal_ideal = completion_map.extension_of_ideal(defining_ideal)
                residue = source.residue_field_at(defining_ideal)
                _install_local_ring_construction(self, maximal_ideal, residue)
            case _:
                pass

    def completion_arithmetic_mode(self):
        return self._adic_arithmetic_mode

    def _completion_element(self, value, *, source_expression=None):
        if getattr(value, "parent", lambda: None)() is not self._engine:
            value = self._engine(value)
        return self.element_class(
            self,
            value,
            exact_source_expression=source_expression,
        )

    def _element_constructor_(self, value):
        if getattr(value, "parent", lambda: None)() is self:
            return value
        completion_map = self._realized_completion_map
        if completion_map is None:
            return super()._element_constructor_(value)
        source = self.completion_source()
        try:
            selected = source(value)
        except (TypeError, ValueError, AttributeError):
            return super()._element_constructor_(value)
        return completion_map(selected)

    def zero(self):
        completion_map = self._realized_completion_map
        if completion_map is None:
            return super().zero()
        return completion_map(self.completion_source().zero())

    def one(self):
        completion_map = self._realized_completion_map
        if completion_map is None:
            return super().one()
        return completion_map(self.completion_source().one())


class GeneratedIdealView(SageObject):
    r"""An ideal remembered by its ambient ring and chosen generators."""

    def __init__(self, ring, generators, source_ideal=None) -> None:
        self._ring = ring
        self._generators = tuple(generators)
        self._source_ideal = source_ideal

    def ring(self):
        return self._ring

    def ideal_generators(self):
        return self._generators

    def source_ideal(self):
        return self._source_ideal

    def __eq__(self, other) -> bool:
        if self is other:
            return True
        if not isinstance(other, GeneratedIdealView) or other.ring() is not self.ring():
            return False
        if self.source_ideal() is not None and other.source_ideal() is not None:
            source = getattr(self.ring(), "localization_source", lambda: None)()
            if source is not None:
                return bool(
                    _engine_ideal(source, self.source_ideal())
                    == _engine_ideal(source, other.source_ideal())
                )
            return bool(self.source_ideal() == other.source_ideal())
        return self.ideal_generators() == other.ideal_generators()

    def __ne__(self, other) -> bool:
        return not self == other

    def _repr_(self):
        return f"Ideal ({', '.join(map(str, self.ideal_generators()))}) of {self.ring()}"


def _maximal_ideal_over_local_base(algebra, base, uniformizers):
    r"""Return the maximal ideal ``m A + (t_1, ..., t_n)`` of a local-base construction.

    Let ``(R, m)`` be local and let ``A`` be ``R[[t_1, ..., t_n]]`` or
    ``R[e]/(e^2)``.  An element of ``A`` is a unit exactly when its constant
    term is a unit of ``R``, hence exactly when that constant term lies outside
    ``m``.  So the non-units of ``A`` are the elements whose constant term lies
    in ``m``, and that set is the ideal generated by the image of ``m``
    together with the new variables.  Either part alone understates it: over a
    field ``m`` is zero and only the variables remain, while over ``Z_(p)`` the
    scalar ``p`` is a non-unit of ``A`` as well.

    The residue field is unchanged by the extra generators, because
    ``A/(m A + (t)) = R/m``.
    """

    engine = _engine_ring(algebra)
    base_maximal = tuple(
        _owned_engine_element(algebra, engine(_engine_element(base, generator)))
        for generator in base.maximal_ideal().ideal_generators()
    )
    return GeneratedIdealView(
        algebra,
        tuple(generator for generator in (*base_maximal, *uniformizers) if not generator.is_zero()),
    )


@cached_function
def _quotient_ring(source, defining_ideal):
    r"""Return the one ``R/I`` for this ring and this ideal.

    ``R/I`` is determined by ``R`` and ``I``, so it is interned on them.  The
    key is the ideal itself rather than a generating set, and ideals decide
    their own equality, so ``(2)`` and ``(2,4)`` reach the same quotient of the
    integers.

    A prime localization is realized by a fraction field, where every nonzero
    ideal is the unit ideal, so a quotient read from that realization would be
    the zero ring however small ``I`` is.  ``R_p/I R_p`` is therefore left to
    the represented classes, whose equality is the owned membership
    ``a - b in I R_p`` and is exact.
    """
    if source in PrimeLocalizations():
        quotient_engine = None
    else:
        engine = _engine_ring(source)
        defining = _engine_ideal(source, defining_ideal)
        try:
            lifted = _engine_quotient_cover_ideal(source, defining)
            quotient_engine = lifted.ring().quotient(lifted)
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            try:
                quotient_engine = engine.quotient(defining)
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                quotient_engine = None

    dimension = None
    if quotient_engine is not None and source in OwnedRings().Noetherian():
        try:
            dimension = _engine_krull_dimension(quotient_engine)
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass

    quotient_is_field = False
    quotient_is_domain = False
    try:
        quotient_is_field = bool(defining_ideal.is_maximal())
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        pass
    if quotient_engine is not None:
        try:
            quotient_is_field = bool(quotient_engine.is_field())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        try:
            quotient_is_domain = bool(quotient_engine.is_integral_domain())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
        if quotient_is_domain and dimension == 0:
            quotient_is_field = True
    placements = []
    if source in OwnedRings().Noetherian():
        placements.append(OwnedRings().Noetherian())
    if quotient_is_field:
        placements.append(OwnedRings().Division().Commutative())
    elif quotient_is_domain:
        placements.append(OwnedRings().Commutative().NoZeroDivisors())
    if quotient_engine is not None:
        try:
            if bool(quotient_engine.is_finite()):
                placements.append(FiniteSets())
        except (AttributeError, NotImplementedError, TypeError, ValueError):
            pass
    if dimension == 0:
        placements.append(OwnedRings().Artinian())

    return _object_of(
        Category.join((QuotientRings(), Algebras(source).Associative().Unital().Commutative(), *placements)),
        source=source,
        defining_ideal=defining_ideal,
        _engine_ring=quotient_engine,
    )


def _localization_descent(source, elements):
    r"""Return the ring under a tower of localizations and these elements there.

    ``a/s`` is a unit exactly when ``a`` is, ``s`` being one already, so
    inverting ``a/s`` over the tower is inverting the numerator over the ring
    at its bottom.  The descent stops at a localization that inverts a set with
    no chosen finite generating set, such as the complement of a prime.
    """
    while source in LocalizationRings() and source not in PrimeLocalizations():
        elements = tuple(
            source.localization_fraction_data(element)[0] for element in elements
        )
        source = source.localization_source()
    return source, elements


def _one_step_inverted_family(source, generators):
    r"""Return the ring and the family that invert in one step what this does.

    Localizing ``S^{-1}A`` at ``g = a/s`` inverts ``S`` together with ``a``:
    ``s`` is a unit already, so ``a/s`` is a unit exactly when ``a`` is.  Then
    ``(S^{-1}A)[1/g]`` and ``(S union {a})^{-1}A`` invert the same subset of
    ``A``, each factors uniquely through the other by the universal property,
    and the canonical isomorphism between them identifies the two.

    Sage localizes ``A`` at a family and refuses to localize ``A[1/x]`` at
    anything, so the one-step family over the bottom ring is the presentation
    a realization can hold.  The owned source and map are unaffected: they
    record the ring that was localized, not the ring underneath.

    The descent stops at a localization that inverts a set with no chosen
    finite generating set, such as the complement of a prime, which no family
    presents.
    """
    inverted = tuple(generators)
    while source in LocalizationRings() and source not in PrimeLocalizations():
        inverted = tuple(
            source.localization_fraction_data(element)[0] for element in inverted
        ) + tuple(source.inverted_elements())
        source = source.localization_source()
    return source, inverted


def _generated_submonoid_contains_zero_in_domain(source, submonoid):
    r"""Decide whether a generated multiplicative submonoid contains zero in a domain.

    In an integral domain a finite product is zero exactly when one factor is
    zero.  Thus a submonoid given by generators contains zero exactly when one
    chosen generator is zero.  Predicate-defined submonoids keep their own
    membership decision, and an unrepresented case remains unknown.
    """
    try:
        return source.zero() in submonoid
    except NotImplementedError:
        try:
            generators = tuple(submonoid.monoid_generators())
        except NotImplementedError:
            return None
        return any(generator == source.zero() for generator in generators)


def _localization_size_placements(source, submonoid):
    r"""Return exact cardinality placements inherited by ``S^-1 R``.

    A localization of a finite ring is finite.  For an infinite domain with
    ``0 not in S``, the canonical map is injective, while every fraction is a
    pair from ``R x S``; hence the localization has exactly the cardinality of
    ``R``.
    """
    if source in FiniteSets():
        return (FiniteSets(),)
    if source not in OwnedRings().Commutative().NoZeroDivisors():
        return ()
    contains_zero = _generated_submonoid_contains_zero_in_domain(source, submonoid)
    if contains_zero is not False:
        return ()
    if source in CountablyInfiniteSets():
        return (CountablyInfiniteSets(),)
    if source in UncountableSets():
        return (UncountableSets(),)
    return ()


def _flattened_symmetric_localization_engine(source, inverted):
    r"""Realize a localization of ``Sym_C(M)`` when ``C`` is itself localized.

    For a finitely generated localization ``C = S^{-1}A`` and a finite
    polynomial algebra ``C[x_1,...,x_n]``, localizing at finitely many
    polynomials is canonically the corresponding localization of
    ``A[x_1,...,x_n]`` after adjoining the already inverted elements of ``S``.
    Sage's nested polynomial localization currently misidentifies such
    polynomials as units; its flattened multivariate polynomial ring has the
    maintained localization implementation and represents the same ring.

    The returned decoder is private representation correspondence from a
    numerator/denominator in that flattened engine back to the owned source
    polynomial algebra.  Public localization data remain ``source`` and its
    selected submonoid.
    """

    coefficient_ring = source.base_ring()
    if (
        source not in SymmetricAlgebras(coefficient_ring)
        or coefficient_ring not in LocalizationRings()
        or coefficient_ring in PrimeLocalizations()
    ):
        return None, None
    try:
        coefficient_inverted = tuple(coefficient_ring.inverted_elements())
    except NotImplementedError:
        return None, None
    coefficient_bottom, coefficient_family = _one_step_inverted_family(
        coefficient_ring,
        coefficient_inverted,
    )
    source_engine = _engine_ring(source)
    coefficient_engine = _engine_ring(coefficient_ring)
    coefficient_bottom_engine = _engine_ring(coefficient_bottom)
    try:
        names = tuple(source_engine.variable_names())
        polynomial_bottom = _SagePolynomialRing(
            coefficient_bottom_engine,
            names=names,
        )
    except (AttributeError, TypeError, ValueError):
        return None, None

    flattening = getattr(polynomial_bottom, "flattening_morphism", None)
    if callable(flattening):
        flattening = flattening()
        engine_bottom = flattening.codomain()
        unflatten = flattening.section()
        to_engine_bottom = flattening
    else:
        engine_bottom = polynomial_bottom

        def unflatten(element):
            return polynomial_bottom(element)

        def to_engine_bottom(element):
            return engine_bottom(element)

    variables = tuple(polynomial_bottom.gens())

    def powers_of(exponent):
        if len(variables) == 1 and not isinstance(exponent, tuple):
            try:
                return (int(exponent),)
            except TypeError:
                pass
        return tuple(int(power) for power in exponent)

    def cleared_polynomial(element):
        represented = source_engine(_engine_element(source, element))
        coefficients = represented.dict()
        common_denominator = coefficient_bottom_engine.one()
        for coefficient in coefficients.values():
            common_denominator *= coefficient_bottom_engine(
                coefficient.denominator()
            )
        cleared = source_engine(coefficient_engine(common_denominator)) * represented
        result = polynomial_bottom.zero()
        for exponent, coefficient in cleared.dict().items():
            if coefficient.denominator() != coefficient_bottom_engine.one():
                raise ArithmeticError(
                    "clearing localized polynomial coefficients left a denominator"
                )
            term = polynomial_bottom(
                coefficient_bottom_engine(coefficient.numerator())
            )
            for variable, power in zip(variables, powers_of(exponent), strict=True):
                if power:
                    term *= variable**power
            result += term
        return to_engine_bottom(result)

    engine_inverted = [
        to_engine_bottom(
            polynomial_bottom(_engine_element(coefficient_bottom, element))
        )
        for element in coefficient_family
    ]
    engine_inverted.extend(cleared_polynomial(element) for element in inverted)
    try:
        localization_engine = engine_bottom.localization(tuple(engine_inverted))
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        return None, None

    def decode(element):
        nested = unflatten(engine_bottom(element))
        return _owned_engine_element(source, source_engine(nested))

    return localization_engine, decode


def _finite_generated_localization(source, submonoid):
    try:
        generators = tuple(submonoid.monoid_generators())
    except NotImplementedError as error:
        raise AssertionError(
            "the active Sage localization engine requires a chosen finite generating set"
        ) from error
    if not generators:
        return source
    bottom, inverted = _one_step_inverted_family(source, generators)
    values = tuple(_engine_element(bottom, value) for value in inverted)
    engine_bottom = _engine_ring(bottom)
    engine_source_decoder = None
    try:
        localization_engine = engine_bottom.localization(values)
    except (AttributeError, NotImplementedError, TypeError, ValueError):
        localization_engine, engine_source_decoder = _flattened_symmetric_localization_engine(
            bottom,
            inverted,
        )
        # Sage does not localize a generic quotient ring directly, even when
        # the quotient is a domain.  Present the same ring by adjoining an
        # inverse variable for each selected denominator:
        #
        #   (P/I)[f_1^-1,...,f_r^-1]
        #       = P[u_1,...,u_r]/(I, u_1 f_1-1, ..., u_r f_r-1).
        #
        # Unlike a quotient of Sage's localization parent, this ordinary
        # polynomial quotient supports exact quotient maps and unit inversion,
        # which are the private operations affine ``Spec`` needs.
        if localization_engine is None:
            try:
                cover = engine_bottom.cover_ring()
                defining = engine_bottom.defining_ideal()
                cover_names = tuple(cover.variable_names())
                occupied = set(cover_names)
                inverse_names = []
                for position in range(len(values)):
                    candidate = f"localization_inverse_{position}"
                    while candidate in occupied:
                        candidate = "localization_" + candidate
                    occupied.add(candidate)
                    inverse_names.append(candidate)
                extended_cover = _SagePolynomialRing(
                    cover.base_ring(),
                    names=(*cover_names, *inverse_names),
                )
                inverse_variables = tuple(
                    extended_cover.gen(len(cover_names) + position)
                    for position in range(len(values))
                )
                relations = tuple(
                    extended_cover(generator) for generator in defining.gens()
                ) + tuple(
                    inverse * extended_cover(value.lift()) - extended_cover.one()
                    for inverse, value in zip(inverse_variables, values, strict=True)
                )
                localization_engine = extended_cover.quotient(
                    extended_cover.ideal(relations)
                )
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                pass
        if localization_engine is None:
            # Localizing at units changes no ring.  Some Sage polynomial-ring
            # engines refuse the syntactic localization at ``1``; in that case
            # the source engine itself is the exact realization of the selected
            # localization.
            try:
                all_units = all(value.is_unit() for value in values)
            except (AttributeError, NotImplementedError, TypeError, ValueError):
                all_units = False
            localization_engine = engine_bottom if all_units else None
    placements = list(_localization_size_placements(source, submonoid))
    if source in OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals():
        placements.append(OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals())
    else:
        if source in OwnedRings().Commutative().NoZeroDivisors():
            placements.append(OwnedRings().Commutative().NoZeroDivisors())
        if source in OwnedRings().Noetherian():
            placements.append(OwnedRings().Noetherian())
    base = source.base_ring()
    algebra_source = (
        source
        if base is not None and source in Algebras(base).Associative().Unital()
        else None
    )
    algebra_categories = []
    if algebra_source is not None:
        algebra_base = algebra_source.base_ring()
        algebra_categories = [Algebras(algebra_base).Associative().Unital()]
        if algebra_source in Algebras(algebra_base).Associative().Unital().Commutative():
            algebra_categories.append(Algebras(algebra_base).Associative().Unital().Commutative())
    return _object_of(
        Category.join((LocalizationRings(), *placements, *algebra_categories)),
        source=source,
        submonoid=submonoid,
        _engine_ring=localization_engine,
        _engine_source_decoder=engine_source_decoder,
        _engine_units_exact=localization_engine is not None,
        algebra_source=algebra_source,
    )


@cached_function
def _nonzero_element_submonoid(source):
    r"""Return the represented multiplicative submonoid ``R - {0}`` of a domain."""
    if source not in OwnedRings().Commutative().NoZeroDivisors():
        raise ValueError("the nonzero elements form this localization submonoid only for a domain")
    return source.predicate_submonoid(
        lambda element: element != source.zero(),
        f"Nonzero multiplicative elements of {source}",
        structure_data={"kind": "nonzero_elements"},
    )


def _fraction_field_localization(source, submonoid):
    r"""Realize ``(R-{0})^-1 R`` while retaining the represented localization datum."""
    if source not in OwnedRings().Commutative().NoZeroDivisors():
        raise ValueError("fraction-field localization requires an integral domain")
    if submonoid._structure_data().get("kind") != "nonzero_elements":
        raise ValueError("fraction-field localization requires the nonzero-element submonoid")
    if source in OwnedRings().Division().Commutative():
        return source

    engine = _engine_ring(source)
    assert engine is not source, (
        f"{source} has no selected computation realization for its fraction field"
    )
    if source in QuotientRings():
        # Sage's IntegralDomains.ParentMethods.fraction_field is precisely
        # FractionField_generic(self).  A represented quotient carries the
        # domain theorem in its owned construction, while its private Sage
        # realization remains in Sage's quotient-ring category.  Use that
        # maintained constructor directly instead of mutating the realization
        # merely to make the category method appear.
        fraction_engine = SageFractionField(engine)
    else:
        fraction_engine = engine.fraction_field()
    field = _own_ring(fraction_engine)
    placements = [OwnedRings().Commutative().NoZeroDivisors(), OwnedRings().Division().Commutative()]
    if source in OwnedRings().Noetherian():
        placements.append(OwnedRings().Noetherian())
    return _object_of(
        Category.join((LocalizationRings(), *placements)),
        source=source,
        submonoid=submonoid,
        _engine_ring=fraction_engine,
        fraction_field_realization=field,
    )


def _localization(source, *datum):
    r"""Return ``S^{-1}R`` from a submonoid ``S -> (R,*)``.

    Passing ring elements is convenience syntax for the submonoid they generate.
    The mathematical localization datum stored on the result is always the
    represented subobject ``S -> (R,*)``.
    """
    if len(datum) == 1 and datum[0] in Monoids().Subobjects(source):
        return _localization_at_submonoid(source, datum[0])
    return _localization_at_elements(
        source,
        tuple(source(element) for element in datum),
    )


@cached_function
def _localization_at_elements(source, elements):
    r"""Return the one ``S^{-1}R`` for the submonoid these elements generate.

    The interning is keyed here rather than on the submonoid, because the
    submonoid is built from the elements and is a fresh subobject on every
    call.  So the key is the chosen generating family, and two families that
    generate one submonoid stay two objects: ``<2>`` and ``<2,4>`` are the same
    submonoid of ``(Z,*)`` and give the same ring, but deciding that two
    finitely generated submonoids of a commutative monoid coincide is not
    something the preamble can do, and it is not claimed here.
    """
    return _localization_at_submonoid(
        source,
        source.generated_submonoid(
            elements,
            description=f"Submonoid generated by {elements!r} in {source}",
            structure_data={"kind": "finitely_generated"},
        ),
    )


@cached_function
def _localization_at_submonoid(source, submonoid):
    r"""Return the one ``S^{-1}R`` for this ring and this represented submonoid."""
    structure = submonoid._structure_data()
    if structure.get("kind") == "prime_complement":
        return _PrimeLocalizationFromSubmonoid(source, submonoid)
    if structure.get("kind") == "nonzero_elements":
        return _fraction_field_localization(source, submonoid)
    return _finite_generated_localization(source, submonoid)


def _quotient_representative(element):
    lift = getattr(element, "lift", None)
    assert lift is not None, (
        "a represented quotient element used in quotient/localization comparison must carry its canonical lift"
    )
    return lift()


def _localization_element_from_source_fraction(localization_ring, numerator, denominator):
    fraction = getattr(localization_ring, "fraction", None)
    if fraction is not None:
        return fraction(numerator, denominator)
    numerator_image = localization_ring.localization_map()(numerator)
    denominator_image = localization_ring.localization_map()(denominator)
    return localization_ring(numerator_image / denominator_image)


def _quotient_localization_comparison(source_quotient, localization_ring):
    r"""Return the canonical isomorphism

    ``S^{-1}(R/I) -> S^{-1}R/S^{-1}I``.

    Localizing ``R/I`` means inverting the image of ``S``.  Where ``S`` is
    given by a chosen finite generating set that image is the submonoid the
    images of those generators generate.  Where ``S`` is the complement of a
    prime ``p`` containing ``I``, the image is the complement of the prime
    ``p/I``, so the left side is the prime localization ``(R/I)_{p/I}`` and the
    comparison is the local ring of a point of the closed subscheme ``V(I)``
    read either way round.
    """
    if source_quotient not in QuotientRings():
        raise TypeError("quotient/localization compatibility starts from a represented quotient ring")
    source_ring = source_quotient.quotient_source()
    if localization_ring not in LocalizationRings():
        raise TypeError("the comparison requires a represented localization of the quotient source")
    if localization_ring.localization_source() is not source_ring:
        raise ValueError("the localization has the wrong source ring")

    source_submonoid = localization_ring.localization_submonoid()
    quotient_map = source_quotient.quotient_map()
    defining_ideal = source_quotient.defining_ideal()

    if localization_ring in PrimeLocalizations():
        prime = localization_ring.localized_prime()
        assert all(
            prime.contains_ambient_element(generator)
            for generator in defining_ideal.ideal_generators()
        ), (
            f"the image of the complement of {prime} in {source_quotient} is the complement "
            f"of a prime only when {defining_ideal} lies inside {prime}; otherwise that "
            "image contains zero and both sides of the comparison are the zero ring, which "
            "is not constructed here"
        )
        localized_quotient = source_quotient.localize_at_prime(
            quotient_map.extension_of_ideal(prime)
        )
    else:
        try:
            source_generators = tuple(source_submonoid.monoid_generators())
        except NotImplementedError as error:
            raise AssertionError(
                "the quotient/localization comparison reads the image of S from a chosen "
                "finite generating set, or from the prime whose complement S is"
            ) from error

        quotient_submonoid = source_quotient.generated_submonoid(
            tuple(quotient_map(generator) for generator in source_generators),
            description=f"Image of {source_submonoid} in {source_quotient}",
            structure_data={"kind": "quotient_image"},
        )
        localized_quotient = source_quotient.localization(quotient_submonoid)

    extended_ideal = defining_ideal.extension_to_localization(localization_ring)
    quotient_after_localization = localization_ring.quotient_ring(extended_ideal)

    right_quotient_map = quotient_after_localization.quotient_map()

    def forward_image(element):
        numerator, denominator = localized_quotient.localization_fraction_data(element)
        numerator_lift = source_ring(_quotient_representative(numerator))
        denominator_lift = source_ring(_quotient_representative(denominator))
        localized = _localization_element_from_source_fraction(
            localization_ring,
            numerator_lift,
            denominator_lift,
        )
        return right_quotient_map(localized)


    forward = localized_quotient.Mor(quotient_after_localization)(
        forward_image,
    )

    def inverse_image(element):
        representative = _quotient_representative(element)
        numerator, denominator = localization_ring.localization_fraction_data(representative)
        return localized_quotient.fraction(
            quotient_map(numerator),
            quotient_map(denominator),
        )

    inverse = quotient_after_localization.Mor(localized_quotient)(
        inverse_image,
    )
    return QuotientLocalizationComparison(
        source_quotient,
        localization_ring,
        localized_quotient,
        quotient_after_localization,
        forward,
        inverse,
        extended_ideal,
    )


def _quotient_completion_comparison(source_quotient, source_ideal, *, precision=20):
    r"""Return the canonical Noetherian comparison ``(R/J)^ ~= R^/J R^``.

    The topology on ``R/J`` is defined by the image of ``source_ideal``.  The
    two arrows are assembled from the quotient and completion maps.  Their
    mathematical existence is the finite-module completion theorem over a
    Noetherian ring; evaluation away from exact retained source expressions
    stays at the ordinary completion computational frontier.
    """
    if source_quotient not in QuotientRings():
        raise TypeError("quotient/completion compatibility starts from a represented quotient ring")
    source = source_quotient.quotient_source()
    if source not in OwnedRings().Noetherian():
        raise TypeError("the represented quotient/completion comparison requires a Noetherian source")
    source_ideal = _owned_ideal(source, source_ideal)
    quotient_map = source_quotient.quotient_map()
    quotient_ideal = quotient_map.extension_of_ideal(source_ideal)

    source_completion = source.adic_completion(source_ideal, precision=precision)
    completed_quotient = source_quotient.adic_completion(
        quotient_ideal,
        precision=precision,
    )
    extended_defining_ideal = source_completion.completion_map().extension_of_ideal(
        source_quotient.defining_ideal()
    )
    quotient_after_completion = source_completion.quotient_ring(
        extended_defining_ideal
    )
    right_quotient_map = quotient_after_completion.quotient_map()

    def quotient_source_to_right(element):
        representative = _quotient_representative(source_quotient(element))
        return right_quotient_map(
            source_completion.completion_map()(representative)
        )

    source_to_right = source_quotient.Mor(quotient_after_completion)(
        quotient_source_to_right,
    )

    def forward_image(element):
        selected = completed_quotient(element)
        source_expression = selected.exact_source_expression()
        if source_expression is None:
            raise AssertionError(
                "quotient/completion comparison evaluation requires an exact retained source expression"
            )
        return source_to_right(source_expression)

    forward = completed_quotient.Mor(quotient_after_completion)(
        forward_image,
    )

    completion_to_completed_quotient = source_completion.induced_map(
        quotient_map,
        completed_quotient,
    )
    for generator in extended_defining_ideal.ideal_generators():
        if completion_to_completed_quotient(generator) != completed_quotient.zero():
            raise ArithmeticError(
                "the completed quotient map does not kill the extended defining ideal"
            )

    def inverse_image(element):
        representative = _quotient_representative(
            quotient_after_completion(element)
        )
        return completion_to_completed_quotient(representative)

    inverse = quotient_after_completion.Mor(completed_quotient)(
        inverse_image,
    )
    return QuotientCompletionComparison(
        source_quotient,
        source_ideal,
        source_completion,
        completed_quotient,
        quotient_after_completion,
        extended_defining_ideal,
        forward,
        inverse,
    )


def _residue_field_at(source, ideal):
    r"""Return ``R/m`` for a represented maximal ideal ``m`` of ``R``."""
    defining = _owned_ideal(source, ideal)
    if not bool(defining.is_maximal()):
        raise ValueError("a residue field is the quotient by a maximal ideal")
    quotient = source.quotient_ring(defining)
    if quotient not in OwnedRings().Division().Commutative():
        raise ArithmeticError("the quotient by a maximal ideal was not returned as a field")
    return quotient


def _PrimeLocalizationFromSubmonoid(source, submonoid):
    r"""Return ``R_p`` for a submonoid represented as the complement of ``p``.

    ``R -> R_p`` is injective exactly when ``R`` is a domain, and then ``R_p``
    is the subring of ``Frac(R)`` whose denominators avoid ``p``, which is the
    realization selected below.  A reducible or nonreduced ``R`` has no
    fraction field to sit in, so it selects none: the represented fractions are
    the object, and every question about them -- which are units, when two are
    equal, which lie in an ideal -- is an ideal computation in ``R`` against
    ``p`` rather than a question put to a realization.
    """
    structure = submonoid._structure_data()
    prime_ideal = structure.get("prime_ideal")
    if prime_ideal is None:
        raise ValueError("prime-complement localization requires its represented prime ideal")
    placements = list(_localization_size_placements(source, submonoid))
    if source in OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals():
        placements.append(OwnedRings().Commutative().NoZeroDivisors().PrincipalIdeals())
    else:
        if source in OwnedRings().Noetherian():
            placements.append(OwnedRings().Noetherian())
        if source in OwnedRings().Commutative().NoZeroDivisors():
            placements.append(OwnedRings().Commutative().NoZeroDivisors())
    if source in OwnedRings().Commutative().NoZeroDivisors():
        fraction_field = source.fraction_field()
        fraction_engine = _engine_ring(fraction_field)
    else:
        fraction_field = None
        fraction_engine = None
    base = source.base_ring()
    algebra_source = (
        source
        if base is not None and source in Algebras(base).Associative().Unital()
        else None
    )
    if algebra_source is not None:
        placements.append(Algebras(base).Associative().Unital())
        if source in Algebras(base).Associative().Unital().Commutative():
            placements.append(Algebras(base).Associative().Unital().Commutative())
    return _object_of(
        Category.join([PrimeLocalizations(), *placements]),
        source=source,
        submonoid=submonoid,
        fraction_field=fraction_field,
        engine_ring=fraction_engine,
    )


def _prime_localization_from_input(source, prime):
    r"""Return ``R_p`` using the submonoid ``R \ p -> (R,*)``."""
    if source not in OwnedRings().Commutative():
        raise TypeError("prime localization requires a commutative source ring")
    prime_ideal = _owned_ideal(source, prime)
    if not prime_ideal.is_prime():
        raise ValueError("R_p requires a prime ideal p")
    return _prime_localization(source, prime_ideal)


@cached_function
def _prime_localization(source, prime_ideal):
    r"""Return the one ``R_p`` for this ring and this prime.

    The complement of a prime is a predicate submonoid, freshly built on each
    call and never recognizable as a copy of itself, so the interning is keyed
    on the prime instead.  That key is exact, because the prime is an ideal and
    ideals decide their own equality.
    """
    prime_engine = _engine_ideal(source, prime_ideal)
    complement = source.predicate_submonoid(
        lambda element: _engine_ring_value(source, element) not in prime_engine,
        f"{source} \\ {prime_ideal}",
        structure_data={"kind": "prime_complement", "prime_ideal": prime_ideal},
    )
    return _localization_at_submonoid(source, complement)


@cached_function
def _adic_completion_from_owned_data(source, defining, precision):
    r"""Private implementation of the represented adic completion ``R^``.

    ``source`` and ``defining`` are already owned and normalized by
    :class:`AdicCompletions`.  This is the sole implementation factory for the
    family; public notation is defined below and delegates back to the category
    constructor.
    """
    if source in PrimeLocalizations() and defining == source.maximal_ideal():
        bottom = source.localization_source()
        prime = source.localized_prime()
        bottom_completion = AdicCompletions()(
            bottom,
            prime,
            precision=precision,
        )
        local_to_completion = source.induced_morphism(
            bottom_completion.completion_map()
        )
        completion_engine = _engine_ring(bottom_completion)
        bottom_projection_lift = bottom_completion._completion_projection_lift()
        assert bottom_projection_lift is not None, (
            "the selected source completion must carry a maintained finite-stage lift"
        )

        def completion_image(element):
            return _engine_element(
                bottom_completion,
                local_to_completion(source(element)),
            )

        def projection_lift(value, exponent):
            return source.localization_map()(
                bottom_projection_lift(value, exponent)
            )

        completed_ideal_generators = tuple(
            completion_image(generator)
            for generator in defining.ideal_generators()
        )
        return _AdicCompletionAlgebraParent(
            completion_engine,
            source,
            defining,
            precision,
            completed_ideal_generators=completed_ideal_generators,
            projection_lift=projection_lift,
            arithmetic_mode=bottom_completion.completion_arithmetic_mode(),
            completion_image=completion_image,
            completion_map_kernel=source.ideal(source.zero()),
        )
    defining_engine = _engine_ideal(source, defining)
    generators = tuple(defining_engine.gens())
    engine = _engine_ring(source)
    zero_ideal = source.ideal(source.zero())
    unit_ideal = source.ideal(source.one())
    if defining == unit_ideal:
        zero_quotient = source.quotient_ring(unit_ideal)
        zero_engine = _engine_ring(zero_quotient)
        assert zero_engine is not zero_quotient, (
            "the unit-adic zero completion needs the represented zero quotient engine"
        )

        def completion_image(_element):
            return zero_engine.zero()

        def projection_lift(_value, _exponent):
            return source.zero()

        return _AdicCompletionAlgebraParent(
            zero_engine,
            source,
            defining,
            precision,
            projection_lift=projection_lift,
            arithmetic_mode="exact_backend",
            completion_image=completion_image,
            completion_map_kernel=unit_ideal,
        )
    if defining == zero_ideal:
        def projection_lift(value, _exponent):
            return _owned_engine_element(source, engine(value))

        return _AdicCompletionAlgebraParent(
            engine,
            source,
            defining,
            precision,
            projection_lift=projection_lift,
            arithmetic_mode="exact_backend",
            completion_image=lambda element: _engine_element(source, source(element)),
            completion_map_kernel=zero_ideal,
        )
    if len(generators) == 1 and engine is SageZZ:
        generator = generators[0]
        prime = abs(SageZZ(generator))
        if not prime.is_prime():
            raise ValueError("the represented ZZ-adic completion is at a prime ideal (p)")
        completion_engine = engine.completion(prime, int(precision))

        def projection_lift(value, exponent):
            assert exponent <= int(precision), (
                "the selected p-adic computation precision must reach the requested truncation exponent"
            )
            return source(int(value.lift()))

        return _AdicCompletionAlgebraParent(
            completion_engine,
            source,
            defining,
            precision,
            projection_lift=projection_lift,
            completion_map_kernel=zero_ideal,
        )

    base = source.base_ring()
    assert (
        source in SymmetricAlgebras(base)
        or source in AlgebrasWithChosenFinitePresentation(base)
    ), (
        "adic completion currently has an exact maintained realization for polynomial rings, p-adic integers, and algebras with a chosen finite presentation"
    )
    if source not in SymmetricAlgebras(base):
        if source in AlgebrasWithChosenFinitePresentation(base):
            selected_power = defining.power(int(precision))
            truncation = source.quotient_ring(selected_power)
            truncation_engine = _engine_ring(truncation)
            assert truncation_engine is not truncation, (
                "the presented completion requires its maintained finite approximation engine"
            )
            quotient_map = truncation.quotient_map()

            def completion_image(element):
                return _engine_element(truncation, quotient_map(source(element)))

            def projection_lift(value, exponent):
                assert exponent <= int(precision), (
                    "the selected finite approximation must reach the requested adic level"
                )
                return _owned_engine_element(truncation, value).lift()

            completed_ideal_generators = tuple(
                completion_image(generator)
                for generator in defining.ideal_generators()
            )
            arithmetic_mode = "finite_approximation"
            completion_map_kernel = None
            if selected_power == zero_ideal:
                arithmetic_mode = "exact_backend"
                completion_map_kernel = zero_ideal
            elif defining.power(2) == defining:
                arithmetic_mode = "exact_backend"
                completion_map_kernel = defining
            return _AdicCompletionAlgebraParent(
                truncation_engine,
                source,
                defining,
                precision,
                completed_ideal_generators=completed_ideal_generators,
                projection_lift=projection_lift,
                arithmetic_mode=arithmetic_mode,
                completion_image=completion_image,
                completion_map_kernel=completion_map_kernel,
            )

    source_engine = _engine_ring(source)
    selected_variables = []
    engine_variables = tuple(source_engine.gens())
    for generator in generators:
        matching = tuple(variable for variable in engine_variables if generator == variable)
        assert len(matching) == 1, (
            "the supported multivariable completion requires an ideal generated by selected polynomial variables"
        )
        selected_variables.append(matching[0])
    completion_parameter = (
        selected_variables[0]
        if len(selected_variables) == len(engine_variables) == 1
        else tuple(selected_variables)
    )
    completion_engine = source_engine.completion(
        completion_parameter,
        prec=Infinity,
    )
    engine_map = completion_engine.coerce_map_from(source_engine)
    completed_ideal_generators = tuple(
        completion_engine(variable) for variable in selected_variables
    )

    def projection_lift(value, exponent):
        polynomial = value.truncate(exponent).polynomial()
        return _owned_engine_element(source, source_engine(polynomial))

    algebra_base = None
    formal_parameter_labels = None
    extra_categories = ()
    if len(selected_variables) == len(engine_variables):
        algebra_base = base
        formal_parameter_labels = tuple(source_engine.variable_names())
        extra_categories = (FormalPowerSeriesRings(base),)
    return _AdicCompletionAlgebraParent(
        completion_engine,
        source,
        defining,
        precision,
        engine_map=engine_map,
        completed_ideal_generators=completed_ideal_generators,
        projection_lift=projection_lift,
        arithmetic_mode="exact_lazy",
        completion_map_kernel=zero_ideal if source in OwnedRings().Commutative().NoZeroDivisors() else None,
        algebra_base=algebra_base,
        formal_parameter_labels=formal_parameter_labels,
        extra_categories=extra_categories,
    )


class FormalPowerSeriesRings(OwnedCategoryOverBaseRing):
    r"""Formal power-series rings ``R[[t]]`` over the owned ring ``R``."""

    def an_object(self):
        r"""The formal power series ring in one variable."""
        return self.base_ring().power_series_ring("t")

    @classmethod
    def _repr_object_names(cls):
        return "formal power-series rings"

    def super_categories(self):
        return [
            Algebras(self.base_ring()).Associative().Unital().Commutative(),
            OwnedAdicallyCompleteRings(),
        ]

    def _call_(self, *args, **kwargs):
        r"""Construct ``R[[x_1,...,x_n]]`` as the selected adic completion.

        Sage's power-series constructor is used only to parse its established
        notation and computational precision.  The mathematical object is the
        completion of ``R[x_1,...,x_n]`` at the ideal generated by the selected
        variables, through the general :class:`AdicCompletions` constructor.
        """
        parser = _SagePowerSeriesRing(_engine_ring(self.base_ring()), *args, **kwargs)
        labels = tuple(parser.variable_names())
        polynomial = self.base_ring().polynomial_ring(labels)
        defining = polynomial.ideal(
            *(polynomial.algebra_generator(label) for label in labels)
        )
        precision = getattr(
            parser,
            "default_prec",
            lambda: kwargs.get("default_prec", 20),
        )()
        completion = AdicCompletions()(
            polynomial,
            defining,
            precision=int(precision),
        )
        if completion not in self:
            raise ArithmeticError(
                "completion at all polynomial variables did not retain the formal-power-series specialization"
            )
        return completion

    class ParentMethods:
        def formal_parameter_set(self):
            r"""Return the selected formal variables, not algebra generators."""
            labels = self._preamble_formal_parameter_labels
            if labels is None:
                raise ArithmeticError(
                    "this completion has no selected formal-power-series variables"
                )
            return labels

        def formal_parameter(self, label):
            r"""Return the image of one polynomial variable in the completion."""
            labels = self.formal_parameter_set()
            normalized = labels(label)
            return self.completion_map()(
                self.completion_source().algebra_generator(normalized)
            )

        def power_series_variable(self):
            labels = self.formal_parameter_set()
            if int(labels.cardinality()) != 1:
                raise ArithmeticError(
                    "a one-variable formal power-series ring has one selected variable"
                )
            return self.formal_parameter(labels[0])

        def cardinality(self):
            r"""Return ``|R|^aleph0`` for a nonconstant formal series ring."""
            parameter_count = int(self.formal_parameter_set().cardinality())
            match parameter_count:
                case 0:
                    return cardinal(self.base_ring().cardinality())
                case _:
                    return cardinal(self.base_ring().cardinality()) ** aleph0

    class ElementMethods:
        def coefficient(self, degree):
            degree = int(degree)
            if degree < 0:
                return self.parent().base_ring().zero()
            parent = self.parent()
            base = parent.base_ring()
            backend = parent._engine_element(self)
            return _owned_engine_element(base, backend[degree])

        def __getitem__(self, degree):
            return self.coefficient(degree)


def Zp(*args, **kwargs):
    source = _own_ring(SageZZ)
    prime_value = args[0] if args else kwargs.get("p")
    owned_prime = source(prime_value)
    prime = SageZZ(_engine_element(source, owned_prime))
    engine_args = (prime, *args[1:]) if args else args
    engine_kwargs = dict(kwargs)
    if not args and "p" in engine_kwargs:
        engine_kwargs["p"] = prime
    parser = _SageZp(*engine_args, **engine_kwargs)
    defining = source.ideal(owned_prime)
    return AdicCompletions()(
        source,
        defining,
        precision=int(parser.precision_cap()),
    )
class _DualNumbersAlgebraParent(_OwnedAlgebraParent):
    r"""The dual-number quotient with its defining quotient data fixed at construction."""

    def __init__(self, engine, base, polynomial, defining_ideal, label) -> None:
        engine_map = engine.coerce_map_from(_engine_ring(polynomial))

        def quotient_map():
            return _canonical_map(
                polynomial,
                self,
                engine_map,
            )

        self._quotient_source = polynomial
        self._quotient_defining_ideal = defining_ideal
        self._quotient_map_factory = quotient_map
        placements = [QuotientRings()]
        if base in OwnedRings().Noetherian():
            placements.append(OwnedRings().Noetherian())
        if base in OwnedRings().Artinian():
            placements.append(OwnedRings().Artinian())
        if base in OwnedRings().Commutative().Local():
            placements.append(OwnedRings().Commutative().Local())
        _OwnedAlgebraParent.__init__(
            self,
            engine,
            base,
            (label,),
            categories=tuple(placements),
        )
        if base in OwnedRings().Commutative().Local():
            epsilon_bar = self._from_engine_element(engine.gen())
            maximal_ideal = _maximal_ideal_over_local_base(
                self,
                base,
                (epsilon_bar,),
            )
            _install_local_ring_construction(
                self,
                maximal_ideal,
                base.residue_field(),
            )


def _dual_numbers(base_ring, name="epsilon"):
    r"""Return the dual-number algebra ``R[epsilon]/(epsilon^2)``."""
    base = _own_ring(base_ring)
    polynomial = _algebra_with_structure(
        _own_ring(_SagePolynomialRing(_engine_ring(base), name)),
        base,
        (name,),
    )
    engine_polynomial = _engine_ring(polynomial)
    epsilon = engine_polynomial.gen()
    defining_ideal = engine_polynomial.ideal(epsilon**2)
    quotient_engine = engine_polynomial.quotient(defining_ideal)
    return _DualNumbersAlgebraParent(
        quotient_engine,
        base,
        polynomial,
        defining_ideal,
        name,
    )


__all__ = [
    "AdicCompletions",
    "DistinguishedOpenSubobjects",
    "GeneratedIdealView",
    "LocalizationRings",
    "PrimeLocalizations",
    "QuotientRings",
    "ZariskiClosedSubobjects",
    "Zp",
]
