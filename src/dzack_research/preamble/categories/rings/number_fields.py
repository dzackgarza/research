r"""Owned number fields and their selected primitive-element presentations."""

from sage.categories.category import Category
from sage.misc.cachefunc import cached_method
from sage.all import (
    CyclotomicField as _SageCyclotomicField,
    NumberField as _SageNumberField,
    QuadraticField as _SageQuadraticField,
)
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.ring_foundation import (
    OwnedFields,
    OwnedOrders,
    OwnedRings,
    _engine_element,
    _engine_ring,
)
from dzack_research.preamble.refine import refine


def _own_number_field(engine):
    from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

    return _refine_number_field_view(_own_ring(engine))


def CyclotomicField(*args, **kwargs):
    return _own_number_field(_SageCyclotomicField(*args, **kwargs))


def QuadraticField(*args, **kwargs):
    return _own_number_field(_SageQuadraticField(*args, **kwargs))


def NumberField(polynomial, *args, **kwargs):
    parent = getattr(polynomial, "parent", lambda: None)()
    if parent not in OwnedRings():
        raise TypeError("NumberField expects a polynomial in a preamble polynomial ring")
    backend_polynomial = _engine_element(parent, polynomial)
    return _own_number_field(_SageNumberField(backend_polynomial, *args, **kwargs))


class OwnedNumberFields(Category):
    r"""Finite extensions of ``QQ``."""

    @classmethod
    def _repr_object_names(cls):
        return "number fields"

    def super_categories(self):
        return [OwnedFields()]

    class ParentMethods:
        def _Hom_(self, codomain, category=None):
            if codomain not in OwnedNumberFields():
                raise TypeError("a number-field embedding must land in a number field")
            if category is not None and not category.is_subcategory(OwnedNumberFields()):
                raise TypeError("this is not a number-field embedding category")
            from dzack_research.preamble.categories.rings.embeddings import (
                number_field_homset,
            )

            return number_field_homset(self, codomain)

        def degree(self):
            r"""Return ``[K:QQ]`` as an owned integer."""
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = SageZZ.one() if engine is SageQQ else SageZZ(engine.degree())
            return integers._from_engine_element(value)

        def discriminant(self):
            r"""Return the discriminant of the ring of integers of ``K``."""
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            value = SageZZ.one() if engine is SageQQ else SageZZ(engine.discriminant())
            return integers._from_engine_element(value)

        def signature(self):
            r"""Return ``(r_1,r_2)`` with ``r_1+2r_2=[K:QQ]``."""
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            integers = _own_ring(SageZZ)
            engine = _engine_ring(self)
            if engine is SageQQ:
                return (integers.one(), integers.zero())
            real, complex_pairs = engine.signature()
            return (
                integers._from_engine_element(SageZZ(real)),
                integers._from_engine_element(SageZZ(complex_pairs)),
            )

        def class_number(self):
            r"""Return the class number of the ring of integers."""
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

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
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            backend_polynomial = _engine_element(polynomial_ring, polynomial)
            return _own_ring(_engine_ring(self).extension(backend_polynomial, name))

        def primes_above(self, prime):
            r"""Return the prime ideals of ``O_K`` above a rational prime."""
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

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
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            engine = _engine_ring(self)
            if engine is SageQQ:
                return _refine_order_view(_own_ring(SageZZ))
            return _refine_order_view(_own_ring(engine.ring_of_integers()))

        maximal_order = ring_of_integers

        def order_generated_by(self, *generators):
            r"""Return the order ``ZZ[generators]`` inside this number field."""
            if not generators:
                raise ValueError("an order construction needs at least one field generator")
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

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
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

            return finite_ordered_set(abs(self.discriminant()).prime_divisors())

        def embeddings(self, target):
            r"""Return the exact owned field embeddings ``K -> target``."""
            from dzack_research.preamble.categories.rings.ring_foundation import OwnedFields
            from dzack_research.preamble.categories.rings.embeddings import (
                number_field_homset,
            )
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

            if target not in OwnedFields():
                raise TypeError("number-field embeddings require an owned target field")
            return finite_ordered_set(number_field_homset(self, target).embeddings())

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
            from dzack_research.preamble.categories.group.groups import _own_group

            if engine is SageQQ:
                from sage.groups.perm_gps.permgroup_named import SymmetricGroup

                return _own_group(SymmetricGroup(1))
            return _own_group(engine.galois_group())

        def normal_closure(self):
            r"""Return a chosen normal closure of ``K/QQ``."""
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            engine = _engine_ring(self)
            return self if engine is SageQQ else _own_ring(engine.galois_closure())

        def normal_closure_galois_group(self):
            r"""Return the Galois group of a chosen normal closure of ``K``."""
            return self.normal_closure().galois_group()

        def as_algebra(self):
            r"""Return this field as the corresponding ``QQ``-algebra object."""
            from dzack_research.preamble.categories.algebras.algebras import (
                FinitelyPresentedAlgebras,
                refine_algebra,
            )

            labels = (
                self.algebra_generating_set()
                if self in NumberFieldsWithChosenPrimitiveElement()
                else None
            )
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring
            algebra = refine_algebra(self, _own_ring(SageQQ), labels)
            return refine(algebra, FinitelyPresentedAlgebras(algebra.base_ring()))


class NumberFieldsWithChosenPrimitiveElement(Category):
    r"""Number fields carrying the primitive element selected by their presentation."""

    @classmethod
    def _repr_object_names(cls):
        return "number fields with a chosen primitive element"

    def super_categories(self):
        return [OwnedNumberFields()]

    class ParentMethods:
        def algebra_generating_set(self):
            return self._preamble_number_field_generating_set

        def primitive_element(self):
            r"""Return the selected primitive element ``alpha``."""
            return self._from_engine_element(_engine_ring(self).gen())

        def algebra_generator(self, label):
            if label not in self.algebra_generating_set():
                raise ValueError(f"{label!r} is not the selected algebra-generator label")
            return self.primitive_element()

        def defining_polynomial(self):
            r"""Return the owned defining polynomial of the selected primitive element."""
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            polynomial = _engine_ring(self).defining_polynomial()
            parent = _own_ring(polynomial.parent())
            return parent._from_engine_element(polynomial)

        def embedding_images(self, target):
            r"""Return the images of the selected primitive element under ``K -> target``."""
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_image

            primitive = self.primitive_element()
            embeddings = self.embeddings(target)
            return finite_ordered_image(
                embeddings,
                lambda embedding: embedding(primitive),
                name="Primitive-element embedding images",
            )


class OrdersWithChosenIntegralBasis(Category):
    r"""Number-field orders carrying their selected integral basis."""

    @classmethod
    def _repr_object_names(cls):
        return "orders with a chosen integral basis"

    def super_categories(self):
        from dzack_research.preamble.categories.algebras.algebras import Algebras
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FinitelyGeneratedFreeModules,
        )
        from dzack_research.preamble.categories.modules.framed.framed_free_modules import (
            FreeModuleBaseRings,
        )
        from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

        integers = _own_ring(SageZZ)
        return [
            OwnedOrders(),
            FreeModuleBaseRings(),
            Algebras(integers),
            FinitelyGeneratedFreeModules(integers),
        ]

    class ParentMethods:
        def base_ring(self):
            from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

            return _own_ring(SageZZ)

        algebra_base_ring = base_ring

        def _Hom_(self, codomain, category=None):
            if codomain not in OwnedOrders():
                raise TypeError("an order embedding must land in an order")
            if category is not None and not category.is_subcategory(OwnedOrders()):
                raise TypeError("this is not an order-embedding category")
            from dzack_research.preamble.categories.rings.embeddings import order_homset

            return order_homset(self, codomain)

        def ideal(self, *module_generators):
            from dzack_research.preamble.categories.modules.fractional_ideals import Ideal

            return Ideal(self, module_generators)

        def fractional_ideal(self, *module_generators):
            from dzack_research.preamble.categories.modules.fractional_ideals import (
                FractionalIdeal,
            )

            return FractionalIdeal(self, module_generators)

        def base_change(self, ring_map):
            if _engine_ring(ring_map.domain()) is not SageZZ:
                raise ValueError("an order is a ZZ-algebra, so scalar extension starts at ZZ")
            target = _engine_ring(ring_map.codomain())
            if target is SageZZ:
                return self
            if target is SageQQ:
                from dzack_research.preamble.categories.rings.ring_foundation import _own_ring

                field = _own_number_field(_engine_ring(self).fraction_field())
                return field.as_algebra()
            raise NotImplementedError(
                "the active order algebra-base-change adapter currently constructs ZZ -> ZZ and ZZ -> QQ"
            )

        def integral_basis(self):
            return self.module_generators()

        @cached_method
        def module_generating_set(self):
            from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

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
            return self._from_engine_element(engine.basis()[labels.position(label)])

        @cached_method
        def module_generators(self):
            from dzack_research.preamble.categories.sets.indexed_families import indexed_family

            return indexed_family(
                self.module_generating_set(),
                self.module_generator,
                name="Ring-module generator family",
            )

        def framing_morphism(self):
            from dzack_research.preamble.categories.modules.framed.framed_free_modules import FreeModuleOn
            from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import framing_morphism

            source = FreeModuleOn(self.base_ring(), self.module_generating_set())
            return framing_morphism(source, self, self.module_generator)

        def rank(self):
            integers = self.base_ring()
            engine = _engine_ring(self)
            return (
                integers.one()
                if engine is SageZZ
                else integers._from_engine_element(SageZZ(engine.rank()))
            )


def _refine_order_view(order):
    r"""Attach the selected integral-basis structure to an owned order."""
    if _engine_ring(order) is SageZZ:
        order = refine(order, OwnedOrders())
    if order not in OwnedOrders():
        raise TypeError("order refinement expects an owned number-field order")
    order = refine(order, OrdersWithChosenIntegralBasis())
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        refine_commutative_ring_constructions,
    )

    return refine_commutative_ring_constructions(order)


def _refine_number_field_view(field):
    r"""Refine an already-owned field view into its number-field categories."""
    if field not in OwnedRings():
        raise TypeError("number-field refinement expects an owned ring view")
    engine = _engine_ring(field)
    categories = [OwnedNumberFields()]
    if engine is not SageQQ:
        from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

        field._preamble_number_field_generating_set = finite_ordered_set(
            engine.variable_names()
        )
        categories.append(NumberFieldsWithChosenPrimitiveElement())
    field = refine(field, categories)
    from dzack_research.preamble.categories.rings.commutative_algebra import (
        refine_commutative_ring_constructions,
    )

    return refine_commutative_ring_constructions(field)



__all__ = [
    "NumberFieldsWithChosenPrimitiveElement",
    "OrdersWithChosenIntegralBasis",
    "OwnedNumberFields",
]
