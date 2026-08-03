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
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.morphism import Morphism
from sage.structure.parent import Parent


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
        def _embedded_source_elements(self) -> tuple[Any, ...]:
            source = self.structure_morphism().domain()
            if hasattr(source, "module_generators"):
                return tuple(source.module_generators())
            if hasattr(source, "group_generators"):
                return tuple(source.group_generators())
            if hasattr(source, "algebra_generators"):
                return tuple(source.algebra_generators())
            raise NotImplementedError(
                "embedded_elements requires a source object with one of: "
                "module_generators(), group_generators(), or algebra_generators()"
            )

        def embedded_elements(self) -> Any:
            r"""Return the images of this subobject's source elements under its structure map."""
            return tuple(
                self.structure_morphism()(source_element)
                for source_element in self._embedded_source_elements()
            )

        def generator_matrix(self) -> Any:
            r"""Return the matrix whose rows are the coordinates of this subobject's generators in its ambient parent."""
            elems = self.embedded_elements()
            if not elems:
                return matrix(self.base_ring(), 0, 0)
            target = self.structure_morphism().codomain()
            def _coords(v):
                if hasattr(v, "_coordinates_"):
                    return list(v._coordinates_)
                if hasattr(target, "coordinate_vector"):
                    return list(target.coordinate_vector(v))
                return list(v)
            return matrix(self.base_ring(), [_coords(v) for v in elems])

        def index(self) -> Any:
            r"""Return the index \([X:A]\) as the cardinality of the cokernel of \(A\hookrightarrow X\)."""
            return self.structure_morphism().index()

        def isotropic_reduction(self) -> Any:
            r"""For an isotropic subobject \(A\hookrightarrow B\) of a formed module, return \(B/A^{\perp}\).

            Requires the structure morphism to carry ``orthogonal_complement``
            (i.e. the codomain is a formed module) and ``cokernel``.  The
            reduction is
            \(\operatorname{coker}(A^{\perp}\hookrightarrow B)\), computed as
            ``self.structure_morphism().orthogonal_complement().structure_morphism().cokernel()``.
            """
            return (
                self.structure_morphism()
                .orthogonal_complement()
                .structure_morphism()
                .cokernel()
            )


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


def Subobject(structure_morphism: Morphism) -> Parent:
    r"""Construct the subobject represented by a monomorphism \(A\hookrightarrow X\)."""
    return Slice(structure_morphism, is_mono=True)


def Superobject(costructure_morphism: Morphism) -> Parent:
    r"""Construct the superobject represented by a monomorphism \(X\hookrightarrow B\)."""
    return Coslice(costructure_morphism, is_mono=True)


def Covering(structure_morphism: Morphism) -> Parent:
    r"""Construct the covering object represented by an epimorphism \(A\twoheadrightarrow X\)."""
    return Slice(structure_morphism, is_epi=True)


def Covered(costructure_morphism: Morphism) -> Parent:
    r"""Construct the covered object represented by an epimorphism \(X\twoheadrightarrow B\)."""
    return Coslice(costructure_morphism, is_epi=True)
