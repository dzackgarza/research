# Browser interface

Import `dist/spectral-sequence-viewer.js` as an ES module. It registers `<spectral-sequence-viewer>`. Assign one complete input object to its `sequence` property. Static HTML can fetch JSON relative to the article and assign it after import. React can assign the same object in a ref callback after importing the module. Assignment works before or after connection once the element is defined. Each connected figure owns its page, selection, filter, and rendering lifecycle.

A successful assignment displays the configured initial page. Invalid assignments throw an error with the offending field path and, where applicable, the page and bidegree. Validate before replacing an existing figure. Interpret labels as TeX or text and never insert author strings as HTML.

Expose labelled previous, next and page selection controls. Disable movement beyond either end. Position p rightwards and q upwards. Make each visible cell inspectable, including unknown and blank zero cells. A keyboard user can enter the grid, move between cells and inspect the focused coordinate. Indicate selected terms, stability and map status in text.

All mode draws admissible arrows with both endpoints visible. Potentially nonzero mode draws nonzero and undetermined arrows. Known nonzero mode draws asserted nonzero arrows. None draws no arrows. Selection highlights incident drawn arrows. In every mode the inspector gives both maps, their endpoints, statuses and supplied formulas, marking offscreen endpoints. Arrow visibility never changes the inspector's underlying data.

## Extended contract

The default axes show native bidegrees. In a regraded view the diagram places both endpoints in display coordinates, and inspection identifies the component by its native page and source bidegree. Selecting a component with several generator images shows each assignment. The signed-coordinate and rank-two examples in the [specification](../spec.md) exercise the same public sequence setter as the Serre figures.

When a generator has a named chart endpoint, the zero image is written as `0`. Its arrow has zero status even when another generator has nonzero image under the same differential. The inspector retains both assignments under every filter. An authored differential that crosses the viewport can be inspected along its visible segment.

Each named class is selectable by keyboard. Arrow keys move to the adjacent bidegree in the displayed coordinates. When that bidegree contains several named classes, focus enters at the first class in the author's list. Tab moves between the classes.
