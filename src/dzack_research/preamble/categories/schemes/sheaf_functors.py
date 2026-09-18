r"""Functorial pullback and direct image for represented affine module sheaves.

For an affine morphism ``f : Spec(B) -> Spec(A)``, quasi-coherent sheaves are
represented by modules and the familiar adjunction is exactly scalar
extension/restriction along ``f^# : A -> B``::

    f^* = B tensor_A -  \dashv  f_* = Res_{f^#}.

This module does not recompute either operation. It raises the existing module
base-change adjunction through the affine module/sheaf equivalence and retains
one associated sheaf for every cached module image. The topological inverse
image ``f^{-1}`` remains distinct; finite-atlas inverse images are represented
in ``categories.schemes.gluing`` before scalar extension to module pullback.
"""

from sage.structure.sage_object import SageObject

from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    QuasiCoherentSheaves,
)


class _AffineQuasiCoherentFunctor(SageObject):
    r"""Common raising layer for one affine quasi-coherent sheaf functor."""

    def __init__(self, scheme_morphism, underlying_functor, domain_scheme, codomain_scheme) -> None:
        self._scheme_morphism = scheme_morphism
        self._underlying_functor = underlying_functor
        self._domain_category = QuasiCoherentSheaves(domain_scheme)
        self._codomain_category = QuasiCoherentSheaves(codomain_scheme)
        self._object_images = []

    def scheme_morphism(self):
        return self._scheme_morphism

    def domain(self):
        return self._domain_category

    def codomain(self):
        return self._codomain_category

    def underlying_module_functor(self):
        return self._underlying_functor

    def _cached_object_image(self, sheaf):
        for source, target in self._object_images:
            if source is sheaf:
                return target
        return None

    def on_object(self, sheaf):
        if sheaf not in self.domain():
            raise TypeError("the affine quasi-coherent functor requires a quasi-coherent sheaf on its source")
        cached = self._cached_object_image(sheaf)
        if cached is not None:
            return cached
        source_module = self.domain().global_sections(sheaf)
        target_module = self.underlying_module_functor()(source_module)
        target = self.codomain().associated_sheaf(target_module)
        self._object_images.append((sheaf, target))
        return target

    def on_morphism(self, morphism):
        r"""Apply the underlying module functor to an affine sheaf morphism."""
        return self.underlying_module_functor()(morphism)

class AffineQuasiCoherentPullbackFunctor(_AffineQuasiCoherentFunctor):
    r"""``f^* : QCoh(Y) -> QCoh(X)`` for an affine ``f:X->Y``."""

    def _repr_(self):
        return f"Quasi-coherent pullback along {self.scheme_morphism()}"


class AffineQuasiCoherentDirectImageFunctor(_AffineQuasiCoherentFunctor):
    r"""``f_* : QCoh(X) -> QCoh(Y)`` for an affine ``f:X->Y``."""

    def _repr_(self):
        return f"Affine quasi-coherent direct image along {self.scheme_morphism()}"


class AffineQuasiCoherentAdjunction(SageObject):
    r"""The affine adjunction ``f^* \dashv f_*`` raised from modules."""

    def __init__(self, scheme_morphism) -> None:
        self._scheme_morphism = scheme_morphism
        ring_map = scheme_morphism.coordinate_algebra_morphism()
        if ring_map.domain() is not scheme_morphism.codomain().coordinate_algebra():
            raise ValueError("the scheme pullback has the wrong affine codomain algebra")
        if ring_map.codomain() is not scheme_morphism.domain().coordinate_algebra():
            raise ValueError("the scheme pullback has the wrong affine domain algebra")
        self._module_adjunction = Modules(ring_map.domain()).base_change_adjunction(ring_map)
        self._pullback = AffineQuasiCoherentPullbackFunctor(
            scheme_morphism,
            self._module_adjunction.left_adjoint(),
            scheme_morphism.codomain(),
            scheme_morphism.domain(),
        )
        self._direct_image = AffineQuasiCoherentDirectImageFunctor(
            scheme_morphism,
            self._module_adjunction.right_adjoint(),
            scheme_morphism.domain(),
            scheme_morphism.codomain(),
        )

    def scheme_morphism(self):
        return self._scheme_morphism

    def left_adjoint(self):
        return self._pullback

    pullback_functor = left_adjoint

    def right_adjoint(self):
        return self._direct_image

    direct_image_functor = right_adjoint

    def underlying_module_adjunction(self):
        return self._module_adjunction

    def unit(self, sheaf):
        r"""Return ``F -> f_* f^* F`` as its represented module morphism."""
        pulled = self.left_adjoint().on_object(sheaf)
        pushed = self.right_adjoint().on_object(pulled)
        unit = self.underlying_module_adjunction().unit(sheaf.module())
        if unit.domain() is not sheaf.module() or unit.codomain() is not pushed.module():
            raise ArithmeticError("the affine sheaf adjunction unit has the wrong module endpoints")
        return unit

    def counit(self, sheaf):
        r"""Return ``f^* f_* G -> G`` as its represented module morphism."""
        pushed = self.right_adjoint().on_object(sheaf)
        pulled = self.left_adjoint().on_object(pushed)
        counit = self.underlying_module_adjunction().counit(sheaf.module())
        if counit.domain() is not pulled.module() or counit.codomain() is not sheaf.module():
            raise ArithmeticError("the affine sheaf adjunction counit has the wrong module endpoints")
        return counit

    def _repr_(self):
        return f"Affine quasi-coherent pullback/direct-image adjunction along {self.scheme_morphism()}"


def _affine_quasi_coherent_adjunction(scheme_morphism):
    r"""Return the affine ``f^* \dashv f_*`` owner for ``scheme_morphism``."""
    return AffineQuasiCoherentAdjunction(scheme_morphism)


__all__ = [
    "AffineQuasiCoherentAdjunction",
    "AffineQuasiCoherentDirectImageFunctor",
    "AffineQuasiCoherentPullbackFunctor",
]
