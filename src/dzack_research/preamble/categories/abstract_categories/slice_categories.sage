r"""Slice, coslice, subobject, superobject, covering, and covered categories.

Symmetric parameterized abstract categories over an ambient \(\mathbf{C}\):

- ``SliceOver(X)`` / ``CosliceUnder(X)``: objects \(A\to X\) / \(X\to A\).
- ``SubObject(X)`` / ``SuperObject(X)``: monomorphisms \(A\hookrightarrow X\)
  (slice) / \(X\hookrightarrow B\) (coslice).
- ``CoveringObject(X)`` / ``CoveredObject(X)``: epimorphisms
  \(A\twoheadrightarrow X\) (slice) / \(X\twoheadrightarrow B\) (coslice).
An object of each category is the arrow itself.  Its domain and codomain are
read from that arrow.  No endpoint is mutated or given a second category.
"""


from dzack_research.preamble.owned_category_bases import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sage.structure.parent import MembershipInput

class _OverAnObject:
    r"""The two parameters a slice category takes.

    They are the ambient category and the object the slice is over.  The
    kernel subcategory takes a *morphism* there: it slices over the domain of
    the map it is the kernel of.

    This is not a category.  Each category below states its place with
    ``super_categories()``.  A category class that inherits another states the
    class graph by hand instead, and then its methods class arrives twice in
    one set of bases, which no method resolution order can satisfy.
    """

    def __init__(self, ambient_category: Category, X: "Parent | Morphism") -> None:
        self._ambient_category = ambient_category
        self._target_object = X
        super().__init__()

    def ambient_category(self) -> Category:
        return self._ambient_category


class _UnderAnObject:
    r"""The two parameters a coslice category takes.

    They are the ambient category and the object the coslice is under.  The
    cokernel subcategory takes a *morphism* there: it coslices under the
    codomain of the map it is the cokernel of.

    Read :class:`_OverAnObject` for why this is not a category.
    """

    def __init__(self, ambient_category: Category, X: "Parent | Morphism") -> None:
        self._ambient_category = ambient_category
        self._source_object = X
        super().__init__()

    def ambient_category(self) -> Category:
        return self._ambient_category


class SliceOverCategory(_OverAnObject, Category):
    r"""Slice category \(\mathbf{C}/X\) of objects over \(X\)."""

    def _repr_(self) -> str:
        return f"Category of objects over {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import ArrowCategory

        return [ArrowCategory(self._ambient_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            isinstance(candidate, Morphism)
            and candidate in self.super_categories()[0]
            and candidate.codomain() is self._target_object
        )


class CosliceUnderCategory(_UnderAnObject, Category):
    r"""Coslice category \(X \setminus \mathbf{C}\) of objects under \(X\)."""

    def _repr_(self) -> str:
        return f"Category of objects under {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        from dzack_research.preamble.categories.abstract_categories.arrow_categories import ArrowCategory

        return [ArrowCategory(self._ambient_category)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            isinstance(candidate, Morphism)
            and candidate in self.super_categories()[0]
            and candidate.domain() is self._source_object
        )


class SubobjectCategory(_OverAnObject, Category):
    r"""Subcategory of ``SliceOver(X)`` represented by monomorphisms \(A\hookrightarrow X\)."""

    def _repr_(self) -> str:
        return f"Category of subobjects of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [SliceOverCategory(self._ambient_category, self._target_object)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in self.super_categories()[0]
            and isinstance(candidate, SubobjectCategory.MorphismMethods)
        )

    class MorphismMethods:
        def is_monomorphism(self) -> bool:
            return True

class SuperobjectCategory(_UnderAnObject, Category):
    r"""Subcategory of ``CosliceUnder(X)`` represented by monomorphisms \(X\hookrightarrow B\)."""

    def _repr_(self) -> str:
        return f"Category of superobjects of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CosliceUnderCategory(self._ambient_category, self._source_object)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in self.super_categories()[0]
            and isinstance(candidate, SuperobjectCategory.MorphismMethods)
        )

    class MorphismMethods:
        def is_monomorphism(self) -> bool:
            return True


class CoveringObjectCategory(_OverAnObject, Category):
    r"""Subcategory of ``SliceOver(X)`` represented by epimorphisms \(A\twoheadrightarrow X\)."""

    def _repr_(self) -> str:
        return f"Category of covering objects of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [SliceOverCategory(self._ambient_category, self._target_object)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in self.super_categories()[0]
            and isinstance(candidate, CoveringObjectCategory.MorphismMethods)
        )

    class MorphismMethods:
        def is_epimorphism(self) -> bool:
            return True


class CoveredObjectCategory(_UnderAnObject, Category):
    r"""Subcategory of ``CosliceUnder(X)`` represented by epimorphisms \(X\twoheadrightarrow B\)."""

    def _repr_(self) -> str:
        return f"Category of covered objects of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CosliceUnderCategory(self._ambient_category, self._source_object)]

    def __contains__(self, candidate: "MembershipInput") -> bool:
        return (
            candidate in self.super_categories()[0]
            and isinstance(candidate, CoveredObjectCategory.MorphismMethods)
        )

    class MorphismMethods:
        def is_epimorphism(self) -> bool:
            return True


def Slice(structure_morphism: Morphism, is_mono: bool = False, is_epi: bool = False) -> Morphism:
    r"""Construct the slice object represented by a morphism \(A\to X\).

    The returned object is the morphism itself.  It is refined into
    ``SliceOver(X)`` by default, ``SubObject(X)`` when ``is_mono``, or
    ``CoveringObject(X)`` when ``is_epi``.
    """
    # Local: refine is imported here rather than at module level, where it
    # would close a cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import common_category
    from dzack_research.preamble.refine import refine

    assert isinstance(structure_morphism, Morphism), (
        "the structure morphism of a slice object must be a Morphism"
    )
    domain = structure_morphism.domain()
    codomain = structure_morphism.codomain()
    cat = common_category((domain, codomain))
    if is_mono:
        category = cat.SubObject(codomain)
    elif is_epi:
        category = cat.CoveringObject(codomain)
    else:
        category = cat.SliceOver(codomain)
    sliced: Morphism = refine(structure_morphism, category)
    return sliced


def Coslice(costructure_morphism: Morphism, is_mono: bool = False, is_epi: bool = False) -> Morphism:
    r"""Construct the coslice object represented by a morphism \(X\to B\).

    The returned object is the morphism itself.  It is refined into
    ``CosliceUnder(X)`` by default, ``SuperObject(X)`` when ``is_mono``, or
    ``CoveredObject(X)`` when ``is_epi``.
    """
    # Local: refine is imported here rather than at module level, where it
    # would close a cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.abstract_categories.arrow_categories import common_category
    from dzack_research.preamble.refine import refine

    assert isinstance(costructure_morphism, Morphism), (
        "the costructure morphism of a coslice object must be a Morphism"
    )
    codomain = costructure_morphism.codomain()
    source = costructure_morphism.domain()
    cat = common_category((source, codomain))
    if is_mono:
        category = cat.SuperObject(source)
    elif is_epi:
        category = cat.CoveredObject(source)
    else:
        category = cat.CosliceUnder(source)
    cosliced: Morphism = refine(costructure_morphism, category)
    return cosliced


def Superobject(costructure_morphism: Morphism) -> Morphism:
    r"""Construct the superobject represented by a monomorphism \(X\hookrightarrow B\)."""
    return Coslice(costructure_morphism, is_mono=True)


def Covering(structure_morphism: Morphism) -> Morphism:
    r"""Construct the covering object represented by an epimorphism \(A\twoheadrightarrow X\)."""
    return Slice(structure_morphism, is_epi=True)


def Covered(costructure_morphism: Morphism) -> Morphism:
    r"""Construct the covered object represented by an epimorphism \(X\twoheadrightarrow B\)."""
    return Coslice(costructure_morphism, is_epi=True)
