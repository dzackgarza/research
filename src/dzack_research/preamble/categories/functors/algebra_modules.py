r"""The forgetful functor \(U\colon R\text{-}\mathbf{Alg}\to R\text{-}\mathbf{Mod}\).

An associative unital \(R\)-algebra is already an \(R\)-module.  Finite
module-backed algebras use that module directly.  A represented free algebra
has infinitely many homogeneous generators as a module, so its underlying module is the
finite-support direct sum of its actual presented homogeneous pieces.
"""

from sage.misc.cachefunc import cached_function

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
from dzack_research.preamble.categories.modules.pure.modules import (
    FramedModules,
    Modules,
)
from dzack_research.preamble.categories.rings.ring_foundation import (
    _engine_element,
    _engine_ring,
    _owned_ring,
)


from dzack_research.preamble.categories.modules.tensor_products import (
    _flatten_tensor_label,
    _nested_tensor_label,
)


def _free_algebra_underlying_module(algebra, source, flavor):
    realization_maps = {}

    def piece(degree):
        return algebra.graded_piece(degree)

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
    r"""An algebra morphism read as its underlying linear map.

    \(U\) changes neither an element nor its image; it changes which
    operations the map answers to.  So this is constructed as an ordinary
    module morphism, on the framing of its domain when there is one and
    elementwise otherwise, and the kernel, cokernel, matrix and composites of
    the module level are then computed from the algebra morphism rather than
    from state a bare ``Morphism`` never established.

    Linearity is not re-established here.  An \(R\)-algebra morphism is
    \(R\)-linear by definition of the structure map, so the module level is
    told the theorem rather than asked to test it.
    """

    def __init__(self, parent, algebra_morphism) -> None:
        self._algebra_morphism = algebra_morphism
        domain = parent.domain()
        if domain.is_framed():
            super().__init__(
                parent,
                lambda label: self._underlying_image(domain.module_generator(label)),
                verify_linearity=False,
            )
            return
        super().__init__(
            parent,
            self._underlying_image,
            elementwise=True,
            verify_linearity=False,
        )

    def _underlying_image(self, element):
        r"""Return the image of one element under the algebra morphism.

        The underlying module of an algebra is either the algebra itself or a
        graded module that realizes it.  Which one is settled by comparing the
        endpoints of this morphism with the endpoints of the algebra morphism
        it comes from, so nothing is asked what class it belongs to.
        """
        source = self.domain()
        target = self.codomain()
        algebra_domain = self._algebra_morphism.domain()
        algebra_codomain = self._algebra_morphism.codomain()
        argument = element if source is algebra_domain else source.realize(element)
        image = self._algebra_morphism(argument)
        if target is algebra_codomain:
            return image
        return target.from_realization(image)

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
        r"""Return the underlying \(R\)-module of one algebra.

        An algebra already is an \(R\)-module, so the algebra itself is the
        answer wherever nothing better is available: when it carries a module
        framing of its own there is nothing to build, and a polynomial ring
        built from variable names has the addition and the scalar action
        without being the free construction on any represented module.

        The one case that does build something is the free algebra of a
        module.  It has infinitely many homogeneous module generators, so no
        finite framing describes it, and its underlying module is stated as
        the finite-support sum of its own graded pieces -- the module it
        realizes, not a second model of it.
        """
        ring = self.base_ring()
        if algebra in FramedModules(ring):
            return algebra
        match algebra:
            case _ if algebra in TensorAlgebras(ring):
                flavor = "tensor"
            case _ if algebra in SymmetricAlgebras(ring):
                flavor = "symmetric"
            case _:
                return algebra
        try:
            source = algebra.free_source_module()
        except AttributeError:
            # Built from variable names rather than from a module, so there is
            # no module to take graded pieces of.
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
