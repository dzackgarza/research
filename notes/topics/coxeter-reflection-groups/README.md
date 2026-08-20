# Coxeter reflection groups — the research prose of the Coxeter working trees

Thirteen documents, landed 2026-08-20 from `~/gitclones/Coxeter` and
`~/gitclones/Coxeter-v2` under `PLAN-coxeter-deletion-audit-registry`
(readers P2, S, V2). They are the mathematical account the two trees were
written against: the classification theory, the hyperbolic geometry, the
history, the open questions, and the two design histories that explain why
the built preamble looks different from either plan.

Each file keeps its origin header. Content is unmodified, including the
errors listed at the bottom of this file.

## The one theorem the whole corpus is organised around

For a Coxeter system with Gram matrix $G$ in the project's convention
$B_{ij} = 2\cos(\pi/m_{ij})$ (so $B_{ii} = -2$, and $B$ is the negative of
the literature's Schläfli matrix $C$), the type is the definiteness of $-G$:

| type | statement about $-G$ | signature of $G$ | acts on |
|---|---|---|---|
| elliptic (spherical) | positive definite | $(0,n,0)$ | $S^{n-1}$ |
| parabolic (euclidean) | positive semidefinite, corank 1 | $(0,n-1,1)$ | $\mathbb{E}^{n-1}$ |
| hyperbolic | indefinite, exactly one negative eigenvalue | $(1,n-1,0)$ | $\mathbb{H}^{n-1}$ |

`foundations/classification-theory.md` states this and, in its opening
section, the distinction that the rest of the corpus is built on:
classification is a property of the form, and eigenvalue counting or a
determinant sign is at most a way of *verifying* it. The preamble took the
same position — `integral_lattices.sage`'s `refine_one_lattice` routes by
the radical of the correlation morphism and says in comment that it is
deliberately not a determinant proxy — so this corpus is the written source
of a doctrine the repository already holds.

## Contents

| Path | What it holds |
|---|---|
| `foundations/mathematical-theory.md` | The full theory account: Coxeter systems and their presentations, root systems, the Gram/Coxeter-matrix correspondence, the classification, maximal parabolic subdiagrams, Vinberg's algorithm. |
| `foundations/classification-theory.md` | The definiteness-based classification alone, with the mathematics-versus-algorithm distinction stated first. |
| `foundations/geometric-foundations.md` | Hyperbolic reflection groups: fundamental domains in $\mathbb{H}^n$, Coxeter polytopes, finite covolume, cusps, the Vinberg and Lannér pictures. |
| `foundations/historical-development.md` | Background: Schläfli, Coxeter, Witt, Vinberg; how the classification reached its present shape. |
| `foundations/mathematical-foundations-reference.md` | An earlier reference version of `mathematical-theory.md`, kept because it is the copy the v1 implementation cites; overlapping but not identical. |
| `foundations/v1-consolidated-theory.md` | The v1 archive's own consolidation, and the shortest complete statement of the program: the classification, then a definitions section (Gram matrix, subdiagram, maximal parabolic subdiagram, Coxeter matrix). It carries three statements the other foundations files do not, two of them consequences of **Cauchy interlacing for principal submatrices** — a non-elliptic subdiagram has no elliptic superdiagram, and the signature of a principal submatrix is constrained by the signature of the whole — and, third, **Vinberg's covolume criterion**. |
| `explorations/open-questions.md` | The research-question catalogue: complexity of maximal-parabolic enumeration, Galois-invariance of the counts, growth asymptotics, regularized indefinite theta series. |
| `explorations/research-notes.md` | The same questions with experiment status attached — what was tried, on which specimens, and what came back. |
| `explorations/alternative-approaches.md` | Design rationale: the classification routes considered and rejected before the definiteness route was fixed. |
| `design-history/v1-implementation-guide.md` | The v1 architecture: an `AlgebraicLattice` base with mixins per property. The preamble diverged to category refinement, so this reads as the road not taken. |
| `design-history/v1-overview.md` | The v1 corpus map, bundled with the guide. |
| `v2-theory/math-core.md` | The Coxeter-v2 authority statement of the same foundations, with two deltas the v1 corpus lacks: Cauchy interlacing for pruning subdiagram search, and non-crystallographic types over $\mathbb{Z}[\phi]$ and cyclotomic fields. |
| `v2-theory/geometric-theory.md` | The v2 research program: order complexes of the parabolic poset, building cohomology, the Tits cone, Schläfli volume formulas, the Galois-invariance conjecture for maximal-parabolic counts, regularized theta series, growth asymptotics. |

## What of this the preamble already owns

The classification predicates and the subdiagram posets are owned twice, at
diagram level and at form level:
`categories/modules/framed/formed/integrallattice/vinberg_invariants.sage`
(`is_elliptic`, `is_parabolic`, `is_hyperbolic`, `is_compact_hyperbolic`,
`is_paracompact_hyperbolic`, `parabolic_subdiagram_poset`,
`maximal_parabolic_subdiagram_poset`) and `coxeter_diagrams.sage`
(`is_elliptic`, `is_parabolic`, `from_coxeter_matrix`, `from_cartan_type`).
`hyperbolic_lattices.sage` owns `vinberg_algorithm` and `is_reflective`.
Exact $2\cos(\pi/n)$ arithmetic for the non-crystallographic types is in
`vinberg_invariants.sage`'s `ReflectionCosineSet`.

So what remains genuinely unbuilt, and is stated only here:

- **the covolume criterion** — a hyperbolic Coxeter group has finite
  covolume iff every maximal parabolic subdiagram is affine — and the
  cusp correspondence, one cusp per maximal parabolic
  (`v2-theory/geometric-theory.md` §2, `foundations/geometric-foundations.md`);
- **hyperbolic-space models**: the hyperboloid, Klein and Poincaré charts,
  and $\cosh d(v,w) = -(v,w)/\sqrt{(v,v)(w,w)}$. Per the vault ruling that
  rays and ideal points live in $L \otimes \mathbb{R}$, their home is the
  base-changed parent, not $L$;
- **Cauchy interlacing** as a pruning rule for the subdiagram search: a
  non-elliptic subdiagram admits no elliptic superdiagram
  (`v2-theory/math-core.md`);
- **the Galois-invariance conjecture** and the regularized indefinite theta
  series (`v2-theory/geometric-theory.md` §3–4);
- **lattices over $\mathbb{Z}[\phi]$ and cyclotomic base rings** for $H_3$,
  $H_4$ and $I_2(p)$: the exact cosine arithmetic exists, a lattice over
  such a ring does not.

## Errors recorded in these documents

Recorded so a later reader cannot re-derive them from the text. The
statements below are the corrections; the documents are unedited.

- `foundations/geometric-foundations.md` (line 198) says a hyperbolic
  fundamental simplex has "some angles obtuse ($>\pi/2$)", and an elliptic
  one all acute. **False.** Dihedral angles of a Coxeter polytope are
  $\pi/m \le \pi/2$ by definition. The spherical/euclidean/hyperbolic
  trichotomy for a simplex is by angle *sum* — for a triangle,
  $\alpha+\beta+\gamma$ against $\pi$ — never by any angle being obtuse.
- `foundations/mathematical-theory.md` (line 207) and
  `foundations/mathematical-foundations-reference.md` (line 178) call
  $A_n, D_n, E_6, E_7, E_8$ the "complete list of finite irreducible
  Coxeter groups". That is the **simply-laced** list. The complete list
  adds $B_n$, $F_4$, $G_2$, $H_3$, $H_4$, $I_2(p)$ — all of which the same
  documents tabulate elsewhere.
- `v2-theory/math-core.md` (line 51) writes the hyperbolic row as "$-G$ is
  indefinite, exactly one positive eigenvalue" with signature $(1,n-1,0)$.
  The two disagree: if $G$ has signature $(1,n-1,0)$ then $-G$ has $n-1$
  positive eigenvalues and one negative. The signature column and the code
  it documents are right; the prose is the slip, and should read "$G$ has
  exactly one positive eigenvalue". The same slip is in §2 item 3 of the
  same file.
- `v2-theory/math-core.md` (line 27) writes $G_{ij} = -2\cos(\pi/M_{ij})$,
  the literature's Schläfli sign. The in-tree convention
  (`tests/coxeter_tdd_specs/literature/PROJECT_CONVENTIONS.md`, and the
  preamble's `minimal_edge_lattices`, where a single edge is
  $[[-2,1],[1,-2]]$) is $B_{ij} = +2\cos(\pi/M_{ij})$. The two differ by
  negating a subset of basis vectors on a tree diagram, so no statement in
  the file is thereby wrong, but the corpus is sign-inconsistent with
  itself and the in-tree owner's sign governs.
