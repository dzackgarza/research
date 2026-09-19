---
title: Periods, Picard-Fuchs operators, and local monodromy of a one-parameter family
unit: method
status: partial
tags:
  - periods
  - monodromy
  - picard-fuchs
  - hodge-theory
  - method
---

# Periods, Picard--Fuchs operators, and local monodromy of a one-parameter family

**Provenance.** `notes/computations/hypersurface-family-monodromy.md`, migrated 2026-08-20 from the `lattice-research` corpus, together with the two extraction specifications and the method comparison in `notes/computations/extraction-specs/` and `notes/computations/comparisons/`.

\longref{def:kulikov-types} classifies a degeneration by the nilpotency index of $N = \log T$, and \longref{thm:lmhs} reads the boundary stratum off the same operator.
This page records how $T$ and $N$ are computed for an explicit one-parameter family, by two constructions with different hypotheses and different failure modes.

## Periods and the period map

::: {.Definition #def:period-map}
### Period matrix and period map

Let $\pi \colon \mathcal{X} \to M$ be a smooth projective (or compact Kähler) family of complex $m$-dimensional varieties over a connected complex quasi-projective variety (or complex manifold) $M$.
Fix a reference fiber $X = X_{t_0} = \pi^{-1}(t_0)$, and let $\{\Sigma_0, \dots, \Sigma_{k-1}\} \subset H_m(X, \mathbb{Z})/\mathrm{tors}$ be an integral basis of the middle homology modulo torsion, where $k = b_m(X)$ is the middle Betti number.
For each $t \in M$, let $\{\omega_1(t), \dots, \omega_p(t)\}$ be a basis of a holomorphic subbundle of the relative de Rham cohomology, such as $H^{m,0}(X_t) \subset H^m_{\mathrm{dR}}(X_t)$ where $p = h^{m,0}(X)$, varying holomorphically with $t$.

1. **The general period matrix and period map:**
   The *period matrix* of the fiber $X_t$ with respect to the chosen bases is the $p \times k$ matrix of period integrals
   $$
   \Pi(t) \;\coloneqq\; \begin{pmatrix}
   \displaystyle\int_{\Sigma_0(t)} \omega_1(t) & \cdots & \displaystyle\int_{\Sigma_{k-1}(t)} \omega_1(t) \\
   \vdots & \ddots & \vdots \\
   \displaystyle\int_{\Sigma_0(t)} \omega_p(t) & \cdots & \displaystyle\int_{\Sigma_{k-1}(t)} \omega_p(t)
   \end{pmatrix}
   \;\in\; \operatorname{Mat}_{p \times k}(\mathbb{C}).
   $$
   Because the basis of holomorphic forms is determined only up to an invertible change of basis in $\operatorname{GL}_p(\mathbb{C})$, the $p$-dimensional subspace spanned by the rows of $\Pi(t)$ defines a point in the Grassmannian $\operatorname{Gr}(p, H^m(X, \mathbb{C}))$, or more precisely in the Griffiths period domain $\mathcal{D} \subset \operatorname{Gr}(p, k)$ cut out by the Riemann–Hodge bilinear relations.
   Modulo the global monodromy group $\Gamma \le \operatorname{Aut}(H_m(X, \mathbb{Z}), Q)$, this association defines the *period map* of the family
   $$
   \mathcal{P} \colon M \longrightarrow \mathcal{D}/\Gamma.
   $$

2. **Specialization to the one-form case ($p = 1$, Calabi–Yau varieties):**
   When $X$ is a smooth $m$-dimensional Calabi–Yau variety (such as an elliptic curve with $m=1$, a K3 surface with $m=2$, or a Calabi–Yau threefold with $m=3$), the space of holomorphic top forms is one-dimensional: $h^{m,0}(X) = 1$.
   There is therefore a unique (up to scaling) non-vanishing holomorphic $m$-form $\Omega \in H^{m,0}(X)$.
   In this setting, there is exactly one form to integrate ($p = 1$), and the general period matrix specializes to a single row vector of $k = b_m$ period integrals $\omega_0, \dots, \omega_{k-1}$, given by
   $$
   \omega_i \;=\; \int_{\Sigma_i} \Omega \qquad (i = 0, \dots, k-1).
   $$
   Since $\Omega$ is determined up to an arbitrary non-zero constant $\lambda \in \mathbb{C}^\times$, the period integrals are determined up to scalar multiplication, and their totality defines a well-defined point $P_X$ in projective space $\mathbb{P}^{k-1}(\mathbb{C})$:
   $$
   P_X \;=\; [\omega_0 : \dots : \omega_{k-1}] \;\in\; \mathbb{P}^{k-1}.
   $$
   When $X = X_t = \pi^{-1}(t)$ varies in a family $\pi \colon \mathcal{X} \to M$, with $\pi$ determining a locally topologically trivial fibration over a complex quasi-projective variety $M$ and $t \in M$, the association $t \mapsto P_{X_t}$ extends to a holomorphic map
   $$
   \omega \colon M \longrightarrow \mathbb{P}^{k-1}, \qquad t \longmapsto P_{X_t} = [\omega_0(t) : \dots : \omega_{k-1}(t)],
   $$
   called the *projective period map* of the family.
:::

## The algebraic construction

::: {.Construction #cons:pf-from-jacobian}
### From the defining polynomial to the local monodromy

Let $k$ have characteristic $0$ and let $f\in k[x_0,\dots,x_{n-1},t]$ present a family of affine hypersurfaces over a one-dimensional base with parameter $t$.

1. Form the Jacobian ideal $J = \left(\partial f/\partial x_0,\dots,\partial f/\partial x_{n-1}\right)$ in $k(t)[x_0,\dots,x_{n-1}]$ and a monomial basis $B$ of the Milnor algebra $k(t)[x]/J$.
   Then $\mu = \lvert B\rvert$ is the Milnor number of the generic fiber, the base field being $k(t)$.

2. On the Brieskorn module of $f$, take the Gauss--Manin connection, and apply it to the form
   $$
   P \;=\; (-1)^{n-1}\,\frac{\partial_t f}{t}\Bigl(\sum_{b\in B} b\Bigr)
   $$
   with cycle vector $e = [1]$.

3. The result is the Picard--Fuchs operator
   $$
   \mathcal L \;=\; \sum_{i=0}^{\mu} c_i(t)\, D_t^{\,i}
   \;\in\; k[t]\langle D_t\rangle ,
   $$
   of order $\mu$, with each $c_i$ a polynomial in $t$ alone.

4. Compute the indicial polynomial of $\mathcal L$ at $t = 0$.
   Its roots are the exponents $\alpha_1,\dots,\alpha_\mu$.
   Its degree equals $\mu$ exactly when $t = 0$ is a regular singular point, so checking that degree is checking the hypothesis under which the remaining steps are valid.

5. Let $R$ be the Jordan form over $\overline{\QQ}$ of the companion matrix of the monic indicial polynomial, and let $R = R_s + R_n$ be its Jordan decomposition into commuting semisimple and nilpotent parts.

6. The local monodromy at $t = 0$ is
   $$
   T \;=\; \exp(2\pi i R) \;=\; \exp(2\pi i R_s)\,\exp(2\pi i R_n),
   \qquad
   \exp(2\pi i R_s) = \operatorname{diag}\!\left(e^{2\pi i\alpha_j}\right),
   $$
   the second factor a finite sum since $R_n$ is nilpotent.
   This is the multiplicative Jordan decomposition of $T$: the first factor is its semisimple part, the second its unipotent part.
:::

::: {.Remark}
### The relation to the log monodromy

$T$ is unipotent exactly when $R_s = 0$, and in that case
$$
N \;=\; \log T \;=\; 2\pi i\, R_n ,
$$
so the nilpotency index of the operator $N$ of \longref{def:kulikov-types} is the nilpotency index of the residue matrix $R_n$, and the Jordan block sizes of $T$ are those of $R$.
Verifying $R_s = 0$ is therefore the unipotency check that \longref{def:kulikov-types} presupposes, carried out algebraically on the indicial polynomial.
:::

::: {.Warning}
### Jordan block sizes come from the decomposition data

The block sizes are part of the Jordan decomposition of step 5, and are the values to use.
Recovering them instead by scanning the superdiagonal of a computed Jordan form is correct only for one normalization of that form, and mis-segments a differently normalized one.
:::

## The Legendre specimen

::: {.Example #ex:legendre-monodromy}
### The Legendre family

For $y^2 = x(x-1)(x-t)$, presented in $k[x,y,t]$ with weights $(2,3,1)$ and the weighted degree-reverse-lexicographic order, \longref{cons:pf-from-jacobian} returns
$$
\mu = 2,
$$
a Picard--Fuchs operator of order $2$ whose coefficient list begins
$$
-3t+3,\qquad 12t^2+8t-4,\qquad 12t^3-8t^2-4t,
$$
indicial polynomial $-4\alpha^2$ at $t = 0$, hence a double exponent $\alpha = 0$; nilpotent part with Jordan form $\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}$; and
$$
T \;=\; \begin{pmatrix} 1 & 2\pi i \\ 0 & 1\end{pmatrix},
$$
a single Jordan block, so $T$ is unipotent with $N\neq 0$ and $N^2 = 0$.
:::

::: {.Remark}
### What the recorded values assert

The coefficient list depends on the choice of the form $P$ and of the monomial basis $B$, so it is a statement about this normalization of \longref{cons:pf-from-jacobian}.
The indicial polynomial is determined up to a scalar by the same choices; its mathematical content is the pair of roots, a double exponent $0$.
The entry $2\pi i$ shows that $T$ is written in a period basis of the relevant cohomology and not in an integral basis of the homology of the fiber, so the values above are not comparisons against the Picard--Lefschetz statement for a nodal degeneration.
The sources identified as those that would ground each assertion are [@Mov21] for the explicit Picard--Fuchs matrix and the Gauss--Manin basis, [@Gri69] for the regular-singularity statement, and SGA 7, Exposé XV for the monodromy in an integral basis; the values above stand against none of them.
:::

::: {.Remark}
### The invariant that survives the change of basis

The Jordan type of a matrix is invariant under conjugation, so the nilpotency index of $N$, and hence the Kulikov type of \longref{def:kulikov-types}, is unaffected by which basis of the fiber cohomology the monodromy is written in.
What is missing for the recorded output to determine that type is the comparison identifying the period basis with a basis of the integral local system; the numerical values of the entries have no meaning without it, and the block structure has meaning as soon as it is established.
:::

## The topological construction

::: {.Construction #cons:lefschetz-periods}
### Periods from a Lefschetz pencil

For a smooth projective hypersurface $X$, an iterated Lefschetz pencil $X\dashrightarrow\PP^1$ has critical values the roots of the discriminant of the pencil.
At each critical value there is a vanishing cycle $\delta_i\in H_{n-1}(X_b)$ in the homology of a nearby fiber, and a thimble $\Delta_i\in H_n(Y,Y_b)$ with $\partial\Delta_i = \delta_i$.
Integrating a basis of rational differential forms over the thimbles gives the period matrix; a homology modification corrects $H_n(Y)$ to $H_n(X)$ across the blow-up.
The monodromy around a critical value is the Picard--Lefschetz twist along the corresponding vanishing cycle, and continuing the periods numerically around each critical value returns the monodromy matrices on $H_{n-1}(X_b)$ in an explicit homology basis.
:::

::: {.Remark}
### What each construction delivers

\longref{cons:pf-from-jacobian} is exact and produces the Gauss--Manin connection matrix, the Picard--Fuchs operator, Hodge numbers and the Hodge filtration through graded Jacobian-ring data, and period vectors and Hodge loci for special families.
It applies where the Jacobian-ring reduction terminates.

\longref{cons:lefschetz-periods} is numerical with interval-arithmetic error bounds, and produces an explicit homology basis, the intersection product on it, integral monodromy matrices, and the period matrix; it does not produce the Gauss--Manin connection, the Hodge filtration, or Hodge loci.
It applies to arbitrary smooth hypersurfaces, to elliptic surfaces over $\PP^1$ together with their Mordell--Weil and Néron--Severi lattices, to double covers of $\PP^2$ branched along a sextic, and to fiber products of elliptic surfaces.

The two compute the same objects; the exact construction gives structure and the numerical one gives an integral basis, which is the datum the previous remark identifies as missing.
:::

::: {.Remark}
### Reduction of rational forms and annihilators

Both constructions rest on the reduction of a rational differential form modulo exact forms and the Jacobian ideal, the algorithmic form of Griffiths' residue calculus [@Gri69].
The same reduction, applied to a rational function of several variables with a distinguished parameter, produces an annihilating differential operator for its periods, and the generating function of the constant terms of the Laurent powers of a rational function and the diagonal of a rational function are transformed into period problems and answered by the same reduction.
Exact linear algebra over $\QQ(t)$ in that reduction is carried out by computing over finite fields and reconstructing the rational functions and operator coefficients in characteristic zero.
:::

## What is and is not computed

::: {.Remark}
### The three levels

For a pure Hodge structure on a fixed smooth hypersurface, computing means producing a basis of de Rham cohomology, grading it by Hodge level, computing Hodge numbers, computing periods against chosen cycles, computing the intersection form, and identifying Hodge classes in middle cohomology.

For a variation of Hodge structure, it means the Gauss--Manin connection matrices, the Picard--Fuchs operators, the period vectors or their Taylor expansions, and the local monodromy data near singular fibers.

For a degeneration, it means the de Rham, Gauss--Manin and Picard--Fuchs data for the explicit family, the local monodromy and the nilpotent part in the one-parameter case, and the material for experiments toward a limiting Hodge structure.
The limiting mixed Hodge structure of an arbitrary degeneration, the nearby- and vanishing-cycle formalism in general, mixed Hodge structures of arbitrary singular varieties, and cycle classes of arbitrary subvarieties are outside what these two constructions supply.
:::

## Where this meets the Coble program

::: {.Remark}
### The K3 cover as a double cover

The K3 cover of a Coble surface is the double cover of $\PP^2$ branched along the rational sextic $C$, with equation $w^2 = F(x,y,z)$ in $\PP(1,1,1,3)$ ([[open-problems]]).
Double covers of $\PP^2$ branched along a sextic are one of the classes \longref{cons:lefschetz-periods} handles directly, so a worked instance of $F$ is the entire input its periods and monodromy require, and the open problem asking for such an instance is what stands between this program and a period computation for its own surfaces.
:::

::: {.Remark}
### The object the construction is a functor out of

The datum \longref{cons:pf-from-jacobian} consumes is a family $X\to S$ over a one-dimensional base together with a point of $S$, and the datum it produces is variation of Hodge structure data: a Gauss--Manin connection, a Picard--Fuchs $D$-module, and a limit mixed Hodge structure at the chosen point.
Stated at that level the local monodromy is a question asked of the connection at a point of $S$, with the multiplicative Jordan decomposition read from the connection data.
:::

Related: [[kulikov-models]], [[open-problems]], [[computational-toolchain-and-recipe]].
