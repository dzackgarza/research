# Design decisions

| Decision | Reason | Alternative considered |
| --- | --- | --- |
| Use the proposed TypeScript custom element with one registration module. | A static page, a dynamically inserted element, and a React ref can all assign the same object property. | A React component as the public API would require a separate static mount interface. |
| Build an ES library with Vite in its own package. | Plain HTML can import the distributed module directly. The root repository is a research and Quarto workspace. | Coupling the module to the book build would make a second site's deployment depend on Quarto. |
| Use SVG for axes and arrows and focusable HTML controls for cells, placed from the same coordinate layout. | Blank cells retain keyboard targets, and TeX labels can use normal HTML math containers. | A canvas would need separate hit testing and an accessible interaction surface. |
| Package MathJax and its required assets with the distribution. Scope conversion to each figure and discard obsolete asynchronous results. | Static hosts can serve the complete figure. Rapid page changes and multiple figures must keep their own labels. | Depending on a host MathJax global works for some book pages but adds a prerequisite for independent hosts. |
| Use JSON Schema plus a semantic validation pass. | The schema can describe record shapes and enums. Continuity and incidence require comparisons across records. | A TypeScript type alone cannot validate an article author's JSON. |

The repository's `writing/dependency-graph.md` already updates math in an interactive article. The reusable viewer takes responsibility for its own math lifecycle. See [MathJax dynamic content](https://docs.mathjax.org/en/latest/advanced/typeset.html), [Vite library mode](https://vite.dev/guide/build.html#library-mode), and [React custom elements](https://react.dev/reference/react-dom/components#custom-html-elements).
