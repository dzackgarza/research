# Automorphism groups across Sage's group constructors

Research code migrated 2026-08-20 from `gitclones/integral_lattice`
(PLAN-corpora-audit-registry, section R3):

- `tests/test_aut_group.py` (source `tests/test_aut_group.py`) — a coverage
  checklist of roughly ninety Sage group constructors, one instantiated
  representative for each, with the computed automorphism-group order
  checked against the object's own baseline. Covered and pending
  constructors are marked in the module docstring's checklist.
- `scripts/aut_group.py` (source `scripts/aut_group.py`) — the dispatcher
  the checklist drives.

Both files are unmodified below their origin headers, and the source tree's
relative layout (`scripts/` beside `tests/`) is reproduced here because the
test resolves the dispatcher by that path — it looks for
`<parent of tests/>/scripts/aut_group.py`, so the two directories must stay
siblings.

## What the checklist is for

Sage carries more than ten distinct notions of *group*, and
$\operatorname{Aut}(G)$ is, depending on which one you hold: present under
`automorphism_group`; present under a different name (`aut`,
`automorphism_group_gens`, `automorphism_group_generators` with a separate
`automorphism_group_order`); absent but computable ($\mathrm{GL}_n(\mathbb
Z)$ for a free abelian object); reachable only through the object's GAP
model; or genuinely uncomputable. That variation is exactly what the
preamble's owned `Aut()` exists to remove
(`src/dzack_research/preamble/categories/group/groups.sage`,
`OwnedGroups.ParentMethods.Aut`), so the dispatcher itself is superseded.

What is **not** superseded is the checklist: it is a requirement list for the
owned `Aut()`, naming which constructors a uniform automorphism-group
operation must answer for, and it records one measured obstruction — Sage's
PARI Smith-form call segfaults on the finitely generated abelian
presentation.

## Recorded defect in the dispatcher (kept unmodified)

Every handler wraps its route in `except Exception`, so a route that *failed*
is indistinguishable from a route that did not *apply*: `compute_aut` moves
on in both cases and reports only the accumulated warning strings when every
route is exhausted. A dispatcher over engines has to keep those two apart —
the owned `Aut()` asserts its hypothesis and says which engine it used
instead of surveying.

The route ordering is the part worth reading: `automorphism_group` first,
then the free-abelian $\mathrm{GL}_n(\mathbb Z)$ construction, then the
generator-returning spellings, then GAP's `AutomorphismGroup` through the
object's GAP model. It is a survey of where Sage keeps the operation, which
is the survey the owned uniform surface answers.
