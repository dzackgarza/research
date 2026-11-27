---
id: SPEC-HISTORICAL-COXETER-FUNDAMENTAL-DOMAIN-OUTPUT
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT]]'
title: Recover Coxeter diagram and fundamental chamber output contracts
status: complete
priority: medium
requirement: Vinberg/Coxeter recovery must specify exact output objects for reflection
  groups, Coxeter diagrams, chamber inequalities, and finite-volume evidence.
acceptanceCriteria:
- Simple roots, reflection morphisms, Coxeter matrix or diagram, Gram data, and chamber
  inequalities are separate typed outputs with shared provenance.
- Fundamental chamber claims include verification that the reported inequalities define
  the chamber for the generated reflection group under stated hypotheses.
- Finite-volume or parabolic-subdiagram claims are exact combinatorial or polyhedral
  checks, not diagram eyeballing.
- Outputs are reusable by downstream Coble Coxeter and cusp-classification features.
complexity: 80
tags:
- FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY
---
# Recover Coxeter diagram and fundamental chamber output contracts

## Source Provenance

- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md`:
  status flag records whether found roots form a finite-volume diagram, while `das`
  is an internal Coxeter-diagram continuation object.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/quad_forms.jl`
  and `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/vinbergs_algo.jl`:
  Gram coefficients, Coxeter coefficients, diagram extension, finite-volume check, and
  sanity checks for roots, acute angles, chamber side, and distance ordering.
- `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/infinite_order_symmetry.jl`:
  graph automorphism work uses root Gram colors, not an unweighted graph alone.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/README.md`
  and `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/vinal.py`:
  CoxIter route, dual-cone/polycone route, finite and ideal vertex extraction, and
  root printing.
- `src.bak/backends/external/vinbergs_algorithm/references/vinal/docs/vin-alg-pseudocode-old.txt`:
  fundamental polyhedron and fundamental cone narrative.
- `src.bak/backends/external/vinbergs_algorithm/references/AlVin/mainpage.dox`:
  AlVin outputs root vectors, CoxIter graph files, finite-volume/invariant data, and
  explicit nontermination/nonreflectivity distinction.
- `src.bak/backends/external/vinbergs_algorithm/references/sterk-peters_symmetric-quadratic-forms.md`
- `theory/foundations/reflective-two-elementary-lattices.md`: Coxeter diagram,
  parabolic diagram, Lanner subgraph, fundamental polyhedron, root, reflection, and
  reflection-group definitions; Sterk-Peters example records maximal parabolic
  subdiagrams and dashed-edge finite-volume checks.
- `.agents/memories/theory-graph-monodromy-hodge-methods.md`: Coxeter diagrams with
  labels and edge multiplicities require colored graph automorphism.
- `plans/features/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION.md`
- `plans/features/FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY/specs/SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT.md`

## Contract

The recovered output surface must separate the mathematical objects involved:
simple roots are lattice elements, reflections are automorphisms of the lattice,
the Coxeter diagram records pairwise reflection data, and the chamber is a polyhedral
object or inequality system in the appropriate hyperbolic cone.

Downstream code must be able to ask for parabolic subdiagrams, finite-volume status,
incidence data, or chamber faces without reconstructing the meaning of a raw root list.

## Output Objects

The output of a complete Vinberg chamber computation is not a graph. It is a linked
collection of exact mathematical objects with shared provenance:

- `simple_roots`: ordered lattice elements from the parent lattice `L`;
- `reflections`: the corresponding elements of `L.Aut()`;
- `root_gram_matrix`: the exact matrix `b(r_i, r_j)`;
- `coxeter_matrix`: pairwise Coxeter exponents or infinity/dashed-edge markers derived
  from the root Gram data under the stated sign convention;
- `coxeter_diagram`: a colored, labeled graph whose vertex colors include root norm or
  root type when relevant and whose edge labels distinguish no edge, finite Coxeter
  angle, affine/tangent, and disjoint/skew hyperplanes;
- `chamber_inequalities`: inequalities such as `b(x, r_i) >= 0` or the chosen equivalent
  convention, with the cone component and sign convention recorded;
- `chamber`: a typed hyperbolic/polyhedral chamber object or an exact inequality system
  tied to the parent lattice and cone;
- `faces`: facet objects linked to roots and reflections;
- `vertices`: finite and ideal vertices when a backend computes them, with ideal
  vertices represented as isotropic lines or sublattices, not loose coordinate rows;
- `finite_volume_certificate`: the exact check or backend certificate supporting
  finite volume;
- `parabolic_subdiagrams`: typed subdiagram data with affine type, rank, connected
  components, and inclusion/maximality data;
- `lanner_subdiagrams`: Lanner obstruction data when used by the termination criterion;
- `symmetry_group`: diagram symmetries only after preserving vertex and edge colors,
  root Gram data, and the map back to lattice isometries.

Partial Vinberg searches may return the same shape with `completeness_status =
partial-prefix` or `shell-complete`, but the chamber and finite-volume certificate must
then be absent or explicitly marked unavailable. A partial prefix can be a fixture,
debug artifact, or continuation state; it is not a fundamental domain.

Docstrings for these surfaces must mention the global diagnostic flag for surprise
logging. When enabled, the implementation should warn if a diagram is returned without
a chamber certificate, if finite-volume status is unknown, if graph symmetries are being
computed on colored data rather than an unweighted graph, if a partial prefix is
returned, or if ideal vertices are represented through isotropic subobjects rather than
ordinary finite vertices.

## Verification Contract

A chamber-complete result must verify the following obligations:

- every simple root satisfies the sourced root predicate for `L`;
- every reflection is admitted through `L.Aut()`;
- pairwise root inner products satisfy the simple-root acute-angle convention used by
  the chamber side;
- each chamber inequality is oriented so the control vector lies on the chosen side;
- the root ordering is compatible with the Vinberg distance/shell data supplied by the
  algorithm contract;
- the inequalities define the claimed chamber for the generated reflection group under
  the backend theorem or certificate;
- finite-volume claims are backed by CoxIter, Vinberg's Lanner/parabolic criterion, an
  exact polyhedral check, or a named backend certificate;
- nonreflective or nonterminating outputs are distinguished from "not enough roots were
  computed".

For the Sterk-Peters rank-19 example, fixture extraction should preserve the sourced
root list, distance levels, dashed-edge data, maximal parabolic subdiagram types, the
rank-2 hyperbolic span condition for dashed-line vertices, and the negative-definite
complement check. These are expected fixture obligations, not generic defaults for all
hyperbolic lattices.

## Downstream Reuse

The Coble Coxeter/parabolic-classification feature should consume the typed Coxeter
output directly. It should not parse pictures, free-text labels, or backend output
files. In particular:

- cusp and boundary classifications consume ideal vertices as isotropic line or plane
  subobjects;
- parabolic classification consumes typed affine subdiagrams and inclusion data;
- graph-monodromy or symmetry steps consume colored Coxeter diagrams and the induced
  lattice isometries;
- fixture data records exact source paths, theorem hypotheses, root norms,
  inner-products, and diagram conventions.

## Non-Preservation Boundaries

- Do not store Coxeter data only as a drawn graph or list of labels.
- Do not treat a Gram matrix of roots as the whole chamber object.
- Do not conflate a root enumeration prefix with a verified fundamental domain.
- Do not make Coble-specific parabolic classification depend on unsourced diagram
  conventions.
- Do not compute diagram symmetries from an unweighted graph when vertex/edge colors,
  root norms, or dashed/affine labels carry mathematical data.
- Do not collapse finite vertices, ideal vertices, isotropic lines, and isotropic planes
  into one coordinate-list output.
- Do not treat AlVin or CoxIter graph files as public API; they are backend artifacts to
  parse into typed objects if the bridge is admitted.
- Do not use a finite-volume status flag without retaining the certificate source and
  hypotheses that make the flag meaningful.

## Acceptance Criteria

- [x] Simple roots, reflections, diagrams, and chambers are distinct linked outputs.
- [x] Finite-volume and parabolic claims have exact checks.
- [x] The output can feed downstream Coble Coxeter/parabolic feature specs.
- [x] Known reference examples can be represented as fixtures with sourced expected
  structure.

## 6-Gate Protocol Review Log

**Reviewer**: automated 6-gate spec review
**Date**: 2026-05-07
**Protocol**: Source grounding verification, mathematical correctness audit

### Gate 1: Source Path Existence

| Source Claimed | Exists? | Notes |
|---|---|---|
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/README.md` | NO | Entire `src.bak/` directory absent from repo. No `vinbergs_algorithm` files found anywhere. The claimed status flags (`found roots form a finite-volume diagram`, `das` Coxeter-diagram continuation object) cannot be verified at this location. Closest available source is `.agents/memories/theory/backends/vinberg-algorithm.md`, which discusses the same reference implementations (VinbergsAlgorithmNF, AlVin, vinal) but at a higher level. |
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/quad_forms.jl` | NO | Same `src.bak/` directory absent. Gram coefficients, Coxeter coefficients, diagram extension, finite-volume check, and sanity checks cannot be verified at this location. |
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/vinbergs_algo.jl` | NO | Same `src.bak/` directory absent. |
| `src.bak/backends/external/vinbergs_algorithm/references/VinbergsAlgorithmNF/src/infinite_order_symmetry.jl` | NO | Same `src.bak/` directory absent. Graph automorphism work using root Gram colors cannot be verified at this location. |
| `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/README.md` | NO | Same `src.bak/` directory absent. CoxIter route, dual-cone/polycone route cannot be verified at this location. |
| `src.bak/backends/external/vinbergs_algorithm/references/vinal/src/sage/vinal.py` | NO | Same `src.bak/` directory absent. |
| `src.bak/backends/external/vinbergs_algorithm/references/vinal/docs/vin-alg-pseudocode-old.txt` | NO | Same `src.bak/` directory absent. |
| `src.bak/backends/external/vinbergs_algorithm/references/AlVin/mainpage.dox` | NO | Same `src.bak/` directory absent. |
| `src.bak/backends/external/vinbergs_algorithm/references/sterk-peters_symmetric-quadratic-forms.md` | NO | Same `src.bak/` directory absent. No `sterk-peters` files found anywhere in repo. |
| `theory/foundations/reflective-two-elementary-lattices.md` | YES | Verified. Contains Coxeter diagram, parabolic diagram, Lanner subgraph, fundamental polyhedron, root, reflection, and reflection-group definitions; Sterk-Peters example records maximal parabolic subdiagrams and dashed-edge finite-volume checks. |
| `.agents/memories/theory-graph-monodromy-hodge-methods.md` | YES | Verified. Line 12 explicitly states: "Coxeter diagrams with root labels/edge multiplicities should use colored graph automorphism methods rather than plain unweighted graph automorphisms." |
| `plans/features/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION/FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION.md` | YES | Verified. Defines downstream Coble Coxeter/parabolic classification feature that consumes typed Coxeter output. Confirms scope: construct Coxeter diagram, enumerate maximal parabolic subdiagrams, verify B̃₇(2) uniqueness. |
| `plans/features/FEATURE-HISTORICAL-VINBERG-COXETER-RECOVERY/specs/SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT.md` | YES | Verified. Exists in same `specs/` directory. Defines the algorithm contract on which this output-contract spec depends. |

**Gate 1 Verdict**: PARTIAL FAIL — 9 of 13 source references point to nonexistent `src.bak/backends/external/vinbergs_algorithm/` paths. The other 4 are verified. The spec's mathematical claims about Vinberg/Coxeter output objects are not falsified by this gap (the output-object taxonomy is grounded in standard Vinberg theory and corroborated by the verified sources), but the provenance is not reproducible for the bulk of the referenced backend code.

### Gate 2: Source Content Match

For the 4 verified sources:

- **reflective-two-elementary-lattices.md**: Confirmed as a comprehensive theory document (1368 lines). Contains all the constructs the spec claims: Coxeter diagram definitions, parabolic diagram, Lanner subgraph, fundamental polyhedron, root/reflection/reflection-group definitions, and Sterk-Peters example with maximal parabolic subdiagrams and dashed-edge finite-volume checks. This single source covers the core mathematical definitions required by the spec.

- **theory-graph-monodromy-hodge-methods.md**: Confirmed to contain the exact claim about Coxeter diagram symmetry requiring colored graph automorphism methods (line 12). Also documents GAP GRAPE/Digraphs/bliss workflows for weighted graph automorphisms which directly support the spec's `symmetry_group` output object requirements.

- **FEATURE-COBLE-COXETER-PARABOLIC-CLASSIFICATION.md**: Confirmed as the downstream consumer. Its scope explicitly includes constructing the Coxeter diagram from computed root inner products, enumerating maximal affine Dynkin subdiagrams, and verifying uniqueness claims. The spec's output objects (typed Coxeter diagram, parabolic subdiagrams, ideal vertices as isotropic subobjects) directly address this feature's needs. The downstream feature's prohibition against hand-coding adjacency matrices and parsing rendered diagrams aligns with the spec's non-preservation boundaries.

- **SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT.md**: Confirmed as the prerequisite algorithm contract spec. This spec correctly depends on it, and the output objects here are a natural downstream surface for the algorithm contract's computational outputs.

**Gate 2 Verdict**: PASS for verified sources. The 4 existing sources accurately support the spec's claims about Coxeter output taxonomy, graph automorphism requirements, downstream consumption needs, and algorithm-contract dependency.

### Gate 3: Mathematical Correctness — Output Objects

| Output Object | Definition | Correct? | Notes |
|---|---|---|---|
| `simple_roots` | Ordered lattice elements from parent lattice `L` | YES | Standard in Vinberg theory. Roots are vectors in the lattice satisfying the root predicate. |
| `reflections` | Corresponding elements of `L.Aut()` | YES | Reflections are automorphisms of the lattice; correct to distinguish from raw root vectors. |
| `root_gram_matrix` | Exact matrix `b(r_i, r_j)` | YES | Standard Gram data; correctly noted as signed under the stated convention. |
| `coxeter_matrix` | Pairwise Coxeter exponents or infinity/dashed-edge markers | YES | Correctly derived from root Gram data under sign convention. The infinity/dashed-edge distinction for non-acute angles is mathematically sound. |
| `coxeter_diagram` | Colored, labeled graph with vertex colors (root norm/type) and edge labels (finite/affine/disjoint) | YES | Correct. Coxeter diagrams are weighted graphs; vertex/edge colors carry mathematical data (root norms, angle types). |
| `chamber_inequalities` | `b(x, r_i) >= 0` with cone component and sign convention recorded | YES | Standard chamber definition. Recording the sign convention is critical for correctness. |
| `chamber` | Typed hyperbolic/polyhedral chamber object tied to parent lattice and cone | YES | Mathematically correct abstraction. |
| `faces` | Facet objects linked to roots and reflections | YES | Standard polyhedral geometry. |
| `vertices` | Finite and ideal vertices with ideal vertices as isotropic lines or sublattices | YES | Critical distinction: ideal vertices correspond to isotropic subspaces, not ordinary points. |
| `finite_volume_certificate` | Exact check or backend certificate | YES | Correctly requires the theorem/certificate, not just a flag. |
| `parabolic_subdiagrams` | Typed subdiagram data with affine type, rank, connected components, inclusion/maximality | YES | Standard for Vinberg termination and cusp classification. |
| `lanner_subdiagrams` | Lanner obstruction data | YES | Vinberg's criterion: Lanner subdiagrams in hyperbolic signature are a standard termination condition. |
| `symmetry_group` | Diagram symmetries preserving vertex/edge colors, root Gram data, and lattice isometry map | YES | Correctly requires colored automorphism computation. |

**Gate 3 Verdict**: PASS. All output object definitions are mathematically correct and consistent with Vinberg/Coxeter theory.

### Gate 4: Mathematical Correctness — Verification Contract

| Obligation | Assessment |
|---|---|
| Every simple root satisfies the sourced root predicate for `L` | Correct. Roots must satisfy `b(r,r) < 0` and `b(r, L) ⊆ Z` (or the field-specific equivalent). |
| Every reflection is admitted through `L.Aut()` | Correct. Reflections must be genuine lattice automorphisms. |
| Pairwise root inner products satisfy simple-root acute-angle convention | Correct. Simple roots of a chamber must satisfy `b(r_i, r_j) ≤ 0` for `i ≠ j` (or the equivalent acute-angle convention under the chosen sign). |
| Each chamber inequality oriented so control vector lies on chosen side | Correct. This is the definition of the fundamental chamber. |
| Root ordering compatible with Vinberg distance/shell data | Correct. Vinberg's algorithm proceeds by distance shells from the control vector. |
| Inequalities define claimed chamber under backend theorem/certificate | Correct. The chamber claim must be verified, not assumed. |
| Finite-volume claims backed by CoxIter, Vinberg criterion, exact polyhedral check, or named backend | Correct. Multiple verification paths are appropriate; the key requirement is a named certificate. |
| Nonreflective/nonterminating distinguished from insufficient computation | Correct. This is a critical diagnostic distinction. |
| Sterk-Peters rank-19 fixture obligations | Correct. Specific fixture requirements are listed: root list, distance levels, dashed-edge data, maximal parabolic subdiagram types, rank-2 hyperbolic span condition, negative-definite complement check. |

**Gate 4 Verdict**: PASS. All verification obligations are mathematically sound and grounded in Vinberg theory.

### Gate 5: Boundary and Non-Preservation Rules

| Rule | Assessment |
|---|---|
| Do not store Coxeter data only as a drawn graph or list of labels | Sound. Graphical representations lose mathematical structure. |
| Do not treat a Gram matrix of roots as the whole chamber object | Sound. A Gram matrix is insufficient to define chamber geometry. |
| Do not conflate root enumeration prefix with verified fundamental domain | Sound. Partial computation ≠ completed chamber. |
| Do not make Coble-specific classification depend on unsourced diagram conventions | Sound. Downstream code must use typed, sourced objects. |
| Do not compute diagram symmetries from unweighted graph when colors/labels carry mathematical data | Sound. Matches the graph-monodromy memory (colored automorphism requirement). |
| Do not collapse finite/ideal vertices, isotropic lines, and isotropic planes into one coordinate list | Sound. These are mathematically distinct object types. |
| Do not treat AlVin/CoxIter graph files as public API | Sound. Backend artifacts must be parsed into typed objects. |
| Do not use finite-volume status flag without retaining certificate source and hypotheses | Sound. A flag without provenance is mathematically meaningless. |

**Gate 5 Verdict**: PASS. All boundary rules protect mathematical correctness and API hygiene.

### Gate 6: Self-Consistency and Completeness

- **Output ↔ Verification alignment**: Every output object listed has a corresponding verification obligation. The chamber, finite-volume certificate, and parabolic subdiagrams are all subject to explicit verification rules.
- **Completeness status orthogonality**: The spec correctly distinguishes partial (`partial-prefix`, `shell-complete`) from complete results. Partial outputs must explicitly mark chamber and finite-volume certificate as absent or unavailable. This is self-consistent.
- **Downstream consumption**: The Coble Coxeter feature spec confirms that it needs exactly the typed outputs defined here: ideal vertices as isotropic subobjects for cusp classification, typed affine subdiagrams for parabolic classification, and colored Coxeter diagrams for symmetry/monodromy steps. No circular dependencies detected.
- **DependsOn correctness**: The spec correctly depends on `SPEC-HISTORICAL-VINBERG-ALGORITHM-CONTRACT`, which defines the upstream algorithm. This output-contract spec is the natural downstream surface.
- **Fixture obligations**: The Sterk-Peters rank-19 fixture requirements are concrete and verifiable, not generic defaults. This is an appropriate level of specificity.
- **Acceptance criteria**: All 4 criteria (distinct linked outputs, exact finite-volume/parabolic checks, downstream feed capability, fixture representation) are verifiable and internally consistent with the body text.
- **Diagnostic flag**: The requirement for docstrings to mention the global diagnostic flag for surprise logging, with explicit warning conditions, adds operational safety without complicating the mathematical contract.

**Gate 6 Verdict**: PASS.

### Overall Assessment

| Gate | Status |
|---|---|
| Gate 1: Source Path Existence | PARTIAL FAIL (9/13 paths broken) |
| Gate 2: Source Content Match | PASS (verified sources match) |
| Gate 3: Output Object Correctness | PASS |
| Gate 4: Verification Contract Correctness | PASS |
| Gate 5: Boundary Rules | PASS |
| Gate 6: Self-Consistency | PASS |

**Summary**: The spec is mathematically correct, internally consistent, and its output-object taxonomy is well-aligned with standard Vinberg/Coxeter theory. The downstream Coble Coxeter/parabolic-classification feature's needs are cleanly addressed. The sole deficiency is the citation of 9 `src.bak/backends/external/vinbergs_algorithm/` paths that no longer exist in the repository. These paths appear to reference a historical snapshot of reference implementations (VinbergsAlgorithmNF, vinal, AlVin) that has since been removed or reorganized. The same reference implementations are discussed in `.agents/memories/theory/backends/vinberg-algorithm.md`, which could serve as an alternative source citation. The spec's mathematical content is not invalidated by this gap (the output-object concepts are standard in Vinberg theory and are corroborated by `theory/foundations/reflective-two-elementary-lattices.md`), but the provenance section should be updated to reference currently existing files.

**Recommendation**: Update the Source Provenance section to either (a) remove the `src.bak/` references and rely on the verified sources, (b) replace them with `.agents/memories/theory/backends/vinberg-algorithm.md` as the canonical reference for the backend implementations, or (c) restore the missing `src.bak/` directory if the historical code snapshot is needed for implementation fidelity.
