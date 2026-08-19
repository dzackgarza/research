"""Free and torsion bilinear module carriers.

FreeBilinearModule: free R-module with bilinear form.
TorsionBilinearModule: finite torsion module with bilinear form.
"""

from __future__ import annotations

from collections.abc import Iterable
from typing import Any

from sage.structure.parent import Parent


class FreeBilinearModule(Parent):
    """Free R-module of rank n equipped with a bilinear form."""

    def __init__(
        self,
        base_ring: object,
        rank: int,
        gram_matrix: Any | None = None,
        form: Any | None = None,
        codomain: Any | None = None,
    ) -> None:
        self._rank = rank
        self._gram = gram_matrix
        self._form = form
        self._cd = codomain
        Parent.__init__(self, base=base_ring)

    def rank(self) -> int:
        return self._rank

    def gram_matrix(self) -> Any | None:
        return self._gram

    def form(self) -> Any | None:
        return self._form

    def codomain(self) -> Any | None:
        return self._cd

    def span(self, elements: object) -> Any:
        raise NotImplementedError

    def perp(self) -> Any:
        raise NotImplementedError


class TorsionBilinearModule(Parent):
    """Finite torsion R-module with bilinear form (e.g., discriminant form)."""

    def __init__(
        self,
        base_ring: object,
        invariants: Iterable[object],
        gram_matrix: Any | None = None,
        form: Any | None = None,
        codomain: Any | None = None,
    ) -> None:
        self._invariants = tuple(invariants) if invariants else ()
        self._gram = gram_matrix
        self._form = form
        self._cd = codomain
        Parent.__init__(self, base=base_ring)

    def invariants(self) -> tuple[object, ...]:
        return self._invariants

    def gram_matrix(self) -> Any | None:
        return self._gram

    def form(self) -> Any | None:
        return self._form

    def codomain(self) -> Any | None:
        return self._cd

    @classmethod
    def from_invariants_and_gram(
        cls,
        base_ring: object,
        invariants: Iterable[object],
        gram: Any,
        codomain: Any | None = None,
    ) -> TorsionBilinearModule:
        return cls(base_ring, invariants, gram_matrix=gram, codomain=codomain)
