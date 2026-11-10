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

::: {.definition #def:gamma-co-groups title="The three groups of the Coble lattice, and the divisor at a $(-2)$-vector"}
$T_\Co$ is the lattice $N$ of [@DK13, (3.6)], $N = \generators{2}\oplus E(2)$ with $E(2) = U(2)\oplus E_8(2)$; in the notation of @lem:primitive_embedding_eta it is $\generators{h}\oplus E_{10}(2)$. Let $\delta\definedas\tilde e-\tilde f$, a $(-2)$-vector of $T_\En$ with $\delta^{\perp T_\En} = \eta(T_\Co)$; then $T_\En = (T_\Co\perp\ZZ\delta)_H$ is the overlattice glued along $H = \generators{(h/2,\,\delta/2)}$ (@lem:primitive_embedding_eta, @def:gluing-datum-of-a-pair).

1. $\Gamma^{\mathrm{un}}_\Co\definedas\Orth(T_\Co)$, the group of the unpolarized moduli space: $M_\Co$ is isomorphic to an open subset of $\bD(N)/\Orth(N)$ [@DK13, Prop. 3.2, p. 513]. Write $F^{\mathrm{un}}_\Co\definedas\bD(T_\Co)/\Gamma^{\mathrm{un}}_\Co$.
2. For $\Gamma$ equal to $\Gamma_\En = \Orth(T_\En)$ [@AEGS25, Def. 2.6] or to $\gent = \rho^{-1}(M)$ with $M$ the summand-preserving subgroup of $\Orth(A_{T_\En},q)$ [@AEGS25, Def. 2.6; @Ste91, Prop. 2.7], put
$$
\Gamma^{\Gamma}_\Co\definedas \text{the image of } \Stab_{\Gamma}(\delta) \text{ in } \Orth(\delta^{\perp T_\En}),
\qquad
F^{\Gamma}_\Co\definedas \bD(T_\Co)/\Gamma^{\Gamma}_\Co,
$$
the group and the space of the Coble divisor at $\delta$.
3. $\Gamma_\Co\definedas\Gamma^{\Gamma_\En}_\Co$ with $F_\Co\definedas F^{\Gamma_\En}_\Co$, and $\Gamma_{\Co,2}\definedas\Gamma^{\gent}_\Co$ with $F_{\Co,2}\definedas F^{\gent}_\Co$.

A fourth group occurs throughout: the stable subgroup
$$
\tilde\Orth^+(T_\Co) = \Orth^+(T_\Co)\intersect\ker\bar\rho,
$$
$\bar\rho$ being the discriminant representation and the star $\ker\bigl(\Orth(L)\to\Orth(A_L)\bigr)$ of [@DK13, (2.1)]. It is contained in $\Gamma^{\Gamma}_\Co$ for either $\Gamma$ (@prop:gamma-co-images), and it is strictly smaller than the first: it fixes every class of $A_{T_\Co}$, whereas $\Gamma^{\mathrm{un}}_\Co$ does not.

Which of the four a statement about $\bD(T_\Co)$ uses is named where the statement is made; in particular every count of $0$-cusps names its group.
:::

::: {.proposition #prop:gamma-co-images title="What the two stabilizer images are"}
With $\delta$, $H$ and $\Gamma^{\Gamma}_\Co$ as in @def:gamma-co-groups, and $\bar\rho$ the discriminant representation of $T_\Co$:

1. $\Gamma^{\Gamma_\En}_\Co$ is the stabilizer in $\Orth(T_\Co)$ of the class $[h/2]$ of $A_{T_\Co}$:
$$
\Gamma^{\Gamma_\En}_\Co = \theset{\varphi\in\Orth(T_\Co)\ \mid\ \bar\rho(\varphi)(h/2) = h/2}.
$$
2. $\Gamma^{\gent}_\Co$ is the subgroup of that stabilizer consisting of the $\varphi$ whose image in $\Orth(A_{T_\En}, q_{T_\En})$ preserves the two summands $A_{U(2)}$ and $A_{E_8(2)}$, under the identification $A_{T_\En}\cong A_{E_{10}(2)} = A_{U(2)}\oplus A_{E_8(2)}$ of the proof.
3. The stabilizer in (1) is all of $\Orth(T_\Co)$: the class $[h/2]$ is the characteristic class of $q_{T_\Co}$, so
$$
\Gamma_\Co = \Gamma^{\Gamma_\En}_\Co = \Orth(T_\Co), \qquad [\Orth(T_\Co) : \Gamma_\Co] = 1,
$$
and $\Gamma_{\Co,2}$ is the proper subgroup $\bar\rho^{-1}(P)$ of $\Orth(T_\Co)$, $P$ the stabilizer of the decomposition $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$ of the proof, of index $[\Orth(T_\Co) : \bar\rho^{-1}(P)] = [\Orth(q_{T_\Co}) : P]$.

Neither group is a discriminant kernel: each contains $\ker\bar\rho$, and each is contained in $\Gamma^{\mathrm{un}}_\Co$.
:::

::: {.proof}
By Nikulin's gluing theorem (@thm:nikulin-gluing), $A_{T_\En}\cong H^{\perp}/H$ inside $A_{T_\Co}\oplus A_{\ZZ\delta}$. The subgroup $A_{E_{10}(2)}\subseteq A_{T_\Co}$ is orthogonal to $h/2$, because $T_\Co = \generators{h}\perp E_{10}(2)$ is an orthogonal sum; so $x\mapsto (x,0)$ carries $A_{E_{10}(2)}$ into $H^{\perp}$, and the composite $A_{E_{10}(2)}\to H^{\perp}\to H^{\perp}/H$ is injective with image of order $2^{10}\cdot 2/4 = 2^{10} = \abs{A_{T_\En}}$ (as $(x,0)\in H$ forces $x = 0$). Hence it is an isomorphism, and it carries the summands $A_{U(2)}, A_{E_8(2)}$ of $A_{E_{10}(2)}$ to the summands of the same name in $A_{T_\En} = A_{U(2)}\oplus A_{E_8(2)}$ --- the same two lattices sit in $T_\Co$ and in $T_\En$.

For (1). Let $g\in\Gamma_\En$ stabilize $\delta$. Then $g$ preserves $\delta^{\perp} = \eta(T_\Co)$, so $g = \varphi\oplus\eps$ with $\varphi = \restrictionof{g}{T_\Co}$ and $\eps = \pm1$ on $\ZZ\delta$, and $g$ preserves the overlattice $T_\En$ exactly when $(\bar\rho(\varphi)\oplus\bar\eps)(H) = H$ (@thm:automorphism-lifting-criterion, applied to the gluing datum of @def:gluing-datum-of-a-pair). The automorphism group of $(A_{\ZZ\delta}, q)$ is trivial, $q(\delta/2) = -1/2$ being nonzero, so $\bar\eps = \id$; and the only element of $H$ with second coordinate $\delta/2$ is its generator, so the condition is $\bar\rho(\varphi)(h/2) = h/2$. Conversely, if $\bar\rho(\varphi)(h/2) = h/2$ then $\varphi\oplus\id$ preserves $H$ and extends to an isometry of $T_\En$ by the same criterion, and that isometry stabilizes $\delta$. This proves (1).

For (2). By definition $\gent = \rho^{-1}(M)$, so a $g\in\Orth(T_\En)$ stabilizing $\delta$ lies in $\gent$ exactly when its image in $\Orth(A_{T_\En},q_{T_\En})$ preserves the two summands. Under the isomorphism above, $g$ acts on $A_{T_\En}$ by $[(x,0)]\mapsto[(\bar\rho(\varphi)(x),0)]$, so the two-summand condition is exactly that $\bar\rho(\varphi)$ preserve $A_{U(2)}$ and $A_{E_8(2)}$. The remainders are immediate: $\bar\rho(\varphi) = \id$ implies both conditions, and both conditions are conditions on $\varphi\in\Orth(T_\Co)$.

For (3). Two facts about $A = A_{T_\Co}$ are used. First, $x\mapsto q(x)\bmod 1$ is a homomorphism $A\to\frac12\ZZ/\ZZ\cong\ZZ/2$: for $u,v\in A$ one has $q(u+v)-q(u)-q(v) = 2b(u,v)$, and $2b(u,v)\in\ZZ$ because $A$ is $2$-elementary and $b$ takes values in $\frac12\ZZ$ on it ([@Nik80, §1.3] for the structure of a $2$-elementary discriminant form). Second, $b$ is nondegenerate on $A$, so a class $w$ with $b(w,x)\equiv q(x)\pmod 1$ for all $x$ is unique.

The class $[h/2]$ is such a $w$. Write $A = \generators{h/2}\oplus A_{U(2)}\oplus A_{E_8(2)}$, an orthogonal decomposition because $T_\Co = \generators{h}\perp E_{10}(2)$. On it $q\equiv0\pmod1$ vanishes on the last two summands --- on $A_{E_8(2)}$ because $q(y/2) = y^2/2\in\ZZ$ for $y\in E_8$ --- while $q(h/2) = h^2/4 = 1/2$; and $b(h/2,\cdot)$ vanishes on the same two summands while $b(h/2,h/2) = 1/2$. By additivity of $q\bmod1$ the two agree on all of $A$, that is $b(h/2,x)\equiv q(x)\pmod1$.

Hence every isometry $\sigma$ of $(A,q)$ fixes $[h/2]$: for every $x$,
$$
b(\sigma(h/2),x) = b(h/2,\sigma^{-1}x)\equiv q(\sigma^{-1}x) = q(x)\equiv b(h/2,x)\pmod 1,
$$
and nondegeneracy of $b$ gives $\sigma(h/2) = h/2$. By (1) the stabilizer of $[h/2]$ is $\Gamma_\Co$, so $\Gamma_\Co = \Orth(T_\Co)$ and the index is $1$.

For the last claim, every $\sigma\in\Orth(q_{T_\Co})$ fixes $w = [h/2]$, hence preserves $w^{\perp}$, of dimension $10$; so $\Orth(q_{T_\Co})\to\Orth(w^{\perp},q|_{w^{\perp}})$ is defined, and it is injective because an isometry fixing $w^{\perp}$ pointwise and $w$ is the identity ($x\mapsto x+f(x)w$ with $f(x) = 1$ changes $q(x)$ by $q(w) = 1/2$). $P$ is the stabilizer in that group of the decomposition $w^{\perp} = A_{U(2)}\oplus A_{E_8(2)}$, and since $\bar\rho$ is onto, the index of $\Gamma_{\Co,2}$ in $\Orth(T_\Co)$ is the index of $P$. The proof does not evaluate that index; it is the number of decompositions of $w^{\perp}$ into a $2$-dimensional summand isometric to $A_{U(2)}$ and an $8$-dimensional one isometric to $A_{E_8(2)}$.
:::

::: {.remark #rmk:gamma-co-counts title="The cusp counts name their group"}
By @prop:gamma-co-images(3) the group of the Coble divisor is the whole group of the moduli space: $\Gamma_\Co = \Gamma^{\mathrm{un}}_\Co = \Orth(T_\Co)$, so $\fco$ and $F^{\mathrm{un}}_\Co$ are one quotient, $\bD(T_\Co)/\Orth(T_\Co)$, which [@DK13, Prop. 3.2] identifies with the moduli space of Coble surfaces up to an open subset. In particular $\fco$ has one $0$-cusp, $\Orth^+(T_\Co)$ being transitive on the primitive isotropic vectors (@thm:unpolarized-cusps), computed by sage-extensions#286 in its $\Orth(T_\Co)$ row, and one $1$-cusp, by @thm:plane-transitivity-tco, certified by the same operation.

That is also what the sources force: [@DK13, Prop. 3.2] gives the moduli space as a quotient by $\Orth(N)$, and the sentence after it states that the quotient of the $(-2)$-Heegner divisor by $\Orth(U\oplus E(2))$ is birational to that moduli space; by @thm:normalization that second quotient is $\bD(T_\Co)/\Gamma_\Co$, so the two agree only if $[\Orth(T_\Co) : \Gamma_\Co] = 1$, which is @prop:gamma-co-images(3).

What remains a proper subgroup is $\Gamma_{\Co,2}$, the group of $F_{\Co,2}$: it is $\bar\rho^{-1}(P)$ of @prop:gamma-co-images(3), of index $[\Orth(q_{T_\Co}) : P]$, and the number of its orbits on the primitive isotropic vectors --- the $0$-cusp count of $F_{\Co,2}$ --- is not computed here. The $527$ recorded in this volume is the count for the stable subgroup $\widetilde\Orth^+(T_\Co)$, and the one orbit recorded for $\Orth(T_\Co)$ is the count for $\fco$.
:::

::: {.theorem #thm:normalization}

Let $\Gamma$ be $\Gamma_\En = \Orth(T_\En)$ or $\gent$, and let $\Gamma^{\Gamma}_\Co$ and $F^{\Gamma}_\Co$ be the group and the space of @def:gamma-co-groups, identified in @prop:gamma-co-images. Then the map induced by the embedding $\eta$ of @lem:primitive_embedding_eta,
$$
f^{\Gamma}\colon F^{\Gamma}_\Co = \bD(T_\Co)/\Gamma^{\Gamma}_\Co \too \bD(\ten)/\Gamma,
$$
is defined and finite, its image is the Heegner divisor $\mch_{-2}/\Gamma$ and not the complement $\fen$ of @sec-moduli-construction, and $f^{\Gamma}$ is birational; hence $F^{\Gamma}_\Co$ is the normalization of that divisor.
:::

::: {.proof}

That $f^{\Gamma}$ is defined is @prop:gamma-co-images: restriction carries $\Stab_{\Gamma}(\delta)$ onto $\Gamma^{\Gamma}_\Co$, so the containment required by the descent criterion (@rmk:descent-of-an-equivariant-inclusion) holds, with equality. The target is the ambient period quotient and not the moduli space $\fen = (\bD(\ten)\sm\mch_{-2})/\Gamma$ of @sec-moduli-construction: every period of $T_\Co$ is orthogonal to $\delta = \tilde e-\tilde f$, a vector of square $-2$, so the image of $f^{\Gamma}$ lies in the Heegner divisor $\mch_{-2}/\Gamma$ and meets no open complement of it. Conflating the two would make the map land outside its own target. Nothing below uses more about $\Gamma^{\Gamma}_\Co$ than that it is this image, so the argument runs for either $\Gamma$. It has three steps: finiteness of the fibres, properness, and generic injectivity.

Fibres.
For $x = [\omega]\in\bD(T_\En)$ let $T(x)$ be the smallest primitive sublattice of $T_\En$ whose complexification contains $\omega$, namely $T(x)\definedas\bigl(T_\En\intersect\omega^{\perp_{T_\En\tensor_\ZZ\CC}}\bigr)^{\perp T_\En}$.
For a primitive sublattice $M\leq T_\En$ of signature $(2,\ast)$ one has $x\in\bD(M)$ if and only if $T(x)\iscontainedin M$.

Fix $y\in\bD(\ten)/\Gamma$ and a lift $\tilde y\in\bD(T_\En)$.
A point of $\inverseof{f^{\Gamma}}(y)$ is a $\Gamma^{\Gamma}_\Co$-orbit of a point $x = g\tilde y$ with $g\in\Gamma$ and $x\in\bD(T_\Co)$.
Writing $M'\definedas \inverseof{g}(T_\Co)$, that last condition says $T(\tilde y)\iscontainedin M'$.
Now $M'^{\perp T_\En} = \inverseof{g}(\ZZ\delta) = \ZZ v$ with $v^2 = -2$, and $v\perp T(\tilde y)$.
The space $T(\tilde y)\tensor_\ZZ\RR$ contains a positive definite plane and $T_\En$ has signature $(2,10)$, so $T(\tilde y)^{\perp T_\En}$ is negative definite and contains only finitely many vectors of square $-2$.
Each such $v$ determines $M' = v^{\perp T_\En}$, so only finitely many $M'$ occur.
For a fixed $M'$ the elements $g$ with $\inverseof{g}(T_\Co) = M'$ form one coset of $\Stab_{\Gamma}(\delta)$, whose restrictions to $T_\Co$ all lie in $\Gamma^{\Gamma}_\Co$ by @prop:gamma-co-images; the corresponding points $x$ therefore form a single $\Gamma^{\Gamma}_\Co$-orbit.
Hence $\inverseof{f^{\Gamma}}(y)$ is finite, of cardinality at most half the number of $(-2)$-vectors of $T(\tilde y)^{\perp T_\En}$.

Properness and finiteness.
By @lem:locally_closed_embedding_BB, the map $f^{\Gamma}$ extends to a morphism $\bar f^{\Gamma}\colon\overline{F^{\Gamma}_\Co}^{\operatorname{BB}}\to \overline{\bD(\ten)/\Gamma}^{\operatorname{BB}}$ of projective varieties, which is therefore proper.
A boundary component of $\overline{F^{\Gamma}_\Co}^{\operatorname{BB}}$ is indexed by a primitive isotropic sublattice $I\leq T_\Co$ of rank $1$ or $2$, and the saturation of $I$ in $T_\En$ is again primitive isotropic of the same rank.
So $\bar f^{\Gamma}$ carries boundary to boundary, giving $\inverseof{\bar f^{\Gamma}}(\bD(\ten)/\Gamma) = F^{\Gamma}_\Co$, and $f^{\Gamma}$ is proper because properness is stable under base change.
A proper morphism with finite fibres is finite ([@stacks-02LS]), so $f^{\Gamma}$ is finite.
Let $Z\definedas f^{\Gamma}(F^{\Gamma}_\Co)$, which is closed because a finite morphism is closed.

Generic injectivity.
A proper primitive sublattice $S\subsetneq T_\Co$ of signature $(2,\ast)$ cuts out a proper closed analytic subset $\bD(S)\subsetneq\bD(T_\Co)$, and there are countably many such $S$.
So the set of $x\in\bD(T_\Co)$ with $T(x) = T_\Co$ is the complement of countably many proper closed analytic subsets, hence dense.
For such an $x$ the fibre computation allows only $M' = T_\Co$: one has $T_\Co = T(x)\iscontainedin M'$ with both primitive of rank $11$.
The fibre through $x$ is therefore a single point.
The locus where a finite morphism of irreducible varieties has more than its generic number of preimages is a proper closed subset, and a dense set is not contained in one, so $f^{\Gamma}$ has degree $1$ and is birational.

Finally $F^{\Gamma}_\Co$ is normal, being the quotient of a bounded symmetric domain by a properly discontinuous group of automorphisms.
A finite birational morphism from a normal variety onto a reduced irreducible variety is its normalization, so $F^{\Gamma}_\Co$ is the normalization of $Z$.
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

The index is the degree of the forgetful map $\fen\to F_{(10,10,0)}$ [@AEGS25 Lem. 2.8], printed there as $2^7\cdot 17\cdot 31$ with the reference to [@Ste95a, Rem. 2.12].
The right-hand index is finite and computable: $\abs{\Orth(A_{\ten},q_{\ten})} = 46\,998\,591\,897\,600$ and, by @prop:gamma-en-two-gluing, $\rho(\gent)$ is the $\gamma$-transport of the image of $\Stab_{\Orth(\sen)}(h)$, which is $\abs{W(E_8)} = 696\,729\,600$ by @prop:polarization-stabilizer-enriques and @thm:coble-heegner-finite-orbits; the quotient is $2^7\cdot17\cdot31$.
For any subgroup the two indices are related by the kernel:
$$
[\Orth(\ten) : \gent] \;=\; [\rho(\Orth(\ten)) : \rho(\gent)]\cdot[K : K\cap \gent],
$$
and $\rho$ is onto $\Orth(A_{\ten},q_{\ten})$ for this lattice (@thm:two-elementary-surjectivity), so the left-hand side equals the right-hand index exactly when $[K:K\cap\gent] = 1$.
Both sides being $67\,456$, that factor is one and $K\subseteq\gent$.

The numerical inputs are computed in `computations/reports/coble_gammaEn2-card.py` and its run, which reports both indices as $67456$ and the order $696\,729\,600$ of the discriminant image of the nine generators.
:::

::: {.proposition #prop:sterk-group-identification title="The group, exactly as @Ste91 defines it"}

With $F$ the image in $\Orth(L^-)$ of $\theset{g\in\Orth L : g\circ I = I\circ g,\; g(h) = h}$, where $h = e+f$ — AEGS Def. 2.6's $\gent$ — the following are read directly from the published text, not from a substitute.
1. **[@Ste91], Prop. 2.7, p. 7.** $F$ is exactly the set of integral isometries of $L^-$ whose induced map on the discriminant described there, $L_-^*/L_-\cong\tfrac12 H(2)/H(2)\ \oplus\ \tfrac12 E_8(-2)/E_8(-2)$, **respects the decomposition into the two summands**. Its proof lifts isometries through the invariant lattice and the polarization stabilizer and uses the displayed $(e+f)^\perp = \ZZ(e-f)\oplus E_8(-2)\cong A_1(-2)\oplus E_8(-2)$.
2. **[@Ste91], Remark 2.8, p. 7.** $F$ is *not* the stabilizer of the **finite discriminant element** $\tfrac12(e'-f') + L_-$: the exhibited transformation has $\psi\notin\Gamma$ although $\psi$ stabilizes that element.
So Remark 2.8 excludes $\Stab_{\Orth(q_\ten)}([h/2])$ as the group to count with, because that group is exactly the discriminant-element stabilizer that contains elements outside $F$. So Remark 2.8 does **not** invalidate the integral gluing construction — that construction is exactly what Prop. 2.7 gives, via the discriminant decomposition-respecting description below and the image/preimage of the polarization stabilizer on $L^+$.
What is excluded is the specific assertion $\gent = \Stab_{\Orth(\ten)}(h)$: that is not even a polarization stabilizer in the source's terms, because $h = e+f\in U(2) = \Delta(U)\subseteq L^+$ is in the *invariant* lattice, while $F\subseteq\Orth(L^-)$, and the stabilizer of $h$ on $L^-$ is not the construction.
The invalid version is rejected by the infinite-index argument (such a stabilizer on the rank-12 lattice cannot have index $2^7\cdot17\cdot31$), and the gluing route, integral invariant-lattice stabilizer and its discriminant image, stands.

In the same source $L^+\oplus L^-\subsetneq L$ with $[L : L^+\oplus L^-] = 2^{10}$, not $L = L^+\oplus L^-$.
:::


::: {.proposition #prop:sterk-e8-computed-example title="One published type computed: the $E_8$ plane"}

With $e$ a basis of the unscaled $U$ summand of $\ten$ and $f'$ a basis of the $U(2)$ summand, put $E = \ZZ e\oplus\ZZ f'$.
This is Sterk's first case in [@Ste91, §4.3.16].

*(i) Normalizer.* Write $g(e) = ae + cf'$ and $g(f') = be + df'$ in the basis of $E$; then $(e,\ten) = \ZZ$ while $(f',\ten) = 2\ZZ$ force $a$ odd and $b$ even: $\rho(g)$ preserves the two divisibility ideals separately, so no whole row is odd or even. By [@Ste91, §4.3.16], $\Gamma(E)\cap SL(E)$ is $\Gamma^1(2)$, not one of the OCR's group names.
*(ii) Primitivity.* $E$ is a *primitive totally isotropic plane*: both generators are isotropic, $(e,f')=0$.
*(iii) Quotient.* $E^* = \ZZ e\oplus \ZZ(f'/2)$, because $(f'/2,e') = 1$ belongs to $\ZZ$ while $(e/2,f) = \tfrac12\notin\ZZ$. So $E^*/E\cong \ZZ/2$, and the discriminant image is the one-dimensional subgroup generated by $[f'/2]$.
*(iv) Complement.* $E^{\perp}/E$ is the full $E_8(2)$-summand, since a vector in the $U\oplus U(2)$-part is orthogonal to both $e$ and $f'$ exactly when it's in $E$; the negative-definite complement has the published root label $E_8$.
*(v) Finite image.* the datum is indeed of order $2$ in the Smith-normal-form computation of `coble_gammaEn2-plane-strata.py` (basis $B$ gives $BG$ with elementary divisors $1,2$ and primitivity index $1$), so this type is an order-$2$ plane class and lives in the dimension-one stratum, with discriminant class $[f'/2]$.
This is a full computed example in the full rank-12 lattice — not a classification of all nine types. The five stabilizers of §4.3.17 and the interlacing of the remaining four types are not derived here.
:::

::: {.proposition #prop:sterk-nine-planes title="All nine published one-cusp types, computed in $T_\En$"}
Script `computations/reports/coble_gammaEn2-planes-published.py`, transcript
`coble_gammaEn2-planes-published-run.txt`: the lattice is certified before any invariant is
computed ($\det\Cartan(E_8) = 1$, the E8(2) summand has exactly 240 vectors of square $-4$ through
the owned `vectors_of_square`), and every shell count below is an exact owned enumeration.

**(i) The four §4.3.16 planes.** With $e$ a type-1 vector and $v$ of Sterk 4.2.3 type $2, 3, 4, 5$
respectively, the planes $\langle e, v\rangle$ (labelled $A_7\oplus A_1$, $E_7\oplus A_1$, $D_8$,
$E_8$ by 4.3.15–4.3.16) are all primitive, all have $\abs{\Pi^*/\Pi} = 2$, and all have
$\Pi^{\perp}/\Pi$ of determinant 256 with exactly **240** roots of square $-4$ and none of square
$-2$ — the statement of [@Ste91, §4.3.5] that the four types are *not* distinguished by
$\Pi^{\perp}/\Pi$. The isomorphism with $E_8(-2)$ is exact and does not rest on the shell counts:
for $\Pi = \langle e, e_1\rangle$ the quotient *is* the $E_8(2)$-summand by construction, and
[@Ste91, Prop. 4.6] identifies the other three with it — its hypothesis, proved there from the
single $\Orth(H(2)\oplus E_8(-2))$-orbit of primitive isotropic vectors in that lattice, is that
every primitive isotropic plane containing a divisibility-one vector is $\Orth(L_-)$-equivalent
to $\ZZ e\oplus\ZZ e'$, and an $\Orth(L_-)$-equivalence of planes induces an isometry of the
quotients $\Pi^{\perp}/\Pi$. The shell counts (240 roots of square $-4$, none of square $-2$,
determinant 256) are recorded as checks on this. Their discriminant images have order 2, with orbit-type $(2,), (3,), (4,), (5,)$
respectively — the four vector types of Prop. 4.2.3 sit in four distinct M-orbits of sizes
$2, 120, 270, 135$.

**(ii) The five §4.3.17 planes.** Their labels $\{2,4,5\}, \{4,5\}, \{3,5\}, \{3,4\}, \{5,5\}$ are
exactly the orbit-type sets of the three nonzero classes in their order-4 discriminant image
$\langle[v/2],[w/2]\rangle$, and all five are primitive with $\abs{\Pi^*/\Pi} = 4$ and
$\Pi^{\perp}/\Pi$ of determinant 64 with **368** roots of square $-4$ and **16** of square $-2$.
No isomorphism between these quotients is inferred from the shared invariants: it follows from
[@Ste91, Prop. 4.6], which leaves exactly two $\Orth(L_-)$-classes of primitive isotropic planes —
these five contain no type-1 vector, lie in the second class, and an $\Orth(L_-)$-equivalence of
planes induces an isometry of the quotients $\Pi^{\perp}/\Pi$. The isomorphism *type* of that
second class is fixed by these invariants and named by no classification theorem here.
:::

::: {.lemma #lem:line-stabilizer-image title="The stabilizer of a primitive isotropic line maps onto the stabilizer of its class"}
Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten},q_{\ten})$ be the discriminant representation with
$K = \ker\rho$, and let $\varphi(\ZZ v) = [v/\operatorname{div}(v)]$ be the class of a primitive
isotropic line. Assume (H1) $K\subseteq\gent$ and (H2) $\rho$ surjective. Then
$$ \rho\bigl(\Stab_{\Orth(\ten)}(\ZZ v)\bigr) \;=\; \Stab_{\Orth(A_{\ten},q_{\ten})}\bigl(\varphi(\ZZ v)\bigr),
\qquad
\rho\bigl(\Stab_{\gent}(\ZZ v)\bigr) \;=\; M_{\varphi(\ZZ v)} \definedas \Stab_M\bigl(\varphi(\ZZ v)\bigr). $$
:::

::: {.proof}
The containments "$\subseteq$" are clear: stabilizing $\ZZ v$ stabilizes its class, and
$\rho(\gent) = M$. For "$\supseteq$" of the first, let $h$ stabilize $c\definedas\varphi(\ZZ v)$
and, by (H2), write $h = \rho(g)$ with $g\in\Orth(\ten)$. Then $g(v)$ and $v$ are primitive
isotropic of the same divisibility (an isometry preserves $(v,\ten)$), and
$\varphi(g(\ZZ v)) = \rho(g)(c) = h(c) = c$. Put $p\definedas\operatorname{div}(v)$; an
isometry preserves the divisibility, so $\operatorname{div}(g(v)) = p$, both $g(v)/p$ and
$v/p$ lie in $\ten^*$, and the equality of classes reads $[g(v)/p] = [v/p]$ in
$\ten^*/\ten$. The class map is a homomorphism whose zero class is $\ten$ itself, so this says
exactly $g(v) - v \in p\,\ten$ — the congruence modulo $pN$ required by [@Ste91, Cor. 3.3] at
$p = \operatorname{div}(v)$, vacuous for $p = 1$ and the divisibility-two congruence for
$p = 2$ — whose own structural hypothesis
holds for this lattice because $\ten = (U\oplus U(2))\oplus E_8(2)$ is of the form $N = A\oplus P$
with $A = H\oplus H(2)$ and $P = E_8(2)$ even and nondegenerate. Corollary 3.3 supplies
$k\in\Orth'(\ten)$ with $k(g(v)) = \pm v$; then $k\circ g$ stabilizes $\ZZ v$ and
$\rho(k\circ g) = h$, because $\Orth'(\ten) = K = \ker\rho$. For the second statement, let
$h\in M_c$; the first part gives $g\in\Stab_{\Orth(\ten)}(\ZZ v)$ with $\rho(g) = h$, and
$h\in M = \rho(\gent)$ gives $g_2\in\gent$ with $\rho(g_2) = h$; then
$gg_2^{-1}\in K\subseteq\gent$ by (H1), so $g = (gg_2^{-1})g_2\in\gent$ lies in
$\Stab_{\gent}(\ZZ v)$ with image $h$.
:::

::: {.theorem #thm:sterk-line-fibres title="The arithmetic fibres of the $0$-cusps: the group identified, then the promotion"}
Let $\rho\colon\Orth(\ten)\to\Orth(A_{\ten},q_{\ten})$ be the discriminant representation,
$K = \ker\rho$, and $\gent$ the degree-$2$ group of @prop:gamma-en-two-gluing with
$\rho(\gent) = M$. Assume:

- **(H1)** $K\subseteq\gent$ — @prop:gamma-en-two-index;
- **(H2)** $\rho$ is surjective onto $\Orth(A_{\ten},q_{\ten})$ — @thm:two-elementary-surjectivity.

**The group identification.** Under the identification $\ten\cong L_-$, $\gent$ *is* Sterk's $F$.
By [@Ste91, Prop. 2.7 and Rem. 2.12], $F$ is the full preimage
$\rho^{-1}(F_q)$ of the subgroup $F_q\leq\Orth(L^*_-/L_-,q)$ preserving the two summands, because
$\Orth'(L_-) = K\subseteq F$ and $[\Orth(L_-):F] = [\Orth(q):F_q]$. The group $M$ preserves the
same decomposition (its nine generators act on the separate summands) and has order
$696\,729\,600 = \abs{\Orth(q)}/(2^7\cdot 17\cdot 31) = \abs{F_q}$, so $M = F_q$ and
$\gent = \rho^{-1}(M) = \rho^{-1}(F_q) = F$.

**The fibre argument.** Define $\varphi$ on primitive isotropic lines by
$\varphi(\ZZ v) \definedas [v/\operatorname{div}(v)]$ with $\operatorname{div}(v) = \gcd(v,\ten)$;
this is well defined, since the only other generator of the line is $-v$, which has the same
divisibility and the negated class, and the negated class *equals* the class because
$A_{\ten}$ has exponent two for this lattice: $A_{\ten}\cong A_{U(2)}\oplus A_{E_8(2)}\cong(\ZZ/2)^2\oplus(\ZZ/2)^8$
since $U$ is unimodular and contributes nothing while both scaled summands have half-vector
discriminant groups of exponent two; the computation
`computations/reports/coble_gammaEn2-planes-published-run.txt` realizes every one of the 1024
classes as a parity vector in $\ker(G\bmod 2)$, each of order two. A $2$-primary order alone
would not suffice, and is not what is used. *Divisibility one:* here
$v\in\ten\subseteq\ten^*$, so $\varphi(\ZZ v) = 0$, and the class is the zero class exactly on
the divisibility-one lines; these form a *single* $\gent$-orbit, because [@Ste91, Cor. 3.3] at
$p = 1$ — equal squares, equal divisibility $\ZZ$, and the congruence mod $1\cdot N$, which is
vacuous — makes $\Orth'(\ten)$ transitive on them (this is [@Ste91, Lem. 4.2.1]), and
$\Orth'(\ten) = K\subseteq\gent$. *Divisibility two:* here $v/2\in\ten^*$ and
$\varphi(\ZZ v) = [v/2]$ is a nonzero isotropic class, since $q([v/2]) = v^2/4 = 0$. Let
$\ZZ v, \ZZ w$ be divisibility-two lines with $[v/2], [w/2]$ in one $M$-orbit. Since
$\rho(\gent) = M$, some $g\in\gent$ carries $[v/2]$ to $[w/2]$; put $v' = g(v)$. Then
$[v'/2] = [w/2]$ in $\ten^*/\ten$, and because the class map is a homomorphism whose zero class
is $\ten$ itself, this says exactly
$$ v' - w \in 2\,\ten , $$
which is the congruence modulo $pN$ at $p = 2$ that [@Ste91, Cor. 3.3] requires alongside equal
squares and equal divisibility $2\ZZ$. Its proof — the Siegel–Eichler step $E_{e,y}$ normalizing
$(v,f) = p$, then $E_{f,u}$ — supplies an element of $\Orth'(\ten)$ carrying $v'$ to $\pm w$,
and $\Orth'(\ten) = K\subseteq\gent$ by (H1). Hence each fibre of lines over an $M$-orbit of
classes is a *single* $\gent$-orbit, and the inequivalence of the representatives is the second
statement of [@Ste91, Prop. 4.2.3]. This is Sterk's own proof of 4.2.3 run for the identified
group, not a citation of its conclusion.

Then the $\gent$-orbits of primitive isotropic lines are **five**: one over the zero class and
four over the nonzero $M$-orbits of sizes $2, 120, 270, 135$ — the computed partition
$[1, 2, 120, 135, 270]$ of the 528 isotropic classes.

**The stabilizer images, and the double-coset criterion.** @lem:line-stabilizer-image identifies
the two inputs that @rmk:gamma-en-two-fibres lists as remaining: the discriminant image of the
stabilizer of each line *is* the stabilizer of its class — $M_c$ at the $\gent$ level — so the
criterion $\rho(\Gamma_c) = M_c\cdot\rho(H)$ of that remark holds with equality
($M_c\cdot\rho(H) = M_c$), and no counting input beyond the computed class partition enters: the
number of $0$-cusps is the number of $M$-orbits of isotropic classes, $1 + 4 = 5$, with the
divisibility-one fibre contributing the one orbit over the zero class. The orders are consistent:
$\abs{M_c} = \abs{M}/\text{(orbit size)}$, so the four class stabilizers have orders
$696\,729\,600/2,\ /120,\ /270,\ /135$ respectively.

**Incidence.** The incidence of the nine plane-orbits with the five line-orbits is the type-set,
with the zero class kept apart from the nonzero ones.
Let $\varPi$ be a plane with discriminant image $D$.
Every *nonzero* class $d\in D$ is the class of a primitive isotropic vector of $\varPi$: for
$D = \langle[v/2],[w/2]\rangle$ of order four the three nonzero classes of the $(\ZZ/2)^2$ are
realized by the primitive combinations $(1,0), (0,1), (1,1)$, and for $D$ of order two its single
nonzero class is realized by the second generator.
Such a vector has divisibility two, so these are the divisibility-two line types of the plane.
The zero class is not of that kind, and membership $0\in D$ does not realize it: by
@lem:zero-datum-divisibility a primitive isotropic line has datum zero exactly when it has
divisibility one, and a divisibility-one vector occurs in $\varPi$ exactly when a combination
$av+bw$ has odd pairing, which is the case precisely for the four 4.3.16 planes; the five 4.3.17
planes have every primitive isotropic vector of divisibility two, so they carry no line of the
zero class.
Hence the type-set of a plane is the set of types of the nonzero classes of its image, together
with type $1$ exactly when the plane contains a divisibility-one vector; and the plane of type-set
$S$ is incident to exactly the $0$-cusps whose types lie in $S$, which reproduces the incidence
diagram of [@Ste91, §4.4, Fig. 14]: $\{1,2\},\{1,3\},\{1,4\},\{1,5\}$ meet the corresponding pairs
of $0$-cusps, and $\{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\}$ meet the $0$-cusps named by their
labels.

**Exhaustion for the planes.** The nine planes of @prop:sterk-nine-planes are representatives,
and the exhaustion is [@Ste91, §4.3] applied to the identified group: for each of the five
representative vectors, the reflection subgroup $W(G_v)$ has finite index in $G_v$ (Vinberg's
criterion, verified by the diagrams of 4.3.5–4.3.9, with the diagram symmetries lifting by the
criterion of 4.3.10–4.3.13), every isotropic line of $v^{\perp}/\ZZ v$ is $W(G_v)$-equivalent to a
vertex at infinity of the fundamental polyhedron, and those vertices are exactly the maximal
parabolic subdiagrams enumerated there, and the passage from vector stabilizers to planes is
4.3.1: a plane $\varPi$ containing $v$ determines the isotropic line $\varPi/\ZZ v$ of
$v^{\perp}/\ZZ v$, on which $G_v$ acts, and the same plane recurs for different $v$ exactly as
recorded in 4.3.15–4.3.16 (the interlacing), so the per-vector enumerations combine into nine
classes.

**The interlacing, with its data.** The map of 4.3.1, $\varPi\mapsto\varPi/\ZZ v$, places each
plane in the vector case of every type its type-set contains, so the interlacing is read off the
computed type-sets: the parabolic classes of case $t$ are the planes whose type-set contains
$t$ —
case 1: $\{1,2\},\{1,3\},\{1,4\},\{1,5\}$ (four, as 4.3.5 enumerates);
case 2: $\{1,2\},\{2,4,5\}$ (two, the two maximal parabolic subdiagrams of 4.3.6);
case 3: $\{1,3\},\{3,4\},\{3,5\}$ (three);
case 4: $\{1,4\},\{2,4,5\},\{3,4\},\{4,5\}$ (four);
case 5: $\{1,5\},\{2,4,5\},\{3,5\},\{4,5\},\{5,5\}$ (five).
The recurrences Sterk names are exactly these repetitions: the first class of 4.3.6 is the
$A_7\oplus A_1$ class of 4.3.5 ($\{1,2\}$ recurs in case 2), the $E_7\oplus A_1$ diagram of
4.3.7 is the class of 4.3.5 ($\{1,3\}$ recurs in case 3), and 4.3.8 shares one class with
4.3.7 ($\{3,4\}$, the class in both case 3 and case 4) besides the $D_8$ recurrence from 4.3.5.
Each class is first seen in the case of its least type — four in case 1, then one, two, one,
one in cases 2–5 — nine in all. (The label list printed in 4.3.9's recurrence sentence is not
reliably legible in the page images and is not used; the table above predicts case 5's five
classes, of which $\{2,4,5\},\{3,5\},\{4,5\}$ are shared with earlier cases and $\{5,5\}$ is
new.) The embeddings behind [@Ste91, Prop. 4.6] are those of Lemma 4.3.4 — under the
summand-wise isometry $\ten\cong L_- = H\oplus H(2)\oplus E_8(-2)$, the identification
$(e')^{\perp}/\ZZ e'\cong H\oplus E_8(-2)$ and the single
$\Orth(H(2)\oplus E_8(-2))$-orbit of primitive isotropic vectors in that lattice — and they give
the two $\Orth(L_-)$-classes, not the finer $F$-classes.

**Inequivalence, independent of any count.** The nine planes of @prop:sterk-nine-planes are
pairwise $\gent$-inequivalent by a triple invariant: the *order* of the discriminant image
$D(\varPi)$ of @cor:enriques-plane-fibres, the *multiset* of $M$-orbit-types of its nonzero
classes, and whether the plane contains a divisibility-one vector. These are preserved by
$\gent$: $g\in\gent$ conjugates $D(\varPi)$ by $\rho(g)\in M$, permutes the orbit-types
with multiplicities, and preserves the divisibility-one property. The nine triples are pairwise
distinct — the four 4.3.16 planes have order $2$ with type $(2,), (3,), (4,), (5,)$ respectively
and a divisibility-one generator, while the five 4.3.17 planes have order $4$ with multisets
$(2,4,5), (4,5), (3,5), (3,4), (5,5,5)$ — so the $\{1,5\}$ and $\{5,5\}$ types, which coincide
even as a set *and* as an order, are separated by the last clause, exactly the point where a
mere type-set (namely $\{5\}$ for both) would fail. No appeal to the published count enters
this inequivalence, nor the exhaustion above; the count nine is the output of the enumeration
with its Vinberg hypotheses, not an input anywhere in the chain.
:::

::: {.corollary #cor:enriques-plane-fibres title="The plane fibres for the identified group, and the general double-coset formula"}
Define the discriminant image of a primitive isotropic plane by
$D(\varPi) \definedas \im\bigl((\varPi_{\QQ}\cap\ten^*)\to A_{\ten}\bigr)$ — *not* by
halves of individual generators, since a divisibility-one generator has no half in the dual.
For the four 4.3.16 planes (which contain a divisibility-one vector) this is the order-$2$
subgroup generated by the class of the second generator, and for the five 4.3.17 planes the
order-$4$ subgroup with its three nonzero classes: that is what the computation of
@prop:sterk-nine-planes produced.

**For the identified group.** The map $\varPi\mapsto D(\varPi)$ is $\gent$-equivariant and
surjective onto the $M$-orbits of images, and the invariant of @prop:sterk-nine-planes — the
order of $D(\varPi)$, the multiset of $M$-orbit-types of its nonzero classes, and whether the
plane contains a divisibility-one vector — is invariant under $\gent$. The nine orbits have
pairwise distinct invariants, so there are at least nine $M$-orbits of images; each supports at
least one $\gent$-orbit and there are nine in all, so exactly nine, indexed by the type data,
and **each fibre of $\varPi\mapsto D(\varPi)$ over an $M$-orbit of images is a single
$\gent$-orbit**. The argument uses the identification $\gent = F$ and the exhaustion of
@thm:sterk-line-fibres, not any stabilizer-image equality.

**For general $\Gamma$ with $K\iscontainedin\Gamma\iscontainedin\Orth(\ten)$ this does not
extend by the same counting.** A bijection of $\gent$-orbit sets does not give one on $K$-orbit
sets: a finite stabilizer may permute several $K$-orbits inside one $\gent$-orbit, and that is
the general phenomenon to expect here. The correct statement is the double-coset formula of
@thm:coble-plane-stabilizer-image, applied with $Q = \rho(\Orth(\ten))$, $H = \rho(\Gamma)$,
$F = \Stab_Q(D)$ and $S = \rho(\Stab_{\Orth(\ten)}(\varPi))$: the $\Gamma$-orbits over the
$H$-orbit of $qD$ are the double cosets $(q^{-1}Hq\intersect F)\setminus F/S$, with the
conjugation for translations of $D$ and the intermediate quotient
$(\Gamma\intersect\tilde q\rho^{-1}(F)\tilde q^{-1})\backslash\rho^{-1}(qFq^{-1})/
\Stab(\tilde q\varPi)$ inside the orbit of $\tilde q\varPi$ under $\rho^{-1}(qFq^{-1})$.
For $\Gamma = \gent$ it returns $1$ by the preceding paragraph; for other $\Gamma$ the count is
whatever the formula gives, and is *not* asserted to $1$. In particular the integral
plane-stabilizer image $\rho(\Stab_{\Orth(\ten)}(\varPi))$ — the input the formula needs beyond
the finite partition — is supplied by the pending lattice-orbit computation with its stabilizer
generators, whose result is not assumed anywhere in this section.
:::

::: {.theorem #thm:enriques-integral-plane-stabilizers title="The integral plane stabilizers of the two $O(T_\En)$-plane classes, with their full discriminant images"}
Throughout, $A = A_{T_\En}$ and $D(\varPi) = \im((\varPi_\QQ\cap\ten^*)\to A)$.
The finite-field machinery of this proof uses the exact identification
$$ A = \ten^*/\ten \;\cong\; K \definedas \ker(G \bmod 2) \;\subseteq\; \ten/2\ten , $$
where $G$ is the Gram matrix of $\ten = U\perp U(2)\perp E_8(2)$.
Concretely, $[x/2]\in A$ corresponds to $x\bmod 2$ on the ten scaled coordinates:
such a class is dual exactly when $(x,\ten)$ is even, and $[x/2] = [y/2]$ iff $x-y \in 2\ten$.
The record `computations/reports/coble_enriques-plane-stabilizers-exact-run.txt` prints $\dim K = 10$ and $|K| = |A| = 1024$, so no action on the larger parity module $\ten/2\ten$ is substituted for the discriminant action.
Using the norm-valued quadratic refinement of @def:discriminant, the forms on these representatives are
$$ b\bigl([x/2],[y/2]\bigr) = \frac{(x,y)}4 \pmod \ZZ, \qquad
q\bigl([x/2]\bigr) = \frac{x^2}{4} \pmod {2\ZZ}, \qquad
\beta \definedas 2b,\quad \beta\bigl([x/2],[y/2]\bigr) = \frac{(x,y)}2 \pmod 2. $$
The equivalent half-norm value is $x^2/8\pmod\ZZ$, *not* modulo $2\ZZ$.
Under $x\mapsto x+2t$ with $t\in\ten$, the norm value changes by $(x,t)+t^2\in2\ZZ$ and the half-norm value by half of that in $\ZZ$, while the finite polar value is unchanged; the record checks these identities on every class.

For a primitive isotropic plane $P = \generators{v,w}$, an integral isometry preserving it satisfies
$$ g(v) = av + cw, \qquad g(w) = bv + dw, \qquad \det\begin{pmatrix}a&b\\c&d\end{pmatrix} = \pm1 $$
with $a,b,c,d\in\ZZ$ determined by $g$. The divisibility constraints of $b$ follow from $g(e)$ having $(e,\ten) = \ZZ$ and $g(e')$ having $(e',\ten) = 2\ZZ$, not from an assertion about whole rows.
For both types the displayed Siegel–Eichler generators are evaluated by the established formula
$$ E(\eta,w)(x) = x + b(x,w)\eta - b(x,\eta)w - \tfrac12(w,w)b(x,\eta)\eta , $$
whose dual-basis parameters are exactly the half-basis vectors of $\ten^*$.
Each candidate in the record is checked for an integral matrix (by membership in $\ZZ$, not by the method call `x.denominator`), for preservation of the form by $S^TGS = G$, and for $g(P) = P$ by an exact integral solve.

**(i) The plane containing a divisibility-one vector, $\varPi_0 = \ZZ e\oplus\ZZ e'$.**
The quotient Gram is the definite summand $Q = E_8(2)$, printed in the record.
The admitted integral Levi is $W(E_8)$ on that definite quotient, together with the congruence part $a$ odd, $b$ even above and the displayed dual-basis transvections.
The owned definite isometry computation on $Q^*/Q$ returns
$$ \abs{\induced O(Q)\text{ on }Q^*/Q} = 348\,364\,800 = \abs{\Orth^+(8,2)} . $$
Nine accepted integral plane-stabilizing Eichler matrices generate a discriminant image of order $256$.
Since $\rho(U)$ for the unipotent radical $U$ fixing $P$ and $P^\perp/P$ lies in the order-$2^8$ normal unipotent radical of $\Stab_{O(q)}([e'/2])$,
the block arithmetic gives the full image, not merely a lower bound:
$$ \rho\bigl(\Stab_{\Orth(T_\En)}(\varPi_0)\bigr)
 = \Stab_{\Orth(A,q)}\bigl([e'/2]\bigr), \qquad
348\,364\,800 \times 256 = 89\,181\,388\,800 = \abs{\Stab_{O(q)}([e'/2])}. $$
The relation $[O^+(8,2):\rho(L)] = 1$ is the exact sequence compute:
$\ker(W(E_8)\to O(E_8/2E_8)) = \{\pm1\}$ [@CCN+85], so $348\,364\,800 = |W(E_8)|/2$.

**(ii) The class with all primitive vectors of divisibility two, represented by $P = \generators{e',z}$ with $z = 2e+2f+\alpha$ for a pair $\alpha$ of orthogonal E_8 roots.**
Its exact quotient Gram $Q = P^\perp/P$ has determinant $64$; the record prints it, then certifies the integral identification with $D_8^*(2)$ in the negative convention by the matrix
$$ R = \begin{pmatrix}
 1 & 2 & 3 & 4 & 5 & 0 & 0 & 1\\
-1 & 0 & 1 & 2 & 3 &-2 &-1 & 0\\
 0 & 0 & 0 & 0 & 0 &-1 & 0 & 0\\
 0 &-1 &-2 &-3 &-4 &-1 & 0 &-1\\
 0 &-1 &-2 &-3 &-4 & 0 & 0 & 0\\
 0 &-1 &-2 &-3 &-3 & 0 & 0 & 0\\
 0 &-1 &-2 &-2 &-2 & 0 & 0 & 0\\
 0 &-1 &-1 &-1 &-1 & 0 & 0 & 0
 \end{pmatrix},
 \qquad R^T(-Q)R = 2(D_8)^{-1}. $$
Thus the claimed identification is proved by an explicit isometry, not inferred from norms.

**The integral Levi lifts.** The owned exact shell of $Q$ has $368$ vectors of square $-4$. Of these, $112$ have representatives $r\in P^\perp\intersect2\ten^*$; for each, the reflection
$$ s_r(x)=x+\frac{(x,r)}2r $$
is integral on $\ten$, preserves its form, and fixes $e'$ and $z$ pointwise. These are therefore actual lifts from the *embedded* plane, not automorphisms of an unrelated copy of $Q$. The remaining $256$ shell vectors are not used. The record verifies every integral reflection matrix and its induced quotient matrix.

The dual-coordinate convention is explicit. If $\Delta=UQV$ is the Smith form of the Gram matrix $Q$, a Smith residual $r$ represents $Q^{-1}U^{-1}r\in Q^*/Q$; a column isometry $X$ of $Q$ acts on its numerator by $X^{-T}$. The record proves this convention on all $64$ classes, including identity, composition and invariance under adding $Q\ZZ^8$. With this action, the native group $O(Q)$ has image of order $40320$, and the $112$ integral reflection lifts have the same image. Thus they generate the full finite Levi action.

**Identification with $D^\perp/D$.** Put $M=P^\perp$, so $M_\QQ=P_\QQ^{\perp}$ and $(M_\QQ)^\perp=P_\QQ$. For $y\in M^*$, choose $u\in(M_\QQ)^\perp$ with $y+u\in\ten^*$. The natural gluing map is
$$ j:A_Q\longrightarrow D^\perp/D,\qquad [y]\longmapsto[y+u]+D. $$
This is not a separate construction for $\ten$: it is the comparison map $\varphi_P$ of @thm:isotropic-reduction-discriminant applied to $L=\ten$ and $P$, where the correction $u\in(M_\QQ)^\perp=P_\QQ$ is the one whose existence and uniqueness modulo $L^\#\cap P_\QQ$ is @lem:isotropic-reduction-extension, well-definedness and choice independence are its last item, and injectivity is proved there from primitivity and nondegeneracy. Surjectivity is *not* obtained by projecting a class in $D^\perp$ to $M^*$: it is the comparison of two independent counts of the same finite set, the order $\cardinality{A_L}/[L^\#\cap P_\QQ:P]^2$ of the subquotient, which is duality for the isotropic subgroup $D=N_V/P$ of the nondegenerate form $A_L$ (@lem:isotropic-subgroup-quotient-order), and the order $\cardinality{A_Q}$ of the cusp quotient's discriminant group, which is the block determinant identity of @lem:isotropic-reduction-index. The same theorem states that $j$ is an isometry of the norm-valued discriminant forms, in the bilinear and the quadratic form, and that it is equivariant for $\Stab_{\Orth(\ten)}(P)$ — equivariance, not the statement that the finite stabilizer is the integral image, which is a lifting question and is the separate content of the integral-stabilizer computation below (@cor:isotropic-reduction-stabilizer states exactly what the general theorem does and does not give); here $\ten$ is even, so the quadratic statement applies. What the record adds to the theorem is the instance: it prints a $10\times6$ matrix $J$ for $j$, checks $\rank(J)=6$ and $\rank([J\mid d_0,d_1])=8$, and verifies directly that all $63$ nonzero vectors of $\im J$ avoid $D$. This proves injectivity *after* quotienting by $D$, not merely in the rank-$10$ module. It also verifies all $64$ classes in $D^\perp$, checks $q_Q=q_\ten\pmod{2\ZZ}$ on every one, and checks for each of the $112$ integral reflections that its direct action on $A$ agrees modulo $D$ with its dual $Q^*/Q$ action transported by $j$. Consequently $j$ identifies the lifted Levi with the full action on $D^\perp/D$.

**The kernel, including its plane block.** Let
$$ F=\Stab_{\Orth(A,q)}(D),\qquad C=\ker\bigl(F\to\Orth(D^\perp/D)\bigr). $$
Write $A=D\oplus D^\vee\oplus(D^\perp/D)$ with the first two summands hyperbolic. In matrix form on these summands, the quadratic-preservation equations for an element of $C$ leave one $GL_2(\F_2)$ block, $12$ bits for the maps $D^\perp/D\to D$, and one further alternating bit. Hence
$$ \abs C=|GL_2(\F_2)|\cdot2^{13}=6\cdot8192=49152. $$
Each of the fifteen integral plane-stabilizing Eichler matrices above is checked to lie in $C$. Their generated group has order $49152$, so it is $C$, not merely a subgroup with an unrelated matching order. As a further direct check, its action on $D$ is all of $GL_2(\F_2)$, and its pointwise-on-$D$ subgroup has order $8192$ and index $6$.

The integral reflection lifts surject to $\Orth(D^\perp/D)$, of order $40320=|\Orth^+(6,2)|$, while the kernel of that same quotient map on $F$ is exactly $C$. Therefore $\rho(\Stab_{\Orth(\ten)}(P))$ contains the full kernel and the full quotient of $F$, and
$$ \rho\bigl(\Stab_{\Orth(T_\En)}(P)\bigr) = F=\Stab_{\Orth(A,q)}(D),
 \qquad 40320\times 49152 = 1\,981\,808\,640 = \abs F. $$
For definiteness, the three nonzero classes of $D$ in the record are
$[z/2]$ (bit string `000011000000`), $[e'/2]$ (`001000000000`), and their sum (`001011000000`), each counted with multiplicity one; no ordered pair is collapsed into a set of distinct vector types.

**Specialization to $\Gamma_{\En,2}$.**
Write $Q_0 = \rho(\Orth(T_\En))$, $H_0 = \rho(\Gamma)$ with $\ker\rho\subseteq\Gamma\subseteq\Orth(T_\En)$, $F = \Stab_{Q_0}(D)$ and $S = \rho(\Stab_{\Orth(T_\En)}(P))$.
Items (i) and (ii) prove $S = F$ for every finite type under consideration, and for any such $\Gamma$ the two-preimage argument gives
$$ \rho\bigl(\Stab_\Gamma(P)\bigr) = \rho\bigl(\Stab_{\Orth(T_\En)}(P)\bigr)\cap H_0 = \Stab_{H_0}(D), $$
because if $h = \rho(g) = \rho(g_2)$ with $g$ in the integral stabilizer and $g_2\in\Gamma$, then $gg_2^{-1}\in\ker\rho\subseteq\Gamma$, so $g\in\Gamma$.
For $\Gamma = \Gamma_{\En,2}$, with $H_0 = M$, the double-coset fibre of @cor:enriques-plane-fibres therefore has count
$$ \bigl(q^{-1}H_0q\intersect F\bigr)\bigl\backslash F \big/ S = F/F = 1 $$
per $M$-orbit of images: the fibre of primitive isotropic planes over each image is a single $\Gamma_{\En,2}$-orbit.
This equality of images is *proved from the integral reflection lifts, the explicit gluing, and the kernel inclusion*, not inferred from a single orbit over an $M$-orbit or from the finite partition.

**The positive-spinor restriction.** Put $\Gamma^+=\Gamma\intersect\Orth^+(\ten)$ and $H_0^+=\rho(\Gamma^+)$. The isometry
$$ \tau=-\id_{U(2)}\oplus\id_{U\perp E_8(2)} $$
belongs to $\ker\rho$, stabilizes both $P=\langle e,e'\rangle$ and $P=\langle e',z\rangle$ (it sends $e'$ to $-e'$ and fixes $e$ and $z$), and has normalized real spinor norm $-1$ by @lem:minus-identity-spinor-norm, since $U(2)$ has positive index one. The two-preimage argument therefore survives the spinor restriction: if $g\in\Stab_{\Orth(\ten)}(P)$ and $g_2\in\Gamma^+$ have the same discriminant image, then $gg_2^{-1}\in\ker\rho$. If $g$ is spinor-negative, replace it by $\tau g$, which is spinor-positive and has the same discriminant image. The resulting element lies in $\Gamma^+$, and
$$ \rho\bigl(\Stab_{\Gamma^+}(P)\bigr)=\Stab_{H_0^+}(D). $$
In particular, with $\Gamma_{\En,2}^+=\Gamma_{\En,2}\intersect\Orth^+(\ten)$ and $M^+=\rho(\Gamma_{\En,2}^+)$, the plane fibre over each $M^+$-orbit is a single $\Gamma_{\En,2}^+$-orbit by the same double-coset formula. This supplies the containment and stabilizer witness that the full-$O$ kernel argument alone does not provide.

For other $\Gamma\supseteq\ker\rho$ the general double-coset formula of that corollary governs; no fibre count is asserted from the reported orbit padding alone.
:::

::: {.theorem #thm:enriques-degree-two-arithmetic title="The source-defined degree-two Enriques family: five 0-cusps, nine 1-cusps, and their incidence"}
Let $\gent$ be the group of [@AEGS25, Def. 2.6], namely the image in $\Orth(\ten)$ of
$$ \theset{g\in\Orth(L)\mid g\circ I_\En=I_\En\circ g,\;g(h)=h}. $$
The source's arithmetic convention is the full orthogonal group: $\Gamma_\En=\Orth(\ten)$ and $\gent=\Gamma_\En\cap\Gamma_{\mathrm{dP}}$, with no intersection with $\Orth^+(\ten)$ implicit in the definition. Then $\gent=F=\rho^{-1}(M)$, and:

1. The map $\ZZ v\mapsto[v/\operatorname{div}(v)]$ on primitive isotropic lines has exactly five $\gent$-orbits. There is one divisibility-one orbit over the zero class, and four divisibility-two orbits over the $M$-orbits of sizes $2,120,270,135$. Each fibre over an $M$-orbit is a single $\gent$-orbit, not merely a surjective finite image.
2. The map $\varPi\mapsto D(\varPi)$ on primitive isotropic planes has exactly nine $\gent$-orbits, labelled by the four 4.3.16 types and the five 4.3.17 types. Each fibre over an $M$-orbit of discriminant images is a single $\gent$-orbit.
3. Their incidences are exactly $\{1,2\},\{1,3\},\{1,4\},\{1,5\}$ among the first four and $\{2,4,5\},\{4,5\},\{3,5\},\{3,4\},\{5,5\}$ among the last five, as in the source's cusp diagram.

The positive-spinor assertion of the preceding theorem is an additional restricted-group statement; it is not a replacement for this full-$O$ arithmetic result.
:::

::: {.proof}
The group identification is @thm:sterk-line-fibres, which uses @prop:gamma-en-two-index for $\ker\rho\subseteq\gent$ and @thm:two-elementary-surjectivity for surjectivity of $\rho$. The same theorem proves item 1 with both divisibilities separated and applies [@Ste91, Cor. 3.3] to the corresponding congruence on each fibre.

For item 2, @thm:sterk-line-fibres' plane exhaustion supplies the nine representatives and its triple invariant proves them pairwise inequivalent. @cor:enriques-plane-fibres proves that their fibres are single $\gent$-orbits. Independently of that direct source-fibre argument, @thm:enriques-integral-plane-stabilizers proves both full integral stabilizer images and returns one double coset in the same formula for every $M$-orbit. Thus the nine count does not depend on a pending lattice-orbit run or on multiplying two unrelated finite group orders. Item 3 is the incidence computation in @thm:sterk-line-fibres. These are the boundary orbits of the Baily--Borel compactification of $\mathcal D(\ten)/\gent$, giving five 0-cusps and nine 1-cusps for the source's $F_{\En,2}$.
:::
::: {.remark #rmk:sterk-one-cusp-types title="The published plane types and their boundary groups"}

The one-dimensional components are the $F$-orbits of primitive isotropic planes, classified by *type* under $F$, not by a single finite invariant. From the published text via its page images:
- the four cases of §4.3.16 ($E_8$, $D_8$, $A_7\oplus A_1$, $E_7\oplus A_1$) built from non-equivalent vectors, whose half-plane components show no cusp identification;
- the five cases of §4.3.17, with $\mathcal F(F)\cap SL(\mathcal F)$ respectively $\Gamma(2)$ for $\{2,4,5\}$, $\Gamma^1(2)$ for $\{4,5\}$, $\Gamma^1(2)$ for $\{3,5\}$, $\Gamma^1(2)$ for $\{3,4\}$, and $SL_2(\ZZ)$ for $\{5,5\}$. The two middle groups have the superscript 1, not the OCR's $E_1(2)$ and $F_1(2)$.
Total nine one-cusps, as AEGS states at §3.3 p. 590.
Whether any two types share a finite plane image is a separate computation of those images; it is not asserted by diagram classification and it is not used here.
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

The criterion is a statement about a chosen set $X$, not about the group: agreement on one $\Gamma$-set says nothing about another.
It is the form taken here by the fibre-level criterion of @prop:descent-spinor-fibre, with the stabilizer of the individual object in place of the stabilizer inside a discriminant fibre.

::: {.theorem #thm:enriques-spinor-orbit-agreement title="Spinor agreement for every polarization family of $\ten$: isotropic lines, isotropic planes and flags"}

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$ with signature $(2,10)$, let $\rho$ be its quadratic discriminant representation and $\widetilde\Orth(N)=\ker\rho$ its discriminant kernel, and let $\Gamma\leq\Orth(N)$ be a subgroup with $\widetilde\Orth(N)\subseteq\Gamma$.
Every subgroup obtained as a finite-character preimage $\rho^{-1}(M)$ with $M\leq\Orth(A_\ten,q_\ten)$ is of this form, and so is the value of `coinvariant_extension_subgroup()` for any source-defined polarization family.
Put $\Gamma^+=\Gamma\intersect\Orth^+(N)$.
Then $\Gamma$ and $\Gamma^+$ have the same orbits on

1. the primitive isotropic lines of $N$;
2. the primitive isotropic planes of $N$;
3. the flags $\ell\subset P$ consisting of a primitive isotropic line contained in a primitive isotropic plane,

For the lines the same holds for primitive isotropic vectors: $-\id_N$ lies in $\ker\rho$ and in $\Orth^+(N)$, being level two because $A_\ten$ is annihilated by $2$ and spinor-positive by @lem:minus-identity-spinor-norm at positive index two, so $-\id_N\in\Gamma\intersect\Gamma^+$ and the two generators of a line lie in one orbit of both groups.
Consequently the counts $\#I_1$, $\#I_2$ and $\#I_{12}$, evaluated on the preimage $\Gamma$, are the corresponding counts of $\Gamma^+$.
Items 1 and 2 are proved below by transporting the two witnesses $\sigma_U$ and $\tau_0$ of @lem:enriques-level-two-transvections along the two $\Orth(N)$-orbits of primitive isotropic lines of [@Ste91, 4.5] and the two $\Orth(N)$-classes of primitive isotropic planes of [@Ste91, 4.6]; item 3 is @thm:enriques-flag-witnesses, which produces a spinor-negative level-two element in the stabilizer of every primitive line of either plane class, and to which the same transport then applies.
:::

::: {.proof}

This is the existence statement for the witnesses; the group theory that converts a witness into an orbit identity is @lem:spinor-orbit-agreement.

*Notation.*
Write $e,f$ for the hyperbolic basis of the summand $U$, $e',f'$ for that of $U(2)$, and $r_1,r_2$ for two orthogonal roots of the summand $E_8(2)$ — two non-adjacent simple roots of $E_8$ in the Bourbaki numbering, of square $-4$ — with $\alpha\definedas r_1+r_2$ and $z\definedas 2e+2f+\alpha$.
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
Both $P_1$ and $P_2$ are primitive totally isotropic planes.
Total isotropy: $e$ and $e'$ are isotropic and orthogonal because $U$ and $U(2)$ are hyperbolic planes, and $z^2=(z,e')=0$ in @lem:enriques-level-two-transvections.
For primitivity: $z$ is primitive in the direct summand $U\oplus E_8(2)$ — the argument of @lem:enriques-level-two-transvections uses only the $U$- and $E_8(2)$-components — $e$ is a basis vector of the summand $U$, $e'$ is a basis vector of the summand $U(2)$, and a span of primitive vectors taken from two orthogonal summands is primitive in their sum, its quotient being the direct sum of the two quotients.
By [@Ste91, 4.6] there are exactly two $\Orth(N)$-classes of primitive isotropic planes, and $P_1$ and $P_2$ lie in different ones.
Indeed $P_1$ contains the divisibility-one vector $e$, whereas every primitive vector $az+be'$ of $P_2$ has divisibility exactly two: the ideal $(\ten,az+be')$ is generated by $2a$, $2b$ and the numbers $a\beta(\alpha,x)$ with $x$ in the summand $E_8(2)$, all of which lie in $2\bZ$ because the bilinear form of that summand takes its values there, while $\gcd(a,b)=1$ makes $2$ one of their combinations.
Divisibility is an invariant of the $\Orth(N)$-orbit, so $P_2$ contains no vector equivalent to $e$; the two classes being exhausted, $P_1$ and $P_2$ are representatives.
For a plane $P$ choose $g$ with $gP_1=P$ or with $gP_2=P$, and put $k\definedas g\sigma_Ug^{-1}$ in the first case and $k\definedas g\tau g^{-1}$ in the second; then $k\in\ker\rho\setminus\Orth^+(N)$ and $k$ stabilizes $P$.

*Conclusion.*
The hypotheses of @lem:spinor-orbit-agreement are met: $\Orth^+(\ten)$ has index two in $\Orth(\ten)$, because $\spinornorm_\bR$ is a homomorphism from $\Orth(\ten)$ to $\{\pm1\}$ with kernel $\Orth^+(\ten)$ and it is onto, $\sigma_U$ being an integral isometry of $\ten$ with $\spinornorm_\bR(\sigma_U)=-1$; and at every primitive isotropic line and at every primitive isotropic plane the stabilizer inside $\Gamma$ meets $\Gamma\setminus\Orth^+(\ten)$.
Items 1 and 2 follow on those two sets.
Item 3 is @thm:enriques-flag-witnesses, which produces such a $k$ for every flag, after which the same lemma gives item 3.
Nothing here counts orbits: what is proved is equality of the orbit *sets*, and no table value enters.
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
No structure theory of $\Orth(V)$ is used: what enters is that a unipotent isometry is the exponential of a nilpotent endomorphism, and that $\bR$ is divisible.

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

Let $N=\ten=U\oplus U(2)\oplus E_8(2)$, with $e,f$ the hyperbolic basis of $U$, $e',f'$ that of $U(2)$, and $r_1,r_2$ two orthogonal roots of the summand $E_8(2)$ — two non-adjacent simple roots of $E_8$ in the Bourbaki numbering; the summand is negative definite, so its norms lie in $4\bZ$ and its inner products in $2\bZ$.
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

1. **Integrality.** These five are integral isometries of $N$, with the images
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
2. **The discriminant kernel.** All five lie in $\widetilde\Orth(N)=\ker\rho$.
3. **Spinor signs.** $\spinornorm_\bR(\sigma_U)=\spinornorm_\bR(\tau_0)=-1$, and $\spinornorm_\bR(E_1)=\spinornorm_\bR(E_2)=\spinornorm_\bR(E_3)=1$.
4. **The two planes and their lines.** $E_1$, $E_1^2$ and $E_2$ stabilize $P_1=\generators{e,e'}$; $E_1$ and $E_3$ stabilize $P_2=\generators{z,e'}$; $\sigma_U$ stabilizes $P_1$; $\tau_0$ stabilizes both. For a primitive $v=ae+ce'$ of $P_1$ the divisibility is $\gcd(a,2c)$, and every primitive vector of $P_2$ has divisibility $2$.

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

No count is asserted: the primitive lines of a plane are infinite in number, and nothing is claimed about the discriminant image of $\Stab_{\Orth(N)}(P_i)$ or about the number of $\Gamma$-orbits on lines, planes or flags.

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
By [@Ste91, 4.6] there are exactly two $\Orth(N)$-classes of primitive isotropic planes, represented by $P_1$ and $P_2$ — the argument for the representatives, including their primitivity, is in @thm:enriques-spinor-orbit-agreement — so there is $g\in\Orth(N)$ with $gP_1=P$ or with $gP_2=P$.
Then $g^{-1}\ell$ is a primitive isotropic line of that representative plane, hence has a witness $k$ by the two paragraphs above, and $gkg^{-1}\in\ker\rho$ has spinor norm $-1$ and fixes $P$ and $\ell$.
Since every witness lies in $\ker\rho\subseteq\Gamma$, the stabilizer inside $\Gamma$ of each of these objects meets $\Gamma\setminus\Orth^+(N)$.

*What this does not give.*
The lines of a totally isotropic plane form the infinite set $\PP^1(\bQ)$, and the argument covers them by the integral Euclidean reduction of @lem:congruence-two-transitivity, not by any count of residue classes: a statement about the image modulo $2$ alone bounds nothing on integral lines, and the transitivity statements used are about the actual primitive vectors.
Nothing is asserted about $\rho\qty(\Stab_{\Orth(N)}(P_i))$, and no number of $\Gamma$-orbits on lines, planes or flags follows from these stabilizer statements; the transition from stabilizers to orbit identity is @lem:spinor-orbit-agreement, applied in @thm:enriques-spinor-orbit-agreement.

:::

The two isotropic families of @thm:enriques-spinor-orbit-agreement are therefore not a place where the preimage and its spinor-positive half differ, and that conclusion is reached object by object: the hypothesis of @lem:spinor-orbit-agreement is verified at a witness in each stabilizer and transported, so it does not rest on any agreement of table values, and equal counts would not have established it.
For flags the mechanism is different and is the content of @thm:enriques-flag-witnesses: a plane witness does not fix a flag, and there the witnesses are the conjugates, inside the stabilizer of the plane, of $\sigma_U$ for the plane $\generators{e,e'}$ and of $\tau_0$ and of the product $\theta=E_1\tau_0$, which fixes the vector $z+e'$, for the plane $\generators{z,e'}$.
The conjugating elements are the explicit transvections, which act on the primitive lines of the plane through the two level-two shears $A$ and $B$ and, on the first plane, through the shear $\mu$; $\mu$ is not in the principal congruence subgroup $\Gamma(2)$, and it is needed exactly to pass between the two divisibility-one classes $[1:0]$ and $[1:1]$ — on that plane the realized group therefore has two orbits on the lines, not three, and the modulus-two image of the group does not determine them.

::: {.corollary #cor:enriques-preimage-vs-positive title="Which subgroup a discriminant-preimage comparison tests"}

Let $M\leq\Orth(A_\ten,q_\ten)$ and $\Gamma=\rho^{-1}(M)$, so that $\rho(\Gamma)=M$ by @thm:two-elementary-surjectivity; put $\Gamma^+=\Gamma\intersect\Orth^+(N)$.

1. $\Gamma^+$ has *index two* in $\Gamma$, and $\rho(\Gamma^+)=\rho(\Gamma)=M$: for $g\in\Gamma$ the element $g\tau$ has the same image as $g$ and the opposite spinor sign.
2. A finite-character preimage construction returns $\Gamma$, not $\Gamma^+$: it returns the full preimage, and the two are infinite arithmetic groups of the same rank, differing by the spinor sign and not by a factor of finite order.
3. Consequently the counts $\#I_1$ and $\#I_2$ of isotropic lines and planes and the incidence count $\#I_{12}$ of flags may be compared against either group without error (@thm:enriques-spinor-orbit-agreement for the first two and its third item with @thm:enriques-flag-witnesses for the third), while the group order, any count of isometries, or orbits on any other $\Gamma$-set are answered only by the group actually supplied: by @lem:spinor-orbit-agreement the orbits agree exactly on the sets whose stabilizers all meet $\Orth(N)\setminus\Orth^+(N)$, and that is verified here for isotropic lines, isotropic planes and flags only.
:::

::: {.proof}

For item 1: $\tau\in\widetilde\Orth(N)\subseteq\Gamma$ is spinor-negative, so for $g\in\Gamma$ one has $g\tau\in\Gamma$ with $\rho(g\tau)=\rho(g)$ and $\spinornorm_\bR(g\tau)=-\spinornorm_\bR(g)$; thus every class of $\Gamma$ modulo $\Orth^+$ is met in $\Gamma^+$ after multiplication by $\tau$ as needed, which gives both $\Gamma=\Gamma^+\sqcup\Gamma^+\tau$ and $\rho(\Gamma^+)=\rho(\Gamma)$.
The kernel of $\rho|_{\Gamma^+}$ is $\widetilde\Orth(N)\intersect\Orth^+(N)=\widetilde\Orth^+(N)$, of index two in $\widetilde\Orth(N)$ because $\tau$ lies in the latter and not the former, so $\Gamma^+$ has index two.
For item 2: the preimage is $\rho^{-1}(M)$ by the defining property of a discriminant preimage, and $\Gamma=\Gamma^+\sqcup\Gamma^+\tau$ exhibits it as the union of two cosets of a subgroup of index two; both are infinite arithmetic groups of the same rank, so no finite factor relates their orders — there are none.
Item 3 is @lem:spinor-orbit-agreement applied to the families of @thm:enriques-spinor-orbit-agreement: the isotropic lines and planes, and the flags of @thm:enriques-flag-witnesses.
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
What the criterion needs is the image of $\Stab_{\Orth(\ten)}(x)$: by @lem:line-stabilizer-image that image *is* the stabilizer of the class — $M_c$ at the $\gent$ level — so the criterion holds with equality and the finite count $5 = 1+4$ is the number of $0$-cusps of $\fen$, not merely a count of $\rho(\gent)$-orbits on classes. The computational route through `computations/reports/coble_gammaEn2-cusps-lattice.py` (the stabilizer generators that `T_En.cusps(1)` retains, for both lines) remains as an independent check of the lemma; it is not the proof of it.

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
For the case at hand, $A = \bD(T_\Co)$ with $G_A = \Gamma^{\Gamma}_\Co$ of @def:gamma-co-groups and $B = \bD(T_\En)$ with $G_B = \Gamma$, and what @prop:gamma-co-images supplies is the strong form, with equality: restriction of $\Stab_{\Gamma}(\delta)$ to $T_\Co$ is exactly $\Gamma^{\Gamma}_\Co$, so $g_A\mapsto g_A\oplus\id_{\ZZ\delta}$ is a genuine homomorphism and $f^{\Gamma}$ is $G_A$-equivariant, not merely orbit-compatible.
It is worth naming what that map is, since the weak form would not have given it: the kernel of restriction is $\{1, s_k\}$, where $s_k$ is the reflection in the $(-2)$-vector $k = \tilde e - \tilde f$ --- it fixes $T_\Co$ pointwise and negates $k$ --- so restriction is two-to-one on the stabilizer and the equivariant assignment is its section, the extension fixing $k$.
Equality of the images does not give injectivity of $\bar f$: two $G_A$-orbits may still be carried into one $G_B$-orbit, and it is the point of $\bD(T_\Co)$ lying on a second translate $\inverseof{g}(T_\Co)$ that the fibre count has to control.
:::
