---
id: SPEC-SAGE-CONSTRUCTOR-METHOD-FRONTIER
trackerStatus:
  type: spec
parents:
- '[[FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES]]'
dependsOn:
- '[[SPEC-CATEGORY-LITERAL-METHOD-OWNERSHIP-INVENTORY]]'
title: Maintain Sage constructor and method operation map
status: in-progress
priority: critical
complexity: 75
requirement: Maintain the source-backed mathematical operation map for category-spec
  scope. Each recorded row translates Sage behavior into a mathematical operation under
  hypotheses, the weakest category or refinement claimed, witness data, return object,
  and source evidence.
acceptanceCriteria:
- The file records the active scope, included category families, included Sage source
  roots, and source roots not yet inspected.
- Every mathematical row records the Sage method body/docs/examples read, the
  mathematical behavior extracted from them, the hypotheses, weakest category or
  refinement, required witnesses, return object, and source evidence.
- Rows without a mathematical operation are recorded only as nonmathematical
  implementation residue or unresolved mathematical questions.
- Progress claims cite rows whose mathematical assertion was added, corrected, rejected
  as residue, or left as an unresolved mathematical question. Row movement, row counts,
  bookkeeping labels, and handoff edits are not progress evidence.
tags:
- FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES
---
# Sage Constructor and Method Operation Map

## Mathematical Assertions Preserved

This spec preserves a source-backed record of mathematical assertions for
category-spec inventory and mapping. The mathematical objects are the operations,
constructions, categories, morphisms, hypotheses, witnesses, and codomains stated by
the rows. The map is only the document that records those propositions. A row is
complete only when it states the Sage behavior and then gives the ordinary
mathematical sentence:
for objects of category `C`, under hypotheses `H`, construction, predicate, or morphism
`m` is defined, has codomain or return object `Y`, and requires witness data or proof
obligations `W`.

```text
Sage body/docs/examples
  -> mathematical operation O on objects satisfying hypotheses H
  -> weakest category C and any refinement membership claimed
  -> witness data or proof obligations required by C
  -> codomain or return object
  -> source evidence
```

Any set-difference notation, row status, or compatibility note is a local
navigation aid only. It is not a second mathematical object and cannot be cited as
progress by itself.

The false substitute this blocks is reporting row counts, file counts, review prose,
handoff updates, broad checkpoints, compatibility cleanups, or current-state summaries
as mathematical progress.

## Control Invariant

A category-spec Sage inventory or mapping session reports mathematical progress only
when it adds, corrects, rejects, or records a source-backed mathematical assertion:

```text
method or constructor m implements operation O on objects satisfying H,
belongs to weakest category or refinement C, and requires witnesses W.
```

The first question is neither "where does Sage expose this name?" nor "which abstract
category-theory words might apply?" The first question is "what behavior do the Sage
method body, examples, and docs actually implement?" Only after that extraction may the
row introduce the mathematical vocabulary, weakest structure, hypotheses, category
membership, refinement membership, and witness requirements.

Compatibility, runtime, display, private, test-helper, package-export, and backend
plumbing methods are not part of the spec unless they change the mathematical
interface or block construction of a required spec object. Otherwise record a one-line
residue classification if useful and move on.

Mapping documents, subtree `SAGE_INVENTORY.md` files, task cards, decisions, and
handoffs remain evidence for definitions, implementations, and gaps. They are not
completion evidence unless they change the operation map itself.

## Scope

Only the constructor/factory batch below has been enumerated into this operation map.
Unknown counts outside that batch are not zero.

| Field | Value |
| --- | --- |
| Active scope | Category-spec mathematical operations, constructors, constructions, and Sage evidence rows for the supporting semantic families below. |
| Included category families | Sets, topological spaces, rings, ideals through ring/module structure, algebras, modules, Hom/End/Aut, forms, lattices, tensor algebra components, posets, and geometry-facing source rows when they block the category-spec phase. |
| Sage source roots included in this map | `sage/modules/free_quadratic_module.py` free-bilinear and field-quadratic factories; `sage/modules/free_quadratic_module_integer_symmetric.py` integral-lattice constructor cluster; `sage/modules/torsion_quadratic_module.py` torsion quadratic constructors; and the local `category_specs/lattices/__init__.py` constructor collector wrapper. |
| Source roots not yet inspected into this map | Every source root outside the recorded constructor/factory rows in this batch; no non-constructor lattice methods or other category families are populated by this edit. |

## Required Mathematical Statement

Before any Sage method, constructor, class, helper, display hook, backend method, or
package export is included in the operation map, the active scope must record what the
source code, examples, or written docs say it does. The row must state the mathematical
operation it implements, or classify it as implementation residue, out-of-scope
evidence, or an unresolved mathematical question.

The extraction step controls the row:

```text
Sage method body/docs/examples
  -> sageBehavior
  -> mathematicalOperation
  -> requiredVocabulary
  -> hypotheses
  -> weakest category/refinement
  -> witnesses/proof obligations
  -> source-backed row, residue classification, or unresolved question
```

If a Sage name has no coherent `mathematicalOperation` after semantic extraction, it is
nonmathematical implementation residue, out-of-scope evidence, or an unresolved
mathematical decision. It is not a mathematical row merely because it appears near the
subtree in Sage.

## Active Lattice Operation Map

The active worker task underneath the current process repair is
`category_specs/lattices` Sage constructor and method inventory, followed by
mathematical mapping. Its next substantive claim is a source-backed mathematical
operation map, not another handoff, memory, review note, local row edit, Sage-symbol
scrape, or a priori category primer.

### Active Lattice Extraction Questions

This is not a completion claim. It is the required extraction checklist for each Sage
method cluster before weakest-category placement.

For each method cluster, record:

- what inputs, outputs, examples, coercions, and branch cases the Sage body/docs expose
- whether the behavior is a morphism operation, object operation, constructor,
  construction route, representation/presentation datum, algorithmic invariant,
  coercion, display/runtime helper, test helper, or backend choice
- whether the behavior is functorial or depends on a chosen representative,
  presentation, side convention, basis, matrix action, backend algorithm, or display
  convention
- which vocabulary the behavior forces: category, concrete category, Hom/End/Aut,
  preadditive/additive or `R`-linear Hom structure, kernels/cokernels/images/coimages,
  finite generation, finite presentation, finite rank, basis/presentation data,
  bilinear or quadratic form, nondegeneracy, integrality, torsion, quotient
  presentation, discriminant form, or backend/algorithm choice
- what weakest structure and hypotheses make the extracted operation meaningful

The BinaryQF and FreeModuleMorphism cases are the diagnostic examples for the workflow.
A compressed Sage row must split when source behavior splits. Evaluation of a binary
quadratic form at a two-coordinate input, coefficientwise additive operations, Gauss
composition, and left/right matrix actions are different mathematical operations.
Likewise, categorical morphism composition/evaluation, additive or exact Hom behavior,
finite-free matrix representation, side-dependent matrix conventions, and
endomorphism-specific spectral algebra cannot be collapsed into one free-module
category label.

After semantic extraction, the lattice operation map must cover the relevant Sage
category providers, constructors/factories, classes reached through those constructors,
parent and element methods, construction routes, Hom objects, End objects, Aut groups,
and source constructors, methods, and classes already recorded by the lattice evidence
files. Each row must be one of:

- a source-backed mathematical assertion;
- nonmathematical implementation residue;
- an unresolved mathematical question;
- out-of-scope evidence.

The word "touches" is not a scope rule. A Sage constructor, method, or class enters the
mathematical operation map only when it is implementation evidence for a mathematical
operation, constructor/construction route, codomain-owned construction, or unresolved
mathematical question needed by the
lattice/category foundation. Package imports, random/test helpers, display hooks,
backend options, deprecated aliases, and source implementation branches are discarded
after one-line residue classification unless they change the public mathematical
interface or block construction of a required object.

## Required Mathematical Mapping

Each mapping must be a theorem-shaped assertion with provenance. A future
implementation may store these assertions as a markdown table, CSV, or generated view,
but this tracked spec remains the canonical location or must point to exactly one
replacement document.

| Field | Required meaning |
| --- | --- |
| `Sage method or constructor` | The Sage constructor, method, class, function, protocol, or export spelling being interpreted. |
| `Sage behavior` | The observed behavior in the Sage body, examples, or written docs: inputs, outputs, branch cases, side effects, and conventions relevant to interpretation. |
| `Mathematical statement` | Complete sentence of the form: for objects of category `C`, under hypotheses `H`, this constructs, returns, or checks `Y`. |
| `Weakest category or refinement` | The weakest project category, construction, or refinement membership in which that sentence is true. |
| `Hypotheses and witnesses` | Mathematical hypotheses, construction data, witness data, or proof obligations required by the statement. |
| `Codomain or return object` | Return object, codomain, or payload class. |
| `Source evidence` | Source path plus section, line, signature, or stable source citation. |
| `Disposition` | `mathematical-assertion`, `nonmathematical-implementation-detail`, `unresolved-definition`, or `out-of-scope`. |

## Canonical Operation Rows

The rows currently recorded here are the constructor/factory cluster already visible in
the lattice evidence files: the free bilinear factory route, the field quadratic-space
wrapper route, the three integral-lattice constructors named by the
`constructorNameInventories` lattice collector, and the two torsion quadratic
constructor routes. This is not a completion claim for non-constructor lattice methods
or other category families.

| Sage method or constructor | Sage behavior | Mathematical statement | Weakest category or refinement | Hypotheses and witnesses | Codomain or return object | Source evidence | Disposition |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `FreeQuadraticModule` | Coerces rank, canonicalizes an `n x n` inner-product matrix over a commutative base ring, caches by presentation data, and dispatches to field, PID, integral-domain, or generic implementations. The form matrix is not required to be symmetric, nondegenerate, integral, or definite. | For a commutative ring `R`, a finite free `R`-module with chosen rank and bilinear form matrix is constructed. | `Modules(R).Free().FiniteRank().WithForms().Bilinear().Constructors().FreeQuadraticModule`; lattice membership requires additional symmetric, integral, nondegenerate, finite-rank free witnesses. | `R` is commutative; `rank` is a nonnegative integer; the matrix coerces to an `n x n` matrix over `R`; the chosen finite free presentation and bilinear form matrix are part of the object data. | Free bilinear module over `R`. | Sage source `sage/modules/free_quadratic_module.py:86-187`; official Sage docs `free_quadratic_module.html`; mapping row `SPEC-MAPPING-LATTICES:196`; inventory row `category_specs/lattices/docs/SAGE_INVENTORY.md:15`. | `mathematical-assertion` |
| `QuadraticSpace` / `InnerProductSpace` | Checks that `K` is a field and `sparse` is boolean, then delegates to `FreeQuadraticModule(K, rank=dimension, inner_product_matrix=..., sparse=sparse)`. | For a field `K`, a finite-dimensional free `K`-module with bilinear form matrix is constructed. | `Modules(K).Free().FiniteRank().WithForms().Bilinear().OverField().Constructors().QuadraticSpace`; not `Lattices(R)` without an integral presentation and lattice witnesses. | `K` is a field; `dimension` is a nonnegative integer; the matrix coerces to a `dimension x dimension` matrix over `K`; the chosen basis and bilinear form matrix are part of the object data. | Field-valued free bilinear module. | Sage source `sage/modules/free_quadratic_module.py:190-223`; official Sage docs `free_quadratic_module.html`; mapping row `SPEC-MAPPING-LATTICES:197`; inventory rows `category_specs/lattices/docs/SAGE_INVENTORY.md:16-17`. | `mathematical-assertion` |
| `IntegralLattice` | Accepts a symmetric rational matrix, integer rank identity form, Cartan/root descriptor, or `"U"`/`"H"`; optional basis data presents a generated sublattice in the ambient quadratic space. | For a finite-rank free abelian group with a symmetric integral nondegenerate Gram presentation, an integral lattice is constructed. | `Lattices(ZZ).Constructors().IntegralLattice`. | The effective Gram presentation is symmetric, integral, and nondegenerate over `ZZ`; optional basis rows or module elements belong to the ambient quadratic space; the finite-rank abelian presentation and form are witnesses. | `Lattice`. | Sage source `sage/modules/free_quadratic_module_integer_symmetric.py:73-259,625-669`; local wrapper `category_specs/lattices/__init__.py:105-174`; mapping row `SPEC-MAPPING-LATTICES:204`. | `mathematical-assertion` |
| `IntegralLatticeDirectSum` | Verifies inputs are Sage integral lattices, forms a block-diagonal ambient form, block-embeds selected bases, and optionally returns homomorphisms from each summand into the block presentation. | For a finite family of integral lattices over `ZZ`, their orthogonal direct sum is constructed, with canonical summand inclusions when requested. | `Lattices(ZZ).OrthogonalDirectSums()` via `Lattices(ZZ).Constructors().IntegralLatticeDirectSum`. | Inputs are a finite list of integral lattices; the block-diagonal form, selected basis presentation, and optional summand inclusions are witness data. | `Lattice` or `(Lattice, Sequence[LatticeMorphism])`. | Sage source `sage/modules/free_quadratic_module_integer_symmetric.py:262-369`; local wrapper `category_specs/lattices/__init__.py:188-237`; mapping row `SPEC-MAPPING-LATTICES:205`. | `mathematical-assertion` |
| `IntegralLatticeGluing` | Forms the orthogonal direct sum with embeddings, coerces glue components through discriminant groups, adjoins rational lifts, and optionally recomputes summand embeddings into the glued lattice. | For a finite family of integral lattices and compatible discriminant-group glue data, an overlattice or gluing lattice is constructed. | `Lattices(ZZ).Overlattices()` via `Lattices(ZZ).Constructors().IntegralLatticeGluing`. | Inputs are a finite list of integral lattices; every glue row has one component per lattice; each component coerces into the corresponding discriminant group; rational lifts and overlattice generators are witness data. | `Lattice` or `(Lattice, Sequence[LatticeMorphism])`. | Sage source `sage/modules/free_quadratic_module_integer_symmetric.py:372-616`; local wrapper `category_specs/lattices/__init__.py:240-271`; mapping row `SPEC-MAPPING-LATTICES:206`. | `mathematical-assertion` |
| `TorsionQuadraticForm` | Coerces a square symmetric rational matrix, clears denominators, uses Smith form, builds a free quadratic `ZZ` cover, forms denominator relations, and returns a torsion quadratic module. | For symmetric rational Gram data satisfying the quotient divisibility conditions, a finite torsion quadratic module is constructed. | `Modules(ZZ).WithForms().Quadratic().Torsion().Constructors().TorsionQuadraticForm`; lattice discriminant-group structure requires the specialization `coker(L -> L^#)` with descended lattice form. | `q` is a square symmetric rational matrix; quotient codomain is `QQ/ZZ` or `QQ/2ZZ`; Smith-denominator data witnesses the finite quotient presentation. | `TorsionQuadraticModule`. | Sage source `sage/modules/torsion_quadratic_module.py:35-87`; official Sage docs `torsion_quadratic_module.html`; mapping row `SPEC-MAPPING-LATTICES:208`; inventory row `category_specs/lattices/docs/SAGE_INVENTORY.md:559`. | `mathematical-assertion` |
| `TorsionQuadraticModule` | Constructs the finite quotient `V/W` where `V` is a symmetric free quadratic module over `ZZ` and `W` is a same-rank submodule; checking enforces equal rank, `ZZ` base, symmetric cover form, and generator data. | For a same-rank inclusion `W <= V` of symmetric free quadratic `ZZ`-modules, the quotient `V/W` is constructed as a finite torsion formed module with quotient-valued bilinear and quadratic forms. | `Modules(ZZ).WithForms().Quadratic().Torsion().Constructors().from_quotient`, with `Lattices(ZZ).DiscriminantGroups()` only for the specialization `coker(L -> L^#)` with descended lattice form. | `V` is a symmetric free quadratic module over `ZZ`; `W <= V` has the same rank; optional `gens` generate `V/W`; codomain moduli satisfy the required divisibility conditions. | `TorsionQuadraticModule`. | Sage source `sage/modules/torsion_quadratic_module.py:188-277`; official Sage docs `torsion_quadratic_module.html`; mapping rows `SPEC-MAPPING-LATTICES:209-210`; inventory rows `category_specs/lattices/docs/SAGE_INVENTORY.md:561-570`. | `mathematical-assertion` |

## Source Evidence Commits

Every substantive inventory or mapping commit must add or correct a source-backed assertion
here or in exactly one replacement structured document named by this spec. The commit
record is provenance for the mathematical assertions, not a second progress ledger.

| Commit | Operation rows added or corrected | Source files used |
| --- | --- | --- |
| `325d8915` | `forms.constructor.free-quadratic-module`; `forms.constructor.quadratic-space`; `forms.constructor.torsion-quadratic-form`; `forms.constructor.torsion-quadratic-module` | `sage/modules/free_quadratic_module.py`; `sage/modules/torsion_quadratic_module.py`; official Sage docs; `category_specs/lattices/docs/SAGE_INVENTORY.md`; `SPEC-MAPPING-LATTICES.md` |
| `a24824cd` | `lattices.constructor.integral-lattice`; `lattices.constructor.integral-lattice-direct-sum`; `lattices.constructor.integral-lattice-gluing` | `sage/modules/free_quadratic_module_integer_symmetric.py`; `category_specs/lattices/__init__.py`; `category_specs/lattices/docs/SAGE_INVENTORY.md`; `SPEC-MAPPING-LATTICES.md` |
