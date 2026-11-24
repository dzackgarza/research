# Tasks for the interactive spectral sequence viewer

All task paths are relative to `widgets/spectral-sequence-viewer/`. Use the [specification](spec.md), [model](data-model.md), [browser contract](contracts/viewer.md), and [validation scenarios](quickstart.md). Run each story through the built module.

## Phase 1 — Package setup

- [X] T001 Configure Bun, TypeScript, Vite library mode, Ajv, MathJax and Playwright Chromium in `package.json`, `bun.lock`, `tsconfig.json`, `vite.config.ts` and `playwright.config.ts`. Provide the build and browser-test commands in the quickstart, static file serving and a React/Vite example host.

## Phase 2 — Shared input

- [X] T002 [P] Publish the author schema in `schema/sequence.schema.json`. Encode “Required `convention` (cohomological or homological), `firstPage`, `extent`, and nonempty ordered `pages`.” Encode the required and optional fields, enums, defaults and integer constraints in every row of the model table, including term labels, formulas, both rectangles and stable-from declarations.
- [X] T003 [P] Author `examples/sequence.json` for all hosts with pages 0–3, asserted count 4, initial page 2, degeneration at 3, a nonzero second differential (0,1) → (2,0), a term stable from 2 at (0,0), and an unmarked repeated label. Include the inspected (2,1) and its incoming and outgoing maps with formulas. Choose consistent statuses, a viewport clipping its incoming source, known zeros, and unknown cells.
- [X] T004 Implement schema and semantic validation in `src/sequence.ts`. Enforce “Optional `pageCount` equals the array length. Page indices increase by one from firstPage.” Derive omitted count, require a supplied initial page, and allow degeneration beyond the last page. Enforce “Inclusive nonnegative integer `pMin,pMax,qMin,qMax`, each minimum at most its maximum”, unique coordinates per record list, and unique stability coordinates. Require term and map sources within the data extent. Return page and field or coordinate on error.
- [X] T005 Implement coordinate lookup and both grading displacements in `src/differentials.ts` and use them in `src/sequence.ts` to validate nonzero assertions before accepting input. “Outside the extent a first-quadrant cell is unknown. Outside the quadrant it is zero.” Apply the unlisted policy only inside the extent. Reject nonzero maps incident to known zeros or to permanent terms from their stable page, or on or after global degeneration. A missing or undetermined map retains undetermined status unless forced zero.

## Phase 3 — US1 Publish a sequence (P1, MVP)

Acceptance: load one dataset in static HTML, React/Vite and after document load. Each instance opens on its configured page. Navigate one figure and observe that the other stays on its original page.

- [X] T006 [P] [US1] Write `tests/publish.spec.ts` for the three hosts, property assignment before and after connection, independent page changes, and preservation of a valid figure after an invalid replacement. Exercise count mismatch, missing pages, duplicates, negative indices and contradictory maps through the public setter and check the reported location.
- [X] T007 [P] [US1] Create static and late-insertion embeds in `examples/static/index.html` and the React ref embed in `examples/react/main.tsx` with its Vite entry `examples/react/index.html`. Load the same fixture and distributed entry point in each.
- [X] T008 [US1] Register the element and its atomic sequence setter in `src/index.ts` and implement the first usable view in `src/viewer.ts`. Show the configured initial page, labelled direct selection and its actual cells. Give each instance its own state. Use the inclusive viewport with p rightwards and q upwards.
- [X] T009 [US1] Wire distribution in `vite.config.ts` to ship `dist/spectral-sequence-viewer.js`, its schema and referenced assets. Open the static example using only shipped assets and the fixture. Run T006 through all hosts.

## Phase 4 — US2 Read successive pages (P1)

Acceptance: navigate by keyboard from page 0 to the last supplied page. Check the page formula, diagram and selected term at each transition, including single-page and post-degeneration views.

- [X] T010 [P] [US2] Write `tests/pages.spec.ts` for previous, next and direct selection, boundary disabling, matching page labels and formulas, retained coordinate, and synchronized inspector. Test absent, displayed and out-of-range degeneration, including four selectable pages with degeneration at 2.
- [X] T011 [P] [US2] Implement scoped MathJax conversion in `src/math.ts`. Package required fonts and assets, treat author strings as text or TeX, and discard stale results after rapid navigation. Verify rendered math on initial load and after navigation without a host MathJax global.
- [X] T012 [US2] Complete keyboard page controls, axis labels, title, page formula, term labels and coordinate inspection in `src/viewer.ts`. Refresh from one selected-page state. Identify the first infinity page only when supplied, preserve the selected cell and filter, and disable navigation beyond either end. Run T010.

## Phase 5 — US3 Inspect a differential (P1)

Acceptance: inspect (2,1) on cohomological page 2 and identify (0,2) and (4,0), even across a viewport edge. Verify the reversed displacement under homological grading.

- [X] T013 [P] [US3] Write `tests/differentials.spec.ts` for both conventions, clipped endpoints, four filters, selection highlighting, forced zeros, and unchanged inspector information when filters change. Exercise all three zero glyphs and keyboard inspection of a blank zero beside an unknown cell.
- [X] T014 [P] [US3] Render SVG arrows and focusable cells from one coordinate layout in `src/diagram.ts`. Draw both-visible admissible arrows in All mode, exclude known zeros in Potentially nonzero, retain only asserted nonzeros in Known nonzero, and draw none in None. Highlight visible incident arrows and render unknown cells distinctly for every zero style.
- [X] T015 [US3] Connect the diagram, keyboard grid movement, labelled filter and inspector in `src/viewer.ts`. Show both incident maps with endpoints, formulas, status and offscreen indications regardless of filtering. Run T013 and confirm page changes preserve filter and coordinate.

## Phase 6 — US4 Distinguish permanent terms (P2)

Acceptance: compare (0,0) before page 2, on page 2, and at global degeneration on page 3. Its first stable page remains readable. A repeated label alone confers no local stability.

- [X] T016 [P] [US4] Write `tests/stability.spec.ts` for the acceptance example, including stability text and color, absence of an early or inferred mark, and vanishing incident maps after the declared stable page begins.
- [X] T017 [P] [US4] Display local stability with text and color in `src/diagram.ts` and its first page in the inspector in `src/viewer.ts`. Preserve local provenance when global degeneration also applies. Run T016 after both tasks land.

## Phase 7 — Publication

- [X] T018 Document the public schema, asset-copy instructions, static, dynamic and React embeddings in `README.md`. Ship the final `dist/spectral-sequence-viewer.js` with its required assets and verify the full quickstart from the frozen lockfile against that distribution.

## Dependencies and delivery

Complete setup before T002 and T003. T004 consumes the schema; T005 consumes the validated model. Deliver US1 first as the independently usable publishing MVP. US2 extends its page selector. US3 extends its selection and inspector. US4 uses the same diagram and inspector to distinguish permanence. Finish publication after all four stories.

Within each phase the marked tasks can start together. For US1 the browser assertions and host examples use the agreed public interface. For US2 the navigation scenarios and math conversion use separate files. For US3 the inspector scenarios and SVG rendering share the coordinate contract. For US4 the browser scenarios and visual treatment use the model's existing permanence rules. Write the acceptance assertions before wiring their corresponding behavior; run them against the finished increment.

## Signed grading, projection, and component maps

The completed first-quadrant tasks above describe the original implementation. The extended stories in the [specification](spec.md) require the following public behaviours.

- [X] T019 Support signed bidegrees in the schema, records, extents, viewport, and endpoint lookup. Make first-quadrant vanishing a support declaration. Exercise the negative-column example and its unknown neighbour through the public viewer.
- [X] T020 Separate the display projection from the native grading in chart placement, axes, clipping, keyboard navigation, and selection. Check the same indexed component in the native and total-degree views under both conventions.
- [X] T021 Represent multiple generator images per component in the schema and inspector. Exercise the rank-two source in the specification through the built widget and verify both assignments remain attached to one arrow.

## Phase 8: Convergence

- [X] T022 Make a displayed differential selectable with pointer and keyboard in `src/diagram.ts` and `src/viewer.ts`. Selecting the arrow from display coordinates (1,−2) to (2,0) must identify the native component from (−2,3) to (0,2). Exercise the arrow itself in `tests/grading.spec.ts` per the regraded-sequence acceptance scenario and FR-07 (missing)
- [X] T023 Distinguish clipped endpoints in the inspector with a non-prose cue independent of mathematical status. Determine visibility in projected coordinates. Exercise the same known nonzero endpoint inside and outside the viewport while preserving its formula, status, and inspectability under all filters per FR-05 and T015 (partial)
- [X] T024 Preserve a distinct author-supplied component formula alongside its generator assignments. In the inspector, exercise a component with a named formula and two generator images; verify the name and both actions remain visible without duplicating the assignments per the differential-inspection acceptance scenario and FR-06 (partial)
- [X] T025 Typeset mathematical labels that still use plain text, including grid zero numerals, the stability page number, and the selectable page expressions. Exercise the open selector, navigation, zero-style changes, and keyboard access with the shipped MathJax renderer per FR-06, T011 and T012 (partial)
- [X] T026 Extend the public browser scenarios to reject a negative page index while retaining the previous figure, and to verify the selected page’s actual formula, cell data, and inspector indices after navigation. Retain the separate signed-bidegree acceptance case per FR-08, T006 and T010 (partial)

## Phase 9: Class-level charts

- [X] T027 Select individual classes sharing a bidegree; attach component assignments to named classes and represent individual permanence.
- [X] T028 Follow an authored representative to a surviving or quotient class on the next page.
- [X] T029 Draw and inspect authored multiplication relations and limiting-page extensions independently of differential filters.
- [X] T030 Clip asserted differentials crossing the viewport, including those with both endpoints outside.
