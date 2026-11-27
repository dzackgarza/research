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

from abc import abstractmethod
from collections.abc import Callable, Iterable, Sequence
from typing import TYPE_CHECKING, Any, Literal, TypeVar, final, overload, override, TypeAlias

from sage.categories.algebras import Algebras as SageAlgebras
from sage.categories.associative_algebras import (
    AssociativeAlgebras as SageAssociativeAlgebras,
)
from sage.categories.magmatic_algebras import MagmaticAlgebras as SageMagmaticAlgebras
from sage.misc.lazy_import import LazyImport

from ..cat import (
    Category,
    Category_module,
    Category_over_base_ring,
    CategoryWithAxiom_over_base_ring,
)
from ..modules import Modules
from ..utils import refine_category
from .homsets import (
    AlgebraAutCategory,
    AlgebraEndCategory,
    AlgebraHomCategory,
)
from .homsets import (
    _AlgebraHomomorphisms as _AlgebraHomomorphisms,
)
from .subcategories.constructions.cartesian_products import _CartesianProducts
from .subcategories.constructions.dual_objects import _DualObjects
from .subcategories.constructions.ideals import AlgebraIdealsCategory
from .subcategories.constructions.objects_over import _ObjectsOver
from .subcategories.constructions.objects_under import _ObjectsUnder
from .subcategories.constructions.quotients import _Quotients
from .subcategories.constructions.subobjects import _Subobjects
from .subcategories.constructions.subquotients import _Subquotients
from .subcategories.constructions.tensor_products import _TensorProducts

_F = TypeVar("_F", bound=Callable[..., object])

if TYPE_CHECKING:
    from ..spec_core import ConstructorRegistry
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
        SetElement,
        SetFamily,
        Tensor,
    )


class _MagmaticAlgebraParentMethods:
    r"""Methods on modules equipped with a bilinear multiplication."""


class _MagmaticAlgebraElementMethods:
    r"""Methods on elements of magmatic algebras."""

    @abstractmethod
    def __mul__(self, other: AlgebraElement) -> AlgebraElement:
        r"""Return the bilinear product of this element with ``other``."""
        ...


class MagmaticAlgebras(Category_over_base_ring):
    r"""Category of modules over ``R`` equipped with a bilinear multiplication.

    Canonical chain: ``MagmaticAlgebras(R)``.
    """

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

    @final
    def additional_structure(self) -> None:
        r"""Return ``None`` because the multiplication is already morphism data."""
        return None

    @override
    @final
    def __contains__(self, A: Any) -> bool:
        r"""Return whether ``A`` is a Sage magmatic algebra over this base ring."""
        return A in SageMagmaticAlgebras(self.base_ring())

    ParentMethods : TypeAlias = _MagmaticAlgebraParentMethods
    ElementMethods : TypeAlias = _MagmaticAlgebraElementMethods

    class _Constructors:
        r"""Magmatic-algebra constructors over a fixed base ring."""

        def __init__(self, category: MagmaticAlgebras) -> None:
            self._category = category

        @final
        def category(self) -> MagmaticAlgebras:
            r"""Return the magmatic algebra category whose constructors are named."""
            return self._category

        @final
        def base_ring(self) -> Ring:
            r"""Return the base ring of the constructed magmatic algebras."""
            return self.category().base_ring()

        @final
        def _refine_constructed_magmatic_algebra(
            self,
            algebra: MagmaticAlgebra,
            category: Category,
        ) -> MagmaticAlgebra:
            return refine_category(
                algebra,
                category,
                test=False,
            )

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
            assert algebra in target_category, f"Sage constructed algebra should lie in {target_category}: {algebra.category()}"
            return self._refine_constructed_magmatic_algebra(algebra, project_target_category)

        @final
        def algebra(self, *, magma: Magma) -> MagmaticAlgebra:
            r"""Return the ``R``-module with basis ``magma``.

            The product is extended ``R``-bilinearly from the magma law.
            """
            from sage.categories.magmas import Magmas

            target = SageMagmaticAlgebras(self.base_ring()).WithBasis()
            return self._sage_algebra_from_source_with_target(
                magma,
                Magmas(),
                target,
                self.category(),
            )

        @final
        def _right_multiplication_table(
            self,
            structure_constants: Sequence[Matrix],
            rank: Integer,
        ) -> Sequence[Matrix]:
            from sage.matrix.constructor import matrix

            assert all(constants.nrows() == rank and constants.ncols() == rank for constants in structure_constants), (
                f"Each structure-constant matrix must be {rank} by {rank}: {structure_constants}"
            )
            return tuple(
                matrix(
                    self.base_ring(),
                    [[structure_constants[output][left, right] for output in range(rank)] for left in range(rank)],
                )
                for right in range(rank)
            )

        @final
        def FiniteDimensionalAlgebra(self, *, multiplication: Tensor) -> MagmaticAlgebra:
            r"""Return the algebra whose product is encoded by ``multiplication``.

            The tensor must lie in ``T_R(M)[1, 2]``. Its parent determines the
            underlying module ``M``, the base ring ``R``, and the preferred
            generating set used for coordinates; no separate basis, table, list
            of matrices, module-element matrix, or right-multiplication data
            belongs in this constructor surface.
            """
            assert multiplication.tensor_type() == (1, 2), f"Algebra multiplication tensors must have type (1, 2): {multiplication.tensor_type()}"
            base_module = multiplication.base_module()
            assert base_module.base_ring() is self.base_ring(), f"Multiplication tensor must be over {self.base_ring()}: {base_module.base_ring()}"
            structure_constants = multiplication.structure_constants()
            assert len(structure_constants) == base_module.rank(), f"Expected one coordinate matrix for each output generator of {base_module}: {structure_constants}"
            from sage.algebras.finite_dimensional_algebras import (
                finite_dimensional_algebra,
            )

            R = self.base_ring()
            FiniteDimensionalAlgebra = finite_dimensional_algebra.FiniteDimensionalAlgebra
            table = self._right_multiplication_table(structure_constants, base_module.rank())
            sage_magmatic_target = SageMagmaticAlgebras(R).FiniteDimensional().WithBasis()
            algebra = FiniteDimensionalAlgebra(R, table, category=sage_magmatic_target)
            project_target: Category = self.category()
            if algebra.is_associative():
                project_target = AssociativeAlgebras(R)
                if algebra.is_unitary():
                    project_target = Algebras(R).WithBasis().FiniteDimensional()
            return self._refine_constructed_magmatic_algebra(algebra, project_target)

    @final
    def Constructors(self) -> MagmaticAlgebras._Constructors:
        r"""Return the named magmatic-algebra constructor collector."""
        return self.__class__._Constructors(self)

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
        return A in MagmaticAlgebras(self.base_ring()) and A in SageAssociativeAlgebras(self.base_ring())

    class ParentMethods:
        @final
        def is_associative(self) -> bool:
            r"""Return whether multiplication satisfies ``(xy)z = x(yz)``.

            This is required for all elements.
            """
            return True

    class ElementMethods: ...

    class _Constructors(MagmaticAlgebras._Constructors):
        r"""Associative, not-necessarily-unital algebra constructors."""

        def __init__(self, category: AssociativeAlgebras) -> None:
            self._category = category

        @override
        @final
        def category(self) -> AssociativeAlgebras:
            r"""Return the associative algebra category whose constructors are named."""
            return self._category

        @overload
        def algebra(self, *, semigroup: Semigroup) -> AssociativeAlgebra: ...

        @overload
        def algebra(self, *, additive_semigroup: AdditiveSemigroup) -> AssociativeAlgebra: ...

        @final
        def algebra(
            self,
            *,
            semigroup: Semigroup | None = None,
            additive_semigroup: AdditiveSemigroup | None = None,
        ) -> AssociativeAlgebra:
            r"""Return the semigroup algebra ``R[S]`` with basis ``S``.

            Multiplication is induced by the semigroup law.
            """
            assert (semigroup is None) != (additive_semigroup is None), "algebra requires exactly one named source: semigroup or additive_semigroup"
            target = SageAssociativeAlgebras(self.base_ring()).WithBasis()
            if semigroup is not None:
                from sage.categories.semigroups import Semigroups

                return self._sage_algebra_from_source_with_target(
                    semigroup,
                    Semigroups(),
                    target,
                    self.category(),
                )
            from sage.categories.additive_semigroups import AdditiveSemigroups

            assert additive_semigroup is not None
            return self._sage_algebra_from_source_with_target(
                additive_semigroup,
                AdditiveSemigroups(),
                target,
                self.category(),
            )

    @final
    def Constructors(self) -> AssociativeAlgebras._Constructors:
        r"""Return the named associative-algebra constructor collector."""
        return self.__class__._Constructors(self)


class _AlgebraParentMethods:
    @abstractmethod
    def base_ring(self) -> Ring:
        r"""Return the scalar ring over which this algebra is defined."""
        ...

    @abstractmethod
    def change_ring(self, R: Ring) -> Algebra:
        r"""Return the scalar extension or base change of this algebra to ``R``."""
        ...

    @abstractmethod
    def algebra_generators(self) -> SetFamily:
        r"""Return algebra generators for this algebra as an ``R``-algebra."""
        ...

    @abstractmethod
    def center(self) -> Algebra:
        r"""Return the center of this algebra."""
        ...

    @abstractmethod
    def radical(self) -> AlgebraIdeal:
        r"""Return the Jacobson radical of this algebra."""
        ...

    @abstractmethod
    def subalgebra(
        self,
        generators: Sequence[AlgebraElement],
    ) -> Algebra:
        r"""Return the subalgebra generated by ``generators``."""
        ...

    @final
    def left_ideal(self, generators: Sequence[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the smallest ``R``-submodule containing ``generators``.

        It is closed under left multiplication by ``A``.
        """
        algebra_parent: Any = self
        ideal: AlgebraIdeal = algebra_parent.ideal_submodule(generators, side="left")
        return ideal

    @final
    def right_ideal(self, generators: Sequence[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the smallest ``R``-submodule containing ``generators``.

        It is closed under right multiplication by ``A``.
        """
        algebra_parent: Any = self
        ideal: AlgebraIdeal = algebra_parent.ideal_submodule(generators, side="right")
        return ideal

    @final
    def two_sided_ideal(self, generators: Sequence[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the smallest ``R``-submodule containing ``generators`` and
        closed under left and right multiplication by ``A``."""
        algebra_parent: Any = self
        ideal: AlgebraIdeal = algebra_parent.ideal_submodule(generators, side="twosided")
        return ideal

    @final
    def principal_left_ideal(self, generator: AlgebraElement) -> AlgebraIdeal:
        r"""Return the principal left ideal ``A * generator``."""
        algebra_parent: Any = self
        ideal: AlgebraIdeal = algebra_parent.principal_ideal(generator, side="left")
        return ideal

    @final
    def principal_right_ideal(self, generator: AlgebraElement) -> AlgebraIdeal:
        r"""Return the principal right ideal ``generator * A``."""
        algebra_parent: Any = self
        ideal: AlgebraIdeal = algebra_parent.principal_ideal(generator, side="right")
        return ideal

    @final
    def principal_two_sided_ideal(self, generator: AlgebraElement) -> AlgebraIdeal:
        r"""Return the principal two-sided ideal ``A * generator * A``."""
        algebra_parent: Any = self
        ideal: AlgebraIdeal = algebra_parent.principal_ideal(generator, side="twosided")
        return ideal

    @abstractmethod
    def derivations(self) -> RModule:
        r"""Return the module of derivations of this algebra."""
        ...

    @abstractmethod
    def annihilator(self, elements: Iterable[AlgebraElement]) -> AlgebraIdeal:
        r"""Return the ideal annihilating every element in ``elements``."""
        ...

    @final
    def ideals(self) -> Category:
        r"""Return the ideal construction category owned by this algebra."""
        return self.category().Ideals(self)

    @abstractmethod
    def hochschild_complex(self, coefficients: RModule) -> HochschildChainComplex:
        r"""Return the Hochschild chain complex with given coefficients."""
        del coefficients
        ...

    @abstractmethod
    def idempotent_lift(self, x: AlgebraElement) -> AlgebraElement:
        r"""Lift the idempotent ``x`` along the algebra's radical quotient."""
        ...

    @abstractmethod
    def peirce_decomposition(
        self,
        idempotents: Sequence[AlgebraElement] | None = None,
        check: bool = True,
    ) -> Sequence[Sequence[Algebra]]:
        r"""Return the Peirce decomposition determined by ``idempotents``."""
        ...

    @abstractmethod
    def semisimple_quotient(self) -> Algebra:
        r"""Return the quotient of this algebra by its Jacobson radical."""
        ...


class _AlgebraElementMethods:
    r"""Methods on elements of algebras."""


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
            SageAlgebras(R),
        ]

    ParentMethods : TypeAlias = _AlgebraParentMethods
    ElementMethods : TypeAlias = _AlgebraElementMethods
    HomCategory : TypeAlias = AlgebraHomCategory

    class SubcategoryMethods:
        @final
        def Commutative(self) -> Category:
            r"""Return the subcategory of commutative algebras."""
            return self._with_axiom("Commutative")

        @final
        def WithBasis(self) -> Category:
            r"""Return the subcategory of algebras with a distinguished basis."""
            return self._with_axiom("WithBasis")

        @final
        def FiniteDimensional(self) -> Category:
            r"""Return the subcategory of finite-dimensional algebras."""
            return self._with_axiom("FiniteDimensional")

        @final
        def Semisimple(self) -> Category:
            r"""Return the subcategory of semisimple algebras."""
            return self._with_axiom("Semisimple")

        @final
        def TensorProducts(self) -> Category:
            r"""Return the tensor-product construction category of algebras."""
            return _TensorProducts.category_of(self)

        @final
        def DualObjects(self) -> Category:
            r"""Return the dual-object construction category of algebras."""
            return _DualObjects.category_of(self)

        @final
        def Ideals(self, algebra: Algebra) -> Category:
            r"""Return the category of ideals in ``algebra``."""
            assert algebra in self, f"Ideals expects an algebra in {self}: {algebra}"
            return AlgebraIdealsCategory(algebra)

    class _Constructors:
        r"""Algebra constructors over a fixed base ring.

        These constructors name the free functors from specific source
        categories into the corresponding category of ``R``-algebra objects.
        Sage's generic ``S.algebra(R)`` compatibility method is not the public
        project API.
        """

        def __init__(self, category: RAlgebra) -> None:
            self._category = category

        @final
        def provenance(self) -> ConstructorRegistry:
            r"""Return typed provenance records for algebra constructors."""
            from category_specs.spec_core import constructor_registry_for_category

            return constructor_registry_for_category(
                self.category(),
                owner_category=f"Algebras({self.base_ring()})",
                id_prefix="algebras",
            )

        @final
        def category(self) -> RAlgebra:
            r"""Return the algebra category whose constructors this object names."""
            return self._category

        @final
        def base_ring(self) -> Ring:
            r"""Return the base ring of the constructed algebras."""
            return self.category().base_ring()

        @final
        def _refine_constructed_algebra(self, algebra: Algebra, category: Category) -> Algebra:
            return refine_category(algebra, category, test=False)

        @final
        def _sage_algebra_from_source(
            self,
            source: Magma | Semigroup | Monoid | Group | AdditiveSemigroup | AdditiveMonoid | AdditiveGroup,
            source_category: Category,
        ) -> Algebra:
            assert source in source_category, f"Expected source in {source_category}: {source}"
            algebra = source.algebra(self.base_ring(), category=source_category)
            return self._refine_constructed_algebra(algebra, self.category().WithBasis())

        @overload
        def FreeAlgebra(
            self,
            *,
            generators: Set,
            implementation: Literal["letterplace"] | None = None,
            degrees: Integer | Sequence[Integer] | None = None,
            sparse: bool | None = None,
            order: str | None = None,
        ) -> Algebra: ...

        @overload
        def FreeAlgebra(
            self,
            *,
            generator_names: Sequence[str],
            generator_count: Integer | None = None,
            implementation: Literal["letterplace"] | None = None,
            degrees: Integer | Sequence[Integer] | None = None,
            sparse: bool | None = None,
            order: str | None = None,
        ) -> Algebra: ...

        @overload
        def FreeAlgebra(
            self,
            *,
            generator_count: Integer,
            names: Sequence[str] | str,
            implementation: Literal["letterplace"] | None = None,
            degrees: Integer | Sequence[Integer] | None = None,
            sparse: bool | None = None,
            order: str | None = None,
        ) -> Algebra: ...

        @overload
        def FreeAlgebra(
            self,
            *,
            generator_count: Integer,
            name: str,
            implementation: Literal["letterplace"] | None = None,
            degrees: Integer | Sequence[Integer] | None = None,
            sparse: bool | None = None,
            order: str | None = None,
        ) -> Algebra: ...

        @final
        def FreeAlgebra(
            self,
            *,
            generators: Set | None = None,
            generator_names: Sequence[str] | None = None,
            generator_count: Integer | None = None,
            names: Sequence[str] | str | None = None,
            name: str | None = None,
            implementation: Literal["letterplace"] | None = None,
            degrees: Integer | Sequence[Integer] | None = None,
            sparse: bool | None = None,
            order: str | None = None,
        ) -> Algebra:
            r"""Return the free associative unital ``R``-algebra."""
            from sage.algebras.free_algebra import FreeAlgebra

            named_shapes = tuple(
                shape
                for shape, present in (
                    ("generators", generators is not None),
                    ("generator_names", generator_names is not None),
                    (
                        "generator_count plus names/name",
                        generator_count is not None and (names is not None or name is not None),
                    ),
                )
                if present
            )
            assert len(named_shapes) == 1, (
                f"FreeAlgebra requires exactly one source shape: generators, generator_names, or generator_count with names/name; received {named_shapes}"
            )
            assert not (names is not None and name is not None), "FreeAlgebra accepts names or name, not both"

            if generators is not None:
                assert generator_names is None and generator_count is None and names is None and name is None, (
                    "FreeAlgebra(generators=...) does not accept generator_names, generator_count, names, or name"
                )
                assert generators.is_finite(), "FreeAlgebra currently requires a finite generator set"
                generator_tuple: tuple[SetElement, ...] = tuple(generators)
                assert len(generator_tuple) == generators.cardinality(), f"finite generator set iteration must recover every generator of {generators}"
                generated_names = tuple(f"x{i}" for i, _ in enumerate(generator_tuple))
                algebra = FreeAlgebra(
                    self.base_ring(),
                    len(generator_tuple),
                    generated_names,
                    implementation=implementation,
                    degrees=degrees,
                    sparse=sparse,
                    order=order,
                )
                algebra._category_specs_generator_set = generators
                algebra._category_specs_generator_presentation = tuple(zip(generator_tuple, algebra.gens(), strict=True))
                return self._refine_constructed_algebra(algebra, self.category().WithBasis())

            if generator_names is not None:
                assert generators is None and names is None and name is None, "FreeAlgebra(generator_names=...) does not accept generators, names, or name"
                assert not isinstance(generator_names, str), "generator_names must be a finite sequence of complete names, not one combined name string"
                generator_name_tuple = tuple(generator_names)
                if generator_count is not None:
                    assert int(generator_count) == len(generator_name_tuple), "generator_count must equal the number of generator_names"
                    algebra = FreeAlgebra(
                        self.base_ring(),
                        generator_name_tuple,
                        int(generator_count),
                        implementation=implementation,
                        degrees=degrees,
                        sparse=sparse,
                        order=order,
                    )
                else:
                    algebra = FreeAlgebra(
                        self.base_ring(),
                        names=generator_name_tuple,
                        implementation=implementation,
                        degrees=degrees,
                        sparse=sparse,
                        order=order,
                    )
                return self._refine_constructed_algebra(algebra, self.category().WithBasis())

            assert generator_count is not None
            if names is not None:
                algebra = FreeAlgebra(
                    self.base_ring(),
                    int(generator_count),
                    names,
                    implementation=implementation,
                    degrees=degrees,
                    sparse=sparse,
                    order=order,
                )
            else:
                assert name is not None
                algebra = FreeAlgebra(
                    self.base_ring(),
                    int(generator_count),
                    name,
                    implementation=implementation,
                    degrees=degrees,
                    sparse=sparse,
                    order=order,
                )
            return self._refine_constructed_algebra(algebra, self.category().WithBasis())

        @final
        def GroupAlgebra(self, *, group: Group) -> Algebra:
            r"""Return the group algebra over ``R``."""
            from sage.categories.groups import Groups

            return self._sage_algebra_from_source(group, Groups())

        @overload
        def algebra(self, *, monoid: Monoid) -> Algebra: ...

        @overload
        def algebra(self, *, additive_monoid: AdditiveMonoid) -> Algebra: ...

        @overload
        def algebra(self, *, additive_group: AdditiveGroup) -> Algebra: ...

        @final
        def algebra(
            self,
            *,
            monoid: Monoid | None = None,
            additive_monoid: AdditiveMonoid | None = None,
            additive_group: AdditiveGroup | None = None,
        ) -> Algebra:
            r"""Return the algebra induced by the named source structure."""
            named_sources = tuple(source for source in (monoid, additive_monoid, additive_group) if source is not None)
            assert len(named_sources) == 1, "algebra requires exactly one named source: monoid, additive_monoid, or additive_group"
            if monoid is not None:
                from sage.categories.monoids import Monoids

                return self._sage_algebra_from_source(monoid, Monoids())
            if additive_monoid is not None:
                from sage.categories.additive_monoids import AdditiveMonoids

                return self._sage_algebra_from_source(additive_monoid, AdditiveMonoids())
            from sage.categories.additive_groups import AdditiveGroups

            assert additive_group is not None
            return self._sage_algebra_from_source(additive_group, AdditiveGroups())

    @final
    def Constructors(self) -> Algebras._Constructors:
        r"""Return the named algebra constructor collector over this base ring."""
        return self.__class__._Constructors(self)

    Commutative = LazyImport("category_specs.algebras.subcategories.commutative", "_CommutativeAlgebras")
    WithBasis = LazyImport("category_specs.algebras.subcategories.with_basis", "_AlgebrasWithBasis")
    FiniteDimensional = LazyImport(
        "category_specs.algebras.subcategories.finite_dimensional",
        "_FiniteDimensionalAlgebras",
    )
    Semisimple = LazyImport("category_specs.algebras.subcategories.semisimple", "_SemisimpleAlgebras")

    Subobjects : TypeAlias = _Subobjects
    Quotients : TypeAlias = _Quotients
    Subquotients : TypeAlias = _Subquotients
    ObjectsOver : TypeAlias = _ObjectsOver
    ObjectsUnder : TypeAlias = _ObjectsUnder
    Ideals : TypeAlias = AlgebraIdealsCategory
    CartesianProducts : TypeAlias = _CartesianProducts
    TensorProducts : TypeAlias = _TensorProducts
    DualObjects : TypeAlias = _DualObjects


AlgebrasCategory : TypeAlias = Algebras
AlgebrasObject : TypeAlias = Algebras.ParentMethods
AlgebrasElement : TypeAlias = Algebras.ElementMethods
AlgebrasMorphism : TypeAlias = AlgebraHomCategory.ElementMethods
AlgebrasHomCategory : TypeAlias = AlgebraHomCategory
AlgebrasEndCategory : TypeAlias = AlgebraEndCategory
AlgebrasAutCategory : TypeAlias = AlgebraAutCategory
AlgebrasHom : TypeAlias = AlgebraHomCategory.ParentMethods
AlgebrasEnd : TypeAlias = AlgebraEndCategory.ParentMethods
AlgebrasAut : TypeAlias = AlgebraAutCategory.ParentMethods
AlgebrasEndomorphism : TypeAlias = AlgebraEndCategory.ElementMethods
AlgebrasAutomorphism : TypeAlias = AlgebraAutCategory.ElementMethods

MagmaticAlgebrasCategory : TypeAlias = MagmaticAlgebras
MagmaticAlgebrasObject : TypeAlias = MagmaticAlgebras.ParentMethods
MagmaticAlgebrasElement : TypeAlias = MagmaticAlgebras.ElementMethods
MagmaticAlgebrasMorphism : TypeAlias = AlgebraHomCategory.ElementMethods
AssociativeAlgebrasCategory : TypeAlias = AssociativeAlgebras
AssociativeAlgebrasObject : TypeAlias = AssociativeAlgebras.ParentMethods
AssociativeAlgebrasElement : TypeAlias = AssociativeAlgebras.ElementMethods
AssociativeAlgebrasMorphism : TypeAlias = AlgebraHomCategory.ElementMethods
