# Kulikov models and limiting mixed Hodge structures {#sec-kulikov-models}

## Kulikov degenerations

::: {.definition #def:kulikov-model title="Kulikov models"}

A *Kulikov model* is a degeneration $\mcx \to \Delta$ of K3 surfaces where:

1. The total space $\mcx$ is regular (smooth as a threefold).

2. The central fiber $\mcx_0$ is a reduced simple normal crossings (snc) divisor.

3. The relative dualizing sheaf is trivial: $\omega_{\mcx/\Delta} \cong \OO_{\mcx}$.

Such a model is *semistable* by conditions (1) and (2) and *$K$-trivial* by condition (3).
:::

::: {.theorem #thm:kulikov-existence title="Existence of $K$-trivial semistable modifications"}

Let $\pi\colon X\to\Delta$ be a proper flat morphism from a complex manifold $X$ of dimension $3$ to the unit disc, with nonsingular fibers $X_t$ for $t\neq 0$.

1. Assume that $\pi$ is projective, that the general fiber is a K3 surface ($m = 1$) or an Enriques surface ($m = 2$), and that $X_0 = V_1 + \cdots + V_n$ is a normal crossings divisor whose components $V_i$ are smooth and of multiplicity $1$.
   Then $\pi$ has a modification $\pi_1\colon X'\to\Delta$ such that $X_0'$ is a normal crossings divisor with smooth components of multiplicity $1$ and $mK_{X'}$ is trivial [@Kul77, Thm. I].

2. Assume that every component of $X_0$ has multiplicity $1$, that $X_0$ has local normal crossings, that $K_{X_t}$ is trivial for $t\neq0$, and that every component of $X_0$ is algebraic.
   Then $\pi$ has a modification $\pi'\colon X'\to\Delta$ such that every component of $X_0'$ has multiplicity $1$, $X_0'$ has local normal crossings, and $K_{X'}$ is trivial [@PP81, Theorem].

Here a modification of $\pi$ is a degeneration $\pi'\colon X'\to\Delta$ with a bimeromorphic map $X \dashrightarrow X'$ over $\Delta$ that is biholomorphic away from $X_0$ and $X_0'$.
:::

::: {.definition #def:kulikov-types title="Type I, II, III Kulikov degenerations"}

Let $T$ be the unipotent Picard--Lefschetz monodromy of a Kulikov model and let $N = \log T$ be the associated *log monodromy* operator, a nilpotent endomorphism.
Depending on the nilpotency index of $N$, Kulikov models are classified into three types [@Kul77, Thm. II]:

- **Type $\latI$** ($N = 0$): $\mcx_0$ is a smooth K3 surface.

- **Type $\latII$** ($N^2 = 0$, $N \neq 0$): $\mcx_0 = V_1 + \cdots + V_n$ is a chain of surfaces glued along elliptic curves $V_i\cap V_{i+1}$.
  The ends $V_1$ and $V_n$ are rational surfaces and $V_2, \dots, V_{n-1}$ are elliptic ruled surfaces.
  The dual complex is an interval.

- **Type $\mathrm{III}$** ($N^3 = 0$, $N^2 \neq 0$): $\mcx_0$ is a union of rational surfaces glued along rational curves, forming an anticanonical cycle on each component.
  The dual complex is a triangulation of the sphere $S^2$; with the integral affine structure of @def:singular_ias it is an $\ias$.
:::

## The monodromy weight filtration

::: {.proposition #prop:weight-filtration-by-type title="The weight filtration by type"}

Let $\mcx\to\Delta$ be a Kulikov model, let $V = H^2(\mcx_t;\QQ)$ for $t\neq 0$, and let $N = \log T$.
There is a unique filtration $0\subseteq W_0\subseteq W_1\subseteq\cdots\subseteq W_4 = V$ with $N(W_l)\subseteq W_{l-2}$ such that $N^l\colon\Gr^W_{2+l}\to\Gr^W_{2-l}$ is an isomorphism for each $l\geq0$ [@Sch73, Lemma 6.4].
It is the following filtration.

1. Type $\latI$: $W_1 = 0$ and $W_2 = V$, so $\Gr^W_2 = V$ is the only non-trivial graded piece.

2. Type $\latII$: $W_0 = 0$, $W_1 = \operatorname{Im}N$, $W_2 = \operatorname{Ker}N$ and $W_3 = V$.
   The non-trivial graded pieces are $\Gr^W_1$, $\Gr^W_2$ and $\Gr^W_3$, and $\Gr^W_0 = \Gr^W_4 = 0$.

3. Type $\mathrm{III}$: $W_0 = W_1 = \operatorname{Im}N^2$ has dimension $1$, and $W_2 = W_3 = \operatorname{Ker}N^2 = W_0^{\perp}$ [@FS86, Sec. 1].
   The non-trivial graded pieces are $\Gr^W_0$, $\Gr^W_2$ and $\Gr^W_4$, of dimensions $1$, $20$ and $1$, and $\Gr^W_1 = \Gr^W_3 = 0$.
:::

::: {.proof}

Each listed filtration satisfies the two conditions of [@Sch73, Lemma 6.4], so it is the unique one.

Type $\latI$: $N = 0$, and the graded pieces $\Gr^W_{2\pm l}$ vanish for $l\geq1$.

Type $\latII$: $N^2 = 0$ gives $\operatorname{Im}N\subseteq\operatorname{Ker}N$, so the spaces form a filtration.
Then $N(W_3) = W_1$ and $N(W_2) = 0$.
The map $N\colon V/\operatorname{Ker}N\to\operatorname{Im}N$ is an isomorphism, and $\Gr^W_0 = \Gr^W_4 = 0$.
Since $N\neq0$, $\Gr^W_1 = \operatorname{Im}N\neq0$, and so $\Gr^W_3\cong\Gr^W_1\neq0$.
The operator $N$ is skew-symmetric for the cup product, because it is the logarithm of the isometry $T$ [@FS86, Sec. 1].
So $(Nx\cdot Ny) = -(x\cdot N^2y) = 0$ for all $x, y$, and $\operatorname{Im}N$ is totally isotropic.
By @prop:k3-lattice the cup product on $V\tensor\RR$ has signature $(3,19)$, so a totally isotropic subspace has dimension at most $3$.
Thus $\dim\Gr^W_2 = \dim\operatorname{Ker}N - \dim\operatorname{Im}N = 22 - 2\dim\operatorname{Im}N\geq16$.

Type $\mathrm{III}$: $\dim W_0 = 1$ and $W_2 = W_0^\perp$ has dimension $21$, so $\Gr^W_0$, $\Gr^W_2$ and $\Gr^W_4$ have dimensions $1$, $20$ and $1$.
:::

::: {.theorem #thm:lmhs title="Limiting mixed Hodge structure and degenerations"}

For a one-parameter degeneration of polarized K3 surfaces over a punctured disk, the unipotent monodromy operator $T \in \Orth(T_{2d})$ and its nilpotent logarithm $N = \log T$ induce a canonical monodromy weight filtration $W^{\bullet}$.

The boundary components of $\bbcpt{\ftd}$ are classified by the nilpotency index of $N$:

- **Type $\latII$ degenerations (1-cusps)**: $N \neq 0$, $N^2 = 0$.
  The weight filtration is 3-step ($W_0 \subset W_1 \subset W_2 \subset W_3$), and $\Gr_2^W = I^\perp / I = \overline{T}_I$ has a pure polarized Hodge structure of weight 2.

- **Type $\mathrm{III}$ degenerations (0-cusps)**: $N^2 \neq 0$, $N^3 = 0$.
  The weight filtration is of maximal length.
  These correspond to normal crossing varieties whose dual complex is a triangulation of $S^2$.
:::

::: {.proof}

The construction of the limiting mixed Hodge structure is the nilpotent orbit theorem together with the Clemens-Schmid sequence [@Sch73; @Cle77], and the relation between the nilpotency index of $N$ and the type of the degeneration is Kulikov's classification [@Kul77, Thm. II; @PP81].

For a degeneration of type II the monodromy is unipotent with $N\neq0$, $N^2=0$, so the weight filtration has the three steps $0\subset W_1\subset W_2\subset W_3$ with $\Gr^W_i=0$ otherwise; the primitive part of $H^2$ contributing to $\Gr^W_2$ is annihilated by $N$ and by its transpose, hence is the orthogonal complement of the isotropic subspace $I$ of the special fibre, quotiented by $I$ itself, which is $\overline{T}_I$ of the boundary lattice.
So the pure Hodge structure of weight $2$ on $\Gr^W_2$ is the one on $\overline{T}_I$, and by @def:signature its signature is $(2-k,n-k)$ for $\rank I=k$.
For type III the index is $3$ and the weight filtration has the maximal length (@prop:weight-filtration-by-type).
The dual complex of the central fibre is a triangulation of $S^2$ [@Kul77, Thm. II].
:::
