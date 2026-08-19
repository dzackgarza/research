# A typed contract for a lattice interface, designed backend-first

Migrated 2026-08-20 from `~/gitclones/lattice_interface/tests/new_lattice_interface/`
(authored 2026-02). Design material, not a maintained surface: the repository's
lattice mathematics is owned by the preamble, and most of what this contract
declares the preamble now provides. What is preserved here is the part of the
design that the preamble does not provide, and the reasoning that produced it.

## What is here

- `specification/types.py` (722 lines) — an abstract type surface written
  *before* and *independently of* any backend: lattices split by definiteness,
  elements, morphisms, automorphisms, subobjects, quotients, the discriminant
  group and its elements, glue data, primitive embeddings, discriminant-form
  isometries, the genus, orthogonal subgroups, Coxeter data, root systems. Every
  method body is `assert False, "stub: ..."`, so the file is a statement of
  obligations and nothing else.

- `specification/conftest.py` — a self-contained rational-arithmetic backend
  that makes the contract runnable without Sage, plus fixture lattices, plus the
  hook that **fails any test marked `tdd_red` which passes**. That inversion is
  the point of the specification: a `tdd_red` assertion states an obligation the
  repository does not yet meet, so it becoming satisfied must be noticed rather
  than silently absorbed.

- `specification/test_*.py` — thirteen specification files (lattice, definite,
  indefinite, hyperbolic, elements and roots, substructures and discriminant,
  orbits, Eichler, group accessors and stabilizers, and three Nikulin
  workflows), plus the scope guard that keeps the `tdd_red` marker out of the
  conformance corpus.

- `test-doctrine-for-conformance-suites.md` — the test doctrine written for this
  corpus.

The scope guard was rebound at migration: it now scans
`computations/scripts/conformance_lattice_engines/` and permits the marker only
in `specification/`, and it asserts a positive count of marked files first,
because a guard ranging over an empty marker set asserts nothing.

## The design item the preamble does not own

Almost every operation the contract declares has a home in the preamble: the
invariants, the dual lattice, the discriminant form, gluing and overlattices,
$O(L)$ and its image in $O(q_L)$, invariant and coinvariant lattices, the
definite metric algorithms, Vinberg.

One family does not, and it is the reason this file is kept
(`specification/types.py:301-345`):

```
automorphism_lifts_to_overlattice(automorphism, complement, glue) -> bool
extend_automorphism_to_overlattice(automorphism, complement, glue) -> LatticeAutomorphism
liftable_automorphisms(complement, glue, *, subgroup=None) -> LatticeOrthogonalSubgroup
glue_compatibility(automorphism_self, automorphism_complement, glue) -> bool
automorphism_lifting_result(automorphism, complement, glue) -> (lifts, witness, obstruction)
```

The question these ask: given $L$ an overlattice of $M \oplus N$ with $M$ and $N$
primitive in $L$, and given isometries $\varphi_M \in O(M)$, $\varphi_N \in O(N)$,
when does the pair extend to an isometry of $L$?

Both halves of the answer are already owned. Nikulin's correspondence
(Nik80 Prop. 1.4.1, Zotero `TTY9FFJS`) makes such an $L$ the same datum as an
isotropic subgroup $H \le A_{M} \oplus A_{N}$ of the discriminant form — this is
what `IntegralLattices.glue`, `.overlattice` and `.maximal_overlattice` are built
on. And the map that sends an isometry to its action on the discriminant form is
`discriminant_representation`, $O(L) \to O(q_L)$. The lifting condition is then a
condition on that action: the pair extends exactly when the induced isometry of
$A_M \oplus A_N$ preserves $H$. So the operation is a *stabilizer* computation
over already-owned structure, and `liftable_automorphisms` is the preimage in
$O(M)$ (or in a given subgroup) of the stabiliser of $H$.

Stated that way it is a method on the gluing datum, or on the pair of primitive
inclusions — not on the lattice, which is where this contract put it. The
contract's placement is the artifact of a backend-shaped design; the mathematics
puts it on the arrow.

The rest of the contract is superseded by the owned categories, and is retained
as the record of an interface designed from the mathematics rather than from any
engine's method list.

## Test doctrine

`test-doctrine-for-conformance-suites.md` restates rules the repository's own
test guidelines already hold — assert mathematics, no content-free assertions,
precise types, no expected-failure masking. Three of its rules are not stated as
such anywhere in the repository and are worth promoting:

1. **No trivial primary witness.** An assertion whose subject is the zero vector,
   the identity map, or the empty object certifies nothing even when the
   assertion is otherwise mathematical.
2. **Agreement between entry points is plumbing, not correctness.** Two code
   paths returning the same answer is a fact about the code; correctness needs an
   independent oracle.
3. **A blacklist or a narrow module filter needs an explicit hidden-surface
   pass.** Otherwise the excluded surface is never counted and coverage is
   measured against a set the test itself chose.

## Related

- The engine survey this contract was designed against:
  `references/lattice-engines/`.
- The conformance suites that record what the engines actually provide:
  `computations/scripts/conformance_lattice_engines/`.
