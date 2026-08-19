# PALP Online Provenance Snapshot (2026-02-17)

- Snapshot date (UTC): 2026-02-17
- Auditor: Codex
- Scope: first-class checklist/reference surface creation for PALP package command and wrapper surfaces.

---

## Canonical sources consulted

1. PALP package metadata (scope and maintained package identity):
   - `https://packages.ubuntu.com/jammy/math/palp`
2. Debian PALP manpage hub:
   - `https://manpages.debian.org/unstable/palp/palp.1.en.html`
3. Command manpages (CLI synopsis and option contracts):
   - `https://manpages.org/polyx`
   - `https://manpages.org/classx`
   - `https://manpages.org/cwsx`
   - `https://manpages.debian.org/unstable/palp/nef.x.1.en.html`
   - `https://manpages.org/morix`
4. Sage lattice polytope docs (optional PALP wrapper methods):
   - `https://doc.sagemath.org/html/en/reference/discrete_geometry/sage/geometry/lattice_polytope.html`

---

## Extracted evidence used in docs

- Package scope and domain:
  - PALP is documented as a package for lattice polytopes/complete-weight-system workflows.
  - Package metadata describes practical focus mainly on dimensions up to four.

- Command inventory:
  - CLI programs `poly.x`, `class.x`, `cws.x`, `nef.x`, and `mori.x` are documented with synopsis-level argument shapes.

- Option surfaces captured:
  - `poly.x`: `-h`, `-f`, `-g`, `-p`, `-r`, `-v`.
  - `class.x`: `-h`, `-f`, `-m`, `-p`, `-v`.
  - `cws.x`: `-h`, `-f`, `-w[#]`.
  - `nef.x`: `-h`, `-f*`, `-N`, `-H`, `-Lv`, `-p`, `-D`, `-P`, `-t`, `-c*`.
  - `mori.x`: `-h`, `-f`, `-g`, `-m`, `-P`, `-K`, `-b`.

- Sage wrapper evidence:
  - Sage docs explicitly mark optional-package `palp` requirements for:
    `all_points()`, `all_points_boundary()`, `all_points_not_interior_to_facets()`,
    `integral_points()`, and `fibration_generator(dim)`.

---

## Residual fidelity gap

- Several PALP options are encoded with compact manpage notation (`-f*`, `-c*`, and multi-parameter modes) that require deeper upstream manual parsing for full typed argument schemas.
- Current pass records source-backed synopsis-level contracts only; a follow-up can expand these into per-option typed tables from the full PALP manual.
