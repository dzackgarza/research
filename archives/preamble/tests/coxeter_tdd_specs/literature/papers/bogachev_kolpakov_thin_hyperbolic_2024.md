# Thin hyperbolic reflection groups

**Source**: arXiv:2112.14642 [math.GR], version v4 (17 Jan 2024)
**Title (verbatim)**: *Thin hyperbolic reflection groups*
**Authors**: Nikolay Bogachev, Alexander Kolpakov
**Bibliography label**: `[BogachevKolpakov2024]`
**First extracted**: 2025-07-26. **Corrected against the v4 full text**: 2026-08-20.

## Corrections to the 2025-07-26 extract

The previous version of this file stated two things wrongly. Both are recorded here rather
than silently overwritten, because the wrong values were already reachable from the
citation index.

1. **A quadratic form was labelled a Gram matrix.** The paper writes
   $f(x) = (x,x)$ — a quadratic form in $x = (x_0, x_1, x_2)$, printed with its
   *doubled* cross terms. The old extract headed both forms "Gram matrix". The Gram
   matrix $G$ of $b$ satisfies $q(x) = x G x^{\mathsf T}$, so every cross coefficient
   is halved: $14 \mapsto 7$, $98 \mapsto 49$. Both halvings are exact, so both Gram
   matrices are integral. Copying the printed form's coefficients into a Gram matrix
   would give the wrong lattice, the wrong determinant and the wrong signature.

2. **The examples were cited as "Section 2, Example 1".** They are **Section 6**, in
   two numbered subsections — §6.1 *Non–reflective lattice with roots* and §6.2 *A
   lattice without roots*. The paper uses numbered subsections, not "Example 1". The
   old extract also said the first four roots establish the nested thin subgroups;
   the paper's own reason for stopping the picture at four is presentational — the
   scheme "becomes non–planar for more than 4 roots" — while non-reflectivity is
   established from the sixteen roots listed below.

## §6.1 Non–reflective lattice with roots

The lattice is $L$, defined over $\mathbb{Q}$, of **signature $(2,1)$** in the paper's
convention (two positive, one negative index of inertia).

Quadratic form, verbatim as printed:

$$f(x) = (x,x) = 3x_0^2 + 14x_0x_1 + 98x_0x_2 + 49x_2^2 .$$

Gram matrix of the associated symmetric bilinear form $b$, with $q(x) = xGx^{\mathsf T}$:

$$G_L = \begin{pmatrix} 3 & 7 & 49 \\ 7 & 0 & 0 \\ 49 & 0 & 49 \end{pmatrix},
\qquad \det G_L = -2401 = -7^4 .$$

Invariant factors of $G_L$: $1,\ 49,\ 49$.

**Statement**: "Then $L$ is non–reflective." That is, the subgroup of $O(L)$ generated
by reflections in roots has infinite index, so the fundamental Coxeter polyhedron has
infinite volume.

Vinberg's algorithm applied to $L$ produces these first sixteen roots (verbatim):

| | | | |
|---|---|---|---|
| $v_1=(0,7,-1)$ | $v_2=(-7,-11,2)$ | $v_3=(0,0,1)$ | $v_4=(-42,-24,5)$ |
| $v_5=(-98,14,1)$ | $v_6=(-140,-31,9)$ | $v_7=(-168,-12,7)$ | $v_8=(-21,-61,14)$ |
| $v_9=(-42,-94,19)$ | $v_{10}=(-329,22,7)$ | $v_{11}=(-42,-108,23)$ | $v_{12}=(-252,-74,19)$ |
| $v_{13}=(-273,-37,14)$ | $v_{14}=(-28,-86,21)$ | $v_{15}=(-56,-151,33)$ | $v_{16}=(-49,-154,39)$ |

Two further statements of §6.1, verbatim:

- "The involution $v_5 \to v_{10}$, $v_{14} \to v_{16}$ turns out to be an
  infinite–order symmetry of the reflective part of $L$."
- "The Coxeter scheme of the root system above quickly becomes complicated (it becomes
  non–planar for more than 4 roots)." The figure therefore draws only $v_1,\dots,v_4$;
  that scheme has three infinite bonds and one bond labelled $4$. Explicit $3\times 3$
  integer matrices for the reflections $r_1,\dots,r_4$ are given in the paper.

## §6.2 A lattice without roots

The lattice is $N$, defined over $\mathbb{Q}$, of **signature $(2,1)$**. The example was
communicated to the authors by **Gaël Collinet**.

Quadratic form, verbatim as printed — note that $x_0$ occurs only in the term
$98x_0x_2$, so this is *not* the index-reversal of the §6.1 form:

$$f(x) = (x,x) = 49x_1^2 + 98x_0x_2 + 14x_1x_2 + 3x_2^2 .$$

Gram matrix:

$$G_N = \begin{pmatrix} 0 & 0 & 49 \\ 0 & 49 & 7 \\ 49 & 7 & 3 \end{pmatrix},
\qquad \det G_N = -117649 = -7^6 .$$

Invariant factors of $G_N$: $1,\ 49,\ 2401$. The last invariant factor is $2401 = 7^4$.

**Statement**: $N$ has no roots at all, so its reflection subgroup is trivial and $N$ is
in particular non-reflective.

### Vinberg's root-length divisibility criterion

The argument rests on a general criterion the paper attributes to Vinberg and states
verbatim as:

> $f(r)$ divides twice the last invariant factor of the Gram matrix.

For $N$ that bound is $2 \cdot 2401 = 4802$. This is what makes "$N$ has no roots" a
*finite* check: only finitely many lengths can occur, and each is excluded in turn.

Among the divisors of $4802 = 2\cdot 7^4$, the paper reduces the candidates to the four
lengths

$$f(r) \in \{49,\ 98,\ 2401,\ 4802\},$$

these being the ones integrally represented by $f$ that survive the local obstructions.

### Excluding $f(r) = 49$

The crystallographic conditions on a root $r$ are

$$2(r, e_i) \in f(r)\,\mathbb{Z}, \qquad i = 1,2,3 .$$

For $f(r) = 49$ they force

$$k_1 = m_1, \qquad k_2 = 7m_2 - 3m_3, \qquad k_3 = 7m_3, \qquad m_1,m_2,m_3 \in \mathbb{Z},$$

whence the rescaled form

$$q(r) = f(r)/49 = 49m_2^2 + 14m_1m_3 - 28m_2m_3 + 6m_3^2 .$$

The paper concludes: "However, $q$ does not integrally represent $1$." Then:
"Analogous arguments exclude the remaining possible roots lengths $98$, $2401$, and
$4802$."

**Derived here, not printed in the paper** — a local obstruction certifying the
non-representation, so that the claim is checkable rather than merely quoted. Reduce
$q$ modulo $7$: the coefficients $49$, $14$ and $28$ all vanish, leaving
$q \equiv 6m_3^2 \pmod 7$. The squares modulo $7$ are $\{0,1,2,4\}$, so
$6m_3^2 \in \{0,6,5,3\}$ and $1$ is not among them. Hence $q$ does not represent $1$
even over $\mathbb{Z}_7$.

## Convention note: signature $(2,1)$ against this repository's convention

The paper prints both forms with signature $(2,1)$. This repository uses the
algebraic-geometry (negative-definite) convention, in which a hyperbolic lattice of
rank $3$ has signature $(1,2)$. The two conventions are related by a twist by $-1$:
the repo-convention lattice is $L(-1)$, whose Gram matrix is $-G_L$ and whose
determinant is $(-1)^3\det G_L = +7^4$. Determinant sign, and only that, changes;
root lengths change sign; the root *set*, the reflection subgroup and reflectivity do
not.

The source data above is stored verbatim in its own $(2,1)$ convention. The catalogue
specimens are the repo-convention twists, and the relation is asserted in the specimen
rows rather than assumed.

## Material retained from the 2025-07-26 extract

The statements below were in the first extract and are **not** re-verified against v4
in this pass. They are kept because the citation index resolves against them; treat
them as pending verification, not as source-checked.

- **Theorem 1**: a finitely generated Zariski dense discrete
  $\Gamma < \mathrm{Isom}(\mathbb{H}^d)$ containing at least one reflection contains a
  discrete Zariski dense subgroup generated by finitely many reflections.
- **Theorem 2**: for $L$ a non-reflective Lorentzian lattice over a totally real number
  field $k$ with $\mathscr{R}(L)$ non-trivial, all $\mathscr{R}_m(L)$ are thin in
  $\mathbf{PO}(L)_{\mathcal{O}_k}$ for sufficiently large $m$.
- **Theorem 3**: every thin hyperbolic reflection group
  $\Lambda < \mathrm{Isom}(\mathbb{H}^d)$ is a subgroup of some
  $\mathscr{R}_m(L) < \mathbf{PO}(L)_{\mathcal{O}_k}$, $m \geq d+1$.
- **Thin**: $\Lambda < \Gamma$ is thin when it is finitely generated, of infinite index,
  and Zariski dense in $\mathbf{G}(\mathbb{R})$.
- **Lorentzian lattice**: a free $\mathcal{O}_k$-module with a scalar product of
  signature $(d,1)$; *reflective* when its maximal reflection subgroup has finite index.
- **Zariski density**: a discrete $\Gamma < \mathrm{Isom}(\mathbb{H}^d)$ is Zariski dense
  exactly when its limit set is not contained in a hypersphere of
  $\partial\mathbb{H}^d$.
- **Vinberg's lemma**: if $\Gamma$ contains reflections then
  $\Gamma = W \rtimes \mathrm{Sym}_\Gamma(\mathscr{P})$, with $W$ the maximal reflection
  subgroup and $\mathscr{P}$ the fundamental Coxeter polyhedron.
- **Diagram type by eigenvalues** (literature convention, i.e. positive-definite):
  all eigenvalues positive → spherical (finite) Coxeter group; all non-negative with at
  least one zero → euclidean (affine); some negative → hyperbolic/indefinite. This
  repository negates, per `PROJECT_CONVENTIONS.md`.

## Where this lands in-tree

- Specimens: `src/dzack_research/preamble/catalogue.sage` —
  `Lattices.BogachevKolpakovNonReflective` (§6.1) and
  `Lattices.BogachevKolpakovWithoutRoots` (§6.2), both in the repo's negative-definite
  convention.
- Specimen rows: `tests/test_known_mathematics.sage`, the
  "Bogachev–Kolpakov ternary Lorentzian lattices" section.
- Vinberg's divisibility criterion: `IntegralLattices.ParentMethods.possible_root_lengths`
  in
  `src/dzack_research/preamble/categories/modules/framed/formed/integrallattice/integral_lattices.sage`,
  beside `reflection`, which is where the root condition already lives.
