---
unit: research-program
status: conjectural
tags:
  - nodal-enriques
  - non-2-elementary
  - moduli
---

# The nodal Enriques moduli program {#sec-nodal-enriques-moduli-program}

## Setting

::: {.definition title="Nodal and unnodal"}

An Enriques surface $Y$ is **nodal** if it contains a rational $(-2)$-curve, and **unnodal** otherwise.
A generic Enriques surface is unnodal, and $F_{\Nod}$ is an irreducible hypersurface in $\fen$.
:::

$$
S_{\Nod} = \generators{-4}\oplus U \oplus E_8(2),
\qquad
T_{\Nod} \definedas S_{\Nod}^\perp \cong \generators{4}\oplus U \oplus E_8(2),
$$
the generic Picard lattice of the K3 cover $X$ and its transcendental lattice.
$F_{\Nod}$ is realized as the divisor $\mch_{-4}/\Orth(\ten)$, a 9-dimensional irreducible quasiprojective variety.

::: {.proposition #prop:nodal-embedding-forms title="Two forms of the embedding $\sen\injects S_{\Nod}$"}

Let $U(2) = \generators{e,f}$, $U = \generators{\tilde e,\tilde f}$ and $\generators{-4} = \generators{h}$.
The map
$$
j_1\colon ((e,f), x) \mapsto \big((2\tilde f + \tilde e + h,\ \tilde e),\ x\big),
$$
the identity on the $E_8(2)$ factor, is a primitive embedding $\sen\injects S_{\Nod}$ [@CDL25, Def. 5.6.3, p. 561].
The map
$$
j_2\colon ((e,f), x) \mapsto \big((\tilde f,\ 2\tilde e + \tilde f + h),\ x\big),
$$
the identity on the $E_8(2)$ factor, is the composite $\tau\circ j_1\circ\sigma$, where $\sigma$ is the isometry $e\leftrightarrow f$ of $\sen$ and $\tau$ is the isometry $\tilde e\leftrightarrow\tilde f$ of $S_{\Nod}$, both the identity on the other summands.
Hence $j_2$ is also a primitive embedding.
:::

::: {.proof}

The map $j_1\circ\sigma$ sends $e\mapsto\tilde e$ and $f\mapsto 2\tilde f+\tilde e+h$.
Then $\tau$ sends these to $\tilde f$ and $2\tilde e+\tilde f+h$, which is $j_2$.
A composite of a primitive embedding with isometries of the source and of the target is a primitive embedding.
:::

## The program

::: {.conjecture title="Baily-Borel boundary by the same techniques"}

Orbits under $\Orth(T_{\Nod})$ of isotropic vectors and planes can be classified, yielding a boundary incidence diagram; and the lattice embedding above allows AEGS23 to be leveraged to construct the KSBA compactification, its dlt models, and the integral-affine structures classifying KSBA stable limits of nodal Enriques surfaces.
:::

::: {.proposition #prop:nodal-transcendental-not-two-elementary title="$T_{\Nod}$ is not $2$-elementary"}

The discriminant group of $T_{\Nod} = \generators{4}\oplus U\oplus E_8(2)$ is
$$
A^\sharp_{T_{\Nod}} \cong \ZZ/4\ZZ\oplus(\ZZ/2\ZZ)^{8},
$$
so $T_{\Nod}$ is not $2$-elementary (@def:p-elementary).
:::

::: {.proof}

The dual lattice of an orthogonal direct sum is the direct sum of the dual lattices (@def:metric-dual), so $A^\sharp_{T_{\Nod}} = A^\sharp_{\generators4}\oplus A^\sharp_U\oplus A^\sharp_{E_8(2)}$.
For $\generators{4} = \ZZ h$ with $h^2 = 4$, the dual lattice is $\ZZ\,h/4$, so $A^\sharp_{\generators4} = \ZZ/4\ZZ$.
The lattice $U$ is unimodular, so $A^\sharp_U = 0$.
The lattice $E_8$ is unimodular, so the dual lattice of $E_8(2)$ is $\tfrac12 E_8$ and $A^\sharp_{E_8(2)} = \tfrac12E_8/E_8\cong(\ZZ/2\ZZ)^8$.
The class of $h/4$ has order $4$, so $A^\sharp_{T_{\Nod}}$ is not isomorphic to $(\ZZ/2\ZZ)^a$ for any $a$.
:::

## Known results on nodal Enriques surfaces

::: {.proposition #prop:nodal-enriques-known-results title="Automorphisms, Reye congruences, derived categories and rationality"}

1. Let $Q$ be the quadratic form of rank $10$ of the Dynkin diagram $T_{2,4,6}$, let $W$ be its Weyl group, and let $\overline W(2)$ be the unique normal subgroup of $W$ that contains the $2$-congruence subgroup $W(2)$ and has $W/\overline W(2)\cong\mathrm{Sp}(8,\mathbb F_2)$.
   Over an algebraically closed field of characteristic $p\notin\theset{2,3,5,7,17}$, the automorphism group of a generic nodal Enriques surface is isomorphic to $\overline W(2)$, and any two nonsingular rational curves on a generic nodal Enriques surface differ by an automorphism of the surface [@CD85, Thms. 1 and 3].

2. Every classical nodal Enriques surface $X$ is a Reye congruence: $X$ has a Fano polarization $H$ whose morphism $\varphi_H\colon X\to\PP^5$ maps $X$ onto a nondegenerate surface of degree $10$ and factors through a smooth quadric hypersurface [@MMV24, Def. 3.1 and Thm. 1.1].

3. Let $S$ be the nodal Enriques surface of a quartic symmetroid $D\subset\PP^3$, let $X$ be the nodal quartic double solid ramified in $D$, and let $X^+$ be a small resolution of $X$.
   Let $\mathcal A_S\subset D^b(S)$ be the orthogonal subcategory of the completely orthogonal exceptional collection $\theset{\mathcal O_S(-F_i^+)}_{i=1}^{10}$, where $F_i^+$ is a multiple fiber of the $i$-th of the ten elliptic pencils on $S$.
   There is a semiorthogonal decomposition $D^b(X^+) = \generators{\mathcal A_{X^+},\ \mathcal O_{X^+}(-h),\ \mathcal O_{X^+}}$, with $h$ the pullback of the hyperplane class of $\PP^3$ and $\mathcal A_{X^+} = \generators{\mathcal O_{X^+}(-h),\mathcal O_{X^+}}^\perp$, and $\mathcal A_{X^+}\cong\mathcal A_S$ [@IK15, §1, Prop. 3.8 and Thm. 4.3].

4. Over $\CC$ the coarse moduli space of nodal Enriques surfaces is rational [@DK13, Thm. 6.4].
:::

Related: [Nodal Enriques lattices](#sec-nodal-enriques-lattices), [Coble families research program](#sec-coble-families-research-program), [Halphen index-2 moduli program](#sec-halphen-index-2-moduli-program).
