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
For a represented closed immersion into projective space this module also
realizes the object ``i^*O_P(d)``.  The quasi-coherent Hom represents arrows
between such pullback objects by pulling back their ambient line-bundle maps;
this bounded realization does not claim a pullback functor on arbitrary
non-affine quasi-coherent sheaves.
"""

from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.abstract_categories.hom_categories import (
    CategoricalIsomorphism,
)
from dzack_research.preamble.categories.schemes.ringed_spaces import (
    QuasiCoherentSheaves,
)


class _AffineQuasiCoherentFunctor(Functor):
    r"""Common raising layer for one affine quasi-coherent sheaf functor."""

    def __init__(self, scheme_morphism, underlying_functor, domain_scheme, codomain_scheme) -> None:
        self._scheme_morphism = scheme_morphism
        self._underlying_functor = underlying_functor
        super().__init__(
            QuasiCoherentSheaves(domain_scheme),
            QuasiCoherentSheaves(codomain_scheme),
        )

    def scheme_morphism(self):
        return self._scheme_morphism

    def underlying_module_functor(self):
        return self._underlying_functor

    def _apply_object(self, sheaf):
        source_module = self.domain().global_sections(sheaf)
        target_module = self.underlying_module_functor()(source_module)
        return self.codomain().associated_sheaf(target_module)

    def _apply_morphism(self, morphism):
        r"""Apply the module functor and raise the result back to the sheaf Hom."""
        source = self(morphism.domain())
        target = self(morphism.codomain())
        match morphism:
            case CategoricalIsomorphism():
                forward = self.on_morphism(morphism.forward())
                inverse = self.on_morphism(morphism.inverse())
                return self.codomain().Core().Mor(source, target)(forward, inverse)
            case _:
                pass
        underlying = self.underlying_module_functor()(
            morphism.underlying_module_morphism()
        )
        return self.codomain().Mor(source, target)(underlying)


class AffineQuasiCoherentPullbackFunctor(_AffineQuasiCoherentFunctor):
    r"""``f^* : QCoh(Y) -> QCoh(X)`` for an affine ``f:X->Y``."""

    def _repr_(self):
        return f"Quasi-coherent pullback along {self.scheme_morphism()}"


class AffineQuasiCoherentDirectImageFunctor(_AffineQuasiCoherentFunctor):
    r"""``f_* : QCoh(X) -> QCoh(Y)`` for an affine ``f:X->Y``."""

    def _repr_(self):
        return f"Affine quasi-coherent direct image along {self.scheme_morphism()}"


class AffineQuasiCoherentAdjunction(Adjunction):
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
        super().__init__(self._pullback, self._direct_image)

    def scheme_morphism(self):
        return self._scheme_morphism

    pullback_functor = Adjunction.left_adjoint
    direct_image_functor = Adjunction.right_adjoint

    def underlying_module_adjunction(self):
        return self._module_adjunction

    def unit(self, sheaf):
        r"""Return ``F -> f_* f^* F`` in the quasi-coherent sheaf Hom."""
        pulled = self.left_adjoint().on_object(sheaf)
        pushed = self.right_adjoint().on_object(pulled)
        unit = self.underlying_module_adjunction().unit(sheaf.module())
        if unit.domain() is not sheaf.module() or unit.codomain() is not pushed.module():
            raise ArithmeticError("the affine sheaf adjunction unit has the wrong module endpoints")
        return self.left_adjoint().domain().Mor(sheaf, pushed)(unit)

    def counit(self, sheaf):
        r"""Return ``f^* f_* G -> G`` in the quasi-coherent sheaf Hom."""
        pushed = self.right_adjoint().on_object(sheaf)
        pulled = self.left_adjoint().on_object(pushed)
        counit = self.underlying_module_adjunction().counit(sheaf.module())
        if counit.domain() is not pulled.module() or counit.codomain() is not sheaf.module():
            raise ArithmeticError("the affine sheaf adjunction counit has the wrong module endpoints")
        return self.left_adjoint().codomain().Mor(pulled, sheaf)(counit)

    def _repr_(self):
        return f"Affine quasi-coherent pullback/direct-image adjunction along {self.scheme_morphism()}"


def _affine_quasi_coherent_adjunction(scheme_morphism):
    r"""Return the affine ``f^* \dashv f_*`` owner for ``scheme_morphism``."""
    return AffineQuasiCoherentAdjunction(scheme_morphism)


def _projective_closed_immersion_module_pullback(scheme_morphism, sheaf):
    r"""Realize ``i^* O_P(d)`` for a represented projective closed immersion.

    This is the object part of quasi-coherent pullback in the one non-affine
    regime whose target object is already represented.  It is deliberately not
    exposed as a ``Functor`` until the common non-affine quasi-coherent Hom
    supplies the arrow action.
    """
    from dzack_research.preamble.categories.divisors.invertible_sheaves import (
        _ProjectiveSpaceLineBundleEngine,
        _projective_subscheme_line_bundle,
    )

    match sheaf:
        case _ProjectiveSpaceLineBundleEngine() if (
            sheaf.projective_space() is scheme_morphism.codomain()
        ):
            return _projective_subscheme_line_bundle(
                scheme_morphism.domain(),
                sheaf,
                pullback_morphism=scheme_morphism,
            )
        case _:
            raise AssertionError(
                "projective closed-immersion pullback is presently realized for standard O(d) objects"
            )


__all__ = [
    "AffineQuasiCoherentAdjunction",
    "AffineQuasiCoherentDirectImageFunctor",
    "AffineQuasiCoherentPullbackFunctor",
]
