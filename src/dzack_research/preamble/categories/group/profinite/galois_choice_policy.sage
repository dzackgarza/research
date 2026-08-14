r"""Deterministic choice policies for realizations of \(G_K\).

A concrete realization of \(G_K\) requires choices: an algebraic closure
\(\bar K\), an embedding \(\iota:K\hookrightarrow\bar K\), prolongations
of places, and extensions of finite-level automorphisms to larger
fields.  These choices are not canonical, but they should be
*reproducible*: given the same inputs, the same choice is made.

This is exactly analogous to choosing a geometric basepoint for
\(\pi_1(X,\bar x)\): changing \(\bar x\) changes the concrete group by
an isomorphism well-defined only up to inner automorphism.  The standard
étale fundamental-group formalism works this way rather than refusing to
choose a basepoint.

A :class:`GaloisChoicePolicy` makes extension choices reproducible.  It
is immutable state of the parent, set at construction::

    G = AbsoluteGaloisGroup(K, closure=QQbar, embedding=iota,
                            choice_policy=my_policy)

The default policy, ``"sage"``, uses Sage's own ordering on embeddings
and extensions: the first embedding returned by
``K.embeddings(Omega)``, the first extension returned by the
normal-extension algorithm, etc.
"""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput

from sage.structure.sage_object import SageObject

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from sage.rings.number_field.number_field_ideal import NumberFieldFractionalIdeal
    from sage.categories.rings import Ring


class GaloisChoicePolicy(SageObject):
    r"""A deterministic policy for making realization choices.

    The policy decides, among finitely many possible extensions of a
    field automorphism to a larger normal field, which one to take.
    Different policies give different realizations of \(G_K\); the
    resulting groups are isomorphic up to inner automorphism.
    """

    def __init__(self, name: str = "sage") -> None:
        self._name = name

    def name(self) -> str:
        r"""Return the policy name (e.g. ``"sage"``, ``"random"``, ``"custom"``)."""
        return self._name

    def choose_embedding(self, K: "Ring", Omega: "Ring") -> "Morphism":
        r"""Choose an embedding \(K\hookrightarrow\Omega\).

        Default: if ``K`` has a distinguished embedding into ``Omega``,
        use it; otherwise take the first of ``K.embeddings(Omega)``.
        """
        emb = getattr(K, "coerce_embedding", None)
        if emb is not None:
            emb = emb()
            if emb is not None and emb.codomain() == Omega:
                distinguished: "Morphism" = emb
                return distinguished
        embeddings = K.embeddings(Omega)
        assert embeddings, f"no embeddings of {K} into {Omega}"
        first: "Morphism" = embeddings[0]
        return first

    def choose_extension(
        self, automorphism: "Morphism", extensions: "list[Morphism]"
    ) -> "Morphism":
        r"""Choose one extension of ``automorphism`` among ``extensions``.

        ``extensions`` is a finite list of automorphisms of a larger
        normal field, each restricting to ``automorphism`` on the
        original field.  Default: take the first.
        """
        assert extensions, "no extensions available"
        first: "Morphism" = extensions[0]
        return first

    def choose_prolongation(
        self,
        prime: "NumberFieldFractionalIdeal",
        closure: "Ring",
        candidates: "list[NumberFieldFractionalIdeal]",
    ) -> "NumberFieldFractionalIdeal":
        r"""Choose a prolongation of ``prime`` to ``closure`` among ``candidates``.

        Default: take the first.
        """
        assert candidates, "no prolongations available"
        return candidates[0]

    def __hash__(self) -> int:
        return hash((type(self), self._name))

    def __eq__(self, other: "MembershipInput") -> bool:
        return (
            isinstance(other, GaloisChoicePolicy)
            and type(other) is type(self)
            and self._name == other._name
        )

    def _repr_(self) -> str:
        return f"Galois choice policy ({self._name})"


def default_choice_policy() -> GaloisChoicePolicy:
    r"""Return the default (``"sage"``) choice policy."""
    return GaloisChoicePolicy("sage")
