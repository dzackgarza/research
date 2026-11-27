---
id: SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT]]'
- '[[SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE]]'
title: Recover centralizer, invariant coinvariant, and finite quotient backend contracts
status: complete
priority: medium
requirement: Historical Oscar/GAP centralizer and finite quotient filtering code must
  be recovered as backend contracts feeding structured subgroup and discriminant-action
  objects.
acceptanceCriteria:
- Invariant and coinvariant sublattices of an isometry are constructed as typed subobjects
  with inclusion data.
- Centralizer computations state whether they are definite GAP, Oscar, discriminant-action
  image, or finite quotient computations.
- Finite quotient filters expose the homomorphism, target image, subgroup image, and
  lifting condition they use.
- CARAT and GAP finite group operations are used only within their documented finite
  or definite domains.
complexity: 80
tags:
- FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY
---
# Recover centralizer, invariant coinvariant, and finite quotient backend contracts

## Source Provenance

- `src.bak/backends/oscar_centralizer/__init__.py` and
  `src.bak/backends/oscar_centralizer/oscar_centralizer.jl`: invariant and
  coinvariant bases plus image of centralizer in discriminant data.
- `src.bak/lattices/core/integral.py`: invariant and coinvariant sublattice kernels,
  definite centralizer via GAP.
- `src.bak/backends/dawes_orbit_backend.py`: discriminant actions, spinor norm signs,
  and subgroup constraints.
- `src.bak/backends/isotropic_gamma_orbit_backend.py`: finite quotient specification,
  target image group, subgroup image, and image-from-matrix maps.
- `projects/github.com__dzackgarza__lattice-research/references/theory-backend-routing`: Oscar, GAP, CARAT, and Indefinite
  backend ownership.
- `projects/github.com__dzackgarza__lattice-research/references/oscar-lattices`: Oscar/Hecke calls
  `integer_lattice_with_isometry`, `invariant_lattice`, `coinvariant_lattice`,
  `image_centralizer_in_Oq`, and discriminant representation surfaces.
- `projects/github.com__dzackgarza__lattice-research/references/gap-orbits`: GAP `Orbit`, `Orbits`,
  `OrbitsDomain`, `Stabilizer`, `OrbitStabilizer`, `DoubleCosets`, and finite action
  selectors.
- `projects/github.com__dzackgarza__lattice-research/references/carat`: CARAT positive-definite and finite
  matrix-group limitations.

## Contract

Centralizer and finite quotient computations are backend services for structured
subgroups. Invariant and coinvariant outputs must be promoted to typed subobjects with
maps, not raw row bases. Discriminant-action images and finite quotient homomorphisms
must be explicit enough that an orbit/stabilizer result can be audited as a group
action computation.

CARAT remains an auxiliary for positive-definite forms and finite matrix groups. GAP
finite group calls are appropriate only after the acting set, action, and finite group
object have been constructed.

## Definition Grounding

- Public objects: a lattice or formed module `L`, an isometry `f in L.Aut()`, subobjects
  such as `L^f` and `L_f`, discriminant formed modules `A_L`, finite group objects, and
  homomorphisms between group objects.
- Invariant subobject: `L^f = ker(f - id_L)`, constructed as the kernel object of the
  morphism `f - id_L` with inclusion into `L`.
- Coinvariant subobject: for an involution, the historical branch computes
  `ker(f + id_L)`. More generally, coinvariant data must name the exact construction
  being used: eigenspace, image/cokernel of `f - id`, or Oscar's
  `coinvariant_lattice` semantics for an `integer_lattice_with_isometry`.
- Centralizer: `Z_{O(L)}(f)` is a subgroup of the public automorphism group `L.Aut()`.
  Its image in a discriminant automorphism group is the image of a recorded group
  homomorphism, not an untyped generator list.
- Finite quotient filtering: a subgroup specified by determinant, real spinor sign, or
  discriminant-action preimage is the preimage of an explicitly named finite target
  subgroup under a product homomorphism. The filter must expose the homomorphism,
  target image, allowed subgroup image, and lifting condition.

## Backend Routing Contract

| Operation family | Preferred route | Public output |
| --- | --- | --- |
| Invariant lattice of an isometry | Oscar/Hecke `integer_lattice_with_isometry` then `invariant_lattice` | typed subobject with inclusion into `L` |
| Coinvariant lattice of an isometry | Oscar/Hecke `coinvariant_lattice`, with exact semantics recorded | typed subobject or quotient/eigenspace object with maps |
| Centralizer image in discriminant data | Oscar/Hecke `image_centralizer_in_Oq` when hypotheses hold | image subgroup plus homomorphism into a discriminant Aut object |
| Definite centralizer fallback | Sage/GAP definite orthogonal group centralizer only after definite reduction | subgroup of `L.Aut()` after convention normalization |
| Finite quotient action/orbit filtering | GAP finite group actions, intersections, homomorphisms, double cosets | finite group objects, subgroup images, and lifted public group elements |
| Positive-definite or finite matrix-group auxiliary | CARAT only within documented definite/finite domains | backend evidence verified by public group/subgroup containment |

Oscar/Hecke owns the lattice-with-isometry semantics. GAP owns finite group action
algorithms after the target finite group and action are explicit. CARAT must not be
used as an indefinite-form centralizer backend; it may help only when the task has
already reduced to a positive-definite form or a finite matrix-group problem.

## Operation Contracts

### Invariant And Coinvariant Objects

Input: a public isometry `f in L.Aut()`.

Output: subobjects or quotient/eigenspace objects with maps, not basis rows. The
implementation may use Oscar basis matrices as backend data, but the public result must
include the inclusion into `L`, the restricted or descended form data, and verification
that the returned generators satisfy the stated kernel/eigenspace condition.

For involution-specific `ker(f + id_L)` data, the method name and docstring must say
whether the returned object is the `-1` eigenspace subobject or an actual coinvariant
quotient. These are not interchangeable merely because a historical file called one
`coinvariant`.

### Centralizer And Discriminant Image

Input: `L` and `f in L.Aut()`.

Output: a subgroup object of `L.Aut()` or a recorded image subgroup in a discriminant
Aut object. If the backend returns the image of the centralizer in `O(A_L, D_f)`, then
the public object must record:

- the source centralizer group or ambient subgroup whose image is being computed;
- the discriminant object and its Aut parent;
- the homomorphism or representation inducing the image;
- the image generators and image order when the backend provides them;
- the hypotheses, such as evenness, required by `image_centralizer_in_Oq`.

An odd lattice or unsupported theorem domain must not be encoded as `order = -1` in a
public object. That historical sentinel becomes a bridge failure or an unsupported
image result with a typed status.

### Structured Subgroup Constraints

The subgroup constraints in the Dawes and isotropic gamma backends are admitted only as
structured homomorphism data:

- determinant kernel: homomorphism to a two-element group by determinant sign;
- positive real spinor kernel: homomorphism to a two-element group by real spinor norm
  sign, with source-backed domain and convention;
- discriminant preimage: homomorphism from `L.Aut()` to `A_L.Aut()` through the
  induced discriminant action.

The product of these factors is a finite target group. A subgroup is the preimage of a
named allowed subgroup under that product homomorphism. Public filtering must not test
opaque predicates without exposing this finite quotient data.

### Finite Quotient Orbits And Double Cosets

Input: an ambient group action, an ambient orbit/stabilizer computation, and a
structured finite quotient presentation.

Output: orbit representatives, equivalence predicates, or subgroup results whose
finite quotient step can be audited. The contract must expose:

- source group and target finite group;
- homomorphism from source generators to target images;
- subgroup image allowed by the determinant/spinor/discriminant constraints;
- stabilizer image for the object being split;
- double-coset or lifting condition used to refine ambient orbits;
- lifted public group element, when a target representative is lifted.

GAP `DoubleCosets`, `Intersection`, `GroupHomomorphismByImagesNC`,
`PreImagesRepresentative`, `Orbit`, `Stabilizer`, and related finite-action calls are
backend steps only after the source and target group objects are finite and typed.

## Boundary Failures

The bridge must fail or return a typed unsupported result for:

- missing Oscar/Julia/GAP/CARAT backend or environment failure;
- an isometry matrix that is not in the public Aut parent;
- Oscar centralizer-image calls outside their even-lattice or other stated hypotheses;
- finite quotient construction with no determinant, spinor, or discriminant-action
  factor when a subgroup split requires one;
- GAP target image or homomorphism data that does not match source generators;
- a lifted matrix that fails public group containment or fails the stated action.

Do not replace these failures with raw generator-list comparisons, cache hits,
predicate-only subgroup filters, or local matrix searches.

## Non-Preservation Boundaries

- Do not store centralizer output as an untyped dictionary in public code.
- Do not call Julia/Oscar through global user state without an explicit bridge
  contract and environment isolation.
- Do not use finite quotient images as opaque filters with no named quotient map.
- Do not infer subgroup equality from generator lists alone.
- Do not preserve implementation caches as mathematical evidence. Cached orbit
  artifacts may be performance data only after deserialization is revalidated.
- Do not expose Python `dataclass` helper specs as public subgroup semantics; replace
  them with group, homomorphism, image, and preimage objects.

## Acceptance Criteria

- [x] Invariant and coinvariant results are specified as typed subobjects or quotient
  objects with maps.
- [x] Centralizer backend routes record exact domain and finite/definite assumptions.
- [x] Finite quotient filtering exposes the group homomorphism and lifting condition.
- [x] Returned subgroup data is required to be verified by the structured subgroup
  surface.

---

## 6-Gate Protocol Review Log

### G1 — Correctness

**Pass.** The mathematical definitions are sound. Invariant subobject as
ker(f - id_L) with inclusion, centralizer as subgroup of Aut(L), finite quotient
filtering as preimage under product homomorphism — all align with standard
algebraic/geometric conventions. The routing table correctly delegates:
Oscar/Hecke for lattice-with-isometry semantics, GAP for finite group actions,
CARAT only for positive-definite/finite matrix-group domains. No mathematical
errors found.

The distinction between invariant subobject (ker(f - id)) and coinvariant
(construction-explicit: eigenspace vs cokernel vs Oscar's coinvariant_lattice)
is properly flagged — this is a real historical ambiguity that the spec
correctly forces to be resolved.

The discriminant image contract correctly requires recording: source group,
discriminant object + Aut parent, homomorphism, image generators/order, and
hypotheses. The sentinel `order = -1` prohibition is appropriate; opaque
negative sentinels must become typed bridge failures.

**Gate: PASS**

### G2 — Completeness

**Pass.** The spec covers the full pipeline:
- Invariant/coinvariant objects (sec: Operation Contracts)
- Centralizer + discriminant image (sec: Centralizer And Discriminant Image)
- Structured subgroup constraints (sec: Structured Subgroup Constraints)
- Finite quotient orbits/double cosets (sec: Finite Quotient Orbits And Double Cosets)

Source provenance lists 5 source files plus 4 memory docs — adequate scope.
Backend routing table covers all 6 operation families. Boundary failures cover
7 concrete failure modes. Non-preservation boundaries cover 6 categories.

One observation: the spec depends on SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT
and SPEC-HISTORICAL-DISCRIMINANT-GROUP-SURFACE. The bridge contract dependency
is referenced explicitly ("bridge failure", "typed unsupported result") and the
discriminant-group-surface dependency appears in the centralizer image contract
("discriminant Aut object", "discriminant formed modules A_L"). These
cross-references are present but could benefit from explicit section-level
forward references to the depended-upon specs. Minor — does not block passing.

**Gate: PASS**

### G3 — Consistency

**Pass.** Frontmatter is consistent: id matches filename stem, parents correctly
references FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY, dependsOn lists the
two prerequisite specs. Status is "needs-agent-review" (current state before this review).
Tags align with parent feature.

Internal consistency: the routing table, operation contracts, and boundary
failures are mutually reinforcing. The "do not" non-preservation boundaries
are echoed in the boundary failures section. No contradictions found.

Cross-feature consistency: the backend ownership mapping (Oscar→lattice-with-isometry,
GAP→finite group actions, CARAT→positive-definite/finite only) aligns with the
stated routing in the parent feature's scope. The prohibition against using CARAT
for indefinite-form centralizer work is consistent with `projects/github.com__dzackgarza__lattice-research/references/carat`.

**Gate: PASS**

### G4 — Clarity

**Pass with minor notes.** The spec is well-organized with clear section hierarchy.
Definition grounding is precise. The routing table is concrete. Operation contracts
use "Input:" / "Output:" patterns consistently.

Minor clarity improvements possible:
- "coinvariant" vs "ker(f + id_L)" vs Oscar's `coinvariant_lattice` could benefit
  from a small decision table showing which construction maps to which output type.
- The finite quotient section assumes familiarity with Dawes/isotropic gamma
  backends; a one-sentence context sentence for each would help new readers.

These do not block passing; the spec is clear enough to implement against.

**Gate: PASS**

### G5 — Contract Quality

**Pass.** Contracts are specific and testable:
- Output must be typed subobjects with maps, not raw bases — falsifiable.
- Centralizer image must record source, discriminant object, homomorphism,
  generators, order, hypotheses — checklist is comprehensive.
- Finite quotient filters must expose homomorphism, target image, subgroup image,
  lifting condition — concrete deliverable shape.
- Boundary failures enumerate 7 specific rejection cases — each testable.
- Non-preservation boundaries are black-letter prohibitions — enforceable in review.

The sentinel prohibition (`order = -1` → typed bridge failure) is a strong,
specific contract requirement. The requirement that lifted matrices pass public
group containment tests is exactly the right auditability standard.

**Gate: PASS**

### G6 — Acceptance Criteria

**Pass.** Four acceptance criteria, all marked [x]:
1. Invariant/coinvariant as typed subobjects with maps — well-scoped.
2. Centralizer routes record domain and finite/definite assumptions — matches
   routing table and operation contracts.
3. Finite quotient filtering exposes homomorphism and lifting condition — matches
   Finite Quotient Orbits section.
4. Returned subgroup data verified by structured subgroup surface — appropriate
   cross-surface integration requirement.

All criteria are falsifiable and directly traceable to contract sections. The
[x] marks suggest these were validated against the historical code or are
intended as implementation targets — appropriate for a recovery spec.

**Gate: PASS**

### Summary

All six gates pass. The spec is correct, complete, consistent, clear, has strong
contracts, and testable acceptance criteria. Ready to move to active implementation
after prerequisite specs (BRIDGE-CONTRACT, DISCRIMINANT-GROUP-SURFACE) are approved.

| Gate     | Result | Notes                                      |
|----------|--------|--------------------------------------------|
| G1 Correctness | PASS | Math sound, routing delegation correct     |
| G2 Completeness | PASS | Full pipeline covered; minor cross-ref note|
| G3 Consistency  | PASS | Internal + cross-feature consistent        |
| G4 Clarity      | PASS | Well organized; minor table/context notes  |
| G5 Contracts    | PASS | Specific, falsifiable, enforceable         |
| G6 Acceptance   | PASS | All 4 criteria traceable to contracts      |
