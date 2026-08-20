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
if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput

from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.group.profinite.absolute_galois_group import (
    RealizedAbsoluteGaloisGroups,
)
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.owned_category_bases import Category_singleton

if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.rings.integer import Integer
    from sage.categories.morphism import Morphism
    from sage.categories.rings import Ring
    from sage.structure.parent import Parent


class OpenAbsoluteGaloisSubgroups(Category_singleton):
    r"""An actual open subgroup \(G_E\subset G_K\), embedded in the chosen \(\bar K\).

    Given \(E/K\), the ambient group's choice policy embeds \(E\) into the
    already-chosen \(\bar K\).  Then \(H=\operatorname{Gal}(\bar K/E)\) is an
    actual subgroup of the realized \(G_K\), not merely a conjugacy class.

    \(\bar K\) is an algebraic closure of \(E\) as well, so \(H\) *is* the
    absolute Galois group of \(E\) realized in that closure.  This level
    therefore adds one datum -- the ambient \(G_K\) -- and reaches everything
    else through :class:`RealizedAbsoluteGaloisGroups`, whose field is \(E\)
    and whose base embedding is \(E\hookrightarrow\bar K\).
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "open subgroups of absolute Galois groups"

    def super_categories(self) -> list:
        return [RealizedAbsoluteGaloisGroups()]

    class ParentMethods:
        def __init__(
            self, ambient: "Parent", **rest: "ConstructionData"
        ) -> None:
            self._ambient = ambient
            super().__init__(**rest)

        def ambient(self) -> "Parent":
            r"""Return \(G_K\), the ambient absolute Galois group."""
            return self._ambient

        def fixed_field(self) -> "Ring":
            r"""Return \(E\) as embedded in \(\bar K\)."""
            return self._field

        def embedding(self) -> "Morphism":
            r"""Return the embedding \(E\hookrightarrow\bar K\)."""
            return self._embedding

        def index(self) -> "Integer":
            r"""Return \([E:K]\), the index of \(G_E\) in \(G_K\)."""
            degree: "Integer" = self._field.degree(self._ambient.base_field())
            return degree

        def is_normal(self) -> bool:
            r"""Return whether \(E/K\) is Galois."""
            galois: bool = self._field.is_galois()
            return galois

        def core(self) -> "Parent":
            r"""Return \(G_{\widetilde E}\) for \(\widetilde E\) the normal closure of \(E/K\)."""
            normal_closure = self._field.galois_closure()
            subgroup: "Parent" = self._ambient.open_subgroup(normal_closure)
            return subgroup

        def conjugacy_class(self) -> "OpenGaloisSubgroupConjugacyClass":
            r"""Return the conjugacy class of this subgroup, forgetting the embedding."""
            return OpenGaloisSubgroupConjugacyClass(self._ambient, self._field)

        def __hash__(self) -> int:
            return hash((type(self), self._ambient, self._field))

        def __eq__(self, other: "MembershipInput") -> bool:
            return (
                type(other) is type(self)
                and self._ambient == other._ambient
                and self._field == other._field
            )

        def _repr_(self) -> str:
            return f"Open subgroup of {self._ambient} corresponding to {self._field}"


def open_absolute_galois_subgroup(
    ambient: "Parent", extension: "Ring", embedding: "Morphism | None" = None
) -> "Parent":
    r"""Return \(G_E=\operatorname{Gal}(\bar K/E)\) inside the realized \(G_K\)."""
    closure = ambient.algebraic_closure()
    if embedding is None:
        embedding = ambient.choice_policy().choose_embedding(extension, closure)
    return object_of(
        OpenAbsoluteGaloisSubgroups(),
        ambient=ambient,
        field=extension,
        closure=closure,
        embedding=embedding,
        choice_policy=ambient.choice_policy(),
    )


class OpenGaloisSubgroupConjugacyClass(SageObject):
    r"""The conjugacy class of open subgroups determined by \(E/K\).

    Choice-independent: forgetting the embedding \(E\hookrightarrow\bar K\)
    yields the conjugacy class.  This is the invariant projection of a
    chosen :class:`OpenAbsoluteGaloisSubgroups` object.
    """

    def __init__(self, ambient: "Parent", extension: "Ring") -> None:
        self._ambient = ambient
        self._extension = extension

    def ambient(self) -> "Parent":
        return self._ambient

    def fixed_field(self) -> "Ring":
        return self._extension

    def index(self) -> "Integer":
        degree: "Integer" = self._extension.degree(self._ambient.base_field())
        return degree

    def representative(self) -> "Parent":
        r"""Return a chosen representative subgroup from this conjugacy class."""
        subgroup: "Parent" = self._ambient.open_subgroup(
            self._extension
        )
        return subgroup

    def __hash__(self) -> int:
        return hash((type(self), self._ambient, self._extension))

    def __eq__(self, other: "MembershipInput") -> bool:
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
