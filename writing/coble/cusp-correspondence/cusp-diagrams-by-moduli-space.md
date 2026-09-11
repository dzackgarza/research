# Cusp diagrams of the Enriques, Coble and Sterk moduli spaces

The mirror move algorithm of [Cusp Diagrams](cusp-diagram-calculations.md#sec:mirror-moves) is applied here to the three moduli spaces the correspondence relates: the unpolarized Enriques moduli space $F_\En$, the unpolarized Coble moduli space $F_\Co$, and Sterk's $F_{\En, 2}$.
Each section records the cusp diagram, the Coxeter diagrams of its 0-cusps, and the maximal parabolic subdiagrams that determine the adjacent 1-cusps.

## The Enriques moduli space

We recall from [@AEGS25] the cusp diagram for $F_\En$, the moduli space of unpolarized Enriques surfaces, in @fig-enriques-cusps and the corresponding Coxeter diagrams in @fig-enriques-coxeter-diagrams.

![Cusp diagram for $F_\En = F_{(10, 10, 0)}$ corresponding to $T_\En = U \oplus E_{10}(2)$.](rendered/fig_Cusp_Diagram_En.svg){#fig-enriques-cusps}

This can be recovered using the mirror move algorithm:

![The mirror moves for $S_{\En} = (10,10,0)_1$.](rendered/mirror_moves_enriques_simplified.svg){#fig-mirror-moves-enriques-simplified}

![Coxeter diagrams $G_{(10, 10, 0)_1} = G_{E_{10}(2)}$ and $G_{(10, 8, 0)_1} = G_{U \oplus E_8(2)}$.](rendered/fig_Coxeter_Diagrams_En_10_10_0_10_8_0.svg){#fig-enriques-coxeter-diagrams}

The maximal parabolic subdiagrams for $(10, 10, 0)$ and $(10, 8, 0)$ are shown in @fig-enriques-maximal-parabolics-10-10-0 and @fig-enriques-maximal-parabolics-10-8-0 respectively.

![The unique maximal parabolic $\widetilde{E}_8(2)$ in $(10, 10, 0)_1$, corresponding to the one-cusp $(8, 8, 0)_0$ in $F_\En$.](rendered/fig_Maximal_Parabolic_E8_2_En_10_10_0.svg){#fig-enriques-maximal-parabolics-10-10-0}

![The two maximal parabolics $\widetilde{E}_8$, $\widetilde{B}_8$ in $(10, 8, 0)_1$ corresponding to the 1-cusps $(8, 8, 0)_0$ and $(8, 6, 0)_0$ respectively.](rendered/fig_Maximal_Parabolics_E8_B8_En_10_8_0.svg){#fig-enriques-maximal-parabolics-10-8-0}

## The Coble moduli space

Applying the same mirror moves, we obtain the cusp diagram for $F_\Co$, the moduli space of unpolarized Coble surfaces, shown in @fig-coble-cusps.

![Cusp diagram for $F_\Co = F_{(11, 11, 1)}$ where $T_\Co = \gens{2} \oplus E_{10}(2)$.](rendered/fig_Cusp_Diagram_Co.svg){#fig-coble-cusps}

The corresponding Coxeter diagrams are computed in [@AN06] and [@AEGS25], and shown in @fig-coble-coxeter-diagrams. Only the maximal parabolic subdiagrams of $(9, 9, 1)$ are relevant when determining 1-cusps, and these are shown in @fig-coble-cusp-9-9-1-parabolics.

![The Coxeter diagram $G_{(9,9,1)_1} = G_{\gens{2} \oplus E_8(2)}$.](rendered/fig_Coxeter_Diagram_Co_9_9_1.svg){#fig-coble-coxeter-diagrams}

![The unique maximal parabolic subdiagram $\widetilde{B}_7(2)$ of $(9, 9, 1)_1$, corresponding to single one-cusp $(7, 7, 1)_0$ in $F_\Co$.](rendered/fig_Maximal_Parabolic_B7_2_Co_9_9_1.svg){#fig-coble-cusp-9-9-1-parabolics}

We note that $G_{(9, 9, 1)_1}$ has precisely one maximal parabolic subdiagram of the form $\tilde B_7(2)$, verifying that there is only one adjacent 1-cusp to the unique 0-cusp in $F_\Co$.
We also note the correspondence between the maximal parabolic $\tilde B_8(2)$ in $F_\En$, and $\tilde B_7(2)$ in $F_\Co$, and furthermore that $G_{(10, 8, 0)_1}$ can be obtained from $G_{(9, 9, 1)_1}$ by inserting one new node.
This correspondingly transforms the $\tilde B_7(2)$ subdiagram of $G_{(9, 9, 1)_1}$ into the $\tilde B_8(2)$ subdiagram of $G_{(10, 8, 0)_1}$.

## Sterk's moduli space and the K3 cusps

::: {.Remark}

We recall Sterk's cusp diagram for $F_{\En, 2}$:

![Sterk's cusp diagram for $F_{\En, 2}$.](rendered/sterk_cusp_diagram.svg){#fig-sterk-cusp-diagram}

We have the following divisibilities in various lattices:

| Sterk Cusp | Vector                           | $\mathrm{div}_{T_\En}$ | $\mathrm{div}_{T_{\mathrm{K3}}}$ |
| :--------- | :------------------------------- | :--------------------- | :------------------------------- |
| 1          | $e$                              | 1                      | 1                                |
| 2          | $e'$                             | 2                      | 2                                |
| 3          | $e' + f' + \overline{\alpha}_8$  | 2                      | 1                                |
| 4          | $2e' + f' + \overline{\alpha}_1$ | 2                      | 1                                |
| 5          | $2e + 2f + \overline{\alpha}_1$  | 2                      | 1                                |

: Isotropic vectors in $F_{\En, 2}$ and their divisibilities.
:::

::: {.Remark}

We recall the cusp diagram for $F_{(2,2,0)}$:

![Cusp diagram for $F_{(2,2,0)}$.](rendered/fig_Cusp_Diagram_220.svg){#fig-220-cusp-diagram}
:::
