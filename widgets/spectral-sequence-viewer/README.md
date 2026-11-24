# Spectral sequence viewer

For a worked example, serve this directory with `python3 -m http.server` and open [The order of π₄(S²)](examples/serre/index.html) at `/examples/serre/`. The article uses the cohomological and homological Serre spectral sequences of the same fibration.

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

Use `supportedColumns` to declare the columns that can contain nonzero terms on any page. Outside those columns all terms vanish, even beyond the supplied extent. The viewport only crops the drawing.

A term's `label` appears on the chart. Its optional `module` identifies the group beneath the indexed term. To show the action on a generator, supply the source term's `generator` and the map's `image` as TeX. The viewer supplies the image of a generator under a known zero map.

Set `support` to `"unrestricted"` for signed native bidegrees. The default is `"first-quadrant"`. Column restrictions, term records, map sources, and stability declarations always use native degrees.

Set `settings.projection` to `"total-filtration"` to plot total degree horizontally and filtration degree vertically. The default is `"native"`. An explicit viewport bounds the horizontal and vertical display coordinates. With no viewport, the viewer projects the extent. Arrow keys follow the displayed axes, and inspection names the native component.

For a component with several generator images, supply an ordered `assignments` array on the map, for example `[{"generator":"a","image":"u"},{"generator":"b","image":"0"}]`. Each assignment occupies one row between the same source and target. Set the status on the component as a whole.

An assignment with class IDs draws an arrow at those classes. Assignments
without class IDs share a component arrow between bidegrees. In a mixed list,
the filters apply to the named arrows and to the unnamed group separately.
Select a class to highlight the edges that name it. A term marked “stable”
can contain individually labelled classes; “permanent” belongs to the class
on which the author declared it.

Products with the same endpoints appear as separate curves. Click a curve or
focus it and press Enter to inspect its formula.
