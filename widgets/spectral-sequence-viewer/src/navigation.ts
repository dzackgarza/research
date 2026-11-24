import { select } from "d3-selection";
import { zoom } from "d3-zoom";
import {
  indexPage,
  nativePoint,
  plotPoint,
  viewport,
  type Rect,
  type Sequence,
} from "./sequence";
import { endpoint } from "./differentials";

const columns = (r: Rect) => r.pMax - r.pMin + 1;
const rows = (r: Rect) => r.qMax - r.qMin + 1;
const span = (r: Rect) => Math.max(columns(r), rows(r));
const clamp = (x: number, lo: number, hi: number) =>
  Math.min(hi, Math.max(lo, x));

export function openingView(data: Sequence): Rect {
  if (data.settings?.viewport) return data.settings.viewport;
  let bounds: Rect | undefined;
  function include(point: { p: number; q: number }) {
    const { p, q } = plotPoint(data, point);
    if (!bounds) bounds = { pMin: p, pMax: p, qMin: q, qMax: q };
    else {
      bounds.pMin = Math.min(bounds.pMin, p);
      bounds.pMax = Math.max(bounds.pMax, p);
      bounds.qMin = Math.min(bounds.qMin, q);
      bounds.qMax = Math.max(bounds.qMax, q);
    }
  }
  for (const page of data.pages) {
    const m = indexPage(data, page);
    for (const t of page.terms) if (t.status === "nonzero") include(t);
    for (const a of page.maps)
      if (a.status === "nonzero") {
        include(a);
        include(endpoint(m, a, 1));
      }
  }
  const b = bounds ?? viewport(data);
  const n = bounds ? span(b) : Math.min(5, span(b));
  const lower = data.support === "unrestricted" ? -Infinity : 0;
  const p = Math.max(
    lower,
    b.pMin - Math.floor(Math.max(0, n - columns(b)) / 2),
  );
  const q = Math.max(lower, b.qMin - Math.floor(Math.max(0, n - rows(b)) / 2));
  return { pMin: p, pMax: p + n - 1, qMin: q, qMax: q + n - 1 };
}

// All coordinate maps are affine, so the corners bound every selected point.
export function safeView(data: Sequence, r: Rect) {
  for (const p of [r.pMin, r.pMax])
    for (const q of [r.qMin, r.qMax]) {
      if (!Number.isSafeInteger(p) || !Number.isSafeInteger(q)) return false;
      const t = nativePoint(data, { p, q });
      if (!Number.isSafeInteger(t.q)) return false;
      for (const index of [
        data.firstPage,
        data.pages[data.pages.length - 1].index,
      ])
        for (const sign of [-1, 1]) {
          const a = { p: t.p + sign * index, q: t.q + sign * (1 - index) };
          if (
            !Number.isSafeInteger(a.p) ||
            !Number.isSafeInteger(a.q) ||
            !Number.isSafeInteger(plotPoint(data, a).p)
          )
            return false;
        }
    }
  return true;
}

export function navigateChart(
  frame: HTMLDivElement,
  data: Sequence,
  r: Rect,
  home: Rect,
  change: (r: Rect) => void,
) {
  const n = span(r);
  const size = () => frame.getBoundingClientRect().width;
  const maximum = () => Math.max(span(home), Math.floor(size() / 44), n);
  const limits = viewport({
    ...data,
    settings: { ...data.settings, viewport: undefined },
  });
  function settle(k: number, dx: number, dy: number) {
    if (!size()) return;
    const count = clamp(Math.round(n / k), 1, maximum());
    const cx = r.pMin + (columns(r) - 1) / 2,
      cy = r.qMin + (rows(r) - 1) / 2;
    const left = Math.round(
      cx + ((0.5 - dx / size()) / k - 0.5) * n - (count - 1) / 2,
    );
    const bottom = Math.round(
      cy - ((0.5 - dy / size()) / k - 0.5) * n - (count - 1) / 2,
    );
    const p = clamp(
      left,
      Math.min(limits.pMin, home.pMin) - count + 1,
      Math.max(limits.pMax, home.pMax),
    );
    const q = clamp(
      bottom,
      Math.min(limits.qMin, home.qMin) - count + 1,
      Math.max(limits.qMax, home.qMax),
    );
    const next = { pMin: p, pMax: p + count - 1, qMin: q, qMax: q + count - 1 };
    if (safeView(data, next)) change(next);
    else change(r);
  }
  const gesture = zoom<HTMLDivElement, undefined>()
    .wheelDelta((event) => {
      // A discrete wheel notch must survive rounding even on a one-box chart.
      const notches =
        event.deltaMode === 1
          ? event.deltaY / 3
          : event.deltaMode === 2
            ? event.deltaY
            : event.deltaY / 100;
      return (
        -notches *
        Math.max(0.25, Math.log2(1 + 1 / n)) *
        (event.ctrlKey ? 5 : 1)
      );
    })
    .extent(() => [
      [0, 0],
      [size(), size()],
    ])
    .filter((event) => {
      gesture.scaleExtent([n / maximum(), n]);
      return (!event.ctrlKey || event.type === "wheel") && !event.button;
    })
    .clickDistance(4)
    .on("zoom", (event) => {
      const layer = frame.firstElementChild as HTMLElement;
      const { x, y, k } = event.transform;
      layer.style.transform = `translate(${x}px,${y}px) scale(${k})`;
    })
    .on("end", (event) => {
      const { k, x, y } = event.transform;
      if (frame.isConnected && (k !== 1 || x !== 0 || y !== 0)) settle(k, x, y);
    });
  select<HTMLDivElement, undefined>(frame).call(gesture);
  frame.onkeydown = (e) => {
    if (e.target !== frame) return;
    const step = size() / n;
    const moves: Record<string, [number, number]> = {
      ArrowLeft: [step, 0],
      ArrowRight: [-step, 0],
      ArrowUp: [0, step],
      ArrowDown: [0, -step],
    };
    if (moves[e.key]) settle(1, ...moves[e.key]);
    else if (["+", "=", "-"].includes(e.key)) {
      const k = e.key === "-" ? n / (n + 1) : n / Math.max(1, n - 1);
      settle(k, (size() * (1 - k)) / 2, (size() * (1 - k)) / 2);
    } else if (e.key === "Home") change(home);
    else return;
    e.preventDefault();
  };
}
