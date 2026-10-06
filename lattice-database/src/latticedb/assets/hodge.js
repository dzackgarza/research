// The Hodge diamond studio: an interactive teaching widget, not catalogue data.
//
// For a smooth complex projective variety of complex dimension n, the Hodge
// numbers h^{p,q} sit at the points (p, q) with 0 <= p, q <= n. This page
// draws them, draws the lines of the symmetries, and names what a click
// selects. The values shown are either the formal symbols h^{p,q} or the
// textbook numbers of the chosen preset:
//
// - projective space P^n: h^{p,p} = 1, the rest 0
//   (https://stacks.math.columbia.edu/tag/0FMG);
// - an elliptic curve: every entry 1;
// - a K3 surface: the numbers of the catalogue's k3-surface card,
//   1, 1, 20, 1, 1;
// - a Calabi-Yau threefold: h^{1,1} = h^{2,2} = a and h^{2,1} = h^{1,2} = b
//   with the sliders, the rest 0 except the four corner 1s;
// - hyperkahler: the K3 numbers with the D4 mirrors on.
//
// The always-true symmetries are exactly the ones the catalogue checks on
// every card: conjugation h^{p,q} = h^{q,p} and Serre duality
// h^{p,q} = h^{n-p,n-q}. The horizontal mirror h^{p,q} = h^{n-p,q} is the extra
// D4 symmetry the catalogue computes (see the `symmetry_group` validator and
// https://hyperkaehler.info/hodge/); the rotation is its composition with
// Serre duality.
(() => {
  "use strict";
  const NS = "http://www.w3.org/2000/svg";
  const svg = document.querySelector("#hodge-svg");
  const info = document.querySelector("#hodge-info");
  const dimInput = document.querySelector("#hodge-dim");
  const dimLabel = document.querySelector("#hodge-dim-value");
  const presetSelect = document.querySelector("#hodge-preset");
  const aInput = document.querySelector("#hodge-a");
  const bInput = document.querySelector("#hodge-b");
  const aLabel = document.querySelector("#hodge-a-value");
  const bLabel = document.querySelector("#hodge-b-value");
  const abRow = document.querySelector("#hodge-ab-row");
  const orbitList = document.querySelector("#hodge-orbit");
  const filtrationInfo = document.querySelector("#hodge-filtration");
  const totalsInfo = document.querySelector("#hodge-totals");

  const el = (tag, attrs = {}) => {
    const node = document.createElementNS(NS, tag);
    for (const [key, value] of Object.entries(attrs))
      node.setAttribute(key, value);
    return node;
  };
  const text = (parent, x, y, content, cls = "") => {
    const node = el("text", { x, y, class: `hodge-text ${cls}`.trim() });
    node.textContent = content;
    parent.appendChild(node);
    return node;
  };

  // The four non-identity generators offered as symmetry checkboxes.
  // Each maps (p, q) to (p, q); the orbit of a cell is the group they generate.
  const GENERATORS = {
    conj: { apply: ([p, q]) => [q, p], axis: "vertical" },
    serre: { apply: ([p, q], n) => [n - p, n - q], axis: "center" },
    horiz: { apply: ([p, q], n) => [n - q, n - p], axis: "horizontal" },
    diag: { apply: ([p, q], n) => [n - p, q], axis: "diagonal" },
    rot: { apply: ([p, q], n) => [n - q, p], axis: "rotation" },
  };
  const GENERATOR_ORDER = ["conj", "serre", "horiz", "diag", "rot"];
  const GENERATOR_LABEL = {
    conj: "conjugation",
    serre: "Serre duality",
    horiz: "conjugation then Serre",
    diag: "square mirror",
    rot: "quarter turn",
  };

  const state = { n: 2, preset: "k3", selected: null, a: 2, b: 1 };

  // Values for the presets; General shows the symbols h^{p,q}.
  function value(p, q) {
    const { n, preset, a, b } = state;
    switch (preset) {
      case "projective":
        return p === q ? 1 : 0;
      case "elliptic":
        return 1;
      case "k3":
        if ((p === 0 || p === 2) && (q === 0 || q === 2)) return 1;
        if (p === 1 && q === 1) return 20;
        return 0;
      case "cy3":
        if ((p === 0 || p === 3) && (q === 0 || q === 3)) return 1;
        if ((p === 1 && q === 1) || (p === 2 && q === 2)) return a;
        if ((p === 2 && q === 1) || (p === 1 && q === 2)) return b;
        return 0;
      case "hyperkahler":
        if ((p === 0 || p === 2) && (q === 0 || q === 2)) return 1;
        if (p === 1 && q === 1) return 20;
        return 0;
      default:
        return null;
    }
  }

  function label(p, q) {
    const v = value(p, q);
    return v === null ? `h${p},${q}` : String(v);
  }

  function checkedGenerators() {
    return GENERATOR_ORDER.filter(
      (key) => document.querySelector(`#hodge-sym-${key}`)?.checked,
    );
  }

  function orbit(cell) {
    const { n } = state;
    const gens = checkedGenerators().map((key) => GENERATORS[key].apply);
    const seen = new Set([cell.join(",")]);
    const queue = [cell];
    while (queue.length) {
      const [p, q] = queue.pop();
      for (const apply of gens) {
        const next = apply([p, q], n);
        const key = next.join(",");
        if (!seen.has(key)) {
          seen.add(key);
          queue.push(next);
        }
      }
    }
    return [...seen].map((key) => key.split(",").map(Number));
  }

  // The Hodge piece named by a click: F^p H^k for k = p + q.
  function filtrationPiece(p, q) {
    const k = p + q;
    const cells = [];
    for (let i = Math.max(p, k - state.n); i <= Math.min(state.n, k); i++) {
      cells.push([i, k - i]);
    }
    return { k, cells };
  }

  function draw() {
    const { n, selected } = state;
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    const s = 64;
    const pad = 90;
    const X = (p, q) => pad + (q - p + n) * s;
    const Y = (p, q) => pad + (p + q) * s;
    const width = pad * 2 + 2 * n * s;
    const height = pad * 2 + 2 * n * s;
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);

    const gens = checkedGenerators();
    const orbitKeys = new Set(
      selected ? orbit(selected).map(([p, q]) => `${p},${q}`) : [],
    );
    let filtration = null;
    if (selected) {
      filtration = filtrationPiece(selected[0], selected[1]);
    }
    const filtrationKeys = new Set(
      filtration ? filtration.cells.map(([p, q]) => `${p},${q}`) : [],
    );

    // Symmetry lines for the checked generators.
    const axes = el("g", { class: "hodge-axes" });
    const cx = pad + n * s;
    const cy = pad + n * s;
    if (gens.includes("conj")) {
      axes.appendChild(
        el("line", {
          x1: cx,
          y1: pad - 40,
          x2: cx,
          y2: pad + 2 * n * s + 40,
          class: "hodge-axis",
        }),
      );
      text(axes, cx, pad - 48, "conjugation", "hodge-axis-label");
    }
    if (gens.includes("horiz")) {
      axes.appendChild(
        el("line", {
          x1: pad - 40,
          y1: cy,
          x2: pad + 2 * n * s + 40,
          y2: cy,
          class: "hodge-axis",
        }),
      );
      text(
        axes,
        pad + 2 * n * s + 48,
        cy + 4,
        "conj∘Serre",
        "hodge-axis-label",
      );
    }
    if (gens.includes("diag")) {
      axes.appendChild(
        el("line", {
          x1: pad - n * s - 30,
          y1: pad - 30,
          x2: pad + n * s + 30,
          y2: pad + 2 * n * s + 30,
          class: "hodge-axis hodge-axis-d4",
        }),
      );
      text(
        axes,
        pad + n * s + 40,
        pad + 2 * n * s + 44,
        "square mirror",
        "hodge-axis-label",
      );
    }
    if (gens.includes("serre") || gens.includes("rot")) {
      axes.appendChild(el("circle", { cx, cy, r: 7, class: "hodge-center" }));
      text(
        axes,
        cx + 12,
        cy - 10,
        gens.includes("rot") ? "90°" : "180°",
        "hodge-axis-label",
      );
    }
    svg.appendChild(axes);

    // Cells of the diamond.
    const layer = el("g", { class: "hodge-cells" });
    for (let p = 0; p <= n; p++) {
      for (let q = 0; q <= n; q++) {
        const g = el("g", {
          class: [
            "hodge-cell",
            `hodge-cell-${p}-${q}`,
            orbitKeys.has(`${p},${q}`) ? "is-orbit" : "",
            filtrationKeys.has(`${p},${q}`) ? "is-filtration" : "",
            selected && selected[0] === p && selected[1] === q
              ? "is-selected"
              : "",
          ]
            .filter(Boolean)
            .join(" "),
        });
        const diamond = el("rect", {
          x: X(p, q) - 24,
          y: Y(p, q) - 24,
          width: 48,
          height: 48,
          class: "hodge-diamond",
          transform: `rotate(45 ${X(p, q)} ${Y(p, q)})`,
        });
        diamond.addEventListener("click", () => {
          state.selected = [p, q];
          draw();
        });
        g.appendChild(diamond);
        text(g, X(p, q), Y(p, q) + 5, label(p, q), "hodge-value");
        layer.appendChild(g);
      }
    }
    svg.appendChild(layer);

    // Readouts.
    const orbitEl = orbitList;
    while (orbitEl.firstChild) orbitEl.removeChild(orbitEl.firstChild);
    const filtrationEl = filtrationInfo;
    while (filtrationEl.firstChild)
      filtrationEl.removeChild(filtrationEl.firstChild);
    if (!selected) {
      orbitEl.textContent =
        "Click a diamond to name its symmetry orbit and its Hodge piece.";
      filtrationEl.textContent = "";
    } else {
      const [p, q] = selected;
      const cells = orbit(selected).sort((a, b) => a[0] - b[0] || a[1] - b[1]);
      const names = cells.map(([a, b]) => `h^{${a},${b}}`).join(" = ");
      const vals = cells.map(([a, b]) => value(a, b));
      const line = vals.every((v) => v !== null)
        ? `${names} = ${vals[0]}`
        : names;
      orbitEl.textContent = `Orbit of h^{${p},${q}} under ${gens.map((g) => GENERATOR_LABEL[g]).join(", ") || "nothing"}: ${line}.`;
      const { k, cells: piece } = filtration;
      const terms = piece.map(([a, b]) => `H^{${a},${k - a}}`).join(" ⊕ ");
      const nums = piece.map(([a, b]) => value(a, b));
      const rank = nums.every((v) => v !== null)
        ? ` of rank ${nums.reduce((x, y) => x + y, 0)}`
        : "";
      filtrationEl.textContent = `F^${p}H^${k} = ${terms}${rank}: the piece of the Hodge filtration named by this click.`;
    }
    const vals = [];
    for (let p = 0; p <= n; p++) {
      for (let q = 0; q <= n; q++) vals.push(value(p, q));
    }
    if (vals.every((v) => v !== null)) {
      const total = vals.reduce((x, y) => x + y, 0);
      totalsInfo.textContent = `Total Hodge rank ${total}.`;
    } else {
      totalsInfo.textContent = "";
    }
  }

  function syncControls() {
    const { n, preset, a, b } = state;
    dimLabel.textContent = String(n);
    abRow.hidden = preset !== "cy3";
    aLabel.textContent = String(a);
    bLabel.textContent = String(b);
    if (preset === "elliptic" || preset === "k3" || preset === "hyperkahler") {
      state.n = preset === "k3" || preset === "hyperkahler" ? 2 : 1;
      dimInput.value = String(state.n);
      dimLabel.textContent = String(state.n);
    }
    if (preset === "cy3") {
      state.n = 3;
      dimInput.value = "3";
      dimLabel.textContent = "3";
    }
  }

  dimInput.addEventListener("input", () => {
    state.n = Number(dimInput.value);
    state.selected = null;
    syncControls();
    draw();
  });
  presetSelect.addEventListener("change", () => {
    state.preset = presetSelect.value;
    state.selected = null;
    if (state.preset === "hyperkahler") {
      for (const key of GENERATOR_ORDER) {
        const box = document.querySelector(`#hodge-sym-${key}`);
        if (box) box.checked = true;
      }
    }
    syncControls();
    draw();
  });
  aInput.addEventListener("input", () => {
    state.a = Number(aInput.value);
    syncControls();
    draw();
  });
  bInput.addEventListener("input", () => {
    state.b = Number(bInput.value);
    syncControls();
    draw();
  });
  for (const key of GENERATOR_ORDER) {
    document
      .querySelector(`#hodge-sym-${key}`)
      ?.addEventListener("change", draw);
  }

  info.hidden = false;
  syncControls();
  draw();
})();
