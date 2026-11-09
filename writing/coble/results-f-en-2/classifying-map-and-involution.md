# The classifying map and the Enriques involution

## Global extension of the Enriques involution

::: {.proposition #prop:enriques-involution-extends title="Extension of the Enriques involution and the classifying morphism"}

Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$, and let $(\mcx_B, \eps\mcr_B)\to B$ be the pullback of the universal family of KSBA-stable pairs.
Its general fibre is a pair $(X, \eps R)$ of an Enriques K3 surface $X$ and the ramification divisor $R$ of the del Pezzo involution.

1. By uniqueness of KSBA-stable limits, the Enriques involution $\ien$ of the general fibre extends to an involution of $(\mcx_B, \eps\mcr_B)$.
   The quotient is a family $(\mcz, \eps\mcr_\mcz)\to B$ over a compact base, which extends the universal family of Enriques surfaces with divisor.

2. The normalization $\normalize{B}$ is a compactification of $\fentwo$ with a universal family of pairs, so there is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$

[@AEGS25, Lem. 2.8 and proof of Thm. 5.9].
:::

::: {.conjecture #conj:enriques_involution_extension title="Uniqueness and compatibility of the extended involution"}

Let $B$ be the Noether--Lefschetz closure of @prop:enriques-involution-extends.
The involution of $(\mcx_B, \eps\mcr_B)$ in @prop:enriques-involution-extends(1) is the unique involution that extends $\ien$, and it commutes with the del Pezzo involution $\idp$.
The quotient $(\mcz, \eps\mcr_\mcz)\to B$ is a flat family of KSBA-stable Enriques pairs over $B$.
:::

## Finiteness of the classifying map

::: {.theorem #thm:classifying-map-finite title="Finiteness of the classifying map"}

The classifying morphism
$$
\phi\colon \normalize{B} \to \ksbacpt{\fentwo}
$$
of @prop:enriques-involution-extends(2), from the normalization $\normalize{B}$ of the Noether--Lefschetz closure, is finite [@AEGS25, proof of Thm. 5.9].
:::

::: {.proposition #prop:enriques-semifan-coarsening title="The semifans of the normalized KSBA compactification"}

Let $\semitorfan = \theset{\semifan{F}_k}_{k=1}^5$ be the generalized Coxeter semifans of the folded Coxeter diagrams of the five $0$-cusps of $\fentwo$ [@AEGS25, Def. 5.3, Lem. 5.5].

1. The normalization $\normksbacpt{\fentwo}$ dominates the Baily--Borel compactification $\bbcpt{\fentwo}$, and it is the semitoroidal compactification for a collection of semifans $\semifan{G}_k$ that coarsen the $\semifan{F}_k$.

2. If the maximal cones of the $\semifan{G}_k$ are the maximal cones of the $\semifan{F}_k$, then $\phi$ is finite.

3. A degeneration of $(\mcz, \eps\mcr_\mcz)$ has the maximal number of double curves if and only if the corresponding degeneration of $(\mcx, \eps\mcr)$ has

[@AEGS25, proof of Thm. 5.9].
:::

## Zariski's Main Theorem and the classifying isomorphism

::: {.theorem #thm:zariski_main_theorem title="Finite birational maps onto a normal variety"}

Let $f\colon X \to Y$ be a finite birational morphism of varieties, with $Y$ normal.
Then $f$ is an isomorphism.
:::

::: {.proof}

A finite morphism is affine, so locally $Y = \Spec A$ and $X = \Spec B$ with $B$ a finite $A$-module containing $A$; birationality identifies $\Frac B$ with $\Frac A = K$, giving $A\iscontainedin B\iscontainedin K$.
Since $Y$ is normal, $A$ is integrally closed in $K$, and $B$ is integral over $A$, so $B = A$.

:::

::: {.conjecture #conj:classifying_map_isomorphism title="The classifying map is an isomorphism"}

The classifying map
$$
\phi\colon \normalize{B} \to \normksbacpt{\fentwo}
$$
is an isomorphism.
:::

::: {.proposition #prop:classifying-map-isomorphism-criterion title="A criterion for the classifying map"}

Let $\phi\colon\normalize{B}\to\normksbacpt{\fentwo}$ be a morphism that is an isomorphism over $\fentwo$ and has finite fibres.
Then $\phi$ is an isomorphism.
In particular, let $\psi\colon\normalize{B}\to\normksbacpt{\fentwo}$ be a morphism whose composite with the normalization morphism $\normksbacpt{\fentwo}\to\ksbacpt{\fentwo}$ is the classifying morphism of @thm:classifying-map-finite.
Each fibre of $\psi$ is contained in a fibre of the classifying morphism, so it is finite.
So if $\psi$ is an isomorphism over $\fentwo$, then $\psi$ is an isomorphism, and @conj:classifying_map_isomorphism holds.
:::

::: {.proof}

The space $\ksbacpt{\fentwo}$ is compact, and it is the closure of $\fentwo$ in the KSBA moduli space of stable pairs [@AEGS25, §5.3].
The space $B$ is closed in the compact space $\ksbacpt{\fttz}$, and $\normalize{B}$ is a compactification of $\fentwo$ (@prop:enriques-involution-extends).
So $\normalize{B}$ and $\normksbacpt{\fentwo}$ are proper, $\fentwo$ is dense in both, and $\phi$ is proper.
A proper morphism with finite fibres is finite [@stacks-02LS].
Since $\phi$ is an isomorphism over the dense open $\fentwo$, it is birational.
The target $\normksbacpt{\fentwo}$ is normal, so $\phi$ is an isomorphism by @thm:zariski_main_theorem.
:::
