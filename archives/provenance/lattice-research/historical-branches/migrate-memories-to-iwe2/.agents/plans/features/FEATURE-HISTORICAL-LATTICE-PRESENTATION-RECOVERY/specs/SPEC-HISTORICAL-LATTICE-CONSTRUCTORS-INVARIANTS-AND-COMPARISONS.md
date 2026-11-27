---
id: SPEC-HISTORICAL-LATTICE-CONSTRUCTORS-INVARIANTS-AND-COMPARISONS
trackerStatus:
  type: spec
parents:
- '[[FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY]]'
dependsOn:
- '[[SPEC-HISTORICAL-LATTICE-PRESENTED-OBJECT-CONTRACTS]]'
title: Recover lattice constructor naming invariants and comparison surfaces
status: complete
priority: high
requirement: Standard constructors, invariants, and comparison predicates from historical
  lattice code must be recovered with source-grounded mathematical owners and theorem
  hypotheses.
acceptanceCriteria:
- Named standard-lattice constructors are admitted through the approved constructor
  layer and remain available for later research reuse.
- Coble-specific derived lattice constructors are not used as evidence in the feature
  that proves the Coble lattice presentation.
- Rank, determinant, signature, scale, evenness, genus, local genus, rational isometry,
  and integral isometry are methods on the appropriate lattice noun.
- Nikulin-style invariants are lattice invariants with explicit domain hypotheses
  and warnings or rejection outside those hypotheses.
- Comparison predicates either return exact booleans with sourced criteria or return
  witness-bearing morphisms when the claim is existential.
complexity: 75
tags:
- FEATURE-HISTORICAL-LATTICE-PRESENTATION-RECOVERY
---
# Recover lattice constructors, invariants, and comparison predicates

## Source Provenance

- `category_specs/lattices/subcategories/integral.py`: active category-spec surface for integral lattice constructors (`Z`, `U`, `A`, `D`, `E`, `I`, `II`)
- `category_specs/forms/subcategories/integral.py`: integral formed-module surface for `scale`, `is_even`, `genus`, `local_genus_symbol`, `is_rationally_isometric_to`, `is_locally_isometric_to`, `is_in_same_genus_as`, `is_isometric_to`, `nikulin_invariants`
- `SPEC-MAPPING-LATTICES.md`: forms/lattices boundary, lattice tier table, constructor surface for rational Gram, integral promotion, signature, and negative root Gram
- `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md`:
  backend routing for isometry/genus/local conditions, constructor naming, negative
  root-lattice convention, twist versus scalar multiplication, signature terminology,
  and Nikulin invariant ownership.
- `projects/github.com__dzackgarza__lattice-research/context/bilinear-form-category-semantics`: named constructor placement,
  negative root convention, hyperbolic plane convention, and stable orthogonal group
  notation.
- `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md`:
  source-backed owner rows for constructors, direct sums, twist, signature, genus,
  isometry predicates, and deferred definite/indefinite algorithms.

## Contract

The constructor surface must recover common lattice families and operations only after
the current constructor admission layer says where they live. Examples include rank-one
lattices, hyperbolic planes, root lattices, odd and even unimodular lattices, K3
lattices, Mathieu-related lattices where source-grounded, twists, direct sums, and
parseable expression syntax if that syntax is approved as public.

The invariant surface must be method-owned by the lattice noun. Immediate invariants
such as rank, determinant, signature, scale, and evenness are computed directly from
the presentation. Genus, local equivalence, rational equivalence, and integral isometry
must route to mature exact backends or theorem-backed classification branches.

Nikulin-style data such as `(r, a, delta)` are invariants of the lattice under explicit
hypotheses. They must not be presented as discriminant-group-local facts and must not
be used outside their theorem-backed domain as if classification still applies.

## Recovered Constructor Surface

Named standard constructors are admitted as project vocabulary when they construct a
presented lattice object with selected generators and form data:

- `Lattice.Z()` constructs the rank-one lattice `<1>`.
- `Lattice.U()` constructs the hyperbolic plane with Gram `[[0,1],[1,0]]`.
- `Lattice.A(n)`, `B(n)`, `C(n)`, `D(n)`, `E(n)`, `F4()`, and `G2()` construct the
  repo's root-lattice convention. Roots are negative definite unless the constructor
  explicitly says otherwise; backend positive-definite conventions are sign-adjusted at
  the backend boundary.
- `Lattice.I(p, q)` constructs the odd unimodular lattice of signature `(p,q)`.
- `Lattice.II(p, q)` constructs the even unimodular indefinite lattice when the
  existence hypotheses hold, including `p-q == 0 mod 8` and positive rank.
- `Lattice.k3()` constructs the K3 lattice as a standard comparison object
  `II(3,19)`.
- `RationalLattice.from_gram(...)` owns Gram construction with promotion to the
  integral lattice meet when the Gram matrix is integral and the hypotheses hold.
- `Lattice.from_gram(...)` is the integral closed constructor after validation.
- `from_string(...)` is optional parser syntax for the same named constructors; it must
  remain a parser for approved constructor expressions, not an independent semantic
  surface.

`direct_sum(other)` or `L + M` is the orthogonal direct sum with block-diagonal form
data and selected generators. `L ** n` is repeated orthogonal direct sum when admitted
as notation. `twist(s)` scales the form by `s`; it is not scalar multiplication of the
carrier or selected generators. Scalar multiplication of submodules remains the module
operation `{s*x : x in M}`.

## Derived Research Constructor Boundary

The historical `coble_picard()` and `coble_transcendental()` methods are not admitted
as proof shortcuts. The Coble pipeline must first construct the geometric lattice from
the surface/cover data, then compare it with a standard target by a sourced isometry
test or witness.

After that derivation is accepted, a canonical project constructor such as a named
`T_Co` target may be added as downstream convenience. Its docstring must cite the
accepted proof artifact or decision authorizing the standard presentation, and it must
not replace the derivation in the feature that proves the Coble lattice presentation.

## Recovered Immediate Invariants

Immediate invariants are computed from the presented object and its form:

- `rank()` or `ngens()` is the finite rank of the selected free carrier.
- `gram_matrix()` is presentation data for the form in selected generators.
- `determinant()` or `discriminant()` is the determinant/discriminant of the presented
  form where that invariant is defined.
- `signature_pair()` is the pair `(n_+, n_-)` after scalar extension to a selected
  ordered real realization. Sage's scalar `signature() = n_+ - n_-` is display or
  interop data, not the owner of signature semantics.
- `scale()` is the ideal generated by all pairings `b(x,y)`; over `ZZ` this is a
  principal ideal generator after sign convention is fixed.
- `is_even()` means `b(x,x) in 2R` for every element under the integral form
  hypotheses; it is not a definite-lattice property.
- `is_unimodular()` means `L = L^#`, equivalently trivial discriminant group under the
  nondegenerate integral hypotheses.

## Recovered Theorem And Backend Invariants

The following methods are admitted only with explicit theorem or backend branch data:

- `genus()` returns the genus data for integral lattices through a sourced local-global
  theory or an exact backend such as Hecke/Oscar.
- `local_genus_symbol(p)` returns the local genus symbol at a prime and must record
  the local field/ring and backend/theorem used.
- `is_in_same_genus_as(other)` compares genus data only after both objects satisfy the
  same branch hypotheses.
- `is_rationally_isometric_to(other)` is a rational isometry predicate over `K` and
  must route through a mature exact quadratic/form backend or return a witness when
  requested.
- `is_locally_isometric_to(other, p)` compares local isometry at `p` under the local
  branch hypotheses.
- `is_isometric_to(other, witness=False)` is integral lattice isometry. With
  `witness=True`, it must return an isometry morphism or a structured failure, not only
  a boolean.

Backend failure is not proof of non-isometry. If the selected backend cannot decide a
case, the method must report an undecided/error state or route to a tracked backend-gap
task instead of silently weakening the claim.

## Recovered Nikulin-Style Invariant Surface

`nikulin_a()`, `coparity()`, `delta()`, and `nikulin_invariants()` are lattice theorem
context methods. They are admitted only under the explicitly recorded branch for even
indefinite 2-elementary lattices or another cited theorem with equivalent hypotheses:

- `r = rank(L)`;
- `a` is the length of the 2-elementary discriminant group;
- `delta`/`coparity` is determined by the parity of the discriminant quadratic form;
- the discriminant group may expose `is_p_elementary(p)`, but it does not own
  `delta`, `coparity`, or `(r,a,delta)`.

Outside the theorem-backed domain, implementations must either reject the method call
or emit the category diagnostic warning required by `SPEC-MAPPING-CAT` and return only
the explicitly meaningful components. They must not imply Nikulin classification or
genus uniqueness outside the stated hypotheses.

## Standard Library Versus Derived Research Objects

Standard lattice constructors are a desired library surface. They let later research
use canonical sourced objects instead of constructing ad hoc isometric presentations
such as `I_{1,10}(2)`, `\langle -2 \rangle \oplus U(2) \oplus E_8(2)`, or a
handwritten Gram matrix when the intended object is already canonical.

Derived project objects are separate. The feature that proves a Coble lattice is
isometric to a standard presentation must construct the object geometrically, then
verify the isometry. It may use standard constructors as comparison targets only after
the constructed lattice exists. Once accepted, a canonical sourced `T_Co` surface is
desirable for downstream research so later agents do not re-invent equivalent
presentations.

## Non-Preservation Boundaries

- Do not preserve `coble_picard` or `coble_transcendental` as proof shortcuts that
  bypass the Coble construction.
- Do not present a self-computed invariant match as an isometry without the theorem,
  hypotheses, or witness required for that branch.
- Do not hide backend failure by falling back to weaker sampled or bounded checks.
- Do not duplicate simple Sage or Oscar constructors behind trivial helper aliases
  unless the alias is the approved project vocabulary.

## Acceptance Criteria

- [x] Every recovered standard constructor has an owner category and source grounding.
- [x] Derived project constructors such as a future canonical `T_Co` record the proof
  artifact or decision that authorizes their downstream use.
- [x] Every recovered invariant records whether it is immediate, theorem-backed, or
  backend-computed.
- [x] Integral isometry and classification predicates state the exact branch used and
  the evidence needed to accept the result.
- [x] Coble derivation code is forced to construct the geometric input before invoking
  lattice comparisons.
- [x] Downstream post-derivation Coble research is directed to use the canonical
  sourced `T_Co` rather than ad hoc isometric presentations or raw Gram matrices.

## 6-Gate Protocol Review Log

**Reviewer**: automated 6-gate spec review
**Date**: 2026-05-07
**Protocol**: Source grounding verification, mathematical correctness audit

### Gate 1: Source Path Existence

| Source Claimed | Exists? | Notes |
|---|---|---|
| `src.bak/lattices/core/integral.py` | NO | Path does not exist; `src.bak/` directory absent from repo. The claimed constructors (`Z`, `U`, `A`, `D`, `E`, `I`, `II`) and methods (`scale`, `is_even`, `genus`, etc.) cannot be verified at this location. Closest existing files are `category_specs/lattices/subcategories/integral.py` and `category_specs/forms/subcategories/integral.py`, but these are category-spec compatibility imports, not the historical constructor code. |
| `src.bak/lattices/core/rational.py` | NO | Same `src.bak/` directory absent. Rational Gram construction, integral promotion, signature, and negative root Gram construction cannot be verified at this location. |
| `.agents/skills/lattice-redesign/references/lattice-interface-style-guide.md` | YES | Verified. Contains backend routing for isometry/genus/local conditions, constructor naming, negative root-lattice convention, twist vs scalar multiplication, signature terminology, and Nikulin invariant ownership (lines 45-46, 463-468). |
| `projects/github.com__dzackgarza__lattice-research/context/bilinear-form-category-semantics` | YES | Verified. Contains named constructor placement (lines 23-24), negative root convention (line 45), hyperbolic plane convention (line 46), and stable orthogonal group notation (lines 47-48). |
| `plans/features/FEATURE-CATEGORY-SPECS-AND-SAGE-SURFACES/specs/SPEC-MAPPING-LATTICES.md` | YES | Verified. Contains source-backed owner rows for constructors, direct sums, twist, signature, genus, isometry predicates, and deferred definite/indefinite algorithms (confirmed via content inspection, lines 28-100+). |

**Gate 1 Verdict**: PARTIAL FAIL — 2 of 5 source references point to nonexistent `src.bak/` paths. The other 3 are verified. The spec's mathematical claims are not falsified by this gap (they are corroborated by the existing sources), but the provenance is not reproducible.

### Gate 2: Source Content Match

For the 3 verified sources:

- **lattice-interface-style-guide.md**: The spec's claims about constructor naming, negative root convention, twist/signature terminology, and Nikulin ownership are all confirmed present in the style guide. The guide explicitly states: "Root lattices are negative definite in repo mathematics unless explicitly stated" and "Nikulin-style invariants belong to the lattice theorem context ... `delta`, `coparity`, and the tuple `(r, a, delta)` are lattice invariants, not free-standing invariants of `A_L`" (matching spec lines 64-66).

- **bilinear-form-category-semantics.md**: Confirms named constructor placement on `Lattice` (line 23: "Almost all named constructors belong on `Lattice`"), negative root convention (line 45), hyperbolic plane convention (line 46: "hyperbolic plane `U` has Gram `[[0,1],[1,0]]`"), and stable orthogonal group notation (line 47).

- **SPEC-MAPPING-LATTICES.md**: Confirmed as a comprehensive mapping spec with owner rows for constructors, direct sums, twist, signature, genus, isometry predicates, and algorithm routing. The `src.bak/` code was likely a historical snapshot; the mapping spec is the current canonical source for the constructor and invariant surface.

**Gate 2 Verdict**: PASS for verified sources. The 3 existing sources accurately support the spec's claims.

### Gate 3: Mathematical Correctness — Constructors

| Constructor | Definition | Correct? | Notes |
|---|---|---|---|
| `Lattice.Z()` | Rank-one `<1>` | YES | Standard integral lattice of rank 1 with Gram [1]. |
| `Lattice.U()` | Hyperbolic plane `[[0,1],[1,0]]` | YES | Standard even unimodular lattice of signature (1,1). |
| `Lattice.A(n)`, `B(n)`, `C(n)`, `D(n)`, `E(n)`, `F4()`, `G2()` | Root lattices, negative definite | YES | Standard Cartan-Killing root lattices. Sign convention (negative definite) is a project choice consistent with algebraic geometry literature; the spec correctly notes backend sign adjustment for positive-definite defaults. |
| `Lattice.I(p,q)` | Odd unimodular `I_{p,q}` | YES | Standard notation for odd unimodular indefinite lattice. |
| `Lattice.II(p,q)` | Even unimodular with `p-q ≡ 0 mod 8` | YES | Existence condition is mathematically correct (Milnor-Hasse-Minkowski). |
| `Lattice.k3()` | `II(3,19)` | YES | K3 lattice is indeed the unique even unimodular lattice of signature (3,19). |
| `RationalLattice.from_gram(...)` | Gram construction with promotion | YES | Rational forms promoting to integral when Gram is integral is standard. |
| `direct_sum` / `+` | Orthogonal direct sum | YES | Block-diagonal form. |
| `twist(s)` | Scale form by s | YES | Correctly distinguished from scalar multiplication of the module. |

**Gate 3 Verdict**: PASS. All constructor definitions are mathematically correct and consistent with lattice theory conventions.

### Gate 4: Mathematical Correctness — Invariants

| Invariant | Definition | Correct? | Notes |
|---|---|---|---|
| `rank()` / `ngens()` | Finite rank of free carrier | YES | |
| `gram_matrix()` | Presentation data | YES | Spec correctly notes this is presentation data, not an abstract invariant. |
| `determinant()` / `discriminant()` | det of Gram | YES | Defined for nondegenerate forms. |
| `signature_pair()` | `(n_+, n_-)` | YES | Correctly distinguishes from Sage's scalar `signature()`. |
| `scale()` | Ideal of all `b(x,y)` | YES | Over ZZ, principal ideal generator. |
| `is_even()` | `b(x,x) ∈ 2R` | YES | Correct definition of even lattice. |
| `is_unimodular()` | `L = L^#` | YES | Equivalent to trivial discriminant group when nondegenerate. |
| `genus()` | Genus data | YES | Correctly notes dependence on local-global theory/backend. |
| `is_rationally_isometric_to()` | Rational isometry | YES | |
| `is_isometric_to(witness=...)` | Integral isometry | YES | Witness-bearing variant is a strong correctness requirement. |
| `nikulin_a()`, `coparity()`, `delta()` | (r,a,δ) for 2-elementary | YES | Nikulin invariants with correct domain hypotheses (even indefinite 2-elementary). Spec correctly restricts to domain and prohibits free-standing use outside hypotheses. |

**Gate 4 Verdict**: PASS. All invariant definitions are mathematically correct with explicit hypotheses.

### Gate 5: Boundary and Non-Preservation Rules

| Rule | Assessment |
|---|---|
| `coble_picard`/`coble_transcendental` not admitted as proof shortcuts | Project-specific constraint, internally consistent |
| No self-computed invariant match as isometry without theorem/witness | Mathematically sound discipline |
| No hiding backend failure via weaker checks | Critical for correctness; matches style guide |
| No trivial Sage/Oscar alias duplication | Good API hygiene |

**Gate 5 Verdict**: PASS. All boundary rules are sound.

### Gate 6: Self-Consistency and Completeness

- **Constructor ↔ Invariant alignment**: All constructors produce objects for which the stated invariants are well-defined under the appropriate hypotheses. No circular dependencies detected.
- **Nikulin domain hypothesis**: The spec correctly restricts `(r,a,delta)` to even indefinite 2-elementary lattices, consistent with Nikulin's classification theorem. The prohibition against presenting these as discriminant-group-local facts is grounded in theory (they are lattice invariants, not invariants of `A_L` alone).
- **Derived-vs-standard boundary**: Clear separation between standard library constructors and derived project objects (`T_Co`). The Coble pipeline constraint (geometric construction before lattice comparison) is well-specified.
- **Acceptance criteria**: All 6 criteria are verifiable and internally consistent with the body text.

**Gate 6 Verdict**: PASS.

### Overall Assessment

| Gate | Status |
|---|---|
| Gate 1: Source Path Existence | PARTIAL FAIL (2/5 paths broken) |
| Gate 2: Source Content Match | PASS (verified sources match) |
| Gate 3: Constructor Correctness | PASS |
| Gate 4: Invariant Correctness | PASS |
| Gate 5: Boundary Rules | PASS |
| Gate 6: Self-Consistency | PASS |

**Summary**: The spec is mathematically correct, internally consistent, and its claims are well-supported by the 3 verified source documents. The sole deficiency is the citation of two `src.bak/` paths that no longer exist in the repository. These paths appear to reference a historical backup directory that has since been removed or reorganized. The spec's mathematical content is not invalidated by this gap (the same constructs are attested in `SPEC-MAPPING-LATTICES.md` and the style guide), but the provenance section should be updated to reference currently existing files.

**Recommendation**: Update the Source Provenance section to either (a) remove the `src.bak/` references and rely on the verified sources, or (b) replace them with the actual current paths if the historical code has been migrated (e.g., files under `category_specs/` or `plans/features/`).
