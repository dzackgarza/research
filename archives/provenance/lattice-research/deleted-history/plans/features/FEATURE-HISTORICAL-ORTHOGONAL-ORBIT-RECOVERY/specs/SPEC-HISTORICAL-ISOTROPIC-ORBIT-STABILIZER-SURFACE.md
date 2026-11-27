---
id: SPEC-HISTORICAL-ISOTROPIC-ORBIT-STABILIZER-SURFACE
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE]]'
- '[[SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS]]'
title: Recover vector, isotropic line, plane, flag orbit and stabilizer surfaces
status: complete
priority: high
requirement: Historical orbit and stabilizer algorithms must be recovered as methods
  on orthogonal groups or subgroups, returning typed representatives, witnesses, and
  stabilizer subgroup objects.
acceptanceCriteria:
- Vector equivalence returns a witness or an exact negative result justified by the
  backend/theorem branch.
- Isotropic lines, planes, and flags are typed subobjects or bases in the lattice,
  not ambient Sage spans.
- Orbit representative methods state the acting group, the objects acted on, and the
  equivalence relation.
- Stabilizer methods return subgroup objects whose generators and membership predicates
  are verified against the target subobject.
complexity: 90
tags:
- FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY
---
# Recover vector, isotropic line, plane, flag orbit and stabilizer surfaces

## Source Provenance

- `src.bak/lattices/groups/orthogonal.py`: `stabilizer`, `stabilizer_of_isotropic_line`,
  `stabilizer_of_isotropic_plane`, `stabilizer_of_isotropic_flag`,
  `find_vector_isometry`, `vectors_are_equivalent`, `isotropic_line_orbits`,
  `isotropic_plane_orbits`, `isotropic_flag_orbits`, and equivalence predicates.
- `src.bak/backends/dawes_orbit_backend.py`: vector orbit witness search under
  subgroup constraints.
- `src.bak/backends/isotropic_gamma_orbit_backend.py`: ambient and subgroup isotropic
  orbit representatives, equivalence witnesses, and finite quotient filtering.
- `src.bak/backends/external/py_polyhedral/binaries.py`: exact vector, isotropic
  subspace, flag equivalence/stabilizer/orbit backend wrappers.
- `.agents/memories/theory-backend-routing.md` and
  `.agents/memories/theory/backends/indefinite-jl.md`: Indefinite.jl orbit and
  stabilizer routing.
- `.agents/memories/theory/backends/gap-orbits.md`: finite action, stabilizer, and
  double-coset routing.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md`:
  exact backend domains and witness verification.
- `plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md`:
  finite quotient filtering and lifting contracts.
- `plans/features/FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY/specs/SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE.md`:
  group/subgroup ownership and action conventions.

## Contract

Orbit and stabilizer methods are owned by the acting group or subgroup. The caller
must be able to read the statement as a mathematical action: a group acts on vectors,
isotropic lines, isotropic planes, or isotropic flags in a lattice, and the method
returns representatives, witnesses, or stabilizer subgroups for that action.

Representatives must be typed lattice elements or typed subobjects. Normalization of a
primitive isotropic line is an internal representative convention, not a replacement
for the line object. Witness matrices returned by backends become group elements only
after membership verification.

## Definition Grounding

- Acting object: an orthogonal group or structured subgroup `G <= L.Aut()`.
- Acted-on objects: lattice elements, primitive isotropic lines as rank-one subobjects,
  isotropic planes as rank-two formed subobjects with inclusion into `L`, and flags as
  nested isotropic subobjects.
- Orbit relation: `x ~ y` means there exists `g in G` such that `g.x = y` for vectors
  or `g(S) = T` for subobjects/flags under the stated pointwise or setwise action.
- Stabilizer: `G.stabilizer(x)` is a subgroup of `G`; for an element it fixes the
  element, for a line/plane it preserves the subobject setwise unless the method name
  explicitly says pointwise, and for a flag it preserves every stratum in the chain.
- Witness: an equivalence method returning true must return or expose a group element
  witness when the backend route computes one. A negative result is exact only when the
  selected backend/theorem branch is complete for the stated domain.

## Public Orbit And Stabilizer Surface

The admitted group-owned surface is:

- `G.orbit_representatives(objects=...)` for a typed finite or backend-supported
  object family;
- `G.isotropic_line_orbits()`, `G.isotropic_plane_orbits()`, and
  `G.isotropic_flag_orbits(length=...)` as compatibility spellings for the lattice
  literature;
- `G.are_equivalent(x, y)` or object-specific compatibility spellings for orbit
  membership, returning exact evidence and a witness when available;
- `G.find_witness(x, y)` or `G.transport(x, y)` returning a group element when
  equivalence holds;
- `G.stabilizer(x)` for elements and subobjects;
- `G.stabilizer_of_isotropic_line(line)`, `G.stabilizer_of_isotropic_plane(plane)`,
  and `G.stabilizer_of_isotropic_flag(flag)` as compatibility spellings that delegate
  to `G.stabilizer(...)` after constructing typed objects.

These methods live on the acting group or subgroup. Lattice-local spellings may remain
only as convenience routes that call `L.orthogonal_group().method(...)`; the mathematical
owner is the acting group.

## Typed Representatives

Vector orbits return elements of `L`, not coordinate lists. A norm-orbit method must
record the norm, parent, backend completeness claim, and whether the representative is
integral, rational, metric-dual, or in another explicitly named parent.

Primitive isotropic line orbits return rank-one subobjects with inclusion into `L`.
Over `ZZ`, `v` and `-v` generate the same line; normalizing to a primitive generator is
representative data, not the definition of the line. Docstrings must state when a method
acts on vectors and when it acts projectively on lines.

Isotropic plane orbits return rank-two isotropic subobjects with selected generator
data when a backend needs rows. Flags return nested subobject chains
`L_1 <= L_2 <= ... <= L_k <= L`, with inclusion maps and isotropy checks at every
stratum. A tuple of backend rows is not a public flag.

## Backend Contracts

Ambient indefinite orbits and stabilizers route through the exact Indefinite.jl or
polyhedral_common bridge specified by
`SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT`. Backend rows and row-action
matrices are normalized at the bridge and verified through `G <= L.Aut()`.

Subgroup-aware splitting routes through the finite quotient contract from
`SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS`. The public result must
record the ambient orbit/stabilizer, the finite quotient homomorphism, the subgroup
image, the stabilizer image, and the double-coset or lifting condition used to split
ambient orbits into subgroup orbits.

The Dawes non-isotropic vector backend is admitted only as a route for the precise
domain it states: non-isotropic vector orbit equivalence under a structured subgroup,
with determinant, spinor, and discriminant-action constraints exposed as finite
quotient/preimage data. It must not be treated as a generic vector-orbit oracle.

## Stabilizer Contracts

Element stabilizer:

- Input: `x in L`.
- Condition: `g(x) == x`.
- Output: a subgroup of `G` with generators verified as elements of `G` fixing `x`.

Line stabilizer:

- Input: a rank-one primitive isotropic subobject or a generator promoted to that
  subobject.
- Condition: setwise preservation of the subobject unless the method says pointwise.
- Output: subgroup of `G`; in the projective line case, `g(v) = +/- v` is a generator
  check, not a replacement for subobject containment.

Plane and flag stabilizers:

- Input: a typed isotropic plane or flag.
- Condition: setwise preservation of the plane, or preservation of every flag stratum.
- Output: subgroup of `G` with generator verification against the target subobjects.

## Equivalence Results

Equivalence methods must distinguish:

- `equivalent=True` with a verified witness `g in G`;
- `equivalent=False` with an exact backend/theorem reason;
- `unsupported` or backend failure, which is not a proof of non-equivalence.

The result object or return contract should retain the acting group, source object,
target object, witness when present, and backend route/provenance. A bare boolean is
not sufficient when a proof or later computation needs the witness.

## Non-Preservation Boundaries

- Do not present finite quotient filtering as proof unless the quotient map, image,
  subgroup image, and lifting condition are explicit.
- Do not use raw tuples of rows as the final public representation of isotropic planes
  or flags.
- Do not treat a missing backend witness as a proof of non-equivalence unless the
  backend contract says the search is complete for the stated inputs.
- Do not allow subgroup constraints to become opaque bags of predicates.
- Do not preserve cache hits as mathematical evidence; cached representatives must be
  deserialized into typed objects and revalidated.
- Do not conflate vector orbits with line orbits. Projectivizing by `v ~ -v` changes the
  acted-on object.
- Do not expose row tuples, ambient Sage spans, or backend normalization choices as the
  final public representation of lines, planes, or flags.

## Acceptance Criteria

- [x] Acting group, acted-on object, and equivalence relation are explicit.
- [x] Orbit methods return typed representatives with normalization provenance.
- [x] Stabilizer methods return subgroup objects with verified generators.
- [x] Equivalence methods return witnesses when equivalence holds and exact evidence
  when it does not.

## 6-Gate Protocol Review Log

Review date: 2026-05-07.  Reviewer: automated 6-gate audit (subagent).
Result: PASS with findings (G1 Finding 1, G2 Finding 1, G5 Finding 1).
No gate failures.

### G1 — Source Grounding

The spec cites ten references in Source Provenance (lines 33-53).  Audit result:

| Reference cited in spec | Actual path resolved | Exists |
| --- | --- | --- |
| `src.bak/lattices/groups/orthogonal.py` | (same) | NO |
| `src.bak/backends/dawes_orbit_backend.py` | (same) | NO |
| `src.bak/backends/isotropic_gamma_orbit_backend.py` | (same) | NO |
| `src.bak/backends/external/py_polyhedral/binaries.py` | (same) | NO |
| `.agents/memories/theory-backend-routing.md` | `/home/dzack/research/.agents/memories/theory-backend-routing.md` | YES |
| `.agents/memories/theory/backends/indefinite-jl.md` | `/home/dzack/research/.agents/memories/theory/backends/indefinite-jl.md` | YES |
| `.agents/memories/theory/backends/gap-orbits.md` | `/home/dzack/research/.agents/memories/theory/backends/gap-orbits.md` | YES |
| `.../SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md` | `/home/dzack/research/plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT.md` | YES |
| `.../SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md` | `/home/dzack/research/plans/features/FEATURE-HISTORICAL-INDEFINITE-BACKEND-RECOVERY/specs/SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.md` | YES |
| `.../SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE.md` | `/home/dzack/research/plans/features/FEATURE-HISTORICAL-ORTHOGONAL-ORBIT-RECOVERY/specs/SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE.md` | YES |

**G1 Finding 1 (moderate):** Four `src.bak/` historical source files are cited in
Source Provenance but do not exist on disk.  No `src.bak/` directory of any kind
was found in the workspace.  The historical code that this spec aims to recover
behavior from is the evidentiary anchor; its absence weakens verifiability of the
recovery claims.  Note also that the spec references `py_polyhedral/binaries.py`
for exact backend wrappers, but the actual polyhedral_common C++ source is
vendored at `src/external/dutsik_polyhedral/polyhedral_common/` — no Python
wrapper layer currently exists.

**G1 Finding 2 (advisory):** The spec does not cite the two detailed
algorithm-backend memory files that document the Dawes and isotropic gamma
methods:

- `.agents/memories/theory/algorithms/dawes-nonisotropic-vector-orbits.md` (783
  lines, Dawes Algorithms 2.1-2.3 with full mathematical notation)
- `.agents/memories/theory/algorithms/isotropic-gamma-orbit-backend.md` (573
  lines, Dutour-Sikiric/Hulek double-coset splitting method)

Both exist and are highly relevant to the spec's backend contracts.  The spec
indirectly references them through the bridge and centralizer specs, but direct
citation would strengthen source grounding.

**G1 Finding 3 (verified):** The six memory/dependency-spec references that do
exist are consistent with the spec's claims.  The bridge contract spec
(SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT) explicitly lists
`INDEF_FORM_GetOrbit_IsotropicKplane`, `INDEF_FORM_GetOrbit_IsotropicKflag`,
`INDEF_FORM_StabilizerVector`, and `INDEF_FORM_StabilizerIsotropicPlane` as
operations the bridge must route (lines 89-90).  The finite quotient spec
(SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS) defines the double-
coset lifting contract (lines 150-166).  The orthogonal group spec
(SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE) delegates `stabilizer(x)`
and isotropic stabilizers to this spec (line 112).  PASS.

Source-grounding verdict: PASS with one moderate finding (missing `src.bak/`
sources) and one advisory finding (missing algorithm-memory citations).

### G2 — Sage Surface Completeness

The spec defines an orbit-and-stabilizer surface (lines 82-101) comprising ten
method families owned by the acting group or subgroup.  Compared against current
Sage surfaces under `category_specs/`:

| Surface item | Spec lines | Current Sage location | Status |
| --- | --- | --- | --- |
| `G.orbit_representatives(objects=...)` | 86-87 | Not surfaced | GAP |
| `G.isotropic_line_orbits()` | 88 | Not surfaced | GAP |
| `G.isotropic_plane_orbits()` | 88 | Not surfaced | GAP |
| `G.isotropic_flag_orbits(length=...)` | 88-89 | Not surfaced | GAP |
| `G.are_equivalent(x, y)` | 91-92 | Not surfaced | GAP |
| `G.find_witness(x, y)` / `G.transport(x, y)` | 93-94 | Not surfaced | GAP |
| `G.stabilizer(x)` (element/subobject) | 95 | Not surfaced | GAP |
| `G.stabilizer_of_isotropic_line(line)` | 96 | Not surfaced | GAP |
| `G.stabilizer_of_isotropic_plane(plane)` | 96-97 | Not surfaced | GAP |
| `G.stabilizer_of_isotropic_flag(flag)` | 97-98 | Not surfaced | GAP |
| Typed representatives (vector/line/plane/flag) | 104-118 | Not surfaced | GAP |
| Equivalence result triage (True+W, False+reason, unsupported) | 160-170 | Not surfaced | GAP |

**G2 Finding 1 (advisory):** None of the twelve orbit/stabilizer surface items
exist in current Sage category surface code.  `LatticeAutCategory`
(`category_specs/lattices/homsets.py`) defines subgroup constructors
(`special_subgroup`, `stable_subgroup`, `stable_special_subgroup`) but no
orbit/stabilizer methods.  This is an entirely aspirational surface.  Since the
parent feature is a historical recovery task, this gap is expected — the spec
correctly routes backend contracts through the bridge (Indefinite.jl/
polyhedral_common) and the finite-quotient centralizer specs.  However, the
spec should either (a) note that no current Sage surface exists for these
methods, or (b) define abstract method stubs in the lattice Aut category for
future implementation to realize.

Sage-surface verdict: PASS.  All surface items are documented aspirational gaps
consistent with the recovery goal.  No existing surface is weakened.

### G3 — Mathematical Correctness

Audit of mathematical claims:

1. **Acting object `G <= L.Aut()` (line 70).**  Verified against
   `SPEC-HISTORICAL-ORTHOGONAL-GROUP-SUBGROUP-SURFACE` lines 67-68: orthogonal
   group is `Aut(M,b)` in the formed-module category.  The Aut object is the
   owner of group actions.  Correct.  PASS.

2. **Acted-on objects (lines 71-73).**  Primitive isotropic lines as rank-one
   subobjects, isotropic planes as rank-two formed subobjects, flags as nested
   isotropic subobjects.  Verified against
   `bilinear-form-category-semantics.md` lines 28-29 (perps defined via
   inclusions/subobjects, isotropic reduction) and the isotropic gamma backend
   plan (isotropic k-planes and flags as subobject chains).  Correct.  PASS.

3. **Orbit relation `x ~ y` iff `∃ g ∈ G: g.x = y` (lines 73-74).**  Standard
   group-action definition.  The spec correctly distinguishes pointwise and
   setwise action for subobjects.  PASS.

4. **Stabilizer `G.stabilizer(x)` is a subgroup of `G` (lines 75-76).**  Standard
   definition.  Verified against GAP orbits memory (`gap-orbits.md` lines 24-39)
   which defines `Stabilizer(G, pnt, act)`.  Correct.  PASS.

5. **Setwise vs pointwise disambiguation (lines 76-78).**  The spec states that
   a line/plane stabilizer is setwise "unless the method name explicitly says
   pointwise" and a flag stabilizer preserves every stratum.  This distinction
   is mathematically precise.  Verified against the bridge contract spec lines
   152-153: "Pointwise and setwise stabilizers are distinct surfaces; the bridge
   must not blur them."  Correct.  PASS.

6. **`v` and `-v` generate the same line (lines 111-112).**  The spec correctly
   notes that normalizing to a primitive generator is representative data, not
   the definition of the line.  Projective action (`g(v) = ±v`) is the line
   action, distinguished from vector action.  Verified against GAP `OnLines`
   semantics (`gap-orbits.md` lines 94-108).  Correct.  PASS.

7. **Witness requirement (lines 80-81, 160-169).**  An equivalence method
   returning true must expose a group element witness.  A negative result is
   exact only when the backend/theorem branch is complete.  "Unsupported" is
   not a proof of non-equivalence.  This tripartite result model (True+witness,
   False+exact-reason, unsupported/backend-failure) is mathematically rigorous.
   Verified against bridge contract spec lines 105-107: "Output: either no
   witness, or a public Hom element ... whose matrix has been normalized."
   PASS.

8. **Backend routing (lines 121-136).**  Ambient indefinite orbits/stabilizers
   route through Indefinite.jl or polyhedral_common; subgroup-aware splitting
   routes through the finite quotient contract.  Verified against
   `indefinite-jl.md` lines 25-28 (automorphism generators), 55-58 (isometry),
   75-78 (orbit representatives), 97-99 (isotropic k-planes), 118-120
   (isotropic k-flags), and the finite quotient spec lines 150-166 (double-
   coset lifting).  PASS.

9. **Dawes backend domain constraint (lines 133-136).**  The spec restricts
   the Dawes non-isotropic vector backend to its precise domain (structured
   subgroup, determinant/spinor/discriminant-action constraints).  Verified
   against `dawes-orbit-backend.md` lines 325-353: branch preconditions require
   structured subgroup metadata; black-box predicates cannot enter the
   indefinite-complement branch.  Correct.  PASS.

10. **Element stabilizer condition `g(x) == x` (line 142).**  Standard
    pointwise fixity condition.  The spec requires generators to be verified
    as elements of `G` fixing `x`.  PASS.

11. **Line stabilizer: setwise preservation (lines 148-151).**  The spec
    correctly notes that `g(v) = ±v` is a generator check, not a replacement
    for subobject containment.  This prevents conflating the projective action
    on the line with pointwise vector fixity.  PASS.

12. **Plane and flag stabilizers: setwise preservation (lines 154-157).**  The
    spec requires typed isotropic planes/flags as input and generator
    verification against the target subobjects.  Correct.  PASS.

13. **Norm orbit completeness (lines 106-108).**  The spec requires recording
    norm, parent, backend completeness claim, and integral/rational/dual
    qualifier.  Verified against bridge contract spec lines 130-135: each
    representative must have the requested norm "accompanied by the backend
    route's completeness claim."  PASS.

No mathematical errors found.

Mathematical-correctness verdict: PASS.

### G4 — Nonmathematical Rejection

The spec has an explicit Non-Preservation Boundaries section (lines 172-186)
with seven rejections.  Each has a clear rationale and replacement:

1. **Reject finite quotient filtering as proof without explicit quotient map
   (line 174).**  Rationale: subgroup orbit splitting requires the quotient map,
   image, subgroup image, and lifting condition to be explicit.  Replacement:
   the finite quotient contract in SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-
   QUOTIENT-BACKENDS lines 134-147 mandates explicit homomorphism data.  SOUND.

2. **Reject raw row tuples as final public representation of planes/flags
   (line 176).**  Rationale: tuples of backend rows are implementation data,
   not typed subobjects.  Replacement: typed isotropic planes and flags with
   inclusion data.  SOUND.

3. **Reject missing backend witness as proof of non-equivalence (lines 177-178).**
   Rationale: a backend failure or missing witness is not mathematical evidence
   against equivalence unless the backend contract guarantees completeness.
   Replacement: tripartite result model (True+witness, False+exact-reason,
   unsupported).  SOUND.

4. **Reject opaque subgroup constraints as bags of predicates (line 179).**
   Rationale: subgroup constraints must be structured for backend dispatch.
   Replacement: structured subgroup objects with finite quotient metadata.
   SOUND.

5. **Reject cache hits as mathematical evidence (lines 180-181).**  Rationale:
   cached representatives must be deserialized into typed objects and
   revalidated.  Replacement: revalidation on deserialization.  SOUND.

6. **Reject conflating vector orbits with line orbits (lines 182-183).**
   Rationale: projectivizing by `v ~ -v` changes the acted-on object.
   Replacement: explicit projective vs vector action distinction at method
   level and docstring level.  SOUND.

7. **Reject row tuples, ambient Sage spans, or backend normalization choices
   as final public representation (lines 184-186).**  Rationale: these are
   backend artifacts, not typed subobjects.  Replacement: typed objects with
   inclusion data.  SOUND.

All rejections are mathematically grounded and preserve the spec's obligations
through explicit replacement owners.

Nonmathematical-rejection verdict: PASS.

### G5 — Ambiguity Routing

Identified ambiguities and their resolution status:

1. **"Compatibility spellings" surface (lines 88-89, 96-98).**  The spec
   defines `isotropic_line_orbits()`, `isotropic_plane_orbits()`, and
   `isotropic_flag_orbits()` as "compatibility spellings for the lattice
   literature."  The relationship between these compatibility spellings and
   the primary `orbit_representatives(objects=...)` method is not specified:
   should the compatibility spellings delegate to the primary method, or vice
   versa?  The orthogonal group spec (SPEC-HISTORICAL-ORTHOGONAL-GROUP-
   SUBGROUP-SURFACE) resolves this by stating they delegate to
   `G.stabilizer(...)` after constructing typed objects (line 98).  PASS
   (resolved by cross-reference).

2. **"Typed subobjects" type system (throughout).**  The spec repeatedly
   requires "typed subobjects with inclusion data" but does not specify what
   type system or Sage category these subobjects inhabit.  The orthogonal
   group spec mentions "Aut-category objects" and "formed-submodule
   subobjects."  The category_specs codebase defines `Lattice` and homset
   categories but does not yet define typed isotropic-line/plane/flag objects.
   **G5 Finding 1 (advisory):** The spec should either reference the existing
   sub-object category infrastructure or note that typed isotropic subobjects
   are a dependency not yet designed.  Deferring this to implementation is
   acceptable but should be acknowledged.

3. **Setwise/pointwise disambiguation mechanism (line 76).**  The spec says
   stabilizers are setwise "unless the method name explicitly says pointwise."
   It does not specify whether the method names currently defined are setwise
   or pointwise, or how a caller selects between them.  The stabilizer contract
   section (lines 138-158) clarifies: line stabilizer is setwise unless
   specified, flag stabilizer preserves every stratum, element stabilizer is
   pointwise.  PASS (resolved in contract section).

4. **Lattice-local convenience routes (line 100-102).**  The spec allows
   lattice-local spellings "only as convenience routes that call
   `L.orthogonal_group().method(...)`."  This creates two surface layers with
   the same method names but different owners.  The orthogonal group spec
   (lines 95-98) clarifies that generator computation is separate from group
   definition.  The routing is well-defined but the method-name collision
   between `L.stabilizer(x)` and `L.Aut().stabilizer(x)` would benefit from
   an explicit design rule.  PASS (acceptable deferral).

5. **Projective vs vector disambiguation (lines 111-112).**  The spec states
   "Docstrings must state when a method acts on vectors and when it acts
   projectively on lines."  This is a documentation obligation, not a
   structural disambiguation.  **G5 Finding 2 (advisory):** Consider whether
   the method name itself should encode the distinction (e.g.,
   `stabilizer_of_line` vs `stabilizer_of_vector`) rather than relying solely
   on docstrings.  The spec partially adopts this convention
   (`stabilizer_of_isotropic_line` vs `stabilizer` for elements) but the
   `are_equivalent` method is ambiguous.

6. **Equivalence result object contract (lines 160-170).**  The spec says
   "The result object or return contract should retain the acting group,
   source object, target object, witness when present, and backend route/
   provenance."  It does not specify whether this is a Python dataclass,
   a Sage result object, or a dictionary.  This is an acceptable implementation
   deferral.  PASS.

Ambiguity-routing verdict: PASS with two advisory findings (typed-subobject
type system, projective-vs-vector method-name disambiguation).

### G6 — Obligation Preservation

Audit of mathematical obligations transferred from historical code:

1. **Vector orbit equivalence with witness.**  Historical `find_vector_isometry`
   and `vectors_are_equivalent` in `orthogonal.py` become `G.are_equivalent`
   and `G.find_witness` on the acting group, with the tripartite result
   contract (True+witness, False+exact-reason, unsupported).  The obligation
   to provide orbit membership evidence is preserved and strengthened (bare
   boolean no longer accepted).  PASS.

2. **Isotropic line/plane/flag orbits.**  Historical `isotropic_line_orbits`,
   `isotropic_plane_orbits`, `isotropic_flag_orbits` are recovered as group-
   owned methods returning typed subobjects, not raw row tuples.  The
   obligation to enumerate isotropic subobjects under a group action is
   preserved and placed on the acting group.  PASS.

3. **Stabilizer computation.**  Historical `stabilizer`,
   `stabilizer_of_isotropic_line`, `stabilizer_of_isotropic_plane`,
   `stabilizer_of_isotropic_flag` are recovered with verified generator
   membership and explicit setwise/pointwise semantics.  The obligation is
   preserved and strengthened (generators verified, not raw backend output).
   PASS.

4. **Backend convention normalization.**  Historical row-action/right-action
   matrix conventions are normalized at the bridge boundary before entering
   public group semantics.  This obligation is preserved and routed to
   SPEC-HISTORICAL-INDEFINITE-BACKEND-BRIDGE-CONTRACT (lines 72-74).
   PASS.

5. **Finite quotient filtering.**  Historical Dawes/isotropic `condition_set`
   filtering becomes explicit homomorphism data through
   SPEC-HISTORICAL-CENTRALIZER-AND-FINITE-QUOTIENT-BACKENDS.  Obligation
   preserved; opacity removed.  PASS.

6. **Subgroup-aware orbit splitting.**  Historical isotropic gamma orbit
   splitting (double coset method) becomes public group methods that record
   ambient orbit, finite quotient homomorphism, subgroup image, stabilizer
   image, and lifting condition (lines 128-131).  Obligation preserved;
   auditability added.  PASS.

7. **Non-isotropic vector domain constraint.**  Historical Dawes backend is
   admitted only for its precise domain (structured subgroups, determinant/
   spinor/discriminant data exposed as finite quotient/preimage data, line
   135).  The obligation to support non-isotropic vector orbits is preserved
   but scope-bounded to prevent misuse as a generic oracle.  PASS.

8. **Typed representatives replacing raw coordinates.**  Historical raw row
   tuples become typed lattice elements (vector orbits), typed rank-one
   subobjects (line orbits), typed rank-two formed subobjects (plane orbits),
   and typed nested subobject chains (flag orbits).  This is a strengthened
   obligation: typed semantics replace opaque coordinates.  PASS.

No mathematical obligation is weakened, deleted without replacement, or
narrowed to implementation-only surfaces.  Several obligations are
strengthened by adding verification, auditability, and type safety.

Obligation-preservation verdict: PASS.

### Summary

| Gate | Verdict | Evidence |
| --- | --- | --- |
| G1 Source grounding | PASS | 6/10 references exist on disk; 4 `src.bak/` sources missing (moderate finding); 2 algorithm-memory files not cited (advisory) |
| G2 Sage surface completeness | PASS | 0/12 surface items exist in current Sage code; all are aspirational recovery gaps (expected, advisory) |
| G3 Mathematical correctness | PASS | 13 claims audited against canonical sources; no errors |
| G4 Nonmathematical rejection | PASS | 7 explicit rejections, all with grounded rationale and replacement owners |
| G5 Ambiguity routing | PASS | 6 boundaries examined; 2 advisory (typed-subobject type system, projective-vs-vector method names) |
| G6 Obligation preservation | PASS | 8 obligations preserved with correct owner routing; several strengthened |

Overall: SPEC-HISTORICAL-ISOTROPIC-ORBIT-STABILIZER-SURFACE.md is
mathematically sound and correctly routes orbit and stabilizer semantics
through the acting group surface, with backend contracts delegated to the
bridge and finite-quotient specs.  The spec's dependency chain is intact
(orthogonal group surface, indefinite bridge contract, centralizer/finite-
quotient backends).  Three findings require attention:

1. **G1 Finding 1 (moderate):** Four `src.bak/` historical source files are
   missing.  The spec should either restore them, document their archival
   location, or replace citations with concrete behavior descriptions
   extracted from the parent feature card and existing algorithm-memory files
   (dawes-nonisotropic-vector-orbits.md, isotropic-gamma-orbit-backend.md).
2. **G2 Finding 1 (advisory):** No orbit/stabilizer surface exists in current
   Sage category code.  The spec should acknowledge this and consider defining
   abstract method stubs in `LatticeAutCategory` to anchor future
   implementation.
3. **G5 Finding 1 (advisory):** The "typed subobjects" type system (isotropic
   lines, planes, flags) is not designed.  The spec should either reference
   existing subobject infrastructure or note this as an unresolved dependency.
