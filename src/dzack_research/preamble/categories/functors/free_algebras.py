r"""Tensor and symmetric algebra adjunctions, plus exterior-algebra functoriality."""

from typing import Any, ClassVar

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras import (
    Algebras,
    AlternatingAlgebraOf,
    AlternatingAlgebras,
    CommutativeAlgebras,
    DividedPowerAlgebraOf,
    DividedPowerAlgebras,
    SymmetricAlgebraOf,
    TensorAlgebraOf,
    power_algebra_homset,
)
from dzack_research.preamble.categories.functors.algebra_modules import (
    algebra_underlying_module_functor,
)
from dzack_research.preamble.categories.functors.core import Adjunction, Functor
from dzack_research.preamble.categories.modules import Modules
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    module_coefficients,
    module_homset,
)
from dzack_research.preamble.categories.rings import owned_ring_view


class _ModuleAlgebraFunctor(Functor):
    _constructor: ClassVar[Any] = None
    _codomain_category: ClassVar[Any] = None
    _name = "free algebra"

    def __init__(self, base_ring) -> None:
        self._base_ring = owned_ring_view(base_ring)
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

        return source.hom(image, target)

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
    _codomain_category = CommutativeAlgebras
    _name = "Symmetric algebra"


class AlternatingAlgebraFunctor(Functor):
    r"""Exterior-algebra functor on represented modules.

    No ordinary free/forgetful adjunction is asserted for this construction.
    """

    def __init__(self, base_ring) -> None:
        self._base_ring = owned_ring_view(base_ring)
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
        self._base_ring = owned_ring_view(base_ring)
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
        self._base_ring = owned_ring_view(base_ring)
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
        return free_algebra.hom(
            lambda label: (
                module.realize_module_generator(label)
                if isinstance(module, GradedDirectSumModule)
                else module.module_generator(label)
            ),
            algebra,
        )

    def hom_set_isomorphism_forward(self, morphism):
        r"""Restrict an algebra map \(F(M)\to A\) to degree one."""
        free_algebra = morphism.domain()
        module = free_algebra.free_source_module()
        return self.right_adjoint()(morphism) * self.unit(module)

    def hom_set_isomorphism_inverse(self, morphism, codomain=None):
        r"""Extend an \(R\)-linear map \(M\to U(A)\) multiplicatively."""
        target_module = morphism.codomain()
        algebra = (
            target_module.realized_object()
            if isinstance(target_module, GradedDirectSumModule)
            else target_module
        )
        represented_underlying = self.right_adjoint()(algebra)
        if represented_underlying is not target_module:
            if not isinstance(represented_underlying, GradedDirectSumModule):
                raise ValueError(
                    "the module map does not land in the represented underlying module"
                )
            source_morphism = morphism
            morphism = module_homset(source_morphism.domain(), represented_underlying)(
                lambda label: represented_underlying.from_realization(
                    source_morphism(source_morphism.domain().module_generator(label))
                )
            )
            target_module = represented_underlying
        if codomain is not None and codomain is not algebra:
            raise ValueError(
                "the stated algebra codomain differs from the module map codomain"
            )
        return self.counit(algebra) * self.left_adjoint()(morphism)

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
