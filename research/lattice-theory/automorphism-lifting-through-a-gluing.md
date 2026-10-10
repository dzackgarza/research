# Automorphism lifting through a gluing {#sec:automorphism-lifting}


## The discriminant representation

::: {.notation #not:discriminant-representation title="Notation for discriminant actions"}

Let $\rho_L\colon\Orth(L)\too\Orth(A_L)$ be the bilinear discriminant representation of @def:discriminant-rep.
For $\varphi\in\Orth(L)$ write $\bar{\varphi}\definedas\rho_L(\varphi)$.
If $L$ is even, write $\bar{\varphi}_q\definedas\rho_{L,q}(\varphi)\in\Orth(A_{L,q})$.
:::

::: {.observation #obs:discriminant-direct-sum-action title="Discriminant action on an orthogonal sum"}

The discriminant functor of @def:discriminant gives
$A_{M\perp N}\isoto A_M\perp A_N$ and
$\rho_{M\perp N}(\varphi_M\perp\varphi_N)
=\bar{\varphi}_M\perp\bar{\varphi}_N$.
If $M$ and $N$ are even, likewise
$A_{M\perp N,q}\isoto A_{M,q}\perp A_{N,q}$ for the quadratic discriminant representations.
:::

## The lifting criterion

::: {.definition #def:gluing-datum-of-a-pair title="The gluing datum of a pair of primitive inclusions"}

Let $\iota_M\colon M\injects L$ and $\iota_N\colon N\injects L$ be primitive embeddings with
$\iota_N(N)=\iota_M(M)^{\perp L}$.
Set $j\definedas\iota_M\oplus\iota_N\colon M\oplus N\injects L$, and let
$$
0\too M\perp N\xrightarrow{j}L\xrightarrow{c}H\too0
$$
be its cokernel sequence.
The cokernel morphism
$\pi_{M\perp N}\colon(M\perp N)^\#\twoheadrightarrow A_{M\perp N}^\sharp$
of @def:metric-dual induces
$h\colon(H,0)\injects A_M\perp A_N$
in $\mathbf{BilMod}_{\bZ}$, characterized by
```tikzcd
L \arrow[r] \arrow[d,two heads,"c"'] & (M\perp N)^\# \arrow[d,two heads,"\pi_{M\perp N}"] \\
H \arrow[r,hook,"U(h)"'] & A_{M\perp N}^\sharp
```
The **gluing datum** is the subobject represented by $h$.

If $L,M,N$ are even, $h$ refines to
$h_q\colon(H,0)\injects A_{M,q}\perp A_{N,q}$
by @thm:nikulin-gluing.
Equivalently, $h$ is the graph subobject of an isometry
$\gamma\colon H_M\isoto H_N(-1)$
between subobjects $H_M\injects A_M$ and $H_N\injects A_N$.
In the even case, $\gamma$ refines to an isometry of the induced quadratic subobjects after the $(-1)$-twist.
:::

::: {.theorem #thm:automorphism-lifting-criterion title="When a pair of isometries lifts"}

Let $L$, $M$, $N$ and $h\colon H\injects A_M\oplus A_N$ be as in @def:gluing-datum-of-a-pair, and let
$\varphi_M\in\Orth(M)$ and $\varphi_N\in\Orth(N)$.
Put $\bar{\varphi}\definedas\bar{\varphi}_M\oplus\bar{\varphi}_N$.
Then $\varphi_M\oplus\varphi_N$ extends to an isometry of $L$ if and only if there exists
$u\in\Aut(H)$ for which the following square commutes:

```tikzcd
H \arrow[r,"u"] \arrow[d,"h"'] & H \arrow[d,"h"] \\
A_M\oplus A_N \arrow[r,"\bar{\varphi}"'] & A_M\oplus A_N
```

The extension is then unique and restricts to $\varphi_M$ on $M$ and to $\varphi_N$ on $N$.
:::

::: {.proof}

Write $\psi\definedas\varphi_M\oplus\varphi_N\in\Orth(M\oplus N)$.
After scalar extension, $\psi_\QQ\colon(M\oplus N)_\QQ\isoto(M\oplus N)_\QQ$ is an isometry and therefore acts on $(M\oplus N)^\#$.
Because $j(M\oplus N)$ spans $L_\QQ$, any isometry of $L$ restricting to $\psi$ must be the restriction of $\psi_\QQ$; this proves uniqueness.

Let
$$
\pi\colon(M\oplus N)^\#\twoheadrightarrow A_{M\perp N}^\sharp\isoto A_M^\sharp\oplus A_N^\sharp
$$
be the discriminant quotient morphism.
By @def:gluing-datum-of-a-pair, $L$ is the inverse image under $\pi$ of the subobject represented by
$h\colon H\injects A_M\oplus A_N$.
The automorphism induced by $\psi_\QQ$ on the target of $\pi$ is $U(\bar{\varphi})$.
Hence $\psi_\QQ$ preserves $L$ exactly when $\bar{\varphi}$ preserves the subobject $h$, which is equivalent to the existence of the automorphism $u$ in the commuting square above.
In that case $\restrictionof{\psi_\QQ}{L}$ is the required isometry.
:::

::: {.corollary #cor:liftable-automorphisms title="The liftable subgroup"}

With the notation of @thm:automorphism-lifting-criterion, fix $\varphi_N=\id_N$ and let
$\Gamma\injects\Orth(M)$ be a subgroup morphism.
Let $\Stab(h)\injects\Orth(A_M)$ be the stabilizer of the bilinear gluing subobject
$h\colon(H,0)\injects A_M\perp A_N$ under the action through the first summand.
Define the **liftable subgroup** $\Gamma_h$ by the pullback

```tikzcd
\Gamma_h \arrow[r] \arrow[d] & \Gamma \arrow[d,"\rho_M|_\Gamma"] \\
\Stab(h) \arrow[r,hook] & \Orth(A_M).
```

Then the elements of $\Gamma_h$ are exactly the isometries of $M$ that extend over $L$ while fixing $N$ pointwise.
The pullback defining $\Gamma_h$ induces the monomorphisms
$$
\widetilde\Orth(M)\mathbin{\times}_{\Orth(M)}\Gamma
\injects
\Gamma_h
\injects
\Gamma,
$$
and the second has finite index.
:::

::: {.proof}

By @thm:automorphism-lifting-criterion, an element $\varphi_M\in\Gamma$ lifts with
$\varphi_N=\id_N$ exactly when $\rho_M(\varphi_M)$ lies in $\Stab(h)$.
This is precisely the universal property of the displayed pullback.
The identity morphism of $A_M$ gives the induced monomorphism
$\widetilde\Orth(M)\mathbin{\times}_{\Orth(M)}\Gamma\injects\Gamma_h$.
The discriminant module $A_M^\sharp$ has finite length over $\bZ$, hence finite cardinality; therefore $\Orth(A_M)$ is finite and $\Gamma_h\injects\Gamma$ has finite index.
:::

::: {.observation #obs:liftability-belongs-to-embedding title="Liftability belongs to the embedding arrows"}

The datum consumed by @thm:automorphism-lifting-criterion is $H$, equivalently the pair of primitive embedding morphisms
$\iota_M\colon M\injects L$ and $\iota_N\colon N\injects L$ of @def:gluing-datum-of-a-pair.
Neither $M$ nor $N$ determines this datum: the same lattice $M$ occurs in many gluings.
Liftability is therefore a property of the pair $(\iota_M,\iota_N)$, and the subgroup of @cor:liftable-automorphisms is attached to that pair.

The hypotheses are morphism-level for the same reason.
A morphism $\iota\colon S\injects M$ is primitive when its cokernel is torsion-free (@prop:primitive-characterization), and saturation and index are properties of $\iota$; a determinant or a greatest common divisor of matrix entries recognizes primitivity only under hypotheses that the definition itself does not state.
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
