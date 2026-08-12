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
from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # The ordered-set noun is type-only: the preamble loads into one
    # shared namespace and nothing named OrderedSet may bind there.
    from dzack_research.preamble.lexicon import OrderedSet


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
            return tuple(obj.module_generators())
        case "group":
            return tuple(obj.group_generators())
        case "algebra":
            return tuple(obj.algebra_generators())


class SliceOverCategory(Category):
    r"""Slice category \(\mathbf{C}/X\) of objects over \(X\)."""

    @staticmethod
    def __classcall_private__(cls, ambient_category: Category, X: Parent) -> "SliceOverCategory":
        return super().__classcall__(cls, ambient_category, X)

    def __init__(self, ambient_category: Category, X: Parent) -> None:
        self._ambient_category = ambient_category
        self._target_object = X
        Category.__init__(self)

    def _repr_(self) -> str:
        return f"Category of objects over {self._target_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]

    class ParentMethods:
        def structure_morphism(self) -> Morphism:
            return self._structure_morphism


class CosliceUnderCategory(Category):
    r"""Coslice category \(X \setminus \mathbf{C}\) of objects under \(X\)."""

    @staticmethod
    def __classcall_private__(cls, ambient_category: Category, X: Parent) -> "CosliceUnderCategory":
        return super().__classcall__(cls, ambient_category, X)

    def __init__(self, ambient_category: Category, X: Parent) -> None:
        self._ambient_category = ambient_category
        self._source_object = X
        Category.__init__(self)

    def _repr_(self) -> str:
        return f"Category of objects under {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [self._ambient_category]

    class ParentMethods:
        def costructure_morphism(self) -> Morphism:
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

        def embedding(self) -> Morphism:
            r"""Return the monomorphism \(A\hookrightarrow X\) representing this subobject.

            The slice category calls this arrow ``structure_morphism``; in a
            subobject category the arrow is a mono, and ``embedding`` is the
            name it earns there.
            """
            return self.structure_morphism()

        inclusion = embedding

        def embedding_codomain(self) -> Parent:
            r"""Return the ambient object \(X\) this subobject embeds into."""
            return self.embedding().codomain()


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
        return [SubobjectCategory(self._ambient_category, self._target_object.domain())]


class CokernelCategory(CoveredObjectCategory):
    r"""Subcategory of ``CoveredObject(f.codomain())``: the cokernel \(\operatorname{cod}f\twoheadrightarrow\operatorname{coker}f\)."""

    def _repr_(self) -> str:
        return f"Category of cokernels of {self._source_object} in {self._ambient_category}"

    def super_categories(self) -> list[Category]:
        return [CoveredObjectCategory(self._ambient_category, self._source_object.codomain())]


Category.SliceOver = lambda self, X: SliceOverCategory(self, X)
Category.CosliceUnder = lambda self, X: CosliceUnderCategory(self, X)
Category.SubObject = lambda self, X: SubobjectCategory(self, X)
Category.SuperObject = lambda self, X: SuperobjectCategory(self, X)
Category.CoveringObject = lambda self, X: CoveringObjectCategory(self, X)
Category.CoveredObject = lambda self, X: CoveredObjectCategory(self, X)
Category.Kernel = lambda self, f: KernelCategory(self, f)
Category.Cokernel = lambda self, f: CokernelCategory(self, f)


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
    cat = domain.category()
    if is_mono:
        refine(domain, cat.SubObject(codomain))
    elif is_epi:
        refine(domain, cat.CoveringObject(codomain))
    else:
        refine(domain, cat.SliceOver(codomain))
    return domain


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
    return codomain


def Superobject(costructure_morphism: Morphism) -> Parent:
    r"""Construct the superobject represented by a monomorphism \(X\hookrightarrow B\)."""
    return Coslice(costructure_morphism, is_mono=True)


def Covering(structure_morphism: Morphism) -> Parent:
    r"""Construct the covering object represented by an epimorphism \(A\twoheadrightarrow X\)."""
    return Slice(structure_morphism, is_epi=True)


def Covered(costructure_morphism: Morphism) -> Parent:
    r"""Construct the covered object represented by an epimorphism \(X\twoheadrightarrow B\)."""
    return Coslice(costructure_morphism, is_epi=True)
