# Living Working Paper

This directory is the native mathematical synthesis artifact for the repo. Cards route
work; reports capture branch outputs; this paper rebuilds the mathematical narrative
with visible provenance and uncertainty.

Use `just paper-build` from the repo root to compile `paper/main.tex`.

Rules:

- Add serious claims to the paper only with a margin-note status.
- Link claims to cards, workstream reports, sources, computations, or review artifacts.
- Mark conjectural, computation-supported, disputed, and human-review-needed claims in
  the margin.
- Preserve failed mathematical explorations when they rule out a strategy or clarify a
  boundary. Do not preserve broken code here.
