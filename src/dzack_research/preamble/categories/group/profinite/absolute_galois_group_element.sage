r"""Elements of \(G_K\) as lazy automorphisms of \(\bar K\).

An element of \(G_K=\operatorname{Aut}_K(\bar K)\) is a field
automorphism of \(\bar K\) fixing \(K\).  Specifying it on every
\(\alpha\in\bar K\) at construction time is impossible; instead, a lift
from a finite quotient is realized lazily.

Suppose \(g\) currently knows its action on a finite normal field
\(L\subset\bar K\).  The user asks ``g(alpha)`` for some
\(\alpha\in\bar K\).  Form a finite normal extension \(M/K\) with
\(L(\alpha)\subset M\subset\bar K\).  Extend \(g|_L\) to an automorphism
of \(M\), choosing one of the finitely many possibilities via the
parent's :class:`GaloisChoicePolicy`, and cache that extension.  The
existence of such an extension is guaranteed by the
normal-extension theorem (Stacks 0BME).
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput

from sage.categories.fields import Fields as SageFields
from sage.categories.homset import Hom
from sage.categories.morphism import Morphism
from sage.structure.element import Element

from dzack_research.preamble.categories.group.profinite.galois_quotient import (
    extensions_along,
    restrict_along,
)

if TYPE_CHECKING:
    from sage.categories.rings import Ring


class AbsoluteGaloisGroupElement(Morphism):
    r"""A lazy automorphism of \(\bar K\) fixing \(K\), an element of \(G_K\).

    Constructed by :meth:`AbsoluteGaloisGroup.lift` from a finite-level
    automorphism.  Its action on \(\bar K\) is realized progressively:
    each evaluation on a new \(\alpha\in\bar K\) forces the automorphism
    to extend to a finite normal field containing \(\alpha\), caching
    the extension.
    """

    def __init__(
        self, parent: "AbsoluteGaloisGroup", stage: "Ring", action: Morphism
    ) -> None:
        r"""Initialize from a finite stage and a finite-level automorphism.

        ``stage`` is a finite Galois extension \(L/K\subset\bar K\).
        ``action`` is an automorphism of ``stage`` over \(K\).
        """
        closure = parent.algebraic_closure()
        Morphism.__init__(self, Hom(closure, closure, SageFields()))
        self._parent = parent
        self._stage = stage
        self._action = action

    def parent(self) -> "AbsoluteGaloisGroup":
        return self._parent

    def stage(self) -> "Ring":
        r"""Return the finite Galois field on which this automorphism is currently realized."""
        return self._stage

    def action(self) -> Morphism:
        r"""Return the finite-level automorphism of :meth:`stage`."""
        return self._action

    def _call_(self, alpha: Element) -> Element:
        r"""Evaluate this automorphism on \(\alpha\in\bar K\), extending lazily.

        If \(\alpha\) lies in the current stage, the cached action
        applies.  Otherwise, form a finite normal extension \(M/K\)
        containing \(\alpha\), extend the action to \(M\) via the
        parent's choice policy, cache, and return.
        """
        if alpha in self._stage:
            known: Element = self._action(alpha)
            return known

        # Force: build M = normal closure of stage(alpha) over K inside bar K
        M = self._parent._normal_closure_containing(self._stage, alpha)
        policy = self._parent.choice_policy()
        embedding = policy.choose_embedding(self._stage, M)
        candidates = [sigma.as_hom() for sigma in self._parent.finite_quotient(M)]
        extensions = extensions_along(self._action, embedding, candidates)
        extension = policy.choose_extension(self._action, extensions)
        self._stage = M
        self._action = extension
        image: Element = extension(alpha)
        return image

    def restrict(self, L: "Ring") -> Morphism:
        r"""Return the restriction of this automorphism to a subfield \(L\) of the current stage.

        The subfield is presented by an embedding \(L\hookrightarrow\)
        stage chosen by the parent's :class:`GaloisChoicePolicy`;
        different embeddings give restrictions that differ by
        conjugation, which is why the choice is the policy's to make.
        """
        embedding = self._parent.choice_policy().choose_embedding(L, self._stage)
        restriction: Morphism = restrict_along(self._action, embedding)
        return restriction

    def conjugacy_class(self) -> "ElementConjugacyClass":
        r"""Return the conjugacy class of this element in \(G_K\)."""
        return ElementConjugacyClass(self._parent, self)

    def _repr_(self) -> str:
        return f"Element of {self._parent} (realized on {self._stage})"

    def __hash__(self) -> int:
        return hash((type(self), self._parent, self._stage, self._action))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            type(other) is type(self)
            and self._parent == other._parent
            and self._stage == other._stage
            and self._action == other._action
        )


class ElementConjugacyClass:
    r"""The conjugacy class of an element of \(G_K\).

    Choice-independent: the conjugacy class does not depend on the
    realization choices that produced the representative.
    """

    def __init__(
        self,
        ambient: "AbsoluteGaloisGroup",
        representative: "AbsoluteGaloisGroupElement",
    ) -> None:
        self._ambient = ambient
        self._representative = representative

    def ambient(self) -> "AbsoluteGaloisGroup":
        return self._ambient

    def representative(self) -> "AbsoluteGaloisGroupElement":
        return self._representative

    def __hash__(self) -> int:
        return hash((type(self), self._ambient))

    def __eq__(self, other: "MembershipInput") -> bool:
        return type(other) is type(self) and self._ambient == other._ambient

    def _repr_(self) -> str:
        return f"Conjugacy class of {self._representative} in {self._ambient}"
