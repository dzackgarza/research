# Automorphism lifting through a gluing {#sec:automorphism-lifting}


## The discriminant representation

::: {.notation #not:discriminant-representation title="Notation for discriminant actions"}

Let
$$
\rho_L\colon\Orth(L)\too\Orth(A_L)
$$
be the bilinear discriminant representation of @def:discriminant-rep.
For $\varphi\in\Orth(L)$ write
$$
\bar\varphi\definedas\rho_L(\varphi).
$$
If $L$ is even, write
$$
\bar\varphi_q\definedas\rho_{L,q}(\varphi)\in\Orth(A_{L,q})
$$
for the quadratic refinement.
:::

::: {.observation #obs:discriminant-direct-sum-action title="Discriminant action on an orthogonal sum"}

The discriminant functor of @def:discriminant gives a canonical isomorphism of bilinear discriminant objects
$$
A_{M\perp N}\isoto A_M\perp A_N,
$$
under which
$$
\rho_{M\perp N}(\varphi_M\perp\varphi_N)
=
\bar\varphi_M\perp\bar\varphi_N.
$$
If $M$ and $N$ are even, the same statement holds for
$$
A_{M\perp N,q}\isoto A_{M,q}\perp A_{N,q}
$$
and the quadratic representations $\rho_{-,q}$.
:::

## The lifting criterion

::: {.definition #def:gluing-datum-of-a-pair title="The gluing datum of a pair of primitive inclusions"}

Let $\iota_M\colon M\injects L$ and $\iota_N\colon N\injects L$ be primitive embeddings with
$\iota_N(N)=\iota_M(M)^{\perp L}$, and let
$$
j\definedas\iota_M\oplus\iota_N\colon M\oplus N\injects L.
$$
Let $H$ be the cokernel object in the short exact sequence
$$
0\too M\perp N\xrightarrow{j}L\xrightarrow{c}H\too0.
$$
The discriminant quotient induces a monomorphism of bilinear modules
$$
h\colon(H,0)\injects A_M\perp A_N,
$$
whose carrier morphism is obtained by factoring the canonical map
$L\to(M\perp N)^\#$ through $c$.
The **gluing datum** is this isotropic bilinear subobject.

If $L,M,N$ are even, the same carrier monomorphism refines to an isotropic quadratic subobject
$$
h_q\colon(H,0)\injects A_{M,q}\perp A_{N,q}
$$
by @thm:nikulin-gluing.
Equivalently, $h$ is the graph subobject of a bilinear anti-isometry
$$
\gamma\colon H_M\isoto H_N
$$
between subobjects $H_M\injects A_M$ and $H_N\injects A_N$; in the even case $\gamma$ refines to an anti-isometry of the induced quadratic subobjects.
:::

::: {.theorem #thm:automorphism-lifting-criterion title="When a pair of isometries lifts"}

Let $L$, $M$, $N$ and $h\colon H\injects A_M\oplus A_N$ be as in @def:gluing-datum-of-a-pair, and let
$\varphi_M\in\Orth(M)$ and $\varphi_N\in\Orth(N)$.
Put
$$
\bar\varphi\definedas\bar\varphi_M\oplus\bar\varphi_N.
$$
Then $\varphi_M\oplus\varphi_N$ extends to an isometry of $L$ if and only if there exists
$u\in\Aut(H)$ for which the following square commutes:

```tikzcd
H \arrow[r,"u"] \arrow[d,"h"'] & H \arrow[d,"h"] \\
A_M\oplus A_N \arrow[r,"\bar\varphi"'] & A_M\oplus A_N
```

The extension is then unique and restricts to $\varphi_M$ on $M$ and to $\varphi_N$ on $N$.
:::

::: {.proof}

Write $\psi\definedas\varphi_M\oplus\varphi_N\in\Orth(M\oplus N)$.
After scalar extension to $\QQ$, $\psi$ determines an isometry
$$
\psi_\QQ\colon(M\oplus N)_\QQ\isoto(M\oplus N)_\QQ
$$
and therefore an isometry of the metric dual $(M\oplus N)^\#$.
Because $j(M\oplus N)$ spans $L_\QQ$, any isometry of $L$ restricting to $\psi$ must be the restriction of $\psi_\QQ$; this proves uniqueness.

Let
$$
\pi\colon(M\oplus N)^\#\too A_M\oplus A_N
$$
be the discriminant quotient morphism.
By @def:gluing-datum-of-a-pair, $L$ is the inverse image under $\pi$ of the subobject represented by
$h\colon H\injects A_M\oplus A_N$.
The automorphism induced by $\psi_\QQ$ on the target of $\pi$ is $\bar\varphi$.
Hence $\psi_\QQ$ preserves $L$ exactly when $\bar\varphi$ preserves the subobject $h$, which is equivalent to the existence of the automorphism $u$ in the commuting square above.
In that case $\restrictionof{\psi_\QQ}{L}$ is the required isometry.
:::

::: {.corollary #cor:liftable-automorphisms title="The liftable subgroup"}

With the notation of @thm:automorphism-lifting-criterion, fix $\varphi_N=\id_N$ and let
$\Gamma\injects\Orth(M)$ be a subgroup morphism.
Let
$$
\Stab(h)\injects\Orth(A_M)
$$
be the stabilizer of the bilinear gluing subobject
$$
h\colon(H,0)\injects A_M\perp A_N
$$
under the action through the first summand.
Define the **liftable subgroup** $\Gamma_h$ by the pullback

```tikzcd id="liftable-subgroup-pullback"
\Gamma_h \arrow[r] \arrow[d] & \Gamma \arrow[d,"\rho_M|_\Gamma"] \\
\Stab(h) \arrow[r,hook] & \Orth(A_M).
```

Then the elements of $\Gamma_h$ are exactly the isometries of $M$ that extend over $L$ while fixing $N$ pointwise.
The pullback subgroup
$$
\widetilde\Orth(M)\mathbin{\times}_{\Orth(M)}\Gamma
$$
factors through $\Gamma_h$, and $\Gamma_h\to\Gamma$ has finite index.
:::

::: {.proof}

By @thm:automorphism-lifting-criterion, an element $\varphi_M\in\Gamma$ lifts with
$\varphi_N=\id_N$ exactly when $\rho_M(\varphi_M)$ lies in $\Stab(h)$.
This is precisely the universal property of the displayed pullback.
The stable discriminant kernel maps to the identity of $\Orth(A_M)$ and therefore factors through $\Gamma_h$.
The carrier module $M^\#/M$ of $A_M$ has finite length over $\bZ$, hence finite cardinality; therefore $\Orth(A_M)$ is finite and $\Gamma_h\to\Gamma$ has finite index.
:::

::: {.observation #obs:liftability-belongs-to-embedding title="Liftability belongs to the embedding arrows"}

The datum consumed by the lifting criterion (@thm:automorphism-lifting-criterion) is $H$, equivalently the pair of primitive inclusions of the gluing-datum definition (@def:gluing-datum-of-a-pair).
Neither $M$ nor $N$ determines it: the same lattice $M$ occurs in many gluings, and each one imposes its own condition.
Liftability is therefore a property of the inclusions, and the subgroup of the liftable-subgroup corollary (@cor:liftable-automorphisms) is attached to them.

The hypotheses are morphism-level for the same reason.
An inclusion is primitive when its cokernel is torsion-free (@prop:primitive-characterization), and saturation and index are properties of the inclusion; a determinant or a greatest common divisor of matrix entries recognizes primitivity only under hypotheses that the definition itself does not state.
:::

## The unimodular case

::: {.corollary #cor:lifting-unimodular title="Lifting across a unimodular overlattice"}

Suppose in addition that $L$ is unimodular.
Then $H$ is the graph of a bilinear anti-isometry
$$
\gamma\colon A_M\isoto -A_N
$$
defined on all of $A_M$, and $\varphi_M\perp\varphi_N$ extends to $L$ if and only if
$$
\bar\varphi_N\circ\gamma=\gamma\circ\bar\varphi_M.
$$
If $L,M,N$ are even, $\gamma$ refines to a quadratic anti-isometry
$$
\gamma_q\colon A_{M,q}\isoto -A_{N,q}.
$$
:::

::: {.proof}

Unimodularity of $L$ forces $H_M = A_M$ and $H_N = A_N$ in @cons:embedding-gluing-data, so $H$ is the graph $\theset{(x, \gamma x) \mid x\in A_M}$ of an anti-isometry defined on all of $A_M$.
A pair preserves that graph exactly when $\bar\varphi_N(\gamma x) = \gamma(\bar\varphi_M x)$ for every $x$, which is the displayed identity.
:::
