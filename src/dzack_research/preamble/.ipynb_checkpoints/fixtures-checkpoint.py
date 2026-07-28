r"""Static matrices, coordinates, names, and recorded results.

EXAMPLES::

    sage: from dzack_research.preamble.fixtures import BONDS, STERK_ROOT_COUNTS
    sage: BONDS["bond1"]
    [ 2 -1]
    [-1  2]
    sage: STERK_ROOT_COUNTS["Sterk_5"]
    14
"""

from __future__ import annotations

from typing import Any

from sage.matrix.constructor import matrix
from sage.rings.integer_ring import ZZ

__all__ = [
    "BONDS",
    "CITATIONS",
    "COMPUTED_ROOT_COUNTS",
    "COXETER_BLACK",
    "COXETER_WHITE",
    "CROSS_CHECK_RECIPES",
    "DIAGRAM_CONVENTION",
    "INVOLUTION_IMAGES",
    "K3_BASIS_NAMES",
    "L20_BASIS_NAMES",
    "L20_DUAL_NAMES",
    "RECORDED_RESULTS",
    "RECORDED_ROOT_MATRIX_ROWS",
    "STERK_POSITIONS",
    "STERK_PUBLISHED",
    "STERK_ROOT_COUNTS",
    "TEN_BASIS_NAMES",
    "TEN_DUAL_NAMES",
    "TWO_ELEMENTARY_8_6_0_INVARIANTS",
    "TWO_ELEMENTARY_BUILDING_BLOCKS",
    "UNBUILT_TWO_ELEMENTARY",
]


BONDS: dict[str, Any] = {
    "bond1": matrix(ZZ, 2, [2, -1, -1, 2]),
    "bond2": matrix(ZZ, 2, [2, -1, -1, 1]),
    "bond3": matrix(ZZ, 2, [6, -3, -3, 2]),
    "heavy_oriented": matrix(ZZ, 2, [4, -2, -2, 1]),
    "heavy_unoriented": matrix(ZZ, 2, [1, -1, -1, 1]),
}

COXETER_WHITE = "#F8F9FE"
COXETER_BLACK = "#BFC9CA"

DIAGRAM_CONVENTION: dict[str, str] = {
    "white node": "root of norm -4",
    "black node": "root of norm -2",
    "double line, white to black": "r_i . r_j = 2",
    "single line, white to white": "r_i . r_j = 2",
    "arrow direction": "points from the -4 node to the -2 node",
}

CROSS_CHECK_RECIPES: tuple[str, ...] = (
    "G = Graph([(1, 2, 3)]); CoxeterMatrix(G)",
    "W = WeylGroup(['B', 3]); s = W.simple_reflections()",
    "(w = s[1]*s[2]*s[3]).canonical_matrix(); w.reduced_word()",
    "W = CoxeterGroup(['H', 3], implementation='reflection'); G = W.coxeter_diagram()",
    "R = RootSystem('A2xB2xF4'); DynkinDiagram(R)",
)

STERK_POSITIONS: dict[str, dict[int, list[float]]] = {
    "Sterk_1": {
        0: [0, 0],
        1: [4, 0],
        2: [8, 0],
        3: [8, -4],
        4: [8, -8],
        5: [4, -8],
        6: [0, -8],
        7: [0, -4],
        8: [2, -6],
        9: [3.25, -4.75],
        10: [4.5, -3.5],
        11: [6, -2],
    },
    "Sterk_2": {
        0: [0, 0],
        1: [-4, 0],
        2: [-8, 0],
        3: [-7, 4],
        4: [-6, 8],
        5: [-5, 12],
        6: [-4, 16],
        7: [-3, 20],
        8: [-2, 24],
        9: [-2, 6],
    },
    "Sterk_3": {
        0: [0, -4],
        1: [0, 4],
        2: [0, 8],
        3: [0, 12],
        4: [0, 16],
        5: [4, 16],
        6: [8, 16],
        7: [12, 16],
        8: [20, 16],
        9: [4, 12],
        10: [6, 2],
        11: [14, 10],
    },
    "Sterk_4": {
        0: [0, 0],
        1: [0, 4],
        2: [0, 8],
        3: [4, 8],
        4: [8, 8],
        5: [12, 8],
        6: [16, 8],
        7: [16, 4],
        8: [16, 0],
        9: [4, 4],
        10: [12, 4],
    },
    "Sterk_5": {
        0: [0, 0],
        1: [10, 0],
        2: [20, 0],
        3: [20, -10],
        4: [20, -20],
        5: [10, -20],
        6: [0, -20],
        7: [0, -10],
        8: [4, -4],
        9: [16, -4],
        10: [16, -16],
        11: [4, -16],
        12: [8, -8],
        13: [8, -12],
    },
}

STERK_ROOT_COUNTS: dict[str, int] = {
    "Sterk_1": 12,
    "Sterk_2": 10,
    "Sterk_3": 12,
    "Sterk_4": 11,
    "Sterk_5": 14,
}

STERK_PUBLISHED: dict[str, dict[str, int]] = {
    "Sterk_1": {"total": 12, "norm_-4": 12, "norm_-2": 0},
    "Sterk_2": {"total": 10, "norm_-4": 9, "norm_-2": 1},
    "Sterk_3": {"total": 12, "norm_-4": 10, "norm_-2": 2},
    "Sterk_4": {"total": 11, "norm_-4": 9, "norm_-2": 2},
    "Sterk_5": {"total": 14, "norm_-4": 10, "norm_-2": 4},
}

COMPUTED_ROOT_COUNTS: dict[str, dict[str, Any]] = {
    "Sterk_1": {"julia": 9, "vinal": 10, "ideal_vertices": 1},
    "Sterk_2": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
    "Sterk_3": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
    "Sterk_4": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
    "Sterk_5": {"julia": 10, "vinal": 10, "ideal_vertices": 2},
}

K3_BASIS_NAMES: tuple[str, ...] = (
    ("v1", "v2", "u1", "u2", "up1", "up2")
    + tuple(f"e{i}" for i in range(1, 9))
    + tuple(f"ep{i}" for i in range(1, 9))
)

INVOLUTION_IMAGES: dict[str, tuple[tuple[str, int], ...]] = {
    "I_dP": tuple(
        [("v1", -1), ("v2", -1), ("up1", 1), ("up2", 1), ("u1", 1), ("u2", 1)]
        + [(f"e{i}", -1) for i in range(1, 9)]
        + [(f"ep{i}", -1) for i in range(1, 9)]
    ),
    "I_En": tuple(
        [("v1", -1), ("v2", -1), ("up1", 1), ("up2", 1), ("u1", 1), ("u2", 1)]
        + [(f"ep{i}", 1) for i in range(1, 9)]
        + [(f"e{i}", 1) for i in range(1, 9)]
    ),
    "I_Nik": tuple(
        [("v1", 1), ("v2", 1), ("u1", 1), ("u2", 1), ("up1", 1), ("up2", 1)]
        + [(f"ep{i}", -1) for i in range(1, 9)]
        + [(f"e{i}", -1) for i in range(1, 9)]
    ),
}

L20_BASIS_NAMES: tuple[str, ...] = tuple(
    ["e", "f", "ep", "fp"]
    + [f"a{i}" for i in range(1, 9)]
    + [f"a{i}t" for i in range(1, 9)]
)
L20_DUAL_NAMES: tuple[str, ...] = tuple(
    ["eb", "fb", "epb", "fpb"]
    + [f"w{i}" for i in range(1, 9)]
    + [f"w{i}t" for i in range(1, 9)]
)
TEN_BASIS_NAMES: tuple[str, ...] = tuple(
    ["e", "f", "ep", "fp"] + [f"a{i}" for i in range(1, 9)]
)
TEN_DUAL_NAMES: tuple[str, ...] = tuple(
    ["ed", "fd", "epd", "fpd"] + [f"w{i}" for i in range(1, 9)]
)

RECORDED_ROOT_MATRIX_ROWS: tuple[tuple[int, ...], ...] = (
    (0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
    (0, 2, 0, 0, -2, -1, -4, -3, -2, -1),
    (1, -1, 0, 0, 0, 0, 0, 0, 0, 0),
    (4, 4, 0, 0, -10, -5, -21, -17, -13, -9),
    (-6, -6, 1, 0, 16, 7, 31, 25, 19, 13),
)

RECORDED_RESULTS: dict[str, str] = {
    "IIPQ(1,17).root_system.num_facets": "19 (mod W)",
    "IIPQ(1,17).root_system.num_rays": "82 (mod W)",
    "J_perp_mod_J": "A17, D10 + E7, E8^2 + A1, D16 + A1",
}

CITATIONS: dict[str, str] = {
    "IIPQ(1,17) root system": "https://arxiv.org/pdf/2002.07127#page=12",
    "LK3_2 Vinberg roots": "https://arxiv.org/pdf/1903.09742#page=22",
}

TWO_ELEMENTARY_8_6_0_INVARIANTS: dict[str, Any] = {
    "rank": 8,
    "signature_pair": (0, 8),
    "determinant": 64,
    "discriminant_group_order": 64,
    "construction": "index-2 overlattice of A1^8",
    "derivation": "TEn.I_perp_mod_I([ep, 2e+2f+2w1])",
    "reference": "AE22 (arXiv:2208.10383), Alexeev-Engel",
    "not_isometric_to": ("D4+A1^4 (same rank and determinant)",),
}

TWO_ELEMENTARY_BUILDING_BLOCKS: tuple[tuple[str, str, str], ...] = (
    ("<2>", "(1,1,1)", "Z(2)"),
    ("U", "(2,0,0)", "hyperbolic plane"),
    ("U(2)", "(2,2,0)", "hyperbolic plane, scaled"),
    ("B_n(2)", "(n,n,1)", "for n >= 2"),
    ("C_4n", "(4n,2,0)", "for 4n >= 8"),
    ("C_{4n+2}", "(4n+2,2,1)", "for 4n+2 >= 6"),
    ("F4", "(4,2,0)", ""),
    ("E7", "(7,1,1)", ""),
    ("E8", "(8,0,0)", "unimodular"),
    ("E8(2)", "(8,8,0)", ""),
)

UNBUILT_TWO_ELEMENTARY: tuple[str, ...] = tuple(
    [f"({n},{n},1)" for n in range(2, 21)]
    + ["(8,2,0)", "(16,2,0)", "(24,2,0)", "(6,2,1)", "(10,2,1)", "(14,2,1)"]
    + ["(18,2,1)", "(22,2,1)", "(4,2,0)", "(7,1,1)"]
)
