# GAP NConvex Online Provenance Snapshot (2026-02-17)

Date accessed (UTC): 2026-02-17
Auditor: Codex
Scope: replace prior NConvex source-blocked placeholder with source-backed method inventory and argument surfaces.

---

## Surveyed sources

Package and manual:

- `https://homalg-project.github.io/NConvex/`
- `https://homalg-project.github.io/NConvex/doc/chap0_mj.html`
- `https://homalg-project.github.io/NConvex/doc/chapInd_mj.html`
- `https://homalg-project.github.io/NConvex/doc/chap3_mj.html`
- `https://homalg-project.github.io/NConvex/doc/chap4_mj.html`
- `https://homalg-project.github.io/NConvex/doc/chap5_mj.html`
- `https://homalg-project.github.io/NConvex/doc/chap6_mj.html`
- `https://homalg-project.github.io/NConvex/doc/chap7_mj.html`

Repository and declaration sources:

- `https://github.com/homalg-project/NConvex`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ConvexObject.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Cone.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Fan.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polyhedron.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Polytope.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/ZSolve.gd`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/PackageInfo.g`
- `https://raw.githubusercontent.com/homalg-project/NConvex/master/README.md`

---

## Evidence captured in this pass

- Canonical manual pages were retrievable and yielded method-index coverage for cones, fans, polyhedra, polytopes, convex-object attributes, and zsolve surfaces.
- Method signatures and argument names were lifted from manual function headers.
- Additional declared surfaces not listed in current manual index were captured from `gap/*.gd` declarations as `[SRC]` source-only surfaces.
- Package metadata (`PackageInfo.g`) confirmed current version line (`2025.12-02`) and dependency context (`CddInterface`, `NormalizInterface`, optional `TopcomInterface`, optional `4ti2Interface`).

---

## Blocker status update

Previous blocker status is cleared:

- Earlier passes recorded manual-index retrieval failure for NConvex.
- In this pass, `chap0_mj`, `chapInd_mj`, and chapter pages were directly retrievable.
- NConvex checklist/reference surfaces were expanded from package-load-only triage to method-level inventory with argument surfaces and constraints.

---

## Reproducibility notes

Representative retrieval commands used in this pass:

```bash
curl -sL https://homalg-project.github.io/NConvex/doc/chapInd_mj.html
curl -sL https://homalg-project.github.io/NConvex/doc/chap4_mj.html
curl -sL https://raw.githubusercontent.com/homalg-project/NConvex/master/gap/Cone.gd
```

Function-index extraction and declaration reconciliation were performed by local command-line parsing of those retrieved artifacts.
