r"""Decomposition, inertia, and Frobenius projections of (G_K)."""

from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.groups import OwnedFiniteGroups
from dzack_research.preamble.categories.rings.ring_foundation import _engine_element, _engine_ring
from dzack_research.preamble.categories.sets.finite_ordered_sets import (
    finite_ordered_filter,
    finite_ordered_set,
)


class PrimeProlongation(SageObject):
    r"""A coherent finite-stage oracle for a chosen prolongation (\bar v)."""

    def __init__(self, base_prime, at_stage) -> None:
        if not callable(at_stage):
            raise TypeError("a prolongation must supply a finite-stage prime function")
        self._base_prime = base_prime
        self._at_stage = at_stage

    def base_prime(self):
        return self._base_prime

    def at(self, extension):
        prime = self._at_stage(extension)
        if prime is None:
            raise ValueError("the prolongation supplies no prime at this finite stage")
        return prime

    def _repr_(self) -> str:
        return f"Chosen prolongation of {self._base_prime}"


def _engine_prime(prime):
    r"""Return the private number-field prime ideal represented by ``prime``."""
    crossing = getattr(prime, "_engine_ideal", None)
    backend = crossing() if crossing is not None else prime
    ring = getattr(backend, "ring", lambda: None)()
    number_field = getattr(ring, "number_field", None)
    if number_field is not None:
        field = number_field()
        try:
            return field.ideal(tuple(backend.gens()))
        except (AttributeError, TypeError, ValueError):
            pass
    return backend


def _image_prime(prime, automorphism):
    prime = _engine_prime(prime)
    backend = automorphism.action()._engine_morphism_crossing()
    try:
        return prime.apply_morphism(backend)
    except AttributeError:
        field = _engine_ring(automorphism.parent().top_field())
        return field.ideal([backend(generator) for generator in prime.gens()])


def _fixes_residue_field(prime, automorphism) -> bool:
    prime = _engine_prime(prime)
    residue = prime.residue_field()
    owned_field = automorphism.parent().top_field()
    field = _engine_ring(owned_field)
    order = field.maximal_order()
    for basis_element in order.basis():
        owned_basis = owned_field._from_engine_element(field(basis_element))
        image = automorphism(owned_basis)
        if residue(_engine_element(owned_field, image)) != residue(basis_element):
            return False
    return True


def _residue_field_order(base_prime):
    from sage.rings.integer_ring import ZZ

    base_prime = _engine_prime(base_prime)
    if base_prime in ZZ:
        return abs(ZZ(base_prime))
    try:
        norm = base_prime.norm()
        if norm in ZZ:
            return abs(ZZ(norm))
    except (AttributeError, TypeError, ValueError):
        pass
    try:
        generators = tuple(base_prime.gens_reduced())
    except (AttributeError, NotImplementedError):
        generators = tuple(base_prime.gens())
    if len(generators) == 1 and generators[0] in ZZ:
        return abs(ZZ(generators[0]))
    raise TypeError(
        "the absolute residue-field cardinality of the base prime is unavailable"
    )


class FiniteGaloisSubgroup(Parent):
    r"""A literal finite subgroup represented by selected quotient elements."""

    def __init__(self, supergroup, elements, description) -> None:
        self._supergroup = supergroup
        self._elements = tuple(elements)
        self._element_set = frozenset(self._elements)
        self._description = description
        if supergroup.one() not in self._element_set:
            raise ValueError("a represented subgroup must contain the identity")
        if any(
            left * right not in self._element_set
            for left in self._elements
            for right in self._elements
        ):
            raise ValueError(
                "the selected finite elements are not closed under multiplication"
            )
        Parent.__init__(self, facade=supergroup, category=OwnedFiniteGroups())

    def supergroup(self):
        return self._supergroup

    def __contains__(self, element) -> bool:
        return element in self._element_set

    def _element_constructor_(self, element):
        element = self._supergroup(element)
        if element not in self:
            raise ValueError("the element is outside this finite subgroup")
        return element

    def __iter__(self):
        return iter(self._elements)

    def one(self):
        return self._supergroup.one()

    def order(self):
        from sage.rings.integer_ring import ZZ

        return ZZ(len(self._elements))

    cardinality = order

    def group_generators(self):

        return finite_ordered_filter(
            finite_ordered_set(self),
            lambda element: element != self.one(),
        )

    def _repr_(self) -> str:
        return f"{self._description} in {self._supergroup}"


class FiniteElementConjugacyClass(SageObject):
    r"""The actual conjugacy orbit of an element in a finite quotient."""

    def __init__(self, supergroup, representative) -> None:
        self._supergroup = supergroup
        self._representative = supergroup(representative)
        self._elements = frozenset(
            element * self._representative * element.inverse() for element in supergroup
        )

    def supergroup(self):
        return self._supergroup

    def representative(self):
        return self._representative

    def __contains__(self, element) -> bool:
        return element in self._elements

    def elements(self) -> tuple:
        return tuple(self._elements)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FiniteElementConjugacyClass)
            and other._supergroup is self._supergroup
            and other._elements == self._elements
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._elements))

    def _repr_(self) -> str:
        return f"Conjugacy class of {self._representative} in {self._supergroup}"


def finite_decomposition_group(quotient, prime_above) -> FiniteGaloisSubgroup:
    backend_prime = _engine_prime(prime_above)
    elements = tuple(
        automorphism
        for automorphism in quotient
        if _image_prime(backend_prime, automorphism) == backend_prime
    )
    return FiniteGaloisSubgroup(
        quotient,
        elements,
        f"Decomposition group at {prime_above}",
    )


def finite_inertia_group(quotient, prime_above) -> FiniteGaloisSubgroup:
    decomposition = finite_decomposition_group(quotient, prime_above)
    elements = tuple(
        automorphism
        for automorphism in decomposition
        if _fixes_residue_field(prime_above, automorphism)
    )
    return FiniteGaloisSubgroup(
        quotient,
        elements,
        f"Inertia group at {prime_above}",
    )


def finite_frobenius_class(
    quotient, base_prime, prime_above
) -> FiniteElementConjugacyClass:
    prime_above = _engine_prime(prime_above)
    if prime_above.ramification_index() != 1:
        raise ValueError("Frobenius is defined here only at an unramified prime")
    decomposition = finite_decomposition_group(quotient, prime_above)
    residue = prime_above.residue_field()
    residue_order = _residue_field_order(base_prime)
    field = _engine_ring(quotient.top_field())
    owned_field = quotient.top_field()
    candidates = []
    for automorphism in decomposition:
        matches = True
        for basis_element in field.maximal_order().basis():
            owned_basis = owned_field._from_engine_element(field(basis_element))
            image = automorphism(owned_basis)
            if residue(_engine_element(owned_field, image)) != residue(basis_element) ** residue_order:
                matches = False
                break
        if matches:
            candidates.append(automorphism)
    if len(candidates) != 1:
        raise ValueError(
            "the finite quotient does not determine a unique unramified Frobenius element"
        )
    return FiniteElementConjugacyClass(quotient, candidates[0])


class AbsoluteDecompositionGroup(SageObject):
    def __init__(self, supergroup, prime, prolongation: PrimeProlongation) -> None:
        if not isinstance(prolongation, PrimeProlongation):
            raise TypeError(
                "an actual decomposition group requires a chosen prime prolongation"
            )
        if prolongation.base_prime() != prime:
            raise ValueError("the prolongation lies over a different base prime")
        self._supergroup = supergroup
        self._prime = prime
        self._prolongation = prolongation

    def supergroup(self):
        return self._supergroup

    def prime(self):
        return self._prime

    def prolongation(self):
        return self._prolongation

    def image(self, quotient):
        return finite_decomposition_group(
            quotient,
            self._prolongation.at(quotient.extension_data()),
        )

    def conjugacy_class(self):
        return DecompositionGroupConjugacyClass(self._supergroup, self._prime)

    def _repr_(self) -> str:
        return f"Decomposition group at {self._prolongation} in {self._supergroup}"


class AbsoluteInertiaGroup(SageObject):
    def __init__(self, supergroup, prime, prolongation: PrimeProlongation) -> None:
        if not isinstance(prolongation, PrimeProlongation):
            raise TypeError(
                "an actual inertia group requires a chosen prime prolongation"
            )
        if prolongation.base_prime() != prime:
            raise ValueError("the prolongation lies over a different base prime")
        self._supergroup = supergroup
        self._prime = prime
        self._prolongation = prolongation

    def supergroup(self):
        return self._supergroup

    def prime(self):
        return self._prime

    def prolongation(self):
        return self._prolongation

    def image(self, quotient):
        return finite_inertia_group(
            quotient,
            self._prolongation.at(quotient.extension_data()),
        )

    def conjugacy_class(self):
        return InertiaGroupConjugacyClass(self._supergroup, self._prime)

    def _repr_(self) -> str:
        return f"Inertia group at {self._prolongation} in {self._supergroup}"


class DecompositionGroupConjugacyClass(SageObject):
    def __init__(self, supergroup, prime) -> None:
        self._supergroup = supergroup
        self._prime = prime

    def supergroup(self):
        return self._supergroup

    def prime(self):
        return self._prime

    def representative(self, prolongation):
        return self._supergroup.decomposition_group(
            self._prime,
            prolongation=prolongation,
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, DecompositionGroupConjugacyClass)
            and other._supergroup is self._supergroup
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._prime, "decomposition"))

    def _repr_(self) -> str:
        return f"Conjugacy class of decomposition groups at {self._prime} in {self._supergroup}"


class InertiaGroupConjugacyClass(SageObject):
    def __init__(self, supergroup, prime) -> None:
        self._supergroup = supergroup
        self._prime = prime

    def supergroup(self):
        return self._supergroup

    def prime(self):
        return self._prime

    def representative(self, prolongation):
        return self._supergroup.inertia_group(
            self._prime,
            prolongation=prolongation,
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, InertiaGroupConjugacyClass)
            and other._supergroup is self._supergroup
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._prime, "inertia"))

    def _repr_(self) -> str:
        return f"Conjugacy class of inertia groups at {self._prime} in {self._supergroup}"


class FrobeniusConjugacyClass(SageObject):
    r"""The canonical global Frobenius class at an unramified base prime."""

    def __init__(self, supergroup, prime) -> None:
        self._supergroup = supergroup
        self._prime = prime

    def supergroup(self):
        return self._supergroup

    def prime(self):
        return self._prime

    def image(self, quotient, prime_above):
        return finite_frobenius_class(quotient, self._prime, prime_above)

    def conjugacy_class(self):
        return self

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FrobeniusConjugacyClass)
            and other._supergroup is self._supergroup
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._prime, "frobenius"))

    def _repr_(self) -> str:
        return f"Frobenius conjugacy class at {self._prime} in {self._supergroup}"


__all__ = [
    "AbsoluteDecompositionGroup",
    "AbsoluteInertiaGroup",
    "DecompositionGroupConjugacyClass",
    "FiniteElementConjugacyClass",
    "FiniteGaloisSubgroup",
    "FrobeniusConjugacyClass",
    "InertiaGroupConjugacyClass",
    "PrimeProlongation",
    "finite_decomposition_group",
    "finite_frobenius_class",
    "finite_inertia_group",
]
