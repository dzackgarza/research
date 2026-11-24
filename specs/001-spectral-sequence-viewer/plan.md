# Interactive spectral sequences

Branch `main`. Design for the [viewer specification](spec.md).

## Technical context

Publish a browser ES module and its adjacent assets from a self-contained TypeScript package in `widgets/spectral-sequence-viewer/`. Use Bun for package management, Vite library mode for distribution, JSON Schema with Ajv for structural validation, MathJax for TeX, and Playwright for browser acceptance. The browser holds the figure state in memory. Authors supply finite page data.

## Implementation order

1. Define the [input model](data-model.md) and publish the schema alongside the module. Validate the entire input before rendering. Index terms by bidegree and differentials by source within each page.
2. Register the [custom element](contracts/viewer.md). Draw the selected page, expose its controls, and update the inspector from the same page state. Resolve endpoint status before clipping. Typeset the title and labels after updates.
3. Build the distribution and expose the same fixture through static HTML, late insertion, and React in Vite. Exercise the [validation scenarios](quickstart.md) through the shipped entry point.

## Project structure

The package owns `src/`, `schema/sequence.schema.json`, `examples/`, and `tests/`. Place the common JSON fixture under `examples/`. The build emits the public module and required assets under `dist/`. Ship the built asset set so a static article author can copy it directly. Host examples consume the public files.

## Constitution check

This checkout supplies governance through `INTENT.md`, `AGENTS.md`, and `CONTRIBUTING.md`. The design satisfies the presentation boundary before and after interface design. Each displayed assertion traces to author data or the grading and display rules in the specification. Browser tests establish observable display behavior. The viewer supplies no computational evidence to the formal programme.

## Extensions to the first-quadrant implementation

Implement signed native coordinates and explicit support in the shared model first. The plotting layer consumes these coordinates and projects both endpoints for display. Selection resolves to the native term before looking up an incident component. Extend the component record and inspector together for multiple generator images. The acceptance examples and open work are in the [specification](spec.md) and [task list](tasks.md).

## Class-level chart inspection

Index named classes within each page. Use explicit predecessor links for page transitions and class references for incidence. Display author-supplied products and extensions as separate relations. Clip asserted differential segments in projected plot coordinates while retaining native endpoints for inspection.
