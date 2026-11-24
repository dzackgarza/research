import {
  key,
  nativePoint,
  plotPoint,
  type Model,
  type Point,
  type Rect,
} from "./sequence";
import { differential, inside, termStatus } from "./differentials";
import { math } from "./math";
import { clipPolyline } from "lineclip";
import type { Relation } from "./sequence";
export const coord = (t: Point) => "(" + key(t) + ")";
export function diagram(
  m: Model,
  r: Rect,
  selected: Point,
  mode: string,
  zeroStyle: string,
  arrowSelected: boolean,
  active: string | undefined,
  choose: (
    t: Point,
    arrow?: boolean,
    active?: string,
    relation?: Relation,
  ) => void,
) {
  const graph = document.createElement("div");
  graph.className = "plot";
  const width = (r.pMax - r.pMin + 1) * 112,
    height = (r.qMax - r.qMin + 1) * 82;
  graph.style.minWidth = (r.pMax - r.pMin + 1) * 60 + "px";
  graph.style.setProperty("--columns", String(r.pMax - r.pMin + 1));
  graph.style.height = height + "px";
  const ns = "http://www.w3.org/2000/svg";
  const svg = document.createElementNS(ns, "svg");
  svg.setAttribute("viewBox", "0 0 " + width + " " + height);
  svg.setAttribute("role", "group");
  svg.setAttribute("aria-label", "Differentials");
  svg.setAttribute("preserveAspectRatio", "none");
  const marker = document.createElementNS(ns, "marker");
  for (const [attr, val] of Object.entries({
    id: "tip",
    viewBox: "0 0 10 10",
    refX: "9",
    refY: "5",
    markerWidth: "5",
    markerHeight: "5",
    orient: "auto",
  }))
    marker.setAttribute(attr, val);
  const tip = document.createElementNS(ns, "path");
  tip.setAttribute("d", "M0 0L10 5L0 10Z");
  tip.setAttribute("fill", "context-stroke");
  marker.append(tip);
  svg.append(marker);
  graph.append(svg);
  const x = (p: number) => (p - r.pMin + 0.5) * 112,
    y = (q: number) => (r.qMax - q + 0.5) * 82;
  function tick(label: number, left: number, top: number) {
    const el = document.createElement("span");
    el.className = "tick";
    el.append(math(String(label)));
    el.style.left = (left / width) * 100 + "%";
    el.style.top = top + "px";
    graph.append(el);
  }
  for (let p = r.pMin; p <= r.pMax; p++) tick(p, x(p), height - 8);
  for (let q = r.qMin; q <= r.qMax; q++) tick(q, 8, y(q));
  const positions = new Map<string, Point>();
  for (let q = r.qMax; q >= r.qMin; q--)
    for (let p = r.pMin; p <= r.pMax; p++)
      positions.set(key({ p, q }), { p, q });
  for (const map of m.page.maps) {
    const point = plotPoint(m.data, map);
    positions.set(key(point), point);
  }
  function offset(id?: string) {
    const classes = id && m.classes.get(id)?.term.classes;
    return classes
      ? (classes.findIndex((c) => c.id === id) - (classes.length - 1) / 2) *
          Math.min(30, 65 / classes.length)
      : 0;
  }
  for (const { p, q } of positions.values()) {
    const a = nativePoint(m.data, { p, q }),
      arrow = differential(m, a),
      b = plotPoint(m.data, arrow.b);
    if ((inside(b, r) || m.maps.has(key(a))) && mode !== "None") {
      const assignments = arrow.assignments?.filter(
        (row) => row.sourceClass || row.targetClass,
      );
      for (const row of assignments?.length ? assignments : [undefined]) {
        const status = row?.image.trim() === "0" ? "zero" : arrow.status;
        if (
          (mode === "Potentially nonzero" && status === "zero") ||
          (mode === "Known nonzero" && status !== "nonzero")
        )
          continue;
        const startY = y(q) + offset(row?.sourceClass),
          endY = y(b.q) + offset(row?.targetClass);
        const dx = x(b.p) - x(p),
          dy = endY - startY,
          length = Math.hypot(dx, dy);
        const segment = clipPolyline(
          [
            [x(p) + (22 * dx) / length, startY + (22 * dy) / length],
            [x(b.p) - (22 * dx) / length, endY - (22 * dy) / length],
          ],
          [0, 0, width, height],
        )[0];
        if (!segment) continue;
        const line = document.createElementNS(ns, "line");
        for (const [attr, val] of Object.entries({
          x1: segment[0][0],
          y1: segment[0][1],
          x2: segment[1][0],
          y2: segment[1][1],
        }))
          line.setAttribute(attr, String(val));
        line.dataset.status = status;
        line.dataset.highlighted = String(
          key(selected) === key(a) ||
            (!arrowSelected && key(selected) === key(arrow.b)),
        );
        line.setAttribute("marker-end", "url(#tip)");
        const hit = line.cloneNode(false) as SVGLineElement;
        hit.removeAttribute("data-status");
        hit.removeAttribute("data-highlighted");
        hit.removeAttribute("marker-end");
        hit.classList.add("arrow-hit");
        hit.setAttribute("role", "button");
        hit.setAttribute("tabindex", "0");
        const name =
          "Differential " +
          (row?.sourceClass ?? coord(a)) +
          " to " +
          (row?.targetClass ?? coord(arrow.b));
        hit.setAttribute("aria-label", name);
        hit.setAttribute("aria-pressed", String(active === name));
        hit.onclick = () => choose(a, true, name);
        hit.onkeydown = (event) => {
          if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            choose(a, true, name);
          }
        };
        svg.append(line, hit);
      }
    }
    if (!inside({ p, q }, r)) continue;
    for (const c of m.terms.get(key(a))?.classes ?? []) {
      const button = document.createElement("button");
      button.className = "cell chart-class";
      button.style.left = (x(p) / width) * 100 + "%";
      button.style.top = y(q) + offset(c.id) + "px";
      button.dataset.status = "nonzero";
      button.setAttribute("aria-label", "Class " + c.id);
      button.setAttribute("aria-pressed", String(active === "Class " + c.id));
      button.append(math(c.label));
      if (c.permanent) {
        const tag = document.createElement("small");
        tag.textContent = "permanent";
        button.append(tag);
      }
      button.onclick = () => choose(a, false, "Class " + c.id);
      graph.append(button);
    }
    if (m.terms.get(key(a))?.classes?.length) continue;
    const cell = document.createElement("button"),
      term = m.terms.get(key(a)),
      status = termStatus(m, a);
    cell.className = "cell";
    cell.style.left = (x(p) / width) * 100 + "%";
    cell.dataset.status = status;
    cell.style.top = y(q) + "px";
    cell.setAttribute("aria-label", coord(a));
    cell.setAttribute(
      "aria-pressed",
      String(!active && key(a) === key(selected)),
    );
    if (status === "zero") {
      if (zeroStyle !== "blank")
        cell.append(math(zeroStyle === "dot" ? "\\cdot" : "0"));
    } else {
      if (status === "unknown") cell.append("?");
      if (term?.label) cell.append(math(term.label));
      else if (status === "nonzero") cell.append("●");
    }
    const first = m.stable.get(key(a));
    if (first !== undefined && first <= m.page.index) {
      cell.classList.add("stable");
      const tag = document.createElement("small");
      tag.textContent = "stable";
      cell.append(tag);
    }
    cell.onclick = () => choose(a);
    cell.onkeydown = (e) => {
      const moves: Record<string, Point> = {
        ArrowUp: { p, q: q + 1 },
        ArrowDown: { p, q: q - 1 },
        ArrowLeft: { p: p - 1, q },
        ArrowRight: { p: p + 1, q },
      };
      const next = moves[e.key];
      if (next) {
        e.preventDefault();
        if (inside(next, r)) choose(nativePoint(m.data, next));
      }
    };
    graph.append(cell);
  }
  for (const rel of m.page.relations ?? []) {
    const term = m.classes.get(rel.source)!.term;
    const a = plotPoint(m.data, term),
      b = plotPoint(m.data, m.classes.get(rel.target)!.term);
    const path = document.createElementNS(ns, "path");
    const ay = y(a.q) + offset(rel.source),
      by = y(b.q) + offset(rel.target);
    path.setAttribute(
      "d",
      `M ${x(a.p)} ${ay} Q ${(x(a.p) + x(b.p)) / 2 + 18} ${(ay + by) / 2 - 28} ${x(b.p)} ${by}`,
    );
    path.setAttribute("class", rel.kind);
    const hit = path.cloneNode(false) as SVGPathElement;
    hit.classList.add("relation-hit");
    const name =
      rel.kind[0].toUpperCase() +
      rel.kind.slice(1) +
      " " +
      rel.source +
      " to " +
      rel.target;
    hit.setAttribute("aria-label", name);
    hit.setAttribute("aria-pressed", String(active === name));
    hit.setAttribute("role", "button");
    hit.setAttribute("tabindex", "0");
    hit.onclick = () => choose(term, false, name, rel);
    hit.onkeydown = (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        choose(term, false, name, rel);
      }
    };
    svg.append(path, hit);
  }
  return graph;
}
