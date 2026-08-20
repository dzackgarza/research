r"""Decomposition, inertia, and Frobenius objects for \(G_K\).

For a number field \(K\) and a place \(v\), the chosen realization
\(\iota:K\hookrightarrow\bar K\) gives a prolongation \(\bar v\) of \(v\)
to \(\bar K\) (chosen by the parent's :class:`GaloisChoicePolicy`).  Then
\(D_{\bar v}\subseteq G_K\) and \(I_{\bar v}\subseteq D_{\bar v}\) are
actual subgroups, and the Frobenius is an actual conjugacy class in the
finite quotient.

The choice-independent invariants are available as ``_class``
variants::

    G.decomposition_group(v)        # chosen prolongation vbar
    G.decomposition_group_class(v)  # canonical conjugacy class

    G.inertia_group(v)
    G.inertia_group_class(v)

    G.frobenius(v)                  # choices made
    G.frobenius_class(v)            # canonical finite-level class

and each chosen object carries ``.conjugacy_class()`` returning its
invariant projection.

These objects need not be concretely enumerable.  Instead they project
into every finite Galois quotient, delegating to Sage's existing
finite-level ``decomposition_group``, ``inertia_group``, and
``artin_symbol``.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import Parent
    from sage.structure.parent import MembershipInput

from sage.structure.sage_object import SageObject

if TYPE_CHECKING:
    # A place of \(K\) is a prime of \(O_K\); a finite quotient of \(G_K\)
    # is one of Sage's finite Galois groups, and it is there that
    # decomposition, inertia and the Artin symbol are computed.
    from sage.rings.number_field.galois_group import (
        GaloisGroup_subgroup,
        GaloisGroup_v2,
        GaloisGroupElement,
    )
    from sage.rings.number_field.number_field_ideal import NumberFieldFractionalIdeal


class AbsoluteDecompositionGroup(SageObject):
    r"""The decomposition group \(D_{\bar v}\subseteq G_K\) at a chosen prolongation of ``prime``.

    Not concretely enumerable; it projects into every finite Galois
    quotient where the implementation delegates to Sage's existing
    finite-level ``decomposition_group``.
    """

    def __init__(
        self, ambient: "Parent", prime: "NumberFieldFractionalIdeal"
    ) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self) -> "Parent":
        return self._ambient

    def prime(self) -> "NumberFieldFractionalIdeal":
        return self._prime

    def image(
        self, quotient: "GaloisGroup_v2", prime_ideal: "NumberFieldFractionalIdeal"
    ) -> "GaloisGroup_subgroup":
        r"""Return the image of \(D_{\bar v}\) in the finite quotient ``quotient``."""
        return quotient.decomposition_group(prime_ideal)

    def conjugacy_class(self) -> "DecompositionGroupConjugacyClass":
        r"""Return the conjugacy class of this decomposition group, forgetting the prolongation."""
        return DecompositionGroupConjugacyClass(self._ambient, self._prime)

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._prime))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._prime == other._prime
        )

    def _repr_(self) -> str:
        return f"Decomposition group at {self._prime} in {self._ambient}"


class AbsoluteInertiaGroup(SageObject):
    r"""The inertia group \(I_{\bar v}\subseteq G_K\) at a chosen prolongation of ``prime``."""

    def __init__(
        self, ambient: "Parent", prime: "NumberFieldFractionalIdeal"
    ) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self) -> "Parent":
        return self._ambient

    def prime(self) -> "NumberFieldFractionalIdeal":
        return self._prime

    def image(
        self, quotient: "GaloisGroup_v2", prime_ideal: "NumberFieldFractionalIdeal"
    ) -> "GaloisGroup_subgroup":
        r"""Return the image of \(I_{\bar v}\) in the finite quotient ``quotient``."""
        return quotient.inertia_group(prime_ideal)

    def conjugacy_class(self) -> "InertiaGroupConjugacyClass":
        r"""Return the conjugacy class of this inertia group, forgetting the prolongation."""
        return InertiaGroupConjugacyClass(self._ambient, self._prime)

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._prime))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._prime == other._prime
        )

    def _repr_(self) -> str:
        return f"Inertia group at {self._prime} in {self._ambient}"


class FrobeniusConjugacyClass(SageObject):
    r"""The Frobenius conjugacy class at a chosen (possibly unramified) place ``prime``.

    Even with a chosen prolongation, the Frobenius is a conjugacy class
    in the finite quotient, not a distinguished global element of
    \(G_K\).  The ``_class`` variant forgets the prolongation choice.
    """

    def __init__(
        self, ambient: "Parent", prime: "NumberFieldFractionalIdeal"
    ) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self) -> "Parent":
        return self._ambient

    def prime(self) -> "NumberFieldFractionalIdeal":
        return self._prime

    def image(
        self, quotient: "GaloisGroup_v2", prime_ideal: "NumberFieldFractionalIdeal"
    ) -> "GaloisGroupElement":
        r"""Return the image (the Artin symbol) in the finite quotient ``quotient``."""
        return quotient.artin_symbol(prime_ideal)

    def conjugacy_class(self) -> "FrobeniusConjugacyClass":
        r"""Return self; the Frobenius is already a conjugacy class."""
        return self

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._prime))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._prime == other._prime
        )

    def _repr_(self) -> str:
        return f"Frobenius conjugacy class at {self._prime} in {self._ambient}"


class DecompositionGroupConjugacyClass(SageObject):
    r"""The conjugacy class of decomposition groups at ``prime``, forgetting the prolongation."""

    def __init__(
        self, ambient: "Parent", prime: "NumberFieldFractionalIdeal"
    ) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self) -> "Parent":
        return self._ambient

    def prime(self) -> "NumberFieldFractionalIdeal":
        return self._prime

    def representative(self) -> "AbsoluteDecompositionGroup":
        chosen: "AbsoluteDecompositionGroup" = self._ambient.decomposition_group(
            self._prime
        )
        return chosen

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._prime))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._prime == other._prime
        )

    def _repr_(self) -> str:
        return f"Conjugacy class of decomposition groups at {self._prime} in {self._ambient}"


class InertiaGroupConjugacyClass(SageObject):
    r"""The conjugacy class of inertia groups at ``prime``, forgetting the prolongation."""

    def __init__(
        self, ambient: "Parent", prime: "NumberFieldFractionalIdeal"
    ) -> None:
        self._ambient = ambient
        self._prime = prime

    def ambient(self) -> "Parent":
        return self._ambient

    def prime(self) -> "NumberFieldFractionalIdeal":
        return self._prime

    def representative(self) -> "AbsoluteInertiaGroup":
        chosen: "AbsoluteInertiaGroup" = self._ambient.inertia_group(self._prime)
        return chosen

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._prime))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._prime == other._prime
        )

    def _repr_(self) -> str:
        return f"Conjugacy class of inertia groups at {self._prime} in {self._ambient}"
