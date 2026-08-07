r"""Form-preserving homomorphisms of integral lattices."""

from typing import Self

from sage.categories.category import Category

from sage_lattice_category_spike.objects.sets import Sets


class LatticeHomomorphisms(Category):
    r"""Native form morphisms between integral lattices."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice homomorphisms"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        def __call__(self: Self, images: dict) -> "Morphism":
            match images:
                case FormMorphism():
                    assert images.parent() is self, (
                        "an existing morphism belongs only to its own homset"
                    )
                    return images
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
            return FormHomset._element_constructor_(self, assignment)


def lattice_homset(domain: "Module", codomain: "Module") -> FormHomset:
    r"""Return the canonical lattice homset for ``domain`` and ``codomain``."""
    homset = FormModules.ParentMethods.Hom(domain, codomain)
    return refine(homset, LatticeHomomorphisms())
