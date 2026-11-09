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

Cusp correspondence between the boundary lattices of $\fco$ and the cusps $(10,10,0)_1$, $(10,8,0)_1$, $(8,8,0)_0$, $(8,6,0)_0$ of the Enriques diagram of $F^K_\En$.
:::

We prove the cusp correspondence by comparing divisibilities of isotropic vectors at the corresponding 0-cusps and 1-cusps in both moduli spaces.

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
By @thm:unpolarized-cusps and @prop:tco-split-maximal, $\Orth^+(T_\Co)$ is transitive on primitive isotropic vectors, with quotient $\latI_{1,8}(2)$ at any of them, so $v_1$ represents *the* $0$-cusp of $\fco$ for the full orthogonal group and $$(v_1)^{\perp T_\Co}/v_1 \cong \latI_{1,8}(2) = (9,9,1) \cong \generators{2} \oplus E_8(2).$$ The arithmetic group $\Gamma_\Co = \Orth^+(T_\Co)^*$ has $527$ orbits of primitive isotropic vectors (@thm:cusp-lifting); they lie in one $\Orth^+(T_\Co)$-orbit, so all $527$ $0$-cusps of $\fco$ have boundary lattice $\latI_{1,8}(2)$.

Since $\tilde e' \tilde f' = 2$, and $\tilde e'$ is orthogonal to the remaining generators of $\ten$, we have

$$
\div_{\ten}(w_1) \definedas \div_{\ten}(\eta(e'))
= \div_{\ten}(\tilde e') = 2.
$$

Explicitly, writing $\ten = U \oplus U(2) \oplus E_8(2)$, one can check the pairing of $\tilde e'$ against an arbitrary vector.
Write $x+y+z\in U \oplus U(2)\oplus E_8(2)$; then

$$
\tilde e'\cdot(x+y+z) = \tilde e'\cdot y\in \theset{0, 2}
$$

since $y\in U(2)$ and $\tilde e'\in (U\oplus E_8(2))^{\perp \ten}$.
Thus $\beta_{\ten}(\tilde e', \ten) = \beta_{\ten}(\tilde e', U(2)) = 2\bZ$ since $\tilde e'\cdot\tilde f' = 2$.
:::

::: {.lemma #lem:w1_perp_calculation}

The 0-cusp $(9,9,1)_1$ in $\fco$ maps to the 0-cusp $(10, 8, 0)_1$ in $\fen$.
:::

::: {.proof}

The cusp correspondence follows from computing the lattice $w_1^{\perp \ten}/w_1$ under the primitive embedding $\eta$, since $\eta(v_1) = w_1$ and $v_1$ is the isotropic vector corresponding to $(9,9,1)_1$ in $\fco$:

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

Write $T_\Co = B(2)$ with $B = \latI_{2,9}$ (@prop:tco-as-twist), and let $J$ be a primitive isotropic plane of $T_\Co$, for instance $J = \generators{v_1, v_2}$ with $v_1 = e'$ and $v_2 = 2h+\alpha_1+\alpha_2$ in the basis $\generators{2}\oplus U(2)\oplus E_8(2)$. For a primitive isotropic line $l\subset J$, the proof of @thm:plane-transitivity-tco gives $l^{\perp B}/l\cong\latI_{1,8}$, and $J/l$ is a primitive isotropic line of it; by the proof of @prop:rank-nine-line-transitivity, its quotient is $\latI_{0,7}$. So $J^{\perp T_\Co}/J\cong\latI_{0,7}(2)\cong A_1^{\oplus 7}$, of type $(7,7,1)$, and all $189\,720$ $1$-cusps of $\fco$ (@thm:cusp-lifting) have boundary lattice $(7,7,1)_0$.
It remains to identify the isomorphism type of the image $\tilde J^{\perp \ten}/\tilde J$ in $\ten$.
One checks that both $v_2$ and $w_2$ are isotropic, and $v_2 \in v_1^{\perp T_\Co}/v_1$, and so $J$ and $\tilde J$ define isotropic planes in $T_\Co$ and $\ten$ respectively.
By [@AE22 Prop. 5.5, Lem. 5.9], it suffices to show

$$
\div_{w_1^{\perp \ten} /w_1}(w_2) \definedas \div_{U \oplus E_8(2)}(2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2)= 2
,
$$

since the isomorphism type of $\tilde J^\perp/\tilde J$ is uniquely determined by the isomorphism type of $w_2^{\perp \ten}/w_2$ in $w_1^{\perp \ten}/w_1$, which is in turn uniquely determined by the characterization of $w_2$ as odd, even ordinary, or even characteristic in $w_1^{\perp \ten}/w_1$, which by the $w_1^\perp$ calculation (@lem:w1_perp_calculation) is isomorphic to $U \oplus E_8(2)$.
One checks directly in coordinates: let $x+y\in U \oplus E_8(2)$ and consider its pairing with $w_2$:

$$
(x+y)\cdot w_2
= (x+y)\cdot (2\tilde e + 2\tilde f + \tilde \alpha_1 + \tilde \alpha_2 )
= 2x\cdot (\tilde e + \tilde f) + y\cdot (\tilde \alpha_1 + \tilde \alpha_2)
,
$$

where we've used orthogonality relations.
We note that the first term is evidently even, while the second term is even because all pairings are either zero or divisible by two in the $E_8(2)$ summand of $U \oplus E_8(2)$.
:::

::: {.remark}

This can also be proved by considering the divisorial presentation of $\fco$ as $\mch_{-2}/\Orth^+(\ten)^*$.
If $J'$ is an isotropic plane in $\ten$ generated by $x_1, x_2$ where both $x_i$ are orthogonal to a $(-2)$-vector in $\ten$, then the 1-cusp corresponding to $J'$ will be contained in the closure of $\mch_{-2}$.
One checks that cusp $(8, 6, 0)_0$ is associated to the isotropic plane

$$
J' = \generators{e', 2e + 2f + 2\bar\alpha_1} \subset \ten
$$

where both $e'$ and $2e + 2f + 2\bar\alpha_1$ are orthogonal to the $(-2)$-vector $e-f\in \ten$.
On the other hand, cusp $(8,8,0)$ does not satisfy this property -- the vector $e\in \ten$ is not orthogonal to any $(-2)$-vectors in $\ten$, and the isotropic plane at this cusp must include $e$ as a generator.
:::

::: {.remark}

The two 1-cusps $(8,8,0)$ and $(8,6,0)$ in $\fen$ are isomorphic to the modular curves $X_0(2)$ and $X \definedas \overline{\bH / \SL_2(\bZ)}$ respectively, and by [@CDL25 Cor. 5.9.10] the 1-cusp $(7,7,1)$ in $\fco$ is isomorphic to $X$.
This can additionally be verified by [@AE22 Prop. 5.13]: the 1-cusp $(7,7,1)$ in $T_\Co$ is incident, as a full-orthogonal-group stratum, to exactly one 0-cusp, as is the 1-cusp $(8,6,0)$ in $\ten$, and thus the corresponding modular curves are both isomorphic to $X$.
We conjecture that general correspondences on $1$-cusps must preserve the isomorphism types of the corresponding modular curves, yielding an alternative proof of @lem:1_cusp_correspondence.
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

An enumeration in Sage agrees: $\tilde J^\perp/\tilde J$ has $480$ roots, forming one irreducible system.
:::

::: {.remark}

Sterk cusp $2$ is the folding of $(18,0,0)_1$ by the reflection $\alpha_k\mapsto\alpha_{20-k}$ of its Coxeter diagram [@AEGS25 Lemma 3.9]. Under @conj:coble-zero-cusp-sterk-two, the integral-affine and Kulikov models at the Coble $0$-cusp are of disc type, as at Sterk cusp $2$ (@ex:fen2_five_cusps).
:::

## The orbit map on $0$-cusps {#sec-cusp-orbit-map}

Throughout, $\Gamma_\En\definedas\Orth^+(\ten)^*$, as in @thm:normalization, and $\Gamma^K_\En\definedas\Orth(\ten)$ is the group of [@AEGS25].

Let $K = T_\Co^{\perp\ten} = \ZZ k$, with $k = \tilde e - \tilde f$ and $k^2 = -2$. The gluing group of $T_\Co\oplus K\subset\ten$ is $H = \generators{(h/2,\,k/2)}\leq A_{T_\Co}\oplus A_K$, which is isotropic because $q_{T_\Co}(h/2) + q_K(k/2) = \frac12-\frac12 = 0$. Every $\varphi\in\Gamma_\Co$ acts trivially on $A_{T_\Co}$, so $\varphi\oplus\id_K$ preserves $H$ and extends to an element of $\Gamma_\En$ by @thm:automorphism-lifting-criterion, as in the proof of @thm:normalization. This gives a homomorphism
$$\mathrm{Ext}\colon\Gamma_\Co\too\Stab_{\Gamma_\En}(T_\Co)\subset\Gamma_\En,\qquad \varphi\mapsto\tilde\varphi,\quad \tilde\varphi(k) = k,$$
with $\mathrm{res}\circ\mathrm{Ext} = \id$. So $\mathrm{Ext}$ is injective, and its image is the stabilizer of the vector $k$ in $\Stab_{\Gamma_\En}(T_\Co)$. The kernel of $\mathrm{res}$ is $\{1, s_k\}$, where $s_k$ is the reflection in $k$, which fixes $T_\Co$ pointwise and negates $k$; so the stabilizer of the line $\ZZ k$ is $\mathrm{Ext}(\Gamma_\Co)\times\generators{s_k}$.
The embedding $\eta$ is equivariant, $\eta(\varphi v) = \mathrm{Ext}(\varphi)\,\eta(v)$, so it induces a map of orbit sets
$$\Phi\colon\Gamma_\Co\backslash\{\text{primitive isotropic vectors of }T_\Co\}\ \longrightarrow\ \Gamma_\En\backslash\{\text{primitive isotropic vectors of }\ten\}.$$

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
$$\Phi^{-1}\bigl([\tilde w]\bigr) = \Stab_{\Gamma_\En}(\tilde w)\,\backslash\, Y\, /\, \mathrm{Ext}(\Gamma_\Co).$$
Both actions preserve $Y$. For $h\in\Stab_{\Gamma_\En}(\tilde w)$, $(h\gamma)^{-1}\tilde w = \gamma^{-1}h^{-1}\tilde w = \gamma^{-1}\tilde w$, so $v_{h\gamma} = v_\gamma$. For $\varphi\in\Gamma_\Co$,
$$\bigl(\gamma\,\mathrm{Ext}(\varphi)\bigr)^{-1}\tilde w = \mathrm{Ext}(\varphi)^{-1}\gamma^{-1}\tilde w = \mathrm{Ext}\bigl(\varphi^{-1}\bigr)\eta(v_\gamma) = \eta\bigl(\varphi^{-1}v_\gamma\bigr),$$
so $v_{\gamma \mathrm{Ext}(\varphi)} = \varphi^{-1}v_\gamma$.
Conversely, if $[v_\gamma] = [v_{\gamma'}]$, say $v_{\gamma'} = \varphi v_\gamma$, then $\gamma'^{-1}\tilde w = \eta(\varphi v_\gamma) = \mathrm{Ext}(\varphi)\gamma^{-1}\tilde w$, that is $\gamma \mathrm{Ext}(\varphi)^{-1}\gamma'^{-1}\in\Stab_{\Gamma_\En}(\tilde w)$, which gives $\gamma' \in \Stab_{\Gamma_\En}(\tilde w)\,\gamma\,\mathrm{Ext}(\Gamma_\Co)$. So the double cosets are exactly the classes over $[\tilde w]$, and the fibre is empty exactly when $Y$ is.

::: {.proposition #prop:cusp-map-separates-mod-two}

Let $v, v'$ be primitive isotropic vectors of $T_\Co$. If $\eta(v)$ and $\eta(v')$ lie in the same $\Gamma_\En$-orbit, then $v\equiv v'\pmod{2T_\Co}$.
:::

::: {.proof}

Put $x = \eta(v)$ and $x' = \eta(v')$, which have divisibility $2$ in $\ten$ by @prop:cusp-map-not-onto, and let $\gamma\in\Gamma_\En$ with $\gamma x = x'$. The class
$$\bar x \definedas \tfrac12 x \bmod \ten \in A_\ten = \ten^\vee/\ten$$
is defined, and isotropic because $x^2 = 0$. Then $\gamma(x/2) = x'/2$, and $\gamma$ acts trivially on $A_\ten$ because $\Gamma_\En\subseteq\discriminantkernel{\ten}$, so $\bar x = \overline{x'}$, that is $\tfrac12(x - x')\in\ten$ and $x\equiv x'\pmod{2\ten}$. Since $\eta(T_\Co)$ is primitive in $\ten$, $2\ten\intersect\eta(T_\Co) = 2\eta(T_\Co)$, so $v\equiv v'\pmod{2T_\Co}$.
:::

::: {.proposition #prop:cusp-map-injective}

The orbit map $\Phi$ is injective: if $v, v'$ are primitive isotropic vectors of $T_\Co$ and $\eta(v)$, $\eta(v')$ lie in one $\Gamma_\En$-orbit, then $v$ and $v'$ lie in one $\Gamma_\Co$-orbit.
:::

::: {.proof}

By @prop:cusp-map-separates-mod-two, $v\equiv v'\pmod{2T_\Co}$, so $\tfrac12 v - \tfrac12 v'\in T_\Co$ and the classes $v^* = \tfrac12 v + T_\Co$ and $v'^*$ of @prop:coble-primitive-isotropic-classes are equal. By @thm:cusp-lifting, parts 1 and 4 with $\Gamma = \ker\rho_{T_\Co}$, for which $H$ is trivial, the map $\Gamma_\Co v\mapsto v^*$ is injective. Hence $\Gamma_\Co v = \Gamma_\Co v'$.
:::

So $\Phi$ embeds the $527$ $0$-cusps of $\fco$ into the set of $\Gamma_\En$-orbits of primitive isotropic vectors of divisibility $2$ in $\ten$. The orbit of such a vector $\tilde w$ is in the image exactly when some $\gamma\in\Gamma_\En$ carries $\tilde w$ into $\eta(T_\Co)=k^{\perp\ten}$, that is, when
$$\beta_\ten\bigl(\tilde w,\ \gamma^{-1}k\bigr) = 0$$
for some $\gamma\in\Gamma_\En$: when $\tilde w$ is orthogonal to a $(-2)$-vector in the $\Gamma_\En$-orbit of $k$.
For example, by @lem:stable-orthogonal-not-transitive the isotropic generators $e'$ and $f'$ of the $U(2)$ summand lie in different $\Gamma_\Co$-orbits, and $[\tilde e']\neq[\tilde f']$.

Every period of $T_\Co$ is orthogonal to $k$, so the image of $\fco$ in $\fen = \bD(\ten)/\Gamma_\En$ lies in the Heegner divisor $\mch_{-2}/\Gamma_\En$ (@thm:normalization). The cusp diagram of [@AEGS25, §2], with the two $0$-cusps $(10,10,0)_1$, $(10,8,0)_1$ and the two $1$-cusps $(8,8,0)_0$, $(8,6,0)_0$, is the diagram of $F^K_\En = \bD(\ten)/\Gamma^K_\En$.
