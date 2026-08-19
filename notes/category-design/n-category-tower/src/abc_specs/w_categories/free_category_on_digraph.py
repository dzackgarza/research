# Origin: gitclones/integral_lattice/cat/src/abc_specs/w_categories/free_category_on_digraph.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, sections R3/R4). Content below is unmodified.
#
# This is a DESIGN RECORD: it states an intended interface, not the built
# preamble. Divergences and recorded errors are listed in the INDEX.md of
# this corpus.

"""
Free Category on Digraph: F(G) where G is a Sage DiGraph.

The free category on a digraph is the universal category containing G:
- Objects (0-cells) = Vertices of G
- Morphisms (1-cells) = Paths in G (composition = path concatenation)
- 2-cells = Trivial (free categories are 1-categories)

The DiGraph G is a Sage object (sage.graphs.digraph.DiGraph).
"""

from __future__ import annotations

from src.local_typing import *
from dataclasses import dataclass

from src._types import CategoryABCs, SageType


# =============================================================================
# 0-cells: Free Category (as object in wCat)
# =============================================================================


@dataclass
class _FreeCategory_ABC(CategoryABCs.Nontrivial_TwoCategory, ABC):
    """
    F(G): The free category on a directed graph G.

    G is a Sage DiGraph. This category has:
    - Objects: vertices of G
    - Morphisms: directed paths in G (via standard cell `path()` method)
    - Composition: path concatenation

    Universal property: For any category C and graph morphism φ: G → U(C),
    there is a unique functor F: F(G) → C such that U(F) ∘ η = φ.
    """

    @classmethod
    @final
    @abstractmethod
    def from_digraph(cls, 
        G: SageType.DiGraph, 
        name: str
    ) -> Self:
        """
        Construct the free category on a digraph.

        Parameters:
        - G: The directed graph as a Sage DiGraph.
        - name: Optional name for the category (default: "F(G)").

        Returns:
        - The free category F(G) on the given digraph G.
        """
        ...

    @classmethod
    def from_vertices_edges(cls, 
        vertices: Sequence[Any], 
        edges: Sequence[tuple[Any, Any]], 
        name: str
    ) -> Self:
        """
        Construct the free category on a digraph from vertices and edges.

        Parameters:
        - vertices: List of vertex labels.
        - edges: List of edge tuples (source, target).
        - name: Optional name for the category (default: "F(G)").

        Returns:
        - The free category F(G) on the given digraph G.
        """
        ...

    @classmethod
    def from_vertices_edges_relationship(cls, 
        vertices: Sequence[str], 
        edges: Sequence[tuple[str, tuple[str, str]]], 
        relations: Sequence[tuple[str, tuple[list[str], list[str]]]], 
        name: str
    ) -> Self:
        """
        Construct the free category on a digraph from vertices and edges, and impose relations.

        Parameters:
        - vertices: List of vertex labels v_i
        - edges: List of tuples of edge labels e_{ij} and source-target pairs (v_i, v_j)
        - relations: A list of relations, formatted as tuples of labels R_{IJKL} and source-target pairs of lists of edges 
        (source = [e_{i_1 j_1}, e_{i_2 j_2}, ...], target = [e_{k_1 l_1}, e_{k_2 l_2}, ...])
        - name: Name for this category.

        """
        ...

    @final
    @abstractmethod
    def extend_functor(
        self,
        target: CategoryABCs.Nontrivial_TwoCategory,
        object_map: dict[_FreeCategory_Object_ABC, CategoryABCs.Object],
        generator_map: dict[_FreeCategory_1Cell_ABC, CategoryABCs.OneMorphism],
    ) -> CategoryABCs.Functor:
        """
        Universal property: extend a graph morphism to a functor.

        Given:
        - object_map: V(G) → Ob(C)
        - generator_map: E(G) → Mor(C) (primitive 1-cells)

        Returns the unique functor F(G) → C extending this data.
        """
        ...


# =============================================================================
# 0-cells within F(G): Vertices of G
# =============================================================================


@dataclass
class _FreeCategory_Object_ABC(CategoryABCs.Object, ABC):
    """
    A 0-cell (object) in the free category F(G).

    Corresponds to a vertex of the underlying digraph G.
    """

# =============================================================================
# 1-cells: Paths in G (accessed via inherited path() method)
# =============================================================================


@dataclass
class _FreeCategory_1Cell_ABC(CategoryABCs.PlainOneMorphism, ABC):
    """
    A 1-cell (morphism) in the free category F(G).

    Corresponds to a directed path in G. The path data is accessible
    via the inherited `path()` method, and primitive cells via `decompose()`.
    """
    ...


@dataclass
class _FreeCategory_Endo1Cell_ABC(_FreeCategory_1Cell_ABC, CategoryABCs.EndoOneMorphism, ABC):
    """An endo-1-cell in F(G): a path from a vertex v back to itself."""
    ...


@dataclass
class _FreeCategory_Auto1Cell_ABC(_FreeCategory_Endo1Cell_ABC, CategoryABCs.AutoOneMorphism, ABC):
    """
    An auto-1-cell in F(G).

    In a free category, only identity paths are automorphisms.
    """

    pass


# =============================================================================
# 2-cells: Trivial (free categories are 1-categories)
# =============================================================================


@dataclass
class _FreeCategory_2Cell_ABC(CategoryABCs.PlainTwoMorphism, ABC):
    """
    A 2-cell in F(G).

    Free categories are 1-categories, so 2-cells are trivial (identity only).
    """
    ...


# Re-exports
_ = _FreeCategory_ABC
_ = _FreeCategory_Object_ABC
_ = _FreeCategory_1Cell_ABC
_ = _FreeCategory_Endo1Cell_ABC
_ = _FreeCategory_Auto1Cell_ABC
_ = _FreeCategory_2Cell_ABC
