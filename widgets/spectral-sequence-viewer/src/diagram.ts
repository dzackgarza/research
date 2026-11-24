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
  pixels: number,
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
  const columns = r.pMax - r.pMin + 1,
    rows = r.qMax - r.qMin + 1;
  const pitch = pixels / Math.max(columns, rows);
  const width = columns * pitch,
    height = rows * pitch,
    side = pixels;
  graph.style.width = (width / side) * 100 + "%";
  graph.style.height = (height / side) * 100 + "%";
  graph.style.setProperty("--columns", String(columns));
  graph.style.setProperty("--rows", String(rows));
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
  const x = (p: number) => (p - r.pMin + 0.5) * pitch,
    y = (q: number) => (r.qMax - q + 0.5) * pitch;
  function tick(label: number, left: number, top: number) {
    const el = document.createElement("span");
    el.className = "tick";
    el.append(math(String(label)));
    el.style.left = (left / width) * 100 + "%";
    el.style.top = (top / height) * 100 + "%";
    graph.append(el);
  }
  const step = Math.max(1, Math.ceil(Math.max(columns, rows) / 16));
  for (let i = 0; i < columns; i += step)
    tick(r.pMin + i, x(r.pMin + i), height - 8);
  for (let i = 0; i < rows; i += step) tick(r.qMin + i, 8, y(r.qMin + i));
  const positions = new Map<string, Point>();
  if (step === 1) {
    for (let q = r.qMax; q >= r.qMin; q--)
      for (let p = r.pMin; p <= r.pMax; p++)
        positions.set(key({ p, q }), { p, q });
  } else {
    graph.classList.add("overview");
    graph.onclick = (event) => {
      if (event.target !== graph) return;
      const box = graph.getBoundingClientRect();
      const p =
        r.pMin +
        Math.min(
          columns - 1,
          Math.floor(((event.clientX - box.left) / box.width) * columns),
        );
      const q =
        r.qMax -
        Math.min(
          rows - 1,
          Math.floor(((event.clientY - box.top) / box.height) * rows),
        );
      choose(nativePoint(m.data, { p, q }));
    };
    for (const term of [...m.page.terms, selected]) {
      const pos = plotPoint(m.data, term);
      if (inside(pos, r)) positions.set(key(pos), pos);
    }
  }
  for (const map of m.page.maps) {
    const point = plotPoint(m.data, map);
    positions.set(key(point), point);
  }
  function offset(id?: string) {
    const classes = id && m.classes.get(id)?.term.classes;
    return classes
      ? (classes.findIndex((c) => c.id === id) - (classes.length - 1) / 2) *
          Math.min(30, (pitch * 0.78) / classes.length)
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
      const unnamed = arrow.assignments?.filter(
        (row) => !row.sourceClass && !row.targetClass,
      );
      const edges = [
        ...(assignments ?? []),
        ...(!assignments?.length || unnamed?.length ? [undefined] : []),
      ];
      for (const row of edges) {
        const zeroImage = row
          ? row.image.trim() === "0"
          : assignments?.length &&
            unnamed?.length &&
            unnamed.every((entry) => entry.image.trim() === "0");
        const status = zeroImage ? "zero" : arrow.status;
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
        const inset = Math.min(22, length / 4);
        const segment = clipPolyline(
          [
            [x(p) + (inset * dx) / length, startY + (inset * dy) / length],
            [x(b.p) - (inset * dx) / length, endY - (inset * dy) / length],
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
        const classId = active?.startsWith("Class ")
          ? active.slice(6)
          : undefined;
        line.dataset.highlighted = String(
          arrowSelected
            ? active === name
            : (key(selected) === key(a) &&
                (!classId || row?.sourceClass === classId)) ||
                (key(selected) === key(arrow.b) &&
                  (!classId || row?.targetClass === classId)),
        );
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
    const navigate = (e: KeyboardEvent) => {
      const moves: Record<string, Point> = {
        ArrowUp: { p, q: q + 1 },
        ArrowDown: { p, q: q - 1 },
        ArrowLeft: { p: p - 1, q },
        ArrowRight: { p: p + 1, q },
      };
      const next = moves[e.key];
      if (next) {
        e.preventDefault();
        if (inside(next, r)) {
          const point = nativePoint(m.data, next);
          const first = m.terms.get(key(point))?.classes?.[0];
          choose(point, false, first && "Class " + first.id);
        }
      }
    };
    for (const c of m.terms.get(key(a))?.classes ?? []) {
      const button = document.createElement("button");
      button.className = "cell chart-class";
      button.style.left = (x(p) / width) * 100 + "%";
      button.style.top = ((y(q) + offset(c.id)) / height) * 100 + "%";
      button.dataset.status = "nonzero";
      button.setAttribute("aria-label", "Class " + c.id);
      button.setAttribute("aria-pressed", String(active === "Class " + c.id));
      button.append(math(c.label));
      if (c.permanent) {
        const tag = document.createElement("small");
        tag.textContent = "permanent";
        button.append(tag);
      }
      button.onkeydown = navigate;
      button.onclick = () => choose(a, false, "Class " + c.id);
      graph.append(button);
    }
    if (m.terms.get(key(a))?.classes?.length) {
      const first = m.stable.get(key(a));
      if (first !== undefined && first <= m.page.index) {
        const tag = document.createElement("small");
        tag.className = "term-stability";
        tag.textContent = "stable";
        tag.setAttribute(
          "aria-label",
          "Term " + coord(a) + " stable from page " + first,
        );
        tag.style.left = (x(p) / width) * 100 + "%";
        tag.style.top = ((y(q) + 30) / height) * 100 + "%";
        graph.append(tag);
      }
      continue;
    }
    const cell = document.createElement("button"),
      term = m.terms.get(key(a)),
      status = termStatus(m, a);
    cell.className = "cell";
    cell.style.left = (x(p) / width) * 100 + "%";
    cell.dataset.status = status;
    cell.style.top = (y(q) / height) * 100 + "%";
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
    cell.onkeydown = navigate;
    graph.append(cell);
  }
  const relations = m.page.relations ?? [];
  for (const rel of relations) {
    const term = m.classes.get(rel.source)!.term;
    const a = plotPoint(m.data, term),
      b = plotPoint(m.data, m.classes.get(rel.target)!.term);
    const path = document.createElementNS(ns, "path");
    const ay = y(a.q) + offset(rel.source),
      by = y(b.q) + offset(rel.target);
    const parallel = relations.filter(
      (other) => other.source === rel.source && other.target === rel.target,
    );
    const lane = parallel.indexOf(rel);
    const bend = (lane % 2 ? -1 : 1) * (32 + 36 * Math.floor(lane / 2));
    const dx = x(b.p) - x(a.p),
      dy = by - ay,
      length = Math.hypot(dx, dy);
    const cx = (x(a.p) + x(b.p)) / 2 + (length ? dy / length : 1) * bend;
    const cy = (ay + by) / 2 - (length ? dx / length : 1) * bend;
    path.setAttribute("d", `M ${x(a.p)} ${ay} Q ${cx} ${cy} ${x(b.p)} ${by}`);
    path.setAttribute("class", rel.kind);
    const hit = path.cloneNode(false) as SVGPathElement;
    hit.classList.add("relation-hit");
    const name =
      rel.kind[0].toUpperCase() +
      rel.kind.slice(1) +
      " " +
      rel.source +
      " to " +
      rel.target +
      (parallel.some((other) => other !== rel && other.kind === rel.kind)
        ? " " + rel.formula
        : "");
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
