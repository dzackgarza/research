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
            raise TypeError(
                f"a prolongation of the prime {base_prime} needs a function assigning to each "
                f"finite Galois extension L/K a prime of L above {base_prime}, but {at_stage} "
                f"is not callable"
            )
        self._base_prime = base_prime
        self._at_stage = at_stage
        super().__init__(**rest)

    def base_prime(self):
        return self._base_prime

    def at(self, extension):
        prime = self._at_stage(extension)
        if prime is None:
            raise ValueError(
                f"the prolongation of {self._base_prime} gives no prime of {extension} above "
                f"{self._base_prime}"
            )
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
        f"the elements chosen for the subgroup '{description}' are not all elements of "
        f"{supergroup}"
    )
    assert supergroup.one() in element_set, (
        f"the element set chosen for '{description}' is not a subgroup of {supergroup}: "
        f"it does not contain the identity"
    )
    assert all(left * right in element_set for left in element_set for right in element_set), (
        f"the element set chosen for '{description}' is not a subgroup of {supergroup}: "
        f"it is not closed under multiplication"
    )
    return PredicateSubgroups(supergroup)(lambda element: element in element_set, description)


def FiniteElementConjugacyClass(supergroup, representative):
    r"""Return the actual conjugacy orbit of ``representative`` in a finite group."""
    return supergroup.conjugacy_class(representative)



def _finite_decomposition_group(quotient, prime_above):
    r"""``D_P = {sigma in Gal(L/K) : sigma(P) = P}``, the stabilizer of ``P``."""
    from dzack_research.preamble.categories.functors.group_actions import GroupActionFunctor
    from dzack_research.preamble.categories.sets.finite_ordered_sets import finite_ordered_set

    # The finite Galois group acts on the finite orbit of the selected prime.
    # Retain the actual action whose point stabilizer is the decomposition group.
    orbit = finite_ordered_set(
        _image_prime(prime_above, automorphism) for automorphism in quotient
    )
    action = GroupActionFunctor(
        quotient,
        Sets(),
        orbit,
        lambda automorphism: Sets().Mor(orbit, orbit)(
            lambda ideal: orbit(_image_prime(ideal, automorphism))
        ),
    )
    return StabilizerSubgroups(quotient)(
        prime_above,
        action,
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
    r"""The Frobenius class at an unramified ``P``: the class of :func:`_finite_frobenius_element`."""
    return FiniteElementConjugacyClass(
        quotient, _finite_frobenius_element(quotient, base_prime, prime_above)
    )


def _finite_frobenius_element(quotient, base_prime, prime_above):
    r"""The arithmetic Frobenius at an unramified ``P``: the ``sigma in D_P`` with ``sigma(x) = x^q`` mod ``P``.

    Definition: Mathlib ``IsArithFrobAt`` (``Mathlib/RingTheory/Frobenius.lean``,
    module docstring), ``sigma x = x^q mod P`` for every ``x`` of ``O_L``,
    ``q = |O_K/p|``; at an unramified ``P`` it is unique
    (``AlgHom.IsArithFrobAt.eq_of_isUnramifiedAt``, same file).
    """
    assert quotient.inertia_group(prime_above).cardinality() == 1, (
        f"the Frobenius at {prime_above} in {quotient} is defined only when "
        f"{prime_above} is unramified, but its inertia group is nontrivial"
    )
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
        f"at the unramified prime {prime_above}, the decomposition group in {quotient} "
        f"should hold exactly one element acting as x -> x^{residue_order} on the residue "
        f"field, but {len(candidates)} elements do"
    )
    return candidates[0]


def _stage_inclusion(smaller, larger):
    r"""The ``K``-embedding ``f: L -> L'`` of two stages inside ``Kbar``, or ``None``.

    ``L`` lies in ``L'`` inside ``Kbar`` exactly when some field map ``f``
    satisfies ``e_{L'} f = e_L`` for the retained embeddings into ``Kbar``;
    such an ``f`` is unique, since ``e_{L'}`` is injective.
    """
    for candidate in smaller.field().exact_embeddings(larger.field()):
        if (larger.embedding() * candidate == smaller.embedding()) is True:
            return candidate
    return None


def _lies_over(prime_above, inclusion, prime_below) -> bool:
    r"""Whether ``P'`` of ``O_{L'}`` lies over ``P`` of ``O_L`` along ``f: L -> L'``.

    For primes of rings of integers, ``P'`` lies over ``P`` exactly when
    ``f(P)`` is contained in ``P'``, read on the generators of ``P``.
    """
    small_field = inclusion.domain()
    large_order = prime_above.ring()
    return all(
        large_order(inclusion(small_field(generator))) in prime_above
        for generator in prime_below.ideal_generators()
    )


class _ChosenRationalProlongation:
    r"""A coherent choice of primes above a rational prime ``p`` at the stages of ``Kbar/QQ``.

    The chosen prime at a stage ``L`` is the contraction of a prime already
    chosen at a stage containing ``L``.  Otherwise it is the first prime of
    ``L`` above ``p``, in the order of ``L.primes_above(p)``, that lies over
    the primes already chosen at the stages contained in ``L``.  Each
    recorded prime is fixed once chosen, and every recorded pair lies over
    every smaller recorded pair, so the choices are the restrictions of one
    prime of ``Kbar`` above ``p``.  The family is a datum of this object, and
    which stages it has fixed depends on which stages it was asked about.
    """

    def __init__(self, rational_prime) -> None:
        self._rational_prime = rational_prime
        self._chosen = []

    def __call__(self, stage):
        for recorded_stage, recorded_prime in self._chosen:
            inclusion = _stage_inclusion(stage, recorded_stage)
            if inclusion is not None:
                return self._contraction(stage, inclusion, recorded_prime)
        smaller = tuple(
            (inclusion, recorded_prime)
            for recorded_stage, recorded_prime in self._chosen
            if (inclusion := _stage_inclusion(recorded_stage, stage)) is not None
        )
        prime = next(
            (
                candidate
                for candidate in stage.field().primes_above(int(self._rational_prime))
                if all(
                    _lies_over(candidate, inclusion, recorded_prime)
                    for inclusion, recorded_prime in smaller
                )
            ),
            None,
        )
        assert prime is not None, (
            f"no prime of {stage.field()} above {self._rational_prime} lies over the "
            f"primes already chosen at the smaller stages"
        )
        self._chosen.append((stage, prime))
        return prime

    def _contraction(self, stage, inclusion, prime_above):
        return next(
            candidate
            for candidate in stage.field().primes_above(int(self._rational_prime))
            if _lies_over(prime_above, inclusion, candidate)
        )


def _chosen_rational_prolongation(rational_prime):
    r"""Construct a coherent chosen prolongation of the rational prime ``p`` to ``Kbar``."""
    return PrimeProlongation(rational_prime, _ChosenRationalProlongation(rational_prime))


class _AbsoluteDecompositionGroupEngine:
    r"""Finite-quotient realization of the decomposition subgroup at ``prolongation``."""

    def __init__(self, prime, prolongation, **rest) -> None:
        if prolongation.base_prime() != prime:
            raise ValueError(
                f"the prolongation {prolongation} lies over {prolongation.base_prime()}, "
                f"not over the prime {prime}"
            )
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
            f"cannot decide whether {element} lies in the decomposition group {self}: "
            f"membership means fixing the prime in every finite Galois quotient, which "
            f"is known only for the identity"
        )

    def _element_constructor_(self, datum):
        ambient = self.supergroup()
        element = datum if datum in ambient else ambient(datum)
        if element == ambient.one():
            return element
        assert False, (
            f"cannot make {element} an element of the decomposition group {self}: only the "
            f"identity is known to fix the prime in every finite Galois quotient"
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
            raise ValueError(
                f"the prolongation {prolongation} lies over {prolongation.base_prime()}, "
                f"not over the prime {prime}"
            )
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
            f"cannot decide whether {element} lies in the inertia group {self}: membership "
            f"means acting trivially on the residue field in every finite Galois "
            f"quotient, which is known only for the identity"
        )

    def _element_constructor_(self, datum):
        ambient = self.supergroup()
        element = datum if datum in ambient else ambient(datum)
        if element == ambient.one():
            return element
        assert False, (
            f"cannot make {element} an element of the inertia group {self}: only the "
            f"identity is known to act trivially on the residue field in every finite "
            f"Galois quotient"
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
                f"{candidate} is not a decomposition group at {self._prime} in "
                f"{self._supergroup}"
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
                f"{candidate} is not an inertia group at {self._prime} in "
                f"{self._supergroup}"
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

    def representative(self):
        r"""The Frobenius element at the group's chosen prolongation of this prime."""
        return self._supergroup.frobenius(self._prime)

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
