---
unit: research-program
status: proved
tags:
  - coble
  - cusps
  - baily-borel
  - morphisms
---

# The Coble cusp correspondence and the morphism chain {#sec-cusp-correspondence-morphism-chain}

## The chain of morphisms

::: {.proposition #prop:fen2-forgetful-maps title="The two morphisms out of $\fentwo$"}

Let $\fttz=\bD(\tdp)/\Gamma_\dP$ be the moduli space of K3 surfaces of degree $4$ with a del Pezzo involution [@AEGS25, §1, Def. 2.7, printed p. 587].

1. The inclusion $\bD(T_\En)\subset\bD(\tdp)$ induces a finite, generically injective morphism $\fentwo\to\fttz$, and $\fentwo$ is the normalization of a closed subvariety of $\fttz$ [@AEGS25, Lemma 2.8, printed p. 587].
2. The inclusion $\gent\subseteq\Gamma^K_\En$ of a subgroup of finite index induces a morphism $\fentwo\to F_{(10,10,0)}=\bD(T_\En)/\Gamma^K_\En$ of degree $2^7\cdot17\cdot31$ [@AEGS25, §2.3; @Ste91, Rem. 2.12, printed p. 8].
:::

::: {#cons:coble-embedding-extensions .construction title="The embedding and its two extensions" defines="$\eta$; $\tilde\eta$"}

By @lem:locally_closed_embedding_BB, the lattice embeddings $T_\Co\injects\ten$ and $T_\Co\injects\tdp$ induce locally closed embeddings $\fco\injects\fen$ and $\fco\injects\fttz$, which extend to morphisms of Baily--Borel compactifications:
$$
\eta: \bbcpt{\fco} \to \bbcpt{\fen},
\qquad
\tilde\eta: \bbcpt{\fco} \to \bbcpt{\fttz} .
$$
The stratification of $\partial\bbcpt{F^{\mathrm{un}}_\Co}$ is obtained by applying the mirror moves (@def:mirror-move) of [@AE22] to $S_{\Co} = (11,11,1)_1$.
On $0$-cusps, $\eta$ induces an injective map from the $527$ $0$-cusps of the stable quotient $\bD(T_\Co)/\widetilde\Orth^+(T_\Co)$ (@thm:coble-zero-cusp-count(2), the cusps being the nonzero isotropic classes, the fibre over one class being a single $\widetilde\Orth^+(T_\Co)$-orbit by @thm:coble-integral-lifting-fibre(1), (2)) to the $0$-cusps of $\fen$ of divisibility $2$: the orbit map is defined because the embedding is equivariant, $\eta(\varphi v) = \mathrm{Ext}(\varphi)\eta(v)$ (@thm:coble-strong-lifting); it is injective (@prop:cusp-map-injective) and it misses the divisibility-$1$ cusps (@prop:cusp-map-not-onto).
:::

## The two cusp identifications

::: {.proposition #prop:fen2-zero-cusp-lattices title="The lattices of the five $0$-cusps of $\fentwo$"}

Let $e\in\ten$ be a primitive isotropic vector, and number the $0$-cusps of $\fentwo$ as in [@Ste91].

1. The lattice $e^{\perp}/e$ is $U(2)\oplus E_8(2)=(10,10,0)_1$ when $e$ represents cusp $1$, and $U\oplus E_8(2)=(10,8,0)_1$ when $e$ represents one of cusps $2$ to $5$ [@AEGS25, Lemmas 3.9, 3.10, printed p. 594].
2. The Coxeter--Vinberg diagram (@def:coxeter-vinberg-diagram) of cusp $2$ is the folding of the Coxeter--Vinberg diagram of $(18,0,0)_1$ by the reflection $\alpha_k\mapsto\alpha_{20-k}$ [@AEGS25, Lemma 3.9, printed p. 594]. The Coxeter--Vinberg diagrams of cusps $1$, $3$, $4$ and $5$ are foldings of the Coxeter--Vinberg diagram of $(18,2,0)_1$ [@AEGS25, Lemma 3.10, printed p. 594].
:::

::: {.corollary #cor:coble-zero-cusp-over-sterk-two-to-five title="The $0$-cusps of $\fentwo$ over the $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$"}

Every $0$-cusp of $\fentwo$ over the image in $F^K_\En$ of the $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$ is one of cusps $2$ to $5$. The reduced dual complex $\Gamma(\mcz_0)$ of each of these cusps is the disc $\Dc^2$.
:::

::: {.proof}

The morphism $\fentwo\to F^K_\En$ of @prop:fen2-forgetful-maps sends the $0$-cusp of a primitive isotropic vector $e\in\ten$ to the $0$-cusp of the same vector $e$, so it preserves the lattice $e^{\perp}/e$. By @lem:w1_perp_calculation the image of $(9,9,1)_1$ is the $0$-cusp $(10,8,0)_1$ of $F^K_\En$. By @prop:fen2-zero-cusp-lattices the cusps of $\fentwo$ with $e^{\perp}/e=(10,8,0)_1$ are cusps $2$ to $5$. Their dual complexes are listed in @ex:fen2_five_cusps.
:::

::: {.lemma #lem:cusp-map-of-a-period-lattice-embedding title="The $0$-cusp of an isotropic line is the point that line names, and it is functorial"}

Let $\iota\colon T\injects T'$ be a primitive embedding of even lattices of signature $(2,n)$ and $(2,n')$ with $n,n'\geq1$, let $v\in T$ be primitive isotropic and $\ell=\ZZ v$. Let $\Gamma\subseteq\Orth^+(T)$ and $\Gamma'\subseteq\Orth^+(T')$ be arithmetic subgroups such that $\iota$ is $\Gamma$-equivariant for a homomorphism $\varphi\colon\Gamma\to\Gamma'$ and such that the induced morphism $\bD(T)/\Gamma\to\bD(T')/\Gamma'$ extends to a morphism $\Phi$ of Baily--Borel compactifications.

1. The boundary component of $\bD(T)$ attached to $\ell$ is the singleton $\{[\ell]\}$ of $\PP(T_\CC)$.
2. $\Phi$ carries the $0$-cusp $[\ell]$ of $\bD(T)/\Gamma$ to the $0$-cusp $[\iota(\ell)]$ of $\bD(T')/\Gamma'$.
:::

::: {.proof}

Choose $u\in T_\QQ$ with $(v,u)=1$, possible because $v\neq0$ and the form is nondegenerate over $\QQ$, and put $K=\generators{v,u}^{\perp T_\QQ}$ and $K'=\generators{\iota v,\iota u}^{\perp T'_\QQ}$. Then $K$ has signature $(1,n-1)$, $K'$ has signature $(1,n'-1)$ and $K\subset K'$. By @cons:hsd-tube-coordinates, applied to the hyperbolic plane $\generators{v,u}$,
$$\bD(T)=\{z\in K_\CC:\operatorname{Im}z\in C\},\qquad \bD(T')=\{z\in K'_\CC:\operatorname{Im}z\in C'\},$$
where $C$ is a component of $\{y\in K_\RR:y^2>0\}$ and $C'$ is a component of $\{y\in K'_\RR:y^2>0\}$ chosen so that $C=C'\intersect K_\RR$; the period of $z=x+iy$ is $[w(z)]$ with $w(z)=u+z-\tfrac12(z,z)v$. The projection $K\to\ell^{\perp T_\QQ}/\QQ v$ is an isomorphism, so $K$ is the cusp cone of $[\ell]$ in the sense of @rmk:hsd-toroidal and $C$ is one of its two positive cones.

For $y_0\in C$ and $t>0$ put $z_t=i t y_0$. Then $w(z_t)=u+i t y_0+\tfrac12t^2y_0^2\,v$, so $[w(z_t)]\to[v]$ in $\PP(T_\CC)$ as $t\to\infty$. The points $w(z_t)$ lie, for $t$ large, in a Siegel domain at $[\ell]$ and in one at $[\iota(\ell)]$, since $\operatorname{Im}z_t=t y_0\in C\subset C'$ and $(t y_0,w)\to\infty$ for $w$ in the interior of the cone; by [@BB66, Lemma 4.7, printed p. 481; §4.8, printed p. 482] they lie in the closure of a fundamental set for $\Gamma$, respectively for $\Gamma'$, and by [@BB66, Thm. 4.9(i), printed p. 482; Prop. 4.10, printed p. 483] the Satake topology agrees with the natural topology on that closure. Hence the images of $w(z_t)$ converge to the $0$-cusp $[\ell]$ in $\bbcpt{\bD(T)/\Gamma}$ and to the $0$-cusp $[\iota(\ell)]$ in $\bbcpt{\bD(T')/\Gamma'}$.

By [@Ste91, §4.1, printed p. 15] the boundary components of $\bD(T)$ are the sets $F_I=\PP(I_\CC)\intersect\overline{\bD(T)}$ for the nonzero isotropic subspaces $I\subset T_\RR$, and $F_I$ is a singleton when $\dim I=1$; by [@Ste91, §4.2, printed p. 15] and [@AEGS25, Def. 2.9, printed p. 588] the zero-dimensional boundary components of $\bD(T)/\Gamma$ are the $\Gamma$-orbits of primitive isotropic lines. The point $[v]$ lies in $\overline{\bD(T)}$ by the previous paragraph, so $F_\ell=\{[v]\}$: the $0$-cusp is the point that the line names. The lattice $\ell^{\perp T}/\ell$ has signature $(1,n-1)$, so it carries no positive $2$-plane at all; it is the cusp cone of the toroidal compactification at $[\ell]$ (@rmk:hsd-toroidal), not a period domain, and in particular not the boundary component.

Finally, $\Phi$ is continuous and agrees with the inclusion on the dense open $\bD(T)/\Gamma$, so
$$\Phi([\ell])=\lim_{t\to\infty}\Phi([w(z_t)])=\lim_{t\to\infty}[w(z_t)]=[\iota(\ell)].$$
:::

::: {.theorem #thm:coble-zero-cusp-sterk-two title="Which cusp of $\fentwo$ carries the Coble $0$-cusp: cusps $2$--$5$ for the boundary lattice, cusp $2$ for the chamber"}

Let $\delta = e-f$, $T_\Co = \delta^{\perp\ten}$, $R_{\gent}$ the image of $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$ (@prop:gamma-co-images(3)) and $F_{\Co,2} = \bD(T_\Co)/\Gamma_{\Co,2}$ with $\Gamma_{\Co,2}$ the monodromy group of the family of @def:coble-family-degree-two (@def:gamma-co-groups(5)), and let $\eta_1,\dots,\eta_5$ be Sterk's five cusp vectors in $\ten = U\oplus U(2)\oplus E_8(2)$, that is the vectors the lattice database returns as `Sterk.selected_isotropic_vectors()` [@Ste91, (4.2.2)--(4.2.3), printed p. 16], whose coordinates and divisibilities are tabulated in @ex:sterk-isotropic-divisibilities.
Then:

1. **Cusp $1$ carries no Coble $0$-cusp.** $(\eta_1,\delta) = -1$, so $\eta_1\notin T_\Co$.
2. **Each of cusps $2$, $3$, $4$, $5$ carries one, and all four have the same boundary lattice.** For $k=2,3,4,5$ the vector $\eta_k$ is primitive and isotropic with $(\eta_k,\delta) = 0$ and $\div_{\ten}(\eta_k) = 2$, and the lattice $\eta_k^{\perp T_\Co}/\ZZ\eta_k$ is even of rank $9$, determinant $2^9$, signature $(1,8)$ and invariants $(r,a,\delta) = (9,9,1)$, hence is $(9,9,1)_1$ (@thm:two-elementary-classification).
   So each of Sterk's cusps $2$ to $5$ carries a $0$-cusp of $F_{\Co,2}$ with boundary lattice $(9,9,1)_1$, by @thm:coble-pair-semifan(0) and @lem:cusp-map-of-a-period-lattice-embedding; and since $\Gamma_{\Co,2}\subseteq\Orth(T_\Co)$ and $\Orth(T_\Co)$ is transitive on primitive isotropic vectors (@thm:unpolarized-cusps), the four sit over the one $0$-cusp $(9,9,1)_1$ of $F^{\mathrm{un}}_\Co$.
   **The boundary lattice therefore singles out no cusp**: the identification of the Coble $0$-cusp with cusp $2$ alone is false in this reading.
3. **The chamber singles out cusp $2$.** Restricted to $\delta^\perp$, the facet at Sterk cusp $2$ is the Coble chamber of @thm:coble-cusp-chamber: nine walls forming a tree with arms of lengths $1$, $2$ and $5$ at its branch vertex, eight walls of square $-4$ and one of square $-2$ at the end of the long arm, every bond of label $3$ except the last bond of the long arm, of label $4$.
   At cusps $3$, $4$ and $5$ the same construction gives $11$, $10$ and $13$ distinct walls, and at each of the three every one of them is a facet of the restricted chamber.
   Two cones with different numbers of facets are not isometric, so cusp $2$ is the unique cusp of $\fentwo$ whose local reflection data are the Coble $0$-cusp's, and this is the sense in which the Coble $0$-cusp is Sterk cusp $2$.
4. **Cusp $2$ is also the unique one of divisibility $2$ in $\tdp$.** $\div_{\tdp}(\eta_2) = 2$ while $\div_{\tdp}(\eta_k) = 1$ for $k = 3,4,5$, so cusp $2$ alone maps to the $(18,0,0)_1$ cusp of $\bbcpt{\fttz}$ and cusps $3$, $4$, $5$ to $(18,2,0)_1$ ([@AEGS25, §3.1, printed p. 589; Lem. 3.2, printed p. 590; §3.8 with Lems. 3.9--3.10, printed pp. 594--595]).
   Its vector is $\eta_2 = e' = v_1$ of @lem:divisibilityTcoOne, the $U(2)$ generator of $T_\Co$.
5. **The check proposed for the old form of the claim tests nothing.** All of cusps $2$ to $5$ have $\Gamma(\mcz_0) = \Dc^2$ (@ex:fen2_five_cusps, from [@AEGS25, Prop. 4.8(1)--(2), printed pp. 603--604]), so every Coble $0$-cusp is of $\Dc^2$-type; cusp $1$, the only $\RP^2$-type cusp, carries none by (1). The $\Dc^2$-type consistency check is a consequence of divisibility $2$ in $\ten$ and of (1), and it cannot distinguish cusp $2$ from cusps $3$, $4$, $5$.
:::

::: {.proof}

Items (1), (2) and (4), and the wall counts of (3), are the record `computations/reports/coble_672-zero-cusp-sterk-two-run.txt`, which works entirely in the lattice database: $T_\Co$, $\ten$ and $\tdp$ are its `NamedLattices.Tco`, `.TEn` and `.TdP`, each verified there to be isometric to the orthogonal sum of its named summands, namely $\langle2\rangle\oplus U(2)\oplus E_8(2)$, $U\oplus U(2)\oplus E_8(2)$ and $U\oplus U(2)\oplus E_8^{\oplus2}$, and the five vectors are its own `Sterk.selected_isotropic_vectors()`.
No Gram matrix is typed in the record and no linear-algebra routine is written in it; the perpendiculars, quotients, radicals, discriminant forms and isometry decisions are the library's own operations, and each conclusion below is that library's verdict.

For (1) and the divisibility of (2): $\delta^2 = -2$ and $\div_{\ten}(\delta) = 1$, and $\delta^{\perp\ten}$ — the perpendicular of the line $\ZZ\delta$ — is isometric to $T_\Co$, of rank $11$, determinant $-2048$ and signature $(2,9)$.
The pairing of $\eta_1$ with $\delta$ is $-1$, so $\eta_1$ is not a vector of $T_\Co$; for $k=2,3,4,5$ the pairing is $0$ and the divisibility ideal in $\ten$ is $2\ZZ$.

For (2): the primitive span of $\delta$ and $\eta_k$ has for its perpendicular the rank-$10$ lattice $M = T_\Co\intersect\eta_k^{\perp}$; since $\eta_k^2 = 0$ and $\eta_k\in M$, the line $\ZZ\eta_k$ is the radical of $M$, so $M/\rad M$ is $\eta_k^{\perp T_\Co}/\ZZ\eta_k$, and the library's radical quotient of $M$ returns it: rank $9$, determinant $2^9$, signature $(1,8)$, even, $2$-elementary with invariants $(9,9,1)$, and isometric to $\langle2\rangle\oplus E_8(2)$ — at each of the four cusps, so the four boundary lattices are one lattice $(9,9,1)_1$ (@thm:two-elementary-classification, whose uniqueness clause is [@Nik80, Thm. 3.6.2, printed p. 144]).
That each is a $0$-cusp of $F_{\Co,2}$ over the cusp named by the same vector is @lem:cusp-map-of-a-period-lattice-embedding applied to $\bD(T_\Co)\subset\bD(\ten)$ with $R_{\gent}\subseteq\gent$; the equivariance it asks for is the definition of $R_\gent$ as the image of $\Stab_{\gent}(\delta)$ in $\Orth(T_\Co)$ (@def:gamma-co-groups).
Cusp $4$ has two printed representatives, (4.2.3)'s and the one its chamber is drawn at [@Ste91, Fig. 10, printed p. 23]; the record runs both, and both give the boundary lattice $(9,9,1)_1$ and divisibility $1$ in $\tdp$, so no clause here depends on the choice.

For (3), the walls of the five cusp chambers are not transcribed: they are the library's `Sterk.cusp_roots_in_TEn(name)`, whose docstring cites Sterk (1991) 4.3.1 and 4.3.6--4.3.9, whose diagrams are Figs. 6, 8, 10 and 12 on printed pp. 21, 22, 23 and 24 for cusps $2$, $3$, $4$ and $5$, together with card `029J`'s `cusp_chambers` row, and they are returned as vectors of $\ten$.
Writing $\bar\alpha = \alpha + \tfrac12(\alpha,\delta)\delta$ for the projection to $\delta^\perp$ — $\delta^2 = -2$, and every printed wall pairs $0$ or $\pm2$ with $\delta$, so the projection is again a vector of $\ten$ — the library's pairing gives $\bar\alpha^2 = \alpha^2 + \tfrac12(\alpha,\delta)^2$ and $(\bar\alpha,\bar\beta) = (\alpha,\beta) + \tfrac12(\alpha,\delta)(\beta,\delta)$.
At each of the four cusps exactly one printed wall is a multiple of $\delta$, the printed $(-2)$-vector $\gamma = e-f$, up to sign, and it projects to $0$, so it is dropped; a wall orthogonal to $\delta$ keeps its square, and a wall pairing $\pm2$ with $\delta$ becomes $\alpha\pm\delta$ of square $\alpha^2+2$. At cusp $2$ this leaves the eight walls of square $-4$ and the one of square $-2$ of item (3).
`CoxeterDiagrams().from_roots` then builds the diagram of the nine projected walls, and its `coxeter_entry` matrix is printed beside the bond list of @thm:coble-cusp-chamber ([@AN06, Table 1, entry $N = 10$, printed p. 52]) handed to the same constructor: the two agree entry by entry, the library reporting both hyperbolic with form rank $9$, so cusp $2$'s facet **is** the Coble chamber.
At cusps $3$, $4$ and $5$ the same calls give $11$, $10$ and $13$ distinct walls. **Two projected walls cut the same hyperplane of $\delta^\perp$ exactly when their projections are proportional**, and that is the only identification made: the record decides it by the rank over $\mathbb{Q}$ of the pair of projected coordinate vectors, and at none of the four cusps are two projections proportional. An earlier form of this count identified the pair whenever $b(x,y)^2 = q(x)q(y)$, which over an indefinite form asserts only that the span of $x$ and $y$ is degenerate: at cusp $3$ a projected pair has $q(x) = q(y) = -2$ and $b(x,y) = 2$, and the two are linearly independent, while cusp $5$ has two such pairs, so that test merged walls that are distinct.
That each of the $11$, $10$ and $13$ walls is a facet, and not an inequality implied by the others, is the record's cone on the projected normals taken as an exact rational polyhedron, every one of whose extreme rays is one of them (`computations/reports/coble_672-zero-cusp-sterk-two-run.txt`).

For (4), the divisibility in $\tdp$ is that of the image under the library's $\ten\injects\tdp$ embedding, and its ideal is $2\ZZ$ for cusp $2$ and $\ZZ$ for cusps $1,3,4,5$; the record also reduces the image at each cusp and confirms by isometry that cusp $2$'s is $U\oplus E_8^{\oplus2}=(18,0,0)_1$ and cusps $1,3,4,5$'s are $U(2)\oplus E_8^{\oplus2}=(18,2,0)_1$.
The two $0$-cusps of $\bbcpt{\fttz}$ are distinguished by $\div_{\tdp}\in\theset{1,2}$ [@AEGS25, §3.1, printed p. 589], and the map on $0$-cusps of $\fentwo\to\fttz$ reads off those divisibilities [@AEGS25, Lem. 3.2 and its proof, printed p. 590].

For (5), $\Gamma(\mcz_0)$ at each of cusps $2$ to $5$ is $\Dc^2$ and at cusp $1$ is $\RP^2$ (@ex:fen2_five_cusps, from [@AEGS25, Prop. 4.8(1)--(2), printed pp. 603--604]), and by (1) and (2) the Coble $0$-cusps are exactly those over cusps $2$ to $5$.
:::

::: {.remark #rmk:coble-zero-cusp-sterk-two title="What the earlier form of this page asserted, and what settles it"}

The claim used to stand here as a conjecture, on the strength of the $\Dc^2$-type check: cusp $1$ of $\fentwo$ is $\RP^2$-type and cusps $2$ to $5$ are $\Dc^2$-type, while Coble degenerations were asserted to be $\Dc^2$-type. Item (5) of @thm:coble-zero-cusp-sterk-two removes the check: it is satisfied by all four Coble $0$-cusps, and what it can see is already excluded by the divisibility $2$ in $\ten$ (@prop:cusp-map-not-onto).
What the claim got right is item (4): the Coble lattice's own isotropic generator $e'$ is Sterk's cusp-$2$ vector, and cusp $2$ is the unique one of the five whose image in $\bbcpt{\fttz}$ is the $(18,0,0)_1$ cusp.
The proof of @lem:cusp-map-of-a-period-lattice-embedding was rewritten as well: an earlier form identified the boundary component of an isotropic line $\ell$ with the period domain $\bD(\ell^{\perp}/\ell)$, but $\ell^{\perp}/\ell$ has signature $(1,n-1)$, so that $\bD(\ell^{\perp}/\ell)$ is empty, and it is the cusp cone of the toroidal compactification at the cusps it names (@rmk:hsd-toroidal), while the Baily--Borel component is the point $[\ell]$ itself ([@Ste91, §4.1, printed p. 15]).
What it got wrong is the uniqueness: the boundary lattice is $(9,9,1)_1$ at all four of cusps $2$ to $5$, and the only invariant that separates cusp $2$ from cusps $3$, $4$, $5$ at $\fentwo$ itself is the chamber, item (3), where the numbers of distinct walls at cusps $2$, $3$, $4$ and $5$ are $9$, $11$, $10$ and $13$ — a count of wall hyperplanes, decided by proportionality of the projected normals.
:::

## Terminal Coble surfaces

::: {#def:terminal-coble-surface .definition title="Terminal" defines="terminal"}

A Coble surface (@def:coble-surface) is **terminal** when it is not the image of any birational but not biregular morphism from another Coble surface.
The $n=1$ case, the blowup of a plane sextic at $N=10$ ordinary double points (some possibly infinitely near), is terminal.
:::
