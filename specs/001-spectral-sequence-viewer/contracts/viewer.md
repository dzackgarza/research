# Browser interface

Import `dist/spectral-sequence-viewer.js` as an ES module. It registers `<spectral-sequence-viewer>`. Assign one complete input object to its `sequence` property. Static HTML can fetch JSON relative to the article and assign it after import. React can assign the same object in a ref callback after importing the module. Assignment works before or after connection once the element is defined. Each connected figure owns its page, selection, filter, and rendering lifecycle.

A successful assignment displays the configured initial page. Invalid assignments throw an error with the offending field path and, where applicable, the page and bidegree. Validate before replacing an existing figure. Interpret labels as TeX or text and never insert author strings as HTML.

Expose labelled previous, next and page selection controls. Disable movement beyond either end. Position p rightwards and q upwards. Make each visible cell inspectable, including unknown and blank zero cells. A keyboard user can enter the grid, move between cells and inspect the focused coordinate. Indicate selected terms, stability and map status in text.

All mode draws admissible arrows with both endpoints visible. Potentially nonzero mode draws nonzero and undetermined arrows. Known nonzero mode draws asserted nonzero arrows. None draws no arrows. Selection highlights incident drawn arrows. In every mode the inspector gives both maps, their endpoints, statuses and supplied formulas, marking offscreen endpoints. Arrow visibility never changes the inspector's underlying data.
