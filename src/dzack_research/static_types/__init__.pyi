from shape_extensions import Int, IntVar
from typing import Any, overload

# A point $(n_1, \ldots, n_k)$ of the product monoid $\mathbb N^k$.  Aliases
# `Any` under `LEX-15` until the product's parent has a static name; see the
# runtime module for the full note.
ProductOfNaturalNumbers = Any


class RelativeContext[Eta, R, A]: ...
class FractionFieldContext[Ctx]: ...
class Dual[M]: ...
class Scalar[R]: ...
class Degree[P: IntVar]: ...
class AlgebraRing[Ctx]: ...
class AlgebraElement[Ctx]: ...


class RingMorphism[R, S, Phi]: ...
class AlgebraCategory[R]: ...
class AlgebraParent[R, A](CategoryObject[AlgebraCategory[R], A]): ...
class AlgebraMorphism[R, Source, Target](
    CategoricalMorphism[AlgebraCategory[R], Source, Target]
): ...
class ScalarExtendedAlgebra[Phi, A]: ...
class RestrictedAlgebra[Phi, B]: ...
class BaseChangedStructure[Phi, Eta]: ...
type BaseChangedRelativeContext[R, S, Phi, Eta, A] = RelativeContext[
    BaseChangedStructure[Phi, Eta], S, ScalarExtendedAlgebra[Phi, A]
]


class AlgebraScalarExtensionFunctor[R, S, Phi]:
    @overload
    def __call__[A](
        self, algebra: AlgebraParent[R, A], /
    ) -> AlgebraParent[S, ScalarExtendedAlgebra[Phi, A]]: ...
    @overload
    def __call__[A, B](
        self, morphism: AlgebraMorphism[R, A, B], /
    ) -> AlgebraMorphism[
        S, ScalarExtendedAlgebra[Phi, A], ScalarExtendedAlgebra[Phi, B]
    ]: ...


class AlgebraRestrictionFunctor[R, S, Phi]:
    @overload
    def __call__[B](
        self, algebra: AlgebraParent[S, B], /
    ) -> AlgebraParent[R, RestrictedAlgebra[Phi, B]]: ...
    @overload
    def __call__[A, B](
        self, morphism: AlgebraMorphism[S, A, B], /
    ) -> AlgebraMorphism[
        R, RestrictedAlgebra[Phi, A], RestrictedAlgebra[Phi, B]
    ]: ...


class AlgebraBaseChangeAdjunction[R, S, Phi]:
    def left_adjoint(self) -> AlgebraScalarExtensionFunctor[R, S, Phi]: ...
    def right_adjoint(self) -> AlgebraRestrictionFunctor[R, S, Phi]: ...
    def unit[A](
        self, algebra: AlgebraParent[R, A], /
    ) -> AlgebraMorphism[
        R, A, RestrictedAlgebra[Phi, ScalarExtendedAlgebra[Phi, A]]
    ]: ...
    def counit[B](
        self, algebra: AlgebraParent[S, B], /
    ) -> AlgebraMorphism[
        S, ScalarExtendedAlgebra[Phi, RestrictedAlgebra[Phi, B]], B
    ]: ...


class ModuleCategory[R]: ...
class HomTag[Source, Target]: ...


class CategoryObject[C, A]: ...
class FunctorImage[F, A]: ...
class CategoricalMorphism[C, Source, Target]: ...
class CategoricalIsomorphism[C, Source, Target](
    CategoricalMorphism[C, Source, Target]
):
    def forward(self) -> CategoricalMorphism[C, Source, Target]: ...
    def inverse(self) -> CategoricalMorphism[C, Target, Source]: ...


class CategoryFunctor[C, D, F]:
    def on_object[A](
        self, obj: CategoryObject[C, A], /
    ) -> CategoryObject[D, FunctorImage[F, A]]: ...
    def on_morphism[Source, Target](
        self, morphism: CategoricalMorphism[C, Source, Target], /
    ) -> CategoricalMorphism[
        D, FunctorImage[F, Source], FunctorImage[F, Target]
    ]: ...


class HomObject[C, Source, Target]:
    def domain_object(self) -> CategoryObject[C, Source]: ...
    def codomain_object(self) -> CategoryObject[C, Target]: ...
class IsoObject[C, Source, Target](HomObject[C, Source, Target]): ...
type EndObject[C, A] = HomObject[C, A, A]
type AutObject[C, A] = IsoObject[C, A, A]
type EndomorphismArrow[C, A] = CategoricalMorphism[C, A, A]
type Automorphism[C, A] = CategoricalIsomorphism[C, A, A]


class ModuleParent[R, M](CategoryObject[ModuleCategory[R], M]): ...
class FiniteFreeModule[R, M, N: IntVar](ModuleParent[R, M]): ...
class ModuleElement[R, M]: ...
class ModuleMorphism[R, Source, Target](
    CategoricalMorphism[ModuleCategory[R], Source, Target],
    ModuleElement[R, HomTag[Source, Target]],
):
    def __call__(
        self, element: ModuleElement[R, Source], /
    ) -> ModuleElement[R, Target]: ...
class FreeModuleMorphism[
    R, Source, N: IntVar, Target, M: IntVar
](ModuleMorphism[R, Source, Target]): ...
class FreeModuleIsomorphism[
    R, Source, N: IntVar, Target, M: IntVar
](CategoricalIsomorphism[ModuleCategory[R], Source, Target]):
    def forward(self) -> FreeModuleMorphism[R, Source, N, Target, M]: ...
    def inverse(self) -> FreeModuleMorphism[R, Target, M, Source, N]: ...
class ModuleHom[R, Source, Target](
    HomObject[ModuleCategory[R], Source, Target],
    ModuleParent[R, HomTag[Source, Target]],
): ...
type ModuleEnd[R, M] = ModuleHom[R, M, M]
type ModuleEndomorphism[R, M] = ModuleMorphism[R, M, M]


class ModuleStructure[R, M]:
    def __call__(self, scalar: Scalar[R], /) -> ModuleEndomorphism[R, M]: ...


class ScalarExtendedModule[Phi, M]: ...
class RestrictedModule[Phi, N]: ...


class ModuleScalarExtensionFunctor[R, S, Phi]:
    @overload
    def __call__[M](
        self, module: ModuleParent[R, M], /
    ) -> ModuleParent[S, ScalarExtendedModule[Phi, M]]: ...
    @overload
    def __call__[M, N](
        self, morphism: ModuleMorphism[R, M, N], /
    ) -> ModuleMorphism[
        S, ScalarExtendedModule[Phi, M], ScalarExtendedModule[Phi, N]
    ]: ...


class ModuleRestrictionFunctor[R, S, Phi]:
    @overload
    def __call__[N](
        self, module: ModuleParent[S, N], /
    ) -> ModuleParent[R, RestrictedModule[Phi, N]]: ...
    @overload
    def __call__[M, N](
        self, morphism: ModuleMorphism[S, M, N], /
    ) -> ModuleMorphism[
        R, RestrictedModule[Phi, M], RestrictedModule[Phi, N]
    ]: ...


class ModuleBaseChangeAdjunction[R, S, Phi]:
    def left_adjoint(self) -> ModuleScalarExtensionFunctor[R, S, Phi]: ...
    def right_adjoint(self) -> ModuleRestrictionFunctor[R, S, Phi]: ...
    def unit[M](
        self, module: ModuleParent[R, M], /
    ) -> ModuleMorphism[
        R, M, RestrictedModule[Phi, ScalarExtendedModule[Phi, M]]
    ]: ...
    def counit[N](
        self, module: ModuleParent[S, N], /
    ) -> ModuleMorphism[
        S, ScalarExtendedModule[Phi, RestrictedModule[Phi, N]], N
    ]: ...


class KahlerTag[Ctx]: ...
class DerivationTag[Ctx, E]: ...
class AlgebraModuleTag[Ctx]: ...
type KahlerDifferentials[Ctx] = ModuleParent[AlgebraRing[Ctx], KahlerTag[Ctx]]
type KahlerOneForm[Ctx] = ModuleElement[AlgebraRing[Ctx], KahlerTag[Ctx]]
type KahlerClassifier[Ctx, E] = ModuleMorphism[
    AlgebraRing[Ctx], KahlerTag[Ctx], E
]
type KahlerClassifierIsomorphism[Ctx, E] = CategoricalIsomorphism[
    ModuleCategory[AlgebraRing[Ctx]],
    HomTag[KahlerTag[Ctx], E],
    DerivationTag[Ctx, E],
]


class Derivation[Ctx, E](
    ModuleElement[AlgebraRing[Ctx], DerivationTag[Ctx, E]]
):
    def __call__(
        self, element: AlgebraElement[Ctx], /
    ) -> ModuleElement[AlgebraRing[Ctx], E]: ...


class DerivationSpace[Ctx, E](
    ModuleParent[AlgebraRing[Ctx], DerivationTag[Ctx, E]]
): ...


class UniversalDerivation[Ctx](Derivation[Ctx, KahlerTag[Ctx]]): ...
type VectorField[Ctx] = Derivation[Ctx, AlgebraModuleTag[Ctx]]


class ExteriorPowerTag[M, P: IntVar]: ...
type ExteriorPower[R, M, P: IntVar] = ModuleParent[R, ExteriorPowerTag[M, P]]
type ExteriorElement[R, M, P: IntVar] = ModuleElement[R, ExteriorPowerTag[M, P]]
type KahlerPForm[Ctx, P: IntVar] = ExteriorElement[
    AlgebraRing[Ctx], KahlerTag[Ctx], P
]
class PoincareDualityIsomorphism[Ctx, N: IntVar, P: IntVar](
    CategoricalIsomorphism[
        ModuleCategory[MetricScalarRing[Ctx]],
        ExteriorPowerTag[Ctx, P],
        ExteriorPowerTag[Dual[Ctx], N - P],
    ]
):
    def forward(self) -> ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Ctx, P],
        ExteriorPowerTag[Dual[Ctx], N - P],
    ]: ...
    def inverse(self) -> ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Dual[Ctx], N - P],
        ExteriorPowerTag[Ctx, P],
    ]: ...


class HodgeStarIsomorphism[Ctx, N: IntVar, P: IntVar](
    CategoricalIsomorphism[
        ModuleCategory[MetricScalarRing[Ctx]],
        ExteriorPowerTag[Dual[Ctx], P],
        ExteriorPowerTag[Dual[Ctx], N - P],
    ]
):
    def forward(self) -> ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Dual[Ctx], P],
        ExteriorPowerTag[Dual[Ctx], N - P],
    ]: ...
    def inverse(self) -> ModuleMorphism[
        MetricScalarRing[Ctx],
        ExteriorPowerTag[Dual[Ctx], N - P],
        ExteriorPowerTag[Dual[Ctx], P],
    ]: ...


class CochainPieceTag[K, I: IntVar]: ...
class CohomologyTag[K, I: IntVar]: ...
class CochainComplex[R, K]: ...
class CochainMorphism[R, SourceK, TargetK]:
    def component[I: IntVar](
        self, degree: Degree[I], /
    ) -> ModuleMorphism[
        R, CochainPieceTag[SourceK, I], CochainPieceTag[TargetK, I]
    ]: ...


type CochainPiece[R, K, I: IntVar] = ModuleParent[R, CochainPieceTag[K, I]]
type Cochain[R, K, I: IntVar] = ModuleElement[R, CochainPieceTag[K, I]]
type CohomologyModule[R, K, I: IntVar] = ModuleParent[R, CohomologyTag[K, I]]
type CohomologyClass[R, K, I: IntVar] = ModuleElement[R, CohomologyTag[K, I]]
type CochainCohomologyMorphism[
    R, SourceK, TargetK, I: IntVar
] = ModuleMorphism[R, CohomologyTag[SourceK, I], CohomologyTag[TargetK, I]]


class InducedHomFunctor[F, C, D, Source, Target]:
    def domain(self) -> HomObject[C, Source, Target]: ...
    def codomain(self) -> HomObject[
        D, FunctorImage[F, Source], FunctorImage[F, Target]
    ]: ...
    def __call__(
        self, morphism: CategoricalMorphism[C, Source, Target], /
    ) -> CategoricalMorphism[
        D, FunctorImage[F, Source], FunctorImage[F, Target]
    ]: ...


class InducedEndFunctor[F, C, D, A]:
    def domain(self) -> EndObject[C, A]: ...
    def codomain(self) -> EndObject[D, FunctorImage[F, A]]: ...
    def __call__(
        self, morphism: EndomorphismArrow[C, A], /
    ) -> EndomorphismArrow[D, FunctorImage[F, A]]: ...


class InducedAutFunctor[F, C, D, A]:
    def domain(self) -> AutObject[C, A]: ...
    def codomain(self) -> AutObject[D, FunctorImage[F, A]]: ...
    def __call__(
        self, automorphism: Automorphism[C, A], /
    ) -> Automorphism[D, FunctorImage[F, A]]: ...


class Up[M, N: IntVar]: ...
class Down[M, N: IntVar]: ...


class Tensor[R, *Slots]: ...


class Vector[R, M, N: IntVar](Tensor[R, Up[M, N]]): ...
class Covector[R, M, N: IntVar](Tensor[R, Down[M, N]]): ...


class LinearMap[R, V, N: IntVar, W, M: IntVar](
    Tensor[R, Up[W, M], Down[V, N]]
): ...


class Endomorphism[R, M, N: IntVar](LinearMap[R, M, N, M, N]): ...


class Isomorphism[R, V, N: IntVar, W, M: IntVar](
    LinearMap[R, V, N, W, M]
): ...


class BilinearForm[R, M, N: IntVar](
    Tensor[R, Down[M, N], Down[M, N]]
): ...


class DualBilinearForm[R, M, N: IntVar](
    Tensor[R, Up[M, N], Up[M, N]]
): ...


class GradedCarrier[G]: ...
class HomogeneousElement[G, P: IntVar]: ...
class GradedMorphism[SourceG, TargetG]:
    def __call__[P: IntVar](
        self, element: HomogeneousElement[SourceG, P], /
    ) -> HomogeneousElement[TargetG, P]: ...


class DifferentialGradedCarrier[G](GradedCarrier[G]): ...
class DifferentialGradedMorphism[SourceG, TargetG](
    GradedMorphism[SourceG, TargetG]
): ...


class DeRhamGradedTag[Ctx]: ...
type DifferentialForm[Ctx, P: IntVar] = HomogeneousElement[
    DeRhamGradedTag[Ctx], P
]
type DeRhamAlgebra[Ctx] = DifferentialGradedCarrier[DeRhamGradedTag[Ctx]]
class RelativeBaseRing[Ctx]: ...
class DeRhamComplexTag[Ctx]: ...


class DifferentialGradedModule[AlgebraG, M]: ...
class DGModuleElement[AlgebraG, M, P: IntVar]: ...
class DGModuleMorphism[AlgebraG, SourceM, TargetM]:
    def __call__[P: IntVar](
        self, element: DGModuleElement[AlgebraG, SourceM, P], /
    ) -> DGModuleElement[AlgebraG, TargetM, P]: ...


class ConnectionModuleTag[Ctx, E]: ...
type CoefficientDeRhamModule[Ctx, E] = DifferentialGradedModule[
    DeRhamGradedTag[Ctx], ConnectionModuleTag[Ctx, E]
]
type CoefficientForm[Ctx, E, P: IntVar] = DGModuleElement[
    DeRhamGradedTag[Ctx], ConnectionModuleTag[Ctx, E], P
]
class FormOperator[Ctx, Shift: IntVar]:
    def __call__[P: IntVar](
        self, form: DifferentialForm[Ctx, P], /
    ) -> DifferentialForm[Ctx, P + Shift]: ...


class GradedDerivationOperator[Ctx, Shift: IntVar](FormOperator[Ctx, Shift]): ...
class DifferentialOperator[Ctx](GradedDerivationOperator[Ctx, 1]): ...
class InteriorOperator[Ctx](GradedDerivationOperator[Ctx, -1]): ...
class LieDerivativeOperator[Ctx](GradedDerivationOperator[Ctx, 0]): ...


class Metric[Ctx, N: IntVar]: ...
class MetricScalarRing[Ctx]: ...
class FractionFieldMetricRing[Ctx]: ...
class FractionFieldMetricModule[Ctx]: ...
type MetricCovariantForm[Ctx, P: IntVar] = ExteriorElement[
    MetricScalarRing[Ctx], Dual[Ctx], P
]
type Multivector[Ctx, P: IntVar] = ExteriorElement[
    MetricScalarRing[Ctx], Ctx, P
]
type FractionFieldCovariantForm[Ctx, P: IntVar] = ExteriorElement[
    FractionFieldMetricRing[Ctx], Dual[FractionFieldMetricModule[Ctx]], P
]
class NondegenerateMetric[Ctx, N: IntVar](Metric[Ctx, N]): ...
class PerfectMetric[Ctx, N: IntVar](NondegenerateMetric[Ctx, N]): ...
class Volume[Ctx, N: IntVar]: ...


class Connection[Ctx, E]: ...
class FlatConnection[Ctx, E](Connection[Ctx, E]): ...


class CoefficientOperator[Ctx, E, Shift: IntVar]:
    def __call__[P: IntVar](
        self, form: CoefficientForm[Ctx, E, P], /
    ) -> CoefficientForm[Ctx, E, P + Shift]: ...


class CovariantDifferential[Ctx, E](CoefficientOperator[Ctx, E, 1]): ...


type DeRhamCohomology[Ctx, I: IntVar] = CohomologyModule[
    RelativeBaseRing[Ctx], DeRhamComplexTag[Ctx], I
]
type DeRhamClass[Ctx, I: IntVar] = CohomologyClass[
    RelativeBaseRing[Ctx], DeRhamComplexTag[Ctx], I
]
class DeRhamCohomologyAlgebra[Ctx]: ...
class RelativeAlgebraMorphism[R, SourceEta, SourceA, TargetEta, TargetA]: ...
type DGAMorphism[SourceCtx, TargetCtx] = DifferentialGradedMorphism[
    DeRhamGradedTag[SourceCtx], DeRhamGradedTag[TargetCtx]
]
class CohomologyMorphism[SourceCtx, TargetCtx, I: IntVar]:
    def __call__(
        self, cohomology_class: DeRhamClass[SourceCtx, I], /
    ) -> DeRhamClass[TargetCtx, I]: ...
class HodgeCohomology[Ctx, P: IntVar, Q: IntVar]: ...
class HodgeToDeRham[Ctx]: ...
class SpectralTerm[S, Page: IntVar, P: IntVar, Q: IntVar]: ...


def vector_view[R, M, N: IntVar](value: object, /) -> Vector[R, M, N]: ...
def covector_view[R, M, N: IntVar](value: object, /) -> Covector[R, M, N]: ...
def linear_map_view[R, V, N: IntVar, W, M: IntVar](
    value: object, /
) -> LinearMap[R, V, N, W, M]: ...
def endomorphism_view[R, M, N: IntVar](
    value: object, /
) -> Endomorphism[R, M, N]: ...
def isomorphism_view[R, V, N: IntVar, W, M: IntVar](
    value: object, /
) -> Isomorphism[R, V, N, W, M]: ...
def bilinear_form_view[R, M, N: IntVar](
    value: object, /
) -> BilinearForm[R, M, N]: ...
def dual_bilinear_form_view[R, M, N: IntVar](
    value: object, /
) -> DualBilinearForm[R, M, N]: ...
def form_view[Ctx, P: IntVar](
    value: object, /
) -> DifferentialForm[Ctx, P]: ...
def de_rham_algebra_view[Ctx](value: object, /) -> DeRhamAlgebra[Ctx]: ...
def graded_carrier_view[G](value: object, /) -> GradedCarrier[G]: ...
def homogeneous_element_view[G, P: IntVar](
    value: object, /
) -> HomogeneousElement[G, P]: ...
def graded_morphism_view[SourceG, TargetG](
    value: object, /
) -> GradedMorphism[SourceG, TargetG]: ...
def differential_graded_carrier_view[G](
    value: object, /
) -> DifferentialGradedCarrier[G]: ...
def differential_graded_morphism_view[SourceG, TargetG](
    value: object, /
) -> DifferentialGradedMorphism[SourceG, TargetG]: ...
def multivector_view[Ctx, P: IntVar](
    value: object, /
) -> Multivector[Ctx, P]: ...
def metric_covariant_form_view[Ctx, P: IntVar](
    value: object, /
) -> MetricCovariantForm[Ctx, P]: ...
def fraction_field_covariant_form_view[Ctx, P: IntVar](
    value: object, /
) -> FractionFieldCovariantForm[Ctx, P]: ...
def coefficient_form_view[Ctx, E, P: IntVar](
    value: object, /
) -> CoefficientForm[Ctx, E, P]: ...
def dg_module_view[AlgebraG, M](
    value: object, /
) -> DifferentialGradedModule[AlgebraG, M]: ...
def dg_module_element_view[AlgebraG, M, P: IntVar](
    value: object, /
) -> DGModuleElement[AlgebraG, M, P]: ...
def dg_module_morphism_view[AlgebraG, SourceM, TargetM](
    value: object, /
) -> DGModuleMorphism[AlgebraG, SourceM, TargetM]: ...
def vector_field_view[Ctx](value: object, /) -> VectorField[Ctx]: ...
def operator_view[Ctx, Shift: IntVar](
    value: object, /
) -> FormOperator[Ctx, Shift]: ...
def graded_derivation_operator_view[Ctx, Shift: IntVar](
    value: object, /
) -> GradedDerivationOperator[Ctx, Shift]: ...
def metric_view[Ctx, N: IntVar](value: object, /) -> Metric[Ctx, N]: ...
def nondegenerate_metric_view[Ctx, N: IntVar](
    value: object, /
) -> NondegenerateMetric[Ctx, N]: ...
def perfect_metric_view[Ctx, N: IntVar](
    value: object, /
) -> PerfectMetric[Ctx, N]: ...
def volume_view[Ctx, N: IntVar](value: object, /) -> Volume[Ctx, N]: ...
def connection_view[Ctx, E](value: object, /) -> Connection[Ctx, E]: ...
def flat_connection_view[Ctx, E](value: object, /) -> FlatConnection[Ctx, E]: ...
def cohomology_view[Ctx, I: IntVar](
    value: object, /
) -> DeRhamCohomology[Ctx, I]: ...
def de_rham_class_view[Ctx, I: IntVar](value: object, /) -> DeRhamClass[Ctx, I]: ...
def cohomology_algebra_view[Ctx](value: object, /) -> DeRhamCohomologyAlgebra[Ctx]: ...
def category_object_view[C, A](value: object, /) -> CategoryObject[C, A]: ...
def morphism_view[C, Source, Target](
    value: object, /
) -> CategoricalMorphism[C, Source, Target]: ...
def categorical_isomorphism_view[C, Source, Target](
    value: object, /
) -> CategoricalIsomorphism[C, Source, Target]: ...
def hom_object_view[C, Source, Target](
    value: object, /
) -> HomObject[C, Source, Target]: ...
def iso_object_view[C, Source, Target](
    value: object, /
) -> IsoObject[C, Source, Target]: ...
def module_view[R, M](value: object, /) -> ModuleParent[R, M]: ...
def finite_free_module_view[R, M, N: IntVar](
    value: object, /
) -> FiniteFreeModule[R, M, N]: ...
def module_element_view[R, M](value: object, /) -> ModuleElement[R, M]: ...
def module_morphism_view[R, Source, Target](
    value: object, /
) -> ModuleMorphism[R, Source, Target]: ...
def free_module_morphism_view[R, Source, N: IntVar, Target, M: IntVar](
    value: object, /
) -> FreeModuleMorphism[R, Source, N, Target, M]: ...
def free_module_isomorphism_view[R, Source, N: IntVar, Target, M: IntVar](
    value: object, /
) -> FreeModuleIsomorphism[R, Source, N, Target, M]: ...
def module_hom_view[R, Source, Target](
    value: object, /
) -> ModuleHom[R, Source, Target]: ...
def module_structure_view[R, M](value: object, /) -> ModuleStructure[R, M]: ...
def module_base_change_adjunction_view[R, S, Phi](
    value: object, /
) -> ModuleBaseChangeAdjunction[R, S, Phi]: ...
def scalar_view[R](value: object, /) -> Scalar[R]: ...
def degree_view[P: IntVar](value: object, /) -> Degree[P]: ...
def algebra_element_view[Ctx](value: object, /) -> AlgebraElement[Ctx]: ...
def ring_morphism_view[R, S, Phi](value: object, /) -> RingMorphism[R, S, Phi]: ...
def algebra_view[R, A](value: object, /) -> AlgebraParent[R, A]: ...
def algebra_morphism_view[R, Source, Target](
    value: object, /
) -> AlgebraMorphism[R, Source, Target]: ...
def algebra_base_change_adjunction_view[R, S, Phi](
    value: object, /
) -> AlgebraBaseChangeAdjunction[R, S, Phi]: ...
def kahler_differentials_view[Ctx](value: object, /) -> KahlerDifferentials[Ctx]: ...
def kahler_one_form_view[Ctx](value: object, /) -> KahlerOneForm[Ctx]: ...
def exterior_power_view[R, M, P: IntVar](
    value: object, /
) -> ExteriorPower[R, M, P]: ...
def exterior_element_view[R, M, P: IntVar](
    value: object, /
) -> ExteriorElement[R, M, P]: ...
def derivation_view[Ctx, E](value: object, /) -> Derivation[Ctx, E]: ...
def derivation_space_view[Ctx, E](value: object, /) -> DerivationSpace[Ctx, E]: ...
def universal_derivation_view[Ctx](value: object, /) -> UniversalDerivation[Ctx]: ...
def cochain_complex_view[R, K](value: object, /) -> CochainComplex[R, K]: ...
def cochain_morphism_view[R, SourceK, TargetK](
    value: object, /
) -> CochainMorphism[R, SourceK, TargetK]: ...
def cochain_piece_view[R, K, I: IntVar](
    value: object, /
) -> CochainPiece[R, K, I]: ...
def cochain_view[R, K, I: IntVar](value: object, /) -> Cochain[R, K, I]: ...
def cohomology_module_view[R, K, I: IntVar](
    value: object, /
) -> CohomologyModule[R, K, I]: ...
def cohomology_class_view[R, K, I: IntVar](
    value: object, /
) -> CohomologyClass[R, K, I]: ...
def relative_algebra_morphism_view[R, SourceEta, SourceA, TargetEta, TargetA](
    value: object, /
) -> RelativeAlgebraMorphism[R, SourceEta, SourceA, TargetEta, TargetA]: ...
def dga_morphism_view[SourceCtx, TargetCtx](
    value: object, /
) -> DGAMorphism[SourceCtx, TargetCtx]: ...
def cohomology_morphism_view[SourceCtx, TargetCtx, I: IntVar](
    value: object, /
) -> CohomologyMorphism[SourceCtx, TargetCtx, I]: ...
def relative_context_view[Eta, R, A](
    value: object, /
) -> RelativeContext[Eta, R, A]: ...
def functor_view[C, D, F](value: object, /) -> CategoryFunctor[C, D, F]: ...


def fraction_field_context[Ctx](context: Ctx, /) -> FractionFieldContext[Ctx]: ...


def base_changed_relative_context[R, S, Phi, Eta, A](
    ring_map: RingMorphism[R, S, Phi],
    context: RelativeContext[Eta, R, A],
    /,
) -> BaseChangedRelativeContext[R, S, Phi, Eta, A]: ...


def algebra_base_change[R, S, Phi](
    ring_map: RingMorphism[R, S, Phi], /
) -> AlgebraBaseChangeAdjunction[R, S, Phi]: ...


def extend_algebra[R, S, Phi, A](
    ring_map: RingMorphism[R, S, Phi],
    algebra: AlgebraParent[R, A],
    /,
) -> AlgebraParent[S, ScalarExtendedAlgebra[Phi, A]]: ...


def restrict_algebra[R, S, Phi, B](
    ring_map: RingMorphism[R, S, Phi],
    algebra: AlgebraParent[S, B],
    /,
) -> AlgebraParent[R, RestrictedAlgebra[Phi, B]]: ...


def extend_algebra_morphism[R, S, Phi, A, B](
    ring_map: RingMorphism[R, S, Phi],
    morphism: AlgebraMorphism[R, A, B],
    /,
) -> AlgebraMorphism[
    S, ScalarExtendedAlgebra[Phi, A], ScalarExtendedAlgebra[Phi, B]
]: ...


def restrict_algebra_morphism[R, S, Phi, A, B](
    ring_map: RingMorphism[R, S, Phi],
    morphism: AlgebraMorphism[S, A, B],
    /,
) -> AlgebraMorphism[
    R, RestrictedAlgebra[Phi, A], RestrictedAlgebra[Phi, B]
]: ...


def algebra_base_change_unit[R, S, Phi, A](
    adjunction: AlgebraBaseChangeAdjunction[R, S, Phi],
    algebra: AlgebraParent[R, A],
    /,
) -> AlgebraMorphism[
    R, A, RestrictedAlgebra[Phi, ScalarExtendedAlgebra[Phi, A]]
]: ...


def algebra_base_change_counit[R, S, Phi, B](
    adjunction: AlgebraBaseChangeAdjunction[R, S, Phi],
    algebra: AlgebraParent[S, B],
    /,
) -> AlgebraMorphism[
    S, ScalarExtendedAlgebra[Phi, RestrictedAlgebra[Phi, B]], B
]: ...


def functor_object_image[C, D, F, A](
    functor: CategoryFunctor[C, D, F],
    obj: CategoryObject[C, A],
    /,
) -> CategoryObject[D, FunctorImage[F, A]]: ...


def functor_morphism_image[C, D, F, Source, Target](
    functor: CategoryFunctor[C, D, F],
    morphism: CategoricalMorphism[C, Source, Target],
    /,
) -> CategoricalMorphism[D, FunctorImage[F, Source], FunctorImage[F, Target]]: ...


def induced_hom[C, D, F, Source, Target](
    functor: CategoryFunctor[C, D, F],
    source: CategoryObject[C, Source],
    target: CategoryObject[C, Target],
    /,
) -> InducedHomFunctor[F, C, D, Source, Target]: ...


def induced_end[C, D, F, A](
    functor: CategoryFunctor[C, D, F],
    obj: CategoryObject[C, A],
    /,
) -> InducedEndFunctor[F, C, D, A]: ...


def induced_aut[C, D, F, A](
    functor: CategoryFunctor[C, D, F],
    obj: CategoryObject[C, A],
    /,
) -> InducedAutFunctor[F, C, D, A]: ...


def module_element_of[R, M](
    module: ModuleParent[R, M], value: object, /
) -> ModuleElement[R, M]: ...


def module_morphism_of[R, Source, Target](
    source: ModuleParent[R, Source],
    target: ModuleParent[R, Target],
    value: object,
    /,
) -> ModuleMorphism[R, Source, Target]: ...


def free_module_morphism_of[R, Source, N: IntVar, Target, M: IntVar](
    source: ModuleParent[R, Source],
    source_rank: Int[N],
    target: ModuleParent[R, Target],
    target_rank: Int[M],
    value: object,
    /,
) -> FreeModuleMorphism[R, Source, N, Target, M]: ...


def vector_of[R, M, N: IntVar](
    module: ModuleParent[R, M], rank: Int[N], value: object, /
) -> Vector[R, M, N]: ...


def covector_of[R, M, N: IntVar](
    module: ModuleParent[R, M], rank: Int[N], value: object, /
) -> Covector[R, M, N]: ...


def linear_map_of[R, Source, N: IntVar, Target, M: IntVar](
    source: ModuleParent[R, Source],
    source_rank: Int[N],
    target: ModuleParent[R, Target],
    target_rank: Int[M],
    value: object,
    /,
) -> LinearMap[R, Source, N, Target, M]: ...


def form_of[Ctx, P: IntVar](
    context: Ctx, degree: Degree[P], value: object, /
) -> DifferentialForm[Ctx, P]: ...


def multivector_of[Ctx, P: IntVar](
    context: Ctx, degree: Degree[P], value: object, /
) -> Multivector[Ctx, P]: ...


def coefficient_form_of[Ctx, R, E, P: IntVar](
    context: Ctx,
    coefficient_module: ModuleParent[R, E],
    degree: Degree[P],
    value: object,
    /,
) -> CoefficientForm[Ctx, E, P]: ...


def differential_operator_of[Ctx](
    context: Ctx, value: object, /
) -> DifferentialOperator[Ctx]: ...
def interior_operator_of[Ctx](
    context: Ctx, value: object, /
) -> InteriorOperator[Ctx]: ...
def lie_derivative_operator_of[Ctx](
    context: Ctx, value: object, /
) -> LieDerivativeOperator[Ctx]: ...


def compose_morphisms[C, Source, Middle, Target](
    outer: CategoricalMorphism[C, Middle, Target],
    inner: CategoricalMorphism[C, Source, Middle],
    /,
) -> CategoricalMorphism[C, Source, Target]: ...


def identity_endomorphism[C, A](
    end_object: EndObject[C, A], /
) -> EndomorphismArrow[C, A]: ...


def compose_endomorphisms[C, A](
    outer: EndomorphismArrow[C, A],
    inner: EndomorphismArrow[C, A],
    /,
) -> EndomorphismArrow[C, A]: ...


def identity_automorphism[C, A](
    aut_object: AutObject[C, A], /
) -> Automorphism[C, A]: ...


def compose_automorphisms[C, A](
    outer: Automorphism[C, A],
    inner: Automorphism[C, A],
    /,
) -> Automorphism[C, A]: ...


def inverse_automorphism[C, A](
    automorphism: Automorphism[C, A], /
) -> Automorphism[C, A]: ...


def apply_module_morphism[R, Source, Target](
    morphism: ModuleMorphism[R, Source, Target],
    element: ModuleElement[R, Source],
    /,
) -> ModuleElement[R, Target]: ...


def compose_module_morphisms[R, Source, Middle, Target](
    outer: ModuleMorphism[R, Middle, Target],
    inner: ModuleMorphism[R, Source, Middle],
    /,
) -> ModuleMorphism[R, Source, Target]: ...


def module_morphism_tensor[R, Source, N: IntVar, Target, M: IntVar](
    morphism: FreeModuleMorphism[R, Source, N, Target, M], /
) -> LinearMap[R, Source, N, Target, M]: ...


def dual_module[R, M, N: IntVar](
    module: FiniteFreeModule[R, M, N], /
) -> FiniteFreeModule[R, Dual[M], N]: ...


def dualize_module_morphism[R, Source, N: IntVar, Target, M: IntVar](
    morphism: FreeModuleMorphism[R, Source, N, Target, M], /
) -> FreeModuleMorphism[R, Dual[Target], M, Dual[Source], N]: ...


def double_dual_morphism[R, M, N: IntVar](
    module: FiniteFreeModule[R, M, N], /
) -> FreeModuleMorphism[R, M, N, Dual[Dual[M]], N]: ...


def module_action[R, M](
    structure: ModuleStructure[R, M],
    scalar: Scalar[R],
    element: ModuleElement[R, M],
    /,
) -> ModuleElement[R, M]: ...


def module_base_change[R, S, Phi](
    ring_map: RingMorphism[R, S, Phi], /
) -> ModuleBaseChangeAdjunction[R, S, Phi]: ...


def extend_module[R, S, Phi, M](
    ring_map: RingMorphism[R, S, Phi],
    module: ModuleParent[R, M],
    /,
) -> ModuleParent[S, ScalarExtendedModule[Phi, M]]: ...


def restrict_module[R, S, Phi, N](
    ring_map: RingMorphism[R, S, Phi],
    module: ModuleParent[S, N],
    /,
) -> ModuleParent[R, RestrictedModule[Phi, N]]: ...


def extend_module_morphism[R, S, Phi, M, N](
    ring_map: RingMorphism[R, S, Phi],
    morphism: ModuleMorphism[R, M, N],
    /,
) -> ModuleMorphism[
    S, ScalarExtendedModule[Phi, M], ScalarExtendedModule[Phi, N]
]: ...


def restrict_module_morphism[R, S, Phi, M, N](
    ring_map: RingMorphism[R, S, Phi],
    morphism: ModuleMorphism[S, M, N],
    /,
) -> ModuleMorphism[
    R, RestrictedModule[Phi, M], RestrictedModule[Phi, N]
]: ...


def module_base_change_unit[R, S, Phi, M](
    adjunction: ModuleBaseChangeAdjunction[R, S, Phi],
    module: ModuleParent[R, M],
    /,
) -> ModuleMorphism[
    R, M, RestrictedModule[Phi, ScalarExtendedModule[Phi, M]]
]: ...


def module_base_change_counit[R, S, Phi, N](
    adjunction: ModuleBaseChangeAdjunction[R, S, Phi],
    module: ModuleParent[S, N],
    /,
) -> ModuleMorphism[
    S, ScalarExtendedModule[Phi, RestrictedModule[Phi, N]], N
]: ...


def universal_derivation[Ctx](
    omega: KahlerDifferentials[Ctx], /
) -> UniversalDerivation[Ctx]: ...


def derive[Ctx, E](
    derivation: Derivation[Ctx, E],
    element: AlgebraElement[Ctx],
    /,
) -> ModuleElement[AlgebraRing[Ctx], E]: ...


def embed_function[Ctx](
    de_rham: DeRhamAlgebra[Ctx],
    element: AlgebraElement[Ctx],
    /,
) -> DifferentialForm[Ctx, 0]: ...


def embed_kahler_one_form[Ctx](
    de_rham: DeRhamAlgebra[Ctx],
    one_form: KahlerOneForm[Ctx],
    /,
) -> DifferentialForm[Ctx, 1]: ...


def classifier_from_derivation[Ctx, E](
    omega: KahlerDifferentials[Ctx],
    derivation: Derivation[Ctx, E],
    /,
) -> KahlerClassifier[Ctx, E]: ...


def derivation_from_classifier[Ctx, E](
    omega: KahlerDifferentials[Ctx],
    target_module: ModuleParent[AlgebraRing[Ctx], E],
    classifier: KahlerClassifier[Ctx, E],
    /,
) -> Derivation[Ctx, E]: ...


def kahler_classifier_isomorphism[Ctx, E](
    omega: KahlerDifferentials[Ctx],
    target_module: ModuleParent[AlgebraRing[Ctx], E],
    /,
) -> KahlerClassifierIsomorphism[Ctx, E]: ...


def exterior_power[R, M, P: IntVar](
    module: ModuleParent[R, M],
    degree: Degree[P],
    /,
) -> ExteriorPower[R, M, P]: ...


def exterior_one[R, M](
    module: ModuleParent[R, M],
    element: ModuleElement[R, M],
    /,
) -> ExteriorElement[R, M, 1]: ...


def wedge_exterior[R, M, P: IntVar, Q: IntVar](
    module: ModuleParent[R, M],
    left_degree: Degree[P],
    left: ExteriorElement[R, M, P],
    right_degree: Degree[Q],
    right: ExteriorElement[R, M, Q],
    /,
) -> ExteriorElement[R, M, P + Q]: ...


def exterior_power_morphism[R, Source, Target, P: IntVar](
    morphism: ModuleMorphism[R, Source, Target],
    degree: Degree[P],
    /,
) -> ModuleMorphism[
    R, ExteriorPowerTag[Source, P], ExteriorPowerTag[Target, P]
]: ...


def embed_exterior_form[Ctx, P: IntVar](
    de_rham: DeRhamAlgebra[Ctx],
    degree: Degree[P],
    exterior_element: KahlerPForm[Ctx, P],
    /,
) -> DifferentialForm[Ctx, P]: ...


def exterior_component[Ctx, P: IntVar](
    de_rham: DeRhamAlgebra[Ctx],
    degree: Degree[P],
    form: DifferentialForm[Ctx, P],
    /,
) -> KahlerPForm[Ctx, P]: ...


def cochain_piece[R, K, I: IntVar](
    complex_: CochainComplex[R, K],
    degree: Degree[I],
    /,
) -> CochainPiece[R, K, I]: ...


def cochain_of[R, K, I: IntVar](
    complex_: CochainComplex[R, K],
    degree: Degree[I],
    value: object,
    /,
) -> Cochain[R, K, I]: ...


def cochain_d[R, K, I: IntVar](
    complex_: CochainComplex[R, K],
    degree: Degree[I],
    cochain: Cochain[R, K, I],
    /,
) -> Cochain[R, K, I + 1]: ...


def cochain_map[R, SourceK, TargetK, I: IntVar](
    morphism: CochainMorphism[R, SourceK, TargetK],
    degree: Degree[I],
    cochain: Cochain[R, SourceK, I],
    /,
) -> Cochain[R, TargetK, I]: ...


def cohomology_of[R, K, I: IntVar](
    complex_: CochainComplex[R, K],
    degree: Degree[I],
    /,
) -> CohomologyModule[R, K, I]: ...


def class_of_cycle[R, K, I: IntVar](
    cohomology_module: CohomologyModule[R, K, I],
    cycle: Cochain[R, K, I],
    /,
) -> CohomologyClass[R, K, I]: ...


def cycle_representative[R, K, I: IntVar](
    cohomology_module: CohomologyModule[R, K, I],
    cohomology_class: CohomologyClass[R, K, I],
    /,
) -> Cochain[R, K, I]: ...


def cohomology_map[R, SourceK, TargetK, I: IntVar](
    morphism: CochainMorphism[R, SourceK, TargetK],
    degree: Degree[I],
    /,
) -> CochainCohomologyMorphism[R, SourceK, TargetK, I]: ...


def map_cohomology_class[R, SourceK, TargetK, I: IntVar](
    morphism: CochainMorphism[R, SourceK, TargetK],
    degree: Degree[I],
    cohomology_class: CohomologyClass[R, SourceK, I],
    /,
) -> CohomologyClass[R, TargetK, I]: ...


def apply[R, V, N: IntVar, W, M: IntVar](
    linear_map: LinearMap[R, V, N, W, M],
    vector: Vector[R, V, N],
    /,
) -> Vector[R, W, M]: ...


def graded_multiply[G, P: IntVar, Q: IntVar](
    left: HomogeneousElement[G, P],
    right: HomogeneousElement[G, Q],
    /,
) -> HomogeneousElement[G, P + Q]: ...


def graded_map[SourceG, TargetG, P: IntVar](
    morphism: GradedMorphism[SourceG, TargetG],
    element: HomogeneousElement[SourceG, P],
    /,
) -> HomogeneousElement[TargetG, P]: ...


def dga_d[G, P: IntVar](
    algebra: DifferentialGradedCarrier[G],
    element: HomogeneousElement[G, P],
    /,
) -> HomogeneousElement[G, P + 1]: ...


def compose[R, U, L: IntVar, V, N: IntVar, W, M: IntVar](
    outer: LinearMap[R, V, N, W, M],
    inner: LinearMap[R, U, L, V, N],
    /,
) -> LinearMap[R, U, L, W, M]: ...


def lower_index[R, M, N: IntVar](
    form: BilinearForm[R, M, N],
    vector: Vector[R, M, N],
    /,
) -> Covector[R, M, N]: ...


def raise_index[R, M, N: IntVar](
    dual_form: DualBilinearForm[R, M, N],
    covector: Covector[R, M, N],
    /,
) -> Vector[R, M, N]: ...


def pair[R, M, N: IntVar](
    covector: Covector[R, M, N],
    vector: Vector[R, M, N],
    /,
) -> Scalar[R]: ...


def precompose_covector[R, V, N: IntVar, W, M: IntVar](
    covector: Covector[R, W, M],
    linear_map: LinearMap[R, V, N, W, M],
    /,
) -> Covector[R, V, N]: ...


def pullback_bilinear_form[R, V, N: IntVar, W, M: IntVar](
    form: BilinearForm[R, W, M],
    morphism: FreeModuleMorphism[R, V, N, W, M],
    /,
) -> BilinearForm[R, V, N]: ...


def dual_tensor[R, M, N: IntVar](
    value: BilinearForm[R, M, N], /
) -> DualBilinearForm[R, M, N]: ...


def wedge[Ctx, P: IntVar, Q: IntVar](
    left: DifferentialForm[Ctx, P],
    right: DifferentialForm[Ctx, Q],
    /,
) -> DifferentialForm[Ctx, P + Q]: ...


def d[Ctx, P: IntVar](
    form: DifferentialForm[Ctx, P], /
) -> DifferentialForm[Ctx, P + 1]: ...


def graded_commutator[Ctx, P: IntVar, Q: IntVar](
    left: GradedDerivationOperator[Ctx, P],
    right: GradedDerivationOperator[Ctx, Q],
    /,
) -> GradedDerivationOperator[Ctx, P + Q]: ...


def interior_operator[Ctx](vector_field: VectorField[Ctx], /) -> InteriorOperator[Ctx]: ...
def interior[Ctx, P: IntVar](
    vector_field: VectorField[Ctx],
    form: DifferentialForm[Ctx, P],
    /,
) -> DifferentialForm[Ctx, P - 1]: ...


def lie_derivative_operator[Ctx](
    vector_field: VectorField[Ctx], /
) -> LieDerivativeOperator[Ctx]: ...
def lie_derivative[Ctx, P: IntVar](
    vector_field: VectorField[Ctx],
    form: DifferentialForm[Ctx, P],
    /,
) -> DifferentialForm[Ctx, P]: ...


def lie_bracket[Ctx](
    left: VectorField[Ctx], right: VectorField[Ctx], /
) -> VectorField[Ctx]: ...


def form_hodge_star[Ctx, N: IntVar, P: IntVar](
    metric: PerfectMetric[Ctx, N],
    volume: Volume[Ctx, N],
    degree: Degree[P],
    form: MetricCovariantForm[Ctx, P],
    /,
) -> MetricCovariantForm[Ctx, N - P]: ...


def metric_tensor[Ctx, N: IntVar](
    metric: Metric[Ctx, N], /
) -> BilinearForm[MetricScalarRing[Ctx], Ctx, N]: ...


def correlation_morphism[Ctx, N: IntVar](
    metric: Metric[Ctx, N], /
) -> FreeModuleMorphism[
    MetricScalarRing[Ctx], Ctx, N, Dual[Ctx], N
]: ...


def correlation_isomorphism[Ctx, N: IntVar](
    metric: PerfectMetric[Ctx, N], /
) -> FreeModuleIsomorphism[
    MetricScalarRing[Ctx], Ctx, N, Dual[Ctx], N
]: ...


def poincare_duality[Ctx, N: IntVar, P: IntVar](
    metric: Metric[Ctx, N],
    volume: Volume[Ctx, N],
    degree: Degree[P],
    /,
) -> PoincareDualityIsomorphism[Ctx, N, P]: ...


def hodge_star_isomorphism[Ctx, N: IntVar, P: IntVar](
    metric: PerfectMetric[Ctx, N],
    volume: Volume[Ctx, N],
    degree: Degree[P],
    /,
) -> HodgeStarIsomorphism[Ctx, N, P]: ...


def form_hodge_star_over_fraction_field[Ctx, N: IntVar, P: IntVar](
    metric: NondegenerateMetric[Ctx, N],
    volume: Volume[Ctx, N],
    degree: Degree[P],
    form: FractionFieldCovariantForm[Ctx, P],
    /,
) -> FractionFieldCovariantForm[Ctx, N - P]: ...


def multivector_hodge_star[Ctx, N: IntVar, P: IntVar](
    metric: Metric[Ctx, N],
    volume: Volume[Ctx, N],
    degree: Degree[P],
    multivector: Multivector[Ctx, P],
    /,
) -> Multivector[Ctx, N - P]: ...


def covariant_d[Ctx, E, P: IntVar](
    connection: FlatConnection[Ctx, E],
    coefficient_form: CoefficientForm[Ctx, E, P],
    /,
) -> CoefficientForm[Ctx, E, P + 1]: ...


def connection_de_rham_module[Ctx, E](
    connection: FlatConnection[Ctx, E], /
) -> CoefficientDeRhamModule[Ctx, E]: ...


def coefficient_zero_form[Ctx, E](
    dg_module: CoefficientDeRhamModule[Ctx, E],
    coefficient: ModuleElement[AlgebraRing[Ctx], E],
    /,
) -> CoefficientForm[Ctx, E, 0]: ...


def dg_module_act[AlgebraG, M, P: IntVar, Q: IntVar](
    dg_module: DifferentialGradedModule[AlgebraG, M],
    module_element: DGModuleElement[AlgebraG, M, P],
    algebra_element: HomogeneousElement[AlgebraG, Q],
    /,
) -> DGModuleElement[AlgebraG, M, P + Q]: ...


def dg_module_d[AlgebraG, M, P: IntVar](
    dg_module: DifferentialGradedModule[AlgebraG, M],
    module_element: DGModuleElement[AlgebraG, M, P],
    /,
) -> DGModuleElement[AlgebraG, M, P + 1]: ...


def cup[Ctx, P: IntVar, Q: IntVar](
    left: DeRhamClass[Ctx, P],
    right: DeRhamClass[Ctx, Q],
    /,
) -> DeRhamClass[Ctx, P + Q]: ...


def de_rham_map[R, SourceEta, SourceA, TargetEta, TargetA](
    morphism: RelativeAlgebraMorphism[
        R, SourceEta, SourceA, TargetEta, TargetA
    ],
    /,
) -> DGAMorphism[
    RelativeContext[SourceEta, R, SourceA],
    RelativeContext[TargetEta, R, TargetA],
]: ...


def pullback_form[
    R, SourceEta, SourceA, TargetEta, TargetA, P: IntVar
](
    morphism: RelativeAlgebraMorphism[
        R, SourceEta, SourceA, TargetEta, TargetA
    ],
    form: DifferentialForm[RelativeContext[SourceEta, R, SourceA], P],
    /,
) -> DifferentialForm[RelativeContext[TargetEta, R, TargetA], P]: ...


def de_rham_cohomology_map[
    R, SourceEta, SourceA, TargetEta, TargetA, I: IntVar
](
    morphism: RelativeAlgebraMorphism[
        R, SourceEta, SourceA, TargetEta, TargetA
    ],
    degree: Degree[I],
    /,
) -> CohomologyMorphism[
    RelativeContext[SourceEta, R, SourceA],
    RelativeContext[TargetEta, R, TargetA],
    I,
]: ...


def pullback_de_rham_class[
    R, SourceEta, SourceA, TargetEta, TargetA, I: IntVar
](
    morphism: RelativeAlgebraMorphism[
        R, SourceEta, SourceA, TargetEta, TargetA
    ],
    degree: Degree[I],
    cohomology_class: DeRhamClass[RelativeContext[SourceEta, R, SourceA], I],
    /,
) -> DeRhamClass[RelativeContext[TargetEta, R, TargetA], I]: ...
