from sage.all import *
from sage.graphs.graph import Graph
from collections import defaultdict, Counter
from functools import reduce
import math
from coxeter_graph import CoxeterGraph

# --- Extracted functions from Isometry Searching.ipynb ---

def matrix_to_graph(M):
    """
    Convert a Sage matrix to a Sage Graph with loops.

    EXAMPLES::

        sage: from isometry_utils import matrix_to_graph
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

def graph_to_matrix(G):
    """
    Convert a Sage Graph to a Sage matrix (ZZ entries).

    EXAMPLES::

        sage: from isometry_utils import graph_to_matrix
        sage: G = Graph([(0,0,'2'), (0,1,'1'), (1,1,'2')], loops=True)
        sage: M = graph_to_matrix(G)
        sage: M
        [2 1]
        [1 2]
    """
    verts = G.vertices()
    n = len(verts)
    M = zero_matrix(ZZ, n)
    Gp = G.relabel(list(range(n)), inplace=False)
    for e in Gp.edges():
        M[ e[0], e[1] ] = e[2]
        M[ e[1], e[0] ] = e[2]
    return M

# --- Add all other function and class definitions from the notebook below, with docstrings and examples where possible ---

def graph_A_n(n):
    """
    Construct the Dynkin diagram of type A_n as a Sage Graph.
    
    EXAMPLES::
        sage: from isometry_utils import graph_A_n
        sage: G = graph_A_n(3)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 1), (1, 1, -2), (1, 2, 1), (2, 2, -2)]
    """
    m = n-1
    G = Graph()
    G.allow_loops(True)
    for i in range(m+1):
        G.add_edge(i, i, -2)
    for i in range(m):
        G.add_edge(i, i+1, 1)
    return G

def matrix_A_n(n):
    """
    Return the Gram matrix for the Dynkin diagram of type A_n.
    
    EXAMPLES::
        sage: from isometry_utils import matrix_A_n
        sage: M = matrix_A_n(3)
        sage: M
        [ 2 -1  0]
        [-1  2 -1]
        [ 0 -1  2]
    """
    return graph_to_matrix(graph_A_n(n))

def graph_A_n_2(n):
    """
    Construct the doubled Dynkin diagram of type A_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_A_n_2
        sage: G = graph_A_n_2(3)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 1, 2), (1, 1, -4), (1, 2, 2), (2, 2, -4)]
    """
    m = n-1
    G = Graph(loops=True)
    for i in range(m+1):
        G.add_edge(i, i, -4)
    for i in range(m):
        G.add_edge(i, i+1, 2)
    return G

def matrix_A_n_2(n):
    """
    Return the Gram matrix for the doubled Dynkin diagram of type A_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_A_n_2
        sage: M = matrix_A_n_2(3)
        sage: M
        [ 4  0  2]
        [ 0  4  0]
        [ 2  0  4]
    """
    return graph_to_matrix(graph_A_n_2(n))

def graph_B_n(n):
    """
    Construct the Dynkin diagram of type B_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_B_n
        sage: G = graph_B_n(3)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 1, 2), (1, 1, -4), (1, 2, 2), (2, 2, -2)]
    """
    m = n-1
    G = Graph(loops=True)
    for i in [0..m]:
        G.add_edge(i, i, -4)
    G.add_edge(m, m, -2)
    for i in [0..m-1]:
        G.add_edge(i, i+1, 2)
    G.add_edge(m-1, m, 2)
    return G

def matrix_B_n(n):
    """
    Return the Gram matrix for the Dynkin diagram of type B_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_B_n
        sage: M = matrix_B_n(3)
        sage: M
        [ 4 -2  0]
        [-2  4 -2]
        [ 0 -2  2]
    """
    return graph_to_matrix(graph_B_n(n))

def graph_B_n_2(n):
    """
    Construct the doubled Dynkin diagram of type B_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_B_n_2
        sage: G = graph_B_n_2(3)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -8), (0, 1, 4), (1, 1, -8), (1, 2, 4), (2, 2, -4)]
    """
    m = n-1
    G = Graph(loops=True)
    for i in [0..m]:
        G.add_edge(i, i, -8)
    G.add_edge(m, m, -4)
    for i in [0..m-1]:
        G.add_edge(i, i+1, 4)
    G.add_edge(m-1, m, 4)
    return G

def matrix_B_n_2(n):
    """
    Return the Gram matrix for the doubled Dynkin diagram of type B_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_B_n_2
        sage: M = matrix_B_n_2(3)
        sage: M
        [ 8  0  4]
        [ 0  8  0]
        [ 4  0  4]
    """
    return graph_to_matrix(graph_B_n_2(n))

def graph_C_n(n):
    """
    Construct the Dynkin diagram of type C_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_C_n
        sage: G = graph_C_n(3)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 1), (1, 1, -2), (1, 2, 2), (2, 2, -4)]
    """
    m = n-1
    G = Graph(loops=True)
    for i in [0..m]:
        G.add_edge(i, i, -2)
    G.add_edge(m, m, -4)
    for i in [0..m-1]:
        G.add_edge(i, i+1, 1)
    G.add_edge(m-1, m, 2)
    return G

def graph_C_n_2(n):
    """
    Construct the doubled Dynkin diagram of type C_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_C_n_2
        sage: G = graph_C_n_2(3)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 1, 4), (1, 1, -4), (1, 2, 4), (2, 2, -8)]
    """
    m = n-1
    G = Graph(loops=True)
    for i in [0..m]:
        G.add_edge(i, i, -4)
    G.add_edge(m, m, -8)
    for i in [0..m-1]:
        G.add_edge(i, i+1, 4)
    G.add_edge(m-1, m, 4)
    return G

def matrix_C_n_2(n):
    """
    Return the Gram matrix for the doubled Dynkin diagram of type C_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_C_n_2
        sage: M = matrix_C_n_2(3)
        sage: M
        [ 4  4  0]
        [ 4  4  4]
        [ 0  4  8]
    """
    return graph_to_matrix(graph_C_n_2(n))

def graph_D_2():
    """
    Construct the Dynkin diagram of type D_2 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_D_2
        sage: G = graph_D_2()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (1, 1, -2)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -2)
    return G

def graph_D_n(n):
    """
    Construct the Dynkin diagram of type D_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_D_n
        sage: G = graph_D_n(4)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 2, 1), (1, 1, -2), (1, 2, 1), (2, 2, -2), (2, 3, 1), (3, 3, -2)]
    """
    if n == 2: return graph_D_2()
    if n == 3: return graph_A_n(2)
    m = n-1
    G = Graph(loops=True)
    for i in [0..m]:
        G.add_edge(i, i, -2)
    G.add_edge(0, 2, 1)
    G.add_edge(1, 2, 1)
    for i in [2..m-1]:
        G.add_edge(i, i+1, 1)
    return G

def matrix_D_n(n):
    """
    Return the Gram matrix for the Dynkin diagram of type D_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_D_n
        sage: M = matrix_D_n(4)
        sage: M
        [ 2  0 -1  0]
        [ 0  2 -1  0]
        [-1 -1  2 -1]
        [ 0  0 -1  2]
    """
    return graph_to_matrix(graph_D_n(n))

def graph_D_n_2(n):
    """
    Construct the doubled Dynkin diagram of type D_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_D_n_2
        sage: G = graph_D_n_2(4)
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 2, 2), (1, 1, -4), (1, 2, 2), (2, 2, -4), (2, 3, 2), (3, 3, -4)]
    """
    m = n-1
    G = Graph(loops=True)
    for i in [0..m]:
        G.add_edge(i, i, -4)
    G.add_edge(0, 2, 2)
    G.add_edge(1, 2, 2)
    for i in [2..m-1]:
        G.add_edge(i, i+1, 2)
    return G

def matrix_D_n_2(n):
    """
    Return the Gram matrix for the doubled Dynkin diagram of type D_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_D_n_2
        sage: M = matrix_D_n_2(4)
        sage: M
        [ 4  0 -2  0]
        [ 0  4 -2  0]
        [-2 -2  4 -2]
        [ 0  0 -2  4]
    """
    return graph_to_matrix(graph_D_n_2(n))

def graph_E_6():
    """
    Construct the Dynkin diagram of type E_6 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_E_6
        sage: G = graph_E_6()
        sage: G.num_verts()
        6
    """
    return matrix_to_graph(matrix_E_6())

def matrix_E_6():
    """
    Return the Gram matrix for the Dynkin diagram of type E_6.
    EXAMPLES::
        sage: from isometry_utils import matrix_E_6
        sage: M = matrix_E_6()
        sage: M.nrows()
        6
    """
    return IntegralLattice("E6").twist(-1).gram_matrix()

def graph_E_6_2():
    """
    Construct the doubled Dynkin diagram of type E_6 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_E_6_2
        sage: G = graph_E_6_2()
        sage: G.num_verts()
        6
    """
    return matrix_to_graph(matrix_E_6_2())

def matrix_E_6_2():
    """
    Return the Gram matrix for the doubled Dynkin diagram of type E_6.
    EXAMPLES::
        sage: from isometry_utils import matrix_E_6_2
        sage: M = matrix_E_6_2()
        sage: M.nrows()
        6
    """
    return IntegralLattice("E6").twist(-2).gram_matrix()

def graph_E_7():
    """
    Construct the Dynkin diagram of type E_7 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_E_7
        sage: G = graph_E_7()
        sage: G.num_verts()
        7
    """
    return matrix_to_graph(matrix_E_7())

def matrix_E_7():
    """
    Return the Gram matrix for the Dynkin diagram of type E_7.
    EXAMPLES::
        sage: from isometry_utils import matrix_E_7
        sage: M = matrix_E_7()
        sage: M.nrows()
        7
    """
    return IntegralLattice("E7").twist(-1).gram_matrix()

def graph_E_7_2():
    """
    Construct the doubled Dynkin diagram of type E_7 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_E_7_2
        sage: G = graph_E_7_2()
        sage: G.num_verts()
        7
    """
    return matrix_to_graph(matrix_E_7_2())

def matrix_E_7_2():
    """
    Return the Gram matrix for the doubled Dynkin diagram of type E_7.
    EXAMPLES::
        sage: from isometry_utils import matrix_E_7_2
        sage: M = matrix_E_7_2()
        sage: M.nrows()
        7
    """
    return IntegralLattice("E7").twist(-2).gram_matrix()

def graph_E_8():
    """
    Construct the Dynkin diagram of type E_8 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_E_8
        sage: G = graph_E_8()
        sage: G.num_verts()
        8
    """
    return matrix_to_graph(matrix_E_8())

def matrix_E_8():
    """
    Return the Gram matrix for the Dynkin diagram of type E_8.
    EXAMPLES::
        sage: from isometry_utils import matrix_E_8
        sage: M = matrix_E_8()
        sage: M.nrows()
        8
    """
    return IntegralLattice("E8").twist(-1).gram_matrix()

def graph_E_8_2():
    """
    Construct the doubled Dynkin diagram of type E_8 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_E_8_2
        sage: G = graph_E_8_2()
        sage: G.num_verts()
        8
    """
    return matrix_to_graph(matrix_E_8_2())

def matrix_E_8_2():
    """
    Return the Gram matrix for the doubled Dynkin diagram of type E_8.
    EXAMPLES::
        sage: from isometry_utils import matrix_E_8_2
        sage: M = matrix_E_8_2()
        sage: M.nrows()
        8
    """
    return IntegralLattice("E8").twist(-2).gram_matrix()

def graph_G_2():
    """
    Construct the Dynkin diagram of type G_2 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_G_2
        sage: G = graph_G_2()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 3), (1, 1, -6)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -6)
    G.add_edge(0, 1, 3)
    return G

def matrix_G_2():
    """
    Return the Gram matrix for the Dynkin diagram of type G_2.
    EXAMPLES::
        sage: from isometry_utils import matrix_G_2
        sage: M = matrix_G_2()
        sage: M
        [ 2 -3]
        [-3  6]
    """
    return graph_to_matrix(graph_G_2())

def graph_G_2_2():
    """
    Construct the doubled Dynkin diagram of type G_2 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_G_2_2
        sage: G = graph_G_2_2()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 1, 6), (1, 1, -12)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -4)
    G.add_edge(1, 1, -12)
    G.add_edge(0, 1, 6)
    return G

def matrix_G_2_2():
    """
    Return the Gram matrix for the doubled Dynkin diagram of type G_2.
    EXAMPLES::
        sage: from isometry_utils import matrix_G_2_2
        sage: M = matrix_G_2_2()
        sage: M
        [ 4 -6]
        [-6 12]
    """
    return graph_to_matrix(graph_G_2_2())

def graph_F_4():
    """
    Construct the Dynkin diagram of type F_4 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_F_4
        sage: G = graph_F_4()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 1), (1, 1, -2), (1, 2, 2), (2, 2, -4), (2, 3, 2), (3, 3, -4)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -2)
    G.add_edge(2, 2, -4)
    G.add_edge(3, 3, -4)
    
    G.add_edge(0, 1, 1)
    G.add_edge(1, 2, 2)
    G.add_edge(2, 3, 2)
    return G

def matrix_F_4():
    """
    Return the Gram matrix for the Dynkin diagram of type F_4.
    EXAMPLES::
        sage: from isometry_utils import matrix_F_4
        sage: M = matrix_F_4()
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_F_4())

def graph_H_3():
    """
    Construct the Dynkin diagram of type H_3 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_H_3
        sage: G = graph_H_3()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 2), (1, 1, -4), (1, 2, 2), (2, 2, -4)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -4)
    G.add_edge(2, 2, -4)
    
    G.add_edge(0, 1, 2)
    G.add_edge(1, 2, 2)
    return G

def matrix_H_3():
    """
    Return the Gram matrix for the Dynkin diagram of type H_3.
    EXAMPLES::
        sage: from isometry_utils import matrix_H_3
        sage: M = matrix_H_3()
        sage: M
        [ 2 -2  0]
        [-2  4 -2]
        [ 0 -2  4]
    """
    return graph_to_matrix(graph_H_3())

def graph_H_3_2():
    """
    Construct the doubled Dynkin diagram of type H_3 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_H_3_2
        sage: G = graph_H_3_2()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 1, 4), (1, 1, -8), (1, 2, 4), (2, 2, -8)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -4)
    G.add_edge(1, 1, -8)
    G.add_edge(2, 2, -8)
    
    G.add_edge(0, 1, 4)
    G.add_edge(1, 2, 4)
    return G

def matrix_H_3_2():
    """
    Return the Gram matrix for the doubled Dynkin diagram of type H_3.
    EXAMPLES::
        sage: from isometry_utils import matrix_H_3_2
        sage: M = matrix_H_3_2()
        sage: M
        [ 4 -4  0]
        [-4  8 -4]
        [ 0 -4  8]
    """
    return graph_to_matrix(graph_H_3_2())

def graph_H_4():
    """
    Construct the Dynkin diagram of type H_4 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_H_4
        sage: G = graph_H_4()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 1), (1, 1, -2), (1, 2, 1), (2, 2, -2), (2, 3, 2), (3, 3, -4)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -2)
    G.add_edge(2, 2, -2)
    G.add_edge(3, 3, -4)
    
    G.add_edge(0, 1, 1)
    G.add_edge(1, 2, 1)
    G.add_edge(2, 3, 2)
    return G

def matrix_H_4():
    """
    Return the Gram matrix for the Dynkin diagram of type H_4.
    EXAMPLES::
        sage: from isometry_utils import matrix_H_4
        sage: M = matrix_H_4()
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_H_4())

# Parabolic types (Affine/Tilde diagrams)

def graph_tilde_A_1():
    """
    Construct the affine Dynkin diagram of type ~A_1 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_A_1
        sage: G = graph_tilde_A_1()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 2), (1, 1, -2)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -2)
    G.add_edge(0, 1, 2)
    return G

def matrix_tilde_A_1():
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~A_1.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_A_1
        sage: M = matrix_tilde_A_1()
        sage: M
        [ 2 -2]
        [-2  2]
    """
    return matrix(ZZ, 2, [2, -2, -2, 2])

def graph_tilde_A_n(n):
    """
    Construct the affine Dynkin diagram of type ~A_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_A_n
        sage: G = graph_tilde_A_n(3)
        sage: G.num_verts()
        4
    """
    G = Graph(loops=True)
    for i in [0..n]:
        G.add_edge(i, i, -2)
    for i in [0..n-1]:
        G.add_edge(i, i+1, 1)
    G.add_edge(n, 0, 1)
    return G

def matrix_tilde_A_n(n):
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~A_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_A_n
        sage: M = matrix_tilde_A_n(3)
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_tilde_A_n(n))

def graph_tilde_B_n(n):
    """
    Construct the affine Dynkin diagram of type ~B_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_B_n
        sage: G = graph_tilde_B_n(3)
        sage: G.num_verts()
        4
    """
    G = Graph(loops=True)
    # Squares
    for i in [0..n-1]:
        G.add_edge(i, i, -2)
    G.add_edge(n, n, -4)
    # Edges
    G.add_edge(0, 2, 1)
    G.add_edge(1, 2, 1)
    for i in [2..n-2]:
        G.add_edge(i, i+1, 1)
    G.add_edge(n-1, n, 2)
    return G

def graph_tilde_B_n_2(n):
    """
    Construct the doubled affine Dynkin diagram of type ~B_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_B_n_2
        sage: G = graph_tilde_B_n_2(3)
        sage: G.num_verts()
        4
    """
    G = Graph(loops=True)
    # Squares
    for i in [0..n-1]:
        G.add_edge(i, i, -4)
    G.add_edge(n, n, -2)
    # Edges
    G.add_edge(0, 2, 2)
    G.add_edge(1, 2, 2)
    for i in [2..n-2]:
        G.add_edge(i, i+1, 2)
    G.add_edge(n-1, n, 2)
    return G

def matrix_tilde_B_n(n):
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~B_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_B_n
        sage: M = matrix_tilde_B_n(3)
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_tilde_B_n(n))

def matrix_tilde_B_n_2(n):
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~B_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_B_n_2
        sage: M = matrix_tilde_B_n_2(3)
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_tilde_B_n_2(n))

def graph_tilde_C_n(n):
    """
    Construct the affine Dynkin diagram of type ~C_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_C_n
        sage: G = graph_tilde_C_n(3)
        sage: G.num_verts()
        4
    """
    G = Graph(loops=True)
    # Squares
    G.add_edge(0, 0, -4)
    for i in [1..n-1]:
        G.add_edge(i, i, -2)
    G.add_edge(n, n, -4)
    # Edges
    G.add_edge(0, 1, 2)
    for i in [1..n-2]:
        G.add_edge(i, i+1, 1)
    G.add_edge(n-1, n, 2)
    return G

def graph_tilde_C_n_2(n):
    """
    Construct the doubled affine Dynkin diagram of type ~C_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_C_n_2
        sage: G = graph_tilde_C_n_2(3)
        sage: G.num_verts()
        4
    """
    G = Graph(loops=True)
    # Squares
    G.add_edge(0, 0, -2)
    for i in [1..n-1]:
        G.add_edge(i, i, -4)
    G.add_edge(n, n, -2)
    # Edges
    G.add_edge(0, 1, 2)
    for i in [1..n-2]:
        G.add_edge(i, i+1, 2)
    G.add_edge(n-1, n, 2)
    return G

def matrix_tilde_C_n(n):
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~C_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_C_n
        sage: M = matrix_tilde_C_n(3)
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_tilde_C_n(n))

def matrix_tilde_C_n_2(n):
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~C_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_C_n_2
        sage: M = matrix_tilde_C_n_2(3)
        sage: M.nrows()
        4
    """
    return graph_to_matrix(graph_tilde_C_n_2(n))

def graph_tilde_D_n(n):
    """
    Construct the affine Dynkin diagram of type ~D_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_D_n
        sage: G = graph_tilde_D_n(4)
        sage: G.num_verts()
        5
    """
    G = Graph(loops=True)
    for i in [0..n]:
        G.add_edge(i, i, -2)
    G.add_edge(0, 2, 1)
    G.add_edge(1, 2, 1)
    for i in [2..n-3]:
        G.add_edge(i, i+1, 1)
    G.add_edge(n-2, n-1, 1)
    G.add_edge(n-2, n, 1)
    return G

def graph_tilde_D_n_2(n):
    """
    Construct the doubled affine Dynkin diagram of type ~D_n as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_D_n_2
        sage: G = graph_tilde_D_n_2(4)
        sage: G.num_verts()
        5
    """
    G = Graph(loops=True)
    for i in [0..n]:
        G.add_edge(i, i, -4)
    G.add_edge(0, 2, 2)
    G.add_edge(1, 2, 2)
    for i in [2..n-3]:
        G.add_edge(i, i+1, 2)
    G.add_edge(n-2, n-1, 2)
    G.add_edge(n-2, n, 2)
    return G

def matrix_tilde_D_n(n):
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~D_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_D_n
        sage: M = matrix_tilde_D_n(4)
        sage: M.nrows()
        5
    """
    return graph_to_matrix(graph_tilde_D_n(n))

def matrix_tilde_D_n_2(n):
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~D_n.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_D_n_2
        sage: M = matrix_tilde_D_n_2(4)
        sage: M.nrows()
        5
    """
    return graph_to_matrix(graph_tilde_D_n_2(n))

def graph_tilde_G_2():
    """
    Construct the affine Dynkin diagram of type ~G_2 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_G_2
        sage: G = graph_tilde_G_2()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -2), (0, 1, 1), (1, 1, -2), (1, 2, 3), (2, 2, -6)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -2)
    G.add_edge(2, 2, -6)
    G.add_edge(0, 1, 1)
    G.add_edge(1, 2, 3)
    return G

def matrix_tilde_G_2():
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~G_2.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_G_2
        sage: M = matrix_tilde_G_2()
        sage: M.nrows()
        3
    """
    return graph_to_matrix(graph_tilde_G_2())

def graph_tilde_G_2_2():
    """
    Construct the doubled affine Dynkin diagram of type ~G_2 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_G_2_2
        sage: G = graph_tilde_G_2_2()
        sage: sorted(G.edges(labels=True))
        [(0, 0, -4), (0, 1, 2), (1, 1, -4), (1, 2, 6), (2, 2, -12)]
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -4)
    G.add_edge(1, 1, -4)
    G.add_edge(2, 2, -12)
    G.add_edge(0, 1, 2)
    G.add_edge(1, 2, 6)
    return G

def matrix_tilde_G_2_2():
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~G_2.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_G_2_2
        sage: M = matrix_tilde_G_2_2()
        sage: M.nrows()
        3
    """
    return graph_to_matrix(graph_tilde_G_2_2())

def graph_tilde_F_4():
    """
    Construct the affine Dynkin diagram of type ~F_4 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_F_4
        sage: G = graph_tilde_F_4()
        sage: G.num_verts()
        5
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -4)
    G.add_edge(1, 1, -4)
    G.add_edge(2, 2, -2)
    G.add_edge(3, 3, -2)
    G.add_edge(4, 4, -2)
    
    G.add_edge(0, 1, 2)
    G.add_edge(1, 2, 2)
    G.add_edge(2, 3, 1)
    G.add_edge(3, 4, 1)
    return G

def matrix_tilde_F_4():
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~F_4.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_F_4
        sage: M = matrix_tilde_F_4()
        sage: M.nrows()
        5
    """
    return graph_to_matrix(graph_tilde_F_4())

def graph_tilde_F_4_2():
    """
    Construct the doubled affine Dynkin diagram of type ~F_4 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_F_4_2
        sage: G = graph_tilde_F_4_2()
        sage: G.num_verts()
        5
    """
    G = Graph(loops=True)
    G.add_edge(0, 0, -2)
    G.add_edge(1, 1, -2)
    G.add_edge(2, 2, -4)
    G.add_edge(3, 3, -4)
    G.add_edge(4, 4, -4)
    
    G.add_edge(0, 1, 1)
    G.add_edge(1, 2, 2)
    G.add_edge(2, 3, 2)
    G.add_edge(3, 4, 2)
    return G

def matrix_tilde_F_4_2():
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~F_4.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_F_4_2
        sage: M = matrix_tilde_F_4_2()
        sage: M.nrows()
        5
    """
    return graph_to_matrix(graph_tilde_F_4_2())

def graph_tilde_E_6():
    """
    Construct the affine Dynkin diagram of type ~E_6 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_E_6
        sage: G = graph_tilde_E_6()
        sage: G.num_verts()
        7
    """
    return matrix_to_graph(matrix_tilde_E_6())

def matrix_tilde_E_6():
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~E_6.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_E_6
        sage: M = matrix_tilde_E_6()
        sage: M.nrows()
        7
    """
    return CoxeterType(["E", 6, 1]).bilinear_form() * -2

def graph_tilde_E_6_2():
    """
    Construct the doubled affine Dynkin diagram of type ~E_6 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_E_6_2
        sage: G = graph_tilde_E_6_2()
        sage: G.num_verts()
        7
    """
    return matrix_to_graph(matrix_tilde_E_6_2())

def matrix_tilde_E_6_2():
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~E_6.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_E_6_2
        sage: M = matrix_tilde_E_6_2()
        sage: M.nrows()
        7
    """
    return CoxeterType(["E", 6, 1]).bilinear_form() * -4

def graph_tilde_E_7():
    """
    Construct the affine Dynkin diagram of type ~E_7 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_E_7
        sage: G = graph_tilde_E_7()
        sage: G.num_verts()
        8
    """
    return matrix_to_graph(matrix_tilde_E_7())

def matrix_tilde_E_7():
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~E_7.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_E_7
        sage: M = matrix_tilde_E_7()
        sage: M.nrows()
        8
    """
    return CoxeterType(["E", 7, 1]).bilinear_form() * -2

def graph_tilde_E_7_2():
    """
    Construct the doubled affine Dynkin diagram of type ~E_7 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_E_7_2
        sage: G = graph_tilde_E_7_2()
        sage: G.num_verts()
        8
    """
    return matrix_to_graph(matrix_tilde_E_7_2())

def matrix_tilde_E_7_2():
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~E_7.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_E_7_2
        sage: M = matrix_tilde_E_7_2()
        sage: M.nrows()
        8
    """
    return CoxeterType(["E", 7, 1]).bilinear_form() * -4

def graph_tilde_E_8():
    """
    Construct the affine Dynkin diagram of type ~E_8 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_E_8
        sage: G = graph_tilde_E_8()
        sage: G.num_verts()
        9
    """
    return matrix_to_graph(matrix_tilde_E_8())

def matrix_tilde_E_8():
    """
    Return the Gram matrix for the affine Dynkin diagram of type ~E_8.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_E_8
        sage: M = matrix_tilde_E_8()
        sage: M.nrows()
        9
    """
    return CoxeterType(["E", 8, 1]).bilinear_form() * -2

def graph_tilde_E_8_2():
    """
    Construct the doubled affine Dynkin diagram of type ~E_8 as a Sage Graph.
    EXAMPLES::
        sage: from isometry_utils import graph_tilde_E_8_2
        sage: G = graph_tilde_E_8_2()
        sage: G.num_verts()
        9
    """
    return matrix_to_graph(matrix_tilde_E_8_2())

def matrix_tilde_E_8_2():
    """
    Return the Gram matrix for the doubled affine Dynkin diagram of type ~E_8.
    EXAMPLES::
        sage: from isometry_utils import matrix_tilde_E_8_2
        sage: M = matrix_tilde_E_8_2()
        sage: M.nrows()
        9
    """
    return CoxeterType(["E", 8, 1]).bilinear_form() * -4

# Utility functions

def sumset(s):
    """
    Sum tuples in a collection element-wise.
    
    EXAMPLES::
        sage: from isometry_utils import sumset
        sage: s = [(1, 2), (3, 4), (5, 6)]
        sage: sumset(s)
        (9, 12)
    """
    return reduce(lambda x, y: (x[0] + y[0], x[1] + y[1]), s)

def is_elliptic_matrix(M):
    """
    Check if a matrix is elliptic (negative definite).
    
    EXAMPLES::
        sage: from isometry_utils import is_elliptic_matrix
        sage: M = matrix([[-2, 1], [1, -2]])
        sage: is_elliptic_matrix(M)
        True
    """
    return (-1 * M).is_positive_definite()

def is_parabolic_matrix(M):
    """
    Check if a matrix is parabolic (negative semidefinite).
    
    EXAMPLES::
        sage: from isometry_utils import is_parabolic_matrix
        sage: M = matrix([[-2, 1], [1, -2]])
        sage: is_parabolic_matrix(M)
        True
    """
    return (-1 * M).is_positive_semidefinite()

def is_elliptic_subgraph(H):
    """
    Check if a graph corresponds to an elliptic subdiagram.
    
    EXAMPLES::
        sage: from isometry_utils import is_elliptic_subgraph, graph_A_n
        sage: G = graph_A_n(3)
        sage: is_elliptic_subgraph(G)
        True
    """
    return is_elliptic_matrix(graph_to_matrix(H))

def is_parabolic_subgraph(H):
    """
    Check if a graph corresponds to a parabolic subdiagram.
    
    EXAMPLES::
        sage: from isometry_utils import is_parabolic_subgraph, graph_tilde_A_n
        sage: G = graph_tilde_A_n(3)
        sage: is_parabolic_subgraph(G)
        True
    """
    return is_parabolic_matrix(graph_to_matrix(H))

def coxeter_str_format(s):
    """
    Format a string for Coxeter diagram labels.
    
    EXAMPLES::
        sage: from isometry_utils import coxeter_str_format
        sage: coxeter_str_format(["A", "3"])
        'A3'
    """
    return "".join(s)

def init_coxeter_colors(G):
    """
    Initialize vertex colors for a Coxeter graph based on loop weights.
    
    EXAMPLES::
        sage: from isometry_utils import init_coxeter_colors, graph_A_n
        sage: G = graph_A_n(3)
        sage: colors = init_coxeter_colors(G)
        sage: len(colors)
        3
    """
    v_labs = dict()
    vertex_colors = {
        '#F8F9FE': [], # white
        '#BFC9CA': [], # black
        '#b3f0fb': []  # blue
    }
    edge_verts = [x for x in G.edges() if x[0] == x[1]]

    for edge in edge_verts:
        v2 = edge[2]
        v_name = edge[0]
        if v2 == -4:
            vertex_colors["#F8F9FE"].append(v_name) # white
        elif v2 == -2:
            vertex_colors["#BFC9CA"].append(v_name) # black
        else:
            vertex_colors["#b3f0fb"].append(v_name) # blue
    if len(reduce(lambda x, y: x+y, list(vertex_colors.values()))) != G.num_verts():
        raise ValueError("Error while assigning vertex colors.")
    return vertex_colors

def get_all_rank_n_types(n):
    """
    Get all ADE type matrices of rank n.
    
    EXAMPLES::
        sage: from isometry_utils import get_all_rank_n_types
        sage: types = get_all_rank_n_types(2)
        sage: len(types)
        3
    """
    if n == 0:
        return [ 
            ("A_{0}" , matrix(ZZ, 0) ) 
       ]
    if n == 1:
        return [ 
            (f"A_{n}" ,matrix_A_n(1) ),
            (f"A_{n}(2)" ,matrix_A_n_2(1)) 
        ]
    if n == 2:
        return [ 
            (f"A_{n}",    matrix_A_n(2)),
            (f"A_{n}(2)", matrix_A_n_2(2)), 
            (f"G_{2}",    matrix_G_2()) 
        ]
    if n == 3:
        return [ 
            (f"A_{n}",    matrix_A_n(3)),
            (f"A_{n}(2)", matrix_A_n_2(3)), 
            (f"B_{n}(2)", matrix_B_n_2(3)),
            (f"C_{n}(2)", matrix_C_n_2(3))
        ]
    else:
        Ms = [ 
            (f"A_{n}",    matrix_A_n(n)),
            (f"A_{n}(2)", matrix_A_n_2(n)), 
            (f"B_{n}(2)", matrix_B_n_2(n)),
            (f"C_{n}(2)", matrix_C_n_2(n)),
            (f"D_{n}",    matrix_D_n(n)),
            (f"D_{n}(2)", matrix_D_n_2(n)) 
        ]
        if n == 6:
            Ms.extend([
                (f"E_6",    matrix_E_6() ),
                (f"E_6(2)", matrix_E_6_2() )
            ])
        elif n == 7:
            Ms.extend([
                (f"E_7",    matrix_E_7() ),
                (f"E_7(2)", matrix_E_7_2() )
            ])
        elif n == 8:
            Ms.extend([
                (f"E_8", matrix_E_8() ),
                (f"E_8(2)", matrix_E_8_2() )
            ])
        return Ms

def get_coxeter_label_connected(H):
    """
    Get the Coxeter type label for a connected graph.
    
    EXAMPLES::
        sage: from isometry_utils import get_coxeter_label_connected, graph_A_n
        sage: G = graph_A_n(3)
        sage: get_coxeter_label_connected(G)
        'A_3'
    """
    n = len(H.vertices())
    ade_types = get_all_rank_n_types(n)
    M_H = graph_to_matrix(H)
    s = ""
    this_type = [x[0] for x in ade_types if x[1].is_similar(M_H)]
    if len(this_type) == 0:
        this_type_negs = [x[0] for x in ade_types if x[1].is_similar(-1*M_H)]
        if len(this_type_negs) == 0:
            return "?"
        assert len(this_type_negs) == 1
        return this_type_negs[0] + "(-1)"
    assert len(this_type) == 1
    return this_type[0]

def is_lanner(G):
    """
    Check if a Coxeter diagram is a Lanner diagram.
    
    A Coxeter diagram S is called a Lanner diagram if any subdiagram of S is
    elliptic, and the diagram S is neither elliptic nor parabolic.
    
    EXAMPLES::
        sage: from isometry_utils import is_lanner, graph_A_n
        sage: G = graph_A_n(3)
        sage: is_lanner(G)
        False
    """
    if is_elliptic_subgraph(G) or is_parabolic_subgraph(G):
        return False
    else:
        return all([is_elliptic_subgraph(H) for H in G.get_subgraphs()])

# Import CoxeterGraph class from separate module
