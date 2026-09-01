r"""Decomposition, inertia, and Frobenius projections of (G_K)."""

from sage.structure.parent import Parent
from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.groups import OwnedFiniteGroups
from dzack_research.preamble.categories.rings.rings import engine_ring


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


def _image_prime(prime, automorphism):
    backend = automorphism.action().engine_morphism()
    try:
        return prime.apply_morphism(backend)
    except AttributeError:
        field = engine_ring(automorphism.parent().top_field())
        return field.ideal([backend(generator) for generator in prime.gens()])


def _fixes_residue_field(prime, automorphism) -> bool:
    residue = prime.residue_field()
    field = engine_ring(automorphism.parent().top_field())
    order = field.maximal_order()
    return all(
        residue(automorphism(basis_element)) == residue(basis_element)
        for basis_element in order.basis()
    )


def _residue_field_order(base_prime):
    from sage.rings.integer_ring import ZZ

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

    def __init__(self, ambient, elements, description) -> None:
        self._ambient = ambient
        self._elements = tuple(elements)
        self._element_set = frozenset(self._elements)
        self._description = description
        if ambient.one() not in self._element_set:
            raise ValueError("a represented subgroup must contain the identity")
        if any(
            left * right not in self._element_set
            for left in self._elements
            for right in self._elements
        ):
            raise ValueError(
                "the selected finite elements are not closed under multiplication"
            )
        Parent.__init__(self, facade=ambient, category=OwnedFiniteGroups())

    def ambient(self):
        return self._ambient

    supergroup = ambient

    def __contains__(self, element) -> bool:
        return element in self._element_set

    def _element_constructor_(self, element):
        element = self._ambient(element)
        if element not in self:
            raise ValueError("the element is outside this finite subgroup")
        return element

    def __iter__(self):
        return iter(self._elements)

    def one(self):
        return self._ambient.one()

    def order(self):
        from sage.rings.integer_ring import ZZ

        return ZZ(len(self._elements))

    cardinality = order

    def group_generators(self):
        from dzack_research.preamble.categories.sets import finite_ordered_set

        return finite_ordered_set(element for element in self if element != self.one())

    gens = group_generators

    def _repr_(self) -> str:
        return f"{self._description} in {self._ambient}"


class FiniteElementConjugacyClass(SageObject):
    r"""The actual conjugacy orbit of an element in a finite quotient."""

    def __init__(self, ambient, representative) -> None:
        self._ambient = ambient
        self._representative = ambient(representative)
        self._elements = frozenset(
            element * self._representative * element.inverse() for element in ambient
        )

    def ambient(self):
        return self._ambient

    def representative(self):
        return self._representative

    def __contains__(self, element) -> bool:
        return element in self._elements

    def elements(self) -> tuple:
        return tuple(self._elements)

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FiniteElementConjugacyClass)
            and other._ambient is self._ambient
            and other._elements == self._elements
        )

    def __hash__(self) -> int:
        return hash((id(self._ambient), self._elements))

    def _repr_(self) -> str:
        return f"Conjugacy class of {self._representative} in {self._ambient}"


def finite_decomposition_group(quotient, prime_above) -> FiniteGaloisSubgroup:
    elements = tuple(
        automorphism
        for automorphism in quotient
        if _image_prime(prime_above, automorphism) == prime_above
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
    if prime_above.ramification_index() != 1:
        raise ValueError("Frobenius is defined here only at an unramified prime")
    decomposition = finite_decomposition_group(quotient, prime_above)
    residue = prime_above.residue_field()
    residue_order = _residue_field_order(base_prime)
    field = engine_ring(quotient.top_field())
    candidates = [
        automorphism
        for automorphism in decomposition
        if all(
            residue(automorphism(basis_element))
            == residue(basis_element) ** residue_order
            for basis_element in field.maximal_order().basis()
        )
    ]
    if len(candidates) != 1:
        raise ValueError(
            "the finite quotient does not determine a unique unramified Frobenius element"
        )
    return FiniteElementConjugacyClass(quotient, candidates[0])


class AbsoluteDecompositionGroup(SageObject):
    def __init__(self, ambient, prime, prolongation: PrimeProlongation) -> None:
        if not isinstance(prolongation, PrimeProlongation):
            raise TypeError(
                "an actual decomposition group requires a chosen prime prolongation"
            )
        if prolongation.base_prime() != prime:
            raise ValueError("the prolongation lies over a different base prime")
        self._ambient = ambient
        self._prime = prime
        self._prolongation = prolongation

    def ambient(self):
        return self._ambient

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
        return DecompositionGroupConjugacyClass(self._ambient, self._prime)

    def _repr_(self) -> str:
        return f"Decomposition group at {self._prolongation} in {self._ambient}"


class AbsoluteInertiaGroup(SageObject):
    def __init__(self, ambient, prime, prolongation: PrimeProlongation) -> None:
        if not isinstance(prolongation, PrimeProlongation):
            raise TypeError(
                "an actual inertia group requires a chosen prime prolongation"
            )
        if prolongation.base_prime() != prime:
            raise ValueError("the prolongation lies over a different base prime")
        self._ambient = ambient
        self._prime = prime
        self._prolongation = prolongation

    def ambient(self):
        return self._ambient

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
        return InertiaGroupConjugacyClass(self._ambient, self._prime)

    def _repr_(self) -> str:
        return f"Inertia group at {self._prolongation} in {self._ambient}"


class DecompositionGroupConjugacyClass(SageObject):
    def __init__(self, ambient, prime) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self):
        return self._ambient

    def prime(self):
        return self._prime

    def representative(self, prolongation):
        return self._ambient.decomposition_group(
            self._prime,
            prolongation=prolongation,
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, DecompositionGroupConjugacyClass)
            and other._ambient is self._ambient
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._ambient), self._prime, "decomposition"))

    def _repr_(self) -> str:
        return f"Conjugacy class of decomposition groups at {self._prime} in {self._ambient}"


class InertiaGroupConjugacyClass(SageObject):
    def __init__(self, ambient, prime) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self):
        return self._ambient

    def prime(self):
        return self._prime

    def representative(self, prolongation):
        return self._ambient.inertia_group(
            self._prime,
            prolongation=prolongation,
        )

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, InertiaGroupConjugacyClass)
            and other._ambient is self._ambient
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._ambient), self._prime, "inertia"))

    def _repr_(self) -> str:
        return f"Conjugacy class of inertia groups at {self._prime} in {self._ambient}"


class FrobeniusConjugacyClass(SageObject):
    r"""The canonical global Frobenius class at an unramified base prime."""

    def __init__(self, ambient, prime) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self):
        return self._ambient

    def prime(self):
        return self._prime

    def image(self, quotient, prime_above):
        return finite_frobenius_class(quotient, self._prime, prime_above)

    def conjugacy_class(self):
        return self

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, FrobeniusConjugacyClass)
            and other._ambient is self._ambient
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._ambient), self._prime, "frobenius"))

    def _repr_(self) -> str:
        return f"Frobenius conjugacy class at {self._prime} in {self._ambient}"


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
