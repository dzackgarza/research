# Period domain embeddings and normalization {#sec-lattices}

::: {.notation title="The lattices of this chapter"}

$$
\begin{aligned}
    \lkt &= (22, 0, 0)_3 = U^3 \oplus E_8^2 = \latII_{3, 19} &
    E_{10} &= (10, 0, 0)_1 = U \oplus E_8 = \latII_{1, 9} \\
    S_\En &= \EnriquesInvariants_1 = E_{10}(2) &
    T_\En &= (12, 10, 0)_2 = U \oplus E_{10}(2) \\
    S_\Co &= (11, 11, 1)_1 = \generators{-2} \oplus E_{10}(2) &
    T_\Co &= (11,11,1)_2 = \generators{2} \oplus E_{10}(2) \\
    \sdp &= (2,2,0)_1 = U(2) &
    \tdp &= (20, 2, 0)_2 = U \oplus U(2) \oplus E_8^2
\end{aligned}
$$

:::

::: {.lemma #lem:primitive_embedding_eta}

Writing

$$
\begin{aligned}
T_\Co = \generators{2} \oplus E_{10}(2) &= \generators{h, e', f',\alpha_1,\cdots, \alpha_8} \\
T_\En = U \oplus E_{10}(2) &= \generators{\tilde e,\tilde f,\tilde e',\tilde f',\tilde \alpha_1,\cdots,\tilde \alpha_8},
\end{aligned}
$$

there is an embedding of lattices $T_\Co \injects T_\En$:

$$
\begin{aligned}
\eta: \generators{2} \oplus E_{10}(2) &\to U \oplus E_{10}(2) \\
(h, x) &\mapsto (\tilde e + \tilde f, x)
\end{aligned}
$$

which sends the basis vector $h$ of $\generators{2}$ to $\tilde e+\tilde f\in U$ and is the identity on the $E_{10}(2)$ summand.
Since $\coker \eta$ is torsionfree, $\eta$ is a primitive embedding.
:::

::: {.proof}

The map is well defined and isometric: $h$ has square $2$ and $\tilde e+\tilde f$ has square $2$, since $\tilde e,\tilde f$ are the isotropic basis of $U$ with $\tilde e\cdot\tilde f=1$; and $\eta$ is the identity on $E_{10}(2)$, which is an orthogonal summand of both sides.
So $\eta$ is a morphism of lattices of $\mathbf{Lat}_{\bZ}$, and it is injective because it is injective on each summand.

For primitivity, $\eta(T_{\Co})=\bZ(\tilde e+\tilde f)\oplus E_{10}(2)$, so
$$
T_\En/\eta(T_\Co)\;\cong\;U/\bZ(\tilde e+\tilde f).
$$
The homomorphism $U\to\bZ$, $a\tilde e+b\tilde f\mapsto a-b$, is surjective with kernel $\bZ(\tilde e+\tilde f)$, so $\coker\eta\cong\bZ$ is torsion-free, and $\eta$ is primitive by @prop:primitive-characterization.
:::

::: {.lemma #lem:sequence_of_embeddings}

There is a sequence of primitive embeddings

$$
T_{\Co} \injects \ten \injects \tdp \injects \lkt
$$

which is unique up to $\Orth(\lkt)$.
In particular, this yields an embedding

$$
\begin{aligned}
\generators{2} \oplus U(2) \oplus E_8(2) &\injects U \oplus U(2) \oplus E_8^2 \\
(h,x,y) & \mapsto (\tilde e + \tilde f, x, y, y)
\end{aligned}
$$

and thus an embedding $\fco \injects \fttz$.
:::

::: {.proof}

The displayed map is isometric on each summand: on $\generators{2}$ as in @lem:primitive_embedding_eta, on $U(2)$ as the identity, and on $E_8(2)$ because $(y,y)^2 = 2y^2$ in $E_8\oplus E_8$.
Its cokernel is $U/\bZ(\tilde e+\tilde f)\oplus(E_8\oplus E_8)/\theset{(y,y)}$.
The first summand is $\bZ$ by @lem:primitive_embedding_eta, and $(a,b)\mapsto a-b$ identifies the second with $E_8$.
The cokernel is torsion-free, so the map is primitive by @prop:primitive-characterization.
The embedding $\fco\injects\fttz$ is the one that @lem:locally_closed_embedding_BB induces.

For uniqueness, by [@AEGS25 Lem. 2.4] it suffices to show uniqueness of $\sen \injects S_{\Co}$, i.e.

$$
E_{10}(2) \injects \generators{-2}\oplus E_{10}(2)
,
$$

or equivalently by untwisting,

$$
E_{10} \injects \generators{-1}\oplus E_{10}
.
$$

This embedding is unique because $E_{10} = U \oplus E_8$ is unimodular.
For a primitive embedding $\iota\colon E_{10}\injects L$, @prop:unimodular-splits gives $L\isoto E_{10}\perp E_{10}^{\perp L}$.
By @cons:embedding-gluing-data, its gluing datum is the graph of an isometry between a subgroup of $A_{E_{10}}$ and a subgroup of $A_{E_{10}^{\perp L}}$; since $A_{E_{10}}=0$, the datum is trivial and the embedding is determined by the isometry class of the complement.
Similarly, by [@Nik80 Cor. 1.5.2, Thm. 3.6.3], the homomorphism $\Orth(\lkt)\to \Orth(T_\Co)$ is surjective.
:::

::: {.lemma #lem:locally_closed_embedding_BB}

The embeddings of lattices $\eta: T_\Co\injects T_\En$ (resp. $T_{\Co} \injects \tdp$) induce locally closed embeddings $\fco \injects \fen$ (resp. $\fco \injects \fttz$) which extend to morphisms on the Baily--Borel compactifications.
:::

::: {.proof}

This follows from [@KK72 §5, Thm.2].
:::

::: {.theorem #thm:normalization}

$\fco$ is the normalization of the Heegner divisor $\mch_{-2}/\Gamma_\En$ of $\fen = \bD(\ten)/\Gamma_\En$.
:::

::: {.proof}

Write $\Gamma_\Co\definedas\Orth^+(T_\Co)^*$ and $\Gamma_\En\definedas\Orth^+(T_\En)^*$, and let
$$
f\colon \fco = \bD(T_\Co)/\Gamma_\Co \too \bD(\ten)/\Gamma_\En
$$
be the map induced by the embedding $\eta$ of @lem:primitive_embedding_eta. Every period of $T_\Co$ is orthogonal to $k = \tilde e-\tilde f$, a vector of square $-2$, so the image of $f$ lies in the Heegner divisor $\mch_{-2}/\Gamma_\En$.

The gluing datum.
Put $K\definedas \eta(T_\Co)^{\perp T_\En}$.
Since $\eta(h) = \tilde e+\tilde f$ and $\eta$ is the identity on the $E_{10}(2)$ summand, $K$ is the orthogonal complement of $\tilde e+\tilde f$ in $U = \generators{\tilde e,\tilde f}$, so $K = \ZZ k$ with $k\definedas\tilde e-\tilde f$ and $k^2 = -2$.
Thus $K\cong\generators{-2}$, and $A_K$ is generated by $k/2$ with $q_K(k/2) = -1/2$.
Because $\tilde e = \frac12\bigl(\eta(h)+k\bigr)$, the overlattice $T_\En$ of $T_\Co\oplus K$ has gluing group
$$
H = \generators{\bigl(h/2,\; k/2\bigr)}\ \leq\ A_{T_\Co}\oplus A_K
$$
in the sense of @def:gluing-datum-of-a-pair.
It has order $2$ and is isotropic, since $q_{T_\Co}(h/2)+q_K(k/2) = \frac12-\frac12 = 0$.

In $A_{T_\Co} = \generators{h/2}\oplus A_{E_{10}(2)}$ the summand $A_{E_{10}(2)}$ is orthogonal to $h/2$.

The stabilizer.
We claim that restriction to $T_\Co$ carries $\Stab_{\Gamma_\En}(T_\Co)$ onto $\Gamma_\Co$.

Let $g\in\Gamma_\En$ satisfy $g(T_\Co) = T_\Co$.
Then $g$ preserves $K = T_\Co^{\perp T_\En}$ as well, so $g = \varphi\oplus\eps$ with $\varphi\definedas\restrictionof{g}{T_\Co}\in\Orth(T_\Co)$ and $\eps = \pm 1$ on $K$.
By @thm:automorphism-lifting-criterion, $g$ preserves $T_\En$ only if $(\bar\varphi\oplus\bar\eps)(H) = H$.
The group $A_K$ has order $2$, so $\bar\eps = \id$, and the condition on the generator of $H$ reads $\bigl(\bar\varphi(h/2),\,k/2\bigr)\in H$.
The only element of $H$ with second coordinate $k/2$ is the generator, so
$$
\bar\varphi(h/2) = h/2
.
$$
Next let $x\in A_{E_{10}(2)}$.
Then $(x,0)\in H^{\perp_{A_{T_\Co}\oplus A_K}}$, because $x$ is orthogonal to $h/2$.
By Nikulin's gluing theorem (@thm:nikulin-gluing) the discriminant group of $T_\En$ is $H^{\perp_{A_{T_\Co}\oplus A_K}}/H$, and $g$ lies in the stable orthogonal group, so $g$ fixes that quotient pointwise; hence $\bigl(\bar\varphi(x)-x,\,0\bigr)\in H$.
Every nonzero element of $H$ has second coordinate $k/2\neq 0$, so $\bar\varphi(x) = x$.
The two displays give $\bar\varphi = \id$ on all of $A_{T_\Co}$, that is $\varphi\in\tilde\Orth(T_\Co)$.
Finally $g$ preserves the component $\bD(T_\En)$, and $\bD(T_\Co) = \bD(T_\En)\intersect\PP(T_\Co\tensor_\ZZ\CC)$, so $\varphi$ preserves $\bD(T_\Co)$ and lies in $\Orth^+(T_\Co)$.
Therefore $\varphi\in\Gamma_\Co$.

Conversely let $\varphi\in\Gamma_\Co$ and put $g\definedas\varphi\oplus\id_K$.
Both $\bar\varphi$ and $\bar{\id}_K$ are the identity, so $g$ preserves $H$ and extends to $T_\En$ by @thm:automorphism-lifting-criterion.
The extension acts trivially on $H^{\perp_{A_{T_\Co}\oplus A_K}}/H = A_{T_\En}$ and preserves $\bD(T_\En)$, so it lies in $\Gamma_\En$; it stabilizes $T_\Co$ and restricts to $\varphi$ there.

Hence $\varphi\mapsto\varphi\oplus\id_K$ is a homomorphism $\Gamma_\Co\to\Gamma_\En$ with $\eta\circ\varphi = (\varphi\oplus\id_K)\circ\eta$, and $f$ is well defined.

Fibres.
For $x = [\omega]\in\bD(T_\En)$ let $T(x)$ be the smallest primitive sublattice of $T_\En$ whose complexification contains $\omega$, namely $T(x)\definedas\bigl(T_\En\intersect\omega^{\perp_{T_\En\tensor_\ZZ\CC}}\bigr)^{\perp T_\En}$.
For a primitive sublattice $M\leq T_\En$ of signature $(2,\ast)$ one has $x\in\bD(M)$ if and only if $T(x)\iscontainedin M$.

Fix $y\in F_\En$ and a lift $\tilde y\in\bD(T_\En)$.
A point of $\inverseof{f}(y)$ is a $\Gamma_\Co$-orbit of a point $x = g\tilde y$ with $g\in\Gamma_\En$ and $x\in\bD(T_\Co)$.
Writing $M'\definedas \inverseof{g}(T_\Co)$, that last condition says $T(\tilde y)\iscontainedin M'$.
Now $M'^{\perp T_\En} = \inverseof{g}(K) = \ZZ v$ with $v^2 = -2$, and $v\perp T(\tilde y)$.
The space $T(\tilde y)\tensor_\ZZ\RR$ contains a positive definite plane and $T_\En$ has signature $(2,10)$, so $T(\tilde y)^{\perp T_\En}$ is negative definite and contains only finitely many vectors of square $-2$.
Each such $v$ determines $M' = v^{\perp T_\En}$, so only finitely many $M'$ occur.
For a fixed $M'$ the elements $g$ with $\inverseof{g}(T_\Co) = M'$ form one coset of $\Stab_{\Gamma_\En}(T_\Co)$, whose restrictions to $T_\Co$ all lie in $\Gamma_\Co$ by the previous step; the corresponding points $x$ therefore form a single $\Gamma_\Co$-orbit.
Hence $\inverseof{f}(y)$ is finite, of cardinality at most half the number of $(-2)$-vectors of $T(\tilde y)^{\perp T_\En}$.

Properness and finiteness.
By @lem:locally_closed_embedding_BB, the map $f$ extends to a morphism $\bar f\colon\overline{F_\Co}^{\operatorname{BB}}\to \overline{F_\En}^{\operatorname{BB}}$ of projective varieties, which is therefore proper.
A boundary component of $\overline{F_\Co}^{\operatorname{BB}}$ is indexed by a primitive isotropic sublattice $I\leq T_\Co$ of rank $1$ or $2$, and the saturation of $I$ in $T_\En$ is again primitive isotropic of the same rank.
So $\bar f$ carries boundary to boundary, giving $\inverseof{\bar f}(\fen) = \fco$, and $f$ is proper because properness is stable under base change.
A proper morphism with finite fibres is finite ([@stacks-02LS]), so $f$ is finite.
Let $Z\definedas f(\fco)$, which is closed in $\fen$ because a finite morphism is closed.

Generic injectivity.
A proper primitive sublattice $S\subsetneq T_\Co$ of signature $(2,\ast)$ cuts out a proper closed analytic subset $\bD(S)\subsetneq\bD(T_\Co)$, and there are countably many such $S$.
So the set of $x\in\bD(T_\Co)$ with $T(x) = T_\Co$ is the complement of countably many proper closed analytic subsets, hence dense.
For such an $x$ the fibre computation allows only $M' = T_\Co$: one has $T_\Co = T(x)\iscontainedin M'$ with both primitive of rank $11$.
The fibre through $x$ is therefore a single point.
The locus where a finite morphism of irreducible varieties has more than its generic number of preimages is a proper closed subset, and a dense set is not contained in one, so $f\colon F_\Co\to Z$ has degree $1$ and is birational.

Finally $F_\Co$ is normal, being the quotient of a bounded symmetric domain by a properly discontinuous group of automorphisms.
A finite birational morphism from a normal variety onto a reduced irreducible variety is its normalization, so $F_\Co$ is the normalization of $Z$.
:::

::: {.remark #rmk:normalization-enriques-analogue title="The Enriques case"}

For Enriques surfaces, $\fentwo$ is the normalization of a closed subvariety of $\fttz$ [@AEGS25 Lem. 2.8].
:::

::: {.proposition #prop:sterk-group-identification title="The discriminant image of $\gent$"}

Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten}, q_{\ten})$ be the discriminant representation and $K = \ker\rho$.
Identify $\ten = U\oplus U(2)\oplus E_8(2)$ with the lattice $L_- = \mathbf H\oplus\mathbf H(2)\oplus E_8(-2)$ of [@Ste91, §2] summand by summand, and let $e', f'$ be the isotropic basis of $U(2)$, with $(e', f') = 2$.

1. $\gent$ is the group $\Gamma$ of [@Ste91, §2], and $\gent = \theset{g\in\Orth(\ten) \st \rho(g)\text{ preserves the summands } A_{U(2)} \text{ and } A_{E_8(2)} \text{ of } A_{\ten}}$.
2. $\rho(\gent) = M\definedas\Orth(q_{U(2)})\times\Orth(q_{E_8(2)})$, and $\gent = \rho^{-1}(M)$; in particular $K\subseteq\gent$.
3. $\gent$ is a proper subgroup of $\Stab_{\Orth(\ten)}\bigl([(e'+f')/2]\bigr)$.
:::

::: {.proof}

(1) The group $\Gamma$ of [@Ste91, §2] is the image in $\Orth(L_-)$ of the isometries of the K3 lattice that commute with the Enriques involution and fix the polarization vector, and $\gent$ is the image in $\Orth(\ten)$ of the same group [@AEGS25 Def. 2.6].
The description by the two summands is [@Ste91, Prop. 2.7].

(2) Because $U$ is unimodular, $A_{\ten} = A_{U(2)}\perp A_{E_8(2)}$, and an isometry of $q_{\ten}$ preserves both summands exactly when it is a pair of isometries of the summands.
So (1) says $\gent = \rho^{-1}(M)$.
The lattice $\ten$ is even, indefinite and $2$-elementary, so $\rho$ is surjective (@thm:two-elementary-surjectivity), and $\rho(\gent) = M$.

(3) The three nonzero classes of $A_{U(2)}$ are $[e'/2]$, $[f'/2]$ and $[(e'+f')/2]$, with $q$-values $0$, $0$ and $(e'+f')^2/4 = 1$.
So every element of $\Orth(q_{U(2)})$ fixes $[(e'+f')/2]$, and $\gent$ stabilizes it by (2).
Since $f'\in\ten$, the classes $[(e'+f')/2]$ and $[(e'-f')/2]$ are equal.
The isometry $\psi\in\Orth(L_-)$ of [@Ste91, Rem. 2.8] stabilizes $\tfrac12(e'-f')+L_-$ and is not in $\Gamma$.
:::

::: {.proposition #prop:gamma-en-two-index title="The index of $\gent$"}

With $\rho$, $K$ and $M$ as in @prop:sterk-group-identification,
$$
[\Orth(\ten) : \gent] \;=\; [\Orth(A_{\ten},q_{\ten}) : M] \;=\; 2^7\cdot 17\cdot 31 \;=\; 67\,456 .
$$
:::

::: {.proof}

By @prop:sterk-group-identification, $\gent = \rho^{-1}(M)$ and $\rho$ is surjective, so $\rho$ induces a bijection $\Orth(\ten)/\gent\to\Orth(A_{\ten},q_{\ten})/M$.
Because $U$ is unimodular, $A_{\ten} = A_{E_{10}(2)}$, so $\abs{\Orth(A_{\ten},q_{\ten})} = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31$ by @prop:coble-discriminant-group.
By @prop:gamma-en-two-gluing, $M = \rho(\gent)$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$ in $\Orth(q_{\sen})$, which has order $\abs{W(E_8)} = 2^{14}\cdot3^5\cdot5^2\cdot7$ by @thm:coble-heegner-finite-orbits(1).
The quotient of the two orders is $2^7\cdot17\cdot31$.
This is the index computed in [@Ste91, Rem. 2.12].
:::

::: {.proposition #prop:ten-plane-classes title="The two classes of primitive isotropic planes of $\ten$"}

Write $e,f$ for the isotropic basis of $U$ and $e',f'$ for that of $U(2)$, with $(e,f) = 1$ and $(e',f') = 2$.
Identify the summand $E_8(2)$ with $E_8 = \theset{y_0\in\ZZ^8\cup(\ZZ^8+s) \st \textstyle\sum_i y_{0,i}\in2\ZZ}$, $s = \tfrac12(1,\dots,1)$ [@CS10, Ch. 4, §8.1], so that $y\leftrightarrow y_0$ and $(y,y') = -2\,y_0\cdot y_0'$.
Let $\alpha\in E_8(2)$ correspond to $2e_1$, and put $z\definedas 2e+2f+\alpha$.
For a primitive totally isotropic plane $\varPi\subseteq\ten$ let $D(\varPi)\leq A_{\ten}$ be the image of $\varPi_\QQ\cap\ten^*$, as in @not:isotropic-reduction-setup.

1. $\varPi_1 = \generators{e,e'}$ and $\varPi_2 = \generators{z,e'}$ are primitive totally isotropic planes.
   Every primitive totally isotropic plane $\varPi$ is $\Orth(\ten)$-equivalent to exactly one of them, and to $\varPi_1$ exactly when it contains a vector of divisibility one.
2. If $\varPi$ contains a vector of divisibility one, then $D(\varPi)$ has order $2$, its nonzero element is $[v/2]$ for every primitive $v\in\varPi$ of divisibility two, and $\varPi^\perp/\varPi\cong E_8(2)$.
3. If $\varPi$ contains no vector of divisibility one, then $D(\varPi)$ has order $4$, its three nonzero elements are the classes $[p/2]$ of the primitive $p\in\varPi$, and $\varPi^\perp/\varPi\cong D_8^*(2)$, where $D_8^*$ carries the negative of the Euclidean form.
:::

::: {.proof}

(1) The vectors $e$, $e'$ and $z$ are isotropic and pairwise orthogonal: $(2e+2f)^2 = 8$ and $\alpha^2 = -2\cdot4 = -8$.
The vector $\alpha/2$ corresponds to $e_1\notin E_8$, so $z$ is primitive in $U\oplus E_8(2)$, and $e'$ is primitive in $U(2)$; a span of primitive vectors of two orthogonal summands is primitive in their sum, so $\varPi_2$ is primitive, and so is $\varPi_1$.
The vector $e$ has divisibility one.
For a primitive $az+be'\in\varPi_2$, the ideal $(az+be',\ten)$ contains $(az+be',f) = 2a$ and $(az+be',f') = 2b$, and it lies in $2\ZZ$ because $(z,\ten)$ and $(e',\ten)$ do; so $az+be'$ has divisibility two.
By [@Ste91, Prop. 4.6] there are exactly two $\Orth(\ten)$-classes of primitive isotropic planes, and divisibility is invariant under $\Orth(\ten)$, so $\varPi_1$ and $\varPi_2$ represent the two classes.

(2), (3): the subgroup $D(\varPi)$.
$A_{\ten}$ has exponent two, so $2\ten^*\subseteq\ten$, and primitivity of $\varPi$ gives $\varPi_\QQ\cap\ten^*\subseteq\tfrac12(\varPi_\QQ\cap\ten) = \tfrac12\varPi$.
A vector $p/2$ with $p\in\varPi$ lies in $\ten^*$ exactly when $(p,\ten)\subseteq 2\ZZ$, and $[p/2] = 0$ exactly when $p\in 2\varPi$.
So $D(\varPi)$ is the image of $\theset{p\in\varPi \st (p,\ten)\subseteq 2\ZZ}$ in $\varPi/2\varPi$.
If $\varPi$ contains a vector of divisibility one, then by (1) it is the image of $\varPi_1$ under an isometry, so it has a basis $u, v$ with $\operatorname{div}(u) = 1$ and $\operatorname{div}(v) = 2$.
Then $(au+bv,\ten)\subseteq 2\ZZ$ exactly when $a$ is even, so $D(\varPi) = \theset{0,[v/2]}$; a primitive $au+bv$ with $a$ even has $b$ odd and the class $[v/2]$.
If $\varPi$ contains no vector of divisibility one, then every $p\in\varPi$ has $(p,\ten)\subseteq 2\ZZ$, so $D(\varPi) = \varPi/2\varPi$ has order $4$, and its nonzero elements are the classes of the primitive vectors.

(2), (3): the quotients.
An isometry carrying $\varPi$ to $\varPi'$ induces an isometry $\varPi^\perp/\varPi\to\varPi'^\perp/\varPi'$, so by (1) it suffices to compute the quotients for $\varPi_1$ and $\varPi_2$.
Write $x = ae+bf+ce'+df'+y$ with $y\in E_8(2)$.
Then $(x,e) = b$ and $(x,e') = 2d$, so $\varPi_1^\perp = \ZZ e\oplus\ZZ e'\oplus E_8(2)$ and $\varPi_1^\perp/\varPi_1\cong E_8(2)$.

For $\varPi_2$, one has $(y,\alpha) = -4y_{0,1}$, so $x$ is orthogonal to $e'$ exactly when $d = 0$, and orthogonal to $z$ exactly when $2a+2b-4y_{0,1} = 0$, that is $a+b = 2y_{0,1}$.
So $\varPi_2^\perp = \ZZ e'\oplus W$ with $W = \theset{ae+bf+y \st a+b = 2y_{0,1}}$, and $z\in W$, so $\varPi_2^\perp/\varPi_2 = W/\ZZ z$.
For $x = ae+bf+y\in W$ put $u\definedas a - y_{0,1}$, so that $a = y_{0,1}+u$ and $b = y_{0,1}-u$, and define the linear map
$$
\pi\colon W\too\QQ^8,\qquad ae+bf+y\longmapsto(u, y_{0,2},\dots,y_{0,8}).
$$
Then $x^2 = 2ab + y^2 = 2(y_{0,1}^2-u^2) - 2\abs{y_0}^2 = -2\abs{\pi(x)}^2$, so $(x,x') = -2\,\pi(x)\cdot\pi(x')$.
If $\pi(x) = 0$, then $y_0 = y_{0,1}e_1\in E_8$ forces $y_{0,1} = 2k$ with $k\in\ZZ$, so $a = b = 2k$, $y = k\alpha$ and $x = kz$; hence $\ker\pi = \ZZ z$.
The image of $\pi$ is $\ZZ^8\cup(\ZZ^8+s)$.
It is contained in this set, because $u$ and $y_{0,1}$ are both integers or both in $\ZZ+\tfrac12$.
For $(u,y')\in\ZZ^8\cup(\ZZ^8+s)$ choose $y_{0,1}$ in $\ZZ$ or in $\ZZ+\tfrac12$, matching $u$, with $y_{0,1}+\sum_j y'_j$ even; then $y_0 = (y_{0,1},y')\in E_8$, the numbers $a = y_{0,1}+u$ and $b = y_{0,1}-u$ are integers, and $\pi(ae+bf+y) = (u,y')$.
The set $\ZZ^8\cup(\ZZ^8+s)$ is $D_8^*$ [@CS10, Ch. 4, §7.1], so $\pi$ induces an isometry $\varPi_2^\perp/\varPi_2\cong D_8^*(2)$.
:::

::: {.lemma #lem:half-vector-eichler title="Eichler transvections along a vector of divisibility two"}

Let $A = A_{\ten}$ with its discriminant quadratic form $q$ of @def:discriminant.
Then $q([x/2]) = x^2/4\bmod 2$, so $(A, q)$ is a quadratic space over $\F_2$, with polar form $\beta_q([x/2],[y/2]) = (x,y)/2\bmod 2$.
Let $d\in A$ be isotropic and nonzero, and for $c\in d^\perp$ define
$$
T_{d,c}(a)\definedas a+\beta_q(a,d)\,c+\bigl(\beta_q(a,c)+q(c)\,\beta_q(a,d)\bigr)\,d .
$$
Let $\eta\in\ten$ be a primitive isotropic vector of divisibility two with $[\eta/2] = d$.

1. For $w\in\ten^*$ with $(w,\eta) = 0$, the Eichler--Siegel transvection $E_{\eta,w}$ of @def:eichler-siegel lies in $\Orth(\ten)$, fixes $\eta$, maps every primitive totally isotropic plane that contains $\eta$ onto itself, and satisfies $\rho(E_{\eta,w}) = T_{d,[w]}$.
2. Every $c\in d^\perp$ is $[w]$ for some $w\in\ten^*$ with $(w,\eta) = 0$.
3. $c\mapsto T_{d,c}$ is a homomorphism $d^\perp\to\Orth(A,q)$ with kernel $\generators{d}$; its image $U_d$ has order $2^8$.
4. Each $T_{d,c}$ fixes $d$ and acts trivially on $d^\perp/\generators{d}$.
   If $D\ni d$ is an isotropic subgroup, then $T_{d,c}$ acts trivially on $D^\perp/D$, and trivially on $D$ when $c\in D^\perp$.
:::

::: {.proof}

Squares of vectors of $\ten^* = U\oplus\tfrac12U(2)\oplus\tfrac12E_8(2)$ are integers: $(ae'+bf')^2/4 = ab$, and $y^2/4 = -\abs{y_0}^2/2\in\ZZ$ for $y\in E_8(2)$ in the coordinates of @prop:ten-plane-classes.
For $x/2\in\ten^*$ and $t\in\ten$ one has $(x+2t)^2/4 = x^2/4+(x,t)+t^2$ with $(x,t)+t^2\in2\ZZ$, so $q([x/2]) = x^2/4\bmod 2$ is well defined, and $\beta_q$ is its polar form because $(x+y)^2/4 = x^2/4+y^2/4+(x,y)/2$.

(1) For $x\in\ten$ one has $(\eta,x)\in2\ZZ$ and $2w\in\ten$, so $(\eta,x)w\in\ten$; also $(w,x)\in\ZZ$ and $\tfrac12 w^2(\eta,x)\in\ZZ$.
So the formula of @def:eichler-siegel maps $\ten$ into $\ten$.
$E_{\eta,w}$ is an isometry of $\ten_\QQ$, so $E_{\eta,w}(\ten)$ has the discriminant of $\ten$ and $E_{\eta,w}(\ten) = \ten$.
For $p\perp\eta$ the formula reads $E_{\eta,w}(p) = p-(w,p)\eta$; so $E_{\eta,w}$ fixes $\eta$ and maps a totally isotropic plane $\varPi\ni\eta$ into itself, and onto itself because $E_{\eta,w}|_\varPi$ is unipotent.
For the discriminant action let $x'\in\ten^*$ represent $a\in A$.
Then $(\eta,x')\equiv\beta_q(a,d)$, $2(w,x')\equiv\beta_q(a,[w])$ and $w^2\equiv q([w])$ modulo $2$.
The formula gives
$$
E_{\eta,w}(x') = x' + (\eta,x')\,w - \bigl(2(w,x')+w^2(\eta,x')\bigr)\tfrac{\eta}{2} .
$$
The two coefficients are integers, $2w\in\ten$ and $\eta\in\ten$, so modulo $\ten$ only their residues modulo $2$ matter, and $A$ has exponent two.
So $\rho(E_{\eta,w})(a) = T_{d,[w]}(a)$.

(2) Let $c = [w_0]$ with $w_0\in\ten^*$.
Then $\beta_q(c,d) = (w_0,\eta)\bmod 2 = 0$, so $(w_0,\eta)\in2\ZZ = (\ten,\eta)$, and there is $t\in\ten$ with $(t,\eta) = -(w_0,\eta)$.
Then $w = w_0+t$ has $(w,\eta) = 0$ and $[w] = c$.

(3) Put $b = T_{d,c'}(a)$.
Since $\beta_q(c',d) = \beta_q(d,d) = 0$, one has $\beta_q(b,d) = \beta_q(a,d)$ and $\beta_q(b,c) = \beta_q(a,c)+\beta_q(a,d)\beta_q(c,c')$.
Substituting, and using $q(c+c') = q(c)+q(c')+\beta_q(c,c')$, gives $T_{d,c}T_{d,c'} = T_{d,c+c'}$.
$T_{d,0} = \id$, and $T_{d,d}(a) = a+\beta_q(a,d)d+\beta_q(a,d)d = a$.
Conversely, if $T_{d,c} = \id$, choose $a$ with $\beta_q(a,d) = 1$, which exists because $\beta_q$ is nondegenerate; then $c = (\beta_q(a,c)+q(c))d\in\generators{d}$.
By (1) and (2) every $T_{d,c}$ is the image of an isometry of $\ten$, so it lies in $\Orth(A,q)$.
$d^\perp$ has order $2^9$, so $U_d$ has order $2^8$.

(4) For $a\in d^\perp$ the formula reads $T_{d,c}(a) = a+\beta_q(a,c)d$, and $T_{d,c}(d) = d$.
If $D\ni d$, then $D^\perp\subseteq d^\perp$, so $T_{d,c}$ acts trivially on $D^\perp/D$.
For $a\in D$ one has $T_{d,c}(a) = a+\beta_q(a,c)d$, which is $a$ when $c\in D^\perp$.
:::

::: {.lemma #lem:ten-base-stabilizers title="The stabilizers of $\ZZ e$, $\ZZ e'$ and $\generators{e,e'}$"}

With the notation of @prop:ten-plane-classes and @lem:half-vector-eichler, put $d_1 = [e'/2]$ and $F_1 = \Stab_{\Orth(A,q)}(d_1)$.
Then $\abs{F_1} = 89\,181\,388\,800$, and
$$
\rho\bigl(\Stab_{\Orth(\ten)}(\ZZ e)\bigr) = \Orth(A,q),\qquad
\rho\bigl(\Stab_{\Orth(\ten)}(\ZZ e')\bigr) = \rho\bigl(\Stab_{\Orth(\ten)}(\varPi_1)\bigr) = F_1 .
$$
:::

::: {.proof}

*The line $\ZZ e$.* The isometries $\id_U\oplus g$ with $g\in\Orth(\sen)$, $\sen = U(2)\oplus E_8(2)$, fix $e$, and they act on $A = A_{\sen}$ through $g$.
$\sen$ is even, indefinite and $2$-elementary, so $\Orth(\sen)\to\Orth(A,q)$ is surjective (@thm:two-elementary-surjectivity).

*The order of $F_1$.* $A = A_{U(2)}\perp A_{E_8(2)}$ is the group $A^0$ of @lem:coble-discriminant-blocks, and $\Orth(A,q)$ is transitive on its $527$ nonzero isotropic elements (@lem:coble-discriminant-blocks(2)).
So $\abs{F_1} = 2^{21}\cdot3^5\cdot5^2\cdot7\cdot17\cdot31/527 = 89\,181\,388\,800$.

*The line $\ZZ e'$ and the plane $\varPi_1$.*
An isometry that stabilizes $\ZZ e'$ fixes $[\pm e'/2] = d_1$, and an isometry that stabilizes $\varPi_1$ fixes the nonzero element $d_1$ of $D(\varPi_1)$ (@prop:ten-plane-classes(2)).
So both images lie in $F_1$.
Let $S_0\leq\Orth(\ten)$ be the group generated by the isometries $\id_{U\oplus U(2)}\oplus w$ with $w\in\Orth(E_8(2)) = W(E_8)$ and the transvections $E_{e',w}$ of @lem:half-vector-eichler(1).
Each generator fixes $e'$ and stabilizes $\varPi_1$, so $\rho(S_0)$ lies in both images.

Let $L = \rho\bigl(\theset{\id\oplus w \st w\in W(E_8)}\bigr)$.
In the coordinates of @prop:ten-plane-classes, $A_{E_8(2)} = \tfrac12E_8(2)/E_8(2)$ is $E_8/2E_8$, and $\id\oplus w$ acts as the identity on $A_{U(2)}$ and as the reduction $\bar w$ of $w$ on $E_8/2E_8$.
If $\bar w = \id$, then for each $r\in E_8$ with $r\cdot r = 2$ the vector $w(r)-r$ lies in $2E_8$, whose nonzero vectors have norm at least $8$, while $(w(r)-r)\cdot(w(r)-r) = 4-2\,w(r)\cdot r\leq 8$ with equality only for $w(r) = -r$.
So $w(r) = \pm r$ for every such $r$.
If two simple roots $r_i, r_j$ are joined in the Dynkin diagram, then $r_i+r_j$ is a root, and its sign agrees with the signs of $r_i$ and $r_j$; the diagram is connected, so $w = \pm\id$.
Hence $\abs{L}\geq\abs{W(E_8)}/2 = 348\,364\,800$.

The group $U_{d_1}$ of @lem:half-vector-eichler lies in $\rho(S_0)$ by @lem:half-vector-eichler(1) and (2), and it has order $2^8$.
Since $d_1^\perp = \generators{d_1}\perp A_{E_8(2)}$, the quotient $d_1^\perp/\generators{d_1}$ is $A_{E_8(2)}$, on which $\id\oplus w$ acts by $\bar w$ and $U_{d_1}$ acts trivially (@lem:half-vector-eichler(4)).
So $L\cap U_{d_1} = 1$, and $\rho(S_0)\supseteq L\,U_{d_1}$ has at least $348\,364\,800\cdot 2^8 = 89\,181\,388\,800 = \abs{F_1}$ elements.
Hence $\rho(S_0) = F_1$, and both images equal $F_1$.
:::

::: {.lemma #lem:line-stabilizer-image title="The stabilizer of a primitive isotropic line maps onto the stabilizer of its class"}

For a primitive isotropic $v\in\ten$ let $c(\ZZ v) = [v/\operatorname{div}(v)]\in A_{\ten}$; it does not depend on the sign of $v$, because $A_{\ten}$ has exponent two.
Let $\Gamma\leq\Orth(\ten)$ contain $K$, and put $H = \rho(\Gamma)$.
Then
$$
\rho\bigl(\Stab_{\Orth(\ten)}(\ZZ v)\bigr) = \Stab_{\Orth(A,q)}\bigl(c(\ZZ v)\bigr),
\qquad
\rho\bigl(\Stab_{\Gamma}(\ZZ v)\bigr) = \Stab_{H}\bigl(c(\ZZ v)\bigr).
$$
:::

::: {.proof}

For $g\in\Orth(\ten)$ one has $c(g\ZZ v) = \rho(g)\,c(\ZZ v)$, because $g$ preserves divisibility.
By [@Ste91, Prop. 4.5] there is $g\in\Orth(\ten)$ with $g\ZZ v_0 = \ZZ v$ for $v_0 = e$ or $v_0 = e'$.
Conjugation by $g$ carries $\Stab_{\Orth(\ten)}(\ZZ v_0)$ to $\Stab_{\Orth(\ten)}(\ZZ v)$, and conjugation by $\rho(g)$ carries the stabilizer of $c(\ZZ v_0)$ to the stabilizer of $c(\ZZ v)$.
The first equality holds for $v_0$ by @lem:ten-base-stabilizers, because $c(\ZZ e) = 0$ and $c(\ZZ e') = d_1$.

For the second, the inclusion $\subseteq$ is clear.
Let $h\in\Stab_H(c(\ZZ v))$.
By the first equality $h = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\ZZ v)$, and $h = \rho(\gamma)$ with $\gamma\in\Gamma$.
Then $s\gamma^{-1}\in K\subseteq\Gamma$, so $s\in\Stab_\Gamma(\ZZ v)$.
:::

::: {.theorem #thm:sterk-line-fibres title="Primitive isotropic lines up to a discriminant preimage"}

Let $\Gamma\leq\Orth(\ten)$ contain $K$, and put $H = \rho(\Gamma)$.
Two primitive isotropic lines $\ell,\ell'\subseteq\ten$ are $\Gamma$-equivalent if and only if $c(\ell')\in H\,c(\ell)$.
:::

::: {.proof}

If $\ell' = \gamma\ell$ with $\gamma\in\Gamma$, then $c(\ell') = \rho(\gamma)c(\ell)$.
Conversely let $c(\ell') = h\,c(\ell)$ with $h\in H$.
The class $c(\ell)$ is $0$ exactly when $\operatorname{div}(\ell) = 1$, so $\ell$ and $\ell'$ have the same divisibility, and by [@Ste91, Prop. 4.5] there is $g\in\Orth(\ten)$ with $g\ell = \ell'$.
Then $h^{-1}\rho(g)$ fixes $c(\ell)$, so by @lem:line-stabilizer-image $h^{-1}\rho(g) = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\ell)$.
The element $\gamma = gs^{-1}$ carries $\ell$ to $\ell'$ and has $\rho(\gamma) = h$, so $\gamma\in\rho^{-1}(H) = \Gamma$.
:::

::: {.theorem #thm:enriques-integral-plane-stabilizers title="The stabilizers of primitive isotropic planes of $\ten$"}

For every primitive totally isotropic plane $\varPi\subseteq\ten$,
$$
\rho\bigl(\Stab_{\Orth(\ten)}(\varPi)\bigr) = \Stab_{\Orth(A,q)}\bigl(D(\varPi)\bigr).
$$
Let $\Gamma\leq\Orth(\ten)$ contain $K$, put $H = \rho(\Gamma)$ and $\Gamma^+ = \Gamma\cap\Orth^+(\ten)$.
Then:

1. $\rho(\Stab_\Gamma(\varPi)) = \rho(\Stab_{\Gamma^+}(\varPi)) = \Stab_H(D(\varPi))$;
2. two primitive totally isotropic planes $\varPi,\varPi'$ are $\Gamma$-equivalent if and only if $D(\varPi')\in H\,D(\varPi)$.
:::

::: {.proof}

For $g\in\Orth(\ten)$ one has $D(g\varPi) = \rho(g)D(\varPi)$, so, as in the proof of @lem:line-stabilizer-image, it suffices by @prop:ten-plane-classes(1) to prove the first equality for $\varPi_1$ and $\varPi_2$.
For $\varPi_1$ it is @lem:ten-base-stabilizers, since $D(\varPi_1) = \generators{d_1}$.

Let $D = D(\varPi_2) = \theset{0, d_1, d_2, d_1+d_2}$ with $d_1 = [e'/2]$ and $d_2 = [z/2]$, let $F = \Stab_{\Orth(A,q)}(D)$ and $S = \rho(\Stab_{\Orth(\ten)}(\varPi_2))\subseteq F$.

*The order of $F$.* The group $A$ is $A^0$ of @lem:coble-discriminant-blocks, so $A_{T_\Co} = \ZZ k\perp A$, and restriction is an isomorphism $\Orth(q_{A_{T_\Co}})\to\Orth(A,q)$ (@lem:coble-discriminant-blocks(3)).
The isotropic subgroups of order $4$ of $A_{T_\Co}$ lie in $k^\perp = A$ (proof of @prop:coble-planecusp-finite(2)), so they are the isotropic subgroups of order $4$ of $A$.
By @prop:coble-planecusp-finite(4), $\abs F = 1\,981\,808\,640 = 6\cdot 40\,320\cdot 2^{13}$.

Consider the homomorphism $\Phi\colon S\to\GL(D)\times\Orth(D^\perp/D)$.

*The Levi part.* Let $R$ be the set of the following vectors of $\varPi_2^\perp$, in the coordinates of @prop:ten-plane-classes: $r = y$ with $y_0 = \pm e_i\pm e_j$ and $2\leq i<j\leq 8$; and $r = 2ue+y$ with $u = \pm1$ and $y_0 = ue_1\pm e_j$, $2\leq j\leq 8$.
Each $r$ has $r^2 = -4$, $(r,\ten)\subseteq2\ZZ$ and $(r,e') = (r,z) = 0$, so the reflection $s_r(x) = x+\tfrac12(x,r)\,r$ lies in $\Orth(\ten)$ and fixes $\varPi_2$ pointwise.
So $s_r\in\Stab_{\Orth(\ten)}(\varPi_2)$, and $\rho(s_r)$ acts trivially on $D\subseteq\tfrac12\varPi_2/\varPi_2$.
The map $\pi$ of @prop:ten-plane-classes sends $R$ bijectively onto the $112$ roots $\pm e_i\pm e_j$ of $D_8$, and since $(x,r) = -2\,\pi(x)\cdot\pi(r)$, the vector $\pi(s_r x)$ is the Euclidean reflection of $\pi(x)$ in $\pi(r)$.
So the $s_r$ induce $W(D_8)$ on $\varPi_2^\perp/\varPi_2\cong D_8^*(2)$.
The discriminant group of $D_8^*(2)$ is $\tfrac12D_8/D_8^*$, which multiplication by $2$ identifies with $D_8/2D_8^*$; and $2D_8^*$ is the set of integral vectors whose coordinates all have the same parity.
Sign changes act trivially on $D_8/2D_8^*$, since $x-\varepsilon x$ has even coordinates.
The kernel of $S_8\to\Aut(D_8/2D_8^*)$ is normal in $S_8$ and contains neither the transposition $(1\,2)$ nor the $3$-cycle $(1\,2\,3)$, because they move $e_1+e_3$ and $e_1+e_4$, respectively, by $e_2-e_1\notin2D_8^*$; so it is trivial.
Hence the $s_r$ induce a group of order $8! = 40\,320$ on the discriminant group of $\varPi_2^\perp/\varPi_2$.
By @cor:isotropic-reduction-stabilizer(2), the isomorphism $\varphi_{\varPi_2}$ of @thm:isotropic-reduction-discriminant intertwines this action with the action of $\rho(s_r)$ on $D^\perp/D$.
So $\Phi(S)\supseteq 1\times\bar R$ with $\abs{\bar R} = 40\,320$.

*The action on $D$.* By @lem:half-vector-eichler(1), $g_1 = E_{z,f'/2}$ and $g_2 = E_{e',y_s/2}$, with $y_s\in E_8(2)$ corresponding to $s$, lie in $\Stab_{\Orth(\ten)}(\varPi_2)$, and by @lem:half-vector-eichler(4) they act trivially on $D^\perp/D$.
One has $g_1(e') = e'-\tfrac12(f',e')z = e'-z$, and $g_2(z) = z-\tfrac12(y_s,\alpha)e' = z+e'$ because $(y_s,\alpha) = -2\,s\cdot2e_1 = -2$.
So $\rho(g_1)$ fixes $d_2$ and sends $d_1$ to $d_1+d_2$, and $\rho(g_2)$ fixes $d_1$ and sends $d_2$ to $d_1+d_2$; these two transvections generate $\GL(D)\cong\GL_2(\F_2)$.
So $\Phi(S)\supseteq\GL(D)\times 1$, and $\abs{\Phi(S)}\geq 6\cdot40\,320$.

*The kernel of $\Phi$.* For $i = 1,2$ let $U_i = \theset{T_{d_i,c} \st c\in D^\perp}$.
By @lem:half-vector-eichler, with $\eta = e'$ and $\eta = z$, these lie in $\ker\Phi$, and $\abs{U_i} = \abs{D^\perp}/2 = 2^7$.
Let $T_{d_1,c} = T_{d_2,c'}$, and choose $a$ with $\beta_q(a,d_1) = 1$ and $\beta_q(a,d_2) = 0$.
Evaluating both sides at $a$ gives $c+(\beta_q(a,c)+q(c))d_1 = \beta_q(a,c')d_2$, so $c\in D$, and $T_{d_1,c}\in\theset{\id, T_{d_1,d_2}}$.
So $\abs{U_1\cap U_2}\leq2$, the set $U_1U_2$ has at least $2^{13}$ elements, and $\abs{\ker\Phi}\geq2^{13}$.

Hence $\abs S\geq 6\cdot40\,320\cdot2^{13} = \abs F$, and $S = F$.

(1) Let $h\in\Stab_H(D(\varPi))$.
By the first equality $h = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\varPi)$, and $h = \rho(\gamma)$ with $\gamma\in\Gamma$; then $s\gamma^{-1}\in K\subseteq\Gamma$, so $s\in\Stab_\Gamma(\varPi)$.
The proof of @thm:enriques-spinor-orbit-agreement gives $k\in K\setminus\Orth^+(\ten)$ with $k\varPi = \varPi$.
Then $s$ or $sk$ lies in $\Stab_{\Gamma^+}(\varPi)$, and both have image $h$.

(2) If $\varPi' = \gamma\varPi$ with $\gamma\in\Gamma$, then $D(\varPi') = \rho(\gamma)D(\varPi)$.
Conversely let $D(\varPi') = h\,D(\varPi)$ with $h\in H$.
The two subgroups have the same order, so by @prop:ten-plane-classes the planes lie in one $\Orth(\ten)$-class, and $g\varPi = \varPi'$ for some $g\in\Orth(\ten)$.
Then $h^{-1}\rho(g)$ stabilizes $D(\varPi)$, so $h^{-1}\rho(g) = \rho(s)$ with $s\in\Stab_{\Orth(\ten)}(\varPi)$, and $\gamma = gs^{-1}\in\rho^{-1}(H) = \Gamma$ carries $\varPi$ to $\varPi'$.
:::

::: {.theorem #thm:enriques-degree-two-arithmetic title="The cusps of $\fentwo$"}

Let $M = \rho(\gent)$ as in @prop:sterk-group-identification.
Use the four $M$-orbits $A$, $B$, $C$, $D$ of nonzero isotropic elements of $A_{\ten}$ and the five $M$-orbits $AAA$, $ABC$, $ACC$, $ADD$, $CCD$ of isotropic subgroups of order $4$ of @ex:gco-finite-orbits, with $[e'/2]$, $[f'/2]$, $[(e'+f')/2]$ in place of $[u_0/2]$, $[w_0/2]$, $[h/2]$.

1. The primitive isotropic lines of $\ten$ form five $\gent$-orbits, the orbits of the vectors of [@Ste91, Prop. 4.2.3]:

   | type | representative | class $c(\ZZ v)$ | $M$-orbit of the class |
   | :--- | :--- | :--- | :--- |
   | $1$ | $e$ | $0$ | $\theset{0}$ |
   | $2$ | $e'$ | $[e'/2]$ | $B$ |
   | $3$ | $e'+f'+\omega$ | $[(e'+f')/2]+[\omega/2]$ | $D$ |
   | $4$ | $e'+2f'+\alpha$ | $[e'/2]+[\alpha/2]$ | $C$ |
   | $5$ | $z = 2e+2f+\alpha$ | $[\alpha/2]$ | $A$ |

   Here $\alpha$ and $z$ are as in @prop:ten-plane-classes, and $\omega\in E_8(2)$ has $\omega^2 = -4$.
2. The primitive totally isotropic planes of $\ten$ form nine $\gent$-orbits.
   Four contain a vector of divisibility one; for them $D(\varPi) = \generators{c}$ with $c$ in $B$, $D$, $C$ or $A$.
   Five contain no vector of divisibility one; for them $D(\varPi)$ lies in $ABC$, $ACC$, $ADD$, $CCD$ or $AAA$.
3. Label a plane by the types of the primitive isotropic vectors it contains, as in [@Ste91, §4.3.15].
   The labels of the nine orbits of item 2 are, in the order listed there, $\theset{1,2}$, $\theset{1,3}$, $\theset{1,4}$, $\theset{1,5}$ and $\theset{2,4,5}$, $\theset{4,5}$, $\theset{3,5}$, $\theset{3,4}$, $\theset{5,5}$.
   A plane orbit is incident to a line orbit of type $t$ exactly when $t$ occurs in its label.
4. For a plane $\varPi$ with label $\lambda$, the intersection of the image of $\Stab_{\gent}(\varPi)$ in $\GL(\varPi)$ with $\SL(\varPi)$ is $\Gamma^1(2)$ for $\lambda = \theset{1,t}$ [@Ste91, §4.3.16]; it is $\Gamma(2)$ for $\theset{2,4,5}$, $\Gamma^1(2)$ for $\theset{4,5}$, $\theset{3,5}$ and $\theset{3,4}$, and $\SL_2(\ZZ)$ for $\theset{5,5}$ [@Ste91, §4.3.17 and the proof of Prop. 4.7].
5. The orbits of $\gent^+ = \gent\cap\Orth^+(\ten)$ on lines and on planes are the orbits of $\gent$.

So the Baily--Borel compactification of $\fentwo$ has five $0$-dimensional and nine $1$-dimensional boundary components, with the incidence of item 3 [@Ste91, §4.2, §4.4].
:::

::: {.proof}

$\gent = \rho^{-1}(M)$ contains $K$ (@prop:sterk-group-identification).

(1) Each representative is primitive and isotropic: $(e'+f')^2 = 4 = -\omega^2$, $(e'+2f')^2 = 8 = -\alpha^2$, and $z$ is treated in @prop:ten-plane-classes(1).
The last four pair evenly with $\ten$, and each pairs to $2$ with $e$ or $f'$, so they have divisibility two, and their classes are the displayed ones.
The class $[\omega/2]$ has $q = -1\equiv1$, and $[\alpha/2]$ has $q = -2\equiv0$ and is nonzero because $\alpha/2\notin\ten$.
So the five classes lie in the five $M$-orbits $\theset{0}$, $B$, $D$, $C$, $A$, which are all the $M$-orbits of isotropic elements.
By @thm:sterk-line-fibres the $\gent$-orbits of lines correspond to these $M$-orbits.

(2) By @thm:enriques-integral-plane-stabilizers(2), the $\gent$-orbits of planes correspond to the $M$-orbits of the subgroups $D(\varPi)$.
For a plane with a vector of divisibility one, $D(\varPi)$ has order $2$ and is generated by a nonzero isotropic element (@prop:ten-plane-classes(2)).
$\Orth(A,q)$ is transitive on the nonzero isotropic elements (@lem:coble-discriminant-blocks(2)), $\rho$ is surjective and $D(g\varPi_1) = \rho(g)D(\varPi_1)$, so every subgroup $\generators{c}$ with $c$ nonzero isotropic occurs; these form four $M$-orbits.
For a plane without such a vector, $D(\varPi)$ is isotropic of order $4$ (@prop:ten-plane-classes(3)).
$\Orth(A,q)$ is transitive on these subgroups (@prop:coble-planecusp-finite(2) and the identification in the proof of @thm:enriques-integral-plane-stabilizers), so every one occurs, and they form five $M$-orbits.
Subgroups of different orders are not $M$-equivalent, so there are nine orbits.

(3) A primitive $v\in\varPi$ of divisibility one has class $0$ and type $1$, and one of divisibility two has class $[v/2]\in D(\varPi)\setminus0$.
For a plane with a vector of divisibility one, every primitive vector of divisibility two has the class $c$ (@prop:ten-plane-classes(2)), and such vectors exist, for example $e'\in\varPi_1$.
For a plane without one, the classes of the primitive vectors are the three nonzero elements of $D(\varPi)$ (@prop:ten-plane-classes(3)).
By item 1 the type of a vector is read off from the $M$-orbit of its class, which gives the labels.
A $0$-dimensional boundary component lies in the closure of a $1$-dimensional one exactly when the line is $\gent$-equivalent to a line in the plane [@Ste91, §4.4].

(4) The nine labels are pairwise distinct.
The planes of [@Ste91, §4.3.16] are the planes $\ZZ e\oplus\ZZ v$ with $v$ of type $2$, $3$, $4$ or $5$, of labels $\theset{1,t}$, and the planes of [@Ste91, §4.3.17] have the five labels without $1$; the groups are computed there.

(5) This is @thm:enriques-spinor-orbit-agreement, items 1 and 2.
:::

::: {.lemma #lem:spinor-orbit-agreement title="When the orbits of a subgroup and of its spinor-positive half agree"}

Let $L$ be a lattice for which $\Orth^+(L)$ of @def:lattice-spinor-kernels has index two in $\Orth(L)$, let $\Gamma\leq\Orth(L)$ satisfy $\Gamma\not\subseteq\Orth^+(L)$, put $\Gamma^+=\Gamma\intersect\Orth^+(L)$, and let $X$ be a $\Gamma$-set.
Then $\Gamma$ and $\Gamma^+$ have the same orbits on $X$ if and only if $\Stab_\Gamma(x)\not\subseteq\Orth^+(L)$ for every $x\in X$.
:::

::: {.proof}

Since $[\Gamma:\Gamma^+]=2$, the complement $\Gamma\setminus\Gamma^+$ is a coset of $\Gamma^+$, so a product of two elements of $\Gamma\setminus\Gamma^+$ lies in $\Gamma^+$, and a product of one element of each lies in $\Gamma\setminus\Gamma^+$.

Suppose first that $\Stab_\Gamma(x)\subseteq\Orth^+(L)$ for some $x$, and choose $\gamma\in\Gamma\setminus\Gamma^+$.
If $\gamma x=\gamma' x$ with $\gamma'\in\Gamma^+$, then $\gamma'^{-1}\gamma\in\Stab_\Gamma(x)\subseteq\Orth^+(L)$, contradicting $\gamma'^{-1}\gamma\in\Gamma\setminus\Gamma^+$.
Hence $\gamma x$ lies in the $\Gamma$-orbit of $x$ but not in its $\Gamma^+$-orbit, and the orbit sets differ.

Conversely suppose $\Stab_\Gamma(x)\not\subseteq\Orth^+(L)$ for every $x$, and let $y=\gamma x$ with $\gamma\in\Gamma$.
If $\gamma\in\Gamma^+$ then $y\in\Gamma^+x$.
If not, choose $\tau\in\Stab_\Gamma(x)\setminus\Orth^+(L)$; then $\gamma\tau\in\Gamma^+$ and $\gamma\tau x=\gamma x=y$, so again $y\in\Gamma^+x$.
Every $\Gamma$-orbit is therefore a single $\Gamma^+$-orbit.
:::

::: {.theorem #thm:enriques-spinor-orbit-agreement title="Spinor agreement for every polarization family of $\ten$: isotropic lines, isotropic planes and flags"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$ with signature $(2,10)$, let $\rho$ be its quadratic discriminant representation and $\widetilde\Orth(N)=\ker\rho$ its discriminant kernel, and let $\Gamma\leq\Orth(N)$ be a subgroup with $\widetilde\Orth(N)\subseteq\Gamma$.
Every preimage $\rho^{-1}(M)$ with $M\leq\Orth(A_\ten,q_\ten)$ is of this form.
Put $\Gamma^+=\Gamma\intersect\Orth^+(N)$.
Then $\Gamma$ and $\Gamma^+$ have the same orbits on

1. the primitive isotropic lines of $N$;
2. the primitive isotropic planes of $N$;
3. the flags $\ell\subset P$ consisting of a primitive isotropic line contained in a primitive isotropic plane.

For the lines the same holds for primitive isotropic vectors: $-\id_N$ lies in $\ker\rho$ and in $\Orth^+(N)$, being level two because $A_\ten$ is annihilated by $2$ and spinor-positive by @lem:minus-identity-spinor-norm at positive index two, so $-\id_N\in\Gamma\intersect\Gamma^+$ and the two generators of a line lie in one orbit of both groups.
:::

::: {.proof}

*Notation.*
Write $e,f$ for the hyperbolic basis of the summand $U$, $e',f'$ for that of $U(2)$, and $r_1,r_2$ for two orthogonal roots of the summand $E_8(2)$ — the roots corresponding to $e_1-e_2$ and $e_1+e_2$ in the coordinates of @prop:ten-plane-classes, of square $-4$ — with $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
Put
$$
\tau\definedas\id_U\oplus(-\id_{U(2)})\oplus\id_{E_8(2)} ,
$$
the $\tau_0$ of @lem:enriques-level-two-transvections.
By @lem:enriques-level-two-transvections, $\alpha^2=-8$, $z$ is primitive isotropic of divisibility two, and
$$
\sigma_U\definedas-\id_U\oplus\id\oplus\id,\qquad E_1\definedas E_{f,e'},\qquad E_2\definedas E_{f',e},\qquad E_3\definedas E_{f',z}
$$
are integral isometries of $N$ lying in $\ker\rho$; together with $\tau$ they satisfy $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau)=-1$ and $\spinornorm_\bR(E_i)=1$.
In particular $\Gamma$ is not contained in $\Orth^+(N)$, since $\sigma_U\in\ker\rho\subseteq\Gamma$ and $\sigma_U\notin\Orth^+(N)$.

*The objects the two witnesses stabilize.*
$\tau(e)=e$, $\tau(e')=-e'$ and $\tau(z)=z$; so $\tau$ fixes the lines $\ZZ e$, $\ZZ e'$, $\ZZ z$ and stabilizes the two planes
$$
P_1\definedas\generators{e,e'},\qquad P_2\definedas\generators{z,e'}
$$
setwise.
Likewise $\sigma_U(e)=-e$ and $\sigma_U(e')=e'$, so $\sigma_U$ fixes $\ZZ e$ and stabilizes $P_1$.

*Transport.*
$\ker\rho$ is normal in $\Orth(N)$, being the kernel of a homomorphism, and $\spinornorm_\bR(gkg^{-1})=\spinornorm_\bR(g)\spinornorm_\bR(k)\spinornorm_\bR(g)^{-1}=\spinornorm_\bR(k)$.
So for $g\in\Orth(N)$ the conjugate $gkg^{-1}$ of a witness $k$ is again a witness, and it stabilizes the objects $k$ stabilizes, transported by $g$; it lies in $\Gamma$ because $\ker\rho\subseteq\Gamma$.

*The primitive isotropic lines.*
By [@Ste91, 4.5] the primitive isotropic vectors of $L_-\cong\ten$ form exactly two $\Orth$-orbits, represented by $e$ on the vectors of divisibility one and by $e'$ on those of divisibility two, and $-\id_N$ carries $v$ to $-v$; so the same holds for primitive isotropic *lines*.
Let $\ell$ be such a line.
If $\operatorname{div}(\ell)=1$, choose $g\in\Orth(N)$ with $g\ZZ e=\ell$ and put $k\definedas g\sigma_Ug^{-1}$; if $\operatorname{div}(\ell)=2$, choose $g$ with $g\ZZ e'=\ell$ and put $k\definedas g\tau g^{-1}$.
In both cases $k\in\ker\rho\setminus\Orth^+(N)$, $k\ell=\ell$, and $k\in\Gamma$.

*The primitive isotropic planes.*
By @prop:ten-plane-classes(1), $P_1 = \varPi_1$ and $P_2 = \varPi_2$ represent the two $\Orth(N)$-classes of primitive totally isotropic planes.
For a plane $P$ choose $g$ with $gP_1=P$ or with $gP_2=P$, and put $k\definedas g\sigma_Ug^{-1}$ in the first case and $k\definedas g\tau g^{-1}$ in the second; then $k\in\ker\rho\setminus\Orth^+(N)$ and $k$ stabilizes $P$.

*Conclusion.*
The hypotheses of @lem:spinor-orbit-agreement are met: $\Orth^+(\ten)$ has index two in $\Orth(\ten)$, because $\spinornorm_\bR$ is a homomorphism from $\Orth(\ten)$ to $\{\pm1\}$ with kernel $\Orth^+(\ten)$ and it is onto, $\sigma_U$ being an integral isometry of $\ten$ with $\spinornorm_\bR(\sigma_U)=-1$; and at every primitive isotropic line and at every primitive isotropic plane the stabilizer inside $\Gamma$ meets $\Gamma\setminus\Orth^+(\ten)$.
Items 1 and 2 follow on those two sets.
Item 3 is @thm:enriques-flag-witnesses, which produces such a $k$ for every flag, after which the same lemma gives item 3.
:::

::: {.lemma #lem:congruence-two-transitivity title="Level-two transitivity on the three parity classes, and the shear that leaves them"}

Let
$$
A\definedas\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad
B\definedas\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad
\mu\definedas\begin{pmatrix}1&0\\1&1\end{pmatrix},
$$
let $\Gamma(2)\definedas\ker\qty(\SL_2(\bZ)\too\SL_2(\bF_2))$ act on $\bZ^2$ and on $\PP^1(\bZ)$, and let $\Lambda\definedas\generators{A,B,-\id}$.
Then $\Lambda\leq\Gamma(2)$, and for a primitive $(a,c)\in\bZ^2$:

1. there is $\lambda\in\Lambda$ with $\lambda(a,c)$ equal to $\pm(1,0)$ if $a$ is odd and $c$ even, to $\pm(0,1)$ if $a$ is even and $c$ odd, and to $\pm(1,1)$ if $a$ and $c$ are both odd;
2. every element of $\Gamma(2)$ is congruent to the identity modulo $2$ and therefore preserves the class of a vector modulo $2$ and sign, so the $\Gamma(2)$-orbits on $\PP^1(\bZ)$ are exactly the three classes $[1:0]$, $[0:1]$, $[1:1]$, and each of them is a single $\Lambda$-orbit of primitive vectors;
3. $\mu$ is not congruent to the identity modulo $2$; it carries $[1:0]$ to $[1:1]$, and fixes $[0:1]$; and every element of $\generators{\Lambda,\mu}$ preserves the parity of the first coordinate, so that $\generators{\Lambda,\mu}$ has exactly two orbits on $\PP^1(\bZ)$, the primitive lines $[a:c]$ with $a$ odd and those with $a$ even.

:::

::: {.proof}

*The three moves.*
$A^k$ and $B^k$ lie in $\Lambda$ for every $k\in\bZ$ and act by
$$
A^k\colon(a,c)\mapsto(a+2kc,\,c),\qquad
B^k\colon(a,c)\mapsto(a,\,c+2ka),
$$
while $-\id$ acts by $(a,c)\mapsto(-a,-c)$.
All three carry primitive vectors to primitive vectors, because $\gcd(a+2kc,c)=\gcd(a,c)$ and $\gcd(a,c+2ka)=\gcd(a,c)$; and all three preserve the parity type of the pair, that is each of the three alternatives of item 1.

*Odd--odd.*
Let $a$ and $c$ be odd.
Choose $k$ with $\abs{a+2kc}\leq\abs{c}$ and apply $A^k$, or symmetrically choose $k$ with $\abs{c+2ka}\leq\abs{a}$ and apply $B^k$.
Both entries remain odd, so neither can become $0$, and the maximum of the absolute values strictly decreases.
Iterating, we reach a pair on which no move reduces the maximum; such a pair has $\abs a=\abs c$, and primitivity forces $\abs a=\abs c=1$.
So the terminal pair is one of $(1,1)$, $(1,-1)$, $(-1,1)$, $(-1,-1)$.
Of these, $(-1,-1)=-\id(1,1)$ and $(-1,1)=-\id(1,-1)$ are reached from $(1,1)$ and $(1,-1)$ by $-\id$, and $B(1,-1)=(1,-1+2)=(1,1)$; so all four lie in the $\Lambda$-orbit of $(1,1)$, and no sign is left unaccounted for.

*Odd--even.*
Let $a$ be odd and $c$ even.
Reducing the larger absolute value by a multiple of twice the smaller keeps $a$ odd and $c$ even, and strictly decreases the maximum until no move reduces it; then either $\abs a=\abs c$, which the parities forbid, or an entry is $0$, which cannot be $a$.
So $c=0$ and $\abs a=1$ by primitivity, the terminal pair is $\pm(1,0)$, and $-\id$ settles the sign.

*Even--odd.*
Symmetrically, a primitive pair with $a$ even and $c$ odd is carried to $\pm(0,1)$.

*Item 2.*
Every element of $\Gamma(2)$ is congruent to the identity modulo $2$, hence acts trivially on $\bF_2^2$ and preserves the class of every vector; and by item 1 each class is a single $\Lambda$-orbit, with $\Lambda\leq\Gamma(2)$.
So no $\Gamma(2)$-orbit is a union of two classes, and the $\Gamma(2)$-orbits on primitive vectors are exactly the three classes.
Passing to lines changes nothing, since $-\id$ acts trivially on $\PP^1(\bZ)$; and the three classes are distinct because they are distinct modulo $2$.

*Item 3.*
$\mu\equiv\begin{pmatrix}1&0\\1&1\end{pmatrix}\not\equiv\id\pmod 2$, and $\mu(a,c)=(a,\,a+c)$.
For $a$ odd the second coordinate changes parity, so $\mu[1:0]=[1:1]$ and $\mu[1:1]=[1:0]$; for $a$ even $\mu$ fixes the vector $(0,c)$.
Hence $\mu$ preserves the parity of the first coordinate, and so do $A$, $B$ and $-\id$, so every element of $\generators{\Lambda,\mu}$ does.
Within the odd part $\Lambda$ is transitive on $[1:0]$ and on $[1:1]$ by item 2 and $\mu$ exchanges them, and within the even part $\Lambda$ is transitive on $[0:1]$; hence these two sets are exactly the orbits.

:::

::: {.lemma #lem:unipotent-spinor-trivial title="The normalized real spinor norm is trivial on unipotent isometries"}

Let $N$ be a nondegenerate lattice and $g\in\Orth(N_\bR)$ unipotent. Then $\spinornorm_\bR(g)=1$.
:::

::: {.proof}

Put $V\definedas N\otimes_\bZ\bR$; unipotence says that $n\definedas g-\id$ is nilpotent.
Then
$$
\nu\definedas\log g\definedas\sum_{k\geq1}\frac{(-1)^{k+1}}{k}n^k
$$
is a finite sum, hence a nilpotent endomorphism of $V$ with $\exp(\nu)=g$; both statements are the formal identities for a nilpotent endomorphism evaluated in the finite-dimensional commutative algebra $\bR[n]$.

*All real powers of $g$ are isometries.*
Put $g^t\definedas\exp(t\nu)=\sum_{k\geq0}t^k\nu^k/k!$, again a finite sum.
For integral $t$ this is the $t$-th power of $g$ and hence an isometry, so for fixed $x,y\in V$ the function $t\mapsto\beta(g^tx,g^ty)-\beta(x,y)$ is a polynomial in $t$ vanishing on $\bZ$, hence identically zero.
Thus $g^t\in\Orth(V)$ for every real $t$; and $g^sg^t$ and $g^{s+t}$ agree for integral $s,t$, so their difference, again a polynomial in $(s,t)$, vanishes identically.
Hence $t\mapsto g^t$ is a homomorphism $(\bR,+)\to\Orth(V)$ carrying $1$ to $g$.

*Conclusion.*
The composite $\chi\colon t\mapsto\spinornorm_\bR(g^t)$ is a homomorphism from $(\bR,+)$ into $\bR^\times/(\bR^\times)^2$, a group of exponent two, and $t=2\cdot(t/2)$ gives $\chi(t)=\chi(t/2)^2=1$.
Therefore $\spinornorm_\bR(g)=\chi(1)=1$.
:::

::: {.lemma #lem:enriques-level-two-transvections title="The level-two transvections of $\ten$: images, plane actions and spinor signs"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$, with $e,f$ the hyperbolic basis of $U$, $e',f'$ that of $U(2)$, and $r_1,r_2$ two orthogonal roots of the summand $E_8(2)$ — the roots corresponding to $e_1-e_2$ and $e_1+e_2$ in the coordinates of @prop:ten-plane-classes; the summand is negative definite, so its norms lie in $4\bZ$ and its inner products in $2\bZ$.
Put $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
Then $\alpha^2=-8$, the vector $z$ is primitive isotropic of divisibility $2$, and $\beta(x,\alpha)\in2\bZ$ for every $x\in N$.

Write $E_{a,w}$ in the notation of @def:eichler-siegel — $a$ the isotropic vector, $w$ the vector orthogonal to it — so that
$$
E_{a,w}(x)=x+\beta(x,a)w-\beta(x,w)a
$$
when $w$ is isotropic as well, and put
$$
\sigma_U\definedas-\id_U\oplus\id\oplus\id,\qquad
\tau_0\definedas\id\oplus(-\id_{U(2)})\oplus\id,\qquad
E_1\definedas E_{f,e'},\qquad
E_2\definedas E_{f',e},\qquad
E_3\definedas E_{f',z}.
$$
Then:

1. These five are integral isometries of $N$, with the images
$$
\begin{aligned}
E_1&\colon e\mapsto e+e',\quad e'\mapsto e',\quad f\mapsto f,\quad f'\mapsto f'-2f,\\
E_2&\colon e\mapsto e,\quad e'\mapsto e'+2e,\quad f\mapsto f-f',\quad f'\mapsto f',\\
E_3&\colon e\mapsto e-2f',\quad f\mapsto f-2f',\quad e'\mapsto e'+2z,\quad f'\mapsto f',\quad x\mapsto x-\beta(x,\alpha)f',
\end{aligned}
$$
the last line for $x$ in the summand $E_8(2)$, on which $E_1$ and $E_2$ act identically; and the inverses
$$
E_1^{-1}=E_{f,-e'},\qquad E_2^{-1}=E_{f',-e},\qquad E_3^{-1}=E_{f',-z}
$$
are again integral isometries.
2. All five lie in $\widetilde\Orth(N)=\ker\rho$.
3. $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau_0)=-1$, and $\spinornorm_\bR(E_1)=\spinornorm_\bR(E_2)=\spinornorm_\bR(E_3)=1$.
4. $E_1$, $E_1^2$ and $E_2$ stabilize $P_1=\generators{e,e'}$; $E_1$ and $E_3$ stabilize $P_2=\generators{z,e'}$; $\sigma_U$ stabilizes $P_1$; $\tau_0$ stabilizes both. For a primitive $v=ae+ce'$ of $P_1$ the divisibility is $\gcd(a,2c)$, and every primitive vector of $P_2$ has divisibility $2$.

:::

::: {.proof}

*The vector $z$.*
$r_1^2=r_2^2=-4$ and $\beta(r_1,r_2)=0$, so $\alpha^2=-8$.
Since $(2e+2f)^2=4\beta(e,f)+4\beta(f,e)=8$, we get $z^2=8-8=0$.
The pairings of $z$ are $\beta(z,e)=\beta(z,f)=2$, $\beta(z,e')=\beta(z,f')=0$ and $\beta(z,x)=\beta(\alpha,x)\in2\bZ$ for $x$ in the summand $E_8(2)$, whose bilinear form takes its values in $2\bZ$; so $(\ten,z)=2\bZ$.
If $z=my$ with $y\in N$ and $m\geq2$, comparing the $U$-components gives $m\mid2$, so $m=2$ and $\alpha/2\in E_8(2)$; but $\alpha^2/4=-2$ while every norm of that summand lies in $4\bZ$.
Hence $z$ is primitive.
Finally $\beta(x,\alpha)=0$ for $x\in U\perp U(2)$, and $\beta(x,\alpha)\in2\bZ$ for $x\in E_8(2)$.

*Integrality and the images.*
Each of the pairs $(a,w)=(f,e')$, $(f',e)$, $(f',z)$ consists of isotropic vectors with $\beta(a,w)=0$, so @def:eichler-siegel applies with the simplified formula displayed above.
Substituting the basis vectors, using $\beta(e,f)=1$, $\beta(e',f')=2$ and $\beta(e,e')=\beta(e,f')=\beta(e',f)=\beta(f,f')=0$:
$$
E_1\colon e\mapsto e+\beta(e,f)e'=e+e',\quad e'\mapsto e',\quad f\mapsto f,\quad f'\mapsto f'+\beta(f',f)e'-\beta(f',e')f=f'-2f,
$$
$$
E_2\colon e\mapsto e,\quad e'\mapsto e'+2e,\quad f\mapsto f+\beta(f,f')e-\beta(f,e)f'=f-f',\quad f'\mapsto f',
$$
$$
E_3\colon e\mapsto e-\beta(e,z)f'=e-2f',\quad f\mapsto f-2f',\quad e'\mapsto e'+2z,\quad f'\mapsto f',\quad x\mapsto x-\beta(x,\alpha)f'.
$$
Every image is an integral vector, and the basis vectors have integral images, so each $E_i$ is an integral isometry of $N$; the three displayed inverses are integral by the same computation, and $E_{a,w}E_{a,-w}=\id$ because the two shears cancel.
$\sigma_U$ and $\tau_0$ are evidently integral isometries.

*The discriminant kernel, on a full generating set.*
$U$ is unimodular, $E_8$ is unimodular, so
$$
N^\#=U\oplus\tfrac12U(2)\oplus\tfrac12E_8(2),\qquad A_\ten=N^\#/N ,
$$
and $A_\ten$ is generated by the classes of $e'/2$, $f'/2$ and $x/2$ for $x$ in a $\bZ$-basis of $E_8(2)$.
Each $E_i$ preserves $N$ and hence $N^\#$, since an isometry carries $\theset{y\in N_\QQ \st \beta(y,N)\subseteq\bZ}$ to itself; so its action on $A_\ten$ is read off on that generating set:
$$
\begin{array}{c|ccc}
 & e'/2 & f'/2 & x/2\\ \hline
E_1 & e'/2 & f'/2-f & x/2\\
E_2 & e'/2+e & f'/2 & x/2\\
E_3 & e'/2+z & f'/2 & x/2-\tfrac12\beta(x,\alpha)f'
\end{array}
$$
Every entry differs from the class in the left column by an element of $N$: $f$ and $z$ lie in $N$, and $\tfrac12\beta(x,\alpha)\in\bZ$ because the bilinear form of the summand $E_8(2)$ takes its values in $2\bZ$.
So all three act trivially on $A_\ten$, that is, lie in $\ker\rho$.
$\sigma_U$ and $\tau_0$ act by $-\id$ on one summand and identically on the others, and $-\id$ is the identity on a group annihilated by $2$; so they lie in $\ker\rho$ as well.

*Spinor signs.*
For $t\in\bR$ put
$$
\sigma^{(1)}_t(x)=x+t\qty[\beta(x,f)e'-\beta(x,e')f],\quad
\sigma^{(2)}_t(x)=x+t\qty[\beta(x,f')e-\beta(x,e)f'],\quad
\sigma^{(3)}_t(x)=x+t\qty[\beta(x,f')z-\beta(x,z)f'],
$$
each of the form $x\mapsto x+t\qty[\beta(x,a)w-\beta(x,w)a]$ with $a,w$ isotropic and $\beta(a,w)=0$.
The coefficient of $t$ in $\beta(\sigma_tx,\sigma_ty)$ is
$\beta(x,a)\beta(w,y)-\beta(x,w)\beta(a,y)+\beta(y,a)\beta(x,w)-\beta(y,w)\beta(x,a)$, which vanishes by cancellation, and the coefficient of $t^2$ is
$\beta(x,a)\beta(y,a)\beta(w,w)-\beta(x,a)\beta(y,w)\beta(w,a)-\beta(x,w)\beta(y,a)\beta(a,w)+\beta(x,w)\beta(y,w)\beta(a,a)$, which vanishes because $a$ and $w$ are isotropic and orthogonal.
So $\sigma^{(i)}_t\in\Orth(N_\bR)$ for every $t$, and $\sigma^{(i)}_s\sigma^{(i)}_t=\sigma^{(i)}_{s+t}$ because $\sigma^{(i)}_t$ fixes both $a$ and $w$ and preserves the two pairings $\beta(\cdot,a)$, $\beta(\cdot,w)$.
Thus $\sigma^{(i)}_1=E_i$ lies in a one-parameter subgroup of $\Orth(N_\bR)$, and $t\mapsto\spinornorm_\bR(\sigma^{(i)}_t)$ is a homomorphism from $(\bR,+)$ to a group of exponent two, hence trivial; so $\spinornorm_\bR(E_i)=1$, which is also the statement of @lem:unipotent-spinor-trivial.
For the two sign changes, @lem:minus-identity-spinor-norm gives $\spinornorm_\bR(-\id_U)=[(-1)^1]$ and $\spinornorm_\bR(-\id_{U(2)})=[(-1)^1]$, the summands having positive index one, and the spinor norm of an orthogonal sum is the product of the spinor norms of its summands, since a reflection of a summand is the corresponding reflection of the sum; so both have spinor norm $-1$.

*The planes.*
From the displayed images: $E_1(e)=e+e'$ and $E_1(e')=e'$ give $E_1^2(e)=e+2e'$, and $E_2(e')=e'+2e$; all three stabilize $P_1$.
Next $E_1(z)=z+\beta(z,f)e'=z+2e'$ and $E_1(e')=e'$, so $E_1$ stabilizes $P_2$, and $E_3(z)=z$, $E_3(e')=e'+2z$ do the same.
The divisibility of $v=ae+ce'\in P_1$ is read off from $\beta(v,f)=a$, $\beta(v,f')=2c$ and the vanishing of the other pairings, so it is $\gcd(a,2c)$; and for $v=az+be'$ of $P_2$ the values are $\beta(v,e)=\beta(v,f)=2a$, $\beta(v,f')=2b$, $\beta(v,e')=0$ and $\beta(v,x)=a\beta(\alpha,x)\in2\bZ$, so the divisibility is $2$ because $\gcd(a,b)=1$.

:::

::: {.theorem #thm:enriques-flag-witnesses title="Flag stabilizers of $\ten$: every primitive line in either plane class has a spinor-negative level-two stabilizer"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$, and let $\Gamma\leq\Orth(N)$ contain $\ker\rho$.
With $\sigma_U$, $\tau_0$, $E_1$, $E_2$, $E_3$ as in @lem:enriques-level-two-transvections, put
$$
P_1\definedas\generators{e,e'},\qquad P_2\definedas\generators{z,e'},\qquad \theta\definedas E_1\tau_0 .
$$
The two planes represent the two $\Orth(N)$-classes of primitive isotropic planes ([@Ste91, 4.6]), and in the coordinates $[a:c]$ of $\ZZ(ae+ce')$ and of $\ZZ(az+ce')$ the elements act by
$$
\begin{array}{ll}
\sigma_U|_{P_1}\colon[a:c]\mapsto[a:-c],&\qquad \tau_0|_{P_2}\colon[a:c]\mapsto[a:-c],\\[2pt]
E_1|_{P_1}\colon[a:c]\mapsto[a:a+c],&\qquad E_2|_{P_1}\colon[a:c]\mapsto[a+2c:c],\\[2pt]
E_1|_{P_2}\colon[a:c]\mapsto[a:c+2a],&\qquad E_3|_{P_2}\colon[a:c]\mapsto[a+2c:c],
\end{array}
$$
while $E_1^2$ acts on $P_1$ by $[a:c]\mapsto[a:2a+c]$. Then:

1. $\theta$ stabilizes $P_2$, lies in $\ker\rho$, and fixes the *vector* $z+e'$; its spinor norm is $-1$.
2. For every primitive isotropic line $\ell\subset P_1$ there is $k\in\ker\rho\cap\Gamma$ with $\spinornorm_\bR(k)=-1$, $k(P_1)=P_1$ and $k(\ell)=\ell$.
3. For every primitive isotropic line $\ell\subset P_2$ there is such a $k$.
4. For every flag $\ell\subset P$, with $\ell$ a primitive isotropic line in a primitive isotropic plane, there is such a $k$ with $k(\ell)=\ell$ and $k(P)=P$.

:::

::: {.proof}

*The witnesses at the base lines.*
$\sigma_U$ negates $e$ and fixes $e'$, so it fixes $\ZZ e$ and stabilizes $P_1$; $\tau_0$ fixes $e$, negates $e'$ and fixes $z$, so it fixes $\ZZ e'$, $\ZZ z$ and stabilizes both $P_1$ and $P_2$.
For the product, $\tau_0(z+e')=z-e'$ and $E_1(z-e')=(z+2e')-e'=z+e'$, using $E_1(z)=z+2e'$ and $E_1(e')=e'$; so $\theta$ fixes the vector $z+e'$, and both factors stabilizing $P_2$, it stabilizes $P_2$.
By @lem:enriques-level-two-transvections all of these lie in $\ker\rho$, and $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau_0)=-1$ while $\spinornorm_\bR(E_1)=1$, so $\spinornorm_\bR(\theta)=-1$.
A conjugate $gkg^{-1}$ of a witness has $\spinornorm_\bR(gkg^{-1})=\spinornorm_\bR(k)$ and lies in $\ker\rho$, which is normal in $\Orth(N)$.

*The lines of $P_1$.*
The subgroup generated by $E_1$ and $E_2$ stabilizes $P_1$ and acts on it by the shears
$$
E_1\mapsto\mu=\begin{pmatrix}1&0\\1&1\end{pmatrix},\qquad E_1^2\mapsto\mu^2=B=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad E_2\mapsto A=\begin{pmatrix}1&2\\0&1\end{pmatrix},
$$
and $-\id_N\in\ker\rho$ acts by $-I$.
By part 3 of @lem:congruence-two-transitivity the group generated by these matrices is transitive on the primitive lines of $P_1$ with first coordinate odd, and on those with first coordinate even; and those two sets are exactly the two divisibility classes of $P_1$ computed in @lem:enriques-level-two-transvections.
So a primitive line $\ell\subset P_1$ of divisibility one is $g\ZZ e$ for some $g\in\generators{E_1,E_2}$, and $g\sigma_Ug^{-1}$ is a witness for it; a line of divisibility two is $g\ZZ e'$ for some such $g$, and $g\tau_0g^{-1}$ is a witness.

*The lines of $P_2$.*
The subgroup generated by $E_1$ and $E_3$, together with $-\id_N$, stabilizes $P_2$ and acts on it by
$$
E_1\mapsto B=\begin{pmatrix}1&0\\2&1\end{pmatrix},\qquad E_3\mapsto A=\begin{pmatrix}1&2\\0&1\end{pmatrix},\qquad -\id_N\mapsto-I .
$$
By parts 1 and 2 of @lem:congruence-two-transitivity this group preserves the class modulo $2$ of a primitive vector of $P_2$ and is transitive on the primitive vectors of each of the three classes.
The base lines are $\ZZ z$ and $\ZZ e'$, both fixed by $\tau_0$, and $\ZZ(z+e')$, fixed by $\theta$; the three have pairwise distinct classes, since $z\equiv(1,0)$, $e'\equiv(0,1)$ and $z+e'\equiv(1,1)$ modulo $2$.
So every primitive line of $P_2$ is the image of one of these three under an element of the group, and the corresponding conjugate is a witness for it.

*Every flag.*
Let $\ell\subset P$ be a flag.
By [@Ste91, 4.6] there are exactly two $\Orth(N)$-classes of primitive isotropic planes, represented by $P_1$ and $P_2$ (@prop:ten-plane-classes(1)), so there is $g\in\Orth(N)$ with $gP_1=P$ or with $gP_2=P$.
Then $g^{-1}\ell$ is a primitive isotropic line of that representative plane, hence has a witness $k$ by the two paragraphs above, and $gkg^{-1}\in\ker\rho$ has spinor norm $-1$ and fixes $P$ and $\ell$.
Since every witness lies in $\ker\rho\subseteq\Gamma$, the stabilizer inside $\Gamma$ of each of these objects meets $\Gamma\setminus\Orth^+(N)$.

:::

::: {.corollary #cor:enriques-preimage-vs-positive title="The spinor-positive half of a discriminant preimage"}

Let $N = \ten$, let $M\leq\Orth(A_\ten,q_\ten)$ and $\Gamma=\rho^{-1}(M)$, so that $\rho(\Gamma)=M$ by @thm:two-elementary-surjectivity; put $\Gamma^+=\Gamma\intersect\Orth^+(N)$, and let $\tau_0$ be as in @lem:enriques-level-two-transvections.

1. $\Gamma = \Gamma^+\sqcup\Gamma^+\tau_0$, so $\Gamma^+$ has index two in $\Gamma$, and $\rho(\Gamma^+)=\rho(\Gamma)=M$.
2. $\Gamma$ and $\Gamma^+$ have the same orbits on primitive isotropic lines, on primitive isotropic planes and on flags.
   On a $\Gamma$-set $X$ their orbits agree exactly when $\Stab_\Gamma(x)$ meets $\Gamma\setminus\Orth^+(N)$ for every $x\in X$.
:::

::: {.proof}

(1) $\tau_0\in\widetilde\Orth(N)\subseteq\Gamma$ is spinor-negative (@lem:enriques-level-two-transvections), so for $g\in\Gamma$ one has $g\tau_0\in\Gamma$ with $\rho(g\tau_0)=\rho(g)$ and $\spinornorm_\bR(g\tau_0)=-\spinornorm_\bR(g)$.
So exactly one of $g$ and $g\tau_0$ lies in $\Gamma^+$, which gives $\Gamma=\Gamma^+\sqcup\Gamma^+\tau_0$ and $\rho(\Gamma^+)=\rho(\Gamma)$.

(2) The first sentence is @thm:enriques-spinor-orbit-agreement, with @thm:enriques-flag-witnesses for the flags, and the second is @lem:spinor-orbit-agreement.
:::

::: {.lemma #lem:gamma-transport-identity title="The gluing anti-isometry for $\gent$"}

Write $A_{\sen} = A_{U(2)}\oplus A_{E_8(2)}$ and $A_{\ten} = A_U\oplus A_{U(2)}\oplus A_{E_8(2)}$ for the two discriminant groups, summand by summand, with $A_U = 0$ because $U$ is unimodular.
Under the identification of the common summands the two forms agree, $q_{\ten} = q_{\sen}$; both take values in $\ZZ/2\ZZ$, where $-1 = 1$, so $q_{\ten}\circ\gamma = -q_{\sen}$ holds for $\gamma = \id$.
Consequently
$$
\rho_{\ten}(\gent) \;=\; \rho_{\sen}\bigl(\Stab_{\Orth(\sen)}(h)\bigr) \;\leq\; \Orth(A_{\ten}, q_{\ten}),
$$
and that group is generated by the discriminant images of the reflection in $u_0-w_0$ and the eight reflections in the simple roots of $E_8(2)$ — all nine of which are isometries of $\ten$ itself, since $U(2)$ and $E_8(2)$ are summands of $\ten = U\oplus U(2)\oplus E_8(2)$.
Any other admissible anti-isometry gives a preimage conjugate to $\gent$ in $\Orth(\ten)$.

:::

::: {.proof}

The discriminant groups of $U(2)$ and of $E_8(2)$ are the same in the two lattices, because both lattices contain those summands isometrically; $U$ contributes nothing. So the canonical identification is an isometry of quadratic spaces, and $\gamma = \id$ is an anti-isometry because negating a $\ZZ/2\ZZ$-valued form changes nothing.
The generators act on the discriminant through their own summands and trivially on the other, so the images of the nine isometries of $\ten$ are the nine generators of the group in @thm:coble-heegner-finite-orbits' first item and equal the $\gamma$-transport of @prop:gamma-en-two-gluing's image.
Two admissible anti-isometries differ by $\tau\in\Orth(A_{\ten},q_{\ten})$, since both satisfy $q_{\ten}(\gamma x) = -q_{\sen}(x)$; by the surjectivity of the discriminant representation (@thm:two-elementary-surjectivity) $\tau = \rho_{\ten}(s)$ for some isometry $s$ of $\ten$, and then
$$
\rho_{\ten}^{-1}(\tau M\tau^{-1}) = s\,\rho_{\ten}^{-1}(M)\,s^{-1},
$$
so the two preimages are conjugate in $\Orth(\ten)$.

:::
