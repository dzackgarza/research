r"""Owned number fields and their selected primitive-element presentations."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_function, cached_method
from sage.all import (
    CyclotomicField as _SageCyclotomicField,
    NumberField as _SageNumberField,
    QuadraticField as _SageQuadraticField,
)
from sage.rings.abc import Order as SageNumberFieldOrder
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories._lattice import signature_pair
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoryPacketMethods,
    HomCategoryConstruction,
)
from dzack_research.preamble.categories.rings.embeddings import (
    NumberFieldHomset,
    order_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    OwnedOrders,
    OwnedRings,
    _engine_element,
    _engine_numeral,
    _engine_ring,
    _owned_engine_ring,
)
from dzack_research.preamble.refine import refine
from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.group.groups import _own_group
from dzack_research.preamble.categories.modules.fractional_ideals import (
    FractionalIdeal,
    Ideal,
)
from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
    FreeModuleOn,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism
from dzack_research.preamble.categories.modules.pure.modules import FinitelyGeneratedFreeModules
from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_image,
    finite_ordered_set,
)
from dzack_research.preamble.categories.sets.cardinals import cardinal
from dzack_research.preamble.categories.sets.indexed_families import indexed_family


def _own_number_field(engine):

    return _refine_number_field_view(_own_ring(engine))


def CyclotomicField(order, *args, **kwargs):
    return _own_number_field(
        _SageCyclotomicField(_engine_numeral(SageZZ, order), *args, **kwargs)
    )


def QuadraticField(discriminant, *args, **kwargs):
    return _own_number_field(
        _SageQuadraticField(_engine_numeral(SageQQ, discriminant), *args, **kwargs)
    )


def NumberField(polynomial, *args, **kwargs):
    parent = getattr(polynomial, "parent", lambda: None)()
    if parent not in OwnedRings():
        raise TypeError("NumberField expects a polynomial in a preamble polynomial ring")
    backend_polynomial = _engine_element(parent, polynomial)
    return _own_number_field(_SageNumberField(backend_polynomial, *args, **kwargs))


class NumberFieldHomCategoryConstruction(HomCategoryConstruction):
    def fixed_category_class(self):
        return NumberFieldHomset


class OwnedNumberFields(CategoryPacketMethods, Category):
    r"""Finite extensions of ``QQ``."""

    _HomCategory = NumberFieldHomCategoryConstruction
    _certifying_predicate = "_preamble_is_number_field"

    @classmethod
    def _repr_object_names(cls):
        return "number fields"

    def super_categories(self):
        return [OwnedFields()]

    def Mor(self, domain, codomain):
        if domain not in self or codomain not in self:
            raise TypeError("a number-field embedding requires two number fields")
        return self.HomCategory().Of(domain, codomain)

    class ParentMethods:
        def Mor(self, codomain, category=None):
            number_fields = OwnedNumberFields()
            if category is None or category.is_subcategory(number_fields):
                return number_fields.Mor(self, codomain)
            return super().Mor(codomain, category=category)

        def degree(self):
            r"""Return ``[K:QQ]`` as an owned integer."""

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = (
                SageZZ.one()
                if engine is SageQQ
                else SageZZ(
                    engine.degree()
                    if engine.is_absolute()
                    else engine.absolute_degree()
                )
            )
            return integers._from_engine_element(value)

        def discriminant(self):
            r"""Return the discriminant of the ring of integers of ``K``."""

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = SageZZ.one() if engine is SageQQ else SageZZ(engine.discriminant())
            return integers._from_engine_element(value)

        def signature(self):
            r"""Return the signature pair ``(r_1,r_2)`` with ``r_1+2r_2=[K:QQ]``."""

            engine = _engine_ring(self)
            if engine is SageQQ:
                return signature_pair(1, 0)
            real, complex_pairs = engine.signature()
            return signature_pair(real, complex_pairs)

        def class_number(self):
            r"""Return the class number of the ring of integers."""

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = SageZZ.one() if engine is SageQQ else SageZZ(engine.class_number())
            return integers._from_engine_element(value)

        def extension(self, polynomial, name="a"):
            r"""Return the finite extension defined by an owned polynomial over ``self``."""
            polynomial_ring = getattr(polynomial, "parent", lambda: None)()
            if polynomial_ring is None or polynomial_ring.base_ring() is not self:
                raise TypeError(
                    "a relative number-field extension requires a polynomial over this field"
                )

            backend_polynomial = _engine_element(polynomial_ring, polynomial)
            return _own_ring(_engine_ring(self).extension(backend_polynomial, name))

        def primes_above(self, prime):
            r"""Return the prime ideals of ``O_K`` above a rational prime."""

            order = self.ring_of_integers()
            integers = order.base_ring()
            prime = integers(prime)
            backend_prime = _engine_element(integers, prime)
            order_engine = _engine_ring(order)
            ideals = []
            for backend_ideal in _engine_ring(self).primes_above(backend_prime):
                generators = tuple(
                    order._from_engine_element(order_engine(generator))
                    for generator in backend_ideal.gens()
                )
                ideals.append(order.ideal(*generators))
            return finite_ordered_set(ideals)

        def ring_of_integers(self):
            r"""Return the maximal order ``O_K`` as an owned ring."""

            engine = _engine_ring(self)
            if engine is SageQQ:
                return _refine_order_view(_own_ring(SageZZ))
            return _refine_order_view(_own_ring(engine.ring_of_integers()))

        maximal_order = ring_of_integers

        def order_generated_by(self, *generators):
            r"""Return the order ``ZZ[generators]`` inside this number field."""
            if not generators:
                raise ValueError("an order construction needs at least one field generator")

            engine = _engine_ring(self)
            backend_generators = tuple(
                _engine_element(self, self(generator)) for generator in generators
            )
            datum = (
                backend_generators[0]
                if len(backend_generators) == 1
                else list(backend_generators)
            )
            return _refine_order_view(_own_ring(engine.order(datum)))

        def ramified_primes(self):
            r"""Return the rational primes ramified in ``K``."""

            return finite_ordered_set(abs(self.discriminant()).prime_divisors())

        def embeddings(self, target):
            r"""Return the exact owned field embeddings ``K -> target``."""

            if target not in OwnedFields():
                raise TypeError("number-field embeddings require an owned target field")
            return self.Mor(target).embeddings()

        def is_galois(self) -> bool:
            r"""Return whether ``K/QQ`` is Galois."""
            engine = _engine_ring(self)
            return True if engine is SageQQ else bool(engine.is_galois())

        def galois_group(self):
            r"""Return ``Gal(K/QQ)``; this name is reserved for Galois ``K``."""
            if not self.is_galois():
                raise ValueError(
                    "K/QQ is not Galois; use normal_closure_galois_group() for the Galois group of its normal closure"
                )
            engine = _engine_ring(self)

            if engine is SageQQ:
                from sage.groups.perm_gps.permgroup_named import SymmetricGroup

                return _own_group(SymmetricGroup(1))
            return _own_group(engine.galois_group())

        def normal_closure(self):
            r"""Return a chosen normal closure of ``K/QQ``."""

            engine = _engine_ring(self)
            return self if engine is SageQQ else _own_ring(engine.galois_closure())

        def normal_closure_galois_group(self):
            r"""Return the Galois group of a chosen normal closure of ``K``."""
            return self.normal_closure().galois_group()

        def as_algebra(self):
            r"""Return this field with its selected finite ``QQ``-algebra presentation."""
            from dzack_research.preamble.categories.algebras.free_algebras import (
                SymmetricAlgebraOn,
                _presented_algebra_on_engine,
            )

            rationals = _own_number_field(SageQQ)
            engine = _engine_ring(self)
            if engine is SageQQ:
                return rationals

            presentation_lift = None
            finite_free_coordinates = None
            if not engine.is_absolute():
                # A relative generator need not generate K over QQ.  Sage's
                # absolute model supplies both the chosen absolute primitive
                # element in this same engine and exact conversion to its
                # one-variable QQ presentation.
                absolute = engine.absolute_field("absolute_generator")
                from_absolute, to_absolute = absolute.structure()
                primitive = from_absolute(absolute.gen())
                polynomial = absolute.defining_polynomial()
                labels = finite_ordered_set(("absolute_generator",))
                presentation_lift = lambda element: to_absolute(element).lift()
                finite_free_coordinates = lambda element: tuple(to_absolute(element))
                degree = int(engine.absolute_degree())
            else:
                primitive = engine.gen()
                polynomial = engine.defining_polynomial()
                labels = self.algebra_generating_set()
                degree = int(engine.degree())

            presentation = SymmetricAlgebraOn(rationals, labels)
            relation = presentation._from_engine_element(
                _engine_ring(presentation)(polynomial)
            )
            return _presented_algebra_on_engine(
                engine,
                presentation,
                (relation,),
                generator_values=(primitive,),
                finite_free_degree=degree,
                finite_free_generator=primitive,
                finite_free_coordinates=finite_free_coordinates,
                presentation_lift=presentation_lift,
            )


class NumberFieldsWithChosenPrimitiveElement(Category):
    r"""Number fields carrying the primitive element selected by their presentation."""

    _certifying_predicate = "_preamble_has_chosen_primitive_element"

    @classmethod
    def _repr_object_names(cls):
        return "number fields with a chosen primitive element"

    def super_categories(self):
        return [OwnedNumberFields()]

    class ParentMethods:
        def algebra_generating_set(self):
            return finite_ordered_set(_engine_ring(self).variable_names())

        def primitive_element(self):
            r"""Return the selected primitive element ``alpha``."""
            return self._from_engine_element(_engine_ring(self).gen())

        def algebra_generator(self, label):
            if label not in self.algebra_generating_set():
                raise ValueError(f"{label!r} is not the selected algebra-generator label")
            return self.primitive_element()

        def defining_polynomial(self):
            r"""Return the owned defining polynomial of the selected primitive element."""

            polynomial = _engine_ring(self).defining_polynomial()
            parent = _own_ring(polynomial.parent())
            return parent._from_engine_element(polynomial)

        def embedding_images(self, target):
            r"""Return the images of the selected primitive element under ``K -> target``."""

            primitive = self.primitive_element()
            embeddings = self.embeddings(target)
            return finite_ordered_image(
                embeddings,
                lambda embedding: embedding(primitive),
                name="Primitive-element embedding images",
            )


class OrdersWithChosenIntegralBasis(Category):
    r"""Number-field orders carrying their selected integral basis."""

    _certifying_predicate = "_preamble_is_number_field_order"

    @classmethod
    def _repr_object_names(cls):
        return "orders with a chosen integral basis"

    def super_categories(self):

        integers = _own_ring(SageZZ)
        return [
            OwnedOrders(),
            Algebras(integers),
            FinitelyGeneratedFreeModules(integers),
        ]

    class ParentMethods:
        def base_ring(self):

            return _own_ring(SageZZ)

        algebra_base_ring = base_ring

        def _Hom_(self, codomain, category=None):
            if codomain not in OwnedOrders():
                raise TypeError("an order embedding must land in an order")
            if category is not None and not category.is_subcategory(OwnedOrders()):
                raise TypeError("this is not an order-embedding category")
            return order_homset(self, codomain)

        def ideal(self, *module_generators):

            return Ideal(self, module_generators)

        def fractional_ideal(self, *module_generators):

            return FractionalIdeal(self, module_generators)

        def localization(self, *elements):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                Localization,
            )

            return Localization(self, *elements)

        localize = localization

        def localize_at_prime(self, prime):
            from dzack_research.preamble.categories.rings.commutative_algebra import (
                PrimeLocalization,
            )

            return PrimeLocalization(self, prime)

        localization_at_prime = localize_at_prime

        def base_change(self, ring_map):
            if _engine_ring(ring_map.domain()) is not SageZZ:
                raise ValueError("an order is a ZZ-algebra, so scalar extension starts at ZZ")
            target = _engine_ring(ring_map.codomain())
            if target is SageZZ:
                return self
            if target is SageQQ:

                field = _own_number_field(_engine_ring(self).fraction_field())
                return field.as_algebra()
            raise NotImplementedError(
                "the active order algebra-base-change adapter currently constructs ZZ -> ZZ and ZZ -> QQ"
            )

        def integral_basis(self):
            return self.module_generators()

        @cached_method
        def module_generating_set(self):

            engine = _engine_ring(self)
            if engine is SageZZ:
                return finite_ordered_set((0,))
            return finite_ordered_set(range(int(engine.rank())))

        def module_generator(self, label):
            labels = self.module_generating_set()
            if label not in labels:
                raise ValueError(f"{label!r} is not a module-generator label")
            engine = _engine_ring(self)
            if engine is SageZZ:
                return self._from_engine_element(SageZZ.one())
            return self._from_engine_element(engine.basis()[labels.ranking_map()(label)])

        @cached_method
        def module_generators(self):

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Ring-module generator family",
            )

        def module_rank(self):
            engine = _engine_ring(self)
            return cardinal(1 if engine is SageZZ else engine.rank())


def _refine_order_view(order):
    r"""Return the constructor-owned order view with its selected integral basis."""
    return _owned_order_view(_engine_ring(order))


def _refine_number_field_view(field):
    r"""Return the constructor-owned number-field view of an engine field."""
    if field not in OwnedRings():
        raise TypeError("number-field construction expects an owned ring view")
    return _owned_number_field_view(_engine_ring(field))


@cached_function
def _owned_order_view(engine):
    r"""The selected-integral-basis view of one engine order.

    One engine has one owned ring, so the view refines that ring in place
    rather than constructing a second parent on the same engine.
    """
    if not (engine is SageZZ or isinstance(engine, SageNumberFieldOrder)):
        raise TypeError("the selected integral-basis view requires a number-field order")
    return refine(_owned_engine_ring(engine), OrdersWithChosenIntegralBasis())


@cached_function
def _owned_number_field_view(engine):
    r"""The strongest number-field view determined by ``engine``, refined in place."""
    categories = [OwnedNumberFields()]
    if engine is not SageQQ:
        categories.append(NumberFieldsWithChosenPrimitiveElement())
    return refine(_owned_engine_ring(engine), Category.join(tuple(categories)))



__all__ = [
    "NumberFieldsWithChosenPrimitiveElement",
    "OrdersWithChosenIntegralBasis",
    "OwnedNumberFields",
]
