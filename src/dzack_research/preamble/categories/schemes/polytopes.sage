r"""Category hierarchy and models for convex and lattice polytopes.

Hierarchy:
             Objects()
                 │
           ConvexPolytopes()
            /             \
  ConvexPolygons()    LatticePolytopes()
   [dim = 2]              [V ⊂ N]
            \             /
            LatticePolygons()
          [dim = 2, V ⊂ N]

Mathematical Foundations:
-------------------------
A convex polytope P \subset N_\RR is the bounded convex hull of finitely many points in N_\RR \cong \RR^d.
In dimension 2 (convex polygons), area is Euclidean 2-volume, and perimeter and 2D plotting are defined.
For integral lattice polytopes (V \subset N), normalized volume is d! * Vol(P), and lattice properties
(reflexivity, smoothness, polar duality, Ehrhart h*-vectors) are defined.

EXAMPLES::

    sage: from dzack_research.preamble.categories.schemes.polytopes import (
    ....:     ConvexPolytopes, ConvexPolygons, LatticePolytopes, LatticePolygons,
    ....:     ConvexPolygon, LatticePolygon
    ....: )
    sage: LatticePolygons().super_categories()
    [Category of convex polygons, Category of lattice polytopes]
    sage: P = LatticePolygon([(0, 0), (0, 3), (6, 0)])
    sage: P.n_integral_points()
    16
    sage: P.n_interior_points()
    4
    sage: P.n_boundary_points()
    12
    sage: P.volume()
    9
    sage: P.normalized_volume()
    18
    sage: CP = ConvexPolygon([(0, 0), (0, 3/2), (3, 0)])
    sage: CP.volume()
    9/4
"""

from typing import Self, Sequence, Callable, Optional, Protocol, TYPE_CHECKING
from dzack_research.preamble.owned_category_bases import Category
from dzack_research.preamble.owned_category import object_of
from dzack_research.preamble.categories.sets.owned_sets import Sets
from sage.structure.parent import Parent
from sage.geometry.toric_lattice import ToricLattice, ToricLattice_generic
from sage.geometry.polyhedron.constructor import Polyhedron as polyhedron
from sage.misc.cachefunc import cached_method

from dzack_research.preamble.lexicon import Polyhedron

if TYPE_CHECKING:
    from dzack_research.preamble.owned_category import ConstructionData
    from sage.plot.plot3d.base import Graphics3d

    type PlotOption = str | int | float | bool | tuple[float, ...]
from sage.rings.rational_field import QQ
from sage.rings.integer_ring import ZZ
from sage.rings.rational import Rational
from sage.rings.integer import Integer
from sage.plot.graphics import Graphics
from sage.plot.line import line
from sage.plot.polygon import polygon
from sage.plot.point import point
from sage.plot.text import text

LatticeCoord = int | Integer | Rational
LatticePoint = Sequence[LatticeCoord]


class _PolyhedronFace(Protocol):
    def vertices(self) -> Sequence[Sequence[LatticeCoord]]: ...
    def as_polyhedron(self) -> Polyhedron: ...


class _LatticePolytopeInterface(Protocol):
    def polyhedron(self) -> Polyhedron: ...
    def vertices(self) -> tuple[LatticePoint, ...]: ...
    def ambient_space(self) -> Callable[[Sequence[LatticeCoord]], LatticePoint]: ...
    def dimension(self) -> int: ...
    def integral_points(self) -> tuple[LatticePoint, ...]: ...
    def interior_integral_points(self) -> tuple[LatticePoint, ...]: ...
    def boundary_integral_points(self) -> tuple[LatticePoint, ...]: ...
    def n_integral_points(self) -> int: ...
    def n_interior_points(self) -> int: ...
    def n_boundary_points(self) -> int: ...
    def volume(self) -> Rational: ...
    def normalized_volume(self) -> Integer: ...


class ConvexPolytopes(Category):
    """
    The category of convex polytopes.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.polytopes import ConvexPolytopes
        sage: ConvexPolytopes()
        Category of convex polytopes
        sage: ConvexPolytopes().super_categories()
        [Category of sets]
    """
    def super_categories(self) -> list[Category]:
        return [Sets()]

    def _repr_object_names(self) -> str:
        return "convex polytopes"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Convex Polytopes}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        r"""
        A convex polytope P \subset N_\RR: the bounded convex hull of finitely
        many points, together with the lattice N it is read in.
        """
        def __init__(
            self: Self,
            vertices: Sequence[Sequence[LatticeCoord]] | Polyhedron | Parent,
            lattice: Optional[ToricLattice_generic] = None,
            base_ring: object = QQ,
            **rest: "ConstructionData",
        ) -> None:
            r"""Build the polytope of ``vertices``, read in the lattice ``lattice``."""
            if isinstance(vertices, Polyhedron):
                poly = vertices
                raw_verts = [list(v) for v in poly.vertices()]
                self._polyhedron = poly
            elif isinstance(vertices, Parent) and vertices in ConvexPolytopes():
                poly = vertices.polyhedron()
                raw_verts = [list(v) for v in poly.vertices()]
                self._polyhedron = poly
            else:
                raw_verts = [list(v) for v in vertices]
                self._polyhedron = polyhedron(vertices=raw_verts, base_ring=base_ring)

            dim = len(raw_verts[0]) if raw_verts else 0
            if lattice is None:
                lattice = ToricLattice(dim, 'N')
            self._lattice = lattice
            self._ambient_space = lattice
            self._raw_vertices = tuple(tuple(v) for v in raw_verts)
            self._dimension = int(self._polyhedron.dim())
            self._facets = tuple(self._polyhedron.facets())
            self._normal_fan = self._polyhedron.normal_fan()
            self._volume = Rational(self._polyhedron.volume())
            super().__init__(base=base_ring, **rest)

        def polyhedron(self: Self) -> Polyhedron:
            """Return the underlying Sage polyhedron."""
            return self._polyhedron

        def ambient_space(self: Self) -> Callable[[Sequence[LatticeCoord]], LatticePoint]:
            """Return the lattice N the polytope is read in."""
            return self._ambient_space

        def _repr_(self: _LatticePolytopeInterface) -> str:
            return f"Convex Polytope of dimension {self.dimension()} with {len(self.vertices())} vertices"

        def _latex_(self: _LatticePolytopeInterface) -> str:
            return fr"\text{{Polytope}}\left(\dim = {self.dimension()},\, |V| = {len(self.vertices())}\right)"

        def dimension(self: _LatticePolytopeInterface) -> int:
            """Return the dimension of the polytope."""
            return self._dimension

        def vertices(self: _LatticePolytopeInterface) -> tuple[LatticePoint, ...]:
            """Return the vertices of the polytope."""
            poly = self.polyhedron()
            return tuple(self.ambient_space()(list(v)) for v in poly.vertices())

        def facets(self: _LatticePolytopeInterface) -> tuple[_PolyhedronFace, ...]:
            """Return the facets (codimension-1 faces) of the polytope."""
            return self._facets

        def normal_fan(self: _LatticePolytopeInterface) -> object:
            """Return the outward normal fan of the polytope."""
            return self._normal_fan

        def volume(self: _LatticePolytopeInterface) -> Rational:
            """Return the Euclidean volume of the polytope."""
            return self._volume

        def normalized_volume(self: _LatticePolytopeInterface) -> Integer:
            r"""
            Return the normalized lattice volume d! * Vol(P).
            """
            import math
            d = self.dimension()
            return Integer(math.factorial(d) * self.volume())

        def is_compact(self: _LatticePolytopeInterface) -> bool:
            """Return True if the polytope is compact (bounded)."""
            return True

        def integral_points(self: _LatticePolytopeInterface) -> tuple[LatticePoint, ...]:
            r"""Return all integral lattice points contained in P (P \cap N)."""
            poly = self.polyhedron()
            return tuple(self.ambient_space()(list(p)) for p in poly.integral_points())

        def interior_integral_points(self: _LatticePolytopeInterface) -> tuple[LatticePoint, ...]:
            """Return all strictly interior integral lattice points of P."""
            poly = self.polyhedron()
            return tuple(self.ambient_space()(list(p)) for p in poly.integral_points() if poly.interior_contains(p))

        def boundary_integral_points(self: _LatticePolytopeInterface) -> tuple[LatticePoint, ...]:
            """Return all boundary integral lattice points of P."""
            poly = self.polyhedron()
            return tuple(self.ambient_space()(list(p)) for p in poly.integral_points() if not poly.interior_contains(p))

        def n_integral_points(self: _LatticePolytopeInterface) -> int:
            """Return the total number of integral lattice points in P."""
            return len(self.integral_points())

        def n_interior_points(self: _LatticePolytopeInterface) -> int:
            """Return the number of strictly interior integral lattice points."""
            return len(self.interior_integral_points())

        def n_boundary_points(self: _LatticePolytopeInterface) -> int:
            """Return the number of boundary integral lattice points."""
            return len(self.boundary_integral_points())

        def contains_point(self: _LatticePolytopeInterface, pt: Sequence[LatticeCoord]) -> bool:
            """Return True if pt lies in P."""
            pt_vec = self.ambient_space()(list(pt))
            return self.polyhedron().contains(pt_vec)

        def interior_contains_point(self: _LatticePolytopeInterface, pt: Sequence[LatticeCoord]) -> bool:
            """Return True if pt lies in the strict relative interior of P."""
            pt_vec = self.ambient_space()(list(pt))
            return self.polyhedron().interior_contains(pt_vec)

        def is_lattice_polytope(self: _LatticePolytopeInterface) -> bool:
            """Return True if all vertices of P are integral lattice points."""
            poly = self.polyhedron()
            return all(all(c in ZZ for c in v) for v in poly.vertices())

        def plot3d(
            self: _LatticePolytopeInterface,
            **kwds: "PlotOption",
        ) -> "Graphics3d":
            """
            Render an interactive 3D graphics visualization of a 3-dimensional polytope,
            including a bounded ambient ZZ^3 grid of spheres distinguishing points in the polytope or on its faces,
            plus standard XYZ coordinate axes.
            """
            from sage.plot.plot3d.shapes2 import sphere, line3d, text3d
            from sage.plot.plot3d.shapes import arrow3d
            from sage.plot.plot3d.index_face_set import IndexFaceSet

            poly = self.polyhedron()
            assert self.dimension() == 3, (
                f"plot3d requires a three-dimensional polytope; dimension={self.dimension()}"
            )

            face_color = kwds.get('color', '#3182CE')
            face_opacity = kwds.get('opacity', 0.35)
            edge_color = kwds.get('edge_color', 'black')
            edge_thickness = kwds.get('edge_thickness', 2)
            show_axes = kwds.get('axes', True)
            show_grid = kwds.get('show_grid', True)

            from dzack_research.preamble.categories.sets.sets import finite_ordered_set

            vertex_set = finite_ordered_set(
                tuple(tuple(vertex) for vertex in poly.vertices())
            )
            verts = [list(vertex) for vertex in vertex_set]
            vert_set = set(tuple(int(c) for c in v) for v in verts)
            faces = [
                [vertex_set.position(tuple(vertex)) for vertex in facet.vertices()]
                for facet in poly.facets()
            ]

            g3d = IndexFaceSet(faces, verts, opacity=face_opacity, color=face_color)

            # Draw facet boundary edges
            for f in poly.facets():
                f_verts = [list(v) for v in f.vertices()]
                for i in range(len(f_verts)):
                    v1 = f_verts[i]
                    v2 = f_verts[(i + 1) % len(f_verts)]
                    g3d += line3d([v1, v2], thickness=edge_thickness, color=edge_color)

            min_x = min(min(int(v[0]) for v in verts), 0)
            max_x = max(max(int(v[0]) for v in verts), 1)
            min_y = min(min(int(v[1]) for v in verts), 0)
            max_y = max(max(int(v[1]) for v in verts), 1)
            min_z = min(min(int(v[2]) for v in verts), 0)
            max_z = max(max(int(v[2]) for v in verts), 1)

            poly_pts = set(tuple(p) for p in self.integral_points())
            int_pts = set(tuple(p) for p in self.interior_integral_points())
            bnd_pts = poly_pts - int_pts
            facet_pts = bnd_pts - vert_set

            # Draw bounded ambient ZZ^3 grid (small gray spheres at each lattice point)
            if show_grid:
                grid_pts = [
                    (x, y, z)
                    for x in range(min_x - 1, max_x + 2)
                    for y in range(min_y - 1, max_y + 2)
                    for z in range(min_z, max_z + 2)
                ]
                ext_pts = [p for p in grid_pts if p not in poly_pts]
                for p in ext_pts:
                    g3d += sphere(p, size=0.035, color='#94A3B8', opacity=0.45)

            # Draw interior lattice points of P (teal spheres)
            for p in int_pts:
                g3d += sphere(p, size=0.08, color='#0D9488')

            # Draw facet/edge boundary points on faces of P (black spheres)
            for p in facet_pts:
                g3d += sphere(p, size=0.065, color='black')

            # Draw vertices of P (prominent black spheres)
            for p in vert_set:
                g3d += sphere(p, size=0.09, color='black')

            # Draw standard XYZ coordinate axes
            if show_axes:
                axis_radius = 0.025
                head_radius = 0.07

                # X-axis (Red)
                x_start = min_x - 0.5 if min_x < 0 else 0
                g3d += arrow3d([x_start, 0, 0], [max_x + 0.8, 0, 0], color='#DC2626', radius=axis_radius, head_radius=head_radius)
                g3d += text3d("x", [max_x + 1.0, 0, 0], color='#DC2626')

                # Y-axis (Green)
                y_start = min_y - 0.5 if min_y < 0 else 0
                g3d += arrow3d([0, y_start, 0], [0, max_y + 0.8, 0], color='#16A34A', radius=axis_radius, head_radius=head_radius)
                g3d += text3d("y", [0, max_y + 1.0, 0], color='#16A34A')

                # Z-axis (Blue)
                z_start = min_z - 0.5 if min_z < 0 else 0
                g3d += arrow3d([0, 0, z_start], [0, 0, max_z + 0.8], color='#2563EB', radius=axis_radius, head_radius=head_radius)
                g3d += text3d("z", [0, 0, max_z + 1.0], color='#2563EB')

            return g3d

        def tikz3d(self: _LatticePolytopeInterface, scale: float = 1.0, show_grid: bool = True) -> str:
            r"""
            Return standard TikZ 3D code using isometric projection.
            """
            poly = self.polyhedron()
            verts = [tuple(v) for v in poly.vertices()]

            header = [
                rf"\begin{{tikzpicture}}[scale={scale}, x={{(1cm,0cm)}}, y={{(0.4cm,0.3cm)}}, z={{(0cm,1cm)}}]",
                r"\tikzset{poly vertex/.style={circle, fill=black, inner sep=2pt}}",
                r"\tikzset{interior point/.style={circle, fill=teal, inner sep=1.8pt}}",
                r"\tikzset{grid point/.style={circle, fill=gray!40, inner sep=0.8pt}}",
            ]

            min_x = min(min(int(v[0]) for v in verts), 0)
            max_x = max(max(int(v[0]) for v in verts), 1)
            min_y = min(min(int(v[1]) for v in verts), 0)
            max_y = max(max(int(v[1]) for v in verts), 1)
            min_z = min(min(int(v[2]) for v in verts), 0)
            max_z = max(max(int(v[2]) for v in verts), 1)

            poly_pts = set(tuple(p) for p in self.integral_points())
            int_pts = set(tuple(p) for p in self.interior_integral_points())
            bnd_pts = poly_pts - int_pts

            grid_lines = []
            if show_grid:
                grid_pts = [
                    (x, y, z)
                    for x in range(min_x - 1, max_x + 2)
                    for y in range(min_y - 1, max_y + 2)
                    for z in range(min_z, max_z + 2)
                ]
                ext_pts = [p for p in grid_pts if p not in poly_pts]
                grid_lines = [rf"\node[grid point] at ({p[0]},{p[1]},{p[2]}) {{}};" for p in ext_pts]

            facet_lines = []
            for f in poly.facets():
                fv = [tuple(v) for v in f.vertices()]
                f_path = " -- ".join(f"({v[0]},{v[1]},{v[2]})" for v in fv) + " -- cycle"
                facet_lines.append(rf"\filldraw[fill=blue!15, fill opacity=0.4, draw=black, thick] {f_path};")

            axis_lines = [
                rf"\draw[->, thick, red!80!black] (0,0,0) -- ({float(max_x) + 0.8:.2f},0,0) node[anchor=north east]{{$x$}};",
                rf"\draw[->, thick, green!60!black] (0,0,0) -- (0,{float(max_y) + 0.8:.2f},0) node[anchor=north west]{{$y$}};",
                rf"\draw[->, thick, blue!80!black] (0,0,0) -- (0,0,{float(max_z) + 0.8:.2f}) node[anchor=south]{{$z$}};",
            ]

            int_lines = [rf"\node[interior point] at ({p[0]},{p[1]},{p[2]}) {{}};" for p in int_pts]
            bnd_lines = [rf"\node[poly vertex] at ({p[0]},{p[1]},{p[2]}) {{}};" for p in bnd_pts]

            return "\n".join([
                *header,
                *axis_lines,
                *grid_lines,
                *facet_lines,
                *int_lines,
                *bnd_lines,
                r"\end{tikzpicture}",
            ])

        def plot(
            self: _LatticePolytopeInterface,
            **kwds: "PlotOption",
        ) -> "Graphics3d":
            r"""Render a three-dimensional polytope."""
            assert self.dimension() == 3, (
                "generic polytope plotting is defined in dimension three; "
                "polygon plotting belongs to ConvexPolygons"
            )
            return self.plot3d(**kwds)

        def _plot_(
            self: _LatticePolytopeInterface,
            **kwds: "PlotOption",
        ) -> "Graphics3d":
            """Sage plotting hook."""
            return self.plot(**kwds)

        def invariants(self: _LatticePolytopeInterface) -> dict[str, object]:
            """Return a dictionary of fundamental invariants."""
            return {
                "dimension": self.dimension(),
                "volume": self.volume(),
                "normalized_volume": self.normalized_volume(),
                "n_integral_points": self.n_integral_points(),
                "n_boundary_points": self.n_boundary_points(),
                "n_interior_points": self.n_interior_points(),
                "is_lattice_polytope": self.is_lattice_polytope(),
            }


class LatticePolytopes(Category):
    """
    The category of integral lattice polytopes (polytopes whose vertices are lattice points).

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.polytopes import LatticePolytopes, ConvexPolytopes
        sage: LatticePolytopes()
        Category of lattice polytopes
        sage: LatticePolytopes().super_categories()
        [Category of convex polytopes]
    """
    def super_categories(self) -> list[Category]:
        return [ConvexPolytopes()]

    def _repr_object_names(self) -> str:
        return "lattice polytopes"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Lattice Polytopes}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """
        Specialized properties for integral lattice polytopes.
        """
        def __init__(
            self: Self,
            **rest: "ConstructionData",
        ) -> None:
            super().__init__(**rest)

        def _repr_(self: _LatticePolytopeInterface) -> str:
            return f"Lattice Polytope of dimension {self.dimension()} with {len(self.vertices())} vertices"

        @cached_method
        def is_reflexive(self: _LatticePolytopeInterface) -> bool:
            """Return True if P is a reflexive lattice polytope."""
            return bool(self.polyhedron().is_reflexive())

        @cached_method
        def is_smooth(self: _LatticePolytopeInterface) -> bool:
            """Return True if the normal fan of P is smooth (Delzant polytope)."""
            return bool(self.normal_fan().is_smooth())

        @cached_method
        def polar_dual(self: _LatticePolytopeInterface) -> Parent:
            """Return the polar dual polytope P*."""
            origin = self.ambient_space()([0] * self.dimension())
            assert self.polyhedron().interior_contains(origin), (
                "the polar dual is a polytope only when the origin is in the interior"
            )
            polar_vertices = tuple(
                tuple(coordinate for coordinate in vertex)
                for vertex in self.polyhedron().polar().vertices()
            )
            if all(coordinate in ZZ for vertex in polar_vertices for coordinate in vertex):
                return LatticePolytope(
                    polar_vertices,
                    lattice=self.ambient_space().dual(),
                )
            return ConvexPolytope(
                polar_vertices,
                lattice=self.ambient_space().dual(),
            )

        @cached_method
        def ehrhart_polynomial(self: _LatticePolytopeInterface):
            """Return the Ehrhart polynomial counting lattice points in dilations k*P."""
            return self.polyhedron().ehrhart_polynomial()

        @cached_method
        def h_star_vector(self: _LatticePolytopeInterface) -> tuple[Integer, ...]:
            r"""
            Return the coefficients of the h*-polynomial (Ehrhart delta-series).
            """
            return tuple(self.polyhedron().h_star_vector())


class ConvexPolygons(Category):
    r"""
    The category of 2-dimensional convex polytopes (convex polygons).

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.polytopes import ConvexPolygons, ConvexPolytopes
        sage: ConvexPolygons()
        Category of convex polygons
        sage: ConvexPolygons().super_categories()
        [Category of convex polytopes]
    """
    def super_categories(self) -> list[Category]:
        return [ConvexPolytopes()]

    def _repr_object_names(self) -> str:
        return "convex polygons"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Convex Polygons}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """
        Domain methods specialized for 2D convex polygons.
        """
        def _repr_(self: _LatticePolytopeInterface) -> str:
            return f"Convex Polygon with {len(self.vertices())} vertices"

        def _latex_(self: _LatticePolytopeInterface) -> str:
            verts_latex = ", ".join(f"({v[0]}, {v[1]})" for v in self.vertices())
            return fr"\text{{Polygon}}\left({verts_latex}\right)"

        def plot(
            self: _LatticePolytopeInterface,
            **kwds: "PlotOption",
        ) -> Graphics:
            return self._plot_2d(**kwds)

        def _plot_2d(self: _LatticePolytopeInterface, **kwds: object) -> Graphics:
            """
            Render a publication-quality Sage Graphics plot of the 2D polygon.
            """
            grid_line_color = kwds.get('grid_line_color', '#CBD5E1')
            grid_line_width = kwds.get('grid_line_width', 0.75)
            fill_color = kwds.get('fill_color', '#E0F2FE')
            fill_alpha = kwds.get('fill_alpha', 0.75)
            boundary_color = kwds.get('boundary_color', '#1E293B')
            boundary_width = kwds.get('boundary_width', 2.0)

            vertices = [tuple(v) for v in self.vertices()]
            all_pts = list(vertices)
            min_x = int(min(p[0] for p in all_pts) - 1)
            max_x = int(max(p[0] for p in all_pts) + 1)
            min_y = int(min(p[1] for p in all_pts) - 1)
            max_y = int(max(p[1] for p in all_pts) + 1)

            g_plot = Graphics()

            # Grid lines
            for gx in range(min_x, max_x + 1):
                g_plot += line([(gx, min_y), (gx, max_y)],
                               color=grid_line_color, thickness=grid_line_width,
                               linestyle=':', zorder=1)
            for gy in range(min_y, max_y + 1):
                g_plot += line([(min_x, gy), (max_x, gy)],
                               color=grid_line_color, thickness=grid_line_width,
                               linestyle=':', zorder=1)

            # Classify lattice points
            all_grid = [(gx, gy) for gx in range(min_x, max_x + 1)
                        for gy in range(min_y, max_y + 1)]
            int_pts = set(tuple(p) for p in self.interior_integral_points())
            bnd_pts = set(tuple(p) for p in self.boundary_integral_points())
            amb_pts = [pt for pt in all_grid if pt not in int_pts and pt not in bnd_pts]

            # Ambient points
            g_plot += point(amb_pts, pointsize=24, color='#94A3B8', alpha=0.5, zorder=2)

            # Polygon interior fill
            g_plot += polygon(vertices, color=fill_color, alpha=fill_alpha, zorder=3)

            # Polygon boundary edges
            poly = self.polyhedron()
            for f in poly.facets():
                v_facet = [tuple(v) for v in f.vertices()]
                if len(v_facet) >= 2:
                    g_plot += line([v_facet[0], v_facet[1]], color=boundary_color, thickness=boundary_width, zorder=4)

            # Interior points (emerald)
            if int_pts:
                g_plot += point(list(int_pts), pointsize=44, color='#059669', zorder=8)

            # Boundary points (obsidian)
            if bnd_pts:
                g_plot += point(list(bnd_pts), pointsize=48, color='#0F172A', zorder=9)

            # Configure axes with strictly integer ticks
            show_axes = kwds.get('axes', False)
            x_ticks = list(range(min_x, max_x + 1))
            y_ticks = list(range(min_y, max_y + 1))
            g_plot.axes(show_axes)
            g_plot.set_axes_range(min_x - 0.2, max_x + 0.2, min_y - 0.2, max_y + 0.2)
            g_plot.SHOW_OPTIONS['ticks'] = [x_ticks, y_ticks]
            g_plot.SHOW_OPTIONS['ticks_integer'] = True

            return g_plot

        def tikz(self: _LatticePolytopeInterface, scale: float = 0.8) -> str:
            """Return standard TikZ code for the polygon."""
            vertices = [tuple(v) for v in self.vertices()]
            min_x = int(min(p[0] for p in vertices) - 1)
            max_x = int(max(p[0] for p in vertices) + 1)
            min_y = int(min(p[1] for p in vertices) - 1)
            max_y = int(max(p[1] for p in vertices) + 1)

            header = [
                rf"\begin{{tikzpicture}}[scale={scale}, baseline]",
                r"\tikzset{poly vertex/.style={circle, fill=black, inner sep=2pt}}",
                r"\tikzset{interior point/.style={circle, fill=teal, inner sep=1.8pt}}",
            ]
            grid_lines = [
                rf"\draw[dotted, lightgray] ({min_x},{min_y}) grid ({max_x},{max_y});",
                rf"\foreach \x in {{{min_x},...,{max_x}}} \foreach \y in {{{min_y},...,{max_y}}} \fill[darkgray] (\x,\y) circle (1pt);",
            ]
            poly_path = " -- ".join(f"({v[0]},{v[1]})" for v in vertices) + " -- cycle"
            poly_lines = [
                rf"\fill[fill=gray!12] {poly_path};",
                rf"\draw[black, thick] {poly_path};",
            ]
            int_lines = [rf"\node[interior point] at ({p[0]},{p[1]}) {{}};" for p in self.interior_integral_points()]
            bnd_lines = [rf"\node[poly vertex] at ({p[0]},{p[1]}) {{}};" for p in self.boundary_integral_points()]

            return "\n".join([
                *header,
                *grid_lines,
                *poly_lines,
                *int_lines,
                *bnd_lines,
                r"\end{tikzpicture}",
            ])

        def _tikz_(self: _LatticePolytopeInterface) -> str:
            return self.tikz()


class LatticePolygons(Category):
    r"""
    The category of 2-dimensional integral lattice polygons.

    EXAMPLES::

        sage: from dzack_research.preamble.categories.schemes.polytopes import (
        ....:     LatticePolygons, ConvexPolygons, LatticePolytopes
        ....: )
        sage: LatticePolygons()
        Category of lattice polygons
        sage: LatticePolygons().super_categories()
        [Category of convex polygons, Category of lattice polytopes]
    """
    def super_categories(self) -> list[Category]:
        return [ConvexPolygons(), LatticePolytopes()]

    def _repr_object_names(self) -> str:
        return "lattice polygons"

    def _latex_(self) -> str:
        return r"\mathbf{Cat}\left(\text{Lattice Polygons}\right)"

    def _repr_latex_(self) -> str:
        return "$\\displaystyle " + self._latex_() + "$"

    class ParentMethods:
        """
        A 2-dimensional integral lattice polygon Q \\subset N.
        """
        def _repr_(self: _LatticePolytopeInterface) -> str:
            return f"Lattice Polygon with {len(self.vertices())} vertices"


def _vertex_dimension(
    vertices: Sequence[Sequence[LatticeCoord]] | Polyhedron | Parent,
) -> int:
    """Return the number of coordinates a vertex of ``vertices`` has."""
    if isinstance(vertices, Polyhedron):
        raw_verts = [list(v) for v in vertices.vertices()]
    elif isinstance(vertices, Parent) and vertices in ConvexPolytopes():
        poly = vertices.polyhedron()
        raw_verts = [list(v) for v in poly.vertices()]
    else:
        raw_verts = [list(v) for v in vertices]
    return len(raw_verts[0]) if raw_verts else 0


def ConvexPolytope(
    vertices: Sequence[Sequence[LatticeCoord]] | Polyhedron | Parent,
    lattice: Optional[ToricLattice_generic] = None,
    base_ring: object = QQ,
    category: Optional[Category] = None,
) -> Parent:
    r"""Return the convex polytope P \subset N_\RR spanned by ``vertices``."""
    if category is None:
        category = ConvexPolygons() if _vertex_dimension(vertices) == 2 else ConvexPolytopes()
    return object_of(
        category, vertices=vertices, lattice=lattice, base_ring=base_ring
    )


def ConvexPolygon(
    vertices: Sequence[Sequence[LatticeCoord]],
    lattice: Optional[ToricLattice_generic] = None,
    base_ring: object = QQ,
    category: Optional[Category] = None,
) -> Parent:
    r"""Return the 2-dimensional convex polygon in N_\RR spanned by ``vertices``."""
    return object_of(
        category or ConvexPolygons(),
        vertices=vertices,
        lattice=lattice,
        base_ring=base_ring,
    )


def LatticePolytope(
    vertices: Sequence[Sequence[LatticeCoord]] | Polyhedron | Parent,
    lattice: Optional[ToricLattice_generic] = None,
    base_ring: object = ZZ,
    category: Optional[Category] = None,
) -> Parent:
    r"""Return the integral lattice polytope P \subset N spanned by ``vertices``."""
    if category is None:
        category = LatticePolygons() if _vertex_dimension(vertices) == 2 else LatticePolytopes()
    return object_of(
        category, vertices=vertices, lattice=lattice, base_ring=base_ring
    )


def LatticePolygon(
    vertices: Sequence[Sequence[LatticeCoord]] | Polyhedron | Parent,
    lattice: Optional[ToricLattice_generic] = None,
) -> Parent:
    r"""Return the 2-dimensional integral lattice polygon Q \subset N."""
    return object_of(
        LatticePolygons(), vertices=vertices, lattice=lattice, base_ring=ZZ
    )
