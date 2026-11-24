import {
  indexPage,
  parseSequence,
  key,
  type Sequence,
  type Point,
} from "./sequence";
import { endpoint, differential, inside, termStatus } from "./differentials";
import { diagram, coord } from "./diagram";
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
    const axes = document.createElement("div");
    axes.className = "axes";
    axes.append(
      "↑ ",
      math(settings.qLabel ?? "q"),
      "　",
      math(settings.pLabel ?? "p"),
      " →",
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
    const title = document.createElement("h3");
    title.append("Term ", math(coord(this.selected)));
    const status = document.createElement("small");
    status.textContent = termStatus(m, this.selected);
    title.append(status);
    panel.append(title);
    const term = m.terms.get(key(this.selected));
    if (term?.label) panel.append(math(term.label));
    const stable = m.stable.get(key(this.selected));
    if (stable !== undefined && stable <= page.index)
      panel.append(" stable from page " + stable);
    const location = (t: Point) =>
      coord(t) + (inside(t, r) ? "" : " offscreen");
    for (const [name, a] of [
      ["Incoming", endpoint(m, this.selected, -1)],
      ["Outgoing", this.selected],
    ] as const) {
      const arrow = differential(m, a),
        row = document.createElement("p");
      const caption = document.createElement("b");
      caption.textContent = name;
      row.append(
        caption,
        " " + location(a) + " → " + location(arrow.b) + " · " + arrow.status,
      );
      if (arrow.formula) row.append("　", math(arrow.formula));
      panel.append(row);
    }
    const header = document.createElement("header");
    header.append(heading, toolbar);
    const canvas = document.createElement("div");
    canvas.className = "canvas";
    canvas.append(axes, scroll);
    const layout = document.createElement("div");
    layout.className = "layout";
    panel.append(display);
    layout.append(canvas, panel);
    section.append(header, formula, layout);
    this.root.replaceChildren(style, section);
    if (focus)
      this.root
        .querySelector<HTMLElement>('[aria-label="' + CSS.escape(focus) + '"]')
        ?.focus({ preventScroll: true });
  }
}
