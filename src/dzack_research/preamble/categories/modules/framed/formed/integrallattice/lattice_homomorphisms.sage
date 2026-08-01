r"""Form-preserving homomorphisms of integral lattices."""

from typing import Any

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
        def __call__(self: Any, images: Any, *args: Any, **kwargs: Any) -> Any:
            match images:
                case FormMorphism():
                    assert images.parent() is self, (
                        "an existing morphism belongs only to its own homset"
                    )
                    return images
                case dict():
                    if any(source in Subobjects() for source in images):
                        expanded = _expand_direct_sum_hom_dict(
                            self.domain(),
                            images,
                        )
                        assignment = dict(
                            zip(
                                self.domain().generating_set(),
                                expanded,
                            )
                        )
                    else:
                        assignment = images
                case list() | tuple():
                    assert len(images) == self.domain().ngens(), (
                        "the number of images does not match the framing set"
                    )
                    assignment = dict(
                        zip(self.domain().generating_set(), images)
                    )
                case _:
                    raise TypeError(
                        "a lattice morphism is declared by images of the "
                        "domain's framing labels"
                    )
            return FormHomset._element_constructor_(self, assignment)


def lattice_homset(domain: Any, codomain: Any) -> FormHomset:
    r"""Return the canonical lattice homset for ``domain`` and ``codomain``."""
    homset = FormModules.ParentMethods.Hom(domain, codomain)
    return refine(homset, LatticeHomomorphisms())
