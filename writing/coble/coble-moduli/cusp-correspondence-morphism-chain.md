---
unit: research-program
status: conjectural
tags:
  - coble
  - cusps
  - baily-borel
  - morphisms
---

# The Coble cusp correspondence and the morphism chain {#sec-cusp-correspondence-morphism-chain}

## The chain of morphisms

::: {.proposition #prop:fen2-forgetful-maps title="The two morphisms out of $\fentwo$"}

Let $\fttz=\bD(\tdp)/\Gamma_\dP$ be the moduli space of K3 surfaces of degree $4$ with a del Pezzo involution [@AEGS25, §1, Def. 2.7].

1. The inclusion $\bD(T_\En)\subset\bD(\tdp)$ induces a finite, generically injective morphism $\fentwo\to\fttz$, and $\fentwo$ is the normalization of a closed subvariety of $\fttz$ [@AEGS25, Lemma 2.8].
2. The inclusion $\gent\subseteq\Gamma^K_\En$ of a subgroup of finite index induces a morphism $\fentwo\to F_{(10,10,0)}=\bD(T_\En)/\Gamma^K_\En$ of degree $2^7\cdot17\cdot31$ [@AEGS25, §2.3; @Ste91, Rem. 2.12].
:::

::: {.construction title="The embedding and its two extensions"}

By @lem:locally_closed_embedding_BB, the lattice embeddings $T_\Co\injects\ten$ and $T_\Co\injects\tdp$ induce locally closed embeddings $\fco\injects\fen$ and $\fco\injects\fttz$, which extend to morphisms of Baily--Borel compactifications:
$$
\eta: \bbcpt{\fco} \to \bbcpt{\fen},
\qquad
\tilde\eta: \bbcpt{\fco} \to \bbcpt{\fttz} .
$$
The stratification of $\partial\bbcpt{F^{\mathrm{un}}_\Co}$ is obtained by applying the mirror moves of [@AE22] to $S_{\Co} = (11,11,1)_1$.
On $0$-cusps, $\eta$ induces an injective map from the $527$ $0$-cusps of the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ to the $0$-cusps of $\fen$ of divisibility $2$ (@prop:cusp-map-injective, @prop:cusp-map-not-onto).
:::

## The two cusp identifications

::: {.proposition #prop:fen2-zero-cusp-lattices title="The lattices of the five $0$-cusps of $\fentwo$"}

Let $e\in\ten$ be a primitive isotropic vector, and number the $0$-cusps of $\fentwo$ as in [@Ste91].

1. The lattice $e^{\perp}/e$ is $U(2)\oplus E_8(2)=(10,10,0)_1$ when $e$ represents cusp $1$, and $U\oplus E_8(2)=(10,8,0)_1$ when $e$ represents one of cusps $2$ to $5$ [@AEGS25, Lemmas 3.9, 3.10].
2. The Coxeter diagram of cusp $2$ is the folding of the Coxeter diagram of $(18,0,0)_1$ by the reflection $\alpha_k\mapsto\alpha_{20-k}$ [@AEGS25, Lemma 3.9]. The Coxeter diagrams of cusps $1$, $3$, $4$ and $5$ are foldings of the Coxeter diagram of $(18,2,0)_1$ [@AEGS25, Lemma 3.10].
:::

::: {.corollary #cor:coble-zero-cusp-over-sterk-two-to-five title="The $0$-cusps of $\fentwo$ over the $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$"}

Every $0$-cusp of $\fentwo$ over the image in $F^K_\En$ of the $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$ is one of cusps $2$ to $5$. The reduced dual complex $\Gamma(\mcz_0)$ of each of these cusps is the disc $\Dc^2$.
:::

::: {.proof}

The morphism $\fentwo\to F^K_\En$ of @prop:fen2-forgetful-maps sends the $0$-cusp of a primitive isotropic vector $e\in\ten$ to the $0$-cusp of the same vector $e$, so it preserves the lattice $e^{\perp}/e$. By @lem:w1_perp_calculation the image of $(9,9,1)_1$ is the $0$-cusp $(10,8,0)_1$ of $F^K_\En$. By @prop:fen2-zero-cusp-lattices the cusps of $\fentwo$ with $e^{\perp}/e=(10,8,0)_1$ are cusps $2$ to $5$. Their dual complexes are listed in @ex:fen2_five_cusps.
:::

::: {.lemma #lem:cusp-map-of-a-period-lattice-embedding title="The $0$-cusp of an isotropic line maps to the $0$-cusp of the same line"}

Let $\iota\colon T\injects T'$ be a primitive embedding of even lattices of signature $(2,n)$ and $(2,n')$ with $n,n'\geq1$, let $\Gamma\subseteq\Orth^+(T)$ and $\Gamma'\subseteq\Orth^+(T')$, and suppose the inclusion of period domains $\bD(T)\subset\bD(T')$ descends to a morphism $\bbcpt{\bD(T)/\Gamma}\to\bbcpt{\bD(T')/\Gamma'}$ extending to the Baily--Borel compactifications [@KK72, §5, Thm. 2].
Then for a primitive isotropic line $\ell = \ZZ v\subset T$ the induced map of $0$-cusps sends $[\ell]$ to $[\iota(\ell)]$.
:::

::: {.proof}

A point of $\bD(T)$ is a positive definite $2$-plane $P\subset T_\bR$, and since $T_\bR\subset T'_\bR$ the same $P$ is a point of $\bD(T')$: the inclusion of period domains is literal.
The boundary component attached to $\ell$ is $F_\ell = \bD(\ell^{\perp T}/\ell)$, the positive $2$-planes whose complex line is $\ell$.
Because $\iota$ is injective, $\ell^{\perp T} = T\intersect\ell^{\perp T'}$, so $\ell^{\perp T}/\ell\subset\ell^{\perp T'}/\ell$ and hence $F_\ell\subset F_{\iota\ell}$ as subdomains of the boundary of $\bD(T')$.
A $0$-cusp is the orbit of one of these components, equivalently of the primitive isotropic line that names it [@AEGS25, §3.1, printed p. 589], and the extension of [@KK72, §5, Thm. 2] carries rational boundary components to rational boundary components compatibly with the action of the two groups.
So the orbit of $F_\ell$ is carried to the orbit of $F_{\iota\ell}$, that is $[\ell]\mapsto[\iota(\ell)]$.
:::

::: {.theorem #thm:coble-zero-cusp-sterk-two title="Which cusp of $\fentwo$ carries the Coble $0$-cusp: cusps $2$--$5$ for the boundary lattice, cusp $2$ for the chamber"}

Let $\delta = e-f$, $T_\Co = \delta^{\perp\ten}$, $\Gamma_{\Co,2} = R_{\Gent}$ and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$, and let $\eta_1,\dots,\eta_5$ be the printed Enriques cusp vectors of @ex:sterk-isotropic-divisibilities, in the coordinates of $\ten = U\oplus U(2)\oplus E_8(2)$.
Then:

1. **Cusp $1$ carries no Coble $0$-cusp.** $(\eta_1,\delta) = -1$, so $\eta_1\notin T_\Co$.
2. **Each of cusps $2$, $3$, $4$, $5$ carries one, and all four have the same boundary lattice.** For $k=2,3,4,5$ the vector $\eta_k$ is primitive and isotropic with $(\eta_k,\delta) = 0$ and $\div_{\ten}(\eta_k) = 2$, and the lattice $\eta_k^{\perp T_\Co}/\ZZ\eta_k$ is even of rank $9$, determinant $2^9$, signature $(1,8)$ and invariants $(r,a,\delta) = (9,9,1)$, hence is $(9,9,1)_1$ (@thm:two-elementary-classification).
   So each of Sterk's cusps $2$ to $5$ carries a $0$-cusp of $F_{\Co,2}$ with boundary lattice $(9,9,1)_1$, by @thm:coble-pair-semifan(0) and @lem:cusp-map-of-a-period-lattice-embedding; and since $\Gamma_{\Co,2}\subseteq\Orth(T_\Co)$ and $\Orth(T_\Co)$ is transitive on primitive isotropic vectors (@thm:unpolarized-cusps), the four sit over the one $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$.
   **The boundary lattice therefore singles out no cusp**: the identification of the Coble $0$-cusp with cusp $2$ alone is false in this reading.
3. **The chamber singles out cusp $2$.** Restricted to $\delta^\perp$, the facet at Sterk cusp $2$ is the Coble chamber of @thm:coble-cusp-chamber: nine walls forming a tree with arms of lengths $1$, $2$ and $5$ at its branch vertex, eight walls of square $-4$ and one of square $-2$ at the end of the long arm, every bond of label $3$ except the last bond of the long arm, of label $4$.
   At cusps $3$, $4$ and $5$ the same construction gives $10$, $10$ and $11$ distinct walls.
   Two cones with different numbers of facets are not isometric, so cusp $2$ is the unique cusp of $\fentwo$ whose local reflection data are the Coble $0$-cusp's, and this is the sense in which the Coble $0$-cusp is Sterk cusp $2$.
4. **Cusp $2$ is also the unique one of divisibility $2$ in $\tdp$.** $\div_{\tdp}(\eta_2) = 2$ while $\div_{\tdp}(\eta_k) = 1$ for $k = 3,4,5$, so cusp $2$ alone maps to the $(18,0,0)_1$ cusp of $\bbcpt{\fttz}$ and cusps $3$, $4$, $5$ to $(18,2,0)_1$ ([@AEGS25, §3.1, printed p. 589; Lem. 3.2, printed p. 590; §3.8 with Lems. 3.9--3.10, printed pp. 594--595]).
   Its vector is $\eta_2 = e' = v_1$ of @lem:divisibilityTcoOne, the $U(2)$ generator of $T_\Co$.
5. **The check proposed for the old form of the claim tests nothing.** All of cusps $2$ to $5$ have $\Gamma(\mcz_0) = \Dc^2$ (@ex:fen2_five_cusps, from [@AEGS25, §3.2, printed p. 590]), so every Coble $0$-cusp is of $\Dc^2$-type; cusp $1$, the only $\RP^2$-type cusp, carries none by (1). The $\Dc^2$-type consistency check is a consequence of divisibility $2$ in $\ten$ and of (1), and it cannot distinguish cusp $2$ from cusps $3$, $4$, $5$.
:::

::: {.proof}

Items (1), (2) and (4), and the wall counts of (3), are the record `computations/reports/coble_672-zero-cusp-sterk-two-run.txt`: it reads the five cusp vectors back from the transcript of @prop:facet-angles-aegs and computes, in exact integer and rational arithmetic, the pairings with $\delta$, the squares, the primitivity, the divisibilities in $\ten$ and in $\tdp$, and the quotient lattices $\eta_k^{\perp T_\Co}/\ZZ\eta_k$ with their invariant factors and invariants $(r,a,\delta)$.
There $\delta^2 = -2$ and $\div_{\ten}(\delta) = 1$; $T_\Co = \delta^{\perp\ten}$ is of rank $11$, determinant $-2048$ and signature $(2,9)$.

For (2), the quotient $\eta_k^{\perp T_\Co}/\ZZ\eta_k$ is computed as the orthogonal complement of $\eta_k$ in $T_\Co$ modulo the line, with the basis obtained by completing $\eta_k$ to a unimodular basis; its invariants are $(9,9,1)$ at each of the four cusps, so by @thm:two-elementary-classification, whose uniqueness clause is [@Nik80, Thm. 3.6.2, printed p. 144], the four boundary lattices are one lattice $(9,9,1)_1$.
That each is a $0$-cusp of $F_{\Co,2}$ over the cusp named by the same vector is @lem:cusp-map-of-a-period-lattice-embedding applied to $\bD(T_\Co)\subset\bD(\ten)$.

For (3), write $\bar\alpha = \alpha + \tfrac12(\alpha,\delta)\delta$ for the projection to $\delta^\perp$; it preserves squares because $\delta^2 = -2$, so of the projected roots of the cusp-$2$ diagram the eight orthogonal to $\delta$ keep square $-4$ and the one with $(\alpha,\delta) = 2$, the printed root $r_9$, becomes the vector $r_9+\delta$ of square $-4+2\cdot2-2 = -2$.
The record prints the labelled graphs of both sides: the Coble chamber's adjacency table, as in @thm:coble-cusp-chamber ([@AN06, Table 1, entry $N = 10$, printed p. 52]), and the facet at cusp $2$, agree edge by edge and vertex by vertex, and the restricted chambers at cusps $3$, $4$ and $5$ have $10$, $10$ and $11$ distinct walls after the induced parallel pairs are identified, the numbers printed beside their bond lists in `computations/reports/coble_pair-semifan-cusps-run.txt`.

For (4), the divisibilities are those of @ex:sterk-isotropic-divisibilities, recomputed in the record, and the two $0$-cusps of $\bbcpt{\fttz}$ are distinguished by $\div_{\tdp}\in\theset{1,2}$ [@AEGS25, §3.1, printed p. 589], while the map on $0$-cusps of $\fentwo\to\fttz$ reads off those divisibilities [@AEGS25, Lem. 3.2 and its proof, printed p. 590].

For (5), $\Gamma(\mcz_0)$ at each of cusps $2$ to $5$ is $\Dc^2$ and at cusp $1$ is $\RP^2$ (@ex:fen2_five_cusps, from [@AEGS25, §3.2, printed p. 590]), and by (1) and (2) the Coble $0$-cusps are exactly those over cusps $2$ to $5$.
:::

::: {.remark #rmk:coble-zero-cusp-sterk-two title="What the earlier form of this page asserted, and what settles it"}

The claim used to stand here as a conjecture, on the strength of the $\Dc^2$-type check: cusp $1$ of $\fentwo$ is $\RP^2$-type and cusps $2$ to $5$ are $\Dc^2$-type, while Coble degenerations were asserted to be $\Dc^2$-type. Item (5) of @thm:coble-zero-cusp-sterk-two removes the check: it is satisfied by all four Coble $0$-cusps, and what it can see is already excluded by the divisibility $2$ in $\ten$ (@prop:cusp-map-not-onto).
What the claim got right is item (4): the Coble lattice's own isotropic generator $e'$ is Sterk's cusp-$2$ vector, and cusp $2$ is the unique one of the five whose image in $\bbcpt{\fttz}$ is the $(18,0,0)_1$ cusp.
What it got wrong is the uniqueness: the boundary lattice is $(9,9,1)_1$ at all four of cusps $2$ to $5$, and the only invariant that separates cusp $2$ from cusps $3$, $4$, $5$ at $\fentwo$ itself is the chamber, item (3).
:::

## Terminal Coble surfaces

::: {.definition title="Terminal"}

A Coble surface is **terminal** when it is not the image of any birational but not biregular morphism from another Coble surface.
The $n=1$ case, the blowup of a plane sextic at $N=10$ ordinary double points (some possibly infinitely near), is terminal.
:::
