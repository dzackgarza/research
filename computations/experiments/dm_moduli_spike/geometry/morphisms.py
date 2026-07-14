r"""Morphisms between moduli stacks and coarse moduli schemes."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..moduli.coarse import CoarseModuliScheme
    from ..moduli.instances import ModuliStack


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
    r"""Universal coarse moduli map `\mathcal M_{g,n} \to M_{g,n}`."""

    def __init__(self, stack: ModuliStack, coarse: CoarseModuliScheme) -> None:
        super().__init__(stack, coarse)

    def coarse_scheme(self) -> CoarseModuliScheme:
        from ..moduli.coarse import CoarseModuliScheme

        assert isinstance(self._codomain, CoarseModuliScheme)
        return self._codomain

    def coarse_space(self) -> CoarseModuliScheme:
        r"""Deprecated alias for :meth:`coarse_scheme`."""
        return self.coarse_scheme()
