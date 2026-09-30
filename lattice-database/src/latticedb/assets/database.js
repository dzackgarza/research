(async () => {
  const siteRoot = new URL(document.body.dataset.siteRoot || "./", document.baseURI);
  const node = document.querySelector("#lattice-table");

  const darkScheme = window.matchMedia("(prefers-color-scheme: dark)");
  const syncLibraryTheme = () => document.documentElement.classList.toggle("dark", darkScheme.matches);
  syncLibraryTheme();
  darkScheme.addEventListener("change", syncLibraryTheme);

  const params = new URLSearchParams(location.search);
  const values = (key) =>
    params
      .getAll(key)
      .flatMap((value) => value.split(","))
      .filter(Boolean);
  const escapeHtml = (text) => String(text).replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;");
  const typeset = async (element) => {
    await window.MathJax?.startup?.promise;
    await window.MathJax?.typesetPromise?.([element]);
  };

  // A column whose cells show one key of the row and sort by another.
  const valued = (shown, value) => ({
    data: shown,
    defaultContent: "",
    className: "dt-right",
    render: (data, type, row) => (type === "sort" || type === "type" ? row[value] : data),
    searchBuilder: { orthogonal: { display: "display", search: "sort" } },
    searchPanes: { show: false },
  });
  // A column whose cells hold a list of labels. The pane of such a column selects the rows that have every chosen label.
  const labels = (key, shown) => ({
    data: key,
    visible: shown,
    orderable: false,
    className: "labels-cell",
    render: (data, type) => {
      if (type === "sp") return data;
      if (type === "display") return data.map((label) => `<span class="chip">${escapeHtml(label)}</span>`).join(" ");
      return data.join(", ");
    },
    searchPanes: { show: true, orthogonal: "sp", combiner: "and", dtOpts: { order: [[1, "desc"]] } },
  });
  const plain = (key, options = {}) => ({ data: key, defaultContent: "", searchPanes: { show: false }, ...options });
  // A column whose cells show the TeX of a key of the row. Search and sort use the text of that key.
  const texOf = (key) =>
    plain(key, {
      className: "nowrap-cell",
      render: (data, type, row) => (type === "display" && row[`${key}_tex`] ? `\\(${escapeHtml(row[`${key}_tex`])}\\)` : data),
    });

  const columns = [
    plain("tag", {
      className: "tag-cell",
      render: (data, type, row) => (type === "display" ? `<a class="tag" href="${escapeHtml(row.url)}">${escapeHtml(data)}</a>` : data),
    }),
    plain("name", {
      render: (data, type, row) => (type === "display" ? `<a class="lattice-link" href="${escapeHtml(row.url)}">\\(${escapeHtml(row.latex)}\\)</a>` : data),
    }),
    { data: "rank", className: "dt-right", searchPanes: { show: true } },
    plain("signature", { orderable: false }),
    valued("determinant", "determinant_value"),
    { data: "definiteness", className: "nowrap-cell", searchPanes: { show: true } },
    labels("properties", true),
    texOf("discriminant_group"),
    valued("minimum", "minimum_value"),
    plain("kissing_number", { className: "dt-right" }),
    valued("automorphism_group_order", "automorphism_group_order_value"),
    texOf("root_system"),
    plain("genus_symbol", { visible: false }),
    labels("families", false),
    plain("aliases", { visible: false, orderable: false, render: (data) => data.join(", ") }),
    plain("n_plus", { visible: false }),
    plain("n_minus", { visible: false }),
    texOf("phi_type"),
    texOf("root_span"),
    plain("root_span_index", { className: "dt-right" }),
    plain("root_span_rank", { visible: false }),
    plain("root_span_primitive", { visible: false }),
  ];
  // A pane selects the options that are equal to the values of its column, so the values of a number column are numbers.
  const paneOf = { rank: [2, Number], definiteness: [5, String], property: [6, String], family: [13, String] };
  const preSelect = Object.entries(paneOf)
    .map(([key, [column, valueOf]]) => ({ column, rows: values(key).map(valueOf) }))
    .filter((pane) => pane.rows.length);

  const { rows } = await fetch(new URL("lattices.json", siteRoot)).then((response) => response.json());
  const table = new DataTable(node, {
    data: rows,
    columns,
    deferRender: true,
    pageLength: 50,
    lengthMenu: [25, 50, 100, { label: "All", value: -1 }],
    search: { search: params.get("q") || "" },
    order: [
      [2, "asc"],
      [0, "asc"],
    ],
    language: {
      paginate: { first: "First", previous: "Previous", next: "Next", last: "Last" },
      searchBuilder: { title: { 0: "Conditions", _: "Conditions (%d)" }, add: "Add a condition" },
    },
    searchPanes: { cascadePanes: true, viewTotal: true, orderable: false, layout: "columns-4", preSelect },
    buttons: [
      { extend: "colvis", text: "Columns" },
      { extend: "csvHtml5", text: "CSV", title: "lattices", exportOptions: { orthogonal: "filter" } },
      { extend: "copyHtml5", text: "Copy", exportOptions: { orthogonal: "filter", columns: ":visible" } },
    ],
    layout: {
      top2: "searchPanes",
      top1: "searchBuilder",
      topStart: ["pageLength", "buttons"],
      topEnd: "search",
      bottomStart: "info",
      bottomEnd: "paging",
    },
  });
  table.on("draw", () => typeset(node));
  await typeset(node);
})();
