r"""Morphisms between moduli and coarse moduli objects."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..moduli.coarse import CoarseModuliSpace
    from ..moduli.stack import DeligneMumfordModuliStack


class ModuliMorphism:
    r"""Base class for morphisms in the moduli landscape."""

    __slots__ = ("_domain", "_codomain")

    def __init__(self, domain: object, codomain: object) -> None:
        self._domain = domain
        self._codomain = codomain

    def domain(self) -> object:
        return self._domain

    def codomain(self) -> object:
        return self._codomain


class OpenImmersion(ModuliMorphism):
    r"""Open immersion `j : X \hookrightarrow \overline X` of moduli stacks."""

    def is_open_immersion(self) -> bool:
        return True


class CoarseModuliMap(ModuliMorphism):
    r"""Universal coarse moduli map `\mathcal M \to M`."""

    def __init__(self, stack: DeligneMumfordModuliStack, coarse: CoarseModuliSpace) -> None:
        super().__init__(stack, coarse)

    def coarse_space(self) -> CoarseModuliSpace:
        from ..moduli.coarse import CoarseModuliSpace

        assert isinstance(self._codomain, CoarseModuliSpace)
        return self._codomain
