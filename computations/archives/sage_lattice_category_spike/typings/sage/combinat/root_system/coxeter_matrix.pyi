from collections.abc import Hashable, Sequence
from typing import Self

from sage.graphs.graph import Graph
from sage.rings.infinity import PlusInfinity
from sage.rings.integer import Integer

class CoxeterMatrix:
    def __new__(
        cls,
        data: object,
        index_set: Sequence[Hashable] | None = ...,
    ) -> Self: ...

    def index_set(self) -> tuple[Hashable, ...]: ...
    def __getitem__(
        self,
        key: tuple[Hashable, Hashable],
    ) -> Integer | PlusInfinity: ...
    def coxeter_graph(self) -> Graph: ...
    def is_finite(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
