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
        def embedding(self) -> Morphism: ...


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


class SliceOverCategory(Category):
    r"""Slice category \(\mathbf{C}/X\) of objects over \(X\)."""

    @staticmethod
    def __classcall_private__(
        cls: type["SliceOverCategory"], ambient_category: Category, X: "Parent | Morphism"
    ) -> "SliceOverCategory":
        # ``X`` is an object for a slice and a *morphism* for the kernel
        # subcategory, which slices over the domain of the map it is the
        # kernel of.
        slice_category: SliceOverCategory = super().__classcall__(
            cls, ambient_category, X
        )
        return slice_category

    def __init__(self, ambient_category: Category, X: "Parent | Morphism") -> None:
        self._ambient_category = ambient_category
        self._target_object = X
        Category.__init__(self)

    def _repr_(self) -> str:
        return f"Category of objects over {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]

    class ParentMethods:
        # Installed on the domain by ``Slice`` below.
        _structure_morphism: Morphism

        def structure_morphism(self: Self) -> Morphism:
            return self._structure_morphism


class CosliceUnderCategory(Category):
    r"""Coslice category \(X \setminus \mathbf{C}\) of objects under \(X\)."""

    @staticmethod
    def __classcall_private__(
        cls: type["CosliceUnderCategory"],
        ambient_category: Category,
        X: "Parent | Morphism",
    ) -> "CosliceUnderCategory":
        # ``X`` is an object for a coslice and a *morphism* for the cokernel
        # subcategory, which coslices under the codomain of that map.
        coslice_category: CosliceUnderCategory = super().__classcall__(
            cls, ambient_category, X
        )
        return coslice_category

    def __init__(self, ambient_category: Category, X: "Parent | Morphism") -> None:
        self._ambient_category = ambient_category
        self._source_object = X
        Category.__init__(self)

    def _repr_(self) -> str:
        return f"Category of objects under {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]

    class ParentMethods:
        # Installed on the codomain by ``Coslice`` below.
        _costructure_morphism: Morphism

        def costructure_morphism(self: Self) -> Morphism:
            return self._costructure_morphism


class SubobjectCategory(SliceOverCategory):
    r"""Subcategory of ``SliceOver(X)`` represented by monomorphisms \(A\hookrightarrow X\)."""

    def _repr_(self) -> str:
        return f"Category of subobjects of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [SliceOverCategory(self._ambient_category, self._target_object)]

    class ParentMethods:
        r"""What being a subobject gives \(A\), and nothing more.

        \(A\) is an object of \(\mathbf{C}\) already, so its generators,
        rank, form, and action are answered by \(\mathbf{C}\).  Being a
        subobject adds one thing: the monomorphism.
        """

        def embedding(self: "SliceParent") -> Morphism:
            r"""Return the monomorphism \(A\hookrightarrow X\) representing this subobject.

            The slice category calls this arrow ``structure_morphism``; in a
            subobject category the arrow is a mono, and ``embedding`` is the
            name it earns there.
            """
            return self.structure_morphism()

        inclusion = embedding

        def embedding_codomain(self: "SliceParent") -> Parent:
            r"""Return the ambient object \(X\) this subobject embeds into."""
            ambient: Parent = self.embedding().codomain()
            return ambient


class SuperobjectCategory(CosliceUnderCategory):
    r"""Subcategory of ``CosliceUnder(X)`` represented by monomorphisms \(X\hookrightarrow B\)."""

    def _repr_(self) -> str:
        return f"Category of superobjects of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CosliceUnderCategory(self._ambient_category, self._source_object)]


class CoveringObjectCategory(SliceOverCategory):
    r"""Subcategory of ``SliceOver(X)`` represented by epimorphisms \(A\twoheadrightarrow X\)."""

    def _repr_(self) -> str:
        return f"Category of covering objects of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [SliceOverCategory(self._ambient_category, self._target_object)]


class CoveredObjectCategory(CosliceUnderCategory):
    r"""Subcategory of ``CosliceUnder(X)`` represented by epimorphisms \(X\twoheadrightarrow B\)."""

    def _repr_(self) -> str:
        return f"Category of covered objects of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CosliceUnderCategory(self._ambient_category, self._source_object)]


class KernelCategory(SubobjectCategory):
    r"""Subcategory of ``SubObject(f.domain())``: the kernel \(\ker(f)\hookrightarrow\operatorname{dom}f\)."""

    def _repr_(self) -> str:
        return f"Category of kernels of {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        map_taken = self._target_object
        assert isinstance(map_taken, Morphism), (
            "a kernel category is parameterized by the morphism it is the kernel of"
        )
        return [SubobjectCategory(self._ambient_category, map_taken.domain())]


class CokernelCategory(CoveredObjectCategory):
    r"""Subcategory of ``CoveredObject(f.codomain())``: the cokernel \(\operatorname{cod}f\twoheadrightarrow\operatorname{coker}f\)."""

    def _repr_(self) -> str:
        return f"Category of cokernels of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        map_taken = self._source_object
        assert isinstance(map_taken, Morphism), (
            "a cokernel category is parameterized by the morphism it is the cokernel of"
        )
        return [CoveredObjectCategory(self._ambient_category, map_taken.codomain())]


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
        assert isinstance(structure_morphism, MonoCapableArrow), (
            "is_mono requires an arrow that can decide injectivity"
        )
        assert structure_morphism.is_injective(), (
            "is_mono requires the structure morphism to be a monomorphism"
        )
    domain = structure_morphism.domain()
    domain._structure_morphism = structure_morphism
    codomain = structure_morphism.codomain()
    cat = domain.category()
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
    cat = codomain.category()
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
