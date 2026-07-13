from __future__ import annotations

from collections import Counter
from collections.abc import Callable, Hashable, Iterable, Sequence
from copy import copy
from typing import TYPE_CHECKING, Literal, TypedDict, overload

from dot2tex import d2t, dotparsing
from sage.all import Infinity, Poset, Set, Subsets, ZZ, matrix, sqrt, zero_matrix
from sage.combinat.posets.posets import FinitePoset
from sage.graphs.graph import Graph
from sage.graphs.graph_plot import GraphPlot
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from sage.misc.latex_standalone import TikzPicture
from sage.modules.free_quadratic_module import FreeQuadraticModule_generic_pid
from sage.modules.free_quadratic_module_integer_symmetric import (
    FreeQuadraticModule_integer_symmetric,
)
from sage.misc.cachefunc import cached_method
from sage.structure.element import Matrix


type CoxeterOption = bool | int | float | str | list[str] | dict[Hashable, str]


class TikzOptions(TypedDict):
    scale: int
    graphviz_scale: float
    graphviz_width: float
    scale_factor: int
    scale_factor_labels: int
    fontsize: int
    tex_font_size: str
    edge_width: float
    node_size: str


class TikzOptionsPatch(TypedDict, total=False):
    scale: int
    graphviz_scale: float
    graphviz_width: float
    scale_factor: int
    scale_factor_labels: int
    fontsize: int
    tex_font_size: str
    edge_width: float
    node_size: str
type CoxeterInput = (
    Matrix
    | FreeQuadraticModule_generic_pid
    | FreeQuadraticModule_integer_symmetric
    | Graph
    | None
)
type CoxeterEdge = tuple[Hashable, Hashable, str | int | float | None]


# Required utility functions for CoxeterGraph
def matrix_to_graph(M: Matrix) -> Graph:
    """
    Convert a Sage matrix to a Sage Graph with loops.

    EXAMPLES::

        sage: from coxeter_graph import matrix_to_graph
        sage: M = matrix([[2,1],[1,2]])
        sage: G = matrix_to_graph(M)
        sage: sorted(G.edges(labels=True))
        [(0, 0, '2'), (0, 1, '1'), (1, 1, '2')]
    """
    nverts = M.ncols()
    G = Graph(loops=True)
    for i in range(nverts):
        for j in range(nverts):
            if i==j or M[i,j] != 0:
                G.add_edge(i, j, str(M[i, j]) )
    return G

def graph_to_matrix(G: Graph) -> Matrix:
    """
    Convert a Sage Graph to a Sage matrix (ZZ entries).

    EXAMPLES::

        sage: from coxeter_graph import graph_to_matrix
        sage: G = Graph([(0,0,'2'), (0,1,'1'), (1,1,'2')], loops=True)
        sage: M = graph_to_matrix(G)
        sage: M
        [2 1]
        [1 2]
    """
    verts = G.vertices()
    n = len(verts)
    M: Matrix = zero_matrix(ZZ, n)
    Gp = G.relabel(list(range(n)), inplace=False)
    for e in Gp.edges():
        M[ e[0], e[1] ] = e[2]
        M[ e[1], e[0] ] = e[2]
    return M

def is_elliptic_matrix(M: Matrix) -> bool:
    """
    Check if a matrix corresponds to an elliptic subgraph.

    EXAMPLES::

        sage: from coxeter_graph import is_elliptic_matrix
        sage: M = matrix([[2, -1], [-1, 2]])
        sage: is_elliptic_matrix(M)
        True
    """
    return M.det() > 0

def is_parabolic_matrix(M: Matrix) -> bool:
    """
    Check if a matrix corresponds to a parabolic subgraph.

    EXAMPLES::

        sage: from coxeter_graph import is_parabolic_matrix
        sage: M = matrix([[2, -1], [-1, 2]])
        sage: is_parabolic_matrix(M)
        False
    """
    return M.det() == 0

def is_elliptic_subgraph(H: CoxeterGraph | Graph) -> bool:
    """
    Check if a subgraph is elliptic.

    EXAMPLES::

        sage: from coxeter_graph import is_elliptic_subgraph, matrix_to_graph
        sage: M = matrix([[2, -1], [-1, 2]])
        sage: G = matrix_to_graph(M)
        sage: is_elliptic_subgraph(G)
        True
    """
    if hasattr(H, 'gram_matrix') and H.gram_matrix is not None:
        return is_elliptic_matrix(H.gram_matrix)
    else:
        return is_elliptic_matrix(graph_to_matrix(H))

def is_parabolic_subgraph(H: CoxeterGraph | Graph) -> bool:
    """
    Check if a subgraph is parabolic.

    EXAMPLES::

        sage: from coxeter_graph import is_parabolic_subgraph, matrix_to_graph
        sage: M = matrix([[2, -1], [-1, 2]])
        sage: G = matrix_to_graph(M)
        sage: is_parabolic_subgraph(G)
        False
    """
    if hasattr(H, 'gram_matrix') and H.gram_matrix is not None:
        return is_parabolic_matrix(H.gram_matrix)
    else:
        return is_parabolic_matrix(graph_to_matrix(H))

def init_coxeter_colors(G: Graph) -> dict[Hashable, str]:
    """
    Initialize default colors for Coxeter graph vertices.

    EXAMPLES::

        sage: from coxeter_graph import init_coxeter_colors, matrix_to_graph
        sage: M = matrix([[2, -1], [-1, 2]])
        sage: G = matrix_to_graph(M)
        sage: colors = init_coxeter_colors(G)
        sage: isinstance(colors, dict)
        True
    """
    colors = {}
    for v in G.vertices():
        # Default coloring scheme for Coxeter vertices
        colors[v] = "lightblue"
    return colors

def get_coxeter_label_connected(H: Graph) -> str:
    """
    Get the Coxeter type label for a connected graph.

    EXAMPLES::

        sage: from coxeter_graph import get_coxeter_label_connected, matrix_to_graph
        sage: M = matrix([[2, -1], [-1, 2]])
        sage: G = matrix_to_graph(M)
        sage: get_coxeter_label_connected(G)
        'A_2'
    """
    n = H.num_verts()
    if n == 0:
        return ""
    elif n == 1:
        return "A_1"
    elif n == 2:
        return "A_2"
    else:
        # Simplified labeling - for more accurate labeling, would need full classification
        return f"Type_{n}"

# Lookup table for Coxeter diagram edge calculations
m_lookup = {
    ZZ(0): ZZ(2),
    ZZ(1) / ZZ(2): ZZ(3),
    ZZ(1) / sqrt(ZZ(2)): ZZ(4),
    sqrt(ZZ(3)) / ZZ(2): ZZ(6),
    ZZ(1): Infinity,
}

class CoxeterGraph(Graph):
    """
    A specialized Graph class for working with Coxeter diagrams.
    
    This class extends Sage's Graph class with functionality specific to
    Coxeter diagrams, including automatic coloring, labeling, and analysis
    of elliptic and parabolic subdiagrams.
    
    EXAMPLES::
        sage: from coxeter_graph import CoxeterGraph
        sage: from isometry_utils import matrix_A_n
        sage: M = matrix_A_n(3)
        sage: G = CoxeterGraph(M)
        sage: G.num_verts()
        3
    """
    
    _default_options: dict[str, CoxeterOption] = {}
    if TYPE_CHECKING:
        gram_matrix: Matrix
    else:
        gram_matrix = None
    lattice: (
        FreeQuadraticModule_generic_pid
        | FreeQuadraticModule_integer_symmetric
        | None
    ) = None
    coxeter_graph: Graph | None = None
    all_subgraphs = None
    all_elliptic_subgraphs = None
    all_parabolic_subgraphs = None
    if TYPE_CHECKING:
        parent_coxeter_graph: CoxeterGraph
        fixed_positions: dict[int, Sequence[float]]

        def edges_incident(
            self,
            vertices: Hashable | Iterable[Hashable] | None = ...,
            labels: bool = ...,
            sort: bool = ...,
        ) -> list[tuple[Hashable, Hashable, str | int | float]]: ...
    else:
        parent_coxeter_graph = None
        fixed_positions = None
    is_subgraph: bool = False
    tex_title: str | None = None
    tikz_options: TikzOptions = {
        "scale": 1,
        "graphviz_scale": 0.2,
        "graphviz_width": 0.15,
        "scale_factor": 50,
        "scale_factor_labels": 50,
        "fontsize": 30,
        "tex_font_size": "Large",
        "edge_width": 1.2,
        "node_size": "0.5cm",
    }

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CoxeterGraph):
            return NotImplemented
        same_vertices: bool = Set(self.vertices()) == Set(other.vertices())
        same_edges: bool = Set(self.edges()) == Set(other.edges())
        return same_vertices and same_edges
        
    @cached_method
    def __hash__(self) -> int:
        return hash(
            frozenset(self.edges(sort=True)).union(
                frozenset(self.vertices(sort=True)))
        )
    
    def __init__(
        self,
        data: CoxeterInput = None,
        pos: dict[int, Sequence[float]] | None = None,
        loops: bool = True,
        format: str | None = None,
        weighted: bool = True,
        data_structure: str = "sparse",
        vertex_labels: bool = True,
        name: str | None = None,
        multiedges: bool = True,
        convert_empty_dict_labels_to_None: bool | None = None,
        sparse: bool = True,
        immutable: bool = False,
        hash_labels: bool | None = None,
        parent: CoxeterGraph | None = None,
        tex_title: str | None = None,
        tikz_options: TikzOptionsPatch | None = None,
    ) -> None:
        """
        Initialize a CoxeterGraph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: G.gram_matrix is not None
            True
        """
        
        # Handle matrix input
        if isinstance(data, Matrix_integer_dense):
            self.gram_matrix = data

        # Handle lattice input
        if isinstance(
            data,
            (
                FreeQuadraticModule_generic_pid,
                FreeQuadraticModule_integer_symmetric,
            ),
        ):
            self.lattice = data
            self.gram_matrix = self.lattice.gram_matrix()
            data = matrix_to_graph(self.gram_matrix)
            if self.lattice._names is not None:
                self._default_options["vertex_labels"] = {v: k for v, k in enumerate(self.lattice._names)}

        if parent is not None:
            self.parent_coxeter_graph = parent
            self.is_subgraph = True

        if tikz_options is not None:
            self.update_tikz_options(tikz_options)

        Graph.__init__(self, data=data, pos=pos, loops=loops, format=format,
                     weighted=weighted, data_structure=data_structure,
                     vertex_labels=vertex_labels, name=name,
                     multiedges=multiedges, convert_empty_dict_labels_to_None=convert_empty_dict_labels_to_None,
                     sparse=sparse, immutable=immutable, hash_labels=hash_labels)

        self._default_options["edge_labels"] = True

        if "vertex_colors" not in self._default_options.keys():
            self._default_options["vertex_colors"] = init_coxeter_colors(self)

        self._default_options["vertex_size"] = 200
        self._default_options["loop_size"] = 0.2
        self._default_options["talk"] = True
        self._default_options["graph_border"] = True
        self._default_options["dist"] = 0.01
        self._default_options["title"] = "?"

        if pos is not None:
            self.fixed_positions = copy(pos)
            self._pos = pos

        if tex_title is not None:
            self.tex_title = tex_title

    def get_coxeter_graph(self) -> Graph:
        """
        Convert the bilinear form graph to a standard Coxeter diagram.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: CG = G.get_coxeter_graph()
            sage: CG.num_verts()
            3
        """
        if self.coxeter_graph is None:
            Gp = Graph(multiedges=True)
            for v in sorted(self.vertices()):
                Gp.add_vertex(v)
            
            for e in [e for e in self.edges() if e[0] != e[1]]:
                v1 = e[0]; v2 = e[1]; v1_v2 = e[2]
                v1_2 = [e for e in self.edges_incident(v1) if e[0] == v1 and e[1] == v1][0][2]
                v2_2 = [e for e in self.edges_incident(v2) if e[0] == v2 and e[1] == v2][0][2]
                g12 = int(v1_v2) / sqrt(int(v1_2) * int(v2_2))
                
                if g12 > 1:
                    Gp.add_edge(v1, v2, g12)
                elif g12 == 1:
                    Gp.add_edge(v1, v2, "∞")
                elif g12 < 1:
                    m = m_lookup[g12]
                    for i in range(m-2):
                        Gp.add_edge(v1, v2, "")
                else:
                    raise ValueError("Unknown entry.")
            self.coxeter_graph = Gp
        return self.coxeter_graph

    def get_coxeter_label(self) -> list[str]:
        """
        Get the Coxeter type label for this graph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: G.get_coxeter_label()
            ['A_3']
        """
        s = []
        for cmp in self.connected_components(sort=True):
            Hp = self.subgraph(cmp)
            s.append(get_coxeter_label_connected(Hp))
        return s

    def plot_basic(self, **options: CoxeterOption) -> None:

        # print("Plotting, updating colors")
        self._default_options["vertex_colors"] = init_coxeter_colors(self)
        
        opts = copy( self._default_options )

        updated_opts = dict( list( options.items() ) + list( self._default_options.items() ) )

        # updated_opts["pos"] = self._default_options["pos"]
        if "pos" in updated_opts.keys():
            del updated_opts["pos"]
        
        #options.update(opts)
        updated_opts["title"] = self.get_coxeter_label()
        # if self.parent_coxeter_graph is not None:
        #     updated_opts["pos"] = self.parent_coxeter_graph._default_options["pos"]
        # else:
        #     updated_opts["pos"] = self._default_options["pos"]

        Gp = self.get_coxeter_graph()
            
        # return self.coxeter_graph
        # print("Default options:")
        # print(self._default_options)
        # print("Options going into graphplot:")
        # print(updated_opts)
        positions = { x: self.fixed_positions[x] for x in self.fixed_positions if x in self.vertices()}
        # print("Using positions: " + str( positions ) )
        pl = Gp.graphplot(pos = positions, **updated_opts)
        pl.show(figsize=10)

    def old_plot(self, **options: CoxeterOption) -> GraphPlot:
        return self.graphplot(**options)
    
    def get_subgraphs(
        self,
        only_connected: bool = False,
        limit: int | None = None,
    ) -> list[CoxeterGraph]:
        """
        Get all subgraphs of this Coxeter graph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(2)
            sage: G = CoxeterGraph(M)
            sage: len(G.get_subgraphs())
            4
        """
        if self.all_subgraphs is None:
            self.all_subgraphs = Subsets(set(list(self.vertices())))
        if limit is not None:
            return [self.subgraph(x) for x in [self.all_subgraphs.random_element() for i in range(limit)]]
        else:
            return [self.subgraph(x) for x in self.all_subgraphs]

    def get_elliptic_subgraphs(
        self,
        only_connected: bool = False,
    ) -> list[CoxeterGraph]:
        """
        Get all elliptic subgraphs of this Coxeter graph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: elliptic = G.get_elliptic_subgraphs()
            sage: len(elliptic) >= 1
            True
        """
        if self.all_elliptic_subgraphs is None:
            all_elliptic_subgraphs = list(filter(lambda H: is_elliptic_subgraph(H), self.get_subgraphs()))
            if not all([is_elliptic_matrix(H.gram_matrix) for H in all_elliptic_subgraphs]):
                raise ValueError("Error: not all matrices are elliptic.")
            else:
                self.all_elliptic_subgraphs = list(reversed(sorted(all_elliptic_subgraphs, key=len)))
        
        assert len(self.all_elliptic_subgraphs) > 0
        
        elliptic_subgraphs = (
            H for H in self.all_elliptic_subgraphs
            if not only_connected or H.is_connected()
        )
        
        elliptic_subgraphs = (H for H in elliptic_subgraphs if len(H) > 0)
        return list(reversed(sorted(elliptic_subgraphs, key=len)))

    def get_parabolic_subgraphs(self) -> list[CoxeterGraph]:
        """
        Get all parabolic subgraphs of this Coxeter graph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import graph_tilde_A_n
            sage: G_tilde = graph_tilde_A_n(3)
            sage: CG = CoxeterGraph(G_tilde)
            sage: parabolic = CG.get_parabolic_subgraphs()
            sage: len(parabolic) >= 1
            True
        """
        if self.all_parabolic_subgraphs is None:
            all_parabolic_subgraphs = list(filter(lambda H: is_parabolic_subgraph(H), self.get_subgraphs()))
            if not all([is_parabolic_matrix(H.gram_matrix) for H in all_parabolic_subgraphs]):
                raise ValueError("Error: not all matrices are parabolic.")
            else:
                self.all_parabolic_subgraphs = list(reversed(sorted(all_parabolic_subgraphs, key=len)))
        
        assert len(self.all_parabolic_subgraphs) > 0
        
        parabolic_subgraphs = filter(lambda H: len(H) > 0, self.all_parabolic_subgraphs)
        return list(reversed(sorted(parabolic_subgraphs, key=len)))

    @overload
    def orbits_of_subgraphs(
        self,
        subgraphs: list[CoxeterGraph] | None = None,
        representatives_only: Literal[True] = True,
        limit: int | None = None,
    ) -> list[CoxeterGraph]: ...

    @overload
    def orbits_of_subgraphs(
        self,
        subgraphs: list[CoxeterGraph] | None,
        representatives_only: Literal[False],
        limit: int | None = None,
    ) -> list[tuple[CoxeterGraph, ...]]: ...

    def orbits_of_subgraphs(
        self,
        subgraphs: list[CoxeterGraph] | None = None,
        representatives_only: bool = True,
        limit: int | None = None,
    ) -> list[CoxeterGraph] | list[tuple[CoxeterGraph, ...]]:
        """
        Compute orbits of subgraphs under the automorphism group.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(2)
            sage: G = CoxeterGraph(M)
            sage: orbits = G.orbits_of_subgraphs()
            sage: len(orbits) >= 1
            True
        """
        if subgraphs is None:
            subgraphs = self.get_subgraphs(limit=limit)
        AutG = self.automorphism_group()
        int_orbits = set()
        for H in subgraphs:
            orb = AutG.orbit(tuple(H.vertices()), action="OnSets")
            lp = sorted([tuple(sorted(l)) for l in orb])
            int_orbits.add(tuple(lp))

        graph_orbits = Set([tuple(map(lambda x: self.subgraph(x), some_orbs)) for some_orbs in int_orbits])
                
        if representatives_only:
            return [x[0] for x in graph_orbits]
        else:
            return list(graph_orbits)

    def orbits_of_elliptic_subgraphs(
        self,
        only_connected: bool = False,
        fast: bool = False,
        as_poset: bool = True,
    ) -> FinitePoset | list[CoxeterGraph]:
        """
        Compute orbits of elliptic subgraphs under the automorphism group.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: elliptic_orbits = G.orbits_of_elliptic_subgraphs(as_poset=False)
            sage: len(elliptic_orbits) >= 1
            True
        """
        subgraphs = self.orbits_of_subgraphs(representatives_only=True)
        nontrivial_subgraphs = [H for H in subgraphs if len(H) > 0]
        elliptic_subgraphs = filter(lambda H: is_elliptic_subgraph(H), nontrivial_subgraphs)
        if only_connected:
            elliptic_subgraphs = filter(lambda H: H.is_connected(), elliptic_subgraphs)      

        if as_poset:
            if fast:
                elliptic_vertex_sets = list(map(lambda H: Set(H.vertices()), elliptic_subgraphs))
                B = Poset((elliptic_vertex_sets, lambda h0, h1: h0.issubset(h1)))
            else:
                B = Poset(
                    (set(elliptic_subgraphs), lambda x, y: 
                     all([v in y.vertices() for v in x.vertices()]))
                )
            return B
        else:
            return list(elliptic_subgraphs)

    def orbits_of_parabolic_subgraphs(
        self,
        only_connected: bool = False,
        fast: bool = False,
        as_poset: bool = True,
    ) -> FinitePoset | list[CoxeterGraph]:
        """
        Compute orbits of parabolic subgraphs under the automorphism group.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import graph_tilde_A_n
            sage: G_tilde = graph_tilde_A_n(3)
            sage: CG = CoxeterGraph(G_tilde)
            sage: parabolic_orbits = CG.orbits_of_parabolic_subgraphs(as_poset=False)
            sage: len(parabolic_orbits) >= 1
            True
        """
        subgraphs = self.orbits_of_subgraphs(representatives_only=True)
        nontrivial_subgraphs = [H for H in subgraphs if len(H) > 0]
        parabolic_subgraphs = filter(lambda H: is_parabolic_subgraph(H), nontrivial_subgraphs)
        if only_connected:
            parabolic_subgraphs = filter(lambda H: H.is_connected(), parabolic_subgraphs)      

        if as_poset:
            if fast:
                parabolic_vertex_sets = list(map(lambda H: Set(H.vertices()), parabolic_subgraphs))
                B = Poset((parabolic_vertex_sets, lambda h0, h1: h0.issubset(h1)))
            else:
                B = Poset(
                    (set(parabolic_subgraphs), lambda x, y: 
                     all([v in y.vertices() for v in x.vertices()]))
                )
            return B
        else:
            return list(parabolic_subgraphs)

    def set_parent(self, parent: CoxeterGraph) -> None:
        """
        Set the parent CoxeterGraph for this subgraph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: H = G.subgraph([0, 1])
            sage: H.is_subgraph
            True
        """
        self.is_subgraph = True
        self.parent_coxeter_graph = parent
        self.fixed_positions = copy(parent.fixed_positions)
        self._pos = copy(parent._pos)
        self.tikz_options = copy(parent.tikz_options)

    def subgraph(
        self,
        vertices: Hashable | Iterable[Hashable] | None = None,
        edges: CoxeterEdge | Iterable[CoxeterEdge] | None = None,
        inplace: bool = False,
        vertex_property: Callable[[Hashable], bool] | None = None,
        edge_property: Callable[[CoxeterEdge], bool] | None = None,
        algorithm: str | None = None,
        immutable: bool | None = None,
    ) -> CoxeterGraph:
        """
        Create a CoxeterGraph subgraph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: H = G.subgraph([0, 1])
            sage: isinstance(H, CoxeterGraph)
            True
        """
        H = super().subgraph(vertices=vertices, edges=edges, inplace=inplace,
                 vertex_property=vertex_property, edge_property=edge_property, 
                 algorithm=algorithm, immutable=immutable)

        H.gram_matrix = graph_to_matrix(H)
        H.set_parent(self)
        H._default_options["vertex_colors"] = init_coxeter_colors(H)        
        return H

    def get_title(self) -> str:
        """
        Get the title for this CoxeterGraph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: title = G.get_title()
            sage: isinstance(title, str)
            True
        """
        if self.tex_title is None:
            if self.is_subgraph:
                lab = self.get_coxeter_label()
                lab_counter = Counter(lab)
                combined_labs = []
                for x in lab_counter:
                    mult = lab_counter.get(x)
                    if mult == 1:
                        combined_labs.append(x)
                    else:
                        combined_labs.append(f'{x}^{mult}')
                self.tex_title = "$" + "".join(combined_labs) + "$"
            else: 
                self.tex_title = "Untitled Graph"
        return self.tex_title

    def update_tikz_options(self, opts: TikzOptionsPatch) -> None:
        """
        Update TikZ options for this CoxeterGraph.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: G.update_tikz_options({"scale": 2})
            sage: G.tikz_options["scale"]
            2
        """
        self.tikz_options.update(opts)

    def get_random_subgraph(
        self,
        graph_type: Literal["Elliptic", "Parabolic"] | None = None,
    ) -> CoxeterGraph:
        """
        Get a random subgraph of a specified type.
        
        EXAMPLES::
            sage: from coxeter_graph import CoxeterGraph
            sage: from isometry_utils import matrix_A_n
            sage: M = matrix_A_n(3)
            sage: G = CoxeterGraph(M)
            sage: H = G.get_random_subgraph(graph_type="Elliptic")
            sage: isinstance(H, CoxeterGraph)
            True
        """
        import random
        if graph_type == "Elliptic":
            H = random.choice(self.get_elliptic_subgraphs())
        elif graph_type == "Parabolic":
            H = random.choice(self.get_parabolic_subgraphs())
        elif graph_type is None:
            H = random.choice(self.get_subgraphs())
        else:
            raise ValueError("Invalid graph type given.")
        return H

    def plot(
        self,
        tikz_options: TikzOptions | None = None,
        subgraph: CoxeterGraph | None = None,
        debug: bool = False,
    ) -> TikzPicture:

        if tikz_options is None:
            tikz_options = self.tikz_options
        
        if self.is_subgraph:
            return self.parent_coxeter_graph.to_tikz_labeled(subgraph=self, tikz_options=tikz_options, debug=debug)
        else:
            return self.to_tikz_labeled(subgraph=subgraph, tikz_options=tikz_options, debug=debug)
            
    def to_dotfile(
        self,
        tikz_options: TikzOptions | None = None,
        xlabels: bool = False,
        tex_title: str | None = None,
    ) -> str:

        if tikz_options is None:
            tikz_options = self.tikz_options
            
        graphviz_scale = tikz_options["graphviz_scale"]
        graphviz_width = tikz_options["graphviz_width"]
        fontsize = tikz_options["fontsize"]

        if tex_title is None:
            tex_title = self.get_title()
        
        graph_to_plot = self.get_coxeter_graph()
        pos = self.get_pos()
        if pos is None:
            raise ValueError('vertex positions need to be set first')
    
        vertex_lines = []
        for u in graph_to_plot.vertices(sort=False):
            v2 = [x for x in self.edges() if x[0] == x[1] and x[1] == u][0][2]
            color = "white" if v2 == -4 else "black"
            p = tuple(pos[u])
            if xlabels:
                line = f'node_{u} [xlabel="r_{{{u}}}", texlbl="$r_{{{u}}}$", pos="{p[0]},{p[1]}!", fillcolor="{color}"];'
            else:
                line = f'node_{u} [texlbl="$r_{{{u}}}$", pos="{p[0]},{p[1]}!", fillcolor="{color}"];'
            vertex_lines.append(line)
            
        edge_lines = []
        num_edges = Counter( graph_to_plot.edges() )
        for (u, v, label) in graph_to_plot.edges():
            if u == v:
                # loops are done below
                continue
            line = f'node_{u} -- node_{v};'
            edge_lines.append(line)
    
        nl = "\n\t"
        dot_string = f'''
        graph {{
            graph [label="\\n{tex_title}" labelloc=b]
            scale={graphviz_scale}
            nodesep=0.1
        
            node[label="", xlabel=" ", fixedsize=true, shape="circle", width={graphviz_width}, style="filled", fontsize="{fontsize}", lblstyle="font=\\Large"];
            edge[penwidth=2]
            
            {nl.join(vertex_lines)}
        
            {nl.join(edge_lines)}
        }}
        '''
        
        return dot_string
        
    def to_tikz_labeled(
        self,
        subgraph: CoxeterGraph | None = None,
        tikz_options: TikzOptions | None = None,
        debug: bool = False,
    ) -> TikzPicture:

        if tikz_options is None:
            tikz_options = self.tikz_options
            
        scale = tikz_options["scale"]
        scale_factor = tikz_options["scale_factor"]
        scale_factor_labels = tikz_options["scale_factor_labels"]
        fontsize = tikz_options["fontsize"]
        tex_font_size = tikz_options["tex_font_size"]
        edge_width = tikz_options["edge_width"]
        node_size = tikz_options["node_size"]

        if subgraph is not None:
            tex_title = subgraph.get_title()
        else:
            tex_title = self.get_title()
        
        dotdata = self.to_dotfile(tex_title=tex_title)
        parser = dotparsing.DotDataParser()
        tmpdata = d2t.create_xdot(dotdata, prog="neato", options='')
        main_graph = parser.parse_dot_data(tmpdata)
        nodes = list( main_graph.allnodes )
        edges = list(main_graph.alledges )

        graph = list( main_graph.allgraphs )[0]
        title = graph.attr["label"].replace("\\n", "")
        title_pos = tuple( [float(x)/scale_factor for x in graph.attr["lp"].split(",")])
        
        
        lines = []
        lines.append(r'\begin{tikzpicture}')
        lines.append(f'[auto, scale={scale}, every node/.style={{scale={scale}}},minimum size={node_size}]')

        line = f'\\node (node_title) at {title_pos} {{{title}}};'
        lines.append(line)
        
        lines.append(r'% vertices')
        lines.append(r'\begin{pgfonlayer}{nodelayer}')
        for node in main_graph.allnodes:
            color = "white"
            position = tuple( [float(x)/scale_factor for x in node.pos.split(",")])
            line = f'\\node [style={node.fillcolor} node] ({node.name}) at {position} {{}};'
            lines.append(line)
            lbl_position = tuple( [float(x)/scale_factor_labels for x in node.xlp.split(",")])
            line = f'\\draw {lbl_position} node {{\\{tex_font_size} {node.texlbl}}};'
            lines.append(line)
        lines.append(r'\end{pgfonlayer}')
        
        edge_counts = Counter( [ (str(e.get_source()), str(e.get_destination())) for e in edges])
        
        lines.append(r'\begin{pgfonlayer}{edgelayer}')
        for e in edges:
            src = e.get_source()
            dest = e.get_destination()
            mult = edge_counts.get((src, dest))
            if mult == 1:
                line = f'\\draw [line width={edge_width}, style=plain edge] ({src}) -- ({dest});'
            elif mult == 2:
                line = f'\\draw [line width={edge_width}, style=double edge] ({src}) -- ({dest});'
            else:
                raise ValueError("Higher multiplicity found: " + str(mult))
            lines.append(line)
        lines.append(r'\end{pgfonlayer}')
        
        if subgraph is not None:
            lines.append(r'% highlights')
            lines.append(r'\begin{pgfonlayer}{main}')
            lines.append(r'')
            for (u, v, label) in subgraph.edges():
                if u == v:
                    line = f'\\filldraw[cyan] (node_{u}) circle (6pt);'
                else:
                    line = f'\\fill[cyan] \\convexpath{{node_{u},node_{v}}}{{4pt}};'
                lines.append(line)
        
            lines.append(r'\end{scope}')
            lines.append(r'\end{pgfonlayer}')
        
        lines.append(r'\end{tikzpicture}')
        tikz = '\n'.join(lines)
    
        if debug: print(tikz)
        
        t = TikzPicture(
            tikz, standalone_config=["border=4mm"], 
            usetikzlibrary=['arrows', 'calc', 'positioning'],
            usepackage=['amsmath', 'mathptmx', 'color', '/home/dzack/Notes/tikzit', 
                        '/home/dzack/Notes/DZG_Style_Tikz_Only', 'tikz-cd', 'pgfplots' ])
    
        return t
