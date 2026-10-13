# Automorphism lifting through a gluing {#sec:automorphism-lifting}


## The discriminant representation

::: {.notation #not:discriminant-representation title="Notation for discriminant actions"}

Let $\rho_L\colon\Orth(L)\too\Orth(A_L)$ be the bilinear discriminant representation of @def:discriminant-rep.
For $\varphi\in\Orth(L)$ write $\bar{\varphi}\definedas\rho_L(\varphi)$.
If $L$ is even, write $\bar{\varphi}_q\definedas\rho_{L,q}(\varphi)\in\Orth(A_{L,q})$.
:::


## The lifting criterion

::: {.definition #def:gluing-datum-of-a-pair title="The gluing datum of a pair of primitive inclusions"}

Let $\iota_M\colon M\injects L$ and $\iota_N\colon N\injects L$ be primitive embeddings with
$\iota_N(N)=\iota_M(M)^{\perp L}$.
Set $j\definedas\iota_M\perp\iota_N\colon M\perp N\injects L$. Its module-component cokernel sequence in $\bZ\text{-}\mathbf{Mod}$ is
$$
0\too M\oplus N\xrightarrow{U_{\mathrm{mod}}(j)}L\xrightarrow{c}H\too0.
$$
The cokernel morphism
$\pi_{M\perp N}\colon(M\perp N)^\#\twoheadrightarrow A_{M\perp N}^\sharp$
of @def:metric-dual induces
$h\colon(H,0)\injects A_{M\perp N}$
in $\mathbf{BilMod}_{\bZ}$, characterized by
```tikzcd
L \arrow[r] \arrow[d,two heads,"c"'] & (M\perp N)^\# \arrow[d,two heads,"\pi_{M\perp N}"] \\
H \arrow[r,hook,"U_{\mathrm{mod}}(h)"'] & A_{M\perp N}^\sharp
```
The gluing datum is the isotropic subobject $h$ of $A_{M\perp N}$, whose value module is $W_b(M\perp N)$ of @def:discriminant. Its canonical common-value description in terms of $A_M$ and $A_N$ is @prop:discriminant-orthogonal-sum.

If $L,M,N$ are even, $h$ refines to
$h_q\colon(H,0)\injects A_{M\perp N,q}$
by @thm:nikulin-gluing.
Equivalently, $h$ is the graph subobject of an isometry
$\gamma\colon H_M\isoto H_N(-1)$
between subobjects $H_M\injects A_M$ and $H_N\injects A_N$.
In the even case, $\gamma$ refines to an isometry of the induced quadratic subobjects after the $(-1)$-twist.
:::

::: {.theorem #thm:automorphism-lifting-criterion title="When a pair of isometries lifts"}

Let $L$, $M$, $N$ and $h\colon(H,0)\injects A_{M\perp N}$ be as in @def:gluing-datum-of-a-pair, and let
$\varphi_M\in\Orth(M)$ and $\varphi_N\in\Orth(N)$.
Put $\psi\definedas\varphi_M\perp\varphi_N$ and $\bar\psi\definedas\rho_{M\perp N}(\psi)\in\Orth(A_{M\perp N})$.
Then $\psi$ extends to an isometry of $L$ if and only if there exists
$u\in\Aut_{\bZ\text{-}\mathbf{Mod}}(H)$ for which the following square commutes:

```tikzcd
H \arrow[r,"u"] \arrow[d,"h"'] & H \arrow[d,"h"] \\
A_{M\perp N} \arrow[r,"\bar\psi"'] & A_{M\perp N}
```

The extension is then unique and restricts to $\varphi_M$ on $M$ and to $\varphi_N$ on $N$.
:::

::: {.proof}

Write $\psi\in\Orth(M\perp N)$ as in the statement.
After scalar extension, $\psi_\QQ\colon(M\oplus N)_\QQ\isoto(M\oplus N)_\QQ$ is an isometry and therefore acts on $(M\oplus N)^\#$.
Because $j(M\oplus N)$ spans $L_\QQ$, any isometry of $L$ restricting to $\psi$ must be the restriction of $\psi_\QQ$; this proves uniqueness.

Let
$$
\pi\colon(M\oplus N)^\#\twoheadrightarrow A_{M\perp N}^\sharp\isoto A_M^\sharp\oplus A_N^\sharp
$$
be the discriminant quotient morphism.
By @def:gluing-datum-of-a-pair, $L$ is the inverse image under $\pi$ of the subobject $h\colon(H,0)\injects A_{M\perp N}$.
The automorphism induced by $\psi_\QQ$ on the target of $\pi$ is $U_{\mathrm{mod}}(\bar\psi)$.
Hence $\psi_\QQ$ preserves $L$ exactly when $\bar\psi$ preserves the subobject $h$, which is equivalent to the existence of the automorphism $u$ in the commuting square above.
In that case $\restrictionof{\psi_\QQ}{L}$ is the required isometry.
:::

::: {.corollary #cor:liftable-automorphisms title="Stabilizer criterion for a fixed complementary action"}

With the notation of @thm:automorphism-lifting-criterion, fix $\varphi_N=\id_N$ and let
$\Gamma\injects\Orth(M)$ be a subgroup morphism.
Let $\Stab_{\Orth(A_M)}(h)\injects\Orth(A_M)$ be the stabilizer of the bilinear gluing subobject
$h\colon(H,0)\injects A_{M\perp N}$ under the action through the first summand of the common-value isometry of @prop:discriminant-orthogonal-sum.
The stabilizer $\Stab_\Gamma(h)$ is the pullback in $\mathbf{Grp}$

```tikzcd
\Stab_\Gamma(h) \arrow[r] \arrow[d] & \Gamma \arrow[d,"\rho_M|_\Gamma"] \\
\Stab_{\Orth(A_M)}(h) \arrow[r,hook] & \Orth(A_M).
```

Then the elements of $\Stab_\Gamma(h)$ are exactly the isometries of $M$ that extend over $L$ while fixing $N$ pointwise.
The pullback defining $\Stab_\Gamma(h)$ induces the monomorphisms
$$
\widetilde\Orth(M)\mathbin{\times}_{\Orth(M)}\Gamma
\injects
\Stab_\Gamma(h)
\injects
\Gamma,
$$
and the second has finite index.
:::

::: {.proof}

By @thm:automorphism-lifting-criterion, an element $\varphi_M\in\Gamma$ lifts with
$\varphi_N=\id_N$ exactly when $\rho_M(\varphi_M)$ lies in $\Stab_{\Orth(A_M)}(h)$.
This is precisely the universal property of the displayed pullback.
The identity morphism of $A_M$ gives the induced monomorphism
$\widetilde\Orth(M)\mathbin{\times}_{\Orth(M)}\Gamma\injects\Stab_\Gamma(h)$.
The discriminant module $A_M^\sharp$ has finite length over $\bZ$, hence finite cardinality; therefore $\Orth(A_M)$ is finite and $\Stab_\Gamma(h)\injects\Gamma$ has finite index.
:::


::: {.proposition #prop:gluing-lifting-obstruction-sequence title="Exact sequence and obstruction set for gluing extensions"}
For $\Gamma\injects\Orth(M)$ and the gluing subobject $h$ of @cor:liftable-automorphisms, put
$$
I_\Gamma\definedas\rho_M(\Gamma)\injects\Orth(A_M),
\qquad
J_h\definedas\Stab_{\Orth(A_M)}(h)\injects\Orth(A_M).
$$
The restriction of the discriminant representation gives the exact sequence of groups
$$
1\too\Gamma\cap\widetilde\Orth(M)
\too\Stab_\Gamma(h)
\xrightarrow{\rho_M}
I_\Gamma\cap J_h
\too1.
$$
The right-coset set of obstructions to lifting $\varphi\in\Gamma$ while acting identically on $N$ is
$$
\Gamma/\Stab_\Gamma(h)
\xrightarrow{\sim}
I_\Gamma/(I_\Gamma\cap J_h),
\qquad
\varphi\,\Stab_\Gamma(h)\longmapsto
\rho_M(\varphi)(I_\Gamma\cap J_h).
$$
In particular,
$$
[\Gamma:\Stab_\Gamma(h)]
=[I_\Gamma:I_\Gamma\cap J_h]<\infty.
$$
The displayed coset sets are groups only when the corresponding stabilizers are normal.
:::

::: {.proof}
By the pullback in @cor:liftable-automorphisms, $\Stab_\Gamma(h)=\rho_M^{-1}(J_h)\cap\Gamma$. The restriction of $\rho_M$ therefore has image $I_\Gamma\cap J_h$ and kernel $\Gamma\cap\ker\rho_M=\Gamma\cap\widetilde\Orth(M)$, proving exactness. The coset bijection and index equality follow by the same pullback and the first isomorphism theorem applied to the image of $\Gamma$.
:::


## The unimodular case

::: {.corollary #cor:lifting-unimodular title="Lifting across a unimodular overlattice"}

Suppose in addition that $L$ is unimodular.
Then $H$ is the graph of an isometry $\gamma\colon A_M\isoto A_N(-1)$ defined on all of $A_M$, and $\varphi_M\perp\varphi_N$ extends to $L$ if and only if
$\bar{\varphi}_N\circ\gamma=\gamma\circ\bar{\varphi}_M$.
If $L,M,N$ are even, $\gamma$ refines to an isometry $\gamma_q\colon A_{M,q}\isoto A_{N,q}(-1)$.
:::

::: {.proof}

Unimodularity of $L$ forces $H_M = A_M$ and $H_N = A_N$ in @cons:embedding-gluing-data, so $H$ is the graph $\theset{(x, \gamma x) \mid x\in A_M}$ of the isometry $\gamma\colon A_M\isoto A_N(-1)$.
A pair preserves that graph exactly when $\bar{\varphi}_N(\gamma x)=\gamma(\bar{\varphi}_M x)$ for every $x$, which is the displayed identity.
:::
