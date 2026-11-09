# The classifying map and the Enriques involution

## Global extension of the Enriques involution

::: {.conjecture #conj:enriques_involution_extension title="Global extension of the Enriques involution"}

Over the Noether--Lefschetz closure $B \iscontainedin \ksbacpt{\fttz}$ of the Enriques Noether--Lefschetz-locus definition (@def:nl-locus-enriques), there is a universal KSBA family $(\mcx_B, \eps \mcr_B)$.
The fixed-point-free Enriques involution $\ien$ on the smooth fibers extends uniquely to an involution of $\mcx_B$.
This involution preserves the slc pair structure and the ramification divisor $\mcr_B$, and commutes with the del Pezzo involution $\idp$, so the quotient $(\mcx_B, \eps \mcr_B) / \ien$ is a flat family of stable Enriques pairs over $B$.
:::

::: {.proposition #prop:enriques-involution-extends title="Extension of the Enriques involution and the classifying morphism"}

Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$, and let $(\mcx_B, \eps\mcr_B)\to B$ be the pullback of the universal family of KSBA-stable pairs.
Its general fibre is a pair $(X, \eps R)$ of an Enriques K3 surface $X$ and the ramification divisor $R$ of the del Pezzo involution.

1. By uniqueness of KSBA-stable limits, the Enriques involution $\ien$ of the general fibre extends to an involution of $(\mcx_B, \eps\mcr_B)$.
   The quotient is a family $(\mcz, \eps\mcr_\mcz)\to B$ over a compact base, which extends the universal family of Enriques surfaces with divisor.

2. The normalization $\normalize{B}$ is a compactification of $\fentwo$ with a universal family of pairs, so there is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$

[@AEGS25, Lem. 2.8 and proof of Thm. 5.9].
:::

## Finiteness of the classifying map

::: {.conjecture #conj:classifying_map_finite title="Finiteness of the classifying map"}

The classifying morphism
$$
\phi\colon \normalize{B} \to \ksbacpt{\fentwo}
$$
from the normalization $B^\nu$ of the Noether--Lefschetz closure is finite.
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
In particular, @conj:classifying_map_finite implies @conj:classifying_map_isomorphism for every such morphism $\phi$.
:::

::: {.proof}

The space $\ksbacpt{\fentwo}$ is compact, and it is the closure of $\fentwo$ in the KSBA moduli space of stable pairs [@AEGS25, §5.3].
The space $B$ is closed in the compact space $\ksbacpt{\fttz}$, and $\normalize{B}$ is a compactification of $\fentwo$ (@prop:enriques-involution-extends).
So $\normalize{B}$ and $\normksbacpt{\fentwo}$ are proper, $\fentwo$ is dense in both, and $\phi$ is proper.
A proper morphism with finite fibres is finite [@stacks-02LS].
Since $\phi$ is an isomorphism over the dense open $\fentwo$, it is birational.
The target $\normksbacpt{\fentwo}$ is normal, so $\phi$ is an isomorphism by @thm:zariski_main_theorem.
:::
