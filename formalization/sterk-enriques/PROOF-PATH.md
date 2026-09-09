# The route, and the strength of each step

One row per node of the dependency graph
(`../../computations/scripts/sterk-enriques-cusps/DAG.md`).  A row is added when
the node's **statement** is written, not when it is proved — the strength a
result is stated in is decided when it is stated.

**Where this prose and the Lean differ, the Lean is right.**

Columns: the node id; the source locator the statement transcribes; the Lean
name once one exists; the strength actually stated; and the status —
`unstated` / `stated` / `read-back` (blind read-back done and audited) /
`proved`.

| Node | Source | Lean name | Strength stated | Status |
| --- | --- | --- | --- | --- |
| — | — | — | — | nothing stated yet |

## Strength: what "restricted" will mean here

The 11-day FLT run proved its deep inputs "in the restricted strength this
argument needs", and said so in a limitations file rather than letting the names
imply the general theorems.  The same will apply here, and the places it will
bite are known in advance:

- **Vinberg (C1).** The general theorem is about any lattice of signature
  $(1,n)$ and any finite-index reflection subgroup.  What this argument needs is
  the fundamental polyhedron for five explicit rank-10 lattices.  A statement
  restricted to those specimens is not a formalization of Vinberg's theorem.
- **Nikulin (A3).** Uniqueness of an even lattice by signature and discriminant
  form, needed only for $L_-$.
- **Baily–Borel (D3, D4).** Needed for one type IV domain and one arithmetic
  group, not for arbitrary reductive $\mathbb{Q}$-groups.
- **Scattone's nine (C11).** A table of possibilities for $F^\perp/F$; usable as
  a statement about the specific lattices in play.

Each such row records the restriction in its own words in the Strength column,
and `LIMITATIONS.md` collects them.
