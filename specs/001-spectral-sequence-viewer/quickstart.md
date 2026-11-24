# Validate the distributed viewer

These commands describe the package entry points to provide during implementation. From `widgets/spectral-sequence-viewer/`, run `bun install --frozen-lockfile`, `bun run build`, then `bun run test:browser` with Playwright Chromium installed. The browser suite must serve a static example from the built assets and start the Vite host. Use the same JSON fixture for each host.

| Scenario | Observable result |
| --- | --- |
| Open the static article, the React/Vite article, and a page that inserts a second viewer after load. | All open on the configured page. Changing the second figure leaves the first on its original page. Math is typeset after initial load and navigation. |
| Supply pages 0–3, count 4, and degeneration at 2. Navigate by keyboard with all three page controls. | Page 2 is labelled E₂ = E∞. Page 3 remains selectable. End controls disable at their boundaries. Removing degeneration or setting it beyond the fixture removes the infinity label. |
| On cohomological page 2 inspect (2,1) with (0,2) beyond the viewport. | The inspector identifies incoming (0,2) and outgoing (4,0), preserving formulas and flagging clipping. Switching to homological grading reverses the displacement. |
| Declare a nonzero map from (0,1) to (2,0) on page 2, local stability at (0,0) from 2, and degeneration at 3. | Selecting the source highlights its visible nonzero arrow. Page 3 shows global degeneration and still gives 2 as the first local stable page. A repeated label elsewhere acquires no local mark. |
| Cycle the four filters with zero, nonzero and undetermined visible maps. Cycle zero styles and focus a blank zero. | The drawn arrows follow the contract. Inspection remains available, and unknown cells keep their distinct mark. |
| Assign each malformed specimen to a previously valid figure. | A count mismatch, gap, duplicate, negative coordinate, and nonzero map conflicting with a zero endpoint or degeneration each identify the offending input. The previous figure remains usable. |
