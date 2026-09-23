# Cusp diagrams of the Enriques, Coble and Sterk moduli spaces

The mirror move algorithm of [Cusp Diagrams](cusp-diagram-calculations.md#sec:mirror-moves) is applied here to the three moduli spaces the correspondence relates: the unpolarized Enriques moduli space $\fen$, the unpolarized Coble moduli space $\fco$, and Sterk's $\fent$.
Each section records the cusp diagram, the Coxeter diagrams of its 0-cusps, and the maximal parabolic subdiagrams that determine the adjacent 1-cusps.

## The Enriques moduli space

We recall from [@AEGS25] the cusp diagram for $\fen$, the moduli space of unpolarized Enriques surfaces, in @fig-enriques-cusps and the corresponding Coxeter diagrams in @fig-enriques-coxeter-diagrams.

::: {#fig-enriques-cusps .figure}
\input{tikz/fig_Cusp_Diagram_En.tex}

Cusp diagram for $\fen = F_{\EnriquesInvariants}$ corresponding to $\ten = U \oplus E_{10}(2)$.
:::

This can be recovered using the mirror move algorithm:

::: {#fig-mirror-moves-enriques-simplified .figure}
\input{tikz/mirror_moves_enriques_simplified.tex}

The mirror moves for $\sen = \EnriquesInvariants_1$.
:::

::: {#fig-enriques-coxeter-diagrams .figure}
\input{tikz/fig_Coxeter_Diagrams_En_10_10_0_10_8_0.tex}

Coxeter diagrams $G_{\EnriquesInvariants_1} = G_{E_{10}(2)}$ and $G_{(10, 8, 0)_1} = G_{U \oplus E_8(2)}$.
:::

The maximal parabolic subdiagrams for $\EnriquesInvariants$ and $(10, 8, 0)$ are shown in @fig-enriques-maximal-parabolics-10-10-0 and @fig-enriques-maximal-parabolics-10-8-0 respectively.

::: {#fig-enriques-maximal-parabolics-10-10-0 .figure}
\input{tikz/fig_Maximal_Parabolic_E8_2_En_10_10_0.tex}

The unique maximal parabolic $\widetilde{E}_8(2)$ in $\EnriquesInvariants_1$, corresponding to the one-cusp $(8, 8, 0)_0$ in $\fen$.
:::

::: {#fig-enriques-maximal-parabolics-10-8-0 .figure}
\input{tikz/fig_Maximal_Parabolics_E8_B8_En_10_8_0.tex}

The two maximal parabolics $\widetilde{E}_8$, $\widetilde{B}_8$ in $(10, 8, 0)_1$ corresponding to the 1-cusps $(8, 8, 0)_0$ and $(8, 6, 0)_0$ respectively.
:::

## The Coble moduli space

Applying the same mirror moves, we obtain the cusp diagram for $\fco$, the moduli space of unpolarized Coble surfaces, shown in @fig-coble-cusps.

::: {#fig-coble-cusps .figure}
\input{tikz/fig_Cusp_Diagram_Co.tex}

Cusp diagram for $\fco = F_{(11, 11, 1)}$ where $T_\Co = \gens{2} \oplus E_{10}(2)$.
:::

The corresponding Coxeter diagrams are computed in [@AN06] and [@AEGS25], and shown in @fig-coble-coxeter-diagrams. Only the maximal parabolic subdiagrams of $(9, 9, 1)$ are relevant when determining 1-cusps, and these are shown in @fig-coble-cusp-9-9-1-parabolics.

::: {#fig-coble-coxeter-diagrams .figure}
\input{tikz/fig_Coxeter_Diagram_Co_9_9_1.tex}

The Coxeter diagram $G_{(9,9,1)_1} = G_{\gens{2} \oplus E_8(2)}$.
:::

::: {#fig-coble-cusp-9-9-1-parabolics .figure}
\input{tikz/fig_Maximal_Parabolic_B7_2_Co_9_9_1.tex}

The unique maximal parabolic subdiagram $\widetilde{B}_7(2)$ of $(9, 9, 1)_1$, corresponding to single one-cusp $(7, 7, 1)_0$ in $\fco$.
:::

We note that $G_{(9, 9, 1)_1}$ has precisely one maximal parabolic subdiagram of the form $\tilde B_7(2)$, verifying that there is only one adjacent 1-cusp to the unique 0-cusp in $\fco$.
We also note the correspondence between the maximal parabolic $\tilde B_8(2)$ in $\fen$, and $\tilde B_7(2)$ in $\fco$, and furthermore that $G_{(10, 8, 0)_1}$ can be obtained from $G_{(9, 9, 1)_1}$ by inserting one new node.
This correspondingly transforms the $\tilde B_7(2)$ subdiagram of $G_{(9, 9, 1)_1}$ into the $\tilde B_8(2)$ subdiagram of $G_{(10, 8, 0)_1}$.

## Sterk's moduli space and the K3 cusps

::: {.Remark}

We recall Sterk's cusp diagram for $\fent$:

::: {#fig-sterk-cusp-diagram .figure}
\input{tikz/dissertation/cusp_diagrams/FEn2-cusp-diagram.tikz}

Sterk's cusp diagram for $\fent$.
:::

We have the following divisibilities in various lattices:

| Sterk Cusp | Vector                           | $\mathrm{div}_{\ten}$ | $\mathrm{div}_{T_{\Kthree}}$ |
| :--------- | :------------------------------- | :--------------------- | :------------------------------- |
| 1          | $e$                              | 1                      | 1                                |
| 2          | $e'$                             | 2                      | 2                                |
| 3          | $e' + f' + \overline{\alpha}_8$  | 2                      | 1                                |
| 4          | $2e' + f' + \overline{\alpha}_1$ | 2                      | 1                                |
| 5          | $2e + 2f + \overline{\alpha}_1$  | 2                      | 1                                |

: Isotropic vectors in $\fent$ and their divisibilities.
:::

::: {.Remark}

We recall the cusp diagram for $F_{(2,2,0)}$:

::: {#fig-220-cusp-diagram .figure}
\input{tikz/fig_Cusp_Diagram_220.tex}

Cusp diagram for $F_{(2,2,0)}$.
:::
:::
