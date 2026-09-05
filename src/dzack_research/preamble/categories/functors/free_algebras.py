r"""Tensor and symmetric algebra adjunctions, plus exterior-algebra functoriality."""

from typing import Any, ClassVar

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    CommutativeAlgebras,
)
from dzack_research.preamble.categories.algebras.framed_free_algebras import (
    AlternatingAlgebraOf,
    DividedPowerAlgebraOf,
    SymmetricAlgebraOf,
    TensorAlgebraOf,
)
from dzack_research.preamble.categories.algebras.free_algebras import (
    AlternatingAlgebras,
    DividedPowerAlgebras,
)
from dzack_research.preamble.categories.algebras.power_algebras import power_algebra_homset
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


class _ModuleAlgebraFunctor(Functor):
    _constructor: ClassVar[Any] = None
    _codomain_category: ClassVar[Any] = None
    _name = "free algebra"

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            Modules(self._base_ring),
            self._codomain_category(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, module):
        return self._constructor(module)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target_module = morphism.codomain()
        target = self(target_module)

        def image(label):
            coefficients = module_coefficients(
                morphism(morphism.domain().module_generator(label)),
                target_module,
            )
            return sum(
                (
                    coefficient * target.algebra_generator(target_label)
                    for target_label, coefficient in coefficients.items()
                ),
                target.zero(),
            )

        homset = source.Mor(target)
        return homset._from_degree_preserving_generator_map(image)

    def _repr_(self):
        return f"{self._name} functor on {self.base_ring()}-modules"


class TensorAlgebraFunctor(_ModuleAlgebraFunctor):
    r"""The functor \(T_R:\mathbf{Mod}_R\to\mathbf{Alg}_R\)."""

    _constructor = staticmethod(TensorAlgebraOf)
    _codomain_category = Algebras
    _name = "Tensor algebra"


class SymmetricAlgebraFunctor(_ModuleAlgebraFunctor):
    r"""The functor \(\operatorname{Sym}_R:\mathbf{Mod}_R\to\mathbf{CAlg}_R\)."""

    _constructor = staticmethod(SymmetricAlgebraOf)
    _codomain_category = staticmethod(CommutativeAlgebras)
    _name = "Symmetric algebra"


class AlternatingAlgebraFunctor(Functor):
    r"""Exterior-algebra functor on represented modules.

    No ordinary free/forgetful adjunction is asserted for this construction.
    """

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            Modules(self._base_ring),
            AlternatingAlgebras(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, module):
        return AlternatingAlgebraOf(module)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return power_algebra_homset(source, target)(morphism)

    def _repr_(self):
        return f"Alternating algebra functor on {self.base_ring()}-modules"


class DividedPowerAlgebraFunctor(Functor):
    r"""The divided-power algebra functor ``Gamma_R : Mod_R -> DPAlg_R``."""

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            Modules(self._base_ring),
            DividedPowerAlgebras(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, module):
        return DividedPowerAlgebraOf(module)

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return power_algebra_homset(source, target)(morphism)

    def _repr_(self):
        return f"Divided-power algebra functor on {self.base_ring()}-modules"


@cached_function
def tensor_algebra_functor(base_ring) -> TensorAlgebraFunctor:
    return TensorAlgebraFunctor(base_ring)


@cached_function
def symmetric_algebra_functor(base_ring) -> SymmetricAlgebraFunctor:
    return SymmetricAlgebraFunctor(base_ring)


class _ModuleAlgebraAdjunction(Adjunction):
    _left_functor_factory: ClassVar[Any] = None
    _name = "module-algebra"

    def __init__(self, base_ring) -> None:
        self._base_ring = _owned_ring(base_ring)
        left = self._left_functor_factory(self._base_ring)
        right = algebra_underlying_module_functor(
            self._base_ring,
            left.codomain(),
        )
        super().__init__(left, right)

    def base_ring(self):
        return self._base_ring

    def unit(self, module):
        r"""The degree-one inclusion \(M\to U(F(M))\)."""
        free_algebra = self.left_adjoint()(module)
        underlying = self.right_adjoint()(free_algebra)
        return module_homset(module, underlying)(
            lambda label: (
                underlying.from_realization(free_algebra.algebra_generator(label))
                if isinstance(underlying, GradedDirectSumModule)
                else free_algebra.algebra_generator(label)
            )
        )

    def counit(self, algebra):
        r"""Evaluation \(F(U(A))\to A\) when ``U(A)`` is represented."""
        module = self.right_adjoint()(algebra)
        free_algebra = self.left_adjoint()(module)
        homset = free_algebra.Mor(algebra)

        def image(label):
            return (
                module.realize_module_generator(label)
                if isinstance(module, GradedDirectSumModule)
                else module.module_generator(label)
            )

        return homset._from_degree_preserving_generator_map(image)


    def _repr_(self):
        return f"{self._name} adjunction over {self.base_ring()}"


class TensorAlgebraAdjunction(_ModuleAlgebraAdjunction):
    r"""The adjunction \(T_R\dashv U:\mathbf{Mod}_R\leftrightarrows\mathbf{Alg}_R\)."""

    _left_functor_factory = staticmethod(tensor_algebra_functor)
    _name = "Tensor-algebra/underlying-module"


class SymmetricAlgebraAdjunction(_ModuleAlgebraAdjunction):
    r"""The adjunction \(\operatorname{Sym}_R\dashv U\) for commutative algebras."""

    _left_functor_factory = staticmethod(symmetric_algebra_functor)
    _name = "Symmetric-algebra/underlying-module"


@cached_function
def alternating_algebra_functor(base_ring) -> AlternatingAlgebraFunctor:
    return AlternatingAlgebraFunctor(base_ring)


@cached_function
def divided_power_algebra_functor(base_ring) -> DividedPowerAlgebraFunctor:
    return DividedPowerAlgebraFunctor(base_ring)


@cached_function
def tensor_algebra_adjunction(base_ring) -> TensorAlgebraAdjunction:
    return TensorAlgebraAdjunction(base_ring)


@cached_function
def symmetric_algebra_adjunction(base_ring) -> SymmetricAlgebraAdjunction:
    return SymmetricAlgebraAdjunction(base_ring)


__all__ = [
    "AlternatingAlgebraFunctor",
    "DividedPowerAlgebraFunctor",
    "SymmetricAlgebraAdjunction",
    "SymmetricAlgebraFunctor",
    "TensorAlgebraAdjunction",
    "TensorAlgebraFunctor",
    "alternating_algebra_functor",
    "divided_power_algebra_functor",
    "symmetric_algebra_adjunction",
    "symmetric_algebra_functor",
    "tensor_algebra_adjunction",
    "tensor_algebra_functor",
]
