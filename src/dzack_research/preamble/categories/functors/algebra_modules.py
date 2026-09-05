r"""The forgetful functor \(U\colon R\text{-}\mathbf{Alg}\to R\text{-}\mathbf{Mod}\).

An associative unital \(R\)-algebra is already an \(R\)-module.  Finite
module-backed algebras use that module directly.  A represented free algebra
has infinitely many homogeneous generators as a module, so its underlying module is the
finite-support direct sum of its actual presented homogeneous pieces.
"""

from sage.misc.cachefunc import cached_function
from sage.categories.morphism import Morphism
from typing import Any, cast

from dzack_research.preamble.categories.algebras.algebras import (
    Algebras,
    AlgebrasWithChosenFinitePresentation,
)
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
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_ring,
)


from dzack_research.preamble.categories.modules.tensor_products import (
    _flatten_tensor_label,
    _nested_tensor_label,
)
from dzack_research.preamble.categories.algebras.sparse_free_algebras import SparseFreeAlgebra


def _presentation_element(algebra, element):
    if hasattr(algebra, "lift_to_presentation"):
        return algebra.lift_to_presentation(element)
    return _engine_ring(algebra)(element)


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
            factors = (
                algebra.algebra_generator(source_label)
                for source_label in label
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
        coefficients_by_degree = {}
        source_labels = source.module_generating_set()


        if isinstance(algebra, SparseFreeAlgebra):
            sparse = algebra(element)
            raw_terms = sparse.monomial_coefficients().items()
            if flavor == "tensor":
                terms = (
                    (
                        len(word),
                        _nested_tensor_label(source, word),
                        coefficient,
                    )
                    for word, coefficient in raw_terms
                )
            else:
                def symmetric_sparse_term(item):
                    monomial, coefficient = item
                    multiplicities = {
                        label: int(exponent)
                        for label, exponent in monomial
                    }
                    degree = sum(multiplicities.values())
                    if degree == 0:
                        label = 0
                    elif degree == 1:
                        label = next(iter(multiplicities))
                    else:
                        label = piece(degree).module_generating_set().from_multiplicities(
                            multiplicities
                        )
                    return degree, label, coefficient

                terms = (symmetric_sparse_term(item) for item in raw_terms)
        else:
            if algebra in AlgebrasWithChosenFinitePresentation(algebra.base_ring()):
                presentation = algebra.presentation_ring()
                presented = algebra.lift_to_presentation(element)
            else:
                presentation = algebra
                presented = algebra(element)
            backend = _engine_element(presentation, presented)
            engine = _engine_ring(presentation)

            if flavor == "tensor":
                def source_label(generator):
                    position = next(
                        index
                        for index, candidate in enumerate(engine.monoid().gens())
                        if candidate == generator
                    )
                    return source_labels.unrank(position)

                def tensor_term(item):
                    monomial, coefficient = item
                    degree = sum(int(exponent) for _generator, exponent in monomial)
                    word = (
                        source_label(generator)
                        for generator, exponent in monomial
                        for _ in range(int(exponent))
                    )
                    return (
                        degree,
                        _nested_tensor_label(source, word),
                        algebra.base_ring()._from_engine_element(
                            _engine_ring(algebra.base_ring())(coefficient)
                        ),
                    )

                terms = (
                    tensor_term(item)
                    for item in engine(backend).monomial_coefficients().items()
                )
            else:
                def symmetric_term(item):
                    exponents, coefficient = item
                    multiplicities = {
                        source_labels.unrank(position): int(exponent)
                        for position, exponent in enumerate(exponents)
                        if exponent
                    }
                    degree = sum(multiplicities.values())
                    if degree == 0:
                        label = 0
                    elif degree == 1:
                        label = next(iter(multiplicities))
                    else:
                        label = piece(degree).module_generating_set().from_multiplicities(
                            multiplicities
                        )
                    return (
                        degree,
                        label,
                        algebra.base_ring()._from_engine_element(
                            _engine_ring(algebra.base_ring())(coefficient)
                        ),
                    )

                terms = (symmetric_term(item) for item in engine(backend).dict().items())

        for degree, label, coefficient in terms:
            degree_coefficients = coefficients_by_degree.setdefault(degree, {})
            degree_coefficients[label] = degree_coefficients.get(
                label, algebra.base_ring().zero()
            ) + coefficient
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
        self._base_ring = _owned_ring(base_ring)
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
        return _free_algebra_underlying_module(algebra, source, flavor)

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
