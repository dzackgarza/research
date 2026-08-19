# Origin: gitclones/integral_lattice/cat/src/abc_specs/new_w_categories/old_interfaces/___cells.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Abstract Base Classes for n-cells in higher categories.

An n-cell is the fundamental building block of an n-category:
- A (-1)-cell is the unique "empty cell" ∅, representing the absence of structure.
- A 0-cell is an object in a category.
- A 1-cell is a morphism f: x → y between 0-cells.
- A 2-cell is a natural transformation α: f ⇒ g between 1-cells with matching source/target.
- An n-cell (for n ≥ 1) is a morphism between (n-1)-cells with matching boundaries.

Each n-cell has:
- A source and target, which are (n-1)-cells.
- A path representation as a sequence of (n-1)-cells.
- An underlying category that contextualizes the cell.
"""

from src._types import BoolProof, CategoryABCs
from src.local_typing import *

from .__arrows import Arrow

# =============================================================================
# Base Cell ABC
# =============================================================================

class _All_Cells_ABC(ABC):
    """
    Abstract base class for all cells in a category.

    A 0-cell is a functor * := [0] -> C.
    A primitive 1-cell is a functor I_1 := {0 -> 1} -> C, and a general 1-cell
    is a functor I_n := {0 -> 1 -> .... -> n-1} -> C for some n.
    A primitive 2-cell is a functor I_1^2 := {
    0 -> 1
       |
       v
       η₁
       ^
       |
    0 <- 1
    } -> C, 
    and a general 2-cell is a functor I_n^2 := {
    0 -> 1 -> ... -> n-1
       |    |    |    |
       v    v    v    v
       η₁   η₂   η₃   η₄
       ^    ^    ^    ^
       |    |    |    |
    0 <- 1 <- ... <- n-1
    } -> C for some n.

    (I.e., I_1^2 is two objects 0,1, two morphisms f: 0 -> 1, g: 1 -> 0, and an invertible 2-morphism η: f => g)
    
    An n-cell is thus represented as a sequence of (n-1)-cells,
    f = {x_1 -> x_2 -> ... -> x_n} = [x_1, ..., x_n],

    There is a unique (-1)-cell ∅.
    A 0-cell is said to have domain = codomain = ∅, and is this regarded 
    as a "named path" x = {∅ -> ∅} = [∅, ∅].
    A 1-cell is represented by a named path f = {x_1 -> ... -> x_n} as above, where 
    domain = x_1 and codomain = x_n.
    An n-cell is a named path η = {f_1 -> ... -> f_n} as above, where 
    domain = f_1 and codomain = f_n.
    """

    @abstractmethod
    def __str__(self) -> str: ...
    
    @abstractmethod
    def __repr__(self) -> str: ...
    
    @abstractmethod
    def __hash__(self) -> int: 
        """
        A "set of cells" must make sense.
        """
        ...
    
    @abstractmethod
    def __eq__(self, other: Any) -> bool: 
        """
        This can implement equality (using the hash) or equivalence by higher cells.
        """
        ...

    @abstractmethod
    def container(self) -> _Cell_Container_ABC:
        """
        All cells should be stored in a container that constructs them, and 
        not constructed independently.
        """
        ...

    @abstractmethod
    def associated_arrows(self) -> Sequence[Arrow.n]:
        ...
    
    @abstractmethod
    def cell_name(self) -> str: ...

    @abstractmethod
    def cell_dimension(self) -> int: ...

    @abstractmethod
    def source(self) -> Cell.n:
        """
        The source of this cell.
        """
        ...

    @abstractmethod
    def target(self) -> Cell.n:
        """
        The target of this cell.
        """
        ...

    @abstractmethod
    def path(self) -> Sequence[Cell.n]:
        """
        Return the path representation as a sequence of (n-1)-cells.

        A primitive cell {x → y} has path [x, y].
        A composed cell {x -> y} ∘ {y -> z} = {x -> y -> z} has path [x, y, z].
        """
        ...

    # -------------------------------------------------------------------------
    # Predicates
    # -------------------------------------------------------------------------

    
    @abstractmethod
    def is_primitive(self) -> bool:
        """
        Return True if this cell is primitive (path length = 2).

        A primitive n-cell F: f → g represents an atomic transformation,
        not decomposable into smaller n-cells. Non-primitive cells
        arise from composition, e.g., F: f → g → h.
        """
        ...

    
    @abstractmethod
    def is_equivalent_to(self, other: Any) -> BoolProof:
        """
        Return True if this cell is equivalent to another cell.

        This is system-dependent: requires higher cells as witnesses.
        """
        ...

    # -------------------------------------------------------------------------
    # String diagram rendering
    # -------------------------------------------------------------------------

    
    @abstractmethod
    def to_string_diagram(self) -> str:
        """
        Render this n-cell as a string diagram.

        String diagrams are the Poincaré dual of commutative diagrams:
        - 0-cells (objects): regions of the plane
        - 1-cells (morphisms): strings/wires that SEPARATE regions
        - 2-cells (natural transformations): nodes/points ON the strings

        Convention: diagrams flow bottom-to-top. A 1-cell f: A → B is a
        vertical string with region A on the left and region B on the right.

        Examples
        --------
        PRIMITIVE CELLS:

        0-cell (object A):
            A single labeled region of the plane:

                    A

        1-cell (morphism f: A → B):
            A vertical string labeled f, separating regions A (left) and B (right):

                A   │   B
                    │f
                A   │   B

        2-cell (natural transformation α: f ⇒ g where f,g: A → B):
            A node α on the string, with wire f entering from below
            and wire g exiting above:

                A   │   B
                    │g
                A  [α]  B
                    │f
                A   │   B

        NON-PRIMITIVE (COMPOSED) CELLS:

        1-cell (composed f ∘ g where f: A → B, g: B → C):
            Two strings side-by-side, f separating A|B, g separating B|C:

                A   │   B   │   C
                    │f      │g
                A   │   B   │   C

            Or equivalently, the composite g∘f as a single string A|C
            with the intermediate region B "squeezed out":

                A   │   C
                    │g∘f
                A   │   C

        1-cell (longer composition f ∘ g ∘ h: A → B → C → D):
            Multiple parallel strings:

                A   │   B   │   C   │   D
                    │f      │g      │h
                A   │   B   │   C   │   D

        2-cell (composed α ∘ β where α: f ⇒ g, β: g ⇒ h, all A → B):
            Nodes stacked vertically on the same string, sharing wire g:

                A   │   B
                    │h
                A  [β]  B
                    │g
                A  [α]  B
                    │f
                A   │   B

        2-cell (horizontal composition α ⋆ β):
            Where α: f ⇒ f' (both A → B) and β: g ⇒ g' (both B → C).
            Two nodes side-by-side on parallel strings:

                A   │   B   │   C
                    │f'     │g'
                A  [α]  B  [β]  C
                    │f      │g
                A   │   B   │   C

        2-cell (naturality square for α: F ⇒ G between functors F,G: C → D):
            For morphism f: A → B in C, the naturality condition is:

                FA   │   FB
                     │Ff
                FA  [αA]  FB
                     │
                GA  [αB]  GB
                     │Gf
                GA   │   GB

            (Note: this shows how 2-cells interact with 1-cells in a 2-category)
        """
        ...

    @abstractmethod
    def primitive_decomposition(self) -> Sequence[Cell.n]:
        """
        Decompose this cell into a composition of primitive cells.
        E.g.
            {a → b → c} = {a → b} ∘ {b → c}
        """

    @abstractmethod
    def compose_with(self, other: Any) -> Cell.n:
        """
        Cells may admit many different compositions, but all cell classes
        should implement a default composition.
        """

    @classmethod
    def _from_path(cls, path: Sequence[Any]) -> Cell.n:
        """
        Construct an n-cell from a path of (n-1)-cells.
        """
        ...

    @classmethod
    def _from_domain_codomain(cls, source: Any, target: Any) -> Cell.n:
        """
        Construct a primitive n-cell from a source and target (n-1)-cell.
        """
        ...

    def is_empty_cell(self) -> bool:
        ...

    def is_zero_cell(self) -> bool:
        ...

    def is_one_cell(self) -> bool:
        ...

    def is_two_cell(self) -> bool:
        ...

    def is_loop(self) -> bool:
        ...

    def is_composable_with(self, other: Cell.n) -> bool:
        ...

    def is_identity(self) -> bool:
        ...

    # -------------------------------------------------------------------------
    # Dimension-shifting views
    # -------------------------------------------------------------------------

    def as_k_cell(self, k: int) -> Cell.n:
        """
        View this n-cell as a k-cell in a related category (0 <= k <= n-1).
        
        An n-cell in C can naturally be viewed as a lower-dimensional cell
        in various related categories:
        
        - 1-cell f: X → Y in C  →  0-cell in Hom_C(X, Y) or in Arr(C)
        - 2-cell η: f ⇒ g in C  →  1-cell in Arr(C)  →  0-cell in Hom_{Arr(C)}(f, g)
        - 2-cell η: F ⇒ G in Cat_w  →  1-cell in Arr(Cat_w)  →  0-cell in Fun(C,D)
        
        Args:
            k: The target dimension (0 <= k <= self.cell_dimension() - 1)
            
        Returns:
            This cell viewed as a k-cell in the appropriate category.
            The ambient category changes based on the dimension shift.
            
        Raises:
            ValueError: If k >= self.cell_dimension() or k < 0
        """
        ...

# =============================================================================
# Explicit n-cell ABCs with tightened types
# =============================================================================

class _EmptyCell(_All_Cells_ABC):
    """
    The unique empty cell
    """
    ...

class _ZeroCell(_All_Cells_ABC):
    """
    A 0-cell: an object in a category.

    0-cells are the objects of a category. Their source and target
    are the unique empty cell, and their path is the singleton [∅].
    """

    @override
    def source(self) -> _EmptyCell: ...

    @override
    def target(self) -> _EmptyCell: ...

    @override
    def path(self) -> list[_EmptyCell]: ...

    @classmethod
    def _from_path(cls, path: Sequence[_EmptyCell]) -> _ZeroCell:
        """
        Construct an 0-cell from a path of (-1)-cells.
        """
        ...

    @classmethod
    def _from_domain_codomain(cls, source: _EmptyCell, target: _EmptyCell) -> _ZeroCell:
        """
        Construct a primitive 0-cell from a source and target (-1)-cell.
        """
        ...

class _OneCell(_All_Cells_ABC):
    """
    A 1-cell: a morphism f: x → y between 0-cells.

    A 1-cell is represented by a sequence of 0-cells:

        f: x₁ → x₂ → ... → xₙ

    0-cells may repeat (allowing loops). The source is x₁, target is xₙ.
    1-cells must have length at least 1; a path of length 1 is a loop at that 0-cell.
    There is no compatibility condition on compositions, since 0-cells always "compose".

    The main idea: you have to remember not only the source x₁ and the target xₙ,
    but a chosen path x₁ → xₙ (which may have loops, repeated 0-cells, or just be
    a length one path). This is equivalent to specifying a rewrite rule:
        "x₁ can be rewritten to xₙ via the path x₁ → ... → xₙ."

    Example: Let G = {a, b, c} and take the free monoid on G, i.e. all words in a,b,c.
    - A 1-cell {a → c} allows replacing any instance of 'a' in a word with 'c'.
    - A 1-cell {a → b → c} naturally induces a 1-cell {a → c} by composition,
      but the two 1-cells are distinct since the paths differ.
    - This still allows you to rewrite 'a' to 'c' in two different ways:
      either directly, or by first replacing 'a' with 'b' and then 'b' with 'c'.
    - This distinction is important when we consider 2-cells between 1-cells,
      since we may want to distinguish between these two rewrites.

    Categorically, a 1-cell with source x₁ and target xₙ is an object in Hom_C(x₁, xₙ).
    Preserving paths means that we distinguish between different morphisms in
    Hom_C(x₁, xₙ) even if they have the same source and target.

    E.g. in G as above, consider:
        f := {a → b → c}
        g := {a → c}
    We regard f and g as distinct, unrelated morphisms in Hom_C(a, c).
    However, a 2-cell η: f ⇒ g would express that g is equivalent to f,
    expressing g as a morphism factoring through b.

    Example: Let G := ℕ = {0, 1, 2, 3, ...}. One can then specify 1-cells:
        P₁₀ := {0 → 1}
        P₁₁ := {1 → 2}
        P₁₂ := {2 → 3}
        ...
        P₁ₙ := {n → n+1}
    One can then specify 1-cells:
        P₂₀ := {0 → 2}
        P₂₁ := {1 → 3}
        P₂₂ := {2 → 4}
        ...
        P₂ₙ := {n → n+2}

    One can freely compose:
        P₁₀.compose_with(P₁₁) = {0 → 1 → 2}
    which is distinct from P₂₀ = {0 → 2}.
    However, it is equal to any 1-cell specified by precisely the same path.

    To impose the relation P₁₀ ∘ P₁₁ == P₂₀, one would need a primitive 2-cell:

        0 → 1 → 2
        |   |   |
        v   v   v
        0 ────→ 2

    More generally, a 2-cell is a sequence of such primitive 2-cells.
    Consider P₁₀ ∘ P₁₁ ∘ P₁₂ = {0 → 1 → 2 → 3} and P₃₀ := {0 → 3}.
    One can impose the relation P₁₀ ∘ P₁₁ ∘ P₁₂ == P₃₀ via a 2-cell:

        0 → 1 → 2 → 3   from P₁₀ ∘ P₁₁ ∘ P₁₂
        |   |   |   |
        v   v   v   v
        0 ────→ 2 → 3   from P₂₀ ∘ P₁₂
        |           |
        v           v
        0 ────────→ 3   from P₃₀
    """

    @override
    def source(self) -> _ZeroCell: ...

    @override
    def target(self) -> _ZeroCell: ...

    @override
    def path(self) -> list[_ZeroCell]: ...

    @override
    def compose_with(self, other: _OneCell) -> _OneCell: ...

    @classmethod
    def _from_path(cls, path: Sequence[_ZeroCell]) -> _OneCell:
        """
        Construct an 1-cell from a path of 0-cells.
        """
        ...

    @classmethod
    def _from_domain_codomain(cls, source: _ZeroCell, target: _ZeroCell) -> _OneCell:
        """
        Construct a primitive 1-cell from a source and target 0-cell.
        """
        ...

class _TwoCell(_All_Cells_ABC):
    """
    A 2-cell: a natural transformation α: f ⇒ g between 1-cells.

    A 2-cell is represented by a sequence of 1-cells:

        f_x:    x₁ → x₂ → ... → xₙ
                |    |          |
                v    v          v
        f_y:    y₁ → y₂ → ... → yₘ
                |    |          |
                v    v          v
                ....................
                |    |          |
                v    v          v
        f_z:    z₁ → z₂ → ... → zₚ

    The source is f_x and the target is f_z.
    Constraint: all source 0-cells must match (x₁ = y₁ = z₁)
    and all target 0-cells must match (xₙ = yₘ = zₚ).

    2-cells witness that one 1-cell can be transformed into another,
    providing the "proofs" or "evidence" for equivalence of morphisms.
    """

    @override
    def source(self) -> _OneCell: ...

    @override
    def target(self) -> _OneCell: ...

    @override
    def path(self) -> list[_OneCell]: ...

    @override
    def compose_with(self, other: _TwoCell) -> _TwoCell: ...

    @classmethod
    def _from_path(cls, path: Sequence[_OneCell]) -> _TwoCell:
        """
        Construct an 2-cell from a path of 1-cells.
        """
        ...

    @classmethod
    def _from_domain_codomain(cls, source: _OneCell, target: _OneCell) -> _TwoCell:
        """
        Construct a primitive 2-cell from a source and target 1-cell.
        """
        ...

    # -------------------------------------------------------------------------
    # 2-cell specific composition
    # -------------------------------------------------------------------------

    
    @abstractmethod
    def horizontally_compose_with(self, other: Self) -> Self:
        """
        Horizontal composition (whiskering): α ⋆ β.

        Given two 2-cells, α:
            f_x:    x₁ → x₂ → ... → xₙ
                    |    |          |
                    v    v          v
            f_y:    y₁ → y₂ → ... → yₘ
                    |    |          |
                    v    v          v
            f_z:    z₁ → z₂ → ... → zₚ

        and β:
            g_r:    r₁ → r₂ → ... → rₖ
                    |    |          |
                    v    v          v
            g_s:    s₁ → s₂ → ... → sₗ
                    |    |          |
                    v    v          v
            g_t:    t₁ → t₂ → ... → tₘ

        Their horizontal composition α ⋆ β is defined when:
            - xₙ = r₁,
            - yₘ = s₁,
            - zₚ = t₁,
        and is given by:
            f_x ∘ g_r:    x₁ → ... → xₙ = r₁ → ... → rₖ
                          |              |           |
                          v              v           v
            f_y ∘ g_s:    y₁ → ... → yₘ = s₁ → ... → sₗ
                          |              |           |
                          v              v           v
            f_z ∘ g_t:    z₁ → ... → zₚ = t₁ → ... → tₘ
        """
        ...

    
    @abstractmethod
    def vertically_compose_with(self, other: Self) -> Self:
        """
        Vertical composition: α ∘ β.

        Given two 2-cells, α:
            f_x:    x₁ → x₂ → ... → xₙ
                    |    |          |
                    v    v          v
            f_y:    y₁ → y₂ → ... → yₘ
                    |    |          |
                    v    v          v
            f_z:    z₁ → z₂ → ... → zₚ

        and β:
            g_r:    r₁ → r₂ → ... → rₖ
                    |    |          |
                    v    v          v
            g_s:    s₁ → s₂ → ... → sₗ
                    |    |          |
                    v    v          v
            g_t:    t₁ → t₂ → ... → tₘ

        Their vertical composition α ∘ β is defined when f_z = g_r,
        i.e. when z₁ = r₁, zₚ = rₖ, and the paths match.

        The resulting 2-cell α ∘ β is then given by:
            h_x:    x₁ → x₂ → ... → xₙ  [f_x]
                    |    |          |
                    v    v          v
            h_y:    y₁ → y₂ → ... → yₘ  [f_y]
                    |    |          |
                    v    v          v
            h_z:    z₁ → z₂ → ... → zₚ  [f_z = g_r, zᵢ = rᵢ]
                    |    |          |
                    v    v          v
            h_s:    s₁ → s₂ → ... → sₗ  [g_s]
                    |    |          |
                    v    v          v
            h_t:    t₁ → t₂ → ... → tₘ  [g_t]
        """
        ...

# =============================================================================
# Cell Container ABC
# =============================================================================

class _Cell_Container_ABC(ABC):
    """
    Container for managing collections of n-cells.

    Provides factory methods for creating cells and predicates for
    testing cell membership and type.
    """

    # -------------------------------------------------------------------------
    # Membership
    # -------------------------------------------------------------------------

    
    @abstractmethod
    def __contains__(self, celldata: Any) -> bool: ...

    # -------------------------------------------------------------------------
    # 0-cell operations
    # -------------------------------------------------------------------------

    
    @abstractmethod
    def add_zero_cell(self, underlying_data: Any) -> _ZeroCell: ...

    
    @abstractmethod
    def get_zero_cells(self) -> Sequence[_ZeroCell]: ...

    # -------------------------------------------------------------------------
    # 1-cell operations
    # -------------------------------------------------------------------------

    # Leave type signature loose here, tighten in specific n-cell classes.
    
    @abstractmethod
    def add_one_cell(self, underlying_data: Any, path: Any) -> _OneCell:
        """
        When adding a 1-cell
        f: x_1 -> x_2 -> ... -> x_n,
        represented by the path [x_1, ..., x_n], you must ensure that all of the following 1-cells are also added:
        x_1 -> x_2,
        x_2 -> x_3,
        ...
        x_{n-1} -> x_n,
        along with all of their compositions.
        """

    
    @abstractmethod
    def get_one_cells(self) -> Sequence[_OneCell]: ...

    
    @abstractmethod
    def get_primitive_one_cells(self) -> Sequence[_OneCell]:
        """
        Return only primitive 1-cells (edges, path length 2).

        For finitary encodings like KBMAG, only primitive cells are generators.
        Composed paths are represented as products of primitive generators.
        """
        ...

    # -------------------------------------------------------------------------
    # 2-cell operations
    # -------------------------------------------------------------------------

    # Leave type signature loose here, tighten in specific n-cell classes.
    
    @abstractmethod
    def add_two_cell(self, underlying_data: Any, path: Any) -> _TwoCell: ...

    
    @abstractmethod
    def get_two_cells(self) -> Sequence[_TwoCell]: ...

    
    @abstractmethod
    def get_primitive_two_cells(self) -> Sequence[_TwoCell]:
        """
        Return only primitive 2-cells (path length 2: just source and target).

        For finitary encodings like KBMAG, only primitive cells are relations.
        Composed 2-cells are derived from primitive relations.
        """
        ...

    # -------------------------------------------------------------------------
    # Generic n-cell operations
    # -------------------------------------------------------------------------

    # Leave type signature loose here, tighten in specific n-cell classes.
    
    @abstractmethod
    def add_n_cell(self, n: int, underlying_data: Any, path: Any) -> Cell.n: ...

    
    @abstractmethod
    def get_n_cells(self, n: int) -> Sequence[Cell.n]: ...

    # -------------------------------------------------------------------------
    # String diagram rendering
    # -------------------------------------------------------------------------

    
    @abstractmethod
    def cell_to_string_diagram(self, cell: Cell.n) -> str:
        """
        Render an n-cell as a string diagram.

        String diagrams are the Poincaré dual of commutative diagrams:
        - 0-cells: regions of the plane
        - 1-cells: wires/strings separating regions
        - 2-cells: nodes/boxes where wires meet

        Dispatches to the cell's to_string_diagram() method.
        """
        ...

    # -------------------------------------------------------------------------
    # Equivalence checks
    # -------------------------------------------------------------------------


    
    @abstractmethod
    def are_equivalent_zero_cells(self, x: _ZeroCell, y: _ZeroCell) -> bool: ...

    
    @abstractmethod
    def are_equivalent_one_cells(self, f: _OneCell, g: _OneCell) -> bool: ...

    
    @abstractmethod
    def are_equivalent_two_cells(self, eta: _TwoCell, mu: _TwoCell) -> bool: ...

# =============================================================================
# Module exports (for type checker satisfaction)
# =============================================================================

class Cell:
    Container = _Cell_Container_ABC
    mn1 = _EmptyCell
    m0 = _ZeroCell
    m1 = _OneCell
    m2 = _TwoCell
    n = _All_Cells_ABC






