# Feature specification — Interactive spectral sequences

## User scenarios and testing

### Publish a sequence (P1)

A mathematician embeds a finite first-quadrant diagram in a static article. Another author uses the same data in a Vite site. Both readers can operate the figure.

**Acceptance.** Load the same fixture in plain HTML, through Vite, and by inserting it into an already loaded page. Each view opens on the configured page. Insert a second figure and navigate it independently.

### Read successive pages (P1)

A reader follows a calculation from its initial terms to its stable page.

**Acceptance.** Given pages 0 through 2 and degeneration at 2, the selector reads \(E_0,E_1,E_2=E_\infty\). Previous, next, and direct selection update the diagram, title formula, and inspector together. Remove the degeneration declaration and the last label reads only \(E_2\).

### Inspect a differential (P1)

A reader selects a term to find the maps that can affect it.

**Acceptance.** On a cohomological second page, selecting (2,1) identifies the incoming source (0,2) and outgoing target (4,0). An inspector names the endpoints, supplied formulas, and known status even when an endpoint lies beyond the viewport. Filtering changes arrow visibility without changing the data.

### Distinguish permanent terms (P2)

A reader finds a term already stable while a differential elsewhere still acts.

**Acceptance.** Mark a term stable from page 2 in a sequence degenerating at 3. Its stability label and color first appear on page 2. Another term with identical labels on successive pages receives no local stability mark without evidence supplied by the author.

## Requirements

| ID | Required behavior |
| --- | --- |
| FR-01 | Publish a documented, machine-readable input schema and a reusable browser widget in the repository. A static host can embed the distributed widget without building an application. |
| FR-02 | Accept a first page index, an ordered contiguous collection of pages defining the page count, an optional initially selected page, and an optional terminal degeneration page. Display one page at a time. Disable navigation past either end. |
| FR-03 | Place terms on integral axes with p increasing rightward and q upward. Track the extent of supplied data separately from the visible rectangle. Within the data extent, an author declares whether unlisted cells mean zero or unknown. Default to unknown. |
| FR-04 | Support the cohomological degree (r,1−r) and homological degree (−r,r−1) on page r. Compute each target from the source and convention. Terms outside the first quadrant are zero. |
| FR-05 | Offer four arrow modes. All shows every admissible arrow between visible cells, including zero maps. Potentially nonzero removes maps explicitly zero or incident to known zero terms, retaining undetermined maps. Known nonzero shows only asserted nonzero maps. None hides arrows. Show status in the inspector and identify clipped endpoints. |
| FR-06 | Accept optional plot title, axis labels, page formulas, term labels, and map formulas. Typeset mathematical content with MathJax on initial display and after navigation. Support zero, centered dot, and blank as display choices for known zero terms. Unknown terms retain a distinct marker. |
| FR-07 | Support per-term stable-from declarations and global degeneration. Use text as well as color to communicate stability. Provide keyboard access to page selection, filtering, and term inspection. |
| FR-08 | Reject contradictory or malformed input with the affected page and field or coordinate. Examples include duplicate term coordinates, negative indices, missing intermediate pages, a declared terminal page different from the last supplied page, and a claimed nonzero map incident to a known zero term. |

### Key entities

The sequence owns the grading convention, data extent, pages, and degeneration declaration. A page owns terms keyed by bidegree and map records keyed by source. A term carries its known-zero, known-nonzero, or unknown status separately from its label. A map carries zero, nonzero, or undetermined status independently of its formula. Figure settings own viewport, labels, initial page, and zero style.

### Edge cases

A single supplied page needs no navigation. A blank zero remains selectable. A missing endpoint outside the supplied rectangle but inside the quadrant has unknown status. Incoming and outgoing differentials on a declared stable page can be shown as zero where global degeneration implies vanishing of that page's differential.

## Success criteria

- From a React application built with Vite, an author can pass the same sequence as a data object. A plain HTML author can load the viewer with one JavaScript module.
- Selecting a term highlights its visible incoming and outgoing arrows. For example, show a nonzero second differential from (0,1) to (2,0), a term at (0,0) marked stable from page 2, and degeneration at page 3. On page 2 the reader can inspect the highlighted map and read the local stability label. On page 3 the reader sees the infinity-page identification.
- An author can set inclusive minimum and maximum values on each visible axis and supply a page formula such as \(E_2^{p,q}=H^p(B;H^q(F))\). An unknown cell has a distinct marker such as a question mark even when the zero glyph is blank.

- An author can reuse one dataset across all three publishing scenarios without changing its mathematical content.
- A reader can reproduce the page labels, endpoints, filter results, and stability distinctions specified above using the public controls.
- Changing zero style preserves every map status and every term's inspectable information.

## Assumptions

Authors supply page data and stability information. The viewer presents that data. Computing cohomology, proving degeneration, and resolving extensions in an abutment fall outside this feature. Choice of rendering library and component framework belongs to implementation planning.

The proposed implementation is a framework-independent TypeScript Web Component registered as `<spectral-sequence-viewer>`, with SVG for the diagram and MathJax for its mathematical labels. React is a possible host and an implementation option. The public embedding behavior above governs the choice.
