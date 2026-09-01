r"""The forgetful functor \(U\colon R\text{-}\mathbf{Alg}\to R\text{-}\mathbf{Mod}\).

An associative unital \(R\)-algebra is already an \(R\)-module.  Finite
module-backed algebras use that carrier directly.  A represented free algebra
has infinitely many homogeneous generators as a module, so its carrier is the
finite-support direct sum of its actual presented homogeneous pieces.
"""

from sage.misc.cachefunc import cached_function
from sage.categories.morphism import Morphism
from typing import Any, cast

from dzack_research.preamble.categories.algebras.algebras import Algebras
from dzack_research.preamble.categories.algebras.free_algebras import (
    SymmetricAlgebras,
    TensorAlgebras,
)
from dzack_research.preamble.categories.functors.core import Functor
from dzack_research.preamble.categories.modules.graded_direct_sums import (
    GradedDirectSumModule,
)
from dzack_research.preamble.categories.modules.module_morphisms.module_morphisms import (
    ModuleMorphism,
    module_homset,
)
from dzack_research.preamble.categories.modules.pure.modules import Modules
from dzack_research.preamble.categories.rings import engine_ring, owned_ring_view


def _nested_tensor_label(word):
    word = tuple(word)
    if not word:
        return 0
    result = word[0]
    for label in word[1:]:
        result = (result, label)
    return result


def _flatten_tensor_label(label, degree):
    if degree == 1:
        return (label,)
    left, right = label
    return _flatten_tensor_label(left, degree - 1) + (right,)


def _presentation_element(algebra, element):
    if hasattr(algebra, "lift_to_presentation"):
        return algebra.lift_to_presentation(element)
    return engine_ring(algebra)(element)


def _free_algebra_piece(algebra, degree):
    return algebra.graded_piece(degree)


def _free_algebra_underlying_module(algebra, source, flavor):
    realization_maps = {}

    def piece(degree):
        return _free_algebra_piece(algebra, degree)

    def generator_word(degree, label):
        if degree == 0:
            return algebra.one()
        if degree == 1:
            return algebra.algebra_generator(label)
        if flavor == "tensor":
            factors = (
                algebra.algebra_generator(source_label)
                for source_label in _flatten_tensor_label(label, degree)
            )
        else:
            source_labels = tuple(source.module_generating_set())
            factors = (
                algebra.algebra_generator(source_label)
                for source_label, exponent in zip(
                    source_labels, tuple(label), strict=True
                )
                for _ in range(int(exponent))
            )
        result = algebra.one()
        for factor in factors:
            result *= factor
        return result

    def realization_map(degree):
        degree = int(degree)
        cached = realization_maps.get(degree)
        if cached is not None:
            return cached
        homogeneous_piece = piece(degree)
        realized = module_homset(homogeneous_piece, algebra)(
            lambda label: generator_word(degree, label)
        )
        realization_maps[degree] = realized
        return realized

    direct_sum = None

    def realize_generator(degree, label):
        homogeneous_piece = piece(degree)
        return realization_map(degree)(homogeneous_piece.module_generator(label))

    def from_realization(element):
        presented = _presentation_element(algebra, element)
        source_labels = tuple(source.module_generating_set())
        coefficients_by_degree = {}

        if flavor == "tensor":
            generator_labels = dict(
                zip(presented.parent().monoid().gens(), source_labels, strict=True)
            )
            terms = []
            for monomial, coefficient in presented.monomial_coefficients().items():
                word = tuple(
                    generator_labels[generator]
                    for generator, exponent in monomial
                    for _ in range(int(exponent))
                )
                terms.append((len(word), _nested_tensor_label(word), coefficient))
        else:
            terms = []
            for monomial, coefficient in presented.monomial_coefficients().items():
                try:
                    exponents = tuple(int(exponent) for exponent in monomial)
                except TypeError:
                    if hasattr(monomial, "exponents"):
                        exponents = tuple(
                            int(exponent) for exponent in monomial.exponents()[0]
                        )
                    else:
                        exponents = (int(monomial),)
                degree = sum(exponents)
                if degree == 0:
                    label = 0
                elif degree == 1:
                    label = source_labels[exponents.index(1)]
                else:
                    label = exponents
                terms.append((degree, label, coefficient))

        for degree, label, coefficient in terms:
            degree_coefficients = coefficients_by_degree.setdefault(degree, {})
            degree_coefficients[label] = degree_coefficients.get(
                label, algebra.base_ring().zero()
            ) + algebra.base_ring()(coefficient)
        return direct_sum.from_components(
            {
                degree: piece(degree).linear_combination(coefficients)
                for degree, coefficients in coefficients_by_degree.items()
            }
        )

    direct_sum = GradedDirectSumModule(
        algebra.base_ring(),
        piece,
        name=f"Underlying graded module of {algebra}",
        realize_generator=realize_generator,
        realized_object=algebra,
        from_realization=from_realization,
    )
    return direct_sum


_FREE_ALGEBRA_UNDERLYING_CACHE: dict[tuple[int, str], GradedDirectSumModule] = {}


class UnderlyingAlgebraModuleMorphism(ModuleMorphism):
    r"""An algebra morphism read as its underlying linear map."""

    def __init__(self, parent, algebra_morphism) -> None:
        Morphism.__init__(self, parent)
        self._algebra_morphism = algebra_morphism

    def _generator_image(self, label):
        domain = cast(Any, self.domain())
        return self._call_(domain.module_generator(label))

    def _call_(self, element):
        source = self.domain()
        target = self.codomain()
        if isinstance(source, GradedDirectSumModule):
            element = source.realize(element)
        image = self._algebra_morphism(element)
        if isinstance(target, GradedDirectSumModule):
            return target.from_realization(image)
        return image

    def algebra_morphism(self):
        return self._algebra_morphism


class AlgebraUnderlyingModuleFunctor(Functor):
    r"""\(U\colon\mathbf{Alg}_R\to\mathbf{Mod}_R\)."""

    def __init__(self, base_ring, algebra_category=None) -> None:
        self._base_ring = owned_ring_view(base_ring)
        domain = (
            Algebras(self._base_ring) if algebra_category is None else algebra_category
        )
        if not domain.is_subcategory(Algebras(self._base_ring)):
            raise ValueError(
                "the underlying-module functor starts on an algebra category"
            )
        super().__init__(domain, Modules(self._base_ring))

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, algebra):
        from dzack_research.preamble.categories.algebras.sparse_free_algebras import (
            SparseFreeAlgebra,
        )

        if isinstance(algebra, SparseFreeAlgebra):
            return algebra

        ring = self.base_ring()
        if algebra in TensorAlgebras(ring):
            flavor = "tensor"
        elif algebra in SymmetricAlgebras(ring):
            flavor = "symmetric"
        else:
            return algebra

        try:
            source = algebra.free_source_module()
        except (AttributeError, ValueError):
            return algebra
        key = (id(algebra), flavor)
        cached = _FREE_ALGEBRA_UNDERLYING_CACHE.get(key)
        if cached is not None and cached.realized_object() is algebra:
            return cached
        module = _free_algebra_underlying_module(algebra, source, flavor)
        _FREE_ALGEBRA_UNDERLYING_CACHE[key] = module
        return module

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        return UnderlyingAlgebraModuleMorphism(
            module_homset(source, target),
            morphism,
        )

    def _repr_(self):
        return f"Underlying-module functor on {self.base_ring()}-algebras"


@cached_function
def algebra_underlying_module_functor(
    base_ring,
    algebra_category=None,
) -> AlgebraUnderlyingModuleFunctor:
    return AlgebraUnderlyingModuleFunctor(base_ring, algebra_category)


__all__ = [
    "AlgebraUnderlyingModuleFunctor",
    "UnderlyingAlgebraModuleMorphism",
    "algebra_underlying_module_functor",
]
