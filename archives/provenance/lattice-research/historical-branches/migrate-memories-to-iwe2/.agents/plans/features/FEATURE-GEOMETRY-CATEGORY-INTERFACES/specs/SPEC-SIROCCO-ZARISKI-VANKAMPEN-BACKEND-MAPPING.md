---
id: SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING
trackerStatus:
  type: spec
parents:
- '[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]'
dependsOn:
- '[[TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS]]'
title: Map Sirocco and Sage Zariski-Van Kampen as plane-curve complement group
  backends
status: complete
priority: medium
requirement: Record the source-backed boundary for using Sirocco through Sage to
  compute braid monodromy and finitely presented fundamental groups of affine and
  projective plane-curve complements.
acceptanceCriteria:
- Upstream SIROCCO2 README/source and Sage Zariski-Van Kampen docs/source are cited.
- The exact mathematical objects exposed by Sage are named.
- Sirocco root continuation is separated from project-level curve-complement group
  ownership.
- Local availability and limitations are recorded.
complexity: 40
tags:
- FEATURE-GEOMETRY-CATEGORY-INTERFACES
---
# Sirocco Zariski-Van Kampen Backend Mapping

## Source Scope

- Upstream SIROCCO2 repository:
  <https://github.com/miguelmarco/sirocco2>.
- Temporary upstream checkout inspected at `/tmp/tmp.NCIpabPSo3/SIROCCO2`.
- Upstream files inspected:
  `README.md`, `ZVK.py`, `sage-sirocco_interface.pyx`, and `include/sirocco.h`.
- Sage documentation, Zariski-Van Kampen method:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/zariski_vankampen.html>.
- Sage documentation, projective plane curve `fundamental_group()`:
  <https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/projective_curve.html>.
- Installed Sage source:
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/schemes/curves/zariski_vankampen.py`.
- Local import checks:
  `sage -c 'from sage.schemes.curves.zariski_vankampen import fundamental_group, braid_monodromy'`
  succeeded, and `sage.libs.sirocco` resolves to
  `/home/dzack/miniforge3/envs/sage/lib/python3.12/site-packages/sage/libs/sirocco.cpython-312-x86_64-linux-gnu.so`.

## Backend Boundary

Sirocco is not a curve-complement group library by itself. Its core C/C++ surface
is certified continuation of roots of bivariate complex polynomials along a
one-dimensional parameter path. Upstream exposes `homotopyPath`,
`homotopyPath_mp`, `homotopyPath_comps`, and `homotopyPath_mp_comps`; the Sage
interface exposes corresponding continuation helpers such as `contpath` and
`contpath_mp`.

Sage's `zariski_vankampen.py` is the geometry-facing layer. It uses Sirocco to
follow strands, converts piecewise-linear strands to braids, computes braid
monodromy for plane-curve projections, and converts braid monodromy to finite
presentations of fundamental groups of affine or projective plane-curve
complements.

The project-level public owner should therefore be one of:

- a plane-curve complement object;
- a braid-monodromy object for a chosen plane-curve projection;
- a finitely presented fundamental group object attached to the complement.

It should not be a raw Sirocco wrapper. Sirocco is a backend bridge below the
mathematical owner.

## Candidate Surface Mapping

| Backend surface | Project owner candidate | Public meaning | Admission status |
| --- | --- | --- | --- |
| SIROCCO2 `homotopyPath*` | backend bridge only | Certified continuation of one root of `f(x,y)` along a parameter segment | Backend evidence; not public geometry vocabulary. |
| Sage `followstrand(f, factors, x0, x1, y0a, prec)` | braid-monodromy computation internals | Piecewise-linear certified path of a root, avoiding roots of optional factors | Internal backend step. |
| Sage `braid_from_piecewise(strands)` | braid group / braid-monodromy object | Braid represented by piecewise-linear strands | Candidate backend utility after braid object ownership exists. |
| Sage `braid_monodromy(f, arrangement=(), vertical=False)` | plane-curve projection braid monodromy | Images of a geometric basis of the complement of the discriminant in `CC` | Candidate public method on plane-curve projection/complement spec. |
| Sage `fundamental_group_from_braid_mon(...)` | finitely presented group from braid monodromy | Zariski-Van Kampen presentation construction | Candidate backend bridge once group/presentation ownership exists. |
| Sage `fundamental_group(f, simplified=True, projective=False, puiseux=True)` | affine or projective plane-curve complement | Presentation of `pi_1` of the curve complement | Candidate public method through a curve-complement spec. |
| Sage plane curve `C.fundamental_group()` | plane curve complement | Presentation of the complement group of `C` | Candidate source evidence for method placement. |

## Mathematical Inputs And Outputs

For `braid_monodromy`, the mathematical input is not an arbitrary curve object:
it is a bivariate polynomial defining a plane curve over `QQ` or a number field
with a fixed complex embedding, together with a chosen projection and optional
arrangement/component data.

The output is braid monodromy of the projection: braids associated to a
geometric basis of loops around the discriminant of the projection, plus
bookkeeping that relates strands to arrangement factors and vertical components.

For `fundamental_group`, the input is a plane affine curve polynomial and flags
selecting affine/projective and Puiseux behavior. The output is a finitely
presented group representing the fundamental group of the complement of the
curve, as computed by Zariski-Van Kampen from braid monodromy.

For projective plane curves, Sage documentation exposes `C.fundamental_group()`
as a curve method requiring `sirocco`; the returned object is still a finite
presentation, not a canonical topological space object.

## Limitations And Audit Requirements

- The backend is restricted to plane-curve complement computations as checked
  here. It is not a general fundamental-group backend for arbitrary varieties,
  manifolds, complements, or higher-dimensional arrangements.
- The polynomial must be over `QQ` or a number field with a complex embedding in
  the Sage route checked here.
- The method depends on projection choices, vertical-component handling,
  discriminant loops, and optional simplification of the resulting presentation.
  Specs must record which data is mathematical output and which data is a
  backend presentation choice.
- A finitely presented group returned by Sage is not automatically a canonical
  group object for equality or isomorphism questions. Later specs need a policy
  for presentations, simplification, meridians, arrangement-factor labeling, and
  comparison.
- Sirocco continuation failures are backend failures, not reasons to change the
  mathematical meaning of the requested group.

## Local Availability Finding

- Searched: `sage -c` imports for `fundamental_group` and `braid_monodromy`;
  `sage -python` import for `sage.libs.sirocco`; installed Sage source path;
  upstream README/source.
- Found: `sage -c` imports succeeded; `sage.libs.sirocco` is installed as a
  compiled extension; a small Sage example for `x^2 + y^3` computed braid
  monodromy `([(s1*s0)^2], {0: 0, 1: 0, 2: 0}, {}, 3)` and a finitely presented
  group `< x0, x1 | x1^-1*x0^-1*x1^-1*x0*x1*x0 >`.
- Conclusion: inference based on the checked local environment: Sirocco is
  available through Sage here and can support future implementation work after
  geometry owner specs are written.
- Confidence: High for local availability of this Sage route.
- Gaps: no package installation test was run; no broad example suite or
  long-running projective/arrangement case was executed.

## Non-Admission Finding

- Searched: upstream SIROCCO2 README/source; Sage Zariski-Van Kampen docs/source;
  local Sage import and one small execution example; existing geometry backend
  mapping specs.
- Found: source-backed support for root continuation, braid monodromy, and
  finite presentations of plane-curve complement groups, but no repo-level
  category owner for plane-curve complements, braid monodromy, finitely presented
  groups with meridians, or presentation comparison policy.
- Conclusion: inference based on the checked sources: create no implementation
  card yet. The mapping is admitted as backend evidence for later geometry
  category specs.
- Confidence: High.
- Gaps: the future geometry category spec still needs to decide method names,
  ownership, presentation semantics, and how this relates to existing Sage curve
  methods.

## Follow-Up Consequence

No new wrapper or dependency-admission task is warranted from this card alone.
The remaining public-surface choices are tracked by
`[[DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE]]`, including:

- whether `C.complement().fundamental_group()` or `C.fundamental_group()` is the
  public owner;
- whether braid monodromy is exposed as an intermediate mathematical object;
- how presentations, meridians, arrangements, and vertical components are typed;
- whether projective-complement relations and affine-complement relations live
  on separate complement objects or as flags on one construction.

## 6-Gate Protocol Review Log

**Review date:** 2026-05-07
**Reviewer:** Hermes Agent (subagent, 6-gate delegated review)
**Card:** SPEC-SIROCCO-ZARISKI-VANKAMPEN-BACKEND-MAPPING
**Outcome:** PASS (all gates satisfied; one advisory observation recorded)

---

### G1 — Source Grounding: PASS

Every upstream source cited in the card resolves to an accessible resource:

| Claimed source | Verification method | Result |
|---|---|---|
| Upstream SIROCCO2 GitHub (`miguelmarco/sirocco2`) | HTTP HEAD → 200 | Exists |
| Temporary checkout `/tmp/tmp.NCIpabPSo3/SIROCCO2` | `ls` listing; README.md, ZVK.py, `sage-sirocco_interface.pyx`, `include/sirocco.h` all present | Exists |
| Sage Zariski-Van Kampen docs URL | HTTP HEAD → 200 (Cloudflare, last-modified 2025-12-27) | Exists |
| Sage `projective_curve.html` docs URL | HTTP HEAD → 200 | Exists |
| Installed Sage source `zariski_vankampen.py` | `ls` confirms path; file exists | Exists |
| Compiled extension `sage/libs/sirocco.cpython-312-x86_64-linux-gnu.so` | `ls` confirms path; file exists | Exists |
| Sage import `fundamental_group`, `braid_monodromy` | `sage -c` import + live computation succeeded | Works |
| SIROCCO2 README content | Read lines 1-50; confirms "homotopy continuation of a given root" description, Sage integration, and fundamental_group methods | Consistent with card claims |

No dead links, missing files, or unverifiable references. Source grounding is complete and reproducible.

---

### G2 — Sage Surface Completeness: PASS

The candidate surface mapping table covers the full backend-to-public chain:

- C-level SIROCCO2: `homotopyPath`, `homotopyPath_mp`, `homotopyPath_comps`, `homotopyPath_mp_comps`
- Sage interface layer: `contpath`, `contpath_mp`, `followstrand`
- Braid construction: `braid_from_piecewise`
- Braid monodromy: `braid_monodromy`
- Group construction: `fundamental_group_from_braid_mon`, `fundamental_group`
- Curve method: `C.fundamental_group()`

Every surface is classified as backend bridge, internal utility, candidate public method, or source evidence. Both affine and projective cases are addressed. No Sage-exposed Zariski-Van Kampen surface appears to be omitted.

---

### G3 — Mathematical Correctness: PASS

The mathematical characterization is sound:

- **Sirocco identity:** Correctly identified as a certified root continuation engine, not a curve-complement group library. This matches the upstream README ("Sirocco Is a ROot Certified COntinuator").
- **Input domain:** Correctly restricted to bivariate polynomials over QQ or number fields with complex embedding, with a chosen projection and optional arrangement data. This matches Sage's `braid_monodromy` signature and source.
- **Output domain:** Correctly identified as braid monodromy (braids associated to geometric basis loops around the discriminant) and finitely presented groups (not canonical topological space objects).
- **Non-canonical presentations:** Correctly notes that finitely presented groups are not automatically canonical for equality/isomorphism. This is a real mathematical limitation of the Sage output type.
- **Limitations:** Correctly scoped to plane-curve complements only — not general varieties, manifolds, or higher-dimensional arrangements.
- **Live verification:** A small test (`x^2 + y^3`) confirmed braid monodromy `([(s1*s0)^2], {0: 0, 1: 0, 2: 0}, {}, 3)` — matches the card exactly. The fundamental group relator differs slightly from the card's recorded string (Sage outputs `x1*x0*x1*x0^-1*x1^-1*x0^-1`; card records `x1^-1*x0^-1*x1^-1*x0*x1*x0`), which is consistent with the card's own warning about non-canonical presentations — see G3 observation below.

**G3 Observation (advisory, not blocking):** The fundamental group presentation recorded in the "Local Availability Finding" section differs from the current Sage output. The card says `< x0, x1 | x1^-1*x0^-1*x1^-1*x0*x1*x0 >` but `sage -c` returns `< x0, x1 | x1*x0*x1*x0^-1*x1^-1*x0^-1 >`. This is expected — the card itself documents (line 113-116) that presentations are not canonical and may vary with version or random choices. No mathematical error; the braid monodromy agrees exactly.

---

### G4 — Nonmathematical Rejection: PASS

The card correctly identifies and rejects non-geometric ownership:

- Raw Sirocco wrapper is explicitly rejected ("It should not be a raw Sirocco wrapper. Sirocco is a backend bridge below the mathematical owner." — line 67-68).
- No implementation card is authorized; the "Non-Admission Finding" section (line 136-151) explicitly blocks premature implementation.
- Continuation failures are classified as backend failures, not reasons to change mathematical meaning (line 117-118).
- The card stays firmly in research/admission scope, consistent with the parent feature's acceptance criterion: "Curve-complement and monodromy backend work stays research-scoped until category ownership is explicit."

---

### G5 — Ambiguity Routing: PASS

Open design questions are explicitly routed to a decision card:

- Referenced: `[[DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE]]` (line 157)
- Four explicit routing items listed:
  1. Public owner: `C.complement().fundamental_group()` vs `C.fundamental_group()`
  2. Whether braid monodromy is an exposed intermediate object
  3. Typing of presentations, meridians, arrangements, vertical components
  4. Affine/projective complement relation modeling

**G5 Advisory:** The referenced decision card `DECISION-SIROCCO-PLANE-CURVE-COMPLEMENT-GROUP-SURFACE` does not yet exist in the workspace. This is acceptable for a spec card (decisions are downstream), but the dependency edge should be formalized when the decision card is created. The missing `dependsOn` entry for `TASK-RESEARCH-SIROCCO-CURVE-COMPLEMENT-FUNDAMENTAL-GROUPS` is similarly noted — that task card does not yet exist.

---

### G6 — Obligation Preservation: PASS

The card preserves future obligations:

- Parent feature: `[[FEATURE-GEOMETRY-CATEGORY-INTERFACES]]` — exists and contains this spec in its tree.
- States "create no implementation card yet" (line 146) — honoring the research-scoped boundary.
- Records local availability with explicit confidence level ("High") and gaps ("no package installation test was run; no broad example suite or long-running projective/arrangement case was executed").
- Limitations section (lines 102-118) itemizes five specific constraints that downstream specs must address.
- Follow-Up Consequence section (lines 153-164) enumerates the remaining public-surface choices that are externalized.

---

### Summary

| Gate | Verdict | Notes |
|---|---|---|
| G1 — Source Grounding | PASS | All 8 sources verified; no dead references |
| G2 — Sage Surface Completeness | PASS | Full C→Sage→public chain mapped |
| G3 — Mathematical Correctness | PASS | Sound mathematical characterization; minor presentation variance is expected |
| G4 — Nonmathematical Rejection | PASS | Raw wrapper correctly rejected; implementation blocked |
| G5 — Ambiguity Routing | PASS | Four open items routed to decision card (not yet created) |
| G6 — Obligation Preservation | PASS | Future obligations, limitations, and gaps recorded |

**Overall: PASS.** The spec is source-grounded, mathematically correct, properly scoped to backend mapping (not implementation), and routes ambiguity to the appropriate decision card. One advisory: the referenced decision card does not yet exist; this is normal for a spec at `needs-agent-review` status and becomes actionable when the decision card is created.
