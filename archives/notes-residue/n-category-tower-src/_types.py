# Origin: gitclones/integral_lattice/cat/src/_types.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Centralized type definitions for the abc module.

All type aliases, protocols, and TypeGuard predicates are defined here
to avoid circular imports. Other modules import from this file.

Organization:
    1. Imports
    2. Type Namespace Classes (SageType, SympyType, PythonType)
    3. Protocols for structural typing
    4. Type Guards
    5. Forward Reference Type Aliases (categorical types)
    6. Data Classes (BoolProof, cells)
    7. Morphism Data Protocol
"""

# pyright: basic

from __future__ import annotations

from src.local_typing import *
from src._sage_types import SageType, SageTypeChecks

# =============================================================================
# Type Namespace Classes
# =============================================================================




class SympyType:
    """Namespace for SymPy type aliases."""

    from sympy import Basic as SymbolicExpression  # type: ignore[external-library]
    from sympy.sets import FiniteSet  # type: ignore[external-library]
    from sympy.sets import Set  # type: ignore[external-library]

class PythonType:
    """Namespace for Python built-in type aliases."""

    Set = set[Any]

# =============================================================================
# Protocols for Structural Typing
# =============================================================================





# =============================================================================
# Type Guards — Organized by namespace
# =============================================================================






class SympyTypeChecks:
    """Type guards for SymPy types."""

    @staticmethod
    def is_symbolic_expression(x: Any) -> TypeIs[SympyType.SymbolicExpression]:
        """Check if x is a SymPy symbolic expression."""
        return isinstance(x, SympyType.SymbolicExpression)

# =============================================================================
# Forward Reference Type Aliases (Categorical Types)
# =============================================================================

class CategoryABCs:
    """
    Namespace for actual ABC class references.

    Use these for type hints and isinstance checks.
    These should ONLY be inherited within the src.abc submodule to define other ABCs.
    For concrete implementations, inherit from CategoryBases

    """

    # =============================================================================
    # Functors (1-cells in Cat_w = 0-cells in Fun(C,D))
    # =============================================================================
    
    from src.abc_specs.w_categories.hom_categories.fun_categories.hom_cat_w_xy import (
        Functor,
        EndoFunctor,
        AutoFunctor,
        NaturalTransformation,
        EndoNaturalTransformation,
        AutoNaturalTransformation,
        Modification,
        EndoModification,
        AutoModification,
    )
    from src.abc_specs.w_categories.cat_w import Cat_w
    from src.abc_specs.cells import CellContainer, Cell

    from src.abc_specs.w_categories.two_category_interface.minimal_two_category import Category 
    from src.abc_specs.w_categories.two_category_interface.nontrivial_two_category import Nontrivial_TwoCategory, Element, Object
    from src.abc_specs.w_categories.hom_categories.hom_c_xy import (
        OneMorphism,
        PlainOneMorphism,
        EndoOneMorphism,
        AutoOneMorphism,
        TwoMorphism,
        PlainTwoMorphism,
        EndoTwoMorphism,
        AutoTwoMorphism,
    )

    # =============================================================================
    # Concrete Categories
    # =============================================================================
    from src.abc_specs.w_categories.empty_category import (
        _EmptyCategory_ABC as EmptyCategory,
    )
    from src.abc_specs.w_categories.one_categories.sets import _SetCategory_ABC as SetCategory
    from src.abc_specs.w_categories.one_categories.sets import _SetObject_ABC as SetObject
    from src.abc_specs.w_categories.terminal_category import (
        _TerminalCategory_ABC as TerminalCategory,
    )
    from src.abc_specs.w_categories.cat_w import _Cat_W_ABC as Cat_w

    # Groups
    from src.abc_specs.w_categories.one_categories.groups import (
        _GroupsCategory_ABC as GroupsCategory,
    )
    from src.abc_specs.w_categories.one_categories.groups import (
        _GroupObject_ABC as GroupObject,
    )
    from src.abc_specs.w_categories.one_categories.groups import (
        _GroupElement_ABC as GroupElement,
    )

    # Rings
    from src.abc_specs.w_categories.one_categories.rings import (
        _RingsCategory_ABC as RingsCategory,
    )
    from src.abc_specs.w_categories.one_categories.rings import (
        _RingObject_ABC as RingObject,
    )
    from src.abc_specs.w_categories.one_categories.rings import (
        _RingElement_ABC as RingElement,
    )

    # Ideals (submodules of R as R-module)
    from src.abc_specs.w_categories.one_categories.ideals import (
        _IdealsCategory_ABC as IdealsCategory,
    )
    from src.abc_specs.w_categories.one_categories.ideals import _Ideal_ABC as Ideal

    # Commutative Rings
    from src.abc_specs.w_categories.one_categories.commutative_rings import (
        _CommutativeRingsCategory_ABC as CommutativeRingsCategory,
    )
    from src.abc_specs.w_categories.one_categories.commutative_rings import (
        _CommutativeRingObject_ABC as CommutativeRingObject,
    )
    from src.abc_specs.w_categories.one_categories.commutative_rings import (
        _CommutativeRingElement_ABC as CommutativeRingElement,
    )

    # R-Modules
    from src.abc_specs.w_categories.one_categories.mod_R import _RMod_ABC as RMod
    from src.abc_specs.w_categories.one_categories.mod_R import (
        _ModuleObject_ABC as ModuleObject,
    )
    from src.abc_specs.w_categories.one_categories.mod_R import (
        _ModuleElement_ABC as ModuleElement,
    )

    # =============================================================================
    # Hom Categories
    # =============================================================================
    from src.abc_specs.w_categories.hom_categories.aut_c import _AutC_ABC as AutC
    from src.abc_specs.w_categories.hom_categories.aut_c_x import _AutC_x_ABC as AutC_x
    from src.abc_specs.w_categories.hom_categories.end_c import _EndC_ABC as EndC
    from src.abc_specs.w_categories.hom_categories.end_c_x import _EndC_x_ABC as EndC_x
    from src.abc_specs.w_categories.hom_categories.hom_c import _HomC_ABC as HomC
    from src.abc_specs.w_categories.hom_categories.hom_c_xy import _HomC_xy_ABC as HomC_xy

    # =============================================================================
    # Functor Categories (Hom/End/Aut over Cat_w)
    # =============================================================================
    from src.abc_specs.w_categories.hom_categories.fun_categories.hom_cat_w import (
        _Fun_ABC as Fun
    )
    from src.abc_specs.w_categories.hom_categories.fun_categories.hom_cat_w_xy import (
        _Fun_xy_ABC as Fun_xy
    )
    from src.abc_specs.w_categories.hom_categories.fun_categories.end_cat_w import (
        _EndoFun_ABC as EndoFun
    )
    from src.abc_specs.w_categories.hom_categories.fun_categories.end_cat_w_x import (
        _EndoFun_x_ABC as EndoFun_x
    )
    from src.abc_specs.w_categories.hom_categories.fun_categories.aut_cat_w import (
        _AutoFun_ABC as AutoFun
    )
    from src.abc_specs.w_categories.hom_categories.fun_categories.aut_cat_w_x import (
        _AutFun_x_ABC as AutFun_x
    )

    # =============================================================================
    # Limits and Colimits
    # =============================================================================
    from src.abc_specs.structures import _CoproductCategory_ABC as Coproduct
    from src.abc_specs.structures import _CosliceCategory_ABC as Coslice
    from src.abc_specs.structures import _CospanCategory_ABC as Cospan
    from src.abc_specs.structures import _DirectSumCategory_ABC as DirectSum
    from src.abc_specs.structures import _InitialCategory_ABC as Initial
    from src.abc_specs.structures import _ProductCategory_ABC as Product
    from src.abc_specs.structures import _PullbackCategory_ABC as Pullback
    from src.abc_specs.structures import _PushoutCategory_ABC as Pushout
    from src.abc_specs.structures import _SliceCategory_ABC as Slice
    from src.abc_specs.structures import _SpanObject_ABC as Span
    from src.abc_specs.structures import _TensorProductCategory_ABC as TensorProduct
    from src.abc_specs.structures import _TerminalCategory_ABC as Terminal
    from src.abc_specs.structures import _ZeroCategory_ABC as Zero

    # Aliases
    Subobject = Slice  # X ≤ Y is a subobject iff ∃ι_X: X -> Y in C.
    Superobject = Coslice  # Y ≥ X is a superobject iff ∃ι_X: X -> Y in C.

    # Point: a morphism from a terminal object to some object
    Point = OneMorphism


# Data Classes
# =============================================================================

@dataclass
class BoolProof:
    """
    Result of an equality/equivalence check.

    Mutable accumulator that tracks:
    - kind: The proof result (TRUE, FALSE, NO_PROOF, PROBABILITY_PROOF)
    - witness_strategy: For conclusive results, the method that succeeded
    - attempted_strategies: List of strategies tried (accumulated via +=)
    - counterexample: For FALSE, witnessing data
    - probability, sample_size: For PROBABILITY_PROOF

    Usage:
        proof = BoolProof()
        proof += check_strategy_1(...)
        if proof.has_proof():
            return proof
        proof += check_strategy_2(...)
        ...
    """

    class BoolProofKind(Enum):
        """Enum for the kind of proof result."""

        TRUE = auto()
        FALSE = auto()
        NO_PROOF = auto()
        PROBABILITY_PROOF = auto()

    kind: BoolProofKind = BoolProofKind.NO_PROOF
    witness_strategy: str = ""
    attempted_strategies: list[str] = field(default_factory=list)
    counterexample: Any | None = None
    probability: float | None = None
    sample_size: int | None = None

    # Convenience constructors
    @classmethod
    def true(cls, witness_strategy: str) -> BoolProof:
        return cls(kind=cls.BoolProofKind.TRUE, witness_strategy=witness_strategy)

    @classmethod
    def false(cls, witness_strategy: str, counterexample: Any | None = None) -> BoolProof:
        return cls(
            kind=cls.BoolProofKind.FALSE,
            witness_strategy=witness_strategy,
            counterexample=counterexample,
        )

    @classmethod
    def no_proof(cls, strategy_name: str) -> BoolProof:
        """Create a NO_PROOF result with a single attempted strategy."""
        return cls(kind=cls.BoolProofKind.NO_PROOF, attempted_strategies=[strategy_name])

    @classmethod
    def probability_proof(
        cls, witness_strategy: str, probability: float, sample_size: int
    ) -> BoolProof:
        return cls(
            kind=cls.BoolProofKind.PROBABILITY_PROOF,
            witness_strategy=witness_strategy,
            probability=probability,
            sample_size=sample_size,
        )

    def __iadd__(self, other: BoolProof) -> BoolProof:
        """
        Accumulate proof attempts.

        If self already has a proof, ignore other.
        If other has a proof, adopt it.
        Otherwise, merge attempted_strategies.
        """
        if self.has_proof():
            return self

        if other.has_proof():
            self.kind = other.kind
            self.witness_strategy = other.witness_strategy
            self.counterexample = other.counterexample
            self.probability = other.probability
            self.sample_size = other.sample_size
            return self

        # Both have no proof - merge attempted strategies
        self.attempted_strategies.extend(other.attempted_strategies)
        return self

    def has_proof(self) -> bool:
        """Returns True if a conclusive result was found."""
        return self.kind in (
            self.BoolProofKind.TRUE,
            self.BoolProofKind.FALSE,
            self.BoolProofKind.PROBABILITY_PROOF,
        )

    def __bool__(self) -> bool:
        """
        Allow use in boolean context.

        - TRUE -> True
        - FALSE -> False
        - Otherwise raise to prevent silent truthiness
        """
        if self.is_true():
            return True
        if self.is_false():
            return False
        raise ValueError("BoolProof has no definitive truth value")

    def is_true(self) -> bool:
        return self.kind == self.BoolProofKind.TRUE

    def is_false(self) -> bool:
        return self.kind == self.BoolProofKind.FALSE

    def is_no_proof(self) -> bool:
        return self.kind == self.BoolProofKind.NO_PROOF

    def is_probability_proof(self) -> bool:
        return self.kind == self.BoolProofKind.PROBABILITY_PROOF

    def __and__(self, other: BoolProof) -> BoolProof:
        """
        Logical AND for BoolProof.

        Truth table (rows = self, cols = other):
                    TRUE        FALSE       NO_PROOF    PROB
        TRUE        TRUE        FALSE       NO_PROOF    PROB
        FALSE       FALSE       FALSE       FALSE       FALSE
        NO_PROOF    NO_PROOF    FALSE       NO_PROOF    NO_PROOF
        PROB        PROB        FALSE       NO_PROOF    PROB(min)
        """
        # FALSE dominates everything except when both are conclusive
        if self.is_false():
            return self
        if other.is_false():
            return other

        # Both TRUE -> TRUE
        if self.is_true() and other.is_true():
            return BoolProof.true(f"({self.witness_strategy}) AND ({other.witness_strategy})")

        # TRUE and something else -> that something else
        if self.is_true():
            return other
        if other.is_true():
            return self

        # Both NO_PROOF -> NO_PROOF
        if self.is_no_proof() and other.is_no_proof():
            return BoolProof.no_proof(f"({', '.join(self.attempted_strategies)}) AND ({', '.join(other.attempted_strategies)})")

        # PROB and PROB -> PROB with min probability
        if self.is_probability_proof() and other.is_probability_proof():
            min_prob = min(self.probability or 0, other.probability or 0)
            total_samples = (self.sample_size or 0) + (other.sample_size or 0)
            return BoolProof.probability_proof(
                f"({self.witness_strategy}) AND ({other.witness_strategy})",
                min_prob,
                total_samples
            )

        # PROB and NO_PROOF -> NO_PROOF (inconclusive)
        if self.is_probability_proof() and other.is_no_proof():
            return other
        if self.is_no_proof() and other.is_probability_proof():
            return self

        # TRUE and NO_PROOF -> NO_PROOF
        # TRUE and PROB -> PROB
        # (already handled above)

        return BoolProof.no_proof("AND: inconclusive")

    def __or__(self, other: BoolProof) -> BoolProof:
        """
        Logical OR for BoolProof.

        Truth table (rows = self, cols = other):
                    TRUE        FALSE       NO_PROOF    PROB
        TRUE        TRUE        TRUE        TRUE        TRUE
        FALSE       TRUE        FALSE       NO_PROOF    PROB
        NO_PROOF    TRUE        NO_PROOF    NO_PROOF    NO_PROOF
        PROB        TRUE        PROB        NO_PROOF    PROB(max)
        """
        # TRUE dominates everything
        if self.is_true():
            return self
        if other.is_true():
            return other

        # Both FALSE -> FALSE
        if self.is_false() and other.is_false():
            return BoolProof.false(f"({self.witness_strategy}) OR ({other.witness_strategy})")

        # FALSE and something else -> that something else
        if self.is_false():
            return other
        if other.is_false():
            return self

        # Both NO_PROOF -> NO_PROOF
        if self.is_no_proof() and other.is_no_proof():
            return BoolProof.no_proof(f"({', '.join(self.attempted_strategies)}) OR ({', '.join(other.attempted_strategies)})")

        # PROB and PROB -> PROB with max probability
        if self.is_probability_proof() and other.is_probability_proof():
            max_prob = max(self.probability or 0, other.probability or 0)
            total_samples = (self.sample_size or 0) + (other.sample_size or 0)
            return BoolProof.probability_proof(
                f"({self.witness_strategy}) OR ({other.witness_strategy})",
                max_prob,
                total_samples
            )

        # PROB and NO_PROOF -> NO_PROOF (inconclusive)
        if self.is_probability_proof() and other.is_no_proof():
            return other
        if self.is_no_proof() and other.is_probability_proof():
            return self

        return BoolProof.no_proof("OR: inconclusive")

# =============================================================================
# Morphism Data Protocol
# =============================================================================

@runtime_checkable
class MorphismData(Protocol):
    """
    Data sufficient to construct a morphism.

    Includes domain, codomain, and one of:
    - callable: f(x) -> y
    - dict: {x: y, ...}
    - relation: {(x, y), ...}
    - list/tuple: [f(x_0), f(x_1), ...]
    - permutation
    - matrix
    """

    type MapData = (
        Callable[[Any], Any]
        | Mapping[Any, Any]
        | Sequence[Any]
        | set[tuple[Any, Any]]
        | SageType.Matrix
        | SageType.Permutation
    )

    @property
    def domain(self) -> Any: ...

    @property
    def codomain(self) -> Any: ...

    @property
    def map_data(self) -> MapData: ...

# =============================================================================
# Category Type Guards
# =============================================================================

class CategoryTypeChecks:
    """Type guards for categorical structures."""

    # --- Cell type checks ---

    @staticmethod
    def is_cell(x: Any) -> TypeIs[CategoryABCs.Cell]:
        """Check if x is a cell."""
        return isinstance(x, CategoryABCs.Cell)

    # --- Category/Functor checks ---

    @staticmethod
    def is_functor(F: Any) -> TypeGuard[CategoryABCs.Functor]:
        """Check if F is a functor."""
        return isinstance(F, CategoryABCs.Functor)

    @staticmethod
    def is_category(C: Any) -> TypeGuard[CategoryABCs.Nontrivial_TwoCategory]:
        """Check if C is a category."""
        return isinstance(C, CategoryABCs.Nontrivial_TwoCategory)

    @staticmethod
    def is_object(C: Any) -> TypeGuard[CategoryABCs.Object]:
        """Check if C is an object."""
        return isinstance(C, CategoryABCs.Object)

    @staticmethod
    def is_morphism(f: Any) -> TypeGuard[CategoryABCs.OneMorphism]:
        """Check if f is a morphism."""
        return isinstance(f, CategoryABCs.OneMorphism)

    @staticmethod
    def is_HomC_category(C: Any) -> TypeGuard[CategoryABCs.HomC]:
        """Check if C is a HomC category."""
        return isinstance(C, CategoryABCs.HomC)

    @staticmethod
    def is_HomC_xy_category(C: Any) -> TypeGuard[CategoryABCs.HomC_xy]:
        """Check if C is a HomC(X, Y) category."""
        return isinstance(C, CategoryABCs.HomC_xy)

    @staticmethod
    def is_endomorphism(f: Any) -> TypeGuard[CategoryABCs.EndoOneMorphism]:
        """Narrow Morphism to Endomorphism when domain == codomain."""
        if not CategoryTypeChecks.is_morphism(f):
            return False
        return f.as_arrow().domain().is_equal_to(f.as_arrow().codomain()).is_true()

    @staticmethod
    def is_EndC_category(C: Any) -> TypeGuard[CategoryABCs.EndC]:
        """Check if C is an EndC category."""
        return isinstance(C, CategoryABCs.EndC)

    @staticmethod
    def is_EndC_x_category(C: Any) -> TypeGuard[CategoryABCs.EndC_x]:
        """Check if C is an EndC(X) category."""
        return isinstance(C, CategoryABCs.EndC_x)

    @staticmethod
    def is_automorphism(f: Any) -> TypeGuard[CategoryABCs.AutoOneMorphism]:
        """Narrow Endomorphism to Automorphism when invertible."""
        if not CategoryTypeChecks.is_endomorphism(f):
            return False
        return f.as_arrow().is_invertible().has_proof()

    @staticmethod
    def is_AutC_category(C: Any) -> TypeGuard[CategoryABCs.AutC]:
        """Check if C is an AutC category."""
        return isinstance(C, CategoryABCs.AutC)

    @staticmethod
    def is_AutC_x_category(C: Any) -> TypeGuard[CategoryABCs.AutC_x]:
        """Check if C is an AutC(X) category."""
        return isinstance(C, CategoryABCs.AutC_x)

    @staticmethod
    def is_identity(f: Any) -> bool:
        """Check if f is the identity morphism."""
        if not CategoryTypeChecks.is_morphism(f):
            return False
        if not CategoryTypeChecks.is_endomorphism(f):
            return False
        return f.as_arrow().is_identity().has_proof()

    # --- Point morphisms (domain is terminal) ---

    @staticmethod
    def is_point(f: Any) -> TypeGuard[CategoryABCs.Object]:
        """Check if f is a point (morphism from a terminal object)."""
        if not CategoryTypeChecks.is_morphism(f):
            return False
        if not CategoryTypeChecks.is_terminal(f.as_arrow().domain()):
            return False
        return CategoryTypeChecks.is_endomorphism(f)

    # --- Object structural checks ---

    @staticmethod
    def is_terminal(x: Any) -> TypeGuard[CategoryABCs.Terminal]:
        """Check if x is a terminal object."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return x.is_terminal().is_true()

    @staticmethod
    def is_initial(x: Any) -> TypeIs[CategoryABCs.Initial]:
        """Check if x is an initial object."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return x.is_initial().is_true()

    @staticmethod
    def is_zero(x: Any) -> TypeGuard[CategoryABCs.Zero]:
        """Check if x is a zero object (both terminal and initial)."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return x.is_zero().is_true()

    # --- Limit/colimit structure checks ---

    @staticmethod
    def is_product(x: Any) -> TypeGuard[CategoryABCs.Product]:
        """Check if x has product structure."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.Product)

    @staticmethod
    def is_coproduct(x: Any) -> TypeGuard[CategoryABCs.Coproduct]:
        """Check if x has coproduct structure."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.Coproduct)

    @staticmethod
    def is_pullback(x: Any) -> TypeGuard[CategoryABCs.Pullback]:
        """Check if x has pullback structure."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.Pullback)

    @staticmethod
    def is_pushout(x: Any) -> TypeGuard[CategoryABCs.Pushout]:
        """Check if x has pushout structure."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.Pushout)

    @staticmethod
    def is_direct_sum(x: Any) -> TypeGuard[CategoryABCs.DirectSum]:
        """Check if x has direct sum structure (biproduct)."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.DirectSum)

    @staticmethod
    def is_tensor_product(x: Any) -> TypeGuard[CategoryABCs.TensorProduct]:
        """Check if x has tensor product structure."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.TensorProduct)

    # --- Slice/coslice checks ---

    @staticmethod
    def is_slice(x: Any) -> TypeGuard[CategoryABCs.Slice]:
        """Check if x has slice structure (subobject)."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.Slice)

    @staticmethod
    def is_coslice(x: Any) -> TypeGuard[CategoryABCs.Coslice]:
        """Check if x has coslice structure (superobject)."""
        if not CategoryTypeChecks.is_object(x):
            return False
        return isinstance(x, CategoryABCs.Coslice)

    # Checking category containment

    @staticmethod
    def is_set_object(x: Any) -> TypeGuard[CategoryABCs.SetObject]:
        return isinstance(x, CategoryABCs.SetObject)



# class CategoryBases:
#     """
#     These are the types that should ACTUALLY be inherited by concrete implementations.
#     These should include any "bases" that have partial implementations, along with any operator mixins.
#     """

#     from src.abc.bases.cat_w import _CatW_Base as Category
#     from src.abc.bases.cells import Cell, CellContainer, EmptyCell, OneCell, TwoCell, ZeroCell
#     from src.abc.bases.concrete_categories.sets import _SetObject_Base as SetObject
#     from src.abc.bases.hom.functors import (
#         Autofunctor_Base as AutoFunctor,
#     )
#     from src.abc.bases.hom.functors import (
#         AutoNaturalTransformation_Base as EndoNaturalTransformation,
#     )
#     from src.abc.bases.hom.functors import (
#         EndoNaturalTransformation_Base as AutoNaturalTransformation,
#     )
#     from src.abc.bases.hom.functors import (
#         NaturalTransformation_Base as NaturalTransformation,
#     )
#     from src.abc.bases.hom.functors import (
#         _Endofunctor_Base as EndoFunctor,
#     )
#     from src.abc.bases.hom.functors import (
#         _Functor_Base as Functor,
#     )
#     from src.abc.bases.hom.hom_categories import (
#         _AutC_Base as AutC,
#     )
#     from src.abc.bases.hom.hom_categories import (
#         _AutC_x_Base as AutC_x,
#     )
#     from src.abc.bases.hom.hom_categories import (
#         _EndC_Base as EndC,
#     )
#     from src.abc.bases.hom.hom_categories import (
#         _EndC_x_Base as EndC_x,
#     )
#     from src.abc.bases.hom.hom_categories import (
#         _HomC_Base as HomC,
#     )
#     from src.abc.bases.hom.hom_categories import (
#         _HomC_xy_Base as HomC_xy,
#     )
#     from src.abc.bases.hom.morphisms import Automorphism_Base as Automorphism
#     from src.abc.bases.hom.morphisms import Endomorphism_Base as Endomorphism
#     from src.abc.bases.hom.morphisms import Morphism_Base as Morphism
#     from src.abc.bases.hom.morphisms import (
#         _Morphism_Category_Cell_Container_Base as Morphism_Cell_Container,
#     )
#     from src.abc.bases.structures import (
#         Coslice_Base as Coslice,
#     )
#     from src.abc.bases.structures import (
#         _CoproductCategory_Base as Coproduct,
#     )
#     from src.abc.bases.structures import (
#         _Cospan_Base as Cospan,
#     )
#     from src.abc.bases.structures import (
#         _DirectSumCategory_Base as DirectSum,
#     )
#     from src.abc.bases.structures import (
#         _InitialCategory_Base as Initial,
#     )
#     from src.abc.bases.structures import (
#         _ProductCategory_Base as Product,
#     )
#     from src.abc.bases.structures import (
#         _PullbackCategory_Base as Pullback,
#     )
#     from src.abc.bases.structures import (
#         _PushoutCategory_Base as Pushout,
#     )
#     from src.abc.bases.structures import (
#         _Slice_Base as Slice,
#     )
#     from src.abc.bases.structures import (
#         _Span_Base as Span,
#     )
#     from src.abc.bases.structures import (
#         _TensorProductCategory_Base as TensorProduct,
#     )
#     from src.abc.bases.structures import (
#         _TerminalCategory_Base as Terminal,
#     )
#     from src.abc.bases.structures import (
#         _ZeroCategory_Base as Zero,
#     )

#     AnyHomCategory = HomC | EndC | AutC
#     AnyHomspace = HomC_xy | EndC_x | AutC_x
#     AnyMorphism = Morphism | Endomorphism | Automorphism

#     # Aliases
#     Subobject = Slice  # X ≤ Y is a subobject iff ∃ι_X: X -> Y in C.
#     Superobject = Coslice  # Y ≥ X is a superobject iff ∃ι_X: X -> Y in C.


#     # Point: a morphism from a terminal object to some object
#     Object = ZeroCell
#     Element = Object
#     Point = Morphism

#     from src.abc.bases.concrete_categories.empty_category import (
#         _Empty_Category_Base as EmptyCategory,
#     )


# =============================================================================
class Categories:

    @staticmethod
    def FromOneCells(cells: list[CategoryABCs.OneMorphism]) -> CategoryABCs.OneMorphism: ...


    class Types:
        from src.abc_specs.w_categories.cat_w import _Cat_W_ABC as Cat_w
        from src.abc_specs.w_categories.empty_category import _EmptyCategory_ABC as EmptyCategory

        # from src.abc_specs.w_categories.hom_categories.fun_categories.hom_cat_w import _Fun_ABC as Fun
        # from src.abc_specs.w_categories.hom_categories.fun_categories.end_cat_w import _EndoFun_ABC as EndoFun
        # from src.abc_specs.w_categories.hom_categories.fun_categories.aut_cat_w import _AutoFun_ABC as AutoFun
        # from src.abc.concrete.empty_category.category import EmptyCategory
        # from src.abc.concrete.terminal_category.category import TerminalCategory
        #from src.abc.concrete.sets.category import SetCategory as Set
        # from src.abc.concrete.groups.category import GroupsCategory as Groups
        # from src.abc.concrete.rings.category import RingsCategory as Rings
        # from src.abc.concrete.crings.category import CRingsCategory as CRings
        # from src.abc.concrete.fields.category import FieldsCategory as Fields
        # from src.abc.concrete.modules.category import Mod_R_Category as Mod_R
        # from src.abc.concrete.modules.category import Mod_Z_Category as Mod_Z
        Set = EmptyCategory
        Groups = EmptyCategory
        Rings = EmptyCategory
        CRings = EmptyCategory
        Fields = EmptyCategory
        Mod_R = EmptyCategory
        Mod_Z = EmptyCategory
        Pure_Element = EmptyCategory

    Cat = Types.Cat() # type: ignore[until-implemented]
    Fun = Types.Fun() # type: ignore[until-implemented]
    EmptyCategory = Types.EmptyCategory() # type: ignore[until-implemented]
    TerminalCategory = Types.TerminalCategory() # type: ignore[until-implemented]

    InitialCategory = EmptyCategory
    Set = Types.Set
    Groups = Types.Groups
    Rings = Types.Rings
    CRings = Types.CRings
    Fields = Types.Fields
    Mod_R = Types.Mod_R
    Mod_Z = Types.Mod_Z

    Functor = Cat.morphism_class()
    NaturalTransformation = Fun.morphism_class()
