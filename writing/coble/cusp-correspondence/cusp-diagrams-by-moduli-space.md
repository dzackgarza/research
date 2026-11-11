# Cusp diagrams of the Enriques, Coble and Sterk moduli spaces {#sec-cusp-diagrams-by-moduli-space}

## The Enriques moduli space

@fig-enriques-cusps is the cusp diagram of the moduli space $\fen$ of unpolarized Enriques surfaces [@AEGS25], and @fig-enriques-coxeter-diagrams gives the corresponding Coxeter diagrams.

::: {#fig-enriques-cusps .figure}
\input{tikz/fig_Cusp_Diagram_En.tex}

Cusp diagram for $\fen = F_{\EnriquesInvariants}$ corresponding to $\ten = U \oplus E_{10}(2)$.
:::

The mirror moves of @sec-mirror-moves in @fig-mirror-moves-enriques-simplified give the same diagram.

::: {#fig-mirror-moves-enriques-simplified .figure}
\begin{tikzpicture}
\pic {object=mirror-moves/enriques};
\end{tikzpicture}

The mirror moves for $\sen = \EnriquesInvariants_1$.
:::

::: {#fig-enriques-coxeter-diagrams .figure}
\input{tikz/fig_Coxeter_Diagrams_En_10_10_0_10_8_0.tex}

Coxeter diagrams $G_{\EnriquesInvariants_1} = G_{E_{10}(2)}$ and $G_{(10, 8, 0)_1} = G_{U \oplus E_8(2)}$.
:::

The maximal parabolic subdiagrams for $\EnriquesInvariants$ and $(10, 8, 0)$ are shown in @fig-enriques-maximal-parabolics-10-10-0 and @fig-enriques-maximal-parabolics-10-8-0 respectively.

::: {#fig-enriques-maximal-parabolics-10-10-0 .figure}
\input{tikz/fig_Maximal_Parabolic_E8_2_En_10_10_0.tex}

The unique maximal parabolic $\wE_8(2)$ in $\EnriquesInvariants_1$, corresponding to the one-cusp $(8, 8, 0)_0$ in $\fen$.
:::

::: {#fig-enriques-maximal-parabolics-10-8-0 .figure}
\input{tikz/fig_Maximal_Parabolics_E8_B8_En_10_8_0.tex}

The two maximal parabolics $\wE_8(2)$, $\wB_8(2)$ in $(10, 8, 0)_1$ corresponding to the 1-cusps $(8, 8, 0)_0$ and $(8, 6, 0)_0$ respectively.
:::

::: {.example #ex:enriques-10-8-0-parabolic-types title="The types of the maximal parabolics of $G_{(10,8,0)_1}$ and $G_{(9,9,1)_1}$"}

In @fig-enriques-coxeter-diagrams the diagram $G_{(10,8,0)_1}$ has nine roots of square $-4$, numbered $1,\ldots,9$ as the diagram $E_9$ in Bourbaki's numbering, and one root $10$ of square $-2$, joined to root $9$ by an edge of weight $4$.
The diagram $G_{(9,9,1)_1}$ of @fig-coble-coxeter-diagrams has eight roots of square $-4$, numbered as $E_8$, and one root $9$ of square $-2$, joined to root $8$ by an edge of weight $4$.
For roots $h_i$, $h_j$ joined by an edge of weight $m$, $\abs{h_i\cdot h_j} = \sqrt{h_i^2h_j^2}\cos(\pi/m)$, so $h_i\cdot h_j = 2$ for each edge of both diagrams.

1. On the vertex set $\theset{1,\ldots,9}$ of $G_{(10,8,0)_1}$, minus the Gram matrix of the roots is $2$ times the Cartan matrix of $\wE_8$, so this parabolic is $\wE_8(2)$.
2. On the vertex set $\theset{2,\ldots,10}$ of $G_{(10,8,0)_1}$, minus the Gram matrix of the roots is $2$ times the Gram matrix of the simple roots $-(e_1+e_2), e_1-e_2, \ldots, e_7-e_8, e_8$ of $\wB_8$, whose short roots have square $1$ as in @def:root-system-Bn-Cn. So this parabolic is $\wB_8(2)$.
3. On the vertex set $\theset{2,\ldots,9}$ of $G_{(9,9,1)_1}$, the same comparison with $\wB_7$ gives $\wB_7(2)$.

Each of these matrices is positive semidefinite of rank $8$, $8$ and $7$ respectively.
This is a computation in SageMath with exact rational arithmetic.
:::

## The Coble moduli space

The same mirror moves give the cusp diagram of the quotient $F^{\mathrm{un}}_\Co = \bD(T_\Co)/\Orth(T_\Co)$ (@def:gamma-co-groups) in @fig-coble-cusps.

::: {#fig-coble-cusps .figure}
\input{tikz/fig_Cusp_Diagram_Co.tex}

Cusp diagram for $F^{\mathrm{un}}_\Co = F_{(11, 11, 1)}$ where $T_\Co = \generators{2} \oplus E_{10}(2)$.
:::

@fig-coble-coxeter-diagrams draws the Coxeter diagram of $(9,9,1)_1$; @thm:coble-cusp-chamber states its bond list, its $f$-vector and its one ideal vertex. The Enriques-side diagrams are the folded diagrams of [@AEGS25], Figures 7 and 8.
The 1-cusps are determined by the maximal parabolic subdiagrams of $(9, 9, 1)_1$, in @fig-coble-cusp-9-9-1-parabolics.

::: {#fig-coble-coxeter-diagrams .figure}
\begin{tikzpicture}
\pic {object=coxeter/vinberg-9-9-1};
\end{tikzpicture}

The Coxeter diagram $G_{(9,9,1)_1} = G_{\generators{2} \oplus E_8(2)}$.
:::

::: {#fig-coble-cusp-9-9-1-parabolics .figure}
\input{tikz/fig_Maximal_Parabolic_B7_2_Co_9_9_1.tex}

The unique maximal parabolic subdiagram $\wB_7(2)$ of $(9, 9, 1)_1$, corresponding to single one-cusp $(7, 7, 1)_0$ in $F^{\mathrm{un}}_\Co$.
:::

::: {.example #ex:coble-cusp-9-9-1-parabolic title="The 1-cusps adjacent to the 0-cusp of $F^{\mathrm{un}}_\Co$"}

By @thm:coble-cusp-chamber, exactly one of the nine one-node deletions of the Coxeter diagram $G_{(9, 9, 1)_1}$ is parabolic, and it has type $\tilde B_7(2)$ (@fig-coble-cusp-9-9-1-parabolics).
So, for the group $\Orth^+(T_\Co)$, the $0$-cusp represented by $v_0$ is incident to exactly one $1$-cusp, and its boundary lattice is $(7,7,1)_0$.
For the stable group $\widetilde\Orth^+(T_\Co)$, the primitive isotropic lines of $T_\Co$ form $527$ orbits, one for each nonzero isotropic class of $A_{T_\Co}$ (@thm:cusp-lifting).
At cusp $2$ of $\fentwo$, the facet of the unique white node $r_{10}$ has the nine-wall diagram $G_{(9,9,1)_1}$ with the induced bond $8-9$ double (@prop:facet-angles-aegs), and all nine white candidates of [@AEGS25], Figures 7--8, have perpendicular lattice $T_\Co$ (@prop:cusp-white-root-complements).

:::

## Sterk's moduli space and the K3 cusps

::: {#fig-sterk-cusp-diagram .figure}
\begin{tikzpicture}
\pic {object=bb-cusps/fen2};
\end{tikzpicture}

Sterk's cusp diagram for $\fentwo$.
:::

::: {.example #ex:sterk-isotropic-divisibilities title="Divisibilities of the Sterk isotropic vectors"}

The isotropic vectors that represent the cusps of @fig-sterk-cusp-diagram have the following divisibilities in $\ten$ and in $T_{\Kthree}$.

| Sterk Cusp | Vector | $\mathrm{div}_{\ten}$ | $\mathrm{div}_{T_{\Kthree}}$ |
| :--------- | :------------------------------- | :--------------------- | :------------------------------- |
| 1 | $e$ | 1 | 1 |
| 2 | $e'$ | 2 | 2 |
| 3 | $e' + f' + \overline{\alpha}_8$ | 2 | 1 |
| 4 | $2e' + f' + \overline{\alpha}_1$ | 2 | 1 |
| 5 | $2e + 2f + \overline{\alpha}_1$ | 2 | 1 |

: Isotropic vectors in $\fentwo$ and their divisibilities.
:::

::: {#fig-220-cusp-diagram .figure}
\begin{tikzpicture}
\pic {object=bb-cusps/f220};
\end{tikzpicture}

Cusp diagram for $\fttz$.
:::

::: {.remark #rmk:diagrams-use-the-mechanism title="The mechanism behind these diagrams"}
The diagrams this page draws are the reflection data at the $0$-cusps of the three moduli spaces; the mechanism by which such data determine the boundary of the compactification, the hypotheses under which it holds, and the replacements in use where the data fail are gathered in @sec-reflection-data-and-replacements.
:::
