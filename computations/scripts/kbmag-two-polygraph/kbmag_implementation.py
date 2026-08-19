# Origin: gitclones/integral_lattice/cat/src/partial_implementation_bases/kbmag_implementation.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, section R4). Content below is unmodified;
# the encoding and its recorded defects are in README.md beside this file.

"""
KBMAG-based partial implementation for cell equivalence checks.

Provides a partial implementation of `_Cell_Container_ABC` using GAP's KBMAG
package for Knuth-Bendix completion to decide cell equivalence.

Classes inheriting from `KBMAGCellContainer` get KBMAG-based implementations of:
- `are_equivalent_two_cells`
- `are_equivalent_one_cells`
- `are_equivalent_zero_cells`

Encoding (2-polygraph → monoid with zero):
- Idempotents `e_<n>` for each 0-cell (represent identity morphisms)
- Zero element `z` for noncomposable products
- Generators for each primitive 1-cell edge (named by symbol_name)
- Typing/zero relations enforce partial composition
- 2-cells become relations `source_word = target_word`

References:
    [1] gap-packages.github.io/kbmag/doc/chap2.html
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import final

from sage.all import libgap # type: ignore[import-cython]

from src._types import CategoryABCs, SageType
from src.abc_specs.cells import *
from functools import reduce


@dataclass(frozen=True, slots=True)
class _Gap_Monoid_Word:
    """
    Thin wrapper around SageType.GapElement to localize Cython type checking issues.
    
    This wrapper exists solely to provide proper type hints for SageType.GapElement,
    which comes from a Cython library and causes type checking errors.
    """

    gap_element: SageType.GapElement

    def __mul__(self, other: _Gap_Monoid_Word) -> _Gap_Monoid_Word:
        return _Gap_Monoid_Word(self.gap_element * other.gap_element)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, _Gap_Monoid_Word) and self.gap_element == other.gap_element

@dataclass(frozen=True, slots=True)
class _WrappedIdentityOneCell:
    """A 0-cell paired with its idempotent generator."""

    identity_cell: OneCell
    identity_word: _Gap_Monoid_Word

    def to_gap(self) -> SageType.GapElement: # type: ignore[cython-return-type]
        return self.identity_word.gap_element

    def raw_zero_cell(self) -> ZeroCell:
        return self.identity_cell.source()


@dataclass(frozen=True, slots=True)
class _WrappedOneCell:
    """A 1-cell paired with its generator and wrapped endpoints."""

    raw_cell: OneCell
    source: _WrappedIdentityOneCell
    target: _WrappedIdentityOneCell
    morphism_word: _Gap_Monoid_Word

    def to_gap(self) -> SageType.GapElement: # type: ignore[cython-return-type]
        return self.morphism_word.gap_element

    def __mul__(self, other: _WrappedOneCell) -> _WrappedOneCell:
        return _WrappedOneCell(
            self.raw_cell.compose_with(other.raw_cell),
            self.source,
            other.target,
            self.morphism_word * other.morphism_word
        )

    def source_raw_cell(self) -> ZeroCell:
        return self.source.raw_zero_cell()

    def target_raw_cell(self) -> ZeroCell:
        return self.target.raw_zero_cell()

    def source_identity_word(self) -> _Gap_Monoid_Word:
        return self.source.identity_word

    def target_identity_word(self) -> _Gap_Monoid_Word:
        return self.target.identity_word

@dataclass
class _WrappedTwoCell:
    raw_cell: TwoCell
    source: _WrappedOneCell
    target: _WrappedOneCell

@dataclass
class _RewritingSystem:
    rws: SageType.GapElement

    def words_equal(self, w1: _Gap_Monoid_Word, w2: _Gap_Monoid_Word) -> bool:
        """Check if two words are equal in the quotient monoid."""
        return libgap.ReducedWord(self.rws, w1.gap_element) == libgap.ReducedWord(self.rws, w2.gap_element)

    def to_gap(self) -> SageType.GapElement: # type: ignore[cython-return-type]
        return self.rws


@dataclass
class KBMAGCellContainer(CategoryABCs.CellContainer):
    """
    Partial _Cell_Container_ABC implementation with KBMAG-based equivalence.

    Provides concrete implementations of equivalence methods using KBMAG's
    Knuth-Bendix completion algorithm. All other abstract methods remain
    for subclasses to implement.
    """

    _wrapped_identity_one_cells: list[_WrappedIdentityOneCell]
    _wrapped_one_cells: list[_WrappedOneCell]
    _wrapped_two_cells: list[_WrappedTwoCell]
    _rewriting_system: _RewritingSystem

    def __post_init__(self) -> None:
        libgap.LoadPackage("kbmag")
        self._build_rewriting_system()

    def _build_rewriting_system(self) -> None:
        """
        Build the KBMAG rewriting system.
        
        Returns:
            - Completed rewriting system
            - List of wrapped 0-cells with generators
            - List of wrapped 1-cells with generators
        """
        # prim_zero_cells = list(self.get_zero_cells())
        prim_one_cells = [x for x in self.get_primitive_one_cells()]
        prim_two_cells = [x for x in self.get_primitive_two_cells() if not x.is_identity()]

        identity_one_cells: list[OneCell] = [
            f for f in prim_one_cells if f.is_identity()
        ]
        nontrivial_one_cells: list[OneCell] = [
            f for f in prim_one_cells if not f.is_identity()
        ]

        # Build generator names
        gen_names = (
            [c.cell_name() for c in identity_one_cells]
            + ["z"]
            + [c.cell_name() for c in nontrivial_one_cells]
        )

        free_monoid = libgap.FreeMonoid(*gen_names)
        raw_gens = [wi for wi in libgap.GeneratorsOfMonoid(free_monoid)]

        n_objects = len(identity_one_cells)
        e_gens = [_Gap_Monoid_Word(g) for g in raw_gens[:n_objects]]
        z = raw_gens[n_objects]
        a_gens = [_Gap_Monoid_Word(g) for g in raw_gens[n_objects + 1 :]]

        # Wrap cells with their generators
        
        wrapped_identity_one_cells: list[_WrappedIdentityOneCell] = [
            _WrappedIdentityOneCell(c, gen)
            for c, gen in zip(identity_one_cells, e_gens, strict=True)
        ]

        wrapped_nontrivial_one_cells: list[_WrappedOneCell] = [
            _WrappedOneCell(
                raw_one_cell, 
                next(w for w in wrapped_identity_one_cells if w.raw_zero_cell() == raw_one_cell.source()),
                next(w for w in wrapped_identity_one_cells if w.raw_zero_cell() == raw_one_cell.target()),
                gap_gen
            )
            for raw_one_cell, gap_gen in zip(nontrivial_one_cells, a_gens, strict=True)
        ]

        # TODO: check if this is correct
        wrapped_two: list[_WrappedTwoCell] = [
            _WrappedTwoCell(c, 
                next(w for w in wrapped_nontrivial_one_cells if w.raw_cell == c.source()), 
                next(w for w in wrapped_nontrivial_one_cells if w.raw_cell == c.target())
            )
            for c in prim_two_cells
        ]

        # Build relations using raw GAP elements
        id_xis = [w.to_gap() for w in wrapped_identity_one_cells]
        f_xi_yjs = [w.to_gap() for w in wrapped_nontrivial_one_cells]
        all_morphism_gens = id_xis + [z] + f_xi_yjs

        rels = []
        
        # Idempotent relations: id_x * id_x = id_x
        rels.extend([[id_x * id_x, id_x] for id_x in id_xis])
        
        # Incompatible objects: id_x * id_y = z for x ≠ y
        rels.extend([[id_x * id_y, z] for id_x, id_y in product(id_xis, repeat=2) if id_x != id_y])
        
        # Zero annihilation: z * f = f * z = z for all morphisms
        rels.extend([[z * f, z] for f in all_morphism_gens])
        rels.extend([[f * z, z] for f in all_morphism_gens])

        # Relations imposed by 1-cells
        for wrapped in wrapped_nontrivial_one_cells:
            id_x = wrapped.source.to_gap()
            id_y = wrapped.target.to_gap()
            f_xy = wrapped.to_gap()
            
            # Composition with correct endpoints
            rels.extend([[id_x * f_xy, f_xy], [f_xy * id_y, f_xy]])
            
            # Composition with wrong endpoints = z
            rels.extend([[id_xp * f_xy, z] for id_xp in id_xis if id_xp != id_x])
            rels.extend([[f_xy * id_yp, z] for id_yp in id_xis if id_yp != id_y])

        # 2-cell relations: source = target
        rels.extend([[tc.source.to_gap(), tc.target.to_gap()] for tc in wrapped_two])

        # Create quotient and complete rewriting system
        quotient = free_monoid / libgap(rels)
        rws = libgap.KBMAGRewritingSystem(quotient)
        libgap.SetOrderingOfKBMAGRewritingSystem(rws, "shortlex")
        libgap.KnuthBendix(rws)

        self._rewriting_system = _RewritingSystem(rws)
        self._wrapped_identity_one_cells = wrapped_identity_one_cells
        self._wrapped_nontrivial_one_cells = wrapped_nontrivial_one_cells
        self._wrapped_two_cells = wrapped_two

    @final
    def are_equivalent_two_cells(
        self, eta: TwoCell, mu: TwoCell
    ) -> bool:
        """Two 2-cells equivalent iff same boundary (no 3-cells)."""
        return (eta.source(), eta.target()) == (mu.source(), mu.target())

    @final
    def are_equivalent_one_cells(
        self, f: OneCell, g: OneCell
    ) -> bool:
        """Two 1-cells equivalent iff same normal form in quotient."""
        if (f.source(), f.target()) != (g.source(), g.target()):
            return False
        if f == g:
            return True

        self._build_rewriting_system()

        composed_wrapped_f = reduce(
            lambda a,b: a * b, [
                self.get_wrapped_nontrivial_cell(onecell)
                for onecell in f.primitive_decomposition()
        ])

        composed_wrapped_g = reduce(
            lambda a,b: a * b, [
                self.get_wrapped_nontrivial_cell(onecell)
                for onecell in g.primitive_decomposition()
        ])

        return self._rewriting_system.words_equal(
            composed_wrapped_f.morphism_word,
            composed_wrapped_g.morphism_word,
        )

    def get_wrapped_identity_cell(self, x: ZeroCell) -> _WrappedIdentityOneCell:
        return next(w for w in self._wrapped_identity_one_cells if w.raw_zero_cell() == x)

    def get_wrapped_nontrivial_cell(self, x: OneCell) -> _WrappedOneCell:
        return next(w for w in self._wrapped_nontrivial_one_cells if w.raw_cell == x)

    def get_wrapped_two_cell(self, x: TwoCell) -> _WrappedTwoCell:
        return next(w for w in self._wrapped_two_cells if w.raw_cell == x)

    def get_identity_word(self, x: ZeroCell) -> _Gap_Monoid_Word:
        return self.get_wrapped_identity_cell(x).identity_word

    def get_morphism_word(self, x: OneCell) -> _Gap_Monoid_Word:
        return self.get_wrapped_nontrivial_cell(x).morphism_word

    def get_one_cells_between(self, x: ZeroCell, y: ZeroCell) -> list[_WrappedOneCell]:
        return [
            w for w in self._wrapped_nontrivial_one_cells
            if w.source_raw_cell == x
            and w.target_raw_cell == y
        ]

    @final
    def are_equivalent_zero_cells(
        self, x: ZeroCell, y: ZeroCell
    ) -> bool:
        """
        Two 0-cells equivalent iff isomorphic via invertible 1-cells.

        Checks if ∃f: x → y, g: y → x such that gf = e_x and fg = e_y.
        """
        if x == y:
            return True

        self._build_rewriting_system()

        # Get identity words
        id_x = self.get_identity_word(x)
        id_y = self.get_identity_word(y)

        # Get primitive 1-cells between x and y
        f_xys = self.get_one_cells_between(x, y)
        g_yxs = self.get_one_cells_between(y, x)

        if len(f_xys) == 0 or len(g_yxs) == 0:
            return False

        return any(
            self._rewriting_system.words_equal(
                g_yx.morphism_word * f_xy.morphism_word, 
                id_x
            )
            and self._rewriting_system.words_equal(
                f_xy.morphism_word * g_yx.morphism_word, 
                id_y
            )
            for f_xy, g_yx in product(f_xys, g_yxs)
        )