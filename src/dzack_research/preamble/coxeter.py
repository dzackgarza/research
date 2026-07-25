r"""Coxeter diagrams and Gram matrices, and the hand-placed Sterk layouts.

Ported from the old init.sage. The diagram/matrix conversions are faithful; the
vertex colouring convention (norm $-4$ white, norm $-2$ black) is the old file's and
is preserved, including its assertion that every vertex gets exactly one colour.
"""

from __future__ import annotations

from typing import Any

from sage.graphs.graph import Graph
from sage.matrix.special import zero_matrix
from sage.rings.integer_ring import ZZ

__all__ = [
    "CROSS_CHECK_RECIPES",
    "DIAGRAM_CONVENTION",
    "STERK_POSITIONS",
    "root_intersection_matrix",
    "coxeter_diagram",
    "graph_to_matrix",
    "matrix_to_quiver",
    "plot_coxeter_diagram",
]

#: Vertex fill colours by root norm, as the old file chose them.
_WHITE = "#F8F9FE"
_BLACK = "#BFC9CA"

#: The full diagram convention, recovered from old lines 713-717. ``coxeter_diagram``
#: implements the node half; the edge and arrow rules are recorded here because the
#: source stated them and they are needed to read the diagrams correctly.
DIAGRAM_CONVENTION: dict[str, str] = {
    "white node": "root of norm -4",
    "black node": "root of norm -2",
    "double line, white to black": "r_i . r_j = 2",
    "single line, white to white": "r_i . r_j = 2",
    "arrow direction": "points from the -4 node to the -2 node",
}


def matrix_to_quiver(gram: Any) -> Any:
    """Every nonzero entry becomes an edge labelled by that entry, loops included."""
    graph = Graph(loops=True)
    for i in range(gram.ncols()):
        for j in range(gram.ncols()):
            entry = gram[i, j]
            if entry != 0:
                graph.add_edge(i, j, str(entry))
    return graph


def graph_to_matrix(graph: Any) -> Any:
    """Symmetric integer matrix from an edge-labelled graph."""
    size = len(graph.vertices())
    gram = zero_matrix(ZZ, size)
    for i, j, label in graph.edges():
        gram[i, j] = label
        gram[j, i] = label
    return gram


def coxeter_diagram(gram: Any) -> Any:
    r"""Coxeter diagram of a root configuration, coloured by root norm.

    Diagonal $-4$ gives a white vertex, $-2$ a black one; only *positive*
    off-diagonal entries become edges. Asserts every vertex received a colour, so a
    Gram matrix with an unexpected diagonal norm fails loudly instead of silently
    producing an uncoloured diagram.
    """
    size = gram.ncols()
    graph = Graph()
    colors: dict[str, list[int]] = {_WHITE: [], _BLACK: []}

    for i in range(size):
        for j in range(size):
            entry = gram[i, j]
            if i == j:
                if entry == -4:
                    colors[_WHITE].append(i)
                elif entry == -2:
                    colors[_BLACK].append(i)
                continue
            if entry > 0:
                graph.add_edge(i, j, str(entry))

    colored = len(colors[_WHITE]) + len(colors[_BLACK])
    assert colored == size, f"{size - colored} vertex/vertices had a diagonal norm other than -4 or -2, so the diagram would be partly uncoloured"
    graph.vertex_colors = colors
    return graph


def root_intersection_matrix(vectors: Any, bilinear_form: Any) -> Any:
    r"""Gram matrix of a root configuration, with the source's own validation.

    Ported from old lines 300-318. The source wrote this validator and then, in the
    Sterk section, never called it -- but its assertions are the correct ones and are
    kept: the matrix is symmetric, its diagonal lies in $\{-2, -4\}$, and each
    diagonal entry really is the square norm of the corresponding vector.

    The ``labels`` parameter the original took was unused in its body; dropped.
    """
    from sage.matrix.constructor import matrix as _matrix

    size = len(vectors)
    gram = _matrix(ZZ, [[bilinear_form(vectors[i], vectors[j]) for j in range(size)] for i in range(size)])
    assert gram.is_symmetric(), "root intersection matrix must be symmetric"
    assert set(gram.diagonal()) <= {-2, -4}, f"diagonal must be root norms -2 or -4, found {sorted(set(gram.diagonal()))}"
    for i in range(size):
        assert gram[i, i] == bilinear_form(vectors[i], vectors[i]), f"diagonal entry {i} disagrees with the vector's own square norm"
    return gram


def plot_coxeter_diagram(graph: Any, vertex_labels: Any, pos: Any = None) -> Any:
    """Render a diagram from :func:`coxeter_diagram`, optionally at fixed positions.

    Returns the plot rather than calling ``display`` as the old file did: a bare
    ``display`` only works inside a kernel, and returning lets a caller show it,
    save it, or compose it.
    """
    labels = dict(enumerate(vertex_labels))
    options = {
        "edge_labels": True,
        "vertex_labels": labels,
        "vertex_size": 200,
        "vertex_colors": graph.vertex_colors,
    }
    if pos:
        options["pos"] = pos
    return graph.plot(**options)


#: Sage invocations the source kept commented at old lines 930-940 as cross-checks for
#: the diagrams: independent routes to the same Coxeter/Dynkin data. Kept as reference
#: strings rather than executed, which is how the source held them.
CROSS_CHECK_RECIPES: tuple[str, ...] = (
    "G = Graph([(1, 2, 3)]); CoxeterMatrix(G)",
    "W = WeylGroup(['B', 3]); s = W.simple_reflections()",
    "(w = s[1]*s[2]*s[3]).canonical_matrix(); w.reduced_word()",
    "W = CoxeterGroup(['H', 3], implementation='reflection'); G = W.coxeter_diagram()",
    "R = RootSystem('A2xB2xF4'); DynkinDiagram(R)",
)

#: Hand-placed vertex coordinates for the Sterk diagrams, ported verbatim. These are
#: presentation choices with no mathematical content -- they exist so the printed
#: diagrams match the ones in the write-up.
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

#: Root counts the old file recorded per Sterk case, in its section headers
#: ("Sterk 1: 12 roots", ...). Kept as the checkable claim those comments were
#: making: a ported diagram whose vertex count disagrees is wrong.
STERK_ROOT_COUNTS: dict[str, int] = {
    "Sterk_1": 12,
    "Sterk_2": 10,
    "Sterk_3": 12,
    "Sterk_4": 11,
    "Sterk_5": 14,
}
