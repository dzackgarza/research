# Adjudicating the research-raised failures against their catalogue contracts

Only three raise-site families in `test_functors_construct.sage` are ours (16 + 16 + 1);
each is adjudicated against what the catalogue actually contracts, not against the count.
Full log `.scratch/functors-failures.txt`.

## Case A — line 63, 16 failures: `assert free in FreeModules(ring)`

`free = Sets().free_module(ring)(Sets.Δ[2])`; the object reports itself as "Free module on
{…} over K in Category of vector spaces with basis over K" (or "modules with basis" over a
general ring).

**Catalogue contract.** `FreeModules(R)` is a project-owned declared category with the
exact edges (`#46`: "project-owned FreeModules(R), FiniteFreeModules(R),
FiniteProjectiveModules(R)"). The image of the free-module functor is free *by
construction*; that is the defining property of the left adjoint.

**Adjudication: the expectation is correct; the placement is the provider's.** The object
is built as free, placed under `*WithBasis`, and does not satisfy membership in
`FreeModules(R)`. Repairing this in research would mean weakening the assertion to the
provider's current placement, which is exactly what the brief forbids. No research change.

## Case B — line 111, 16 failures: `…Commutative().de_rham_adjunction()`

**Adjudication: provider-side missing constructor.** `CommutativeAlgebras` has no
`de_rham_adjunction` attribute at the deployed `6ad7a5ea`; nothing in this repository can
supply it. Handoff.

## Case C — line 24, 1 failure: the non-vacuity assertion I added

`NULLARY_FUNCTORS` is empty while the file's own known-values test names seven nullary
functors. **This one is a verified research-side defect.**

**Decision: kept as a failing assertion, not repaired by filling the dictionary with
unverified entries.** Populating it requires per-functor constructor/specimen triples, and
the deployed runtime already shows at least one of those specimens (`Groups().abelianization()`
applied to `Groups.S(3)`) raising a provider error. Adding entries on a guess would create
*our* false assertions — the opposite of "repair only verified defects". The assertion
names the obligation precisely; filling it is a per-entry task with its own evidence.

## Result

Two provider handoffs (free-module refinement into `FreeModules(R)`; `de_rham_adjunction`),
one open research item precisely stated. No assertion weakened, no exclusion, no skip
masked. `#417` remains unaccepted: this file still fails 147 of its cases, and coverage is
one of 754 construction files.
