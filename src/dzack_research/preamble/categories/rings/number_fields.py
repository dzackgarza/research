r"""Owned number fields and their selected primitive-element presentations."""

from sage.categories.category import Category
from sage.rings.integer_ring import ZZ as SageZZ
from sage.rings.rational_field import QQ as SageQQ

from dzack_research.preamble.categories.rings.rings import (
    OwnedFields,
    OwnedOrders,
    OwnedRings,
    engine_ring,
)
from dzack_research.preamble.refine import refine


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
            r"""Return ``[K:QQ]``."""
            engine = engine_ring(self)
            return SageZZ.one() if engine is SageQQ else SageZZ(engine.degree())

        def discriminant(self):
            r"""Return the discriminant of the ring of integers of ``K``."""
            engine = engine_ring(self)
            return SageZZ.one() if engine is SageQQ else SageZZ(engine.discriminant())

        def signature(self):
            r"""Return ``(r_1,r_2)`` with ``r_1+2r_2=[K:QQ]``."""
            engine = engine_ring(self)
            if engine is SageQQ:
                return (SageZZ.one(), SageZZ.zero())
            real, complex_pairs = engine.signature()
            return (SageZZ(real), SageZZ(complex_pairs))

        def class_number(self):
            r"""Return the class number of the ring of integers."""
            engine = engine_ring(self)
            return SageZZ.one() if engine is SageQQ else SageZZ(engine.class_number())

        def ring_of_integers(self):
            r"""Return the maximal order ``O_K`` as an owned ring."""
            from dzack_research.preamble.categories.rings.rings import own_ring

            engine = engine_ring(self)
            if engine is SageQQ:
                return refine(own_ring(SageZZ), OwnedOrders())
            return own_ring(engine.ring_of_integers())

        maximal_order = ring_of_integers

        def ramified_primes(self):
            r"""Return the rational primes ramified in ``K``."""
            from dzack_research.preamble.categories.sets import finite_ordered_set

            return finite_ordered_set(abs(self.discriminant()).prime_divisors())

        def embeddings(self, target):
            r"""Return the exact field embeddings ``K -> target`` supplied by Sage."""
            from dzack_research.preamble.categories.sets import finite_ordered_set

            return finite_ordered_set(
                engine_ring(self).embeddings(engine_ring(target))
            )

        def is_galois(self) -> bool:
            r"""Return whether ``K/QQ`` is Galois."""
            engine = engine_ring(self)
            return True if engine is SageQQ else bool(engine.is_galois())

        def galois_group(self):
            r"""Return ``Gal(K/QQ)``; this name is reserved for Galois ``K``."""
            if not self.is_galois():
                raise ValueError(
                    "K/QQ is not Galois; use normal_closure_galois_group() for the Galois group of its normal closure"
                )
            engine = engine_ring(self)
            from dzack_research.preamble.categories.group.groups import refine_group

            if engine is SageQQ:
                from sage.groups.perm_gps.permgroup_named import SymmetricGroup

                return refine_group(SymmetricGroup(1))
            return refine_group(engine.galois_group())

        def normal_closure(self):
            r"""Return a chosen normal closure of ``K/QQ``."""
            from dzack_research.preamble.categories.rings.rings import own_ring

            engine = engine_ring(self)
            return self if engine is SageQQ else own_ring(engine.galois_closure())

        def normal_closure_galois_group(self):
            r"""Return the Galois group of a chosen normal closure of ``K``."""
            return self.normal_closure().galois_group()

        def as_algebra(self):
            r"""Return this field as the corresponding ``QQ``-algebra object."""
            from dzack_research.preamble.categories.algebras.algebras import refine_algebra
            from dzack_research.preamble.categories.algebras.finitely_presented_algebras import (
                FinitelyPresentedAlgebras,
            )

            labels = (
                self.algebra_generating_set()
                if self in NumberFieldsWithChosenPrimitiveElement()
                else None
            )
            algebra = refine_algebra(self, SageQQ, labels)
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
            return engine_ring(self).gen()

        def algebra_generator(self, label):
            if label not in self.algebra_generating_set():
                raise ValueError(f"{label!r} is not the selected algebra-generator label")
            return self.primitive_element()

        def defining_polynomial(self):
            r"""Return the defining polynomial of the selected primitive element."""
            return engine_ring(self).defining_polynomial()

        def embedding_images(self, target):
            r"""Return the images of the selected primitive element under ``K -> target``."""
            from dzack_research.preamble.categories.sets import finite_ordered_set

            primitive = self.primitive_element()
            return finite_ordered_set(
                embedding(primitive) for embedding in self.embeddings(target)
            )


def _refine_number_field_view(field):
    r"""Refine an already-owned field view into its number-field categories."""
    if field not in OwnedRings():
        raise TypeError("number-field refinement expects an owned ring view")
    engine = engine_ring(field)
    categories = [OwnedNumberFields()]
    if engine is not SageQQ:
        from dzack_research.preamble.categories.sets import finite_ordered_set

        field._preamble_number_field_generating_set = finite_ordered_set(
            engine.variable_names()
        )
        categories.append(NumberFieldsWithChosenPrimitiveElement())
    return refine(field, categories)


def refine_number_field(field):
    r"""Return the owned number-field view of a native number field."""
    if field in OwnedRings():
        return _refine_number_field_view(field)
    from dzack_research.preamble.categories.rings.rings import own_ring

    return own_ring(field)


__all__ = [
    "NumberFieldsWithChosenPrimitiveElement",
    "OwnedNumberFields",
    "refine_number_field",
]
