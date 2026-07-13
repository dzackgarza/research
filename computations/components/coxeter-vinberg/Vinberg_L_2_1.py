from collections.abc import Sequence

from sage.arith.misc import gcd
from sage.functions.other import sqrt
from sage.geometry.polyhedron.base import Polyhedron_base
from sage.geometry.polyhedron.constructor import Polyhedron
from sage.graphs.graph import Graph
from sage.graphs.graph_plot import GraphPlot
from sage.matrix.constructor import diagonal_matrix
from sage.modules.free_module_element import FreeModuleElement, vector
from sage.plot.graphics import Graphics
from sage.rings.integer import Integer
from sage.rings.rational_field import QQ
from sage.rings.rational import Rational
from sage.structure.element import Matrix as SageMatrix


def plot_coxeter_diagram_detailed(
    simple_roots: Sequence[FreeModuleElement], Q: SageMatrix = diagonal_matrix([-1, 1, 1])
) -> Graphics:
    G = Graph(multiedges=False, loops=False)

    # Precompute exact cos(pi/m) values
    cos_table = {
        2: -1,
        3: -QQ(1)/2,
        4: -QQ(1)/sqrt(2),
        5: -(sqrt(5) + 1) / 4,
        6: -QQ(1)/(2 * sqrt(3)),
        # etc... extend as needed
    }

    for i in range(len(simple_roots)):
        for j in range(i + 1, len(simple_roots)):
            ri, rj = simple_roots[i], simple_roots[j]
            ip = (ri * Q * rj)
            val = -ip / 2

            if val == 1:
                continue  # no edge
            elif val == -1:
                G.add_edge(i, j, label='∞')
                continue

            # Determine m from known cos(pi/m) values
            found = False
            for m, cosval in [(2, -1), (3, -QQ(1)/2), (4, 0), (6, QQ(1)/2)]:
                if val == cosval:
                    G.add_edge(i, j, label=str(m))
                    found = True
                    break
            if not found:
                G.add_edge(i, j, label='?')  # fallback for unrecognized angles

    vertex_labels = {
        i: f"{i}\n({(r * Q * r)})" for i, r in enumerate(simple_roots)
    }

    graph_plot: GraphPlot = G.graphplot(
        vertex_labels=vertex_labels,
        edge_labels=True,
        figsize=6,
    )
    return graph_plot.plot()



# Lorentzian form Q with signature (2,1)
Q: SageMatrix = diagonal_matrix([-1, 1, 1])

def lorentz_inner(u: FreeModuleElement, v: FreeModuleElement) -> Integer | Rational:
    return u * Q * v

def in_hyperbolic_domain(v: FreeModuleElement) -> bool:
    # Negative norm and future cone (to pick one sheet)
    negative_norm: bool = lorentz_inner(v, v) < 0
    future_pointing: bool = v[0] > 0
    return negative_norm and future_pointing

def reflect(x: FreeModuleElement, r: FreeModuleElement) -> FreeModuleElement:
    rr = lorentz_inner(r, r)
    if rr == 0:
        raise ValueError("Reflection undefined for isotropic root vector")
    return x - 2 * lorentz_inner(x, r) / rr * r

def chamber_polyhedron(roots: Sequence[FreeModuleElement]) -> Polyhedron_base:
    # Inequalities for half-spaces: (r, x) >= 0
    # Sage Polyhedron inequalities: c + a1 x1 + ... >= 0
    # So use: [0, -r0, -r1, -r2]
    ieqs = []
    for r in roots:
        ieqs.append([0] + [-x for x in r])
    return Polyhedron(ieqs=ieqs)

def chamber_fully_in_hyperbolic(chamber: Polyhedron_base) -> bool:
    # Vertices and rays inside hyperbolic domain or on boundary (ideal vertices)
    for v in chamber.vertices():
        vec = vector(v)
        if lorentz_inner(vec, vec) >= 0 or vec[0] <= 0:
            return False
    for ray in chamber.rays():
        ray_vec = vector(ray)
        # Rays may be isotropic (null) or negative norm; disallow positive norm or backward pointing
        if lorentz_inner(ray_vec, ray_vec) > 0 or ray_vec[0] < 0:
            return False
    return True

def is_new_root(
    r: FreeModuleElement, roots: Sequence[FreeModuleElement], tol: float = 1e-12
) -> bool:
    # Check if root r (or its negative) already in roots
    for s in roots:
        if (r - s).norm() < tol or (r + s).norm() < tol:
            return False
    return True

def primitive_root(r: FreeModuleElement) -> FreeModuleElement:
    # Make integer vector primitive by dividing by gcd of entries
    g = gcd(list(r))
    if g != 0 and g != 1 and g != -1:
        r = r // g
    return r

def vinberg_algorithm(simple_roots: Sequence[FreeModuleElement]) -> list[FreeModuleElement]:
    roots = list(simple_roots)
    new_roots_added = True
    iteration = 0

    while new_roots_added:
        iteration += 1
        new_roots_added = False

        chamber = chamber_polyhedron(roots)
        if chamber_fully_in_hyperbolic(chamber):
            print(f"Chamber fully contained in hyperbolic domain after iteration {iteration}")
            break

        candidates = []
        for r in roots:
            for s in roots:
                if r == s:
                    continue
                # Reflect r in s only if s has norm -2 (root reflection)
                norm_s = lorentz_inner(s, s)
                if norm_s != -2:
                    continue
                if norm_s == 0:
                    # Skip isotropic roots - reflections undefined
                    continue

                reflected = reflect(r, s)

                # Check reflected is norm -2 root
                norm_reflected = lorentz_inner(reflected, reflected)
                if norm_reflected != -2:
                    continue

                reflected = primitive_root(reflected)

                if in_hyperbolic_domain(reflected):
                    candidates.append(reflected)

        for c in candidates:
            if is_new_root(c, roots):
                roots.append(c)
                new_roots_added = True

        print(f"Iteration {iteration}: number of simple roots = {len(roots)}")

    return roots

if __name__ == "__main__":
    # Example initial simple roots of norm -2 (change for your lattice)
    simple_roots = [
        vector([-1, 1, 0]),
        vector([-1, 0, 1]),
        vector([-2, 1, 1])
    ]

    roots = vinberg_algorithm(simple_roots)
    print("Simple roots found:")
    for r in roots:
        print(r)
    print(f"Total simple roots: {len(roots)}")

    p = plot_coxeter_diagram_detailed(roots, Q)
    p.show()
