# Period domain embeddings and normalization {#sec-lattices}

We summarize the lattices that will be relevant to our discussion:

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

which sends the generator $h$ of $\generators{2}$ to $\tilde e+\tilde f\in U$ and is the identity on the $E_{10}(2)$ summand.
Since $\coker \eta$ is torsionfree, $\eta$ is a primitive embedding.
:::

::: {.proof}

The map is well defined and isometric: $h$ has square $2$ and $\tilde e+\tilde f$ has square $2$, since $\tilde e,\tilde f$ are the isotropic basis of $U$ with $\tilde e\cdot\tilde f=1$; and $\eta$ is the identity on $E_{10}(2)$, which is an orthogonal summand of both sides.
So $\eta$ is a morphism of lattices of $\mathbf{Lat}_{\bZ}$, and it is injective because it is injective on each summand.

For primitivity, by @prop:primitive-characterization it suffices that $\coker\eta$ be torsion-free, equivalently that $\eta(T_{\Co})$ be saturated in $T_{\En}$.
Suppose $x\in T_{\En}$ has $mx\in\eta(T_{\Co})$ for some $m\geq1$; the claim is $x\in\eta(T_{\Co})$.

Write $x=x_U+x_{E}$ with $x_U\in U$ and $x_E\in E_{10}(2)$, and $\eta(T_{\Co})=\bZ(\tilde e+\tilde f)\oplus E_{10}(2)$.
From $mx\in\eta(T_{\Co})$, the $E_{10}$ component gives $mx_E\in E_{10}(2)$, so $x_E\in E_{10}(2)$, since $E_{10}(2)$ is a lattice and in particular saturated in itself as a summand.
Then $mx_U\in\bZ(\tilde e+\tilde f)$.
Write $x_U=a\tilde e+b\tilde f$; then $\tilde e+\tilde f$ generates a primitive rank-one sublattice of $U$, because the functional $U\to\bZ$ given by $\tilde e\mapsto1$, $\tilde f\mapsto0$ takes the value $1$ on $\tilde e+\tilde f$.
A vector pairing to $1$ with a primitive vector witnesses that no integral multiple of it can be reached from a non-integral point, so $a=b$, and $x_U=a(\tilde e+\tilde f)\in\bZ(\tilde e+\tilde f)$.
Hence $x\in\eta(T_{\Co})$.

The only fact used about $E_{10}(2)$ is that it is a direct summand, so the same argument shows that adjoining a primitive rank-one summand preserves primitivity; the specific form of $E_{10}(2)$ enters only through that.
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

The diagonal map exhibited is isometric on each summand, and it is embedding of lattices by the same argument as @lem:primitive_embedding_eta: a primitive rank-one summand adjoined to a summand that is saturated on both sides stays primitive, the check being that the quotient is torsion-free summand by summand.

Uniqueness up to $\Orth(\lkt)$ is the input from the source and not derived here: it is the rigidity statement of [@AEGS25] for the embedding chain, quoted at @thm:aegs-rigidity.
What this lemma adds to that is the recognition that the abstract chain of the source is realized by the diagonal map on the two $E_8$ summands, so the chain can be written down in coordinates rather than referred to existentially.
That coordinate form is what the cusp computations need, since they pick explicit isotropic vectors.

The final clause passes to period domains: an embedding of lattices is an isometry of the associated symmetric spaces, and $\fco\embeds\fttz$ is the induced inclusion of period domains, which is how the boundary strata of the two compactifications are compared.
:::


::: {.proof}

By [@AEGS25 Lem. 2.4], it suffices to show uniqueness of $\sen \injects S_{\Co}$, i.e.

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

$\fco$ is the normalization of a closed subvariety of the ambient period quotient $\bD(\ten)/\Gamma_\En$, namely of its Heegner divisor $\mch_{-2}/\Gamma_\En$; not of $\fen$, which is the complement of that divisor (@sec-moduli-construction).
:::

::: {.proof}

Write $\Gamma_\Co\definedas\Orth^+(T_\Co)^*$ and $\Gamma_\En\definedas\Orth^+(T_\En)^*$, and let
$$
f\colon \fco = \bD(T_\Co)/\Gamma_\Co \too \bD(\ten)/\Gamma_\En
$$
be the map induced by the embedding $\eta$ of @lem:primitive_embedding_eta. The target is the ambient period quotient and not the moduli space $\fen = (\bD(\ten)\sm\mch_{-2})/\Gamma_\En$ of @sec-moduli-construction: every period of $T_\Co$ is orthogonal to $k = \tilde e-\tilde f$, a vector of square $-2$, so the image of $f$ lies in the Heegner divisor $\mch_{-2}/\Gamma_\En$ and meets no open complement of it. Conflating the two would make the map land outside its own target. The argument has four steps: a gluing computation that identifies the stabilizer of $T_\Co$, finiteness of the fibres, properness, and generic injectivity.

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

Two features of $A_{T_\Co} = \generators{h/2}\oplus A_{E_{10}(2)}$ are used below.
First, $A_{E_{10}(2)}$ is orthogonal to $h/2$.
Second, $q_{T_\Co}(h/2) = \frac12$, whereas $q_{T_\Co}$ takes values in $\ZZ/2\ZZ$ on $A_{E_{10}(2)}$ because $E_{10}$ is even and unimodular.

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

In particular the containment required by the descent criterion (@rmk:descent-of-an-equivariant-inclusion) holds, with equality, so $f$ is defined.

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

::: {.remark #rmk:normalization-enriques-analogue title="The same statement one level up"}

@thm:normalization is the Coble analogue of [@AEGS25 Lem. 2.8], which asserts that $\fentwo$ is the normalization of a closed subvariety of $\fttz$.
There the stabilizer step is run through $T_\dP$: the isometry group $\Orth(T_\dP)$ is the image of $\theset{g\in\Orth(\lkt)\mid g(T_\dP) = T_\dP,\; g(h) = h}$, because the order-two group $\Orth(q_{S_\dP})$ preserves the class of $\tfrac12 h$ in $A_{S_\dP}\cong A_{U(2)}\cong(\ZZ/2)^2$, and the stabilizer of $T_\En$ in $\Gamma_\dP$ is then $\Gamma_{\En,2}$.
The proof above replaces that detour by the direct gluing computation, which is available here because $T_\Co^{\perp T_\En}\cong\generators{-2}$ is of rank one.
:::

::: {.proposition #prop:gamma-en-two-index title="The index of $\gent$ and the kernel of its discriminant map"}

Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten}, q_{\ten})$ be the discriminant representation, $K=\ker\rho$, and $\gent$ the degree-$2$ group of @prop:gamma-en-two-gluing. Then
$$
[\Gamma_\En : \gent] \;=\; 2^7\cdot 17\cdot 31 \;=\; 67\,456 \;=\; [\Orth(A_{\ten},q_{\ten}) : \rho(\gent)],
$$
and consequently $K\subseteq\gent$: the group $\gent$ is the full preimage in $\Orth(\ten)$ of its discriminant image.

:::

::: {.proof}

The index is the degree of $\fen\to\fttz$ [@AEGS25 Lem. 2.8], printed there as $2^7\cdot 17\cdot 31$ with the reference to [@Ste95a, Rem. 2.12].
The right-hand index is finite and computable: $\abs{\Orth(A_{\ten},q_{\ten})} = 46\,998\,591\,897\,600$ and, by @prop:gamma-en-two-gluing, $\rho(\gent)$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$, which is $\abs{W(E_8)} = 696\,729\,600$ by @prop:polarization-stabilizer-enriques and @thm:coble-heegner-finite-orbits; the quotient is $2^7\cdot17\cdot31$.
For any subgroup the two indices are related by the kernel:
$$
[\Orth(\ten) : \gent] \;=\; [\rho(\Orth(\ten)) : \rho(\gent)]\cdot[K : K\cap \gent],
$$
and $\rho$ is onto $\Orth(A_{\ten},q_{\ten})$ for this lattice (@thm:two-elementary-surjectivity), so the left-hand side equals the right-hand index exactly when $[K:K\cap\gent] = 1$.
Both sides being $67\,456$, that factor is one and $K\subseteq\gent$.

The numerical inputs are computed in `computations/reports/coble_gammaEn2-card.py` and its run, which reports both indices as $67456$ and the order $696\,729\,600$ of the discriminant image of the nine generators.

::: {.proposition #prop:sterk-group-identification title="The group, exactly as @Ste91 defines it"}

With $F$ the image in $\Orth(L^-)$ of $\theset{g\in\Orth L : g\circ I = I\circ g,\; g(h) = h}$ — the degree-$2$ definition of @prop:gamma-en-two-gluing — the published statement is:
1. **Prop. 2.7, [@Ste91], p. 7.** $F$ is exactly the set of integral isometries of $L^-$ whose induced map on $L_-^*/L_-\cong\tfrac12 H(2)/H(2)\cong E_8(-2)/E_8(-2)$ **respects the decomposition into the two summands**; in the notation of `@prop:gamma-en-two-gluing`, that is a condition on the action on $A_{U(2)}\oplus A_{E_8(2)}$.
2. **Remark 2.8, [@Ste91], p. 8.** $F$ is *not* the stabilizer of $\langle e'-f'\rangle+L$: there is a Siegel-Eichler transformation that stabilizes that line and lies in $F$.
This supersedes the earlier identification $\Stab_{\Orth(\ten)}(h)$ on two independent grounds (it has infinite index in $\Orth(\ten)$, and Sterk 2.8 excludes it by name), and it is the statement the preimage construction of coble_gammaEn2-subgroup-orbits.py computes: the discriminant group $M$ is built from the images of the $U(2)$ reflection and the eight reflections in the simple roots of $E_8(2)$, which respect the two summands and have order $|W(E_8)|$.
:::

::: {.remark #rmk:sterk-one-cusp-types title="The published plane types"}

Under the same $F$, the one-dimensional boundary components are the $F$-orbits of primitive isotropic planes, classified by **type**, not by a single finite invariant.
The four cases of [@Ste91] §4.3.16 ($E_8$, $D_8$, $A_7\oplus A_1$, $E_7\oplus A_1$) are built from inequivalent isotropic vectors and give half-plane components with no cusp identification; the five of §4.3.17 are determined by Siegel-Eichler transformations, with $\mathcal F(F)\cap SL(\mathcal F)$ respectively $\Gamma(2)$ for $\{2,4,5\}$, $\Gamma_1(2)$ for $\{4,5\}$, $E_1(2)$ for $\{3,5\}$, $F_1(2)$ for $\{3,4\}$, and $SL_2(\ZZ)$ for $\{5,5\}$ (as printed there).
Total nine one-cusps, the AEGS number.
A plane's type-data is its parabolic diagram together with the primitive isotropic vectors it contains and its group $\mathcal F(F)$; a finite image in $A_{\sen}$ cannot separate the types on its own, and the classification is a statement about stabilizers of lifts rather than about a finite plane stratum.
:::


:::

::: {.lemma #lem:gamma-transport-identity title="The gluing anti-isometry is the identity, and the transport is computed on $\ten$ itself"}

Write $A_{\sen} = A_{U(2)}\oplus A_{E_8(2)}$ and $A_{\ten} = A_U\oplus A_{U(2)}\oplus A_{E_8(2)}$ for the two discriminant groups, summand by summand, with $A_U = 0$ because $U$ is unimodular.
Under the identification of the common summands the two forms agree, $q_{\ten} = q_{\sen}$; both take values in $\ZZ/2\ZZ$, where $-1 = 1$, so $q_{\ten}\circ\gamma = -q_{\sen}$ holds for $\gamma = \id$.
Consequently
$$
\rho_{\ten}(\gent) \;=\; \rho_{\sen}\bigl(\Stab_{\Orth(\sen)}(h)\bigr) \;\leq\; \Orth(A_{\ten}, q_{\ten}),
$$
and that group is generated by the discriminant images of the reflection in $u_0-w_0$ and the eight reflections in the simple roots of $E_8(2)$ — all nine of which are isometries of $\ten$ itself, since $U(2)$ and $E_8(2)$ are summands of $\ten = U\oplus U(2)\oplus E_8(2)$.

:::

::: {.proof}

The discriminant groups of $U(2)$ and of $E_8(2)$ are the same in the two lattices, because both lattices contain those summands isometrically; $U$ contributes nothing. So the canonical identification is an isometry of quadratic spaces, and $\gamma = \id$ is an anti-isometry because negating a $\ZZ/2\ZZ$-valued form changes nothing.
The generators act on the discriminant through their own summands and trivially on the other, so the images of the nine isometries of $\ten$ are the nine generators of the group in @thm:coble-heegner-finite-orbits' first item and equal the $\gamma$-transport of @prop:gamma-en-two-gluing's image.
In particular $\gent = \rho_{\ten}^{-1}(M)$ with $M$ built from isometries of $\ten$, which is what makes the preimage construction of `computations/reports/coble_gammaEn2-subgroup-orbits.py` a construction on $\ten$ and not on the glued lattice.
The number of $\gent$-orbits of primitive isotropic lines, and of planes, is invariant under the choice of admissible $\gamma$, but the invariance is a statement about *integral* orbits and needs a lift: conjugating a finite subgroup of $\Orth(A_{\ten},q_{\ten})$ moves finite orbits, whereas the cusps are orbits on the lattice.
Two admissible anti-isometries differ by $\tau\in\Orth(A_{\ten},q_{\ten})$, since both satisfy $q_{\ten}(\gamma x) = -q_{\sen}(x)$; by the surjectivity of the discriminant representation (@thm:two-elementary-surjectivity) $\tau = \rho_{\ten}(s)$ for some isometry $s$ of $\ten$, and then
$$
\rho_{\ten}^{-1}(\tau M\tau^{-1}) = s\,\rho_{\ten}^{-1}(M)\,s^{-1},
$$
so the two preimages are conjugate in $\Orth(\ten)$ and conjugation by a lattice isometry permutes the primitive isotropic lines and planes.
That lift is the hypothesis the invariance uses, and it is the surjectivity theorem, cited rather than assumed; without it the finite conjugacy says nothing about cusps.

:::

::: {.remark #rmk:gamma-en-two-fibres title="What the index does and does not give for the cusps"}

The $0$-cusps of $\fen$ are the $\gent$-orbits of primitive isotropic $v\in\ten$.
$[\Gamma_\En : \gent]$ being a finite index of an infinite arithmetic group, and equal to the index of $\rho(\gent)$ in the finite orthogonal group, is what lets a discriminant computation say anything here at all; it is not itself a count of orbits, and two further facts are needed.

*Surjectivity of the divisibility map.*
A primitive isotropic $v$ with $\operatorname{div}(v) = 2$ satisfies $v^2 = 0$, so $v/2\in\ten^*$ has $q_{\ten}([v/2]) = 0$ and $[v/2]\neq 0$; and $\operatorname{div}(v)=1$ gives the class $0$.
By [@AEGS25 §3.2] $\Orth(\ten)$ has exactly two orbits on primitive isotropic vectors, $\operatorname{div}=1$ and $\operatorname{div}=2$ — reproduced as a lattice computation by `T_En.cusps(1)`, which returns the two $0$-cusps of $F_{(10,10,0)}$ (record `computations/reports/coble_gammaEn2-cusps-lattice.md`) — and $\Orth(A_{\ten},q_{\ten})$ is transitive on the $527$ nonzero isotropic classes, which `coble_gammaEn2-card-run.txt` reports as one orbit before passing to a subgroup.

The lattice call counts *lines*, and the passage to vectors is a separate step rather than the same statement: a $0$-cusp is a primitive isotropic rank-one subobject $\ZZ v$, not the vector $v$, and $\theset{v,-v}$ are two generators of one line.
The two counts agree because $-\id_{\ten}\in\Orth(\ten)$ sends $v$ to $-v$, so a line's $\Orth(\ten)$-orbit is the image of a single vector orbit and the map $\text{vector orbits}\to\text{line orbits}$ is bijective: it is onto by definition of the action on subobjects, and injective because the two generators of a line lie in one vector orbit.
The same argument makes the class $[v/\operatorname{div}(v)]$ an invariant of the line, since $v$ and $-v$ have the same class in $A_{\ten}$. So the image of the $\operatorname{div}=2$ class is a single $\Orth(q)$-orbit, and it is nonempty: every one of the $527$ classes is $[v/2]$ for some primitive isotropic $v$ with $\operatorname{div}(v)=2$. The divisibility map is therefore surjective onto the classes, and $\gent$-orbits map onto $\rho(\gent)$-orbits.

*What is not proved by equivariance alone, and what is.*
Surjectivity on point sets does not make the map on orbits injective, and the correct criterion is not transitivity of the kernel.
Let $X$ be a $\Gamma_\En$-orbit of primitive isotropic lines, $x\in X$, $H = \Stab_{\Gamma_\En}(x)$, $c = \varphi(x)$ its class, $M_c = \Stab_M(c)$ for $M = \rho(\gent)$, and $\Gamma_c = \Stab_{\Gamma_\En}(c)$, $\gent_c = \rho^{-1}(M_c)$.
The $\gent$-orbits on $X$ are the double cosets $\gent\backslash\Gamma_\En/H$, the orbit of $gx$ has size $[\gent : \gent\cap gHg^{-1}]$, and the $\gent$-orbits lying over one $M$-orbit of classes are the double cosets $\gent_c\backslash\Gamma_c/H$.
There is exactly one of those --- that is, the finite count below is exact on that class --- if and only if
$$
\Gamma_c = \gent_c\cdot H
\quad\Longleftrightarrow\quad
\rho(\Gamma_c) = M_c\cdot\rho(H)
\quad\Longleftrightarrow\quad
\Stab_{\rho(\Gamma_\En)}(c) = M_c\cdot\rho(H),
$$
the middle equality being the image of the first under $\rho$ and the last a rewriting of it; the criterion is stated in $\rho(\Gamma_\En)$, and replacing that group by all of $\Orth(q_{\ten})$ uses the surjectivity of the discriminant representation (@thm:two-elementary-surjectivity), not the definition.
It holds in particular when $\rho(H) = \Stab_{\rho(\Gamma_\En)}(c)$: when the discriminant image of the stabilizer of the chosen line is the *whole* stabilizer of its class in the image group.
Transitivity of the kernel $K = \ker\rho$ on the fibre is **sufficient** for a single $\gent$-orbit there: $K\subseteq\gent_c$ by @prop:gamma-en-two-index, so $K$ transitive gives $\Gamma_c = K\cdot H$, whence $\rho(\Gamma_c) = \rho(H)$, and the criterion holds because $M_c\subseteq\rho(\Gamma_c)$. It is **not necessary**, and the obstruction is exactly the lifting of $M_c$: $\gent_c/K\cong M_c$ acts on the set of $K$-orbits in the fibre, the fibre is one $\gent_c$-orbit exactly when that action is transitive, and $M_c$ may permute several $K$-orbits cyclically. That is why the criterion is stated with $\rho(H)$ and not with $K$, and why $K$-transitivity is a sufficient but not a necessary condition.
What the criterion needs is the image of $\Stab_{\Orth(\ten)}(x)$, which `computations/reports/coble_gammaEn2-cusps-lattice.py` computes from the stabilizer generators that `T_En.cusps(1)` retains, for both lines.
Until that image is known to be the class stabilizer, the finite count $5 = 1+4$ stands as a count of $\rho(\gent)$-orbits on classes and not as the number of $0$-cusps of $\fen$.

**A bounded rank-4 search, as evidence only.**
The enumeration that produced those lines asks a decidable finite question and should be read at exactly its scope. For any lattice $L$ of rank $r$ with basis $B$ of a totally isotropic plane $\varPi$ (a $2\times r$ integer matrix) one has $\varPi^*/\varPi = R^{\mathrm{sat}}/R$ where $R$ is the row space of $BG$ in $\ZZ^r$; and $\varPi$ is primitive in $L$ exactly when that product computed for $B$ alone is $1$.
The script `computations/reports/coble_gammaEn2-plane-strata.py` runs this with $r = 4$, in the rank-$4$ summand $U\oplus U(2)$ **of** $T_\En$ — not in $T_\En$ itself, whose rank is 12, where the basis would be $2\times 12$ and the E_8(2)-components would matter. It then enumerates all primitive totally isotropic **presentations** with entries in $[-3,3]$: bases of planes, not the planes themselves, so the pairwise count double-counts planes with different bases of the same plane and is not a count of planes.
This is hence *bounded evidence in the rank-$4$ summand only*: it exhibits planes of order $2$ ($1040$ presentations), it finds none of order $1$ or $4$ in that box, and it proves nothing about nonexistence — not there, and still less in $T_\En$, where no reduction to the summand has been proved. The plane $\varPi = \langle e,e'\rangle$ displayed above is the genuine order-$2$ exhibit.
**What is open.** Order-$1$ and order-$4$, the reduction from the summand to $T_\En$, the availability of a primitive $w\in\varPi\cap U(2)$ on which a halving argument could rest, and the integrality of the next half each remain unproved. The nine published $1$-cusps are not assessed by this search in either direction, and no sum over the finite strata is asserted here as an arithmetic count.
No conclusion about cusps is drawn from that bounded search: the published nine $1$-cusps remain the source target, and liftability of order-$1$ and order-$4$ stays open rather than being negated.

:::

::: {.remark #rmk:descent-of-an-equivariant-inclusion title="What the stabilizer statement has to supply"}

The stabilizer step of @thm:normalization is one instance of a criterion for descending a map to a pair of quotients, and the criterion has a weak form and a strong one that are worth separating.
Let $f\colon A\injects B$ be an inclusion of sets, with groups $G_A$ and $G_B$ acting on $A$ and on $B$.
A map of orbit sets $\bar f\colon G_A\backslash A\too G_B\backslash B$ is well defined as soon as $f$ carries orbits into orbits: for every $x\in A$ and every $g_A\in G_A$ there must be some $g_B\in G_B$, allowed to depend on both $x$ and $g_A$, with $g_B f(x) = f(g_A x)$.
That is all a set-theoretic descent needs, and it is strictly weaker than an equivariance statement.
The strong form is a uniform assignment, for instance a homomorphism $G_A\too G_B$ with $f\circ g_A = g_B\circ f$ for all $g_A$ at once.
It is not necessary for $\bar f$ to exist, but it is what the geometric statements here use: it makes $f$ equivariant rather than merely orbit-compatible, it is what identifies quotients rather than just producing a map between them, and it is what any comparison of stabilizers or of orbit decompositions has to stand on.
For the case at hand, $A = \bD(T_\Co)$ with $G_A = \Orth^+(T_\Co)^*$ and $B = \bD(T_\En)$ with $G_B = \Orth^+(T_\En)^*$, and what the gluing computation above supplies is the strong form, with equality: restriction of $\Stab_{G_B}(T_\Co)$ to $T_\Co$ is exactly $G_A$, so $g_A\mapsto\id_K\oplus g_A$ is a genuine homomorphism and $f$ is $G_A$-equivariant, not merely orbit-compatible.
It is worth naming what that map is, since the weak form would not have given it: the kernel of restriction is $\{1, s_k\}$, where $s_k$ is the reflection in the $(-2)$-vector $k = \tilde e - \tilde f$ --- it fixes $T_\Co$ pointwise and negates $k$ --- so restriction is two-to-one on the stabilizer and the equivariant assignment is its section, the extension fixing $k$.
Equality of the images does not give injectivity of $\bar f$: two $G_A$-orbits may still be carried into one $G_B$-orbit, and it is the point of $\bD(T_\Co)$ lying on a second translate $\inverseof{g}(T_\Co)$ that the fibre count has to control.
:::
