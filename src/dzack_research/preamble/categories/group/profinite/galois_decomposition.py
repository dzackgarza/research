r"""Decomposition, inertia, and Frobenius projections of (G_K)."""

from sage.rings.integer import Integer
from sage.rings.integer_ring import ZZ

from dzack_research.preamble.categories.abstract_categories.cat import Cat
from dzack_research.preamble.categories.abstract_categories.objects import Objects
from dzack_research.preamble.categories.group.groups import OwnedGroups, Subgroups
from dzack_research.preamble.categories.group.predicate_subgroups import (
    PredicateSubgroups,
    StabilizerSubgroups,
)
from dzack_research.preamble.categories.group.profinite.profinite_groups import (
    ProfiniteGroups,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _own_ring,
)
from dzack_research.preamble.categories.sets.set_categories import Set, Sets
from dzack_research.preamble.owned_category import _object_of


class _PrimeProlongationEngine:
    r"""A coherent finite-stage oracle for a chosen prolongation (\bar v)."""

    def __init__(self, base_prime, at_stage, **rest) -> None:
        if not callable(at_stage):
            raise TypeError("a prolongation must supply a finite-stage prime function")
        self._base_prime = base_prime
        self._at_stage = at_stage
        super().__init__(**rest)

    def base_prime(self):
        return self._base_prime

    def at(self, extension):
        prime = self._at_stage(extension)
        if prime is None:
            raise ValueError("the prolongation supplies no prime at this finite stage")
        return prime

    def _repr_(self) -> str:
        return f"Chosen prolongation of {self._base_prime}"


def PrimeProlongation(base_prime, at_stage):
    r"""Construct a chosen prime prolongation as represented mathematical data."""
    return _object_of(
        Objects(),
        _engine=(Objects(), _PrimeProlongationEngine, None),
        base_prime=base_prime,
        at_stage=at_stage,
    )


def _image_prime(prime, automorphism):
    r"""``sigma(P)``, the image of a number-field prime under an exact automorphism."""
    return prime.image_under_fraction_field_automorphism(automorphism.action())


def _fixes_residue_field(prime, automorphism) -> bool:
    r"""Whether ``sigma`` acts trivially on ``O_L / P``, read on a basis of ``O_L``."""
    owned_field = automorphism.parent().top_field()
    order = owned_field.ring_of_integers()
    return all(
        prime.congruent(
            order(automorphism(owned_field(basis_element))),
            basis_element,
        )
        for basis_element in order.integral_basis()
    )


def _residue_field_order(base_prime):
    r"""``|O_K / p|``: the prime itself for a rational prime, else the absolute norm.

    Engine adapter: a rational prime is written as a Python or Sage integer
    or as an owned integer; a prime ideal of ``O_K`` has absolute norm
    ``|O_K / p|``.
    """
    integers = _own_ring(ZZ)
    match base_prime:
        case int() | Integer():
            return abs(ZZ(base_prime))
        case _ if base_prime in integers:
            return abs(ZZ(int(base_prime)))
        case _:
            return abs(ZZ(int(base_prime.residue_cardinality())))


def FiniteGaloisSubgroup(supergroup, elements, description):
    r"""The subgroup of the finite group ``supergroup`` whose elements are ``elements``.

    The element set is checked to contain the identity and to be closed under
    the law, which makes it a subgroup of a finite group; the subgroup is the
    predicate subgroup cut out by membership in that set.
    """
    element_set = frozenset(elements)
    assert all(element in supergroup for element in element_set), (
        "the selected subgroup elements belong to the containing group"
    )
    assert supergroup.one() in element_set, "a represented subgroup contains the identity"
    assert all(left * right in element_set for left in element_set for right in element_set), (
        "the selected finite elements are closed under multiplication"
    )
    return PredicateSubgroups(supergroup)(lambda element: element in element_set, description)


def FiniteElementConjugacyClass(supergroup, representative):
    r"""Return the actual conjugacy orbit of ``representative`` in a finite group."""
    return supergroup.conjugacy_class(representative)



def _finite_decomposition_group(quotient, prime_above):
    r"""``D_P = {sigma in Gal(L/K) : sigma(P) = P}``, the stabilizer of ``P``."""
    return StabilizerSubgroups(quotient)(
        prime_above,
        "prime ideal",
        lambda automorphism: _image_prime(prime_above, automorphism) == prime_above,
        description=f"Decomposition group at {prime_above}",
    )


def _finite_inertia_group(quotient, prime_above):
    r"""``I_P``: the elements of ``D_P`` acting trivially on the residue field ``O_L / P``."""
    decomposition = quotient.decomposition_group(prime_above)
    return PredicateSubgroups(quotient)(
        lambda automorphism: automorphism in decomposition and _fixes_residue_field(prime_above, automorphism),
        f"Inertia group at {prime_above}",
    )


def _finite_frobenius_class(quotient, base_prime, prime_above):
    r"""The Frobenius class at an unramified ``P``: the ``sigma in D_P`` with ``sigma(x) = x^q`` mod ``P``."""
    assert quotient.inertia_group(prime_above).cardinality() == 1, "Frobenius is defined here only at a relatively unramified prime"
    residue_order = _residue_field_order(base_prime)
    owned_field = quotient.top_field()
    order = owned_field.ring_of_integers()

    def acts_as_frobenius(automorphism) -> bool:
        return all(
            prime_above.congruent(
                order(automorphism(owned_field(basis_element))),
                order(owned_field(basis_element) ** int(residue_order)),
            )
            for basis_element in order.integral_basis()
        )

    candidates = tuple(
        automorphism for automorphism in quotient.decomposition_group(prime_above) if acts_as_frobenius(automorphism)
    )
    assert len(candidates) == 1, (
        "at an unramified prime the finite quotient has exactly one Frobenius element"
    )
    return FiniteElementConjugacyClass(quotient, candidates[0])


class _AbsoluteDecompositionGroupEngine:
    r"""Finite-quotient realization of the decomposition subgroup at ``prolongation``."""

    def __init__(self, prime, prolongation, **rest) -> None:
        if prolongation.base_prime() != prime:
            raise ValueError("the prolongation lies over a different base prime")
        self._prime = prime
        self._prolongation = prolongation
        super().__init__(**rest)

    def ambient(self):
        r"""Return the ambient absolute Galois group."""
        return self.supergroup()

    def prime(self):
        return self._prime

    def prolongation(self):
        return self._prolongation

    def image(self, quotient):
        return quotient.decomposition_group(
            self._prolongation.at(quotient.extension_data())
        )

    def conjugacy_class(self):
        return DecompositionGroupConjugacyClass(self.supergroup(), self._prime)

    def one(self):
        return self.supergroup().one()

    def __contains__(self, element) -> bool:
        ambient = self.supergroup()
        if element not in ambient:
            return False
        if element == ambient.one():
            return True
        assert False, (
            "membership in an absolute decomposition subgroup is the compatible "
            "stabilizer condition over every finite quotient; finitely many realized "
            "coordinates do not decide it"
        )

    def _element_constructor_(self, datum):
        ambient = self.supergroup()
        element = datum if datum in ambient else ambient(datum)
        if element == ambient.one():
            return element
        assert False, (
            "constructing a nonidentity element of an absolute decomposition subgroup "
            "requires a complete compatible prolongation-stabilizer witness"
        )

    def _repr_(self) -> str:
        return f"Decomposition group at {self._prolongation} in {self.supergroup()}"


def AbsoluteDecompositionGroup(supergroup, prime, prolongation):
    r"""Construct the profinite subgroup ``D_pbar <= G_K`` from its finite images."""
    return _object_of(
        Cat().meet((ProfiniteGroups(), Subgroups(supergroup))),
        _engine=(OwnedGroups(), _AbsoluteDecompositionGroupEngine, None),
        supergroup=supergroup,
        prime=prime,
        prolongation=prolongation,
    )


class _AbsoluteInertiaGroupEngine:
    r"""Finite-quotient realization of the inertia subgroup at ``prolongation``."""

    def __init__(self, prime, prolongation, **rest) -> None:
        if prolongation.base_prime() != prime:
            raise ValueError("the prolongation lies over a different base prime")
        self._prime = prime
        self._prolongation = prolongation
        super().__init__(**rest)

    def ambient(self):
        r"""Return the ambient absolute Galois group."""
        return self.supergroup()

    def prime(self):
        return self._prime

    def prolongation(self):
        return self._prolongation

    def image(self, quotient):
        return quotient.inertia_group(
            self._prolongation.at(quotient.extension_data())
        )

    def conjugacy_class(self):
        return InertiaGroupConjugacyClass(self.supergroup(), self._prime)

    def one(self):
        return self.supergroup().one()

    def __contains__(self, element) -> bool:
        ambient = self.supergroup()
        if element not in ambient:
            return False
        if element == ambient.one():
            return True
        assert False, (
            "membership in an absolute inertia subgroup is the compatible residue-"
            "triviality condition over every finite quotient; finitely many realized "
            "coordinates do not decide it"
        )

    def _element_constructor_(self, datum):
        ambient = self.supergroup()
        element = datum if datum in ambient else ambient(datum)
        if element == ambient.one():
            return element
        assert False, (
            "constructing a nonidentity element of an absolute inertia subgroup "
            "requires a complete compatible inertia witness"
        )

    def _repr_(self) -> str:
        return f"Inertia group at {self._prolongation} in {self.supergroup()}"


def AbsoluteInertiaGroup(supergroup, prime, prolongation):
    r"""Construct the profinite subgroup ``I_pbar <= G_K`` from its finite images."""
    return _object_of(
        Cat().meet((ProfiniteGroups(), Subgroups(supergroup))),
        _engine=(OwnedGroups(), _AbsoluteInertiaGroupEngine, None),
        supergroup=supergroup,
        prime=prime,
        prolongation=prolongation,
    )


class _DecompositionGroupConjugacyClassEngine:
    def __init__(self, supergroup, prime, **rest) -> None:
        self._supergroup = supergroup
        self._prime = prime
        super().__init__(**rest)

    def supergroup(self):
        return self._supergroup

    def ambient(self):
        r"""Return the ambient absolute Galois group."""
        return self.supergroup()

    def prime(self):
        return self._prime

    def representative(self, prolongation):
        return self._supergroup.decomposition_group(
            self._prime,
            prolongation=prolongation,
        )

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, _AbsoluteDecompositionGroupEngine)
            and candidate.supergroup() is self._supergroup
            and candidate.prime() == self._prime
        )

    def _element_constructor_(self, candidate):
        if candidate not in self:
            raise ValueError(
                "the subgroup is not in this decomposition-group conjugacy class"
            )
        return candidate

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _DecompositionGroupConjugacyClassEngine)
            and other._supergroup is self._supergroup
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._prime, "decomposition"))

    def _repr_(self) -> str:
        return f"Conjugacy class of decomposition groups at {self._prime} in {self._supergroup}"


def DecompositionGroupConjugacyClass(supergroup, prime):
    r"""Construct the conjugacy class of decomposition subgroups as a set."""
    return _object_of(
        Sets(),
        _engine=(Sets(), _DecompositionGroupConjugacyClassEngine, None),
        supergroup=supergroup,
        prime=prime,
    )


class _InertiaGroupConjugacyClassEngine:
    def __init__(self, supergroup, prime, **rest) -> None:
        self._supergroup = supergroup
        self._prime = prime
        super().__init__(**rest)

    def supergroup(self):
        return self._supergroup

    def ambient(self):
        r"""Return the ambient absolute Galois group."""
        return self.supergroup()

    def prime(self):
        return self._prime

    def representative(self, prolongation):
        return self._supergroup.inertia_group(
            self._prime,
            prolongation=prolongation,
        )

    def __contains__(self, candidate) -> bool:
        return (
            isinstance(candidate, _AbsoluteInertiaGroupEngine)
            and candidate.supergroup() is self._supergroup
            and candidate.prime() == self._prime
        )

    def _element_constructor_(self, candidate):
        if candidate not in self:
            raise ValueError(
                "the subgroup is not in this inertia-group conjugacy class"
            )
        return candidate

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _InertiaGroupConjugacyClassEngine)
            and other._supergroup is self._supergroup
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._prime, "inertia"))

    def _repr_(self) -> str:
        return f"Conjugacy class of inertia groups at {self._prime} in {self._supergroup}"


def InertiaGroupConjugacyClass(supergroup, prime):
    r"""Construct the conjugacy class of inertia subgroups as a set."""
    return _object_of(
        Sets(),
        _engine=(Sets(), _InertiaGroupConjugacyClassEngine, None),
        supergroup=supergroup,
        prime=prime,
    )


class _FrobeniusConjugacyClassEngine:
    r"""The canonical global Frobenius class at an unramified base prime."""

    def __init__(self, supergroup, prime, **rest) -> None:
        self._supergroup = supergroup
        self._prime = prime
        super().__init__(**rest)

    def supergroup(self):
        return self._supergroup

    def ambient(self):
        r"""Return the ambient absolute Galois group."""
        return self.supergroup()

    def prime(self):
        return self._prime

    def image(self, quotient, prime_above):
        return quotient.frobenius_class(self._prime, prime_above)

    def conjugacy_class(self):
        return self

    def __eq__(self, other) -> bool:
        return (
            isinstance(other, _FrobeniusConjugacyClassEngine)
            and other._supergroup is self._supergroup
            and other._prime == self._prime
        )

    def __hash__(self) -> int:
        return hash((id(self._supergroup), self._prime, "frobenius"))

    def _repr_(self) -> str:
        return f"Frobenius conjugacy class at {self._prime} in {self._supergroup}"


def FrobeniusConjugacyClass(supergroup, prime):
    r"""Construct the choice-independent global Frobenius datum."""
    return _object_of(
        Objects(),
        _engine=(Objects(), _FrobeniusConjugacyClassEngine, None),
        supergroup=supergroup,
        prime=prime,
    )


__all__ = [
    "AbsoluteDecompositionGroup",
    "AbsoluteInertiaGroup",
    "DecompositionGroupConjugacyClass",
    "FiniteElementConjugacyClass",
    "FiniteGaloisSubgroup",
    "FrobeniusConjugacyClass",
    "InertiaGroupConjugacyClass",
    "PrimeProlongation",
]
