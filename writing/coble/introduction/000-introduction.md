# Overview

::: {.theorem #thm:baily-borel-compactification title="The Baily--Borel compactification"}

Let $G$ be a connected semisimple $\QQ$-group with trivial center whose symmetric space $X = K\backslash G_\RR$ is a bounded domain, and let $\Gamma$ be an arithmetic group of automorphisms of $X$.
Let $X^*$ be the union of the rational boundary components of $X$ with the Satake topology, and let $V^* = X^*/\Gamma$ be the compactification of $V = X/\Gamma$.
Then $V^*$ is the disjoint union of finitely many quotients $V_i = F_i/\Gamma(F_i)$ of rational boundary components $F_i$, with $F_0 = X$.
The space $V^*$ is an irreducible normal analytic space, in which each $V_i$ is a locally closed analytic subspace [@BB66, 10.1, Thm. 10.4].
There are finitely many automorphic forms of one weight whose map $V^*\to\PP^N$ is an isomorphism onto a normally projective subvariety of $\PP^N$ [@BB66, Thm. 10.11].

:::

::: {#fig-baily-borel-schematic .figure}
\input{tikz/baily_borel_schematic.tikz}

The Baily--Borel compactification of $F_{2d} = D_{L_{2d}}/\Gamma_{L_{2d}}$.
:::

::: {#fig-coxeter-fan-cone .figure}
\input{tikz/hyperbolic_cone_fundamental_domain.tikz}

A fundamental polyhedron $P$ for the Weyl group of a hyperbolic lattice acting on the positive cone $\mcc$, together with its images under the reflections in the walls of $P$; the Coxeter fan is the resulting decomposition of $\mcc$.
Such a polyhedron is computed by Vinberg's algorithm [@Vin75 §1].
:::

::: {.conjecture #conj:coble-ksba-semitoroidal-morphism title="The KSBA compactification of $\fco$ maps to a semitoroidal one"}

There is a collection of semifans $\theset{\mcf_I}$, one at each $0$-cusp of $\fco$, such that there exists a morphism
$$
\Psi: (\overline{F_\Co})^{\nu} \to \overline{F_\Co}^{\theset{\mcf_I}}
$$
from the normalization of the KSBA compactification to the semitoroidal compactification associated with them.
At the cusp represented by $v_1$, whose boundary lattice is $\latI_{1,8}(2) = (9,9,1)_1$, the Coxeter fan of $T_{\Co}$ refines the semifan $\mcf_{v_1}$.
Stable Coble surfaces in the boundary of $\overline{F_\Co}$ admit explicit descriptions in terms of surfaces associated to sub-Dynkin diagrams of Coxeter diagrams.
:::

## Acknowledgements
I would like to thank my advisor Valery Alexeev for his guidance and support throughout this project.
I thank Luca Schaffler and Philip Engel for many useful discussions.
I would also like to gratefully acknowledge financial support from the Office of the Graduate School of the University of Georgia and the Research and Training Group in Algebra, Algebraic Geometry, and Number Theory at the University of Georgia.
