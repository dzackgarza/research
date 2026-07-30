r"""Subobjects of integral lattices."""

from typing import Any

from sage.structure.category_object import CategoryObject
from sage.structure.element import Vector


class Subobject(CategoryObject):
    r"""A pair \((L_i, f)\) with an embedding \(f: L_i\to L\)."""

    def __init__(self, embedding: Any) -> None:
        self._embedding = embedding
        # The category comes from where the embedding lands: a subobject of a
        # lattice and a subobject of a torsion form are subobjects of different
        # things, and only the codomain knows which.
        refine(self, embedding.codomain().category().Subobjects())

    def embedding(self) -> Any:
        r"""Return \(f: L_i\to L\)."""
        return self._embedding

    def embedding_codomain(self) -> Any:
        r"""Return \(L\)."""
        return self.embedding().codomain()

    def embedded_gens(self) -> tuple:
        r"""Return the images under \(f\) of the generators of \(L_i\).

        Images are finished lattice elements and are made immutable — like
        Sage's own ``gens()`` — so they can serve as dict keys (the
        generator-image join in ``_expand_direct_sum_hom_dict``).
        """
        images = []
        for generator in self.embedding().domain().gens():
            image = self.embedding()(generator)
            # Freezing is a property of Sage vectors, not of elements at large:
            # a lattice element is one and a torsion class is not.
            if isinstance(image, Vector):
                image.set_immutable()
            images.append(image)
        return tuple(images)

    def __repr__(self) -> str:
        return f"Subobject(embedding={self._embedding!r})"
