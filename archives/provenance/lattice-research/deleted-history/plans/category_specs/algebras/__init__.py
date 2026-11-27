"""Static algebra category surface for the category spec redesign.

Subcategory hierarchy::

    Algebras(R)
    |-- Commutative()
    |-- WithBasis()
    |   `-- FiniteDimensional()
    |-- FiniteDimensional()
    |-- Semisimple()
    |-- Subobjects()
    |-- Quotients()
    |-- Subquotients()
    |-- ObjectsOver()
    |-- ObjectsUnder()
    |-- Ideals(A)
    |-- CartesianProducts()
    |-- TensorProducts()
    |-- DualObjects()
    `-- HomCategory()
        |-- EndCategory()
        `-- AutCategory()
"""

from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any, final, override

from sage.categories.associative_algebras import AssociativeAlgebras as SageAssociativeAlgebras
from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.magmatic_algebras import MagmaticAlgebras as SageMagmaticAlgebras
from sage.misc.abstract_method import abstract_method
from sage.misc.cachefunc import cached_method
from sage.misc.lazy_import import LazyImport

from ..cat import (
    Cat,
    Category,
    Category_module,
    Category_over_base_ring,
    CategoryWithAxiom_over_base_ring,
)
from ..modules import Modules
from ..utils import refine_category
from .homsets import AlgebraAutCategory, AlgebraEndCategory, AlgebraHomCategory
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.ideals import AlgebraIdealsCategory
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients
from .subcategories.constructions.tensor_products import _TensorProducts

if TYPE_CHECKING:
    from ..types import (
        AdditiveGroup,
        AdditiveMonoid,
        AdditiveSemigroup,
        Algebra,
        AlgebraElement,
        AlgebraIdeal,
        AssociativeAlgebra,
        Group,
        HochschildChainComplex,
        Integer,
        Magma,
        MagmaticAlgebra,
        Matrix,
        Monoid,
        RAlgebra,
        Ring,
        RModule,
        Semigroup,
        Set,
        SetFamily,
        Tensor,
    )


class _MagmaticAlgebraParentMethods:
    r"""Methods on modules equipped with a bilinear multiplication."""


class _MagmaticAlgebraElementMethods:
    r"""Methods on elements of magmatic algebras."""

    @abstract_method
    def __mul__(self, other: AlgebraElement) -> AlgebraElement:
        r"""Return the bilinear product of this element with ``other``."""
        ...


class _MagmaticAlgebraMorphismMethods:
    r"""Methods on magmatic algebra morphisms."""


class MagmaticAlgebras(Category_over_base_ring):
    r"""Category of modules over ``R`` equipped with a bilinear multiplication.

    Canonical chain: ``MagmaticAlgebras(R)``.
    """

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageMagmaticAlgebras(self.base_ring()),)

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"magmatic algebras over {self.base_ring()}"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return module and Sage magmatic-algebra supercategories."""
        R = self.base_ring()
        return [Modules(R), SageMagmaticAlgebras(R)]

    @override
    @final
    def additional_structure(self):
        r"""Return ``None`` because the multiplication is already morphism data."""
        return None

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is a Sage magmatic algebra over this base ring."""
        return A in SageMagmaticAlgebras(self.base_ring())

    ParentMethods = _MagmaticAlgebraParentMethods
    ElementMethods = _MagmaticAlgebraElementMethods
    MorphismMethods = _MagmaticAlgebraMorphismMethods

    Associative = LazyImport("category_specs.algebras", "AssociativeAlgebras")


class AssociativeAlgebras(CategoryWithAxiom_over_base_ring):
    r"""Category of associative, not necessarily unital, algebras over ``R``.

    Canonical chain: ``MagmaticAlgebras(R).Associative()``.
    """

    _base_category_class_and_axiom = (MagmaticAlgebras, "Associative")

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return magmatic and Sage associative-algebra supercategories."""
        R = self.base_ring()
        return [MagmaticAlgebras(R), SageAssociativeAlgebras(R)]

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is a Sage associative algebra over this base ring."""
        return (
            A in MagmaticAlgebras(self.base_ring())
            and A in SageAssociativeAlgebras(self.base_ring())
        )

    class ParentMethods:
        @final
        def is_associative(self) -> bool:
            r"""Return whether multiplication satisfies ``(xy)z = x(yz)`` for all elements."""
            return True

    class ElementMethods: ...
    class MorphismMethods: ...


class _AlgebraParentMethods:
    @abstract_method
    def base_ring(self) -> Ring:
        r"""Return the scalar ring over which this algebra is defined."""
        ...

    @abstract_method
    def change_ring(self, R: Ring) -> Algebra:
        r"""Return the scalar extension or base change of this algebra to ``R``."""
        ...

    @abstract_method
    def algebra_generators(self) -> SetFamily:
        r"""Return algebra generators for this algebra as an ``R``-algebra."""
        ...

    @abstract_method
    def center(self) -> Algebra:
        r"""Return the center of this algebra."""
        ...

    @abstract_method
    def radical(self) -> AlgebraIdeal:
        r"""Return the Jacobson radical of this algebra."""
        ...

    @abstract_method
    def subalgebra(
        self,
        generators: Sequence[AlgebraElement],
    ) -> Algebra:
        r"""Return the subalgebra generated by ``generators``."""
        ...

    @final
    def left_ideal(self, generators: Sequence[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the smallest ``R``-submodule containing ``generators`` and closed under left multiplication by ``A``."""
        return self.ideal_submodule(generators, side="left")

    @final
    def right_ideal(self, generators: Sequence[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the smallest ``R``-submodule containing ``generators`` and closed under right multiplication by ``A``."""
        return self.ideal_submodule(generators, side="right")

    @final
    def two_sided_ideal(self, generators: Sequence[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the smallest ``R``-submodule containing ``generators`` and closed under left and right multiplication by ``A``."""
        return self.ideal_submodule(generators, side="twosided")

    @final
    def principal_left_ideal(self, generator: AlgebraElement) -> AlgebraIdeal:
        r"""Return the principal left ideal ``A * generator``."""
        return self.principal_ideal(generator, side="left")

    @final
    def principal_right_ideal(self, generator: AlgebraElement) -> AlgebraIdeal:
        r"""Return the principal right ideal ``generator * A``."""
        return self.principal_ideal(generator, side="right")

    @final
    def principal_two_sided_ideal(self, generator: AlgebraElement) -> AlgebraIdeal:
        r"""Return the principal two-sided ideal ``A * generator * A``."""
        return self.principal_ideal(generator, side="twosided")

    @abstract_method
    def derivations(self) -> RModule:
        r"""Return the module of derivations of this algebra."""
        ...

    @abstract_method
    def annihilator(self, elements: Iterable[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the ideal annihilating every element in ``elements``."""
        ...

    @final
    def ideals(self) -> Category:
        r"""Return the ideal construction category owned by this algebra."""
        return self.category().Ideals(self)

    @abstract_method
    def hochschild_complex(self, coefficients: RModule) -> HochschildChainComplex:
        r"""Return the Hochschild chain complex with coefficients in ``coefficients``."""
        ...

    @override
    @abstract_method
    def has_standard_involution(self) -> bool:
        r"""Return whether this algebra has Sage's standard involution."""
        ...

    @abstract_method
    def idempotent_lift(self, x: AlgebraElement) -> AlgebraElement:
        r"""Lift the idempotent ``x`` along the algebra's radical quotient."""
        ...

    @abstract_method
    def peirce_decomposition(
        self,
        idempotents: Sequence[AlgebraElement] | None = None,
        check: bool = True,
    ) -> Sequence[Sequence[Algebra]]:
        r"""Return the Peirce decomposition determined by ``idempotents``."""
        ...

    @abstract_method
    def semisimple_quotient(self) -> Algebra:
        r"""Return the quotient of this algebra by its Jacobson radical."""
        ...


class _AlgebraElementMethods:
    r"""Methods on elements of algebras."""


class _AlgebraMorphismMethods:
    r"""Methods on algebra morphisms."""


class Algebras(Category_module):
    r"""Category of algebras over a fixed base ring.

    Canonical chain: ``Algebras(R)``.
    """

    @override
    @final
    def _sage_super_categories(self) -> tuple[Category, ...]:
        return (SageAlgebras(self.base_ring()),)

    @override
    @final
    def _repr_object_names(self) -> str:
        return f"algebras over {self.base_ring()}"

    @override
    @final
    def super_categories(self) -> list[Category]:
        r"""Return rings-under-``R``, modules over ``R``, and Sage algebras."""
        from ..rings import Rings

        R = self.base_ring()
        return [
            AssociativeAlgebras(R),
            Rings().RingsUnder(R),
            Modules(R),
            SageAlgebras(R),
        ]

    ParentMethods = _AlgebraParentMethods
    ElementMethods = _AlgebraElementMethods
    MorphismMethods = _AlgebraMorphismMethods
    HomCategory = AlgebraHomCategory

    class SubcategoryMethods:
        @cached_method
        @final
        def Commutative(self) -> Category:
            r"""Return the subcategory of commutative algebras."""
            return self._with_axiom("Commutative")

        @cached_method
        @final
        def WithBasis(self) -> Category:
            r"""Return the subcategory of algebras with a distinguished basis."""
            return self._with_axiom("WithBasis")

        @cached_method
        @final
        def FiniteDimensional(self) -> Category:
            r"""Return the subcategory of finite-dimensional algebras."""
            return self._with_axiom("FiniteDimensional")

        @cached_method
        @final
        def Semisimple(self) -> Category:
            r"""Return the subcategory of semisimple algebras."""
            return self._with_axiom("Semisimple")

        @cached_method
        @final
        def TensorProducts(self) -> Category:
            r"""Return the tensor-product construction category of algebras."""
            return _TensorProducts.category_of(self)

        @cached_method
        @final
        def DualObjects(self) -> Category:
            r"""Return the dual-object construction category of algebras."""
            return _DualObjects.category_of(self)

        @final
        def Ideals(self, algebra: Algebra) -> Category:
            r"""Return the category of ideals in ``algebra``."""
            assert algebra in self, f"Ideals expects an algebra in {self}: {algebra}"
            return AlgebraIdealsCategory(algebra)

    class Constructors:
        r"""Algebra constructors over a fixed base ring.

        These constructors name the free functors from specific source
        categories into the corresponding category of ``R``-algebra objects.
        Sage's generic ``S.algebra(R)`` compatibility method is not the public
        project API.
        """

        def __init__(self, category: RAlgebra) -> None:
            self._category = category

        @final
        def category(self) -> RAlgebra:
            r"""Return the algebra category whose constructors this object names."""
            return self._category

        @final
        def base_ring(self) -> Ring:
            r"""Return the base ring of the constructed algebras."""
            return self.category().base_ring()

        @final
        def _refine_constructed_algebra(self, algebra: Algebra, categories: Sequence[Category]) -> Algebra:
            return refine_category(algebra, [self.category(), *categories])

        @final
        def _refine_constructed_magmatic_algebra(
            self,
            algebra: MagmaticAlgebra,
            categories: Sequence[Category],
        ) -> MagmaticAlgebra:
            return refine_category(algebra, [MagmaticAlgebras(self.base_ring()), *categories])

        @final
        def _sage_algebra_from_source(
            self,
            source: Magma | Semigroup | Monoid | Group | AdditiveSemigroup | AdditiveMonoid | AdditiveGroup,
            source_category: Category,
        ) -> Algebra:
            assert source in source_category, f"Expected source in {source_category}: {source}"
            algebra = source.algebra(self.base_ring(), category=source_category)
            return self._refine_constructed_algebra(algebra, [self.category().WithBasis()])

        @final
        def _sage_algebra_from_source_with_target(
            self,
            source: Magma | Semigroup | AdditiveSemigroup,
            source_category: Category,
            target_category: Category,
            project_target_category: Category,
        ) -> MagmaticAlgebra:
            assert source in source_category, f"Expected source in {source_category}: {source}"
            algebra = source.algebra(self.base_ring(), category=source_category)
            assert algebra in target_category, (
                f"Sage constructed algebra should lie in {target_category}: {algebra.category()}"
            )
            return self._refine_constructed_magmatic_algebra(algebra, [project_target_category, target_category])

        @final
        def free_algebra_from_set(self, generators: Set) -> Algebra:
            r"""Return the free associative unital ``R``-algebra on ``generators``."""
            from sage.algebras.free_algebra import FreeAlgebra

            assert generators.is_finite(), "free_algebra_from_set currently requires a finite generator set"
            algebra = FreeAlgebra(self.base_ring(), generators.cardinality(), "x")
            return self._refine_constructed_algebra(algebra, [self.category().WithBasis()])

        @final
        def free_algebra_from_magma(self, magma: Magma) -> MagmaticAlgebra:
            r"""Return the ``R``-module with basis ``magma`` and product extended ``R``-bilinearly from the magma law."""
            from sage.categories.magmas import Magmas

            target = SageMagmaticAlgebras(self.base_ring()).WithBasis()
            return self._sage_algebra_from_source_with_target(
                magma,
                Magmas(),
                target,
                MagmaticAlgebras(self.base_ring()),
            )

        @final
        def free_algebra_from_semigroup(self, semigroup: Semigroup) -> AssociativeAlgebra:
            r"""Return the semigroup algebra ``R[S]`` with basis ``S`` and multiplication induced by the semigroup law."""
            from sage.categories.semigroups import Semigroups

            target = SageAssociativeAlgebras(self.base_ring()).WithBasis()
            return self._sage_algebra_from_source_with_target(
                semigroup,
                Semigroups(),
                target,
                AssociativeAlgebras(self.base_ring()),
            )

        @final
        def free_algebra_from_monoid(self, monoid: Monoid) -> Algebra:
            r"""Return the monoid algebra over ``R``."""
            from sage.categories.monoids import Monoids

            return self._sage_algebra_from_source(monoid, Monoids())

        @final
        def free_algebra_from_group(self, group: Group) -> Algebra:
            r"""Return the group algebra over ``R``."""
            from sage.categories.groups import Groups

            return self._sage_algebra_from_source(group, Groups())

        @final
        def free_algebra_from_additive_semigroup(self, semigroup: AdditiveSemigroup) -> AssociativeAlgebra:
            r"""Return the semigroup algebra with product ``[x][y] = [x + y]`` extended ``R``-bilinearly."""
            from sage.categories.additive_semigroups import AdditiveSemigroups

            target = SageAssociativeAlgebras(self.base_ring()).WithBasis()
            return self._sage_algebra_from_source_with_target(
                semigroup,
                AdditiveSemigroups(),
                target,
                AssociativeAlgebras(self.base_ring()),
            )

        @final
        def free_algebra_from_additive_monoid(self, monoid: AdditiveMonoid) -> Algebra:
            r"""Return the monoid algebra with product ``[x][y] = [x + y]`` and unit the additive identity."""
            from sage.categories.additive_monoids import AdditiveMonoids

            return self._sage_algebra_from_source(monoid, AdditiveMonoids())

        @final
        def free_algebra_from_additive_group(self, group: AdditiveGroup) -> Algebra:
            r"""Return the group algebra with product ``[x][y] = [x + y]`` and inverses from the additive group law."""
            from sage.categories.additive_groups import AdditiveGroups

            return self._sage_algebra_from_source(group, AdditiveGroups())

        @final
        def _right_multiplication_table(
            self,
            structure_constants: Sequence[Matrix],
            rank: Integer,
        ) -> Sequence[Matrix]:
            from sage.matrix.constructor import matrix

            assert all(
                constants.nrows() == rank and constants.ncols() == rank
                for constants in structure_constants
            ), f"Each structure-constant matrix must be {rank} by {rank}: {structure_constants}"
            return tuple(
                matrix(
                    self.base_ring(),
                    [
                        [structure_constants[output][left, right] for output in range(rank)]
                        for left in range(rank)
                    ],
                )
                for right in range(rank)
            )

        @final
        def from_multiplication_tensor(self, multiplication: Tensor) -> MagmaticAlgebra:
            r"""Return the algebra whose product is encoded by ``multiplication``.

            The tensor must lie in ``T_R(M)[1, 2]``. Its parent determines the
            underlying module ``M``, the base ring ``R``, and the preferred
            generating set used for coordinates; no separate basis, table, list
            of matrices, module-element matrix, or right-multiplication data
            belongs in this constructor surface.
            """
            assert multiplication.tensor_type() == (1, 2), (
                f"Algebra multiplication tensors must have type (1, 2): {multiplication.tensor_type()}"
            )
            base_module = multiplication.base_module()
            assert base_module.base_ring() is self.base_ring(), (
                f"Multiplication tensor must be over {self.base_ring()}: {base_module.base_ring()}"
            )
            structure_constants = multiplication.structure_constants()
            assert len(structure_constants) == base_module.rank(), (
                f"Expected one coordinate matrix for each output generator of {base_module}: {structure_constants}"
            )
            from sage.algebras.finite_dimensional_algebras.finite_dimensional_algebra import FiniteDimensionalAlgebra

            R = self.base_ring()
            table = self._right_multiplication_table(structure_constants, base_module.rank())
            sage_magmatic_target = SageMagmaticAlgebras(R).FiniteDimensional().WithBasis()
            algebra = FiniteDimensionalAlgebra(R, table, category=sage_magmatic_target)
            categories: list[Category] = [sage_magmatic_target]
            if algebra.is_associative():
                categories.extend(
                    [
                        AssociativeAlgebras(R),
                        SageAssociativeAlgebras(R).FiniteDimensional().WithBasis(),
                    ]
                )
                if algebra.is_unitary():
                    categories.extend(
                        [
                            self.category(),
                            self.category().FiniteDimensional(),
                            self.category().WithBasis(),
                            self.category().WithBasis().FiniteDimensional(),
                        ]
                    )
            return self._refine_constructed_magmatic_algebra(algebra, categories)

    _Constructors = Constructors

    @cached_method
    @final
    def Constructors(self):
        r"""Return the named algebra constructor collector over this base ring."""
        return self.__class__._Constructors(self)

    Commutative = LazyImport("category_specs.algebras.subcategories.commutative", "_CommutativeAlgebras")
    WithBasis = LazyImport("category_specs.algebras.subcategories.with_basis", "_AlgebrasWithBasis")
    FiniteDimensional = LazyImport(
        "category_specs.algebras.subcategories.finite_dimensional",
        "_FiniteDimensionalAlgebras",
    )
    Semisimple = LazyImport("category_specs.algebras.subcategories.semisimple", "_SemisimpleAlgebras")

    Subobjects = _Subobjects
    Quotients = _Quotients
    Subquotients = _Subquotients
    ObjectsOver = _ObjectsOver
    ObjectsUnder = _ObjectsUnder
    Ideals = AlgebraIdealsCategory
    CartesianProducts = _CartesianProducts
    TensorProducts = _TensorProducts
    DualObjects = _DualObjects


AlgebrasCategory = Algebras
AlgebrasObject = Algebras.ParentMethods
AlgebrasElement = Algebras.ElementMethods
AlgebrasMorphism = Algebras.MorphismMethods
AlgebrasHomCategory = AlgebraHomCategory
AlgebrasEndCategory = AlgebraEndCategory
AlgebrasAutCategory = AlgebraAutCategory
AlgebrasHom = AlgebraHomCategory.ParentMethods
AlgebrasEnd = AlgebraEndCategory.ParentMethods
AlgebrasAut = AlgebraAutCategory.ParentMethods
AlgebrasEndomorphism = AlgebraEndCategory.ElementMethods
AlgebrasAutomorphism = AlgebraAutCategory.ElementMethods

MagmaticAlgebrasCategory = MagmaticAlgebras
MagmaticAlgebrasObject = MagmaticAlgebras.ParentMethods
MagmaticAlgebrasElement = MagmaticAlgebras.ElementMethods
MagmaticAlgebrasMorphism = MagmaticAlgebras.MorphismMethods
AssociativeAlgebrasCategory = AssociativeAlgebras
AssociativeAlgebrasObject = AssociativeAlgebras.ParentMethods
AssociativeAlgebrasElement = AssociativeAlgebras.ElementMethods
AssociativeAlgebrasMorphism = AssociativeAlgebras.MorphismMethods
