# Synthetic Lattice Model

A standalone abstract lattice category that replaces Sage's lattice surface —
not a wrapper over it. A lattice is a based projective `R`-module of finite
rank with an exact symmetric bilinear form; no ambient space, no echelon
coordinate frame, no basis-matrix vocabulary survives on the public surface.

## Bounded contexts

- **Category tree** (`categories.py`): `Lattices(R)` with axiom subcategories
  (Nondegenerate, Integral, Even, Unimodular, Definite, PositiveDefinite,
  NegativeDefinite, Indefinite, Hyperbolic, RootGenerated) and
  `DiscriminantForms(ZZ)` with its strata (Bilinear, Quadratic, Even,
  WithSourceLattice). Carriers from the typed domain algebra install as
  `ParentMethods` deltas.
- **Lattice parents/elements/morphisms** (`parents.py`, `elements.py`,
  `homsets.py`): one concrete hierarchy per stratum; typed elements carrying
  `b`/`q`; form-preserving homsets; `O(L)` with typed subgroups as the only
  supplied-generators home.
- **Discriminant forms** (`discriminant_forms.py`, `discriminant.py`): ONE
  stratified finite-quotient parent carrying the TorsionQuadraticModule + FGP
  + AdditiveAbelianGroup parity surface once; the sibling notions (discriminant
  group, plain finite quotient, torsion quadratic form, twist, subquotient) are
  constructions returning it. A plain finite quotient answers no form question.
- **Reduction/CVP/Voronoi suite** (decision D1 revised 2026-07-04): the
  spec-2.6 suite (BKZ, HKZ, closest/approximate-closest vector, Voronoi cell
  and relevant vectors, Gaussian heuristic, Hadamard ratio) lives on the
  positive-definite kernel — the subcategory Sage's own crypto lattice
  implementations presuppose (`IntegerLattice` is `ZZ^n` under the dot
  product; Gram positive definite, unimodularity never assumed). There is no
  `Cryptographic` axiom and no opt-in refinement; the suite is absent off the
  positive-definite stratum by ordinary category gating. Crypto-style lattice
  generators (q-ary, LWE/NTRU, random unimodular), when built, are widely
  exposed constructors, never axiom-gated methods.

## Construction and computation

- The category-namespace constructors (`Lattices(R).from_gram_matrix`, the
  named section-6 constructors, `DiscriminantForms(ZZ)` factories) are the only
  public entry; constructors prove invariants once and downstream code never
  re-checks them (parse-don't-validate).
- Every computational result is obtained by building an ephemeral Sage engine
  from the object's own data and asking it — never by reimplementing the
  algorithm and never from remembered theorems. Owned code is the ontology
  layer; Sage as-is is the oracle; suspected oracle bugs are filed issues plus
  gap-ledger rows, never patched around.
- Dispatch is by category membership and declared types; no `hasattr`/
  `getattr` probing selects behavior in implementation code.
- Sage upstream defects are never corrected inline: the isolated
  `sage_patches/` subtree holds one module per defect (a monkey-patch applied
  at package import, or — where cython immutability forbids patching — a
  corrected re-export owned code calls instead of the defective method). The
  package `__init__` and the test conftest both import it, so every consumer
  and every test run carries all patches.

## Signals (spec section 1.4)

Two signals, always distinct:

- **Absence**: where an operation is mathematically undefined, the name does
  not resolve (category gating), it does not raise.
- **Assertion (ADDD)**: internal invariants and domain contracts are plain
  `assert` statements whose messages dump the offending data and name the fix
  surface. `raise AssertionError(...)` branch forms and raise-for-invariant
  `if` guards are banned (POLICY.PREFER_ASSERTION; the `python -O` stripping
  rationale is rejected as cargo cult by the runtime-control-flow policy).
- Typed exceptions are NOT owned vocabulary: the ratified policy is
  assert-only (the earlier "boundary-validator" `ValueError` carve-out was
  confabulated and is rescinded). The implementation modules carry zero
  manually-raised typed exceptions (Tier C of the terminology-drift-cleanup
  plan, converted 2026-07-04 with their `pytest.raises` pins in lockstep).
  Engine rejections propagate as-is; the only typed-error pins are Sage
  engine rejections and Python operator-protocol TypeErrors, both parity
  surface.
- No runtime fallbacks, no legacy paths, no `try/except` in owned runtime code.

## Testing

Correctness evidence uses very small lattices; expected values come from the
Sage oracle (reference agreement) or the mapped doctest corpus, never from
agent memory. When a small fixture is slow here, the slowness is a defect
finding (a brute-force body where a delegation belongs), not a cost to absorb.
