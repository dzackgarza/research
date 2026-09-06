r"""Views of lattice polytopes: an SVG picture of a polygon, an HTML page of a
three-dimensional polytope.

This is presentation support, not mathematics.  Nothing here decides anything
about a polytope: each function asks a live owned object for what it already
knows and lays the answer out.  No display hook is installed and no rich
representation is attached to any mathematical class -- a session calls these
when it wants a picture, and the objects are unchanged when it does not.

Implicit typesetting of a bare result in a notebook cell is owned elsewhere,
by the tracked ``sage-init.sage`` at the repository root; this module does not
touch the display formatter.

The drawing cores take plain coordinate pairs so they can be exercised and
looked at without a session.
"""

from fractions import Fraction

_PALETTE = {
    "grid": "#d8dee9",
    "edge": "#2e3440",
    "face": "#eceff4",
    "highlight": "#bf616a",
    "interior": "#5e81ac",
    "boundary": "#ffffff",
    "distinguished": "#d08770",
}


def _as_float(coordinate) -> float:
    r"""One coordinate as a drawing number, exactly through a rational."""
    return float(Fraction(str(coordinate)))


def _plane_point(point):
    x, y = tuple(point)
    return (_as_float(x), _as_float(y))


def _bounds(points):
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    return (min(xs), min(ys), max(xs), max(ys))


def _polygon_svg_document(
    vertices,
    interior_points=(),
    boundary_points=(),
    highlighted_sides=(),
    distinguished_point=None,
    size=420,
):
    r"""An SVG picture of one convex polygon with its lattice points.

    ``vertices`` are in boundary order.  ``highlighted_sides`` are pairs of
    positions in that order; they are stroked in the highlight colour, which
    is how the sides of an ADE polygon through the distinguished point are
    told apart from the rest.  The vertical axis is flipped so the picture
    reads the way the plane does.
    """
    vertices = tuple(vertices)
    margin = 1.0
    left, bottom, right, top = _bounds(
        (*vertices, *interior_points, *boundary_points)
    )
    left, bottom = left - margin, bottom - margin
    right, top = right + margin, top + margin
    width, height = right - left, top - bottom
    scale = size / max(width, height)

    def place(point):
        x, y = point
        return ((x - left) * scale, (top - y) * scale)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width * scale:.1f}" '
        f'height="{height * scale:.1f}" viewBox="0 0 {width * scale:.1f} '
        f'{height * scale:.1f}">'
    ]

    path = " ".join(
        f"{'M' if position == 0 else 'L'} {place(vertex)[0]:.1f} {place(vertex)[1]:.1f}"
        for position, vertex in enumerate(vertices)
    )
    parts.append(
        f'<path d="{path} Z" fill="{_PALETTE["face"]}" '
        f'stroke="{_PALETTE["edge"]}" stroke-width="2"/>'
    )

    # After the face, so the lattice stays legible inside the polygon too.
    for column in range(int(left) - 1, int(right) + 2):
        for row in range(int(bottom) - 1, int(top) + 2):
            x, y = place((column, row))
            parts.append(
                f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.8" fill="{_PALETTE["grid"]}"/>'
            )

    for first, second in highlighted_sides:
        start, end = place(vertices[first]), place(vertices[second])
        parts.append(
            f'<line x1="{start[0]:.1f}" y1="{start[1]:.1f}" '
            f'x2="{end[0]:.1f}" y2="{end[1]:.1f}" '
            f'stroke="{_PALETTE["highlight"]}" stroke-width="4" '
            f'stroke-linecap="round"/>'
        )

    for point in boundary_points:
        x, y = place(point)
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{_PALETTE["boundary"]}" '
            f'stroke="{_PALETTE["edge"]}" stroke-width="1.5"/>'
        )
    for point in interior_points:
        x, y = place(point)
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="{_PALETTE["interior"]}"/>'
        )

    if distinguished_point is not None:
        x, y = place(distinguished_point)
        parts.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.5" '
            f'fill="{_PALETTE["distinguished"]}" stroke="{_PALETTE["edge"]}" '
            f'stroke-width="1.5"/>'
        )

    parts.append("</svg>")
    return "".join(parts)


def _polytope_html_document(vertices, title, size=600):
    r"""A self-contained page showing the convex hull of the stated points.

    The hull is built by three.js's own ``ConvexGeometry``, so no facet
    ordering or triangulation is computed here.
    """
    points = ", ".join(
        f"new THREE.Vector3({x:.6f}, {y:.6f}, {z:.6f})" for x, y, z in vertices
    )
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>body{{margin:0;background:{_PALETTE["face"]}}}canvas{{display:block}}</style>
</head><body>
<script type="importmap">
{{"imports": {{"three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
 "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}}}
</script>
<script type="module">
import * as THREE from 'three';
import {{ OrbitControls }} from 'three/addons/controls/OrbitControls.js';
import {{ ConvexGeometry }} from 'three/addons/geometries/ConvexGeometry.js';

const points = [{points}];
const scene = new THREE.Scene();
scene.background = new THREE.Color('{_PALETTE["face"]}');
const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({{antialias: true}});
renderer.setSize({size}, {size});
document.body.appendChild(renderer.domElement);

const geometry = new ConvexGeometry(points);
scene.add(new THREE.Mesh(geometry, new THREE.MeshStandardMaterial(
    {{color: '{_PALETTE["interior"]}', transparent: true, opacity: 0.75,
      side: THREE.DoubleSide}})));
scene.add(new THREE.LineSegments(new THREE.EdgesGeometry(geometry),
    new THREE.LineBasicMaterial({{color: '{_PALETTE["edge"]}'}})));
for (const point of points) {{
    const dot = new THREE.Mesh(new THREE.SphereGeometry(0.06, 16, 16),
        new THREE.MeshStandardMaterial({{color: '{_PALETTE["highlight"]}'}}));
    dot.position.copy(point);
    scene.add(dot);
}}

scene.add(new THREE.AmbientLight(0xffffff, 0.7));
const lamp = new THREE.DirectionalLight(0xffffff, 0.8);
lamp.position.set(4, 6, 8);
scene.add(lamp);

const box = new THREE.Box3().setFromPoints(points);
const centre = box.getCenter(new THREE.Vector3());
const radius = box.getSize(new THREE.Vector3()).length();
camera.position.copy(centre).add(new THREE.Vector3(radius, radius, radius));
const controls = new OrbitControls(camera, renderer.domElement);
controls.target.copy(centre);
controls.update();
renderer.setAnimationLoop(() => renderer.render(scene, camera));
</script></body></html>
"""


def polygon_svg(polygon, highlighted_sides=(), distinguished_point=None, size=420):
    r"""An SVG picture of a two-dimensional convex polytope.

    The polygon answers for its own vertices and, when it is integral, for its
    interior and boundary lattice points; this only lays them out.
    """
    assert int(polygon.dimension()) == 2, "this view draws a polygon"
    assert polygon.n_vertices() >= 3, "a polygon has at least three vertices"
    vertices = tuple(_plane_point(vertex) for vertex in polygon.vertices())
    if polygon.is_lattice_polytope():
        interior = tuple(_plane_point(point) for point in polygon.interior_integral_points())
        boundary = tuple(_plane_point(point) for point in polygon.boundary_integral_points())
    else:
        interior, boundary = (), ()
    return _polygon_svg_document(
        vertices,
        interior_points=interior,
        boundary_points=boundary,
        highlighted_sides=tuple(highlighted_sides),
        distinguished_point=(
            None if distinguished_point is None else _plane_point(distinguished_point)
        ),
        size=size,
    )


def ade_polygon_svg(ade_log_pair, size=420):
    r"""The polygon of an ADE log pair, with ``p*`` and its decorated sides."""
    sides = tuple(
        tuple(
            int(vertex)
            for vertex in ade_log_pair.side_decorations()[position].side
        )
        for position in ade_log_pair.side_decorations().index_set()
    )
    return polygon_svg(
        ade_log_pair.polygon(),
        highlighted_sides=sides,
        distinguished_point=ade_log_pair.distinguished_point(),
        size=size,
    )


def polytope_html(polytope, title="Polytope", size=600):
    r"""A page showing a three-dimensional convex polytope, rotatable."""
    assert int(polytope.dimension()) == 3, "this view draws a three-dimensional polytope"
    vertices = tuple(
        tuple(_as_float(coordinate) for coordinate in vertex)
        for vertex in polytope.vertices()
    )
    return _polytope_html_document(vertices, title, size=size)


__all__ = ["ade_polygon_svg", "polygon_svg", "polytope_html"]
