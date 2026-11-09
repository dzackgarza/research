# Cusp Diagrams

::: {#fig-nikulin-table .figure}
\begin{tikzpicture}[x=0.6cm, y=0.6cm]
\pic {object=nikulin/two-elementary-table};
\end{tikzpicture}

Nikulin's table of even $2$-elementary lattices. White nodes are $\delta=0$, black are $\delta=1$, double circled are $\delta = 0,1$.
:::

## Mirror moves {#sec-mirror-moves}

The mirror move algorithm of [@AE22, Thm. 5.10], applied to the $2$-elementary lattice $S_\Co = (11, 11, 1)_1$, gives the 0-cusps and 1-cusps of $\fco$ in @fig-mirror-moves-coble.

::: {#fig-mirror-moves-coble .figure}
\begin{tikzpicture}
\pic[mirror targets=all] {object=mirror-moves/coble};
\end{tikzpicture}

Blue (resp. red) indicate lattices which are valid (resp. invalid) targets of mirror moves.
:::

By @thm:unpolarized-cusps there is one $\Orth^+(T_\Co)$-orbit of $0$-cusps, represented by an isotropic vector $v_0$ with

$$
v_0^{\perp T_{\Co}}/\generators{v_0} \cong (9,9,1)_1 \cong \generators{2} \oplus E_{8}(2)
$$

The group $\Gamma_\Co$ is not transitive on the primitive isotropic vectors (@lem:stable-orthogonal-not-transitive); it has $527$ orbits of them, one for each nonzero isotropic class of $A_{T_\Co}$ (@thm:cusp-lifting).
This $0$-cusp $v_0$ is incident to one $\Orth^+(T_\Co)$-orbit of $1$-cusps, represented by an isotropic plane $J = \generators{v_0, v_1}$ with

$$
J^{\perp T_{\Co}}/\generators{J} \cong (7,7,1)_0 \cong A_1^{\oplus 7} ,
$$

where $v_1 \in v_0^{\perp T_{\Co}}/\generators{v_0}$.
In the diagrammatic language of [@AE22 Fig. 1, Thm. 5.10], this corresponds to a composite of two even ordinary mirror moves, with $H = U(2)$, summarized in the following mirror move diagram:

::: {#fig-mirror-moves-coble-simplified .figure}
\begin{tikzpicture}
\pic {object=mirror-moves/coble};
\end{tikzpicture}

The mirror moves for $S_{\Co} = (11,11,1)_1$.
:::

The $0$-cusp $v_0$ corresponds to a Type $\rm{III}$ boundary, and the $1$-cusp $J$ to a Type $\rm{II}$ boundary.
By [@AE22, §5] such isotropic vectors are unique up to $\Orth(T_\Co)$, with representatives

- $v_0 = e'$,

- $v_1 = 2h + \alpha_1 + \alpha_2$.

Then $v_0^2 = v_1^2 = 0$, $v_1 \in v_0^{\perp T_{\Co}}/\generators{v_0}$ and $v_0v_1 = 0$, so $J \definedas \generators{v_0, v_1}$ is an isotropic plane.
Write $\div_{T_{\Co}}(v_0, v_1) \definedas \bigl(\div_{T_{\Co}}(v_0), \div_{T_{\Co}}(v_1)\bigr)$; then $\div_{T_{\Co}}(v_0, v_1) = (2, 2)$.

::: {.example #ex:coble-cusp-divisibilities title="Divisibilities of $v_0$ and $v_1$"}

| Lattice | Image of $v_0$ | Image of $v_1$ | Divisibility |
| :-------- | :------------- | :----------------------------------------------------------------- | :----------- |
| $T_{\Co}$ | $e'$ | $2h + \alpha_1 + \alpha_2$ | $(2, 2)$ |
| $\ten$ | $e'$ | $2e + 2f + \alpha_1 + \alpha_2$ | $(2, 2)$ |
| $\tdp$ | $e'$ | $2e + 2f + \alpha_1 + \tilde\alpha_1 + \alpha_2 + \tilde \alpha_2$ | $(2, 1)$ |

: Images of the isotropic vectors of $T_{\Co}$ and their divisibilities. {#tbl-coble-cusp-divisibilities}

In $\tdp$ the image of $v_0$ is $e'\in U(2)$ and $e'f' = 2$, so $\div_{\tdp}(v_0) = 2$. Since $v_1\alpha_3 = 1$, $\div_{\tdp}(v_1) = 1$.
:::

::: {.example #ex:coble-cusp-parabolic title="The maximal parabolic subdiagram at $v_0$"}

The Coxeter diagram $G_{(9,9,1)_1}$ of $v_0^{\perp T_\Co}/\generators{v_0}\cong\generators{2}\oplus E_8(2)$ (@fig-coble-coxeter-diagrams) has exactly one maximal parabolic subdiagram, of type $\wB_7(2)$ (@fig-coble-cusp-9-9-1-parabolics).
By @thm:unpolarized-cusps the $0$-cusp $v_0$ is incident to exactly one $\Orth^+(T_\Co)$-orbit of $1$-cusps.
:::
