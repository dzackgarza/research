---
unit: computation
status: computed
tags:
  - coxiter
  - coxeter-diagrams
  - cusps
  - hyperbolic-lattices
notes: |-
  Provenance: the archived Sterk 1--5 CoxIter reports and CoxIter diagram collection. None of this appears in the dissertation.
---

# CoxIter results for the Sterk cusps and the 0-cusp lattices {#sec-coxiter-results-for-cusp-lattices}


## The five Sterk cusps

::: {.example #ex:coxiter-sterk-cusp-invariants title="CoxIter invariants of the folded Sterk diagrams"}

For the folded Coxeter diagram of each of the five Sterk cusps of $\fentwo$, CoxIter returns dimension $9$, non-cocompact with finite covolume, Euler characteristic $0$, and the following data.

| Cusp | Nodes | Gram field | Vertices at $\infty$ | Signature line | $f$-vector |
| --- | --- | --- | --- | --- | --- |
| Sterk 1 | 12 | $\QQ$ | 9 | $9,1,2$ | $(23,114,288,462,504,378,192,63,12,1)$ |
| Sterk 2 | 10 | $\QQ[\sqrt2]$ | 2 | $9,1,0$ | $(10,45,120,210,252,210,120,45,10,1)$ |
| Sterk 3 | 12 | $\QQ[\sqrt2]$ | 4 | $9,1,2$ | $(33,164,398,602,616,434,208,65,12,1)$ |
| Sterk 4 | 11 | $\QQ[\sqrt2]$ | 5 | $9,1,1$ | $(26,125,300,450,460,330,165,55,11,1)$ |
| Sterk 5 | 14 | $\QQ[\sqrt2]$ | 13 | $9,1,4$ | $(115,600,1352,1768,1508,875,346,90,14,1)$ |
:::

::: {.example #ex:coxiter-sterk-one-growth-rate title="Growth rate of Sterk 1"}

The growth rate of the Coxeter group of the folded Sterk 1 diagram is
$$
2.6246613781819533651112379994955986218 ,
$$
a Perron number that is neither a Pisot number nor a Salem number.
At rank $9$ the Sterk 1 diagram has $4$ spherical subdiagrams of type $A_1 \oplus E_8$, each with Weyl group of order $1393459200$.
:::

::: {.proposition #prop:aegs-coxeter-ray-counts title="Rays of the Coxeter fans and of the semifans"}

For $k = 1,\dots,5$ let $G^k$ be the folded Coxeter diagram of the $0$-cusp $k$ of $\fentwo$, and let $\Gamma_k = \operatorname{Aut}(G^k)\ltimes W(G^k)$ be the group induced on $e^{\perp}/e$.
The Type II rays of the Coxeter fan correspond to the maximal parabolic subdiagrams of $G^k$, and the Type III cones to its elliptic subdiagrams [@AEGS25, §5.1].
The numbers of Type II and Type III rays modulo $\Gamma_k$ are $4+4$, $2+8$, $3+15$, $4+12$, $5+17$ for $k = 1,\dots,5$ [@AEGS25, Lem. 5.2].
After removal of every subdiagram with a connected component of irrelevant roots, the numbers of Type II and Type III divisors at the cusps of the semitoroidal compactification are $2+0$, $2+7$, $2+7$, $4+7$, $3+0$ [@AEGS25, Lem. 5.8].
:::

::: {.example #ex:sterk-one-ideal-vertex-orbits title="Ideal vertices of Sterk 1 modulo diagram symmetries"}

An ideal vertex of the Coxeter polytope of $G^1$ is a maximal parabolic subdiagram (@cor:ideal-vertices-are-parabolic).
The polytope has nine ideal vertices (@ex:coxiter-sterk-cusp-invariants), and by @prop:aegs-coxeter-ray-counts they form four orbits under $\operatorname{Aut}(G^1)$.
:::

## The 0-cusp lattices

::: {.example #ex:coxiter-zero-cusp-lattices title="CoxIter invariants of the $0$-cusp lattices"}

| Lattice $(r,a,\delta)$ | Diagram | Field | Dim | Vertices at $\infty$ | $f$-vector | $\chi$ |
| --- | --- | --- | --- | --- | --- | --- |
| $(9,9,1)_1$ | nine nodes, arms of lengths $1,2,5$ at a branch node, label 4 on the last edge of the long arm | $\QQ[\sqrt2]$ | 8 | 1 | $(9,36,84,126,126,84,36,9,1)$ | $17/1393459200$ |
| $(10,8,0)_1$ | ten nodes, arms of lengths $1,2,6$ at a branch node, label 4 on the last edge of the long arm | $\QQ[\sqrt2]$ | 9 | 2 | $(10,45,120,210,252,210,120,45,10,1)$ | $0$ |
| $(10,10,0)_1$ | $T_{2,3,7}$: ten nodes, arms of lengths $1,2,6$ at a branch node, all edges label 3 | $\QQ$ | 9 | 1 | $(10,45,120,210,252,210,120,45,10,1)$ | $0$ |
:::

::: {.proposition #prop:zero-cusp-lattice-types title="The $0$-cusp lattices by type"}

The even $2$-elementary hyperbolic lattices of types $(9,9,1)$, $(10,10,0)$ and $(10,8,0)$ are $\I_{1,8}(2)$, $U(2)\oplus E_8(2)$ and $U\oplus E_8(2)$.
The first is the Coble $0$-cusp lattice and the other two are the two Enriques $0$-cusp lattices (@thm:zero-cusp-chambers).
:::

::: {.proof}

By @thm:two-elementary-classification an indefinite even $2$-elementary lattice is determined by its signature, $a$ and $\delta$, so it suffices to compute these invariants.
The types of $U(2)\oplus E_8(2)$ and $U\oplus E_8(2)$ are computed in @prop:sterk-cusp-quotients.
The lattice $\I_{1,8}$ is odd unimodular of rank $9$, so $\I_{1,8}(2)$ is even with discriminant group $\tfrac12\I_{1,8}(2)/\I_{1,8}(2)\cong(\ZZ/2)^9$, and $a = 9$.
Its quadratic form takes the value $\tfrac12 y^2$ on the class of $\tfrac12 y$, which is not in $\ZZ$ when $y^2$ is odd, so $\delta = 1$.
The identification with the $0$-cusp lattices is @thm:zero-cusp-chambers.
:::

## Elliptic subdiagram enumerations

::: {.example #ex:sterk-elliptic-subdiagram-counts title="Connected elliptic subdiagrams of the folded Sterk diagrams"}

The numbers of connected elliptic subdiagrams of the folded Sterk diagrams, counted without any quotient by diagram symmetries, are:

| Cusp | Elliptic subdiagrams | Node/rank range |
| --- | --- | --- |
| Sterk 1 | 121 | 0-8 |
| Sterk 2 | 65 | 0-9 |
| Sterk 3 | 67 | 0-8 |
| Sterk 4 | 78 | 0-8 |
| Sterk 5 | 119 | 0-8 |

The types that occur are the mixed-norm systems $A_n(2)$, $B_n(2)$, $D_n(2)$, $E_n(2)$ and $G_2$.
At rank $8$ the Sterk 1 diagram has $4$ subdiagrams of type $A_8(2)$, $4$ of type $E_8(2)$ and $8$ of type $D_8(2)$.
:::

Related: [root vectors and folded Sterk diagrams](#sec-root-vectors-and-folded-sterk-diagrams), [computational toolchain and recipe](#sec-computational-toolchain-and-recipe), [Sterk root counts and computed chambers](#sec-sterk-root-counts-and-computed-chambers).
