import {
  indexPage,
  parseSequence,
  key,
  type Sequence,
  type Point,
} from "./sequence";
import { endpoint, differential, inside, termStatus } from "./differentials";
import { diagram } from "./diagram";
import { math } from "./math";
import css from "./viewer.css?inline";

function select(
  label: string,
  items: [string, string][],
  current: string,
  change: (value: string) => void,
) {
  const wrapper = document.createElement("label");
  wrapper.append(label + " ");
  const el = document.createElement("select");
  el.setAttribute("aria-label", label);
  for (const [value, text] of items) el.add(new Option(text, value));
  el.value = current;
  el.onchange = () => change(el.value);
  wrapper.append(el);
  return wrapper;
}
const labels = (items: string[]): [string, string][] =>
  items.map((s) => [s, s]);
const subscript = (i: number) =>
  String(i).replace(/\d/g, (d) => "₀₁₂₃₄₅₆₇₈₉"[Number(d)]);
export class Viewer extends HTMLElement {
  private root = this.attachShadow({ mode: "open" });
  private data?: Sequence;
  private i = 0;
  private selected: Point = { p: 0, q: 0 };
  private filter = "All";
  private zeros = "zero";
  set sequence(input: Sequence) {
    const data = parseSequence(input);
    this.data = data;
    this.i = (data.settings?.initialPage ?? data.firstPage) - data.firstPage;
    const r = data.settings?.viewport ?? data.extent;
    this.selected = { p: r.pMin, q: r.qMin };
    this.zeros = data.settings?.zeroStyle ?? "zero";
    this.filter = "All";
    this.render();
  }
  private render() {
    const data = this.data;
    if (!data) return;
    const focus = this.root.activeElement?.getAttribute("aria-label");
    const settings = data.settings ?? {},
      r = settings.viewport ?? data.extent,
      page = data.pages[this.i],
      m = indexPage(data, page);
    const style = document.createElement("style");
    style.textContent = css;
    const section = document.createElement("section");
    const heading = document.createElement("h2");
    heading.append(settings.title ? math(settings.title) : "Spectral sequence");
    const formula = document.createElement("div");
    formula.setAttribute("aria-label", "Page formula");
    if (page.formula) formula.append(math(page.formula));
    const toolbar = document.createElement("div");
    toolbar.className = "toolbar";
    const move = (i: number) => {
      this.i = i;
      this.render();
    };
    const step = (name: string, delta: number) => {
      const b = document.createElement("button");
      b.textContent = delta < 0 ? "‹" : "›";
      b.title = name;
      b.setAttribute("aria-label", name);
      b.disabled = !data.pages[this.i + delta];
      b.onclick = () => move(this.i + delta);
      return b;
    };
    toolbar.append(
      step("Previous", -1),
      select(
        "Page",
        data.pages.map((p) => [
          String(p.index),
          "E" +
            subscript(p.index) +
            (p.index === data.degenerationPage ? " = E∞" : ""),
        ]),
        String(page.index),
        (v) => move(Number(v) - data.firstPage),
      ),
      step("Next", 1),
    );
    const display = document.createElement("details");
    display.open = this.root.querySelector("details")?.open ?? false;
    const summary = document.createElement("summary");
    summary.textContent = "Display options";
    display.append(
      summary,
      select(
        "Arrows",
        labels(["All", "Potentially nonzero", "Known nonzero", "None"]),
        this.filter,
        (v) => {
          this.filter = v;
          this.render();
        },
      ),
      select(
        "Zero style",
        labels(["zero", "dot", "blank"]),
        this.zeros,
        (v) => {
          this.zeros = v;
          this.render();
        },
      ),
    );
    const pageControl = toolbar.querySelector("label")!;
    pageControl.firstChild?.remove();
    pageControl.prepend(
      math(
        "E_{" +
          page.index +
          "}" +
          (page.index === data.degenerationPage ? "=E_{\\infty}" : ""),
      ),
    );
    const scroll = document.createElement("div");
    scroll.className = "scroll";
    scroll.append(
      diagram(m, r, this.selected, this.filter, this.zeros, (t) => {
        this.selected = t;
        this.render();
        this.root
          .querySelector<HTMLButtonElement>('[aria-pressed="true"]')
          ?.focus();
      }),
    );
    const panel = document.createElement("aside");
    panel.setAttribute("role", "region");
    panel.setAttribute("aria-label", "Inspector");
    const source = endpoint(m, this.selected, -1);
    const first = differential(m, source);
    const second = differential(m, this.selected);
    const rIndex = page.index;
    const colored = (status: string, tex: string) =>
      "\\class{state-" + status + "}{" + tex + "}";
    const term = (point: Point) => {
      const degree = point.p + "," + point.q;
      const symbol =
        data.convention === "cohomological"
          ? "E_" + (rIndex < 10 ? rIndex : "{" + rIndex + "}") + "^{" + degree + "}"
          : "E^{" + rIndex + "}_{" + degree + "}";
      const status = termStatus(m, point);
      const notes = [];
      const label = m.terms.get(key(point))?.label;
      if (label) notes.push(label);
      if (point.p >= 0 && point.q >= 0 && !inside(point, r))
        notes.push("\\text{offscreen}");
      return colored(status, notes.length
        ? "\\underset{" + notes.join("\\;") + "}{" + symbol + "}"
        : symbol);
    };
    const arrow = (map: typeof first) => {
      const label = map.status === "zero" ? "0" : "d_{" + rIndex + "}";
      const annotation = map.formula === "0" ? "" : (map.formula ?? "");
      return colored(map.status, "\\xrightarrow[" + annotation + "]{" + label + "}");
    };
    const tex =
      term(source) +
      arrow(first) +
      term(this.selected) +
      arrow(second) +
      term(second.b);
    const chain = math(tex);
    chain.classList.add("chain");
    chain.querySelector("svg")!.setAttribute("aria-label", tex);
    panel.append(chain);
    const stable = m.stable.get(key(this.selected));
    if (stable !== undefined && stable <= page.index)
      panel.append(" stable from page " + stable);
    const header = document.createElement("header");
    header.append(heading, toolbar);
    const canvas = document.createElement("div");
    canvas.className = "canvas";
    const vertical = document.createElement("div");
    vertical.className = "vertical-axis";
    vertical.append(math(settings.qLabel ?? "q"), " ↑");
    const horizontal = document.createElement("div");
    horizontal.className = "horizontal-axis";
    horizontal.append(math(settings.pLabel ?? "p"), " →");
    canvas.append(vertical, scroll, horizontal);
    const layout = document.createElement("div");
    layout.className = "layout";
    const guide = document.createElement("div");
    guide.className = "guide";
    const button = document.createElement("button");
    button.textContent = "Color key";
    const legend = document.createElement("div");
    legend.popover = "auto";
    button.popoverTargetElement = legend;
    for (const [state, name] of [["zero", "Red · zero"], ["nonzero", "Blue · nonzero"], ["unknown", "Orange · unknown"]]) {
      const item = document.createElement("span");
      item.className = "state-" + state;
      item.textContent = name;
      legend.append(item);
    }
    guide.append(button, legend);
    panel.append(guide, display);
    layout.append(canvas, panel);
    section.append(header, formula, layout);
    this.root.replaceChildren(style, section);
    if (focus)
      this.root
        .querySelector<HTMLElement>('[aria-label="' + CSS.escape(focus) + '"]')
        ?.focus({ preventScroll: true });
  }
}
