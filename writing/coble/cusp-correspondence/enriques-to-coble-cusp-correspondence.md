# Enriques to Coble correspondence {#sec-enriques-coble-correspondence}


::: {.theorem #thm:cusp_correspondence}

Let $\eta\colon T_\Co\injects\ten$ be the primitive embedding, $v_1, v_2$ the isotropic vectors of @lem:divisibilityTcoOne and $\tilde J = \generators{\eta(v_1), \eta(v_2)}$. Then $\tilde J$ is an isotropic plane, $\eta(v_1)$ is isotropic with $\div_\ten(\eta(v_1)) = 2$, and
$$\eta(v_1)^{\perp\ten}/\eta(v_1)\cong(10,8,0)_1, \qquad \tilde J^{\perp\ten}/\tilde J\cong(8,6,0)_0,$$
the boundary lattices of the $0$-cusp $(10,8,0)_1$ and the $1$-cusp $(8,6,0)_0$ of the Enriques cusp diagram; while
$$v_1^{\perp T_\Co}/v_1\cong(9,9,1)_1, \qquad J^{\perp T_\Co}/J\cong(7,7,1)_0$$
are the corresponding Coble boundary lattices.
:::

::: {.proof}

The vector $\eta(v_1)$ is isotropic with $\div_\ten(\eta(v_1)) = 2$ by @lem:divisibilityTcoOne, and its boundary lattice is $(10,8,0)_1$ by @lem:w1_perp_calculation. The plane $\tilde J$ is isotropic with boundary lattice $(8,6,0)_0$ by @lem:1_cusp_correspondence. The Coble boundary lattices are computed in the proofs of @lem:divisibilityTcoOne and @lem:1_cusp_correspondence.
:::
::: {#fig-enriques-coble-correspondence .figure}
\input{tikz/fig_Cusp_Correspondence_Co_En.tex}

Cusp correspondence between the boundary lattices of $F^{\mathrm{un}}_\Co$ and the cusps $(10,10,0)_1$, $(10,8,0)_1$, $(8,8,0)_0$, $(8,6,0)_0$ of the Enriques diagram of $F^K_\En$.
:::

::: {.lemma #lem:divisibilityAlwaysTwoTco}

Every $v\in T_\Co$ has $\div_{T_\Co}(v)$ even; and $\div_{T_\Co}(v) = 2$ exactly when $\div_L(v) = 1$ for $L=\generators{1}\oplus E_{10}$, that is when $v$ is primitive in $L$, equivalently when its coordinates in a $\ZZ$-basis of $L$ have no common divisor.
:::

::: {.proof}

Write $T_\Co=L(2)$ for $L\definedas\generators{1}\oplus E_{10}$, which is unimodular: this is the identity
$$
T_\Co=\generators{2}\oplus E_{10}(2)=\qty{\generators{1}\oplus E_{10}}(2)
$$
of @prop:coble-transcendental, and twisting by a unit does not change the underlying module.
So $T_\Co$ and $L$ have the same underlying $\bZ$-module and $\beta_{T_\Co}=2\,\beta_L$.

For $v,x\in T_\Co$ then $\beta_{T_\Co}(v,x)=2\beta_L(v,x)$, so every value is even, whether or not $v$ pairs nontrivially with something: $\div_{T_\Co}(v)$ is even for every $v$.

For the second, $\div_{T_\Co}(v)=2\div_L(v)$, so $\div_{T_\Co}(v)=2$ exactly when $\div_L(v)=1$, that is when no integer $m>1$ divides every value $\beta_L(v,x)$.
Because $L$ is unimodular, $\beta_L^{\sharp}\colon L\to L^{*}$ is an isomorphism, and $\beta_L(v,-)$ is divisible by $m$ exactly when $v\in mL$; so $\div_L(v)=1$ is the indivisibility of the functional $\beta_L(v,-)$, equivalently the primitivity of $v$ in $L$, and in coordinates it is the statement that the gcd of the coordinates of $v$ is one.
Evaluated in a $\ZZ$-basis with Gram matrix $G$, the divisibility is the gcd of the entries of $Gv$, which is the gcd of the coordinates of $v$ exactly when $G$ is unimodular; the two gcds are then related by the adjugate, whose entries are integral.
The gcd of the coordinates is itself basis-independent, since one $\ZZ$-basis of $L$ changes to another by a unimodular matrix.
For a form that is not unimodular the identification fails, and the rank-one lattice $\generators{2}$ shows both directions failing: its generator is primitive and has divisibility $2$, while $3$ is not primitive and has divisibility $6$.
:::

::: {.lemma #lem:divisibilityTcoOne}

Fixing notation,

$$
\begin{aligned}
v_1 &\definedas e' & w_1 &\definedas \eta(v_1) = \tilde e' \\
v_2 &\definedas 2h + \alpha_1 + \alpha_2 & w_2 &\definedas \eta(v_2) = 2\tilde e + 2\tilde f + \tilde\alpha_1 + \tilde\alpha_2 \\
J &\definedas \generators{v_1, v_2} & \tilde J &\definedas \generators{w_1, w_2}
\end{aligned}
$$

We then have $\div_{\ten}(w_1) = 2$.
:::

::: {.proof}

By @lem:divisibilityAlwaysTwoTco, $v_1$ has divisibility $2$ in $T_\Co$; moreover it is isotropic.
By @thm:unpolarized-cusps and @prop:tco-split-maximal, $\Orth^+(T_\Co)$ is transitive on primitive isotropic vectors, with quotient $\latI_{1,8}(2)$ at any of them, so $v_1$ represents *the* $0$-cusp of $F^{\mathrm{un}}_\Co$ and $$(v_1)^{\perp T_\Co}/v_1 \cong \latI_{1,8}(2) = (9,9,1) \cong \generators{2} \oplus E_8(2).$$ The stable group $\widetilde\Orth^+(T_\Co)$ has $527$ orbits of primitive isotropic vectors (@thm:coble-zero-cusp-count(2), one orbit per nonzero isotropic class by @thm:coble-integral-lifting-fibre(1), (2)); they lie in one $\Orth^+(T_\Co)$-orbit, so all $527$ $0$-cusps of the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ have boundary lattice $\latI_{1,8}(2)$.

Since $\tilde e' \tilde f' = 2$, and $\tilde e'$ is orthogonal to the remaining generators of $\ten$, we have

$$
\div_{\ten}(w_1) \definedas \div_{\ten}(\eta(e'))
= \div_{\ten}(\tilde e') = 2.
$$

Explicitly, write $\ten = U \oplus U(2) \oplus E_8(2)$ and $x+y+z\in U \oplus U(2)\oplus E_8(2)$. Then

$$
\tilde e'\cdot(x+y+z) = \tilde e'\cdot y\in 2\bZ
$$

since $y\in U(2)$ and $\tilde e'\in (U\oplus E_8(2))^{\perp \ten}$.
Thus $\beta_{\ten}(\tilde e', \ten) = \beta_{\ten}(\tilde e', U(2)) = 2\bZ$ since $\tilde e'\cdot\tilde f' = 2$.
:::

::: {.lemma #lem:w1_perp_calculation}

The 0-cusp $(9,9,1)_1$ in $F^{\mathrm{un}}_\Co$ maps to the 0-cusp $(10, 8, 0)_1$ in $F^K_\En$.
:::

::: {.proof}

The cusp correspondence follows from computing the lattice $w_1^{\perp \ten}/w_1$ under the primitive embedding $\eta$, since $\eta(v_1) = w_1$ and $v_1$ is the isotropic vector corresponding to $(9,9,1)_1$ in $F^{\mathrm{un}}_\Co$:

$$
{(\tilde e')^{\perp \ten} \over \generators{\tilde e'}} =
{
\generators{\tilde{e}, \tilde{f}}
\oplus
\generators{\tilde{e}'}
\oplus
\generators{\tilde{\alpha}_1, \dots, \tilde{\alpha}_8}
\over
\generators{ \tilde{e}' }}\cong\generators{\tilde{e}, \tilde{f}} \oplus\generators{
\tilde{\alpha}_{1}, \dots, \tilde{\alpha}_{8}
} \cong U \oplus E_{8}(2) \cong (10,8,0)_1.
$$

Alternatively, by [@AE22 Prop. 5.5], the isomorphism type of $w_1^{\perp \ten}/w_1$ is determined by $\mathrm{div}_{\ten}(w_1)$, which the divisibility calculation (@lem:divisibilityTcoOne) gives as $2$; divisibility is also what distinguishes the two Enriques $0$-cusps, $(10,10,0)_1$ at divisibility $1$ and $(10,8,0)_1$ at divisibility $2$ [@AEGS25, §2].
So $\eta(v_1)$ sits at the $(10,8,0)_1$ cusp.
:::

::: {.lemma #lem:1_cusp_correspondence}

The isotropic plane $\tilde J = \generators{\eta(v_1), \eta(v_2)}$ lies at the Enriques $1$-cusp $(8,6,0)_0$, while $J = \generators{v_1, v_2}$ lies at the Coble $1$-cusp $(7,7,1)_0$.
:::

::: {.proof}

Write $T_\Co = B(2)$ with $B = \latI_{2,9}$ (@prop:tco-as-twist), and let $J$ be a primitive isotropic plane of $T_\Co$, for instance $J = \generators{v_1, v_2}$ with $v_1 = e'$ and $v_2 = 2h+\alpha_1+\alpha_2$ in the basis $\generators{2}\oplus U(2)\oplus E_8(2)$. For a primitive isotropic line $l\subset J$, the proof of @thm:plane-transitivity-tco gives $l^{\perp B}/l\cong\latI_{1,8}$, and $J/l$ is a primitive isotropic line of it; by the proof of @prop:rank-nine-line-transitivity, its quotient is $\latI_{0,7}$. So $J^{\perp T_\Co}/J\cong\latI_{0,7}(2)\cong A_1^{\oplus 7}$, of type $(7,7,1)$, and every $1$-cusp of $\fco$ has boundary lattice $(7,7,1)_0$.
It remains to identify the isomorphism type of the image $\tilde J^{\perp \ten}/\tilde J$ in $\ten$.
Both $v_2$ and $w_2$ are isotropic: $v_2^2 = 4h^2+\alpha_1^2+\alpha_2^2 = 8-4-4 = 0$ and $w_2^2 = 8\,\tilde e\cdot\tilde f+\tilde\alpha_1^2+\tilde\alpha_2^2 = 8-4-4 = 0$, since $\alpha_1\perp\alpha_2$ and the roots of $E_8(2)$ have square $-4$. Also $v_2 \in v_1^{\perp T_\Co}/v_1$. So $J$ and $\tilde J$ are isotropic planes in $T_\Co$ and $\ten$ respectively.
By [@AE22 Prop. 5.5, Lem. 5.9], it suffices to show

$$
\div_{w_1^{\perp \ten} /w_1}(w_2) \definedas \div_{U \oplus E_8(2)}(2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2)= 2
,
$$

since the isomorphism type of $\tilde J^\perp/\tilde J$ is uniquely determined by the isomorphism type of $w_2^{\perp \ten}/w_2$ in $w_1^{\perp \ten}/w_1$, which is in turn uniquely determined by the characterization of $w_2$ as odd, even ordinary, or even characteristic in $w_1^{\perp \ten}/w_1$, which by the $w_1^\perp$ calculation (@lem:w1_perp_calculation) is isomorphic to $U \oplus E_8(2)$.
For $x+y\in U \oplus E_8(2)$, the orthogonality of the summands gives

$$
(x+y)\cdot w_2
= (x+y)\cdot (2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2 )
= 2x\cdot (\tilde e + \tilde f) + y\cdot (\tilde \alpha_1 + \tilde \alpha_2)
,
$$

The first term is even. The second term is even because every pairing in $E_8(2)$ is even. Since $\tilde e\cdot w_2 = 2\,\tilde e\cdot\tilde f = 2$, the divisibility is exactly $2$.
:::

::: {.proposition #prop:enriques-bb-boundary-curves title="The one-dimensional boundary components of the Enriques and Coble moduli spaces"}

Let $\mcm_{\mathrm{Enr}}\subset\Gamma_{\mathrm{Enr}}\backslash\bD(\ten)$ be the moduli space of Enriques surfaces in the period quotient of [@CDL25, Thm. 5.9.8], with period lattice $\ten = U\oplus U(2)\oplus E_8(2)$, and let $\overline{\mcm}_{\mathrm{Enr}}$ be its Baily--Borel compactification. The complement $\mcm_{\mathrm{Cob}}\definedas\Gamma_{\mathrm{Enr}}\backslash\bD(\ten)\setminus\mcm_{\mathrm{Enr}}$ is an irreducible divisor, isomorphic to the moduli space of Coble surfaces of K3 type [@CDL25, Thm. 5.9.8(1)]. Let $X\definedas\overline{\SL_2(\bZ)\backslash\bH}$.

1. The boundary $\overline{\mcm}_{\mathrm{Enr}}\setminus(\mcm_{\mathrm{Enr}}\cup\mcm_{\mathrm{Cob}})$ is the union of two curves that meet in one point. They are the boundary components of the two $\Gamma_{\mathrm{Enr}}$-orbits of primitive isotropic planes of $\ten$. The curve of an isotropic plane $P_1$ with $P_1^{\perp}/P_1\cong E_8(2)$ is the modular curve $X_0(2)$, and the other curve is $X$ [@CDL25, Thm. 5.9.8 and its proof].
2. The boundary of the closure of $\mcm_{\mathrm{Cob}}$ in $\overline{\mcm}_{\mathrm{Enr}}$ has exactly one $0$-dimensional component and exactly one $1$-dimensional component, and the $1$-dimensional component is isomorphic to $X$ [@CDL25, Cor. 5.9.10].
3. The boundary curve of the isotropic plane $\tilde J$ of @lem:1_cusp_correspondence is $X$.
:::

::: {.proof}

Items 1 and 2 are the cited results. For item 3, $\tilde J^{\perp}/\tilde J\cong(8,6,0)_0$ by @lem:1_cusp_correspondence. Its discriminant group has order $2^6$, and the discriminant group of $E_8(2)$ has order $2^8$. So $\tilde J$ is not in the orbit of $P_1$, and by item 1 its boundary curve is $X$.
:::

::: {.lemma #lem:cusp_map_dP}

Let $\tilde w_i$ be the images of $v_i$ in $\tdp$ under the embedding of @lem:sequence_of_embeddings. Then

$$
\begin{aligned}
\tilde w_1^{\perp \tdp}/\tilde w_1 &\cong (18, 0, 0)_1 \cong U \oplus E_8^2 \\
\tilde w_2^{\perp \tdp}/\tilde w_2 &\cong (16, 0, 0)_0
\end{aligned}
$$

The first identification is forced: $(18,0,0)_1$ is the unique even unimodular lattice of its (indefinite) signature.
The second lattice is even, unimodular, and negative-definite of rank $16$, and is thus determined only up to the two such isometry classes.

Thus the embedding $\fco \injects \fttz$ induces the following maps on cusps:

$$
\begin{aligned}
    (9, 9, 1)_1 &\mapsto (18, 0, 0)_1 \\
    (7, 7, 1)_0 &\mapsto (16, 0, 0)_0
\end{aligned}
$$
:::

::: {.proof}

The map on 0-cusps follows from identifying $\tilde w_1 = e' \in \tdp = \generators{e,f} \oplus \generators{e', f'}\oplus \generators{\alpha_1,\cdots,\alpha_8}\oplus \generators{\tilde \alpha_1,\cdots, \tilde \alpha_8}$ and noting

$$
\begin{aligned}
{ (e')^{\perp \tdp} \over e'} &\cong {\generators{e,f}
\oplus \generators{e'}\oplus \generators{\alpha_1,\dots,\alpha_8}\oplus \generators{\tilde
\alpha_1,\dots, \tilde \alpha_8} \over e'} \\ &\cong \generators{e,f} \oplus
\generators{\alpha_1,\dots,\alpha_8}\oplus \generators{\tilde \alpha_1,\dots, \tilde
\alpha_8} \\ &\cong U \oplus E_8^2.
\end{aligned}
$$

To determine the map on 1-cusps, it suffices to determine $$\div_{U\oplus E_8^2}(\tilde w_2), \qquad \tilde w_2 = 2e + 2f + \alpha_1 + \alpha_2 + \tilde \alpha_1 + \tilde \alpha_2.$$

However, observing that $\tilde w_2\cdot \alpha_3 = 1$, we immediately obtain that the divisibility is one.
Thus $\tilde w_2$ is odd, and we apply case (a) of [@AE22 Thm. 5.10].
:::

::: {.proposition #prop:rank_16_cusp_D16}

The negative-definite lattice $\tilde w_2^{\perp \tdp}/\tilde w_2 \cong (16,0,0)_0$ of @lem:cusp_map_dP is isometric to $D_{16}^+$; among the two even negative-definite unimodular lattices of rank $16$, this specifies the $D_{16}^+$ class.
:::

::: {.proof}

The invariants $(r,a,\delta) = (16,0,0)$ do not by themselves determine the isometry class, since the even negative-definite unimodular lattices of rank $16$ are exactly $E_8^{\oplus 2}$ and $D_{16}^+$.
The root system of $E_8^{\oplus 2}$ has two orthogonal components, each of rank $8$; the root system of $D_{16}^+$ is the irreducible system $D_{16}$.
So it suffices to exhibit a chain of roots of $\tilde J^\perp/\tilde J$, where $\tilde J = \generators{\tilde w_1, \tilde w_2}$, in which consecutive roots are not orthogonal and which spans a sublattice of rank greater than $8$.

Label the simple roots of each $E_8$ summand as in Bourbaki, so that $\alpha_1 \perp \alpha_2$, as $\tilde w_2^2 = 0$ requires, and $\alpha_3$ meets $\alpha_1$, as in the proof above.
Put $s = \alpha_3 + \alpha_4$ and $\tilde s = \tilde\alpha_3 + \tilde\alpha_4$.
The twelve vectors

$$
\tilde\alpha_8,\ \tilde\alpha_7,\ \tilde\alpha_6,\ \tilde\alpha_5,\ \tilde s - f,\ \tilde\alpha_1 + f,\ \tilde\alpha_1 + e,\ s - f,\ \alpha_5,\ \alpha_6,\ \alpha_7,\ \alpha_8
$$

have square $-2$ and are orthogonal to $\tilde w_1 = e'$ and to $\tilde w_2 = 2e + 2f + \alpha_1 + \alpha_2 + \tilde\alpha_1 + \tilde\alpha_2$.
Consecutive vectors in the list pair to $\pm 1$.
Since $\tilde J$ is isotropic, it lies in the radical of the form on $\tilde J^\perp$, so the images in $\tilde J^\perp/\tilde J$ are roots with the same pairings.
The twelve vectors together with $\tilde J$ span a sublattice of rank $14$, so the images span a sublattice of rank $12$.
The images therefore lie in one irreducible component of rank at least $12$, and $\tilde J^\perp/\tilde J \not\cong E_8^{\oplus 2}$.
:::

## The orbit map on $0$-cusps {#sec-cusp-orbit-map}

Throughout, $\Gamma_\En\definedas\widetilde\Orth^+(\ten)=\Orth^+(\ten)\intersect\discriminantkernel{\ten}$ is the stable group of @def:gamma-co-groups, $\discriminantkernel{L}$ being the kernel of the map (2.1) of [@DK13, printed p. 511], and $\Gamma^K_\En\definedas\Orth(\ten)$ is the group that [@AEGS25, Def. 2.6, printed p. 587] writes $\Gamma_\En$.

Let $K\definedas T_\Co^{\perp\ten}=\ZZ k$, with $k = \tilde e-\tilde f$ and $k^2 = -2$. Then $\eta(T_\Co) = k^{\perp\ten}$ and $\ten/(\eta(T_\Co)\oplus K)\cong\ZZ/2$, so that the gluing subgroup of $\eta(T_\Co)\oplus K\subset\ten$ is the order-two isotropic subgroup $H = \generators{(h/2,\,k/2)}\leq A_{T_\Co}\oplus A_K$. The embedding $\eta$ carries representatives of the $0$-cusps of $T_\Co$ to representatives of $0$-cusps of $\ten$, on which $\Gamma_\En$ acts, and the induced map of orbit sets is
$$\Phi\colon\widetilde\Orth^+(T_\Co)\backslash\{\text{primitive isotropic vectors of }T_\Co\}\ \longrightarrow\ \Gamma_\En\backslash\{\text{primitive isotropic vectors of }\ten\}.$$

::: {.theorem #thm:coble-strong-lifting title="The strong lifting over the Coble sublattice"}

1. For every $\varphi\in\widetilde\Orth^+(T_\Co)$ there is exactly one $\mathrm{Ext}(\varphi)\in\Orth(\ten)$ with $\mathrm{Ext}(\varphi)\circ\eta = \eta\circ\varphi$ and $\mathrm{Ext}(\varphi)(k) = k$, and it lies in $\Gamma_\En$. The assignment is a group homomorphism $\mathrm{Ext}\colon\widetilde\Orth^+(T_\Co)\to\Gamma_\En$ with $\mathrm{res}\circ\mathrm{Ext} = \id$, where $\mathrm{res}(\gamma)\definedas\eta^{-1}\gamma\eta$ for $\gamma\in\Orth(\ten)$ preserving $\eta(T_\Co)$; hence $\mathrm{Ext}$ is injective and $\eta$ is $\mathrm{Ext}$-equivariant, $\eta(\varphi v) = \mathrm{Ext}(\varphi)\,\eta(v)$.
2. $\mathrm{Ext}\bigl(\widetilde\Orth^+(T_\Co)\bigr) = \theset{\gamma\in\Gamma_\En \st \gamma(k) = k} = \Stab_{\Gamma_\En}(k)$; the image of $\mathrm{res}\colon\Stab_{\Gamma_\En}(\eta(T_\Co))\to\Orth(T_\Co)$ is $\widetilde\Orth^+(T_\Co)$, and its kernel is $\{1,s_k\}$, $s_k$ the reflection in $k$. Hence
$$\Stab_{\Gamma_\En}(\ZZ k) = \mathrm{Ext}\bigl(\widetilde\Orth^+(T_\Co)\bigr)\times\generators{s_k}\cong\widetilde\Orth^+(T_\Co)\times\ZZ/2.$$
3. The map $\Phi$ is well defined.
:::

::: {.proof}

*The two lattices and the gluing.* By [@AEGS25, Def. 2.3, printed p. 586], $\ten=U\oplus U(2)\oplus E_8(2)$ is the even $2$-elementary lattice $(12,10,0)_2$ of signature $(2,10)$; by [@DK13, (3.6), printed p. 513], the Coble lattice is $T_\Co = \generators{2}\oplus\mathbb{E}(2) = \generators{h}\oplus U(2)\oplus E_8(2)$, where $\mathbb{E} = E_8\oplus U$ is the Enriques lattice of [@DK13, printed p. 510] --- of rank $10$, unimodular, so $A_{\mathbb E} = 0$, and doubled to give the $U(2)\oplus E_8(2)$ summand. The lattice $T_\Co$ is the even $2$-elementary lattice of signature $(2,9)$ of the same display [@DK13, (3.6), printed p. 513]. In the notation of @lem:primitive_embedding_eta, $\eta$ sends $h$ to $\tilde e+\tilde f$ and is the identity on $U(2)\oplus E_8(2)$, the vectors $\tilde e,\tilde f$ being the isotropic basis of $U$ with $\tilde e\cdot\tilde f = 1$. Then
$$k^2 = (\tilde e-\tilde f)^2 = -2,\qquad k\cdot\eta(T_\Co) = 0,\qquad \ten/(\eta(T_\Co)\oplus\ZZ k)\cong U/(\ZZ(\tilde e+\tilde f)\oplus\ZZ(\tilde e-\tilde f))\cong\ZZ/2,$$
so $\eta(T_\Co)\subseteq k^{\perp\ten}$ with both of rank $11$ gives $\eta(T_\Co) = k^{\perp\ten}$, the vector $k$ is primitive, and $\eta(T_\Co)\oplus\ZZ k$ has index two in $\ten$.
The gluing subgroup of [@Nik80, Prop. 1.5.1, printed p. 111] is generated by the class of $\tfrac12(\eta(h)+k) = \tilde e$, that is by $(h/2,k/2)$: the class $h/2$ lies in the dual of $T_\Co$ because $h^2 = 2$ and $h\perp E_{10}(2)$, the class $k/2$ generates $A_K\cong\ZZ/2$ because $k^2 = -2$, and $q_{T_\Co}(h/2)+q_K(k/2) = \frac12-\frac12\equiv0\pmod{2\ZZ}$ is the isotropy of $H$ that an overlattice of index two requires. Under the two projections $p_{T_\Co}\colon H\to A_{T_\Co}$ and $p_K\colon H\to A_K$ the gluing isomorphism is $\gamma = p_Kp_{T_\Co}^{-1}\colon h/2\mapsto k/2$, and $q_K\circ\gamma = -q_{T_\Co}$ on $H$.

*Existence of the lift.* Apply [@Nik80, Cor. 1.5.2, printed p. 111] with $S_1 = S_2 = \eta(T_\Co)\subset\ten$, with the given $\varphi\in\Orth(T_\Co)$ and with $\psi = \id_K$: an extension of $\varphi$ to an automorphism of $\ten$ acting as $\psi$ on $K$ exists if and only if $\bar\psi\circ\gamma = \gamma\circ\bar\varphi$ on $H$, the bars denoting the discriminant actions. Since $A_K\cong\ZZ/2$ carries the nonzero value $q_K(k/2) = -\frac12$, its only isometry is the identity, so $\bar\psi = \id$ and the condition reads $\bar\varphi(h/2) = h/2$. For $\varphi\in\widetilde\Orth^+(T_\Co)$ the discriminant action is trivial on all of $A_{T_\Co}$, by the definition of $\widetilde\Orth$ as the kernel of (2.1) [@DK13, printed p. 511], so the condition holds and the lift $\mathrm{Ext}(\varphi)$ exists.

*Uniqueness and the homomorphism property.* Two automorphisms of $\ten$ that agree on $\eta(T_\Co)$ and fix $k$ agree on $\eta(T_\Co)\oplus\ZZ k$, a full-rank sublattice, hence everywhere. So $\mathrm{Ext}(\varphi)$ is unique, $\mathrm{Ext}(\varphi)\mathrm{Ext}(\varphi')$ and $\mathrm{Ext}(\varphi\varphi')$ agree on $\eta(T_\Co)$ and fix $k$, so $\mathrm{Ext}$ is a homomorphism, and $\mathrm{res}\circ\mathrm{Ext} = \id$ holds by construction; in particular $\mathrm{Ext}$ is injective, and $\eta(\varphi v) = \mathrm{Ext}(\varphi)\eta(v)$ is the identity $\mathrm{Ext}(\varphi)\circ\eta = \eta\circ\varphi$.

*The lift lies in the stable group.* For $y\in\ten^\vee$ write $y = y_S+y_K$ with $y_S\in\eta(T_\Co)^\vee$ and $y_K\in K^\vee$, the dual splitting being that of the orthogonal splitting $\ten\otimes\QQ = \eta(T_\Co)\otimes\QQ\perp K\otimes\QQ$. Then $\mathrm{Ext}(\varphi)(y)-y = \varphi(y_S)-y_S$, which lies in $\eta(T_\Co)$ because $\bar\varphi = \id$; so $\mathrm{Ext}(\varphi)$ acts trivially on $A_\ten$ and lies in $\discriminantkernel{\ten}$. For the sign, the two $\Orth^+$ are the kernels of the real spinor norm of @def:spinor-norm and @def:lattice-spinor-kernels; over $\RR$ the lift is $\varphi_\RR\perp\id_{K_\RR}$, so a Cartan--Dieudonné decomposition $\varphi_\RR = s_{u_1}\cdots s_{u_m}$ with $u_i\in\eta(T_\Co)\otimes\RR$ [@Mei13, Theorem 1.1] is one for $\mathrm{Ext}(\varphi)_\RR$ --- the reflection in $u_i$ does not see $K_\RR$, which is orthogonal to $u_i$ --- whence
$$\spinornorm_\RR\bigl(\mathrm{Ext}(\varphi)\bigr) = \prod_{i=1}^m\Bigl[-\frac{u_i^2}{2}\Bigr] = \spinornorm_\RR(\varphi),$$
and $\varphi\in\Orth^+$ exactly when $\mathrm{Ext}(\varphi)\in\Orth^+$. Both conditions being inherited, $\mathrm{Ext}$ lands in $\Gamma_\En$.

*The stabilizer comparison.* Let $\gamma\in\Gamma_\En$ fix $k$. It then preserves $k^{\perp\ten} = \eta(T_\Co)$, so $\varphi = \mathrm{res}(\gamma)\in\Orth(T_\Co)$ is defined, and $\gamma = \mathrm{Ext}(\varphi)$ will follow from $\varphi\in\widetilde\Orth^+(T_\Co)$ and uniqueness both ways.
For the sign, $\gamma = \mathrm{Ext}(\varphi)$ is one extension of $\varphi$, so the identity of the previous paragraph gives $\spinornorm_\RR(\varphi) = \spinornorm_\RR(\gamma) = 1$.
For the discriminant action, let $x\in A_{E_{10}(2)}\subseteq A_{T_\Co}$ and take its representative $\tilde x\in E_{10}(2)^\vee\subseteq T_\Co^\vee$, orthogonal to $h$; the functional $y$ on $\eta(T_\Co)\oplus\ZZ k$ with $y(\eta s) = \beta_{T_\Co}(\tilde x,s)$ and $y(k) = 0$ vanishes on $\eta(h)+k = 2\tilde e$, so it is integral on $\ten$. Since $\gamma\in\discriminantkernel{\ten}$, $\gamma y - y\in\ten$, and restricting to $\eta(T_\Co)$ gives $\bar\varphi^{\,-1}(x) = x$: the class of $(\gamma y)|_{\eta(T_\Co)} = y\circ\gamma^{-1}|_{\eta(T_\Co)}$ is $\bar\varphi^{\,-1}(x)$, the class of $y|_{\eta(T_\Co)}$ is $x$, and their difference lies in $\eta(T_\Co)$. So $\bar\varphi$ fixes every class of $A_{E_{10}(2)}$. It also fixes the class $h/2$: the vector $\tilde e = \tfrac12(\eta(h)+k)$ lies in $\ten^\vee$ because $\tilde e\cdot\ten\subseteq\ZZ$, so $\gamma\tilde e-\tilde e\in\ten$, and
$$\gamma\tilde e-\tilde e = \tfrac12\bigl(\eta\varphi(h)-\eta(h)\bigr),\qquad \beta_\ten\bigl(\gamma\tilde e-\tilde e,\,k\bigr) = \beta_\ten(\tilde e,k)-\beta_\ten(\tilde e,k) = 0,$$
using $\gamma k = k$; a vector of $\ten$ orthogonal to $k$ lies in $\ten\intersect k^{\perp\ten} = \eta(T_\Co)$, both sides having rank $11$ and $k$ being primitive, so $\varphi(h)-h = 2(\gamma\tilde e-\tilde e)\in2T_\Co$, that is $\bar\varphi(h/2) = h/2$. As $A_{T_\Co} = A_{\generators{h}}\oplus A_{E_{10}(2)}$ is the discriminant group of the orthogonal splitting $T_\Co = \generators{h}\perp E_{10}(2)$, $\bar\varphi = \id$, so $\varphi\in\widetilde\Orth^+$, and $\gamma = \mathrm{Ext}(\varphi)$ by uniqueness. So $\mathrm{Ext}\bigl(\widetilde\Orth^+(T_\Co)\bigr) = \Stab_{\Gamma_\En}(k)$, and $\mathrm{res}$ carries $\Stab_{\Gamma_\En}(\eta(T_\Co))$ onto $\widetilde\Orth^+(T_\Co)$.

*The kernel of $\mathrm{res}$ and the line stabilizer.* Let $\gamma\in\Gamma_\En$ act trivially on $\eta(T_\Co)$. Then $\gamma(k) = \pm k$, since $K = \eta(T_\Co)^{\perp\ten}$ is preserved. If $\gamma(k) = k$ then $\gamma = \id$ by the uniqueness step; if $\gamma(k) = -k$ then $s_k\gamma$ fixes $k$ and acts trivially on $\eta(T_\Co)$, hence $s_k\gamma = \id$ and $\gamma = s_k$. Conversely $s_k\in\Gamma_\En$: it is the isometry $y\mapsto y+\beta_\ten(y,k)k$, integral because $k^2 = -2$, it acts trivially on $A_\ten$ because $\beta_\ten(y,k)k\in\ten$ for $y\in\ten^\vee$, and $\spinornorm_\RR(s_k) = [-k^2/2] = [1]$. So $\ker\mathrm{res} = \{1,s_k\}$. An element of $\Gamma_\En$ preserving the line $\ZZ k$ satisfies $\gamma(k) = \pm k$; in the first case $\gamma = \mathrm{Ext}(\mathrm{res}\,\gamma)$ and in the second $s_k\gamma = \mathrm{Ext}(\mathrm{res}\,\gamma)$, so $\Stab_{\Gamma_\En}(\ZZ k) = \mathrm{Ext}\bigl(\widetilde\Orth^+(T_\Co)\bigr)\generators{s_k}$ with trivial intersection, and $\generators{s_k}$ is centralized by the image because $s_{\gamma k} = \gamma s_k\gamma^{-1}$ and $\mathrm{Ext}(\varphi)k = k$. The product is thus direct.

*$\Phi$ is well defined.* If $v' = \varphi v$ with $\varphi\in\widetilde\Orth^+(T_\Co)$, then $\eta(v') = \mathrm{Ext}(\varphi)\eta(v)$ with $\mathrm{Ext}(\varphi)\in\Gamma_\En$, so $\eta(v)$ and $\eta(v')$ lie in one $\Gamma_\En$-orbit.
:::

::: {.lemma #lem:monodromy-is-spinor-positive title="The monodromy of a family of Coble surfaces lies in $\Orth^+(T_\Co)$"}

Let $\mathcal S\to B$ be a family of Coble surfaces over a connected base, with the local system of lattices $T_\Co$, monodromy group $\Gamma_\Co\le\Orth(T_\Co)$ (@def:gamma-co-groups(1)) and periods in one component $D^+\subset\bD(T_\Co)$. Then $\Gamma_\Co\subseteq\Orth^+(T_\Co)=\Theta_\bR(T_\Co)$.
:::

::: {.proof}

Transport is an isometry (@prop:local-system-of-lattices-monodromy), and it carries $D^+$ to $D^+$: the period map of the family is single-valued on the connected base, so $\rho(\gamma)$ permutes the components of $\bD(T_\Co)$ and fixes the one containing the periods (@eq-period-map-equivariance).

*The component stabilizer, modulo the kernel.* The lattice $T_\Co$ carries the weight-$2$ Hodge structure of its K3 double cover and its $(1,1)$-part vanishes --- $T_\Co$ is transcendental --- so the case $h^{1,1}=0$ of @thm:period-domain-component-stabilizer applies (on the input of @lem:weight-two-positive-subspace): the image of $\Stab_{G_\bR}(D^+)$ in $\Orth(T_\Co\otimes\bR)/\theset{\pm\id}$ is the image of the identity component $G_\bR^\circ=\SO(T_\Co\otimes\bR)\intersect\Theta_\bR(T_\Co\otimes\bR)$. The kernel is taken because $-\id$ acts trivially on $\bD(T_\Co)$, every point being a line, and $-\id\notin\SO$ at odd rank, $T_\Co$ having rank $11$; so the stabilizer itself is
$$\Stab_{G_\bR}(D^+) = G_\bR^\circ\cup(-\id)\,G_\bR^\circ,$$
which is a subgroup because $-\id$ normalizes $G_\bR^\circ$ and squares to the identity.

*Both pieces lie in the spinor kernel.* $G_\bR^\circ\subseteq\Theta_\bR$ by definition (@def:lattice-spinor-kernels), and
$$\spinornorm_\bR(-\id_{T_\Co}) = [(-1)^2] = [1]$$
by @lem:minus-identity-spinor-norm, the positive index of $T_\Co$ being $2$. So $\Stab_{G_\bR}(D^+)\subseteq\Theta_\bR(T_\Co\otimes\bR) = \Orth^+(T_\Co)$ (@conv:spinor-positive-subgroup), and $\rho(\gamma)$ lies there.

The conclusion is sharp and is not containment in $\SO$: a reflection $s_\delta$ in a vector of square $-2$ has $\det = -1$ and $\spinornorm_\bR(s_\delta) = [-\delta^2/2] = [1]$, so it lies in $\Orth^+$ and not in $\SO$, and @prop:monodromy-contains-root-reflections places such reflections in the geometric monodromy. What the lifting needs is the spinor condition, which is what this lemma gives.
:::

::: {.remark #rmk:coble-strong-lifting-group title="The group in the strong lifting"}

The statement is about $\widetilde\Orth^+(T_\Co) = \discriminantkernel{T_\Co}\intersect\Orth^+(T_\Co)$, and every step of the proof uses only that group: the condition $\bar\varphi(h/2) = h/2$ of the extension criterion holds because $\bar\varphi$ is the identity on $A_{T_\Co}$, and the sign is inherited by the spinor-norm identity. So the conclusion holds verbatim for every subgroup of $\widetilde\Orth^+(T_\Co)$. The lifting of the monodromy group $\Gamma_\Co$ of the Coble family (@def:gamma-co-groups(1)) is therefore exactly the inclusion $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$, and that inclusion is false (@thm:gamma-co-not-stable): the monodromy contains the reflection in a $(-4)$-class, carried by the nodal-pair degeneration, and such a reflection lies outside the discriminant kernel. So the $\Gamma_\Co$ form of the lifting fails, while the theorem above, stated for $\widetilde\Orth^+(T_\Co)$, stands unharmed. Neither the equivariance nor the stabilizer comparison is asserted here for $\Gamma_\Co$. The reverse inclusion $\widetilde\Orth^+(T_\Co)\subseteq\Gamma_\Co$ is open (@rmk:gamma-co-status).
:::

::: {.proposition #prop:gamma-co-strong-lifting title="The $\Gamma_\Co$ form of the strong lifting, under the inclusion it needs"}

Let $\Gamma_\Co\le\Orth(T_\Co)$ be the monodromy group of the family of unpolarized Coble surfaces, with $\fco=\bD(T_\Co)/\Gamma_\Co$ and periods in one component (@def:gamma-co-groups(1)).

1. Every $\varphi\in\Gamma_\Co$ has exactly one $\gamma\in\Gamma_\En$ with $\gamma\circ\eta=\eta\circ\varphi$ and $\gamma(k)=k$; the assignment $\mathrm{Ext}\colon\Gamma_\Co\to\Gamma_\En$ is a homomorphism, $\mathrm{res}$ is a left inverse of it, and $\eta$ is $\mathrm{Ext}$-equivariant.
2. $\Gamma_\Co\subseteq\widetilde\Orth^+(T_\Co)$.
3. Under (1), $\mathrm{Ext}(\Gamma_\Co) = \Stab_{\Gamma_\En}(k)$.

Then (1) and (2) are equivalent, and, given (1), (3) is equivalent to the equality $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ of the former @conj:gamma-co-stable, which @thm:gamma-co-not-stable refutes. Clause (2) is false (@thm:gamma-co-not-stable): the sign half holds unconditionally, $\Gamma_\Co\subseteq\Orth^+(T_\Co)$ (@lem:monodromy-is-spinor-positive), and the discriminant half, $\Gamma_\Co\subseteq\discriminantkernel{T_\Co}$, fails. The equivalence is what the proposition asserts, and with (2) false it says that the $\Gamma_\Co$ form of the lifting fails, which it does.
:::

::: {.proof}

Assume (2). Then $\Gamma_\Co$ is a subgroup of $\widetilde\Orth^+(T_\Co)$ and @rmk:coble-strong-lifting-group gives (1), the theorem applying verbatim to every subgroup.
Conversely, a lift $\gamma\in\Gamma_\En$ of $\varphi$ lies in $\discriminantkernel{\ten}$, and $\gamma\circ\eta = \eta\circ\varphi$ with $\gamma(k)=k$ makes it preserve $\eta(T_\Co)$; the two arguments of the stabilizer comparison in the proof of @thm:coble-strong-lifting --- on the classes of $A_{E_{10}(2)}$ and on the class $h/2$ --- conclude $\bar\rho_{T_\Co}(\varphi) = \id$ from exactly those three facts. So (1) places $\Gamma_\Co$ in $\discriminantkernel{T_\Co}$, and with the sign of @lem:monodromy-is-spinor-positive it gives (2).

For (3), assume (1). The image $\mathrm{Ext}(\Gamma_\Co)$ is a subgroup of $\Stab_{\Gamma_\En}(k) = \mathrm{Ext}(\widetilde\Orth^+(T_\Co))$ by (2) and @thm:coble-strong-lifting(2), and $\mathrm{Ext}$ is injective, so $\mathrm{Ext}(\Gamma_\Co) = \mathrm{Ext}(\widetilde\Orth^+(T_\Co))$ holds exactly when $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$. The reverse implication is that theorem again. (Without (1) the group $\mathrm{Ext}(\Gamma_\Co)$ is not defined, which is why (3) is stated under it.)
:::

::: {.corollary #cor:coble-lifting-under-conjecture title="The $\Gamma_\Co$ form of the strong lifting, under the book's own conjecture"}

Assume @conj:gamma-co-stable, that is $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$ --- an assumption that is false (@thm:gamma-co-not-stable), so the corollary is vacuous and nothing about $\Gamma_\Co$ follows from it. What it records is the implication: then the conclusion of @thm:coble-strong-lifting holds with $\Gamma_\Co$ in place of $\widetilde\Orth^+(T_\Co)$:

1. every $\varphi\in\Gamma_\Co$ has exactly one $\gamma\in\Gamma_\En$ with $\gamma\circ\eta = \eta\circ\varphi$ and $\gamma(k) = k$, and the assignment $\mathrm{Ext}$ is a homomorphism of which $\mathrm{res}$ is a left inverse;
2. $\mathrm{Ext}(\Gamma_\Co) = \Stab_{\Gamma_\En}(k)$, and $\eta$ is $\mathrm{Ext}$-equivariant.

:::

::: {.proof}

By the hypothesis $\Gamma_\Co = \widetilde\Orth^+(T_\Co)$, which is false (@thm:gamma-co-not-stable), so condition (2) of @prop:gamma-co-strong-lifting holds, and (1) there gives the first clause; clause (3) of the same proposition gives the second, since $\Gamma_\Co$ is now the whole of $\widetilde\Orth^+(T_\Co)$ and the image of $\mathrm{Ext}$ on that group is $\Stab_{\Gamma_\En}(k)$ by @thm:coble-strong-lifting(2). The equivariance is the identity $\mathrm{Ext}(\varphi)\circ\eta = \eta\circ\varphi$.
:::

::: {.lemma #lem:meridian-kernel title="The reflections and Eichler transvections lie in the discriminant kernel"}

Let $L$ be an integral lattice, $A_L = L^\vee/L$, and $\rho = \rho_L\colon\Orth(L)\too\Orth(A_L,q_L)$ the discriminant representation of @def:discriminant-rep. Let $\Gamma\leq\Orth(L)$ be generated by elements of the two forms

1. a reflection $s_\delta$ in a vector $\delta\in L$ with $\delta^2 = -2$, that is $s_\delta(x) = x - \frac{2(x,\delta)}{(\delta,\delta)}\delta$ (@def:spinor-norm);
2. an Eichler transvection $\tau_{u,v}(x) \definedas x + (x\cdot u)v - (x\cdot v)u$, for $u,v\in L$ isotropic with $u\cdot v = 0$.

Then $\Gamma\subseteq\ker\rho$.

Consequently, with @lem:monodromy-is-spinor-positive, if the monodromy group $\Gamma_\Co$ of the family of unpolarized Coble surfaces is generated by these two forms --- the reflections being the Picard--Lefschetz monodromies of the $(-2)$-walls, for which @prop:monodromy-contains-root-reflections supplies the containment $W(T_\Co)\subseteq\Gamma^{\mathrm{geom}}$, and the transvections the unipotent monodromies at the cusps, whose lattice form is verified in `computations/reports/coble_658-cusp-parabolic-probe-run.txt` --- then $\Gamma_\Co\subseteq\ker\rho_{T_\Co}\cap\Orth^+(T_\Co) = \widetilde\Orth^+(T_\Co)$, which is condition (2) of @prop:gamma-co-strong-lifting, and the $\Gamma_\Co$ form of @thm:coble-strong-lifting follows.
:::

::: {.proof}

For $x\in L^\vee$ and $\delta\in L$ one has $(x,\delta)\in\ZZ$ by the definition of $L^\vee$, so
$$s_\delta(x) - x = -\frac{2(x,\delta)}{(\delta,\delta)}\,\delta = (x,\delta)\,\delta \in L .$$
Likewise, for $x\in L^\vee$ and $u,v\in L$, both $(x,u)$ and $(x,v)$ are integers, so
$$\tau_{u,v}(x) - x = (x\cdot u)\,v - (x\cdot v)\,u \in L .$$
Each generator therefore acts trivially on $A_L = L^\vee/L$, and $\rho$ is a homomorphism, so $\rho$ is trivial on the subgroup they generate.
:::

::: {.lemma #lem:coble-discriminant-actions-conjugate title="The two discriminant actions of an isometry of the K3 lattice"}

Let $M = \generators{e_0,\dots,e_{10}}\cong\generators{2}\oplus\generators{-2}^{\oplus 10}$ be the Picard lattice generated by the classes of $E_0,\dots,E_{10}$ on the K3 double cover of a Coble surface, and $N\definedas M^{\perp\lkt}$ its orthogonal complement in $\lkt = \latII_{3,19}$, so that $N\cong T_\Co$ and $q_N\cong -q_M$ [@DK13, printed p. 513; @Nik80, Cor. 1.6.2, printed p. 112]; in particular $M$ is primitive in $\lkt$ and $A_M\cong(\ZZ/2)^{11}$. Since $\lkt$ is unimodular, the gluing subgroup of $M\oplus N$ is the graph of an isometry $\gamma\colon A_M\isoto A_N(-1)$ (@cor:lifting-unimodular). Let $g\in\Orth(\lkt)$ preserve $M$ and $N$, with $\psi\definedas\restrictionof{g}{M}$, $\varphi\definedas\restrictionof{g}{N}$ and $\bar\psi\definedas\rho_M(\psi)$, $\bar\varphi\definedas\rho_N(\varphi)$. Then
$$\bar\varphi = \gamma\,\bar\psi\,\gamma^{-1}.$$
A subgroup $G\subseteq\Orth(\lkt)$ preserving both summands therefore acts trivially on $A_N = A_{T_\Co}$ exactly when it acts trivially on $A_M$. In particular an isometry carrying $e_i$ to $e_j$ with $i\neq j$ moves the class of $\tfrac12 e_i$, and so acts nontrivially on $A_{T_\Co}$.
:::

::: {.proof}

The isometry $g$ preserves $M\oplus N$ and $\lkt$, hence preserves the gluing subgroup, which is the graph $\theset{(x,\gamma x)\st x\in A_M}$ in $A_M\oplus A_N$. For $x\in A_M$ the class $(x,\gamma x)$ is in it, so $(\bar\psi x,\bar\varphi\gamma x)$ is in it as well, and the graph meets the fibre over $\bar\psi x$ in one point: $\bar\varphi\gamma x = \gamma\bar\psi x$. That is $\bar\varphi\circ\gamma = \gamma\circ\bar\psi$, the displayed identity. For the last claim, $\bar\psi$ sends $[e_i/2]$ to $[e_j/2]\neq[e_i/2]$, because $e_j-e_i$ has a coordinate equal to $1$ and so does not lie in $2M$.
:::

::: {.corollary #cor:gamma-co-lifting-criterion title="What decides the lifting for the monodromy group"}

Let $X\to\PP^2$ be the double cover branched along the plane sextic, a K3 surface on which the classes $e_0,\dots,e_{10}$ of $M = \generators{2}\oplus\generators{-2}^{\oplus 10}$ are the classes of $E_0,\dots,E_{10}$, with $N_X = M_X^{\perp\lkt}\cong T_\Co$ and $q_{N_X} = -q_M$ [@DK13, printed p. 513]. The period lattice of the Coble moduli problem is that $N_X$ [@DK13, Prop. 3.2, printed p. 513], and $M$ and $N$ are the two summands of one $H^2$ of one family, so the monodromy of the family of Coble surfaces --- the image of $\pi_1$ of its base, which maps to that of the base of the family of K3 double covers --- acts on $M$ as well as on $T_\Co$. Then
$$\Gamma_\Co\subseteq\discriminantkernel{T_\Co}\quad\Longleftrightarrow\quad\text{the monodromy acts trivially on }A_M,$$
which by @rmk:coble-strong-lifting-group is one of the two conditions for the strong lifting to hold for $\Gamma_\Co$. $A_M$ is generated by the classes of $\tfrac12 e_0,\dots,\tfrac12 e_{10}$, so the condition holds exactly when every loop of the family fixes each of those eleven classes, and it fails as soon as a loop exchanges two of the ten exceptional classes $e_1,\dots,e_{10}$; such a loop refutes the $\Gamma_\Co$ form of the lifting (@lem:coble-discriminant-actions-conjugate). The other condition, the sign, needs no hypothesis: $\Gamma_\Co\subseteq\Orth^+(T_\Co)$ (@lem:monodromy-is-spinor-positive). So, on the presentation of the moduli problem that [@DK13, Prop. 3.2, printed p. 513] uses, the $\Gamma_\Co$ form of @thm:coble-strong-lifting holds exactly when the monodromy acts trivially on $A_M$: that is condition (2) of @prop:gamma-co-strong-lifting, which is there shown equivalent to the $\Gamma_\Co$ form of the theorem.
:::

::: {.remark #rmk:coble-lifting-criterion-not-lattice title="What the criterion is not decided by"}

The condition of @cor:gamma-co-lifting-criterion is not a question about the lattices. The discriminant representation $\rho_{T_\Co}$ is onto (@thm:two-elementary-surjectivity), so for every $\psi\in\Orth(M)$ there is $\varphi\in\Orth(T_\Co)$ with $\bar\varphi\gamma = \gamma\bar\psi$ on the gluing subgroup, and by @cor:lifting-unimodular the pair extends to an isometry of $L_{\mathrm{K3}}$; in particular every permutation of the ten exceptional classes is realised by an isometry of $L_{\mathrm{K3}}$. What is at issue is whether it is realised by an element of the monodromy group $\Gamma_\Co$. So the criterion is decided by the family, not by exhibiting an isometry of the lattices.

Nor is it decided by functoriality from the Enriques family, which is the second tempting shortcut. @def:gamma-co-groups(1) says that the family of unpolarized Enriques surfaces "induces this family and its local system", and @prop:gamma-co-images(1) identifies the image of $\Stab_{\Gamma_\En}(\delta)$ in $\Orth(T_\Co)$ with $\widetilde\Orth^+(T_\Co)$; together those read as if $\Gamma_\Co$ were the restriction of $\Gamma_\En$ and lay inside $\widetilde\Orth^+(T_\Co)$ in two lines. The inference is not available, because what the Enriques family induces is the pair of local systems $T_\Co = \delta^{\perp\ten}\subset\ten$ and not an inclusion of bases. The periods of Coble surfaces lie in the Heegner divisor $\mch_{-2}$, which is the image of the map of @thm:normalization, while the moduli space of Enriques surfaces is the complement $(\bD(\ten)\sm\mch_{-2})/\Orth(\ten)$ [@DK13, printed p. 512]. The Coble moduli is thus a stratum that the Enriques moduli excludes, there is no map $\pi_1$ of the one base into that of the other, and no containment of $\Gamma_\Co$ in the image of $\Stab_{\Gamma_\En}(\delta)$ follows. That image is what a monodromy would have to lie in if it were known to come from the Enriques side; it is not what $\Gamma_\Co$ is known to be.
:::

The same argument applies to the other gluing of the Coble lattice, $S_\Co\oplus T_\Co\subset\lkt$: $\lkt$ is unimodular and the index is $2^{11} = \abs{A_{S_\Co}} = \abs{A_{T_\Co}}$, so the gluing subgroup is the graph of an anti-isometry $A_{S_\Co}\isoto A_{T_\Co}(-1)$ (@cor:lifting-unimodular), and a subgroup of $\Orth(\lkt)$ preserving both summands acts trivially on $A_{T_\Co}$ exactly when it acts trivially on $A_{S_\Co}$. The monodromy of the one-node construction lands in the stabilizer of the quadruple $(S_\Co,S_{\mathrm{dP}},H,\alpha)$ (@cor:construction-monodromy), so it preserves both summands, and the criterion for that family can be read on either side.

::: {.proposition #prop:cusp-map-not-onto}

Every vector in the image of $\Phi$ has divisibility $2$ in $\ten$. Hence $\Phi$ is not surjective: the $\Gamma_\En$-orbit of $\tilde e$, which has divisibility $1$ and boundary lattice $\tilde e^{\perp\ten}/\tilde e\cong U(2)\oplus E_8(2) = (10,10,0)_1$, is not in the image.
:::

::: {.proof}

Divisibility is an isometry invariant, so it is constant on $\Gamma_\En$-orbits, and $\div_\ten(\tilde e) = 1$ because $\tilde e\cdot\tilde f = 1$. So it suffices to show that $\div_\ten(\eta(v))$ is even for every primitive isotropic $v\in T_\Co$.

Since $\ten = \eta(T_\Co) + \ZZ\tilde e$,
$$\div_\ten(\eta(v)) = \gcd\bigl(\div_{T_\Co}(v),\ \beta_\ten(\eta(v),\tilde e)\bigr), \qquad \beta_\ten(\eta(v),\tilde e) = \tfrac12\beta_{T_\Co}(v,h),$$
the second because $\tilde e = \tfrac12(h+k)$ with $\eta(v)\perp k$. Both entries of the gcd are even. $\div_{T_\Co}$ is even for every vector, since the Gram matrix of $T_\Co$ is even entrywise; and if $v = ah + y$ with $y$ in the $U(2)\oplus E_8(2)$ summand, then $v^2 = 2a^2 + y^2$ with $y^2\equiv0 \pmod 4$, that summand being twice an even lattice, so $v^2 = 0$ forces $a$ even. Hence $\div_\ten(\eta(v))$ is even, and since $\eta(v)$ is a primitive vector of a $2$-elementary lattice, it is $2$.
:::

*The fibres of $\Phi$.* The fibre of $\Phi$ over the class $[\tilde w]$ consists of the classes $[v]$ with $\gamma\eta(v) = \tilde w$ for some $\gamma\in\Gamma_\En$. Put
$$Y = \{\gamma\in\Gamma_\En : \gamma^{-1}\tilde w\in\eta(T_\Co)\}, \qquad v_\gamma \definedas \eta^{-1}\bigl(\gamma^{-1}\tilde w\bigr).$$
Then the fibre is the double-coset set
$$\Phi^{-1}\bigl([\tilde w]\bigr) = \Stab_{\Gamma_\En}(\tilde w)\,\backslash\, Y\, /\, \mathrm{Ext}(\widetilde\Orth^+(T_\Co)).$$
Both actions preserve $Y$. For $h\in\Stab_{\Gamma_\En}(\tilde w)$, $(h\gamma)^{-1}\tilde w = \gamma^{-1}h^{-1}\tilde w = \gamma^{-1}\tilde w$, so $v_{h\gamma} = v_\gamma$. For $\varphi\in\widetilde\Orth^+(T_\Co)$,
$$\bigl(\gamma\,\mathrm{Ext}(\varphi)\bigr)^{-1}\tilde w = \mathrm{Ext}(\varphi)^{-1}\gamma^{-1}\tilde w = \mathrm{Ext}\bigl(\varphi^{-1}\bigr)\eta(v_\gamma) = \eta\bigl(\varphi^{-1}v_\gamma\bigr),$$
so $v_{\gamma \mathrm{Ext}(\varphi)} = \varphi^{-1}v_\gamma$.
Conversely, if $[v_\gamma] = [v_{\gamma'}]$, say $v_{\gamma'} = \varphi v_\gamma$, then $\gamma'^{-1}\tilde w = \eta(\varphi v_\gamma) = \mathrm{Ext}(\varphi)\gamma^{-1}\tilde w$, that is $\gamma \mathrm{Ext}(\varphi)^{-1}\gamma'^{-1}\in\Stab_{\Gamma_\En}(\tilde w)$, which gives $\gamma' \in \Stab_{\Gamma_\En}(\tilde w)\,\gamma\,\mathrm{Ext}(\widetilde\Orth^+(T_\Co))$. So the double cosets are exactly the classes over $[\tilde w]$, and the fibre is empty exactly when $Y$ is.

::: {.proposition #prop:cusp-map-separates-mod-two}

Let $v, v'$ be primitive isotropic vectors of $T_\Co$. If $\eta(v)$ and $\eta(v')$ lie in the same $\Gamma_\En$-orbit, then $v\equiv v'\pmod{2T_\Co}$.
:::

::: {.proof}

Put $x = \eta(v)$ and $x' = \eta(v')$, which have divisibility $2$ in $\ten$ by @prop:cusp-map-not-onto, and let $\gamma\in\Gamma_\En$ with $\gamma x = x'$. The class
$$\bar x \definedas \tfrac12 x \bmod \ten \in A_\ten = \ten^\vee/\ten$$
is defined, and isotropic because $x^2 = 0$. Then $\gamma(x/2) = x'/2$, and $\gamma$ acts trivially on $A_\ten$ because $\Gamma_\En\subseteq\discriminantkernel{\ten}$, so $\bar x = \overline{x'}$, that is $\tfrac12(x - x')\in\ten$ and $x\equiv x'\pmod{2\ten}$. Since $\eta(T_\Co)$ is primitive in $\ten$, $2\ten\intersect\eta(T_\Co) = 2\eta(T_\Co)$, so $v\equiv v'\pmod{2T_\Co}$.
:::

::: {.proposition #prop:cusp-map-injective}

The orbit map $\Phi$ is injective: if $v, v'$ are primitive isotropic vectors of $T_\Co$ and $\eta(v)$, $\eta(v')$ lie in one $\Gamma_\En$-orbit, then $v$ and $v'$ lie in one $\widetilde\Orth^+(T_\Co)$-orbit.
:::

::: {.proof}

By @prop:cusp-map-separates-mod-two, $v\equiv v'\pmod{2T_\Co}$, so $\tfrac12 v - \tfrac12 v'\in T_\Co$ and the classes $v^* = \tfrac12 v + T_\Co$ and $v'^*$ of @prop:coble-primitive-isotropic-classes are equal. By @thm:coble-zero-cusp-count, parts 1 and 2, the map $\widetilde\Orth^+(T_\Co) v\mapsto v^*$ is injective. Hence $\widetilde\Orth^+(T_\Co) v = \widetilde\Orth^+(T_\Co) v'$.
:::

::: {.proposition #prop:cusp-map-surjective-on-classes title="The image of $\Phi$ is exactly the divisibility-$2$ classes"}

The image of $\Phi$ is the set of all $527$ nonzero isotropic classes of $A_{\ten}$, and $v\mapsto[\eta(v)/2]$ is a bijection from the $\widetilde\Orth^+(T_\Co)$-orbits of primitive isotropic vectors of $T_\Co$ onto them. In particular a divisibility-$2$ $0$-cusp of $\fen$ lies over a Coble $0$-cusp if and only if its class is a nonzero isotropic class of $A_{\ten}$ --- which every divisibility-$2$ class is.
:::

::: {.proof}

*The image lies in the set.* For primitive isotropic $v\in T_\Co$, $\eta(v)$ is primitive of divisibility $2$ (@lem:divisibilityAlwaysTwoTco, @prop:cusp-map-not-onto), so $[\eta(v)/2]$ is defined, and it is isotropic because $v^2 = 0$. A class is $\Gamma_\En$-invariant, because $\Gamma_\En\subseteq\discriminantkernel{\ten}$ acts trivially on $A_\ten$, so $v\mapsto[\eta(v)/2]$ is well defined on orbits.

*The image has $527$ elements.* $\Phi$ is injective (@prop:cusp-map-injective) and its source is the set of $527$ orbits of $\widetilde\Orth^+(T_\Co)$ (@thm:coble-zero-cusp-count(2)).

*The class separates them.* If $[\eta(v)/2] = [\eta(v')/2]$ then $\eta(v)-\eta(v')\in 2\ten$, so $v\equiv v'\pmod{2T_\Co}$ by primitivity of $\eta$ (@lem:primitive_embedding_eta), that is the classes $v^* = [v/2]$ and $v'^*$ of @prop:coble-primitive-isotropic-classes agree; by @thm:coble-zero-cusp-count(1) $v$ and $v'$ then lie in one $\widetilde\Orth^+(T_\Co)$-orbit. So distinct source orbits give distinct classes, and the image meets $527$ nonzero isotropic classes.

*There are exactly $527$.* $|A_{\ten}| = 2^{10}$ because $\det\ten = 2^{10}$ (@lem:primitive_embedding_eta's lattice) and the count of nonzero isotropic classes of $A_{\ten}$ is $527$, exactly as for $T_\Co$; both counts are computed from the Gram matrices in `computations/reports/coble_658-image-census-probe-run.txt`, the $T_\Co$ count reproducing the $527$ of @thm:coble-zero-cusp-count(2).

A set of $527$ distinct classes inside a set of $527$ is the whole set.
:::

So $\Phi$ embeds the $527$ $0$-cusps of the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ (@thm:coble-zero-cusp-count(2), one $0$-cusp per nonzero isotropic class, the fibre over one class being a single orbit, by @thm:coble-integral-lifting-fibre(1), (2)) into the set of $\Gamma_\En$-orbits of primitive isotropic vectors of divisibility $2$ in $\ten$. The orbit of such a vector $\tilde w$ is in the image exactly when some $\gamma\in\Gamma_\En$ carries $\tilde w$ into $\eta(T_\Co)=k^{\perp\ten}$, that is, when
$$\beta_\ten\bigl(\tilde w,\ \gamma^{-1}k\bigr) = 0$$
for some $\gamma\in\Gamma_\En$: when $\tilde w$ is orthogonal to a $(-2)$-vector in the $\Gamma_\En$-orbit of $k$.
For example, by @lem:stable-orthogonal-not-transitive the isotropic generators $e'$ and $f'$ of the $U(2)$ summand lie in different $\widetilde\Orth^+(T_\Co)$-orbits, and $[\tilde e']\neq[\tilde f']$.

Every period of $T_\Co$ is orthogonal to $k$, so the image of $\fco$ in $\fen = \bD(\ten)/\Gamma_\En$ lies in the Heegner divisor $\mch_{-2}/\Gamma_\En$ (@thm:normalization). The cusp diagram of [@AEGS25, §2], with the two $0$-cusps $(10,10,0)_1$, $(10,8,0)_1$ and the two $1$-cusps $(8,8,0)_0$, $(8,6,0)_0$, is the diagram of $F^K_\En = \bD(\ten)/\Gamma^K_\En$.
