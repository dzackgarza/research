r"""Slice, coslice, subobject, superobject, covering, covered, kernel, and cokernel categories.

Symmetric parameterized abstract categories over an ambient \(\mathbf{C}\):

- ``SliceOver(X)`` / ``CosliceUnder(X)``: objects \(A\to X\) / \(X\to A\).
- ``SubObject(X)`` / ``SuperObject(X)``: monomorphisms \(A\hookrightarrow X\)
  (slice) / \(X\hookrightarrow B\) (coslice).
- ``CoveringObject(X)`` / ``CoveredObject(X)``: epimorphisms
  \(A\twoheadrightarrow X\) (slice) / \(X\twoheadrightarrow B\) (coslice).
- ``Kernel(f)`` / ``Cokernel(f)``: the kernel \(\ker(f)\hookrightarrow\operatorname{dom}f\)
  is a subobject of \(\operatorname{dom}f\); the cokernel
  \(\operatorname{cod}f\twoheadrightarrow\operatorname{coker}(f)\) is a covered
  object of \(\operatorname{cod}f\).

Each slice object carries its ``structure_morphism()``; each coslice object
carries its ``costructure_morphism()``.

A slice object *is* the domain of its structure morphism, refined into the
slice category -- never a wrapper around it.  ``A`` keeps every method
\(\mathbf{C}\) gives it and gains only the arrow.  The module-level
``Subobject`` constructor (``subobjects.sage``) is the ``is_mono`` entry
point into this file's ``Slice``.
"""


from sage.categories.groups import Groups
from sage.categories.modules import Modules
from dzack_research.preamble.owned_category_bases import Category
from sage.categories.morphism import Morphism
from sage.structure.element import Element
from sage.structure.parent import Parent

from typing import Protocol, Self, TYPE_CHECKING, runtime_checkable


# Runtime class, not a TYPE_CHECKING declaration: ``Slice(..., is_mono=True)``
# gates on ``isinstance(..., MonoCapableArrow)`` before asserting injectivity,
# so the protocol must exist when that assert runs.
@runtime_checkable
class MonoCapableArrow(Protocol):
    r"""An arrow that can decide whether it is a monomorphism.  Sage puts
    ``is_injective`` on particular morphism classes, not on ``Morphism``,
    and the slice construction is what requires it."""

    def is_injective(self) -> bool: ...


@runtime_checkable
class DecidableImageArrow(Protocol):
    r"""A morphism with a decision procedure for membership in its image."""

    def is_in_image(self, element: Element) -> bool: ...


if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from sage.categories.groups import Group
    from sage.categories.modules import Module
    from dzack_research.preamble.lexicon import OrderedSet

    # The algebra noun, taken the way the lexicon takes ``Ring`` and
    # ``Group``: the category's own ``ParentMethods``.
    from dzack_research.preamble.categories.algebras.algebras import Algebras

    class SliceParent(Protocol):
        r"""What an object of a slice category has from its placement: the
        arrow it is an object over."""

        def structure_morphism(self) -> Morphism: ...


def sole_structure_generators(obj: Parent) -> "OrderedSet":
    r"""Return the generating family of the one structure ``obj`` is framed by.

    Which families an object has is settled by the categories it lives in -- a
    module has module generators, a group has group generators, an algebra has
    algebra generators -- so the categories are asked, not the instance.  An
    object framed twice, such as a free algebra framed as an algebra by $S$ and
    as a module by $\operatorname{Mon}(S)$, has no sole family: which one is
    meant is the caller's to say, so this refuses rather than pick one.
    """
    # Local: the algebra node reaches this module, so a module-level import
    # would close that cycle; it is built by the time this function runs.
    from dzack_research.preamble.categories.algebras.algebras import Algebras

    families = {
        "module": obj in Modules(obj.base_ring()),
        "group": obj in Groups(),
        "algebra": obj in Algebras(obj.base_ring()),
    }
    named = tuple(name for name, present in families.items() if present)
    assert named, (
        f"{obj} is in no category with a distinguished generating family"
    )
    assert len(named) == 1, (
        f"{obj} is framed by more than one structure ({', '.join(named)}); "
        "ask it for the family you mean by name"
    )
    match named[0]:
        case "module":
            module: "Module" = obj
            return tuple(module.module_generators())
        case "group":
            group: "Group" = obj
            return tuple(group.group_generators())
        case "algebra":
            algebra: "Algebras.ParentMethods" = obj
            return tuple(algebra.algebra_generators())


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
        return [self._ambient_category]

    class ParentMethods:
        # Installed on the domain by ``Slice`` below.
        _structure_morphism: Morphism

        def structure_morphism(self: Self) -> Morphism:
            return self._structure_morphism


class CosliceUnderCategory(_UnderAnObject, Category):
    r"""Coslice category \(X \setminus \mathbf{C}\) of objects under \(X\)."""

    def _repr_(self) -> str:
        return f"Category of objects under {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]

    class ParentMethods:
        # Installed on the codomain by ``Coslice`` below.
        _costructure_morphism: Morphism

        def costructure_morphism(self: Self) -> Morphism:
            return self._costructure_morphism


class SubobjectCategory(_OverAnObject, Category):
    r"""Subcategory of ``SliceOver(X)`` represented by monomorphisms \(A\hookrightarrow X\)."""

    def _repr_(self) -> str:
        return f"Category of subobjects of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [SliceOverCategory(self._ambient_category, self._target_object)]

    class ParentMethods:
        def inclusion(self: "SliceParent") -> Morphism:
            r"""Return the monomorphism that represents this subobject."""
            return self.structure_morphism()

        def __contains__(self: "SliceParent", element: Element) -> bool:
            r"""Return whether ``element`` lies in the image of the inclusion."""
            if not isinstance(element, Element):
                return False
            if element.parent() is self:
                return True
            inclusion = self.structure_morphism()
            assert isinstance(inclusion, DecidableImageArrow), (
                f"image membership is not decidable for {inclusion}"
            )
            return inclusion.is_in_image(element)


class SuperobjectCategory(_UnderAnObject, Category):
    r"""Subcategory of ``CosliceUnder(X)`` represented by monomorphisms \(X\hookrightarrow B\)."""

    def _repr_(self) -> str:
        return f"Category of superobjects of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CosliceUnderCategory(self._ambient_category, self._source_object)]


class CoveringObjectCategory(_OverAnObject, Category):
    r"""Subcategory of ``SliceOver(X)`` represented by epimorphisms \(A\twoheadrightarrow X\)."""

    def _repr_(self) -> str:
        return f"Category of covering objects of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [SliceOverCategory(self._ambient_category, self._target_object)]


class CoveredObjectCategory(_UnderAnObject, Category):
    r"""Subcategory of ``CosliceUnder(X)`` represented by epimorphisms \(X\twoheadrightarrow B\)."""

    def _repr_(self) -> str:
        return f"Category of covered objects of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CosliceUnderCategory(self._ambient_category, self._source_object)]


class KernelCategory(_OverAnObject, Category):
    r"""Subcategory of ``SubObject(f.domain())``: the kernel \(\ker(f)\hookrightarrow\operatorname{dom}f\)."""

    def _repr_(self) -> str:
        return f"Category of kernels of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        map_taken = self._target_object
        assert isinstance(map_taken, Morphism), (
            "a kernel category is parameterized by the morphism it is the kernel of"
        )
        return [SubobjectCategory(self._ambient_category, map_taken.domain())]


class CokernelCategory(_UnderAnObject, Category):
    r"""Subcategory of ``CoveredObject(f.codomain())``: the cokernel \(\operatorname{cod}f\twoheadrightarrow\operatorname{coker}f\)."""

    def _repr_(self) -> str:
        return f"Category of cokernels of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        map_taken = self._source_object
        assert isinstance(map_taken, Morphism), (
            "a cokernel category is parameterized by the morphism it is the cokernel of"
        )
        return [CoveredObjectCategory(self._ambient_category, map_taken.codomain())]


def with_chosen_arrows_forgotten(category: Category) -> Category:
    r"""Return ``category`` with every chosen arrow forgotten.

    Being an object of \(\mathbf{C}/X\) is not a property of \(A\): it is
    \(A\) *together with* a chosen arrow \(A\to X\).  So a construction that
    builds a **new** object out of \(A\) -- the formed module classified by a
    form written on \(A\), say -- inherits \(A\)'s structure and none of
    \(A\)'s arrows: there is no morphism out of the new object to inherit,
    and placing it in \(\mathbf{C}/X\) would assert one that does not exist.

    The category the new object is built in is therefore the image of \(A\)'s
    under the forgetful \(\mathbf{C}/X\to\mathbf{C}\), applied until no chosen
    arrow is left.  ``super_categories()`` is where each of these categories
    already states what it forgets to, so this reads that and nothing else.
    """
    # Local: the module-level subobject category is above this file in the
    # tree, and it is built by the time a construction forgets an arrow.
    from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import (
        Subobjects,
    )
    from sage.categories.category import Category as SageCategory
    from sage.categories.category import JoinCategory
    from sage.categories.subobjects import SubobjectsCategory

    # The two parameter classes above are the whole slice and coslice family;
    # ``Subobjects`` states the same of a module without naming the object it
    # embeds in, and Sage's construction category states it of any C.
    carries_a_chosen_arrow = (
        _OverAnObject,
        _UnderAnObject,
        Subobjects,
        SubobjectsCategory,
    )

    def forgotten(member: Category) -> list[Category]:
        if isinstance(member, (JoinCategory, *carries_a_chosen_arrow)):
            return [
                forgetful
                for above in member.super_categories()
                for forgetful in forgotten(above)
            ]
        return [member]

    return SageCategory.join(forgotten(category))


def Slice(structure_morphism: Morphism, is_mono: bool = False, is_epi: bool = False) -> Parent:
    r"""Construct the slice object represented by a morphism \(A\to X\).

    The structure morphism is stored on the domain and the domain is refined
    into ``SliceOver(X)`` by default, ``SubObject(X)`` when ``is_mono``, or
    ``CoveringObject(X)`` when ``is_epi``.
    """
    # Local: refine is imported here rather than at module level, where it
    # would close a cycle; it is built by the time this function runs.
    from dzack_research.preamble.refine import refine

    assert isinstance(structure_morphism, Morphism), (
        "the structure morphism of a slice object must be a Morphism"
    )
    if is_mono:
        assert structure_morphism.is_injective(), (
            "is_mono requires the structure morphism to be a monomorphism"
        )
    domain = structure_morphism.domain()
    domain._structure_morphism = structure_morphism
    codomain = structure_morphism.codomain()
    # \(\mathbf{C}/X\) is a slice of \(\mathbf{C}\), so the category sliced is
    # \(A\)'s as an object of \(\mathbf{C}\) -- not as an object of a slice it
    # already sits in.  A free module can be the degree-2 piece of two tensor
    # algebras, and reading its sliced category back in would nest
    # \(\mathbf{C}/X\) inside \(\mathbf{C}/X\), which no method resolution
    # order satisfies.
    cat = with_chosen_arrows_forgotten(domain.category())
    if is_mono:
        refine(domain, cat.SubObject(codomain))
    elif is_epi:
        refine(domain, cat.CoveringObject(codomain))
    else:
        refine(domain, cat.SliceOver(codomain))
    sliced: Parent = domain
    return sliced


def Coslice(costructure_morphism: Morphism, is_mono: bool = False, is_epi: bool = False) -> Parent:
    r"""Construct the coslice object represented by a morphism \(X\to B\).

    The costructure morphism is stored on the codomain and the codomain is
    refined into ``CosliceUnder(X)`` by default, ``SuperObject(X)`` when
    ``is_mono``, or ``CoveredObject(X)`` when ``is_epi``.
    """
    # Local: refine is imported here rather than at module level, where it
    # would close a cycle; it is built by the time this function runs.
    from dzack_research.preamble.refine import refine

    assert isinstance(costructure_morphism, Morphism), (
        "the costructure morphism of a coslice object must be a Morphism"
    )
    codomain = costructure_morphism.codomain()
    codomain._costructure_morphism = costructure_morphism
    source = costructure_morphism.domain()
    # The category cosliced is \(B\)'s own, for the reason :func:`Slice` gives.
    cat = with_chosen_arrows_forgotten(codomain.category())
    if is_mono:
        refine(codomain, cat.SuperObject(source))
    elif is_epi:
        refine(codomain, cat.CoveredObject(source))
    else:
        refine(codomain, cat.CosliceUnder(source))
    cosliced: Parent = codomain
    return cosliced


def Superobject(costructure_morphism: Morphism) -> Parent:
    r"""Construct the superobject represented by a monomorphism \(X\hookrightarrow B\)."""
    return Coslice(costructure_morphism, is_mono=True)


def Covering(structure_morphism: Morphism) -> Parent:
    r"""Construct the covering object represented by an epimorphism \(A\twoheadrightarrow X\)."""
    return Slice(structure_morphism, is_epi=True)


def Covered(costructure_morphism: Morphism) -> Parent:
    r"""Construct the covered object represented by an epimorphism \(X\twoheadrightarrow B\)."""
    return Coslice(costructure_morphism, is_epi=True)
