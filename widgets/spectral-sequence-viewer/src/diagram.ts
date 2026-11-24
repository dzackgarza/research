import { key, type Model, type Point, type Rect } from "./sequence";
import { differential, inside, termStatus } from "./differentials";
import { math } from "./math";
export const coord = (t: Point) => "(" + key(t) + ")";
export function diagram(
  m: Model,
  r: Rect,
  selected: Point,
  mode: string,
  zeroStyle: string,
  choose: (t: Point) => void,
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
  svg.setAttribute("aria-hidden", "true");
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
  for (let q = r.qMax; q >= r.qMin; q--)
    for (let p = r.pMin; p <= r.pMax; p++) {
      const a = { p, q },
        arrow = differential(m, a),
        b = arrow.b;
      if (
        inside(b, r) &&
        mode !== "None" &&
        (mode === "All" ||
          (mode === "Potentially nonzero"
            ? arrow.status !== "zero"
            : arrow.status === "nonzero"))
      ) {
        const dx = x(b.p) - x(p),
          dy = y(b.q) - y(q),
          length = Math.hypot(dx, dy);
        const line = document.createElementNS(ns, "line");
        for (const [attr, val] of Object.entries({
          x1: x(p) + (22 * dx) / length,
          y1: y(q) + (22 * dy) / length,
          x2: x(b.p) - (22 * dx) / length,
          y2: y(b.q) - (22 * dy) / length,
        }))
          line.setAttribute(attr, String(val));
        line.dataset.status = arrow.status;
        line.dataset.highlighted = String(
          key(selected) === key(a) || key(selected) === key(b),
        );
        line.setAttribute("marker-end", "url(#tip)");
        svg.append(line);
      }
      const cell = document.createElement("button"),
        term = m.terms.get(key(a)),
        status = termStatus(m, a);
      cell.className = "cell";
      cell.style.left = (x(p) / width) * 100 + "%";
      cell.dataset.status = status;
      cell.style.top = y(q) + "px";
      cell.setAttribute("aria-label", coord(a));
      cell.setAttribute("aria-pressed", String(key(a) === key(selected)));
      if (status === "zero")
        cell.textContent =
          zeroStyle === "blank" ? "" : zeroStyle === "dot" ? "·" : "0";
      else {
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
          if (inside(next, r)) choose(next);
        }
      };
      graph.append(cell);
    }
  return graph;
}
