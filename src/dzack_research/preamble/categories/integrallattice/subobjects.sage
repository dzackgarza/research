r"""Subobjects of integral lattices."""

from typing import Any

from sage.structure.category_object import CategoryObject


class Subobject(CategoryObject):
    r"""A pair \((L_i, f)\) with an embedding \(f: L_i\to L\)."""

    def __init__(self, embedding: Any) -> None:
        self._embedding = embedding
        refine(self, IntegralLattices().Subobjects())

    def embedding(self) -> Any:
        r"""Return \(f: L_i\to L\)."""
        return self._embedding

    def embedding_codomain(self) -> Any:
        r"""Return \(L\)."""
        return self.embedding().codomain()

    def embedded_gens(self) -> tuple:
        r"""Return the images under \(f\) of the generators of \(L_i\)."""
        return tuple(
            self.embedding()(generator)
            for generator in self.embedding().domain().gens()
        )

    def __repr__(self) -> str:
        return f"Subobject(embedding={self._embedding!r})"
