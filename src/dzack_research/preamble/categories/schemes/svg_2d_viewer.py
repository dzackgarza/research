r"""
High-definition 2D SVG Generator for Lattice Polygons and ADE Base Log Pairs.

Provides crisp vector graphics matching the visual aesthetic of the 3D Three.js viewer:
- Anti-aliased integer lattice grid with coordinate axes and ticks
- Glassmorphic polygon fill with subtle gradient and glowing boundary edges
- Distinguished Blue Line boundary divisor C
- Radiant crimson star for distinguished point p*
- Colored lattice point classification (Emerald interior, Obsidian boundary, Azure C-points, Slate ambient)
- Long/Short side pill badges and centered LaTeX labels
- Embedded Dynkin diagram visualization support
- Interactive SVG tooltips for all lattice points
"""

import io
import math
import re
from typing import Any, Mapping, Optional, Sequence, Tuple


def _format_monomial_2d(x: float, y: float, var_x: str = "x", var_y: str = "y") -> str:
    """Format an integer lattice point (x, y) into its corresponding standard Laurent character/monomial."""
    ix = int(round(float(x)))
    iy = int(round(float(y)))
    superscripts = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹',
        '-': '⁻'
    }
    def sup(n: int) -> str:
        if n == 1:
            return ""
        return "".join(superscripts.get(c, c) for c in str(n))

    parts = []
    if ix != 0:
        parts.append(f"{var_x}{sup(ix)}")
    if iy != 0:
        parts.append(f"{var_y}{sup(iy)}")
    if not parts:
        return "1"
    return "".join(parts)


def _star_path(cx: float, cy: float, r_outer: float, r_inner: float, points: int = 5) -> str:
    """Generate SVG path data for a regular star centered at (cx, cy)."""
    coords = []
    angle_step = math.pi / points
    start_angle = -math.pi / 2
    for i in range(2 * points):
        r = r_outer if i % 2 == 0 else r_inner
        angle = start_angle + i * angle_step
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        coords.append(f"{x:.2f},{y:.2f}")
    return "M " + " L ".join(coords) + " Z"


def _latex_to_svg_group(tex_str: str, cx: float, cy: float, color: str = "#F8FAFC", fontsize: float = 14) -> str:
    """Render a LaTeX math formula into an embedded vector SVG group centered at (cx, cy)."""
    if not tex_str:
        return ""
    try:
        import matplotlib.pyplot as plt
        math_str = "$" + tex_str.strip("$") + "$"
        fig = plt.figure(figsize=(2, 0.8))
        fig.text(0.5, 0.5, math_str, fontsize=fontsize, color=color, ha="center", va="center")
        buf = io.StringIO()
        fig.savefig(buf, format="svg", transparent=True, bbox_inches="tight", pad_inches=0.01)
        plt.close(fig)
        svg_data = buf.getvalue()

        w_match = re.search(r'width="([^"]+)"', svg_data)
        h_match = re.search(r'height="([^"]+)"', svg_data)
        w = float(re.sub(r'[^\d.]', '', w_match.group(1))) if w_match else 30.0
        h = float(re.sub(r'[^\d.]', '', h_match.group(1))) if h_match else 20.0

        start_idx = svg_data.find("<svg")
        if start_idx != -1:
            inner_svg = svg_data[start_idx:]
            return f'<g transform="translate({cx - w/2:.1f}, {cy - h/2:.1f})">{inner_svg}</g>'
        return ""
    except Exception:
        clean = tex_str.replace("$", "")
        return f'<text x="{cx:.1f}" y="{cy + 4.5:.1f}" fill="{color}" font-size="{fontsize}" font-weight="700" text-anchor="middle">{clean}</text>'


def generate_2d_polygon_svg(
    vertices: Sequence[Sequence[float]],
    *,
    interior_points: Sequence[Sequence[float]] = (),
    boundary_points: Sequence[Sequence[float]] = (),
    distinguished_points: Sequence[Sequence[float]] = (),
    blue_facets: Sequence[Sequence[Sequence[float]]] = (),
    p_star: Optional[Sequence[float]] = None,
    side_decorations: Optional[Mapping[str, Any]] = None,
    latex_label: str = "",
    dynkin_data: Optional[Mapping[str, Any]] = None,
    theme: str = "dark",
    width: int = 520,
    height: int = 420,
    padding: float = 1.2,
) -> str:
    """
    Generate an ultra-crisp, publication-grade SVG for a 2D lattice polygon.
    """
    # 1. Compute Coordinate Bounds
    all_x = [float(v[0]) for v in vertices]
    all_y = [float(v[1]) for v in vertices]
    if p_star:
        all_x.append(float(p_star[0]))
        all_y.append(float(p_star[1]))

    min_x_val = min(all_x) if all_x else 0.0
    max_x_val = max(all_x) if all_x else 1.0
    min_y_val = min(all_y) if all_y else 0.0
    max_y_val = max(all_y) if all_y else 1.0

    x_min = int(math.floor(min_x_val - padding))
    x_max = int(math.ceil(max_x_val + padding))
    y_min = int(math.floor(min_y_val - padding))
    y_max = int(math.ceil(max_y_val + padding))

    span_x = max(1, x_max - x_min)
    span_y = max(1, y_max - y_min)

    margin = 44.0
    usable_w = width - 2 * margin
    usable_h = height - 2 * margin

    scale_x = usable_w / span_x
    scale_y = usable_h / span_y
    scale = min(scale_x, scale_y)

    origin_x = margin + (usable_w - span_x * scale) / 2.0 - x_min * scale
    origin_y = height - margin - (usable_h - span_y * scale) / 2.0 + y_min * scale

    def to_svg(x: float, y: float) -> Tuple[float, float]:
        return (origin_x + float(x) * scale, origin_y - float(y) * scale)

    # 2. Palette Definitions
    is_dark = (theme == "dark")
    bg_color = "#07090E" if is_dark else "#FFFFFF"
    border_color = "#1E293B" if is_dark else "#E2E8F0"
    grid_color = "rgba(51, 65, 85, 0.45)" if is_dark else "rgba(226, 232, 240, 0.9)"
    axis_color = "#475569" if is_dark else "#94A3B8"
    axis_text_color = "#64748B" if is_dark else "#64748B"

    poly_stroke = "#0284C7" if is_dark else "#0369A1"
    blue_line_stroke = "#38BDF8" if is_dark else "#2563EB"

    amb_point_color = "#334155" if is_dark else "#CBD5E1"
    bnd_point_color = "#F8FAFC" if is_dark else "#0F172A"
    int_point_color = "#10B981"
    dist_point_color = "#38BDF8" if is_dark else "#2563EB"
    p_star_color = "#EF4444"

    svg_parts = []
    svg_parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="100%" height="{height}" style="background: {bg_color}; border-radius: 12px; '
        f'border: 1px solid {border_color}; box-shadow: 0 10px 30px rgba(0,0,0,0.4); font-family: -apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif;">'
    )

    # SVG Defs (Gradients, Filters, Markers, CSS Hover Lighting)
    svg_parts.append(
        """<defs>
            <style>
                .lattice-node {
                    cursor: pointer;
                    transition: transform 0.15s ease, r 0.15s ease, filter 0.15s ease, stroke 0.15s ease, stroke-width 0.15s ease;
                    transform-origin: center;
                    transform-box: fill-box;
                }
                .lattice-node:hover {
                    r: 7.5px !important;
                    filter: drop-shadow(0 0 6px #38BDF8) brightness(1.35);
                    stroke: #38BDF8 !important;
                    stroke-width: 2.4px !important;
                }
                .pstar-node {
                    cursor: pointer;
                    transition: transform 0.15s ease, filter 0.15s ease;
                    transform-origin: center;
                    transform-box: fill-box;
                }
                .pstar-node:hover {
                    transform: scale(1.35);
                    filter: drop-shadow(0 0 10px #EF4444) brightness(1.35);
                }
            </style>
            <filter id="pStarGlow" x="-50%" y="-50%" width="200%" height="200%">
                <feGaussianBlur stdDeviation="3.5" result="blur" />
                <feMerge>
                    <feMergeNode in="blur" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
            <filter id="blueLineGlow" x="-30%" y="-30%" width="160%" height="160%">
                <feGaussianBlur stdDeviation="2.0" result="blur" />
                <feMerge>
                    <feMergeNode in="blur" />
                    <feMergeNode in="SourceGraphic" />
                </feMerge>
            </filter>
            <linearGradient id="polyGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.22" />
                <stop offset="100%" stop-color="#0284C7" stop-opacity="0.06" />
            </linearGradient>
            <marker id="axisArrowX" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#EF4444" />
            </marker>
            <marker id="axisArrowY" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#22C55E" />
            </marker>
        </defs>"""
    )

    # 3. Grid Lines
    svg_parts.append('<g id="grid_lines">')
    for gx in range(x_min, x_max + 1):
        x1, y1 = to_svg(gx, y_min)
        x2, y2 = to_svg(gx, y_max)
        svg_parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{grid_color}" stroke-width="1" stroke-dasharray="2 3" />'
        )
    for gy in range(y_min, y_max + 1):
        x1, y1 = to_svg(x_min, gy)
        x2, y2 = to_svg(x_max, gy)
        svg_parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{grid_color}" stroke-width="1" stroke-dasharray="2 3" />'
        )
    svg_parts.append('</g>')

    # 4. Coordinate Axes (X in red, Y in green)
    ax_x1, ax_y0 = to_svg(x_min, 0)
    ax_x2, _ = to_svg(x_max + 0.35, 0)
    ax_x0, ax_y1 = to_svg(0, y_min)
    _, ax_y2 = to_svg(0, y_max + 0.35)

    svg_parts.append(
        f'<line x1="{ax_x1:.1f}" y1="{ax_y0:.1f}" x2="{ax_x2:.1f}" y2="{ax_y0:.1f}" '
        f'stroke="#EF4444" stroke-width="1.6" stroke-opacity="0.8" marker-end="url(#axisArrowX)" />'
    )
    svg_parts.append(
        f'<line x1="{ax_x0:.1f}" y1="{ax_y1:.1f}" x2="{ax_x0:.1f}" y2="{ax_y2:.1f}" '
        f'stroke="#22C55E" stroke-width="1.6" stroke-opacity="0.8" marker-end="url(#axisArrowY)" />'
    )

    # Axis Labels
    svg_parts.append(
        f'<text x="{ax_x2 + 8:.1f}" y="{ax_y0 + 4:.1f}" fill="#EF4444" font-size="12" font-weight="700">X</text>'
    )
    svg_parts.append(
        f'<text x="{ax_x0 - 4:.1f}" y="{ax_y2 - 8:.1f}" fill="#22C55E" font-size="12" font-weight="700">Y</text>'
    )

    # Tick Numbers
    for gx in range(x_min, x_max + 1):
        if gx == 0:
            continue
        tx, ty = to_svg(gx, 0)
        svg_parts.append(
            f'<line x1="{tx:.1f}" y1="{ty - 3:.1f}" x2="{tx:.1f}" y2="{ty + 3:.1f}" stroke="{axis_color}" stroke-width="1.2" />'
            f'<text x="{tx:.1f}" y="{ty + 15:.1f}" fill="{axis_text_color}" font-size="10" font-family="monospace" text-anchor="middle">{gx}</text>'
        )
    for gy in range(y_min, y_max + 1):
        if gy == 0:
            continue
        tx, ty = to_svg(0, gy)
        svg_parts.append(
            f'<line x1="{tx - 3:.1f}" y1="{ty:.1f}" x2="{tx + 3:.1f}" y2="{ty:.1f}" stroke="{axis_color}" stroke-width="1.2" />'
            f'<text x="{tx - 8:.1f}" y="{ty + 3.5:.1f}" fill="{axis_text_color}" font-size="10" font-family="monospace" text-anchor="end">{gy}</text>'
        )

    # 5. Ambient Lattice Points
    int_set = set((float(p[0]), float(p[1])) for p in interior_points)
    bnd_set = set((float(p[0]), float(p[1])) for p in boundary_points)
    v_set = set((float(v[0]), float(v[1])) for v in vertices)
    dist_set = set((float(p[0]), float(p[1])) for p in distinguished_points)

    svg_parts.append('<g id="ambient_points">')
    for gx in range(x_min, x_max + 1):
        for gy in range(y_min, y_max + 1):
            pt = (float(gx), float(gy))
            if pt not in int_set and pt not in bnd_set and pt not in v_set:
                px, py = to_svg(gx, gy)
                svg_parts.append(
                    f'<circle class="lattice-node" cx="{px:.1f}" cy="{py:.1f}" r="2.4" fill="{amb_point_color}" opacity="0.4">'
                    f'<title>({gx}, {gy}) : {_format_monomial_2d(gx, gy)}</title></circle>'
                )
    svg_parts.append('</g>')

    # 6. Polygon Interior & Standard Edges
    if vertices:
        poly_pts_str = " ".join(f"{to_svg(v[0], v[1])[0]:.1f},{to_svg(v[0], v[1])[1]:.1f}" for v in vertices)
        svg_parts.append(
            f'<polygon points="{poly_pts_str}" fill="url(#polyGrad)" stroke="{poly_stroke}" stroke-width="1.8" '
            f'stroke-linejoin="round" />'
        )

    # 7. Blue Line Boundary Facets (C)
    if blue_facets:
        svg_parts.append('<g id="blue_facets">')
        deco_map = {}
        if side_decorations:
            for deco in side_decorations.values():
                edge = getattr(deco, 'edge', ())
                dtype = getattr(deco, 'decoration_type', '')
                if len(edge) >= 2 and edge[0] < len(vertices) and edge[1] < len(vertices):
                    v1_t = (float(vertices[edge[0]][0]), float(vertices[edge[0]][1]))
                    v2_t = (float(vertices[edge[1]][0]), float(vertices[edge[1]][1]))
                    deco_map[frozenset([v1_t, v2_t])] = dtype

        for facet in blue_facets:
            if len(facet) >= 2:
                p1_val = (float(facet[0][0]), float(facet[0][1]))
                p2_val = (float(facet[1][0]), float(facet[1][1]))
                p1 = to_svg(p1_val[0], p1_val[1])
                p2 = to_svg(p2_val[0], p2_val[1])
                dtype = deco_map.get(frozenset([p1_val, p2_val]), "")
                title_elem = f'<title>{dtype}</title>' if dtype else ''

                # Glow underlay
                svg_parts.append(
                    f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" '
                    f'stroke="{blue_line_stroke}" stroke-width="7" stroke-opacity="0.3" stroke-linecap="round" filter="url(#blueLineGlow)">'
                    f'{title_elem}</line>'
                )
                # Core vibrant line
                svg_parts.append(
                    f'<line x1="{p1[0]:.1f}" y1="{p1[1]:.1f}" x2="{p2[0]:.1f}" y2="{p2[1]:.1f}" '
                    f'stroke="{blue_line_stroke}" stroke-width="3.6" stroke-linecap="round">'
                    f'{title_elem}</line>'
                )
        svg_parts.append('</g>')

    # 8. Dynkin Diagram Visualization (if present)
    if dynkin_data:
        edges = dynkin_data.get('edges', [])
        node_types = dynkin_data.get('node_types', {})
        svg_parts.append('<g id="dynkin_diagram">')
        for e in edges:
            if len(e) >= 2:
                dp1 = to_svg(e[0][0], e[0][1])
                dp2 = to_svg(e[1][0], e[1][1])
                svg_parts.append(
                    f'<line x1="{dp1[0]:.1f}" y1="{dp1[1]:.1f}" x2="{dp2[0]:.1f}" y2="{dp2[1]:.1f}" '
                    f'stroke="#6366F1" stroke-width="2.8" stroke-linecap="round" />'
                )
        for n, ntype in node_types.items():
            nx, ny = to_svg(n[0], n[1])
            if ntype == 'black':
                svg_parts.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="5.0" fill="#0F172A" stroke="#6366F1" stroke-width="1.5" />')
            elif ntype == 'white':
                svg_parts.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="5.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="2" />')
            elif ntype == 'circled_white':
                svg_parts.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="8.0" fill="none" stroke="#6366F1" stroke-width="1.8" />')
                svg_parts.append(f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="4.5" fill="#FFFFFF" stroke="#0F172A" stroke-width="1.8" />')
        svg_parts.append('</g>')

    # 9. Boundary Integral Points
    svg_parts.append('<g id="boundary_points">')
    for p in boundary_points:
        pt = (float(p[0]), float(p[1]))
        mon_str = _format_monomial_2d(p[0], p[1])
        px, py = to_svg(p[0], p[1])
        if pt in dist_set:
            svg_parts.append(
                f'<circle class="lattice-node" cx="{px:.1f}" cy="{py:.1f}" r="5.2" fill="{dist_point_color}" stroke="#0F172A" stroke-width="1.4" '
                f'onmouseenter="showSvgTip(evt, \'({p[0]}, {p[1]})\', \'{mon_str}\', false)" onmouseleave="hideSvgTip(evt)">'
                f'<title>({p[0]}, {p[1]}) ⟶ {mon_str}</title></circle>'
            )
        elif pt not in v_set:
            svg_parts.append(
                f'<circle class="lattice-node" cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{bnd_point_color}" stroke="#334155" stroke-width="1.2" '
                f'onmouseenter="showSvgTip(evt, \'({p[0]}, {p[1]})\', \'{mon_str}\', false)" onmouseleave="hideSvgTip(evt)">'
                f'<title>({p[0]}, {p[1]}) ⟶ {mon_str}</title></circle>'
            )
    svg_parts.append('</g>')

    # 10. Interior Integral Points (Emerald)
    svg_parts.append('<g id="interior_points">')
    for p in interior_points:
        px, py = to_svg(p[0], p[1])
        mon_str = _format_monomial_2d(p[0], p[1])
        svg_parts.append(
            f'<circle class="lattice-node" cx="{px:.1f}" cy="{py:.1f}" r="4.8" fill="{int_point_color}" stroke="#065F46" stroke-width="1.4" '
            f'onmouseenter="showSvgTip(evt, \'({p[0]}, {p[1]})\', \'{mon_str}\', false)" onmouseleave="hideSvgTip(evt)">'
            f'<title>({p[0]}, {p[1]}) ⟶ {mon_str}</title></circle>'
        )
    svg_parts.append('</g>')

    # 11. Vertices
    svg_parts.append('<g id="vertices">')
    white_vertices = set()
    if side_decorations:
        for deco in side_decorations.values():
            if getattr(deco, 'vertex_color', '') == 'white' or getattr(deco, 'decoration_type', '') == 'long':
                for vi in getattr(deco, 'edge', ()):
                    if vi < len(vertices):
                        white_vertices.add((float(vertices[vi][0]), float(vertices[vi][1])))

    for v in vertices:
        vx, vy = to_svg(v[0], v[1])
        mon_str = _format_monomial_2d(v[0], v[1])
        if (float(v[0]), float(v[1])) in white_vertices:
            svg_parts.append(
                f'<circle class="lattice-node" cx="{vx:.1f}" cy="{vy:.1f}" r="6.0" fill="#FFFFFF" stroke="#0F172A" stroke-width="2.2" '
                f'onmouseenter="showSvgTip(evt, \'({v[0]}, {v[1]})\', \'{mon_str}\', false)" onmouseleave="hideSvgTip(evt)">'
                f'<title>({v[0]}, {v[1]}) ⟶ {mon_str}</title></circle>'
            )
        else:
            svg_parts.append(
                f'<circle class="lattice-node" cx="{vx:.1f}" cy="{vy:.1f}" r="5.2" fill="{bnd_point_color}" stroke="#0F172A" stroke-width="1.6" '
                f'onmouseenter="showSvgTip(evt, \'({v[0]}, {v[1]})\', \'{mon_str}\', false)" onmouseleave="hideSvgTip(evt)">'
                f'<title>({v[0]}, {v[1]}) ⟶ {mon_str}</title></circle>'
            )
    svg_parts.append('</g>')

    # 12. Distinguished Point p* (Radiant Crimson Star)
    if p_star:
        px, py = to_svg(p_star[0], p_star[1])
        star_d = _star_path(px, py, r_outer=10.0, r_inner=4.5, points=5)
        p_mon_str = _format_monomial_2d(p_star[0], p_star[1])
        svg_parts.append(
            f'<g id="p_star" filter="url(#pStarGlow)">'
            f'<path class="pstar-node" d="{star_d}" fill="{p_star_color}" stroke="#FFFFFF" stroke-width="1.2" '
            f'data-cx="{px:.1f}" data-cy="{py:.1f}" '
            f'onmouseenter="showSvgTip(evt, \'({p_star[0]}, {p_star[1]})\', \'{p_mon_str}\', true)" onmouseleave="hideSvgTip(evt)">'
            f'<title>p* = ({p_star[0]}, {p_star[1]}) ⟶ {p_mon_str}</title></path>'
            f'</g>'
        )

    # 14. Centered Math Label
    if latex_label and vertices:
        cx_val = sum(float(v[0]) for v in vertices) / len(vertices)
        cy_val = sum(float(v[1]) for v in vertices) / len(vertices)
        lx, ly = to_svg(cx_val, cy_val)
        lbl_svg = _latex_to_svg_group(latex_label, lx, ly, color="#F8FAFC", fontsize=15)
        if lbl_svg:
            svg_parts.append(lbl_svg)

    # 15. Dynamic Floating SVG Tooltip Card
    svg_parts.append(
        """<g id="svg_tip_overlay" visibility="hidden" pointer-events="none">
            <rect id="svg_tip_box" x="0" y="0" width="118" height="28" rx="6" fill="#0F172A" fill-opacity="0.94" stroke="#38BDF8" stroke-width="1.2" filter="url(#blueLineGlow)"/>
            <text id="svg_tip_coord" x="10" y="19" fill="#F8FAFC" font-size="12" font-weight="700" font-family="monospace">(0, 0)</text>
            <text id="svg_tip_arrow" x="58" y="19" fill="#64748B" font-size="12">⟶</text>
            <text id="svg_tip_mon" x="76" y="19" fill="#38BDF8" font-size="14" font-weight="700" font-style="italic" font-family="serif">1</text>
        </g>
        <script type="text/javascript">
        <![CDATA[
        function showSvgTip(evt, coord, mon, isPStar) {
            var svg = evt.target.ownerSVGElement;
            if (!svg) return;
            var tip = svg.getElementById('svg_tip_overlay');
            var tCoord = svg.getElementById('svg_tip_coord');
            var tArrow = svg.getElementById('svg_tip_arrow');
            var tMon = svg.getElementById('svg_tip_mon');
            var tBox = svg.getElementById('svg_tip_box');
            if (!tip || !tCoord || !tMon || !tBox) return;

            tCoord.textContent = isPStar ? 'p* ' + coord : coord;
            tMon.textContent = mon;
            tMon.setAttribute('fill', isPStar ? '#F87171' : '#38BDF8');
            tBox.setAttribute('stroke', isPStar ? '#EF4444' : '#38BDF8');

            var coordLen = tCoord.textContent.length;
            var monLen = mon.length;
            var arrowX = 10 + coordLen * 7.5 + 4;
            tArrow.setAttribute('x', arrowX);
            var monX = arrowX + 18;
            tMon.setAttribute('x', monX);
            var boxW = monX + monLen * 9 + 12;
            tBox.setAttribute('width', Math.max(90, boxW));

            var cx = parseFloat(evt.target.getAttribute('cx') || evt.target.getAttribute('data-cx') || 0);
            var cy = parseFloat(evt.target.getAttribute('cy') || evt.target.getAttribute('data-cy') || 0);
            tip.setAttribute('transform', 'translate(' + Math.max(10, cx - boxW / 2) + ',' + (cy - 36) + ')');
            tip.setAttribute('visibility', 'visible');
        }
        function hideSvgTip(evt) {
            var svg = evt.target.ownerSVGElement;
            if (!svg) return;
            var tip = svg.getElementById('svg_tip_overlay');
            if (tip) tip.setAttribute('visibility', 'hidden');
        }
        ]]>
        </script>"""
    )

    svg_parts.append('</svg>')
    return "\n".join(svg_parts)
