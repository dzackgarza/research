r"""``LatticeHomomorphisms`` — form-preserving maps between integral lattices.

A morphism \(L\to M\) is an element of \(\operatorname{Hom}(L,M)\): a
\(\mathbb{Z}\)-linear map with \(I\,G_M\,I^{\mathsf T}=G_L\), which is
\(f^*b_M = b_L\) written in matrices.  That is what a :class:`FormMorphism` is
and what it checks on construction, so a lattice morphism is one.  What this
module adds is the homset -- the object whose elements they are -- and the
several ways a caller names one of them.
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.sets_cat import Sets
from sage.matrix.constructor import matrix
from sage.matrix.matrix0 import Matrix
from sage.rings.integer_ring import ZZ


def _hom_images_from_dict(domain: Any, mapping: dict) -> list:
    if domain in DirectSumObjects():
        return _expand_direct_sum_hom_dict(domain, mapping)

    images = dict(mapping)
    ordered = []
    for generator in domain.gens():
        assert generator in images, f"missing image for generator {generator}"
        ordered.append(images[generator])
    return ordered


def _hom_images(domain: Any, codomain: Any, x: Any) -> list:
    r"""Return the images of ``domain``'s generators that ``x`` names.

    A map is where the generators go, and there are three ways to say it: name
    the images one by one, name them by the generator they come from, or give
    the matrix whose rows are their coordinates.  The last is a reading of a
    matrix as a map, so it is stated in one place -- here -- and every row
    becomes an element of the codomain before anything else happens.
    """
    match x:
        case dict():
            return _hom_images_from_dict(domain, x)
        case Matrix():
            rows = matrix(ZZ, x).rows()
            assert len(rows) == len(domain.gens()), (
                f"the matrix has {len(rows)} rows and the domain has "
                f"{len(domain.gens())} generators"
            )
            return [codomain.linear_combination(row) for row in rows]
        case FormMorphism() | ModuleMorphism():
            return _hom_images(domain, codomain, matrix(ZZ, x.matrix()))
        case list() | tuple():
            return list(x)
        case _:
            raise TypeError(
                "a form morphism is specified by images, an image dictionary, "
                "a matrix, or an existing module/form morphism"
            )


class LatticeHomomorphisms(Category):
    r"""Form-preserving homomorphisms of integral lattices."""

    @classmethod
    def _repr_object_names(cls) -> str:
        return "lattice homomorphisms"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""Homset construction: a map is where the generators go."""

        def __call__(self: Any, x: Any, *args: Any, **kwargs: Any) -> Any:
            r"""Build a form-preserving morphism from images, a dictionary, or a matrix.

            For a chosen direct sum, a dictionary may specify images of entire
            summand subobjects.

            Preserving the form is not checked here: the morphism checks it,
            by pulling the codomain's form back along itself and comparing it
            to the domain's, which is the same statement as
            $I\,G_M\,I^{\mathsf T}=G_L$ and is made in one place.
            """
            domain = self.domain()
            codomain = self.codomain()
            images = _hom_images(domain, codomain, x)
            for image in images:
                assert image in codomain, (
                    f"a map into {codomain} sends generators to its elements, "
                    f"and this is {image!r}"
                )
            return domain.hom(images, parent=self)
