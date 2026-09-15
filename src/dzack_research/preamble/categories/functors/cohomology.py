r"""Cohomology functors for represented cochain complexes and de Rham DGAs."""

from sage.misc.cachefunc import cached_function

from dzack_research.preamble.categories.algebras.cohomology_algebras import (
    CohomologyAlgebra,
    CohomologyAlgebras,
)
from dzack_research.preamble.categories.algebras.differential_graded_algebras import (
    DifferentialGradedAlgebras,
    StrictlyCommutativeDifferentialGradedAlgebras,
)
from dzack_research.preamble.categories.functors.core import (
    CompositeFunctor,
    Functor,
)
from dzack_research.preamble.categories.functors.de_rham import de_rham_functor
from dzack_research.preamble.categories.modules.cochain_complexes import (
    CochainComplexes,
)
from dzack_research.preamble.categories.modules.pure.modules import FinitelyPresentedModules
from dzack_research.preamble.categories.rings.ring_foundation import _owned_ring


class CohomologyFunctor(Functor):
    r"""The degree-``p`` cohomology functor ``H^p : Coch_R -> Mod_R``."""

    def __init__(self, base_ring, degree) -> None:
        self._base_ring = _owned_ring(base_ring)
        self._degree = int(degree)
        super().__init__(
            CochainComplexes(self._base_ring),
            FinitelyPresentedModules(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def degree(self):
        return self._degree

    def _apply_object(self, complex_):
        return complex_.cohomology(self.degree())

    def _apply_morphism(self, morphism):
        source = self(morphism.domain())
        target = self(morphism.codomain())
        try:
            component = morphism.component(self.degree())
        except AttributeError as error:
            raise TypeError(
                "a represented cochain morphism must expose its degreewise components"
            ) from error
        return source.module_category().Mor(source, target)(
            {
                label: target.class_of_cycle(
                    component(
                        source.cycle_representative(source.module_generator(label))
                    )
                )
                for label in source.module_generating_set()
            }
        )

    def _repr_(self):
        return f"H^{self.degree()} on cochain complexes over {self.base_ring()}"


class DeRhamCohomologyFunctor(CompositeFunctor):
    r"""The literal composite ``H^p ∘ U_Coch ∘ DR_R``."""

    def __init__(self, base_ring, degree) -> None:

        self._base_ring = _owned_ring(base_ring)
        self._degree = int(degree)
        de_rham = de_rham_functor(self._base_ring)
        forget_to_complex = StrictlyCommutativeDifferentialGradedAlgebras(
            self._base_ring
        ).inclusion_into(CochainComplexes(self._base_ring))
        de_rham_complex = CompositeFunctor(de_rham, forget_to_complex)
        super().__init__(
            de_rham_complex,
            cohomology_functor(self._base_ring, self._degree),
        )

    def base_ring(self):
        return self._base_ring

    def degree(self):
        return self._degree

    def _repr_(self):
        return f"H^{{{self.degree()}}}_dR(-/{self.base_ring()})"


class CohomologyAlgebraFunctor(Functor):
    r"""The graded cohomology-algebra functor ``H^*`` on represented DGAs."""

    def __init__(self, base_ring) -> None:

        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            DifferentialGradedAlgebras(self._base_ring),
            CohomologyAlgebras(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _apply_object(self, dga):

        return CohomologyAlgebra(dga)

    def _apply_morphism(self, morphism):

        source = self(morphism.domain())
        target = self(morphism.codomain())
        return self.codomain().Mor(source, target)(morphism)

    def _repr_(self):
        return f"graded cohomology algebra over {self.base_ring()}"


class DeRhamCohomologyAlgebraFunctor(CompositeFunctor):
    r"""The composite ``H^* ∘ DR_R``."""

    def __init__(self, base_ring) -> None:

        self._base_ring = _owned_ring(base_ring)
        super().__init__(
            de_rham_functor(self._base_ring),
            cohomology_algebra_functor(self._base_ring),
        )

    def base_ring(self):
        return self._base_ring

    def _repr_(self):
        return f"H^*_dR(-/{self.base_ring()})"


@cached_function
def cohomology_functor(base_ring, degree) -> CohomologyFunctor:
    return CohomologyFunctor(base_ring, degree)


@cached_function
def de_rham_cohomology_functor(base_ring, degree) -> DeRhamCohomologyFunctor:
    return DeRhamCohomologyFunctor(base_ring, degree)


@cached_function
def cohomology_algebra_functor(base_ring) -> CohomologyAlgebraFunctor:
    return CohomologyAlgebraFunctor(base_ring)


@cached_function
def de_rham_cohomology_algebra_functor(base_ring) -> DeRhamCohomologyAlgebraFunctor:
    return DeRhamCohomologyAlgebraFunctor(base_ring)


__all__ = [
    "CohomologyFunctor",
    "CohomologyAlgebraFunctor",
    "DeRhamCohomologyFunctor",
    "DeRhamCohomologyAlgebraFunctor",
    "cohomology_algebra_functor",
    "cohomology_functor",
    "de_rham_cohomology_algebra_functor",
    "de_rham_cohomology_functor",
]
