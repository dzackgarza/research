import { key, type Model, type Point, type Rect } from "./sequence";
export function inside({ p, q }: Point, r: Rect) {
  return p >= r.pMin && p <= r.pMax && q >= r.qMin && q <= r.qMax;
}
export function endpoint(m: Model, source: Point, direction: 1 | -1) {
  const sign = m.data.convention === "cohomological" ? direction : -direction;
  return {
    p: source.p + sign * m.page.index,
    q: source.q + sign * (1 - m.page.index),
  };
}
export function termStatus(m: Model, t: Point) {
  if (t.p < 0 || t.q < 0) return "zero";
  if (m.data.supportedColumns && !m.data.supportedColumns.includes(t.p)) return "zero";
  return (
    m.terms.get(key(t))?.status ??
    (inside(t, m.data.extent) ? m.data.unlisted : undefined) ??
    "unknown"
  );
}
export function forcedZero(m: Model, a: Point, b: Point) {
  return (
    m.page.index >= (m.data.degenerationPage ?? Infinity) ||
    [a, b].some(
      (t) =>
        termStatus(m, t) === "zero" ||
        m.page.index >= (m.stable.get(key(t)) ?? Infinity),
    )
  );
}
export function differential(m: Model, a: Point) {
  const b = endpoint(m, a, 1),
    record = m.maps.get(key(a));
  return {
    a,
    b,
    status: forcedZero(m, a, b) ? "zero" : (record?.status ?? "undetermined"),
    formula: record?.formula,
    image: record?.image,
  };
}
