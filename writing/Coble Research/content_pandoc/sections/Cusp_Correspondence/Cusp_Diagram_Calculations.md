# Cusp Diagrams

::: {.remark}

We recall the mirror move algorithm from [@AE22].
We have Nikulin's 2-elementary diagram:

![White nodes are $\delta=0$, black are $\delta=1$, double circled are $\delta = 1,2$.](rendered/nikulin_2elementary_table.svg){#fig:nikulin_table}
:::

### Mirror moves {#sec:mirror-moves}

Having identified the 2-elementary lattice $S_\Co = (11, 11, 1)_1$, one can apply the mirror move algorithm of [@AE22 Thm. 5.10] to determine the 0-cusps and 1-cusps of $F_\Co$.
The outcome of the algorithm is summarized by the following tree:

![Blue (resp. red) indicate lattices which are valid (resp. invalid) targets of mirror moves.](rendered/fig_Mirror_Move_Co_Lattices.svg){#fig:mirror-moves-coble}

Thus $F_\Co$ has one 0-cusp corresponding to an isotropic vector $v_0$ with

$$
v_0^{\perp T_{\Co}}/\gens{v_0} \cong (9,9,1)_1 \cong \gens{2} \oplus E_{8}(2)
$$

Moreover, this 0-cusp $v_0$ is incident to one 1-cusp $C_0$ corresponding to an isotropic plane $J = \gens{v_0, v_1}$ with

$$
J^{\perp T_{\Co}}/\gens{J} \cong (7,7,1)_0 \cong A_1^{\oplus 7} ,
$$

where $v_1 \in v_0^{\perp T_{\Co}}/\gens{v_0}$.
In the diagrammatic language of [@AE22 Fig. 1, Thm. 5.10], this corresponds to a $U^2$ move and can be summarized in the following mirror move diagram as a composition of two even ordinary $U(2)$-type moves:

![The mirror moves for $S_{\Co} = (11,11,1)_1$.](rendered/mirror_moves_coble_simplified.svg){#fig:mirror-moves-coble-simplified}

Note that $v_0$ corresponds to a Type $\rm{III}$ boundary, while $C_0$ corresponds to a type $\rm{II}$ boundary.
It is easily verified that the Coxeter diagram $G_{(9,9,1)_1}$ at $v_0$ has precisely one maximal parabolic subdiagram, corresponding to a finite-index root lattice of type $B_7$.
We note that by [@AE22 §5], such isotropic vectors are unique up to $\Orth(T_\Co)$, and so we can choose representatives:

- $v_0 = e'$,

- $v_1 = 2h + \alpha_1 + \alpha_2$.

Calculations verify that $v_0^2 = v_1^2 = 0$, that $v_1 \in v_0^{\perp T_{\Co}}/\gens{v_0}$, and that $v_0v_1 = 0$, and thus $J \da \gens{v_0, v_1}$ is an admissible choice of an isotropic plane.
We further note that $\div_{T_{\Co}}(v_0) = \div_{T_{\Co}}(v_1) = 2$, which will be an important invariant for establishing a correspondence to cusps of other moduli spaces.
For an isotropic plane $J$, we denote the divisibilities of the constituent generating vectors as a tuple $(d_1, d_2)$, and in this convention we have $\div_{T_{\Co}}(v_0, v_1) = (2, 2)$.

By [@CDL25 Prop. 5.46], there is an open embedding $F_{(11, 11, 1)} \injects F_{(10,10,0)}$, i.e. $F_\Co \injects F_\En$, realizing $F_\Co$ as the coarse space of marked Coble surfaces with $n=1$, where $n$ is the number of boundary components in $C = C_1 + \cdots + C_n$.
The image is an open subset of a closed irreducible subset of $\cH_{-2}/\Gamma_\En$.
By [@CDL25 Thm. 5.8.2], the coarse space of $F_\Co$ is a rational variety, and since $F_\En$ is quasiprojective, so too is $F_\Co$.
Moreover, $\partial \overline{F_{\En}}^{\mathrm{BB}}$ consists of $F_{\Co}$ and two modular curves $X$ and $X_0(2)$ by [@CDL25 Rem.5.9.12], and the closure of $\cH_{-2}$ contains the modular curve $X$.

::: {.remark}

We note the divisibilities of the $v_i$ under various lattice embeddings:

| Coble Vector | Representative             | $\mathrm{div}_{T_{\Co}}$ | $\mathrm{div}_{T_{\En}}$ | $\mathrm{div}_{T_{\dP}}$ |
| :----------- | :------------------------- | :----------------------- | :----------------------- | :----------------------- |
| $v_0$        | $e'$                       | 2                        | 2                        | 2                        |
| $v_1$        | $2h + \alpha_1 + \alpha_2$ | 2                        | 2                        | 1                        |

: Divisibilities of the isotropic vectors $v_0, v_1$ under the embeddings of $T_{\Co}$.\label{tbl:coble-vector-divisibilities}

More concisely:

| Lattice   | Image of $v_0$ | Image of $v_1$                                                     | Divisibility |
| :-------- | :------------- | :----------------------------------------------------------------- | :----------- |
| $T_{\Co}$ | $e'$           | $2h + \alpha_1 + \alpha_2$                                         | $(2, 2)$     |
| $T_{\En}$ | $e'$           | $2e + 2f + \alpha_1 + \alpha_2$                                    | $(2, 2)$     |
| $T_{\dP}$ | $e'$           | $2e + 2f + \alpha_1 + \tilde\alpha_1 + \alpha_2 + \tilde \alpha_2$ | $(2, 1)$     |

: Images of the isotropic vectors of $T_{\Co}$ and their divisibilities.\label{tbl:coble-cusp-divisibilities}

The divisibilities in $T_{\dP}$ can be seen as follows: the image of $v_0$ in $T_{\dP}$ is $e'\in U(2)$ and $e'f' = 2$, while $\div_{T_{\dP}}(v_1) = 1$ follows from the fact that $v_1\alpha_3 = 1$.
:::

::: {.remark}

As further proof that the cusp diagram of $F_{\Co}$ is correct, we can use the theory of Coxeter diagrams.
Given an isotropic vector $e\in L$ a lattice of signature $(2, n)$, the lattice $e^{\perp L}/\gens{e}$ is a hyperbolic lattice equipped with a root system $R_e$ with a Coxeter diagram $G_e$.
Generally, when $e$ corresponds to a 0-cusp in a Baily-Borel compactification, the adjacent 1-cusps correspond precisely to maximal parabolic subdiagrams of $G_e$.
The cusp diagram of $F_{\Co}$ suggests that the 0-cusp $v_0$ should have a Coxeter diagram $G_{v_0}$ with precisely one maximal parabolic subdiagram.
One can run Vinberg's algorithm to determine the Coxeter diagram for $v_0$, and it is a straightforward check to determine that there is indeed a unique maximal parabolic subdiagram of the form $\tilde B_7(2)$; see \cref{fig:coble-cusp-9-9-1-parabolics}.
:::
