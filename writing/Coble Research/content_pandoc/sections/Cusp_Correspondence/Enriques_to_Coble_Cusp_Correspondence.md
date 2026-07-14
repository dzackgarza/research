# Enriques to Coble correspondence

::: {#thm:cusp_correspondence .theorem}

The embedding $F_\Co\to F_\En$ induces the correspondence on boundary cusps of
the Baily-Borel compactifications shown in \cref{fig:enriques-coble-correspondence}.

![Cusp correspondence $F_\Co \to F_\En$.](rendered/fig_Cusp_Correspondence_Co_En.svg){#fig:enriques-coble-correspondence}

We prove the cusp correspondence by comparing divisibilities of isotropic
vectors at 0-cusps.

::: {#lem:divisibilityAlwaysTwoTco .lemma}

Any $v\in T_\Co$ satisfies $\di_{T_\Co}(v) = 2$ if there exists any
$v'\in T_\Co$ for which $v\cdot v' \neq 0$.

:::

::: {.proof}

Let $M_{T_\Co}$ be the Gram matrix for $T_\Co$, and note that since

$$
T_\Co = \gens{2} \oplus E_{10}(2) = \qty{\gens{1} \oplus E_{10}}(2)
,
$$

every entry in $M_{T_\Co}$ is 2-divisible.
Thus one can write
$M_{T_\Co} = 2A$ for some integral matrix $A$.
Letting $v' \in T_\Co$ be
any other vector not orthogonal to $v$, we have

$$
v\cdot v' = \langle v, M_{T_\Co}v' \rangle = \langle v, 2 Av' \rangle
= 2\langle v, Av' \rangle \neq 0
,
$$

$$
\begin{aligned}
v_1 &\da e' & w_1 &\da \eta(v_1) = \tilde e' \\
v_2 &\da 2h + \alpha_1 + \alpha_2 & w_2 &\da \eta(v_2) = 2\tilde e + 2\tilde f + \tilde\alpha_1 + \tilde\alpha_2 \\
J &\da \gens{v_1, v_2} & \tilde J &\da \gens{w_1, w_2}
\end{aligned}
$$

where $\langle \cdot, \cdot\rangle$ is the standard
Euclidean inner product.
Thus 2 divides $v\cdot v'$, and since
$\di_{T_\Co}(v) \in \ts{1, 2}$ for any $v \in T_\Co$, the
result follows.

:::

::: {#lem:divisibilityTcoOne .lemma}

Fixing
notation,

$$
\begin{aligned}
v_1 &\da e' & w_1 &\da \eta(v_1) = \tilde e' \\
v_2 &\da 2h + \alpha_1 + \alpha_2 & w_2 &\da \eta(v_2) = 2\tilde e + 2\tilde f + \tilde\alpha_1 + \tilde\alpha_2 \\
J &\da \gens{v_1, v_2} & \tilde J &\da \gens{w_1, w_2}
\end{aligned}
$$

We then have $\di_{T_\En}(w_1) = 2$.

:::

::: {.proof}

By \cref{lem:divisibilityAlwaysTwoTco}, we have in particular that
$v_1$ has divisibility 2 in $T_\Co$; moreover it is isotropic.
Since
there is a unique $\Gamma_\Co$-orbit of isotropic vectors in $T_\Co$,
one can associate $v_1$ to the unique 0-cusp of $F_\Co$, so that
$$(v_1)^{\perp T_\Co}/v_1 \cong (9,9,1) \cong \gens{2} \oplus E_8(2).$$

Since $\tilde e' \tilde f' = 2$, and $\tilde e'$ is orthogonal to the remaining
generators of $T_\En$, we have

$$
\di_{T_\En}(w_1) \da \di_{T_\En}(\eta(e'))
= \di_{T_\En}(\tilde e') = 2.
$$

:::

::: {#lem:w1_perp_calculation .lemma}

Cusp
$(9,9,1)$ maps to cusp $(10, 8, 0)$.

:::

::: {.proof}

The cusp correspondence follows from computing the lattice
$w_1^{\perp T_{\En}}/w_1$ under the primitive embedding $\eta$:

$$
{(\tilde e')^{\perp T_\En} \over \gens{\tilde e'}} =
{
\gens{\tilde{e}, \tilde{f}}
\oplus
\gens{\tilde{e}'}
\oplus
\gens{\tilde{\alpha}_1, \dots, \tilde{\alpha}_8}
\over
\gens{ \tilde{e}' }}\cong\gens{\tilde{e}, \tilde{f}} \oplus\gens{
\tilde{\alpha}_{1}, \dots, \tilde{\alpha}_{8}
} \cong U \oplus E_{8}(2) \cong (10,8,0).
$$

Alternatively, by [@AE22 Prop. 5.5], the isomorphism type of
$w_1^{\perp T_{\En}}/w_1$ is determined by $\mathrm{div}_{T_\En}(w_1)$; by
\cref{lem:divisibilityTcoOne} $\mathrm{div}_{T_\En}(w_1) = 2$.
Since the divisibility of the isotropic vector at the Enriques 0-cusp
$(10, 8,
0)$ is also 2, the correspondence follows.

:::

::: {#lem:1_cusp_correspondence .lemma}

Cusp $(7,7,1)$ maps to cusp $(8, 6, 0)$.

:::

::: {.proof}

The results follows from verifying that the unique orbit $J$ of a
primitive isotropic plane in $T_\Co$ satisfies
$J^{\perp T_\Co}/J \cong (7,7,1)$, and identifying the isomorphism type of its
image $\tilde J^{\perp T_\En}/\tilde J$ in $T_\En$.
One checks that both $v_2$ and $w_2$ are isotropic, and
$v_2 \in v_1^{\perp T_\Co}/v_1$, and so $J$ and $\tilde J$ define isotropic
planes in $T_\Co$ and $T_\En$ respectively.
By [@AE22 Prop. 5.5, Lem. 5.9], it suffices to show

$$
\di_{w_1^{\perp T_\En} /w_1}(w_2) \da \di_{U \oplus E_8(2)}(2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2)= 2
,
$$

since the isomorphism type of $\tilde J^\perp/\tilde J$ is uniquely
determined by the isomorphism type of $w_2^{\perp T_\En}/w_2$ in
$w_1^{\perp T_\En}/w_1$, which is in turn uniquely determined by the
characterization of $w_2$ as odd, even ordinary, or even characteristic
which by \cref{lem:w1_perp_calculation} is isomorphic to $U \oplus E_8(2)$.
One checks directly in coordinates: let $x+y\in U \oplus E_8(2)$ and
consider its pairing with $w_2$:

$$
(x+y)\cdot w_2
= (x+y)\cdot (2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2 )
= 2x\cdot (\tilde e + \tilde f) + y\cdot (\tilde \alpha_1 + \tilde \alpha_2)
,
$$

where we've used orthogonality relations.
We note that
the first term is evidently even, while the second term is even because
all pairings are either zero or divisible by two in the $E_8(2)$ summand
of $U \oplus E_8(2)$.

:::

::: {.remark}

This can also be proved by considering the divisorial presentation of
$F_{\Co}$ as $\cH_{-2}/\Orth(T_\En)$.
If $J'$ is an isotropic plane in
$T_\En$ generated by $x_1, x_2$ where both $x_i$ are orthogonal to a
$(-2)$-vector in $T_\En$, then the 1-cusp corresponding to $J'$ will be
contained in the closure of $\cH_{-2}$.
One checks that cusp
$(8, 6, 0)_0$ is associated to the isotropic plane

$$
J' = \gens{e', 2e + 2f + 2\bar\alpha_1} \subset T_\En
$$

where both
$e'$ and $2e + 2f + 2\bar\alpha_1$ are orthogonal to the $(-2)$-vector
$e-f\in T_{\En}$.
On the other hand, cusp $(8,8,0)$ does not satisfy
this property -- the vector $e\in T_\En$ is not orthogonal to any
$(-2)$-vectors in $T_\En$, and the isotropic plane at this cusp must
include $e$ as a generator.

:::

::: {.remark}

The two 1-cusps $(8,8,0)$ and $(8,6,0)$ in $F_\En$ are isomorphic to the
modular curves $X_0(2)$ and $X \da \overline{\bH / \SL_2(\bZ)}$
respectively, and by [@CDL24 Cor. 5.9.10] the 1-cusp $(7,7,1)$ in $F_\Co$ is isomorphic to $X$.
This can additionally be verified by
[@AE22 Prop. 5.13]: the 1-cusp $(7,7,1)$ in $T_\Co$ is
incident to exactly one 0-cusp, as is the 1-cusp $(8,6,0)$ in $T_\En$,
and thus the corresponding modular curves are both isomorphic to $X$.
We
conjecture that general correspondences on 1-cusps must preserve the
isomorphism types of the corresponding modular curves, yielding an
alternative proof of \cref{lem:1_cusp_correspondence}.

:::

::: {#lem:cusp_map_dP .lemma}

Let $\tilde w_i$ be the
images of $v_i$ in $T_\dP$ under the embedding described in \cref{lem:sequence_of_embeddings}.
Then

$$
\begin{aligned}
\tilde w_1^{\perp T_\dP}/\tilde w_1 &\cong (18, 0, 0)_1 \cong U \oplus E_8^2 \\
\tilde w_2^{\perp T_\dP}/\tilde w_2 &\cong (16, 0, 0)_0 \cong E_8^2
\end{aligned}
$$

Thus the embedding $F_\Co \injects F_{(2,2,0)}$ induces
the following maps on cusps:

$$
\begin{aligned}
    (9, 9, 1)_1 &\mapsto (18, 0, 0)_1 \\
    (7, 7, 1)_0 &\mapsto (16, 0, 0)_0
\end{aligned}
$$

:::

::: {.proof}

The map on 0-cusps follows from identifying
$\tilde w_1 = e' \in T_{\dP} = \gens{e,f} \oplus \gens{e', f'}\oplus \gens{\alpha_1,\cdots,\alpha_8}\oplus \gens{\tilde \alpha_1,\cdots, \tilde \alpha_8}$
and noting

$$
\begin{aligned}
{ (e')^{\perp T_\dP} \over e'} &\cong {\gens{e,f}
\oplus \gens{e'}\oplus \gens{\alpha_1,\dots,\alpha_8}\oplus \gens{\tilde
\alpha_1,\dots, \tilde \alpha_8} \over e'} \\ &\cong \gens{e,f} \oplus
\gens{\alpha_1,\dots,\alpha_8}\oplus \gens{\tilde \alpha_1,\dots, \tilde
\alpha_8} \\ &\cong U \oplus E_8^2.
\end{aligned}
$$

To determine the map on 1-cusps, it suffices to determine
$$\di_{U\oplus E_8^2}(\tilde w_2), \qquad \tilde w_2 = 2e + 2f + \alpha_1 + \alpha_2 + \tilde \alpha_1 + \tilde \alpha_2.$$

However, observing that $\tilde w_2\cdot \alpha_3 = 1$, we immediately obtain
that the divisibility is one.
Thus $\tilde w_2$ is odd, and we apply case (a) of [@AE22 Thm.
5.10].

:::

:::

::: {.remark}

By the cusp correspondence in [@AEGS23], this matches cusp $(9,9,1)_1$ in
$T_\Co$ with Sterk cusp 2 as the folding of $(18,0,0)_1$ by the horizontal
symmetry of its Coxeter diagram.
This means that the corresponding IAS and Kulikov models will be disc type, and
correspond to the folding involution of Sterk 2.

:::
