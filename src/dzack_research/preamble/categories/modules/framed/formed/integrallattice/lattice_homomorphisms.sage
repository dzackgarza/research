r"""Form-preserving homomorphisms of integral lattices."""

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sage.categories.modules import Module

from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormHomset
if TYPE_CHECKING:
    from sage.categories.morphism import Morphism

from typing import Protocol, TYPE_CHECKING

from sage.categories.category import Category

from dzack_research.preamble.categories.sets.owned_sets import Sets


if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeAlias

    from sage.categories.morphism import SetMorphism

    # How a lattice map may be named: an assignment on the framing labels, an
    # ordered list of images, an existing morphism, or a function on the
    # framing set.
    LatticeMapSpecification: TypeAlias = (
        SetMorphism | dict | list | tuple | Callable
    )

    class LatticeHomsetParent(Protocol):
        r"""What a lattice homset offers: the lattice its morphisms leave."""

        def domain(self) -> "Module": ...


class LatticeHomomorphisms(Category):
    r"""Native form morphisms between integral lattices."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice homomorphisms"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def __call__(
            self: "LatticeHomsetParent",
            images: "LatticeMapSpecification",
        ) -> "Morphism":
            # Local: a module-level import here would close a cycle; by call time this module is built.
            from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormMorphism
            from dzack_research.preamble.categories.modules.framed.formed.integrallattice.subobjects import Subobjects
            from dzack_research.preamble.categories.modules.direct_sum_objects import _expand_direct_sum_hom_dict
            match images:
                case FormMorphism():
                    assert images.parent() is self, (
                        "an existing morphism belongs only to its own homset"
                    )
                    morphism: "Morphism" = images
                    return morphism
                case dict():
                    match any(source in Subobjects() for source in images):
                        case True:
                            expanded = _expand_direct_sum_hom_dict(
                                self.domain(),
                                images,
                            )
                            assignment = dict(
                                zip(
                                    self.domain().module_generating_set(),
                                    expanded,
                                    strict=True,
                                )
                            )
                        case False:
                            assignment = images
                case list() | tuple():
                    assert len(images) == self.domain().number_of_module_generators(), (
                        "the number of images does not match the framing set"
                    )
                    assignment = dict(
                        zip(self.domain().module_generating_set(), images)
                    )
                case _:
                    assert False, (
                        "a lattice morphism is declared by images of the "
                        "domain's framing labels"
                    )
            declared: "Morphism" = FormHomset._element_constructor_(self, assignment)
            return declared


def lattice_homset(domain: "Module", codomain: "Module") -> FormHomset:
    r"""Return the canonical lattice homset for ``domain`` and ``codomain``."""
    # Local: a module-level import here would close a cycle; by call time this module is built.
    from dzack_research.preamble.categories.modules.framed.formed.form_modules import FormModules
    from dzack_research.preamble.refine import refine
    homset = FormModules.ParentMethods.Hom(domain, codomain)
    return refine(homset, LatticeHomomorphisms())
