# Coxeter and lattice algorithm surveys

Seven documents, landed 2026-08-20 from `~/gitclones/Coxeter` under
`PLAN-coxeter-deletion-audit-registry` (readers H, P2). They answer one
question the rest of the corpus keeps running into: **which lattice algorithm
applies to which signature**, and where an implementation for it exists.

Three of the seven come in two generations of the same document — the
`tmp_restore/docs/api-planning/` version and the later
`research/explorations/` version. The later one is a superset: it adds worked
`sage:` snippets to the prose. Both are kept because two of those added
snippets carry recorded errors, and because the earlier generation is what the
v1 implementation was written against.

## Contents

| Path | What it holds |
|---|---|
| `algorithms-survey-api-planning.md`, `algorithms-survey-explorations.md` | The core survey. Which of Sage/PARI/GAP/CoxIter answers which problem, split by the definite/indefinite line: shortest vectors, isometry testing, $O(L)$, theta series, genus, Vinberg's algorithm, covolume. Each row names an implementation source and an integration cost. |
| `investigations-api-planning.md`, `investigations-explorations.md` | Why the v1 lattice interface was rebuilt off `CombinatorialFreeModule`: the session should write `v = a*e + b*f` and `v*w` for the form, not carry combinatorial machinery. This is the design rationale of the generator syntax the preamble now has. |
| `research-roadmap-api-planning.md`, `research-roadmap-explorations.md` | The research roadmap: which variant of Vinberg's algorithm, convergence and stopping criteria, lattices over number fields for the non-crystallographic types, theta series, root/weight lattice coercions, discriminant forms. |
| `bilinear-modules-tdd-plan.md` | The doctest-first specification of the bilinear-module category: the API was written as docstring examples before any implementation. |

## The distinction the survey is built on

Most named lattice algorithms are *positive definite* algorithms. Coxeter
theory works in signature $(1,n-1)$. So the survey's central table separates:

- **definite** — LLL/BKZ/HKZ reduction, shortest and closest vectors, theta
  series, kissing number, automorphism group by short-vector orbits. All
  available, and now owned:
  `categories/modules/framed/formed/integrallattice/definite_lattices.sage`
  (`vectors_of_square`, `closest_vector`, `babai`, `voronoi_cell`, LLL/BKZ/HKZ)
  and `integral_lattices.sage` (`minimum`, `enumerate_short_vectors`).
- **indefinite** — where the same questions are open or need different
  machinery: $O(L)$ for indefinite $L$ is infinite and needs group generators
  rather than enumeration; the theta series diverges and needs regularization;
  primitive-embedding existence needs Nikulin's genus criteria rather than
  search. These remain live gaps; `enumerate_short_vectors` is
  positive-definite-only by construction.

Vinberg's algorithm and reflectivity are owned
(`hyperbolic_lattices.sage`: `vinberg_algorithm`, `is_reflective`, with
CoxIter behind the covolume check); the classification predicates and
subdiagram posets are owned in `vinberg_invariants.sage`. Discriminant forms
are owned (`torsionform/`, `tests/test_discriminant_forms.sage`), which closes
one roadmap row outright.

## Errors recorded in these documents

The statements below are the corrections; the documents are unedited.

- `algorithms-survey-explorations.md` gives the $E_8$ Gram spectrum as
  $[2,2,2,2,2,2,2,0]$ and calls $E_8$ positive **semi**definite. Both false:
  the $E_8$ Gram matrix is positive definite and unimodular (determinant 1, no
  zero eigenvalue).
- `research-roadmap-explorations.md` gives the $A_2$ theta series as
  $1 + 6q^2 + 6q^4 + 6q^6 + 12q^8 + O(q^{10})$. With Gram $[[2,-1],[-1,2]]$ the
  norms are twice the Loeschian numbers, $2, 6, 8, 14, \dots$, so the series is
  $1 + 6q^2 + 6q^6 + 6q^8 + 12q^{14} + \cdots$; there is no $q^4$ term.
- `research-roadmap-explorations.md` gives $H_3$ the Gram matrix
  $[[-2,\phi,0],[\phi,-2,1],[0,1,-2]]$ for the Coxeter matrix
  $[[1,3,2],[3,1,5],[2,5,1]]$. The off-diagonal entries are swapped: the
  $\phi$ sits on the $(1,2)$ edge, which that Coxeter matrix labels 3 (entry 1
  in this convention), while the order-5 edge $(2,3)$ gets 1 instead of $\phi$.
- `investigations-explorations.md` computes $(2e+3f)\cdot(e-f) = 5$ on the
  hyperbolic plane. The sign of $-f$ was dropped: the value is
  $2\cdot(-1)\cdot 1 + 3\cdot 1\cdot 1 = 1$.
- `investigations-explorations.md` states
  `QuadraticForm(ZZ,2,[0,1,0]).find_reps(1)` has the four solutions
  $(\pm1,\pm1)$. Over $\mathbb{Z}$, $xy = 1$ has exactly $(1,1)$ and
  $(-1,-1)$; the mixed-sign pairs give $xy = -1$.
- `bilinear-modules-tdd-plan.md` carries three: (a) it calls the $B_2$ root
  lattice indefinite on the ground that its Gram determinant is negative —
  $B_2$ is definite and its Gram determinant is positive; (b) it calls
  $x \mapsto 2x$ from Gram $I$ to Gram $2I$ an isometry — that map scales the
  form by 8; (c) it asserts $\alpha_1$ and $\alpha_2$ are adjacent in $E_8$
  with pairing $-1$ — in the Bourbaki labelling Sage uses, node 1 is adjacent
  to 3 and node 2 to 4, so $\alpha_1\cdot\alpha_2 = 0$.
