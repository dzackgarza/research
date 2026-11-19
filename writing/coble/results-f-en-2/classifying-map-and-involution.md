# The classifying map and the Enriques involution

## Global extension of the Enriques involution

::: {.proposition #prop:enriques-involution-extends title="Extension of the Enriques involution and the classifying morphism"}

Let $B$ be the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$, and let $(\mcx_B, \eps\mcr_B)\to B$ be the pullback of the universal family of KSBA-stable pairs.
Its general fibre is a pair $(X, \eps R)$ of an Enriques K3 surface $X$ and the ramification divisor $R$ of the del Pezzo involution.

1. The Enriques involution (@def:enriques-surface) $\ien$ of the general fibre extends uniquely to an involution of $(\mcx_B, \eps\mcr_B)$ commuting with the del Pezzo involution $\idp$.
   The quotient is a flat family $(\mcz, \eps\mcr_\mcz)\to B$ over a compact base, which extends the universal family of Enriques surfaces with divisor.

2. The normalization $\normalize{B}$ is a compactification of $\fentwo$ with a universal family of pairs, so there is a classifying morphism $\normalize{B}\to\ksbacpt{\fentwo}$

[@AEGS25, Lem. 2.8 and proof of Thm. 5.9].
:::

::: {.proof}

The generic involution preserves $R$, hence acts on the relative log canonical algebra that forms the stable model. It therefore extends to the relative $\Proj$ of that algebra. Two extensions agree on a dense open subset and hence everywhere by separatedness; since $\ien$ and $\idp$ commute on the generic fibre, their extensions commute. In characteristic zero, the invariant part of a flat relative coordinate algebra is a direct summand, so the finite quotient remains flat over $B$. The quotient is a family of stable Enriques pairs; over $\fentwo$ it is the original family, which gives the classifying morphism after normalization [@AEGS25, proof of Thm. 5.9].
:::

## Finiteness of the classifying map

::: {.theorem #thm:classifying-map-finite title="Finiteness of the classifying map"}

The classifying morphism
$$
\phi\colon \normalize{B} \to \ksbacpt{\fentwo}
$$
of @prop:enriques-involution-extends(2), from the normalization $\normalize{B}$ of the Noether--Lefschetz closure (@def:nl-locus-enriques), is finite [@AEGS25, proof of Thm. 5.9].
:::

::: {.proof}

The normalization of the KSBA compactification (@def:ksba-compactification) dominates its Baily–Borel compactification: at a Type II boundary point, the elliptic modulus can be recovered from the slc Enriques pair. Either its double curve is elliptic, or it is a rational curve with four distinguished $A_1$ points. In the latter case, the double cover of $\PP^1$ branched at those points has the required $j$-invariant [@AEGS25, proof of Thm. 5.9; @AET23, Thm. 3.17].

The normalized KSBA space therefore lies between the semitoroidal compactification (@def:semitoroidal-compactification) determined by the folded semifans $\semifan{F}_k$ and Baily–Borel. The semitoroidal comparison theorem makes its semifans coarsenings $\semifan{G}_k$ of the $\semifan{F}_k$ [@AE23, Thm. 7.18]. If a maximal cone were lost in a strict coarsening, a codimension-one cone of some $\semifan{F}_k$ would parametrize a one-dimensional family of K3 pairs with fewer than the maximal number of double curves while their Enriques quotients had the maximal number. The explicit quotient models have the maximal number of double curves exactly when their K3 covers do [@AEGS25, Prop. 4.8, Cor. 4.9]. Thus the maximal cones remain distinct, and the classifying morphism is finite by the semitoroidal cone comparison [@AEGS25, proof of Thm. 5.9].
:::

::: {.proposition #prop:enriques-semifan-coarsening title="The semifans of the normalized KSBA compactification"}

Let $\semitorfan = \theset{\semifan{F}_k}_{k=1}^5$ be the generalized Coxeter semifans (@def:generalized-coxeter-semifan) of the folded Coxeter diagrams (@def:coxeter-matrix) of the five $0$-cusps of $\fentwo$ [@AEGS25, Def. 5.3, Lem. 5.5].

1. The normalization $\normksbacpt{\fentwo}$ dominates the Baily--Borel compactification $\bbcpt{\fentwo}$, and it is the semitoroidal compactification (@def:semitoroidal-compactification) for a collection of semifans $\semifan{G}_k$ that coarsen the $\semifan{F}_k$.

2. If the maximal cones of the $\semifan{G}_k$ are the maximal cones of the $\semifan{F}_k$, then $\phi$ is finite.

3. A degeneration of $(\mcz, \eps\mcr_\mcz)$ has the maximal number of double curves if and only if the corresponding degeneration of $(\mcx, \eps\mcr)$ does.

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

::: {.theorem #thm:classifying-map-isomorphism title="The classifying map is an isomorphism onto the normalization"}

Let $\nu\colon\normksbacpt{\fentwo}\to\ksbacpt{\fentwo}$ be the normalization morphism, and let $\phi\colon\normalize{B}\to\ksbacpt{\fentwo}$ be the classifying morphism of @thm:classifying-map-finite.
Then there is a unique morphism
$$
\psi\colon\normalize{B}\too\normksbacpt{\fentwo}
$$
with $\nu\circ\psi=\phi$, and $\psi$ is an isomorphism.
:::

::: {.proof}

The space $\fentwo=\bD(\ten)/\gent$ is the image of the connected complex manifold $\bD(\ten)$, so it is irreducible.
The space $\ksbacpt{\fentwo}$ is a compactification of $\fentwo$: it is the closure of $\fentwo$ in the moduli space of KSBA-stable pairs, and $\fentwo$ is open in it [@AEGS25, Def. 2.10].
So $\ksbacpt{\fentwo}$ is irreducible.
The space $B$ is the closure of the image of $\fentwo$ in $\ksbacpt{\fttz}$, so it is irreducible too, and its normalization $\normalize{B}$ is an integral normal variety [@stacks-035Q, (1)].
The space $\normalize{B}$ is a compactification of $\fentwo$ that carries a universal family of pairs extending the universal family of Enriques pairs over $\fentwo$ (@prop:enriques-involution-extends, [@AEGS25, proof of Thm. 5.9]).
Over the open subset $\fentwo\iscontainedin\normalize{B}$, the morphism $\phi$ classifies the universal family of Enriques pairs, so it restricts to the open embedding $\fentwo\injects\ksbacpt{\fentwo}$.

The image of $\phi$ therefore contains the dense subset $\fentwo$, so $\phi$ is dominant.
By the universal property of normalization [@stacks-035Q, (4)], $\phi$ factors uniquely as $\phi=\nu\circ\psi$.
The morphism $\phi$ is finite (@thm:classifying-map-finite) and $\nu$ is separated, so $\psi$ is finite [@stacks-035D].

The space $\fentwo$ is normal: it is the open stratum $V_0$ of its Baily--Borel compactification, which is a normal analytic space (@thm:baily-borel-compactification).
So $\nu$ is an isomorphism over $\fentwo$, and $\psi$ restricts to an isomorphism of the dense open subset $\fentwo$ of $\normalize{B}$ onto the dense open subset $\nu^{-1}(\fentwo)$ of $\normksbacpt{\fentwo}$.
Hence $\psi$ is birational.
The variety $\normksbacpt{\fentwo}$ is normal, so the finite birational morphism $\psi$ is an isomorphism by @thm:zariski_main_theorem.
:::
