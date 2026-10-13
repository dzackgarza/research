# Torsion pairings and linking forms {#sec-torsion-linking-forms}

Let $R$ be a Dedekind domain with fraction field $K$. The general pairing category $\mathbf{Pair}_{R,W}$ and its adjoints are defined in @def:module-pairing and @def:pairing-adjoints.

## Torsion-valued pairings {#sec-torsion-pairings}

::: {.definition #def:torsion-pairing title="Pairings on finite-length modules"}
For $W\in R\text{-}\mathbf{Mod}$, let $\mathcal B_{R,W}^{\mathrm{fl}}$ be the replete full subcategory of the fixed-value bilinear form category $\mathcal B_{R,W}$ of @def:form-categories on objects $(T,b)$ whose module component $T$ has finite length over $R$. No nondegeneracy or symmetry is assumed.

A **torsion linking pairing** is a bilinear form
$$
b\colon T\tensor_RT\longrightarrow K/R
$$
with $T$ of finite length; equivalently, it is an object of $\mathcal B_{R,K/R}^{\mathrm{fl}}$. The left and right adjoints and their complete radical–coradical exact sequences are the restrictions of @def:pairing-adjoints.
:::

::: {.definition #def:torsion-Pontryagin-dual title="The dual of a finite torsion module"}
For a finite-length $R$-module $T$, define the **torsion dual** and its evaluation morphism by
$$
T^\dagger\definedas\Hom_R(T,K/R),
\qquad
\eta_T\colon T\longrightarrow T^{\dagger\dagger}.
$$
The morphism $\eta_T$ is induced by evaluation $T\tensor_RT^\dagger\too K/R$ under the tensor–Hom adjunction of @def:closed-monoidal.
:::

::: {.proposition #prop:torsion-duality-exact title="Exact self-duality of finite torsion modules"}
The contravariant functor $(-)^\dagger$ is exact on the category of finite-length $R$-modules, and $\eta_T$ is an isomorphism for every such $T$. In particular, for a short exact sequence
$$
0\too T_1\too T_2\too T_3\too0
$$
the dual sequence
$$
0\too T_3^\dagger\too T_2^\dagger\too T_1^\dagger\too0
$$
is exact, and $T^\dagger$ has the same finite length as $T$ at each nonzero prime of $R$.
:::

::: {.proof}
The divisible module $K/R$ is injective over the Dedekind domain $R$, so $\Hom_R(-,K/R)$ is exact. Localization decomposes a finite-length module into its primary components. Over the discrete valuation ring $R_{\mathfrak p}$ the dual of $R_{\mathfrak p}/\mathfrak p^e R_{\mathfrak p}$ is $\mathfrak p^{-e}R_{\mathfrak p}/R_{\mathfrak p}$, which has the same length and is isomorphic to the original cyclic module. Evaluation identifies each component with its double dual. These componentwise isomorphisms give the natural biduality isomorphism $\eta_T$.
:::

::: {.proposition #prop:torsion-perfectness title="Nondegenerate linking pairings are perfect"}
Let $b\colon T\tensor_RT\too K/R$ be a symmetric pairing on a finite-length $R$-module $T$, with adjoint
$$
b^\sharp\colon T\longrightarrow T^\dagger.
$$
Then the following are equivalent: $\ker(b^\sharp)=0$; $\operatorname{coker}(b^\sharp)=0$; and $b^\sharp$ is an isomorphism. Hence a symmetric finite torsion linking pairing is nondegenerate exactly when it is perfect.

The complete exact sequence is
$$
0\too\radic(b)\too T\xrightarrow{b^\sharp}T^\dagger
\twoheadrightarrow\operatorname{corad}(b)\too0.
$$
:::

::: {.proof}
The modules $T$ and $T^\dagger$ have identical finite lengths at every prime by @prop:torsion-duality-exact. An injective morphism between them must have zero cokernel, and a surjective morphism must have zero kernel. Symmetry identifies the two adjoints of @def:pairing-adjoints, proving the equivalence with nondegeneracy.
:::

## Discriminant forms as categorical cokernels {#sec-torsion-discriminants}

::: {.theorem #thm:metric-discriminant-perfect-linking title="Metric-dual cokernels give perfect linking pairings"}
Let $L\in\mathbf{Lat}_R^{\mathrm{nd}}$ be a symmetric integral lattice. The metric dual $L^\#=L^{\#R}$ of @def:metric-dual and its embedding $\iota_L\colon L\injects L^\#$ have the finite-length module cokernel sequence
$$
0\too L\xrightarrow{\iota_L}L^\#
\xrightarrow{\pi_L}A_L^\sharp\too0.
$$
The restricted bilinear form on $L^\#$ induces a pairing
$$
\begin{aligned}
\overline\beta_L\colon A_L^\sharp\tensor_R A_L^\sharp
&\longrightarrow K/R,\\
(\pi_L(x),\pi_L(y))&\longmapsto\beta_{L_K}(x,y)+R.
\end{aligned}
$$
This is a perfect symmetric torsion linking pairing. For $R=\bZ$, it is the composite of the bilinear discriminant form $A_L$ of @def:discriminant with the canonical value-module inclusion $W_b(L)\injects\bQ/\bZ$.

The adjective **discriminant** refers to the bilinear form arising from this metric-dual cokernel (and, for quadratic refinements, to the corresponding quadratic discriminant cokernel). It is not a synonym for an arbitrary torsion linking pairing.
:::

::: {.proof}
The formula descends along $\pi_L$ in both entries: $\beta_{L_K}(L,L^\#)\subseteq R$ by the metric-dual pullback. If $x\in L^\#$ pairs integrally with every $y\in L^\#$, then $x\in(L^\#)^\#=L$, so the adjoint of $\overline\beta_L$ has zero kernel. By @prop:torsion-perfectness it is an isomorphism. The value-module comparison for $R=\bZ$ is the universal property of the bilinear-module cokernel of @def:discriminant and the canonical embedding of its value module in $\bQ/\bZ$.
:::

::: {.example #ex:rank-one-discriminant-linking title="The linking form of a rank-one lattice"}
For $R=\bZ$ and the integral rank-one lattice $L=\generators{m}$ with $m>0$, the metric dual is $L^\#=\tfrac1m\bZ$. Its cokernel $A_L^\sharp\isoto\bZ/m\bZ$ has perfect linking pairing
$$
\overline\beta_L(\bar a,\bar b)=\frac{ab}{m}+\bZ
\quad\text{in }\bQ/\bZ.
$$
If $m$ is even, the corresponding quadratic discriminant refinement is $q_L(\bar a)=a^2/m+2\bZ$ in $\bQ/2\bZ$, with its natural value module as in @def:discriminant.
:::
