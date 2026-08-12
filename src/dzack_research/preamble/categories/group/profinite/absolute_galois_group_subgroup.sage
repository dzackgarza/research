r"""Open subgroups of \(G_K\) carrying finite extensions.

Given \(E/K\) and the chosen realization \(\iota:K\hookrightarrow\bar K\),
embed \(E\) into \(\bar K\) and form the actual subgroup
\(H=\operatorname{Gal}(\bar K/E)\).  This is a genuine subgroup of the
realized \(G_K\), not merely a conjugacy class.

The conjugacy class — the choice-independent invariant obtained by
forgetting the embedding — is available as
:func:`open_subgroup_class` or :meth:`conjugacy_class` on the
chosen subgroup.

Subgroup operations are field computations by the infinite Galois
correspondence:

==========================  ========================================
group operation             field computation
==========================  ========================================
``H.index()``               \([E:K]\)
``H.is_normal()``            whether \(E/K\) is Galois
``H1 <= H2``                 \(E_2\subseteq E_1\)
``H1.intersection(H2)``     \(G_{E_1E_2}\)
``H.core()``                \(G_{\widetilde E}\) (normal closure)
``H.normalizer_quotient()`` \(N_{G_K}(G_E)/G_E\simeq\operatorname{Aut}_K(E)\)
==========================  ========================================
"""

from typing import TYPE_CHECKING

from sage.structure.sage_object import SageObject

if TYPE_CHECKING:
    from sage.categories.morphism import Morphism
    from dzack_research.preamble.lexicon import Ring


class OpenAbsoluteGaloisSubgroup(SageObject):
    r"""An actual open subgroup \(G_E\subset G_K\), embedded in the chosen \(\bar K\).

    Given \(E/K\), the parent's choice policy embeds \(E\) into the
    already-chosen \(\bar K\).  Then
    \(H=\operatorname{Gal}(\bar K/E)\) is an actual subgroup of the
    realized \(G_K\), not merely a conjugacy class.
    """

    def __init__(
        self,
        ambient: "AbsoluteGaloisGroup",
        extension: "Ring",
        embedding: "Morphism | None" = None,
    ) -> None:
        self._ambient = ambient
        self._extension = extension

        if embedding is None:
            closure = ambient.algebraic_closure()
            embedding = ambient.choice_policy().choose_embedding(
                extension, closure
            )
        self._embedding = embedding

    def ambient(self) -> "AbsoluteGaloisGroup":
        r"""Return \(G_K\), the ambient absolute Galois group."""
        return self._ambient

    def fixed_field(self) -> "Ring":
        r"""Return \(E\) as embedded in \(\bar K\)."""
        return self._extension

    def embedding(self) -> "Morphism":
        r"""Return the embedding \(E\hookrightarrow\bar K\)."""
        return self._embedding

    def index(self) -> "Integer":
        r"""Return \([E:K]\), the index of \(G_E\) in \(G_K\)."""
        degree: "Integer" = self._extension.degree(self._ambient.base_field())
        return degree

    def is_normal(self) -> bool:
        r"""Return whether \(E/K\) is Galois."""
        galois: bool = self._extension.is_galois()
        return galois

    def core(self) -> "OpenAbsoluteGaloisSubgroup":
        r"""Return \(G_{\widetilde E}\) for \(\widetilde E\) the normal closure of \(E/K\)."""
        normal_closure = self._extension.galois_closure()
        subgroup: "OpenAbsoluteGaloisSubgroup" = self._ambient.open_subgroup(
            normal_closure
        )
        return subgroup

    def conjugacy_class(self) -> "OpenGaloisSubgroupConjugacyClass":
        r"""Return the conjugacy class of this subgroup, forgetting the embedding."""
        return OpenGaloisSubgroupConjugacyClass(
            self._ambient, self._extension
        )

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._extension))

    def __eq__(self, other: object) -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._extension == other._extension
        )

    def _repr_(self) -> str:
        return f"Open subgroup of {self._ambient} corresponding to {self._extension}"


class OpenGaloisSubgroupConjugacyClass(SageObject):
    r"""The conjugacy class of open subgroups determined by \(E/K\).

    Choice-independent: forgetting the embedding \(E\hookrightarrow\bar K\)
    yields the conjugacy class.  This is the invariant projection of a
    chosen :class:`OpenAbsoluteGaloisSubgroup`.
    """

    def __init__(self, ambient: "AbsoluteGaloisGroup", extension: "Ring") -> None:
        self._ambient = ambient
        self._extension = extension

    def ambient(self) -> "AbsoluteGaloisGroup":
        return self._ambient

    def fixed_field(self) -> "Ring":
        return self._extension

    def index(self) -> "Integer":
        degree: "Integer" = self._extension.degree(self._ambient.base_field())
        return degree

    def representative(self) -> "OpenAbsoluteGaloisSubgroup":
        r"""Return a chosen representative subgroup from this conjugacy class."""
        subgroup: "OpenAbsoluteGaloisSubgroup" = self._ambient.open_subgroup(
            self._extension
        )
        return subgroup

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._extension))

    def __eq__(self, other: object) -> bool:
        return (
            type(other) is type(self)
            and self._ambient == other._ambient
            and self._extension == other._extension
        )

    def _repr_(self) -> str:
        return (
            f"Conjugacy class of open subgroups of {self._ambient} "
            f"corresponding to {self._extension}"
        )