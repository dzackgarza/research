# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/cells.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

# from collections.abc import Sequence
# from dataclasses import dataclass
# from typing import Any, Literal, Never, TypeIs, assert_never, cast, final, overload

# from pydantic import NonNegativeInt

# from src._types import CategoryABCs


# @dataclass
# class Cell(CategoryABCs.Cell):
#     """A generic n-cell for n >= 0."""

#     _underlying_category: Any
#     _n: NonNegativeInt
#     _path: list[Cell]

#     def __hash__(self) -> int:
#         return hash((tuple(x.__hash__() for x in self._path),))

#     def __eq__(self, other: object) -> bool:
#         if not isinstance(other, Cell):
#             return False
#         return self.dimension() == other.dimension() and self.path() == other.path()

#     def __post__init__(self) -> None:
#         assert self.source().dimension() == self.dimension() - 1, "Source dimension mismatch"
#         assert self.target().dimension() == self.dimension() - 1, "Target dimension mismatch"
#         match self.dimension():
#             case -1:
#                 assert self.path() == [], "EmptyCell must have empty path"
#             case 0:
#                 assert len(self.path()) == 1, "0-cell must have path of length 1"
#                 assert self.source() == EmptyCell() and self.target() == EmptyCell(), (
#                     "0-cell source and target must be EmptyCell"
#                 )
#             case 1:
#                 assert len(self.path()) >= 1, "1-cell must have path of length at least 1"
#                 assert isinstance(self.source(), ZeroCell), "1-cell source must be ZeroCell"
#                 assert isinstance(self.target(), ZeroCell), "1-cell target must be ZeroCell"
#             case 2:
#                 assert len(self.path()) >= 1, "2-cell must have path of length at least 1"
#                 assert isinstance(self.source(), OneCell), "2-cell source must be OneCell"
#                 assert isinstance(self.target(), OneCell), "2-cell target must be OneCell"
#             case _:
#                 raise NotImplementedError("NCell only implemented for n=0,1,2")

#     @final
#     def dimension(self) -> NonNegativeInt:
#         return self._n

#     @final
#     def source(self) -> Cell:
#         if len(self.path()) == 0:
#             assert self.dimension() == -1, "Only EmptyCell can have empty path"
#             raise TypeError("EmptyCell has no source")
#         return self.path()[0]

#     @final
#     def target(self) -> Cell:
#         if len(self.path()) == 0:
#             assert self.dimension() == -1, "Only EmptyCell can have empty path"
#             raise TypeError("EmptyCell has no target")
#         return self.path()[-1]

#     @final
#     def underlying_data(self) -> Any:
#         return self._underlying_category

#     @final
#     def path(self) -> list[Cell]:
#         return self._path

#     @final
#     def is_primitive(self) -> bool:
#         """
#         Check if this 1-cell is primitive, i.e. has length 1.
#         E.g.

#         f: x -> y is primitive,
#         g: x -> x is primitive,
#         but
#         h: x -> y -> z is not.
#         """
#         p = self.path()
#         return len(p) == 2 or (
#             len(p) == 1 and p[0] == p[1] # Allow length 1 paths for loops
#         )

#     @classmethod
#     def from_source_and_target(cls, underlying_data: Any, source: Cell, target: Cell) -> Cell:
#         """
#         Shortcut for primitive paths x->y.
#         """
#         return cls(
#             _underlying_category=underlying_data, _n=source.dimension() + 1, _path=[source, target]
#         )


# @dataclass
# class EmptyCell(Cell):
#     _underlying_category: CategoryABCs.EmptyCategory
#     _n: NonNegativeInt = -1
#     _path: list[Cell] = []


# @dataclass
# class ZeroCell(Cell):
#     _underlying_category: CategoryABCs.EmptyCategory
#     _n: NonNegativeInt = 0
#     _path: list[Cell] = [EmptyCell()]


# @dataclass
# class OneCell(Cell):
#     """
#     A 1-cell represented by a sequence of 0-cells:

#     f_x: x_1 -> x_2 -> ... -> x_n

#     0-cells are allowed to repeat, so this includes loops.
#     1-cells must have length at least 1; a path of length 1 is a loop at that 0-cell.
#     1-cells have source x_1 and target x_n.
#     There is no compatibility condition on compositions, since 0-cells always "compose".

#     The main idea: you have to remember not only the source x_1 and the target x_n, but a chosen path x_1 -> x_n (which may have loops, repeated 0-cells, or just be a length one path).
#     This is equivalent to specifying a rewrite rule:
#         "x_1 can be rewritten to x_n via the path x_1 -> ... -> x_n".

#     E.g. let G = {a, b, c} and take the free monoid on G, i.e. all words in a,b,c.
#     Then a 1-cell {a -> c} allows replacing any instance of 'a' in a word with 'c'.
#     A 1-cell {a -> b -> c} naturally induces a 1-cell {a->c} by composition, but the two 1-cells are distinct since the paths differ.
#     This still allows you to rewrite 'a' to 'c' in two different ways, either directly by replacing 'a' with 'c', or by first replacing 'a' with 'b' and then 'b' with 'c'.
#     This is important when we consider 2-cells between 1-cells, since we may want to distinguish between these two rewrites.

#     Categorically, a 1-cell with source x_1 and target x_n is an object in Hom_C(x_1, x_n). Preserving paths means that we distinguish between different morphisms in Hom_C(x_1, x_n) even if they have the same source and target.
#     E.g. in G as above, consider

#     f := {a -> b -> c}

#     g := {a -> c}

#     We regard f and g as distinct, unrelated morphisms in Hom_C(a, c). However, a 2-cell η: f => g would express that g is equivalent to f, expressing g as a morphism factoring through b.

#     E.g. consider G := NN := {0,1,2,3,...}. One can then specify 1-cells
#     P_1_0 := {0 -> 1}
#     P_1_1 := {1 -> 2}
#     P_1_2 := {2 -> 3}
#     ...
#     P_1_n := {n -> n+1}
#     One can then specify 1-cells
#     P_2_0 := {0 -> 2}
#     P_2_1 := {1 -> 3}
#     P_2_2 := {2 -> 4}
#     ...
#     P_2_n := {n -> n+2}
#     One can freely compose:
#     P_1_0.compose_with(P_1_1) = {0 -> 1 -> 2},
#     which is distinct from P_2_0 = {0 -> 2}.
#     However, it is equal to any 1-cell specified by precisely the same path.
#     To impose the relation P_1_0.compose_with(P_1_1) == P_2_0, one would need a primitive 2-cell between them:

#     0 -> 1 -> 2
#     |    |    |
#     v    v    v
#     0 ------> 2

#     More generally, a 2-cell is a sequence of such primitive 2-cells: consider P_1_0 ∘ P_1_1 ∘ P_1_2 = {0 -> 1 -> 2 -> 3} and P_3_0 := {0 -> 3}.
#     Then one can impose the relation P_1_0 ∘ P_1_1 ∘ P_1_2 == P_3_0 via a 2-cell:

#     0 -> 1 -> 2 -> 3 from P_1_0 ∘ P_1_1 ∘ P_1_2
#     |    |    |    |
#     v    v    v    v
#     0 ------->2--->3 from P_2_0 ∘ P_1_2
#     |              |
#     v              v
#     0 ------------>3 from P_3_0
#     """

#     _n: NonNegativeInt = 1

#     def horizontally_compose(self, other: OneCell) -> OneCell:
#         """
#         One-cells can be composed horizontally: suppose
#         f: x_1 -> x_2 -> ... -> x_n
#         g: y_1 -> y_2 -> ... -> y_m

#         Their (horizontal) composition is defined when x_n = y_1, and is given by
#         f ∘ g: x_1 -> x_2 -> ... -> x_n = y_1 -> y_2 -> ... -> y_m
#         Note that there is no restriction on the lengths of f and g.
#         """
#         assert self.target() == other.source(), "Cells don't compose"
#         new_data = (self.underlying_data(), other.underlying_data())
#         new_path = self.path() + other.path()[1:]
#         return OneCell(_underlying_category=new_data, _path=new_path)


# @dataclass
# class TwoCell(Cell):
#     """
#     A 2-cell represented by a sequence of 1-cells:
#     f_x:    x_1 -> x_2 -> ... -> x_n
#             |      |             |
#             v      v             v
#     f_y:    y_1 -> y_2 -> ... -> y_m
#             |      |             |
#             v      v             v
#             .......................
#             |      |             |
#             v      v             v
#     f_z:    z_1 -> z_2 -> ... -> z_p

#     Here the source is f_x and the target is f_z.
#     We require that x_1 = y_1 = z_1 and x_n = y_m = z_p, i.e. the source and target 0-cells match.
#     """

#     def __init__(self, _underlying_category: Any, _path: list[Cell]) -> None:
#         Cell.__init__(self, _underlying_category=_underlying_category, _n=2, _path=_path)

#         sources = {cell.source() for cell in self.path()}
#         targets = {cell.target() for cell in self.path()}
#         assert len(sources) == 1, "All source 0-cells must match"
#         assert len(targets) == 1, "All target 0-cells must match"

#     def vertically_compose(self, other: TwoCell) -> TwoCell:
#         """
#         Given two 2-cells, say α given by
#         f_x:    x_1 -> x_2 -> ... -> x_n
#                 |      |             |
#                 v      v             v
#         f_y:    y_1 -> y_2 -> ... -> y_m
#                 |     |              |
#                 v     v              v
#         f_z:    z_1 -> z_2 -> ... -> z_p

#         and β given by
#         g_r:    r_1 -> r_2 -> ... -> r_k
#                 |      |             |
#                 v      v             v
#         g_s:    s_1 -> s_2 -> ... -> s_l
#                 |      |             |
#                 v      v             v
#         g_t:    t_1 -> t_2 -> ... -> t_m

#         Their vertical composition α ∘ β is defined when f_z = g_r, i.e. when z_1 = r_1, z_p = r_k, and the paths match.
#         The resulting 2-cell α ∘ β is then given by
#         h_x:    x_1 -> x_2 -> ... -> x_n [f_x]
#                 |      |             |
#                 v      v             v
#         h_y:    y_1 -> y_2 -> ... -> y_m [f_y]
#                 |      |             |
#                 v      v             v
#         h_z:    z_1 -> z_2 -> ... -> z_p [f_z = g_r, z_i = r_i]
#                 |      |             |
#                 v      v             v
#         h_s:    s_1 -> s_2 -> ... -> s_l [g_s]
#                 |      |             |
#                 v      v             v
#         h_t:    t_1 -> t_2 -> ... -> t_m [g_t]
#         """
#         assert self.target() == other.source(), "Cells don't compose"
#         new_data = (self.underlying_data(), other.underlying_data())
#         new_path = self.path() + other.path()[1:]
#         return TwoCell(_underlying_category=new_data, _path=new_path)

#     def _is_onecell_path(self, p: Any) -> TypeIs[list[OneCell]]:
#         return all(isinstance(cell, OneCell) for cell in p)

#     def horizontally_compose(self, other: TwoCell) -> TwoCell:
#         """
#         Given two 2-cells, say α given by
#         f_x:    x_1 -> x_2 -> ... -> x_n
#                 |      |             |
#                 v      v             v
#         f_y:    y_1 -> y_2 -> ... -> y_m
#                 |     |              |
#                 v     v              v
#         f_z:    z_1 -> z_2 -> ... -> z_p

#         and β given by
#         g_r:    r_1 -> r_2 -> ... -> r_k
#                 |      |             |
#                 v      v             v
#         g_s:    s_1 -> s_2 -> ... -> s_l
#                 |      |             |
#                 v      v             v
#         g_t:    t_1 -> t_2 -> ... -> t_m

#         Their horizontal composition α ⋆ β is defined when:
#             - x_n = r_1,
#             - y_m = s_1,
#             - z_p = t_1,
#         and is given by
#         f_x ∘ g_r:    x_1 -> ... -> x_n = r_1 -> ... -> r_k
#                         |                 |              |
#                         v                 v              v
#         f_y ∘ g_s:    y_1 -> ... -> y_m = s_1 -> ... -> s_l
#                         |                 |              |
#                         v                 v              v
#         f_z ∘ g_t:    z_1 -> ... -> z_p = t_1 -> ... -> t_m
#         """
#         p1 = self.path()
#         p2 = other.path()
#         assert len(p1) == len(p2), "2-Cells must have same height to compose horizontally"
#         self_targets = [cell.target() for cell in p1]
#         other_sources = [cell.source() for cell in p2]
#         assert self_targets == other_sources, "Cells don't compose horizontally"
#         assert self._is_onecell_path(p1), "Self path must be OneCells"
#         assert self._is_onecell_path(p2), "Other path must be OneCells"
#         new_data = (self.underlying_data(), other.underlying_data())
#         new_path = [
#             self_cell.compose_with(other_cell)
#             for self_cell, other_cell in zip(p1, p2, strict=True)
#         ]
#         return TwoCell(_underlying_category=new_data, _path=new_path)


# class CellContainer(CategoryABCs.CellContainer):
#     _cells: dict[int, set[Cell]] = {0: set(), 1: set(), 2: set()}

#     @overload
#     def add_n_cell(self, n: Literal[0], underlying_data: Any, path: Any) -> ZeroCell: ...

#     @overload
#     def add_n_cell(self, n: Literal[1], underlying_data: Any, path: Any) -> OneCell: ...

#     @overload
#     def add_n_cell(self, n: Literal[2], underlying_data: Any, path: Any) -> TwoCell: ...

#     @final
#     def add_n_cell(self, n: int, underlying_data: Any, path: Any) -> Cell:
#         """Add an n-cell to the container given cell data, and return that cell."""
#         assert 0 <= n <= 2, f"Only n=0,1,2 supported, got n={n}"
#         match n:
#             case 0:
#                 return self.add_zero_cell(underlying_data)
#             case 1:
#                 return self.add_one_cell(underlying_data, path)
#             case 2:
#                 return self.add_two_cell(underlying_data, path)
#             case _:
#                 assert_never(cast("Never", n))

#     @overload
#     def get_n_cells(self, n: Literal[0]) -> Sequence[ZeroCell]: ...

#     @overload
#     def get_n_cells(self, n: Literal[1]) -> Sequence[OneCell]: ...

#     @overload
#     def get_n_cells(self, n: Literal[2]) -> Sequence[TwoCell]: ...

#     @final
#     def get_n_cells(
#         self, n: int
#     ) -> Sequence[Cell]:
#         """Return a list of n-cells in C."""
#         assert 0 <= n <= 2, f"Only n=0,1,2 supported, got n={n}"
#         return list(self._cells[n])

#     @final
#     def is_n_cell(self, celldata: Any) -> bool:
#         """Check if celldata corresponds to an n-cell in C."""
#         return any(
#             celldata == cell.underlying_data()
#             for cell in [cell for i in self._cells for cell in self._cells[i]]
#         )

#     def add_zero_cell(self, underlying_data: CategoryABCs.Object) -> ZeroCell:
#        C0 = ZeroCell(_underlying_category=underlying_data)
#        self._cells[0].add(C0)
#        return C0.underlying_data()

#     def get_zero_cells(self) -> Sequence[ZeroCell]:
#         return self.get_n_cells(0)

#     def add_one_cell(self, underlying_data: Any, path: Any) -> OneCell:
#         f = OneCell(_underlying_category=underlying_data, _path=path)
#         self._cells[1].add(f)
#         return f.underlying_data()

#     def get_one_cells(self) -> Sequence[OneCell]:
#         return self.get_n_cells(1)

#     def get_primitive_one_cells(self) -> Sequence[OneCell]:
#         return [c for c in self.get_one_cells() if c.is_primitive()]

#     def add_two_cell(self, underlying_data: Any, path: Any) -> TwoCell:
#         alpha = TwoCell(_underlying_category=underlying_data, _path=path)
#         self._cells[2].add(alpha)
#         return alpha.underlying_data()

#     def get_two_cells(self) -> Sequence[TwoCell]:
#         return self.get_n_cells(2)

#     def get_primitive_two_cells(self) -> Sequence[TwoCell]:
#         return [c for c in self.get_two_cells() if c.is_primitive()]

#     def __contains__(self, celldata: Any) -> bool:
#         return any(
#             x == celldata
#             for i in self._cells for x in self._cells[i]
#         )

#     def are_equivalent_two_cells(
#         self, alpha: TwoCell, beta: TwoCell
#     ) -> bool:
#         """
#         By definition, let α = β iff there exists a 3-cell Γ: α => β in C.
#         """
#         return (alpha.source(), alpha.target()) == (beta.source(), beta.target())

#     def are_equivalent_one_cells(
#         self, f: OneCell, g: OneCell
#     ) -> bool:
#         """
#         By definition, let f = g iff there exists a 2-cell α: f => g in C.
#         """
#         TempTwoCell = TwoCell(_underlying_category=None, _path=[f, g])
#         return any(
#             self.are_equivalent_two_cells(alpha, TempTwoCell)
#             for alpha in self.get_two_cells()
#         )

#     def are_equivalent_zero_cells(
#         self, x: ZeroCell, y: ZeroCell
#     ) -> bool:
#         """
#         x ≃ y iff there exist:
#             - a 1-cell f: x -> y in C,
#             - a 1-cell g: y -> x in C,
#             - a 2-cell η: g∘f => id_x in C,
#             - a 2-cell θ: f∘g => id_y in C.
#         Thus the algorithm to determine equivalence proceeds as follows:
#         1. Find all 1-cells f: x -> y in C.
#         2. Fina all 1-cells g: y -> x in C.
#         3. For each pair (f, g), create a temporary 2-cell g∘f => id_x and check if any existing 2-cell in C is equivalent to it.
#         4. Similarly, create a temporary 2-cell f∘g => id_y and check for equivalence of 2-cells.
#         5. If such η and θ exist for any pair (f, g), then x ≃ y.
#         6. Otherwise, x and y are not equivalent.
#         """
#         id_x = OneCell.from_source_and_target(
#             underlying_data=None, source=x, target=x
#         )
#         id_y = OneCell.from_source_and_target(
#             underlying_data=None, source=y, target=y
#         )
#         valid_f_x_to_y = [
#             f for f in self.get_one_cells()
#             if f.source() == x and f.target() == y
#         ]
#         valid_g_y_to_x = [
#             g for g in self.get_one_cells()
#             if g.source() == y and g.target() == x
#         ]

#         for f in valid_f_x_to_y:
#             for g in valid_g_y_to_x:
#                 # Check for 2-cells η: g∘f => id_x and θ: f∘g => id_y
#                 gf = g.horizontally_compose(f)
#                 fg = f.horizontally_compose(g)
#                 TempTwoCell_gf = TwoCell(_underlying_category=None, _path=[gf, id_x])
#                 eta_exists = any(
#                     self.are_equivalent_two_cells(alpha,TempTwoCell_gf)
#                     for alpha in self.get_two_cells()
#                 )
#                 TempTwoCell_fg = TwoCell(_underlying_category=None, _path=[fg, id_y])
#                 theta_exists = any(
#                     self.are_equivalent_two_cells(beta, TempTwoCell_fg)
#                     for beta in self.get_two_cells()
#                 )
#                 if eta_exists and theta_exists:
#                     return True
#         return False
