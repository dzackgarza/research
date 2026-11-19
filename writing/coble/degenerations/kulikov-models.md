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

1. Assume that $\pi$ is projective, that the general fiber is a K3 surface ($m = 1$) or an Enriques surface (@def:enriques-surface) ($m = 2$), and that $X_0 = V_1 + \cdots + V_n$ is a normal crossings divisor whose components $V_i$ are smooth and of multiplicity $1$.
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

## Anticanonical components and the dual complex

::: {.example #ex:tetrahedral-quartic-degeneration title="A tetrahedral quartic degeneration"}

Consider the pencil in $\PP^3\times\Delta$ given by
$$
x_0x_1x_2x_3=t(x_0^4+x_1^4+x_2^4+x_3^4).
$$
For $t=0$ the fiber is the union of the four coordinate planes, with tetrahedral dual complex. The total space is singular at the points where two coordinates vanish and the sum of the fourth powers of the other two vanishes. Each of the six coordinate lines contains four such points, giving $24$ ordinary double points. At one of these points, two vanishing coordinates and a local coordinate for the residual quartic put the equation in the node form $uv=tw$ to first order. A choice of small resolutions yields a smooth semistable model; different choices can be related by flops. With a symmetric distribution of the resolutions, each plane component is blown up at six points, two on each of its three boundary lines. Its dual complex remains the tetrahedron, while the anticanonical components acquire the blowups needed for the triple-point formula. This example is a degree-four K3 degeneration and illustrates the Type III geometry independently of the degree-two construction in @cons:degree-two-k3-affine-sphere.
:::

![The four planes $H_i$ give the vertices of the tetrahedral dual complex; their pairwise lines $L_{ij}$ give its edges and their triple points give its triangular faces.](/rendered/dual_complex.jpg){#fig-tetrahedral-quartic-dual-complex}

For a proper variety $X$ and an effective $\QQ$-divisor $D$, a *log Calabi–Yau pair* has log canonical singularities and $K_X+D\sim_{\QQ}0$ [@KX16, Introduction]. If a $K$-trivial degeneration has a dlt pair $(\mcx,\mcx_0)$, adjunction gives $K_{V_i}+D_i\sim_{\QQ}0$ on the normalization of each central-fiber component $V_i$, where $D_i$ is its conductor. Thus the anticanonical pairs below are the surface components of a log Calabi–Yau degeneration. The definition of a Kulikov model above is the smooth-total-space, normal-crossings case.

The dimension of the dual complex distinguishes the three Kulikov types: it is $0$ in Type I, $1$ in Type II, and $2$ in Type III. In particular, only Type III has the maximal-dimensional dual complex $S^2$. For a simply connected strict Calabi–Yau general fiber of dimension $n$, Kollár and Xu call a dlt Calabi–Yau degeneration *maximal* when its dual complex has dimension $n$; they prove that this dual complex is a simply connected rational homology sphere and is homeomorphic to $S^n$ for $n\leq3$, as well as for $n=4$ with simple normal crossings central fiber [@KX16, §4, Question 7 and Proposition 8]. Their question asks whether the sphere conclusion holds in general. The proposed mirror-symmetry relation is that this dual complex supplies the base of a limiting torus fibration, whose dual torus fibration produces a mirror; the integral affine structures and their discrete Legendre transform make that relation more precise [@GS03]. This relation is a mirror-symmetry proposal, rather than an identification supplied by the Kulikov classification.

::: {.proposition #prop:kulikov-ias-gluing title="Integral affine gluing from a Type III central fiber"}

Let $\mcx_0=\Union_iV_i$ be a $d$-semistable Type III Kulikov surface, and let $D_i=\Sum_jD_{ij}$ be the cycle of double curves on $V_i$. The dual complex is assembled from the pseudofans of the anticanonical pairs (@def:anticanonical-pair) $(V_i,D_i)$. Each face is a unit lattice triangle. For consecutive primitive edge vectors $e_{i,j-1},e_{ij},e_{i,j+1}$ in the star of the vertex of $V_i$, the integral affine gluing rule is
$$
e_{i,j-1}+e_{i,j+1}=-D_{ij}^{2}e_{ij}.
$$
The structure extends across the vertex exactly when $Q(V_i,D_i)=0$, equivalently when $(V_i,D_i)$ is toric [@AE22, §6.2].
:::

::: {.proof}

The displayed relation fixes the transition between adjacent unit triangles. In the simple normal crossings Kulikov model, each $D_{ij}$ is a smooth rational curve. The relations from its two sides agree precisely when the triple point formula $D_{ij}^2+D_{ji}^2=-2$ holds [@AE22, §6.2, citing Engel, Prop. 2.2]. At a vertex, the pseudofan is a toric fan precisely when the anticanonical pair has charge zero by @prop:charge-under-blowup. Thus positive charge is the obstruction to extending the affine chart over that vertex [@AE22, §6.2].
:::

For a general anticanonical pseudofan with an irreducible nodal rational boundary component $D_j$, the local coefficient is $-D_j^2+2$ rather than $-D_j^2$ [@AE22, §6.2]. The proposition applies to the smooth double curves of a simple normal crossings Kulikov central fiber. The more general double-curve relation is $D_{ij}^2+D_{ji}^2=-2+2g$ for arithmetic genus $g$ [@AE23, Prop. 3.3].

The triangulation specifies which component pairs meet along double curves and which triples meet at triple points. It does not select the gluing isomorphisms or a smoothing: for a fixed triangulated sphere, the $d$-semistable central fibers form a torus described in [@AE22, §6.2].

The *intersection complex* draws a polygonal tile for each component $V_i$ and labels its sides by the double curves $D_{ij}$. Its dual cellulation places a vertex at each $V_i$, an edge at each $D_{ij}$, and a triangle at each triple point. The latter is the dual complex $\Gamma(X_0)$ used above. Its vertex stars are the pseudofans of the anticanonical pairs, so dualizing the tile picture explains the gluing rule [@AE22, §6.2].

At a positive-charge vertex the pseudofan needs a monodromy direction in addition to the visible edges. Two adjacent vertices give components that meet along the curve represented by their common edge. A triangle records a triple point [@AE22, §6.2].

![The monodromy direction at a singular vertex of a pseudofan.](/rendered/IASmonodromy.jpg){#fig-kulikov-monodromy-direction}

![Stars of two adjacent vertices, giving surfaces glued along one double curve.](/rendered/IASgluing.jpg){#fig-kulikov-adjacent-stars}

::: {.definition #def:d-semistability title="$d$-semistability of a Type III surface"}

For a normal crossings Type III surface $X_0$, its infinitesimal smoothing sheaf is
$$
T^1_{X_0}=\mathcal{E}xt^1_{\OO_{X_0}}(\Omega^1_{X_0},\OO_{X_0}),
$$
an invertible sheaf on the double locus $(X_0)_{\mathrm{sing}}$. The surface is *$d$-semistable* if $T^1_{X_0}\simeq\OO_{(X_0)_{\mathrm{sing}}}$ [@AET23, §2A].
:::

::: {.theorem #thm:type-iii-d-semistable-smoothing title="Smoothing a Type III surface"}

A Type III normal crossings K3 surface is smoothable to a K3 surface if and only if it is $d$-semistable [@Fri83a; @AET23, §2A].
:::

::: {.proof}

This is Friedman's smoothing theorem as stated in [@AET23, §2A]. The condition on $T^1_{X_0}$ constrains the component deformations and the gluing isomorphisms, which are extra data beyond the triangulated dual complex.
:::

::: {.proposition #prop:type-iii-monodromy-triple-points title="Monodromy and triple points"}

For a Type III Kulikov degeneration, there are classes $\delta,\lambda\in H^2(X_t,\ZZ)$ with $\delta$ primitive, $\delta^2=\delta\cdot\lambda=0$, such that
$$
Nx=(x\cdot\delta)\lambda-(x\cdot\lambda)\delta,
\qquad \lambda^2=\#\{\text{triple points of }X_0\}.
$$
Here $N=\log T$ is the log monodromy [@FS86; @AET23, §2A].
:::

::: {.proof}

This is the Picard–Lefschetz and triple-point formula of [@FS86, Lem. 1.1 and Prop. 7.1], as quoted in [@AET23, §2A].
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
The operator $N$ is skew-symmetric for the cup product, because it is the logarithm of the isometry $T$ [@FS86, proof of Lem. 1.1].
So $(Nx\cdot Ny) = -(x\cdot N^2y) = 0$ for all $x, y$, and $\operatorname{Im}N$ is totally isotropic.
By @prop:k3-lattice the cup product on $V\tensor\RR$ has signature $(3,19)$, so a totally isotropic subspace has dimension at most $3$.
Thus $\dim\Gr^W_2 = \dim\operatorname{Ker}N - \dim\operatorname{Im}N = 22 - 2\dim\operatorname{Im}N\geq16$.

Type $\mathrm{III}$: $\dim W_0 = 1$ and $W_2 = W_0^\perp$ has dimension $21$, so $\Gr^W_0$, $\Gr^W_2$ and $\Gr^W_4$ have dimensions $1$, $20$ and $1$.
:::

::: {.theorem #thm:lmhs title="Limiting mixed Hodge structure and degenerations"}

For a one-parameter degeneration of polarized K3 surfaces over a punctured disk, the unipotent monodromy operator $T \in \Orth(T_{2d})$ and its nilpotent logarithm $N = \log T$ induce a canonical monodromy weight filtration $W^{\bullet}$.

The [boundary components]{.other-sense} of $\bbcpt{\ftd}$ are classified by the nilpotency index of $N$:

- **Type $\latII$ degenerations (1-cusps)**: $N \neq 0$, $N^2 = 0$.
  The weight filtration is 3-step ($W_0 \subset W_1 \subset W_2 \subset W_3$), and $\Gr_2^W = I^\perp / I = \overline{T}_I$ has a pure polarized Hodge structure of weight 2.

- **Type $\mathrm{III}$ degenerations (0-cusps)**: $N^2 \neq 0$, $N^3 = 0$.
  The weight filtration is of maximal length.
  These correspond to normal crossing varieties whose dual complex is a triangulation of $S^2$.
:::

::: {.proof}

The construction of the limiting mixed Hodge structure is the nilpotent orbit theorem together with the Clemens-Schmid sequence [@Sch73, Thm. 4.9; @Cle77], and the relation between the nilpotency index of $N$ and the type of the degeneration is Kulikov's classification [@Kul77, Thm. II; @PP81].

For a degeneration of type II the monodromy is unipotent with $N\neq0$, $N^2=0$, so the weight filtration has the three steps $0\subset W_1\subset W_2\subset W_3$ with $\Gr^W_i=0$ otherwise; the primitive part of $H^2$ contributing to $\Gr^W_2$ is annihilated by $N$ and by its transpose, hence is the orthogonal complement of the isotropic subspace $I$ of the special fibre, quotiented by $I$ itself, which is $\overline{T}_I$ of the boundary lattice.
So the pure Hodge structure of weight $2$ on $\Gr^W_2$ is the one on $\overline{T}_I$, and by @def:signature its signature is $(2-k,n-k)$ for $\rank I=k$.
For type III the index is $3$ and the weight filtration has the maximal length (@prop:weight-filtration-by-type).
The dual complex of the central fibre is a triangulation of $S^2$ [@Kul77, Thm. II].
:::
