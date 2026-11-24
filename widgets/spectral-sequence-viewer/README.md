# Spectral sequence viewer

Copy `dist/` onto a static HTTP host. The ES module includes MathJax with SVG glyphs. Supply an author dataset that follows [the JSON Schema](dist/sequence.schema.json). [The example](examples/sequence.json) supplies four cohomological pages. Serve the package directory with `python3 -m http.server` and open `/examples/static/` for an interactive article.

```html
<spectral-sequence-viewer></spectral-sequence-viewer>
<script type="module">
  import './dist/spectral-sequence-viewer.js';
  const response = await fetch('./sequence.json');
  if (!response.ok) throw new Error(response.statusText);
  document.querySelector('spectral-sequence-viewer').sequence = await response.json();
</script>
```

To insert another figure, create the element after importing the module, assign its `sequence` property and append it to the article. The element accepts assignment before or after insertion. Invalid input throws and preserves the last accepted figure. In React, import the module once and assign the data object in a ref callback. See the [Vite example](examples/react/main.tsx).

Supply contiguous pages starting at `firstPage`. Term and map coordinates belong to the data extent. Each map record names its source. Its target follows from the page and grading convention. The viewport can clip either endpoint. Unlisted cells default to unknown. Set `unlisted` to `zero` only when omitted cells in the extent are known zero. A stable term declaration gives its first permanent page. A degeneration declaration marks the global infinity page and permits later supplied pages.

Use the page selector or Previous and Next. Select a cell to inspect both differentials; arrow keys move between cells. The Arrows selector filters the drawing. The Zero style selector changes the glyph for known zero terms. The inspector preserves the underlying statuses in either case. Formulas and labels accept TeX without delimiters.

## Build and validate

Run from this directory with Bun, Node.js, Python 3 and Chromium available.

```sh
bun install --frozen-lockfile
bun run build
bunx playwright install chromium
bun run test:browser
```

For an installed Chromium, supply its executable with `CHROMIUM_PATH=/path/to/chromium bun run test:browser`. The tests serve the built assets over HTTP and open both article hosts.
