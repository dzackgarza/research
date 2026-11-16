# Cusp diagrams of the Enriques, Coble and Sterk moduli spaces {#sec-cusp-diagrams-by-moduli-space}

The archived working picture @fig-archived-cusp-correspondence-sketch juxtaposes the Enriques and Sterk boundary curves and marks proposed correspondences between their labelled cusps. Its handwritten checks and question marks record the stage of the calculation; the established maps and lattice obstructions are given in @sec-enriques-coble-correspondence.

![An archived working diagram of cusp correspondences, including tentative identifications and symmetry checks.](/rendered/valery_colorful_diagram.png){#fig-archived-cusp-correspondence-sketch}

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

For the upper diagram, number the ten vertices along its nine-vertex chain and its branch as in the archived $E_{10}$ drawing. Its Cartan matrix is $A=2I_{10}-\operatorname{Adj}(T_{2,3,7})$, with edges
$$
(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,9),(7,10).
$$
Thus the Gram matrix of the norm-$-2$ roots of $E_{10}\cong\mathrm{II}_{1,9}$ in this simple system is $-A$, and the norm-$-4$ roots in $E_{10}(2)$ have Gram matrix $-2A$. This records the Cartan matrix and its sign and scale conventions alongside the native diagram [@AE22, Fig. 3].

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

::: {#fig-k3-cusp-18-2-0-vinberg .figure}
\begin{tikzpicture}
\pic[root labels=index] {object=coxeter/vinberg-18-2-0};
\end{tikzpicture}

The $22$-node Vinberg diagram of $(18,2,0)_1$, with indices $1$ through $22$ used for its diagram automorphisms.
:::

The degree-four K3 cusp with boundary lattice $(18,0,0)_1\cong U\oplus E_8^2$ has the following Vinberg diagram. Its two maximal parabolic subdiagrams have types $2\widetilde E_8$ and $\widetilde D_{16}$, giving the two one-cusp types adjacent to this zero-cusp.

::: {#fig-k3-cusp-18-0-0-vinberg .figure}
\begin{tikzpicture}
\pic {object=coxeter/vinberg-18-0-0};
\end{tikzpicture}

The canonical Vinberg diagram of $(18,0,0)_1$, reconstructed from the archived `Vinberg1` example.
:::

::: {#fig-k3-cusp-18-0-0-parabolics .figure}
\input{tikz/dissertation/coxeter_diagrams/18_0_0_Parabolic1.tikz}
\input{tikz/dissertation/coxeter_diagrams/18_0_0_Parabolic2.tikz}

The two maximal parabolic subdiagrams of $(18,0,0)_1$.
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

In @fig-220-cusp-diagram, a single arrow from a zero-cusp $[\ZZ e]$ to a one-cusp $[\Pi]$ means that the $2$-elementary discriminant ranks of $e^\perp/e$ and $\Pi^\perp/\Pi$ agree. A double arrow means that the rank drops by $2$ on passage to $\Pi^\perp/\Pi$ [@AE22, §§5C–5D]. This arrow convention records a discriminant change; Scattone's incidence multiplicity $\mu$ is defined separately in @sec-scattone-cusp-method.

The forgetful cusp maps from $\fentwo$ can be read in the following two source-native composites. Under $\fentwo\to\fen$, cusp $1$ maps to the $E_{10}(2)$ boundary lattice and cusps $2$--$5$ map to $U\oplus E_8(2)$. Under $\fentwo\to\fttz$, cusp $2$ maps to $U\oplus E_8^2$ and cusps $1,3,4,5$ map to $U(2)\oplus E_8^2$ (@prop:fen2-folded-coxeter; @ex:sterk-isotropic-divisibilities).

::: {#fig-sterk-to-enriques-cusp-map .figure}
\input{tikz/dissertation/cusp_correspondence_one.tex}

The cusp diagram of $\fentwo$ above that of $\fen$ under the forgetful map.
:::

::: {#fig-sterk-to-k3-cusp-map .figure}
\input{tikz/dissertation/cusp_correspondence_two.tex}

The cusp diagram of $\fentwo$ above that of $\fttz$ under the forgetful map.
:::

The general polarized K3 moduli spaces of degrees two and four have different Baily–Borel boundaries. In both cases there is one zero-cusp. The degree-two space has four one-cusps (@prop:scattone-niemeier-complements); the degree-four space has nine, with generalized complement types listed in @sec-scattone-cusp-method.

::: {#fig-degree-two-k3-cusp-diagram .figure}
\begin{tikzpicture}
\pic {object=bb-cusps/f2};
\end{tikzpicture}

The four one-cusps incident to the zero-cusp of the degree-two K3 moduli space.
:::

::: {#fig-degree-four-k3-cusp-diagram .figure}
\begin{tikzpicture}
\pic {object=bb-cusps/f4};
\end{tikzpicture}

The nine one-cusps incident to the zero-cusp of the degree-four K3 moduli space.
:::
