r"""Subobjects: objects of the slice category, not pairs.

A subobject of \(L\) is an object of \(\mathcal C_{/L}\) -- an object of
\(\mathcal C\) equipped with a structure morphism into \(L\), which here is
mono.  It *is* that object: it has the rank, the generators, the form and the
radical it has, and asking any of them is asking it, not something reachable
through it.  There are projections to \(\mathcal C\) and to
\(\operatorname{Ar}(\mathcal C)\), but it is not their product and there is no
pair to take apart.

So this module does not wrap.  It takes the object the inclusion starts from,
attaches the inclusion as structure, and refines it -- exactly the way a form
module is a module equipped with a form.  Nothing is delegated, because there
is nothing to delegate through.
"""

from typing import Any

from sage.categories.category import Category
from sage.categories.sets_cat import Sets


class Subobjects(Category):
    r"""Objects equipped with a mono into another object.

    What the structure adds, and all it adds: the morphism, and the images of
    the generators under it.  Everything else an object of this category can be
    asked is what it could be asked anyway -- it is still a lattice, or a
    torsion form, and it stayed in its own category when it acquired this one.
    """

    @classmethod
    def _repr_object_names(cls) -> str:
        return "subobjects"

    def super_categories(self) -> list:
        return [Sets()]

    class ParentMethods:
        r"""The structure morphism, and what is read off it."""

        def embedding(self: Any) -> Any:
            r"""Return the structure morphism $\iota: A\to L$."""
            return self._structure_morphism

        def embedding_codomain(self: Any) -> Any:
            r"""Return $L$, the object this one is a subobject of."""
            return self.embedding().codomain()

        def index(self: Any) -> Any:
            r"""Return the index of this subobject in its codomain."""
            return self.embedding().index()

        def isotropic_reduction(self: Any) -> Any:
            r"""Return $I^{\perp}/I$ with its induced form, for $I$ this subobject.

            Defined for any isotropic sub-form-module, which is what makes this
            one construction rather than a family of them: $I$ isotropic means
            the form vanishes on it, hence $I\subseteq I^{\perp}$, hence the
            quotient exists and the form descends to it -- moving a
            representative by an element of $I$ changes a pairing by something
            $I$ pairs to zero.

            An element's version is the same construction on the rank-one
            subobject it spans; a single isotropic $e$ is not a different case.

            The result is a form module of the ambient's kind -- a lattice
            where the ambient is one -- and its form can be degenerate, since
            nothing here says $I$ was all of the radical of $I^{\perp}$.
            """
            ambient = self.embedding_codomain()
            gram = self.gram_matrix()
            assert gram.is_zero(), (
                f"isotropic reduction is defined for an isotropic subobject, "
                f"and the form restricted to this one is {gram.list()}. "
                "I ⊆ I^perp is what makes the quotient exist, and it is what "
                "fails here."
            )
            perp = self.embedding().orthogonal_complement()
            inside = perp.embedding()
            relations = matrix(
                ZZ,
                [
                    inside.lift(image)._coordinates()
                    for image in self.embedded_gens()
                ],
            )
            lifts = _free_quotient_lifts(perp.rank(), relations)
            induced = matrix(
                ZZ,
                [
                    [
                        perp.linear_combination(u).b(perp.linear_combination(v))
                        for v in lifts
                    ]
                    for u in lifts
                ],
            )
            assert induced.is_symmetric(), "induced form is not symmetric"
            return ambient._sub_form_module(induced)

        def embedded_gens(self: Any) -> tuple:
            r"""Return the images in $L$ of this object's generators.

            Elements of $L$, not of this object: the two are related by
            $\iota$ and by nothing else, which is why they are asked for
            separately from :meth:`gens`.

            Images are owned elements of $L$, so they are already suitable as
            dict keys for the generator-image join in
            ``_expand_direct_sum_hom_dict``.
            """
            images = []
            for generator in self.gens():
                image = self.embedding()(generator)
                images.append(image)
            return tuple(images)


def _free_quotient_lifts(rank: Any, relations: Matrix) -> list:
    r"""Return coordinate lifts of generators of $R^{\text{rank}}/\langle\text{relations}\rangle$.

    Farmed out: a quotient of a free module by a submodule is a Smith form
    computation, and Sage's free modules are where it is implemented.
    Coordinates go out and coordinates come back; the objects built here do not
    leave this function.
    """
    from sage.modules.free_module import FreeModule as _sage_free_module

    ambient = _sage_free_module(ZZ, rank)
    quotient = ambient / ambient.submodule(matrix(ZZ, relations).rows())
    return [generator.lift() for generator in quotient.gens()]


def Subobject(embedding: Any) -> Any:
    r"""Return ``embedding``'s domain, equipped with it as structure.

    The construction, and it constructs nothing: the object already exists --
    it is where the inclusion starts -- so what happens here is that it
    acquires the morphism and the category that says it has one.  Calling this
    twice on one object with different inclusions would be two different
    subobjects claiming the same object, which the assertion below refuses.
    """
    subobject = embedding.domain()
    existing = getattr(subobject, "_structure_morphism", None)
    assert existing is None or existing is embedding, (
        f"{subobject} is already a subobject of {existing.codomain()}, and a "
        "second inclusion would make one object two subobjects. Build the "
        "object again for the other inclusion."
    )
    subobject._structure_morphism = embedding
    return refine(subobject, [subobject.category(), Subobjects()])
