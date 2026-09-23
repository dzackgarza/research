# Constructions of the moduli space

We summarize the relevant moduli spaces:

$$
\begin{aligned}
F_\En &= \bD(T_\En)/\Orth^+(T_\En)^* &
\fent &= \bD(T_\En)/\Gamma_{\En, 2} \\
F_\Co &= \bD(T_\Co) / \Orth^+(T_\Co)^* &
F_{\Co, 2} &= \bD(T_\Co)/\Gamma_{\Co, 2}
\end{aligned}
$$

where

$$
\begin{aligned}
\Gamma_{\En, 2} &= \Orth(T_\En) \intersect \Orth(\tdp) \containedin \Orth(\lkt) \\
\Gamma_{\Co, 2} &= \mathrm{Stab}_{\Orth(T_\En)}(T_\Co) \containedin \Orth(T_\En) \\
F_{\Nod} &= \bD(T_\Nod)/\Orth^+(T_\Nod)^* \\
F_{\Nod, 2} &= ???
\end{aligned}
$$

where $\tdp$ is described in [@AEGS25]. Note that we implicitly use the embedding $\eta: T_\Co \injects T_\En$ of [the primitive-embedding lemma](#lem:primitive_embedding_eta).

::: {.Question}
Degree 2 polarized Coble surfaces do not seem to appear in previous literature, merely (unpolarized?) Cobles with $n$ boundary components. So I can not yet determine a more explicit description of $\Gamma_{\Co, 2}$.
:::

We note, as in [@DK13], that $T_{\Co} \cong v^{\perp \ten}$ for some $v^2=-2$, which implies that there is a birational isomorphism $\fco \birational \cH_{-2}/\Orth^+(\ten)^*$.

```{.tikz}
%%| filename: moduli-tower
%%| additionalPackages: \usepackage{amsmath,amssymb,tikz-cd}
\begin{tikzcd}[column sep=large, row sep=large]
F_{\mathrm{Co},2}
  \arrow[r]
  \arrow[d, "?"'] &
F_{\mathrm{En},2}
  \arrow[r]
  \arrow[d] &
F_{(2,2,0)}
  \arrow[r, hook] &
F_4 \\
F_{\mathrm{Co}}
  \arrow[r] &
F_{\mathrm{En}}
\end{tikzcd}
```

The tower relates the degree-$2$ numerically polarized Coble and Enriques moduli
$F_{\Co,2}$, $\fentwo$, their unpolarized quotients $\fco$, $F_\En$, and the
degree-$(2,2,0)$ K3 moduli space $F_{(2,2,0)}\injects F_4$.
The map $F_{\Co,2}\to F_\Co$ marked $?$ is the one not yet determined, for the reason
above: $\Gamma_{\Co,2}$ has no explicit description.



## The GIT construction

::: {.Remark}
### GIT construction

Following [@DK13], by varying the coefficients of $p_i$ in the planar blowup
construction, one can construct $F_\Co$ as a locally closed subvariety of
$(\PP^2)^{10}/\PGL_3$, which is of dimension

$$
\dim (\PP^2)^{10}/\PGL_3 = \dim (\PP^2)^{10} - \dim \PGL_3 = 2\cdot 10 - (3^2-1) = 12
.
$$

A posteriori, the number of moduli for a Coble surface is 9, which
means that there should be 3 conditions imposed upon the configuration
of 10 points.
These 3 conditions are precisely the _discriminant
conditions_ described in [@Cob19 §2, Prop. (10)].
Letting $D$ be the corresponding discriminant locus, we can identify $\fco$
as an open subset of $\qty{ (\PP^2)^{10} \sm D }/\PGL_3$ at the level of coarse
moduli spaces.
:::

## The Horikawa model

::: {.Remark}
### Horikawa's construction

Alternatively, Horikawa [@Hor77] and more recently [@AEGS25] consider
the following: let $Y\da \PP^1\times \PP^1$ and define an involution
$\tau(x,y) \da (-x,-y)$.
Letting $B\in\abs{-2K_Y}^\tau$ be a
$\tau$-invariant anti-bicanonical curve in $Y$, if $B$ passes through a
$\tau$-fixed point $x,y\in \ts{0, \pm \infty}$, then the corresponding
double branched cover branched over $B$ is a nodal K3 surface $X$ with $A_1$
singularities and covering involution $\idp$ such that
$Y = X/\gens{\idp}$.
Letting $\ien$ be a lift of $\tau$, the quotient
$Z\da X/\gens{\ien}$ is a Coble surface.
The case in which $B$ does not
pass through a $\tau$-invariant point yields an Enriques surface $Z$,
and an analysis of the corresponding moduli is carried out in [@AEGS25].

It is well-known that there consequently exists a Coble surface $S$ and
a blowdown $S\to X/\iota$ along the strict transform of $B$.
In this
way, one realizes the moduli space $\fco$ of unpolarized Coble
surfaces as a divisor in $\fen$, the 10-dimensional moduli space of
unpolarized Enriques surfaces.
:::

## Period domains

By passing to the K3 cover, one can embed $F_\Co$ into an arithmetic quotient of a 9-dimensional Hermitian symmetric domain of type $\rm{IV}$.
Let $\lkt = U^3 \oplus E_8^2$ be the canonical K3 lattice.
We recall that for any primitively embedded lattice $S\injects \lkt$, letting $T \da S^{\perp \lkt}$, there is a Hodge-theoretic description of the coarse moduli space $F_S$ of $S$-polarized K3 surfaces given by $$F_S \da D_T/\Orth^+(T)^*$$

where $\Orth^+(T)^* \da \Orth^+(T) \intersect \ker\qty{\Orth(T) \to \Orth(q_T)}$, the group $\Orth^+(T)$ is the index-two subgroup of $\Orth(T)$ preserving the component $D_T$, and $D_T$ is a connected component of

$$
\Omega_T \da \ts{[v]\in \PP(T_\CC) \st v^2=0,\, v\bar v > 0}
.
$$

::: {.Proposition #prop:type-iv-dimension}
### Dimension of a type IV domain

Let $T$ be a lattice of rank $r$ and signature $(2, r-2)$.
Then the type IV domain $D_T$ has complex dimension $r - 2$.
:::

::: {.proof}

The complexification $T_\CC$ has dimension $r$, so $\PP(T_\CC)$ has dimension
$r-1$.
The equation $v^2 = 0$ is a single nondegenerate quadratic equation and cuts out a
smooth quadric hypersurface of dimension $r-2$ inside $\PP(T_\CC)$.
The condition $v\bar v > 0$ is open, so it selects an open subset of that quadric,
and $D_T$ is one of its connected components.
:::

::: {.Corollary #cor:m-polarized-k3-dimension}
### Dimension of $M$-polarized K3 moduli

Let $M\injects\lkt$ be a primitive embedding of a lattice of signature
$(1, \rank(M) - 1)$ with orthogonal complement
$T = M^{\perp\lkt}$.
Then
$$
\dim_\CC D_T = \rank(T) - 2 = 20 - \rank(M)
.
$$
For the Coble lattices $\rank(S_\Co) = 11$, so
$\dim_\CC D_{T_\Co} = 9$.
:::

::: {.proof}

The K3 lattice has rank $22$, so $\rank(T) = 22 - \rank(M)$,
and $T$ has signature $(2, 20 - \rank(M))$; apply
[the type-IV dimension proposition](#prop:type-iv-dimension).
:::

Letting $E_{10} \da U \oplus E_8$, one can similarly consider the Enriques lattices $S_\En := E_{10}(2)$ with $T_\En = U \oplus E_{10}(2)$.
Letting

$$
\cH_{-2d} = \Union_{\delta^2 = -2d} \delta^{\perp D_T}
,
$$

be the union of the hyperplane sections cut out by the vectors $\delta$ of norm
$-2d$, as in @fig-period-domain-hyperplanes, one can thus present

$$
\begin{aligned}
\fen &= \qty{D_{T_\En} \sm \cH_{-2}} / \Orth^+(T_\En)^* \\
\fco &= \cH_{-2} / \Orth^+(T_\En)^* \\
F_{\Nod} &= \qty{\cH_{-4} \sm \cH_{-2}} / \Orth^+(T_\En)^*
\end{aligned}
$$

where surfaces along the divisor $\cH_{-2}$ in $\fen$ correspond precisely to Coble surfaces and those along $\cH_{-4}\sm \cH_{-2}$ correspond to Enriques surfaces with $A_1$ singularities.

::: {#fig-period-domain-hyperplanes .figure}
\input{tikz/fig_type_iv_hsd.tex}

The period domain $D_{T_\En}$ together with the hyperplanes $v_i^{\perp}$ cut out by vectors $v_i$ of fixed negative norm. The Coble surfaces are precisely the periods lying on the hyperplanes of $\cH_{-2}$.
:::

Alternatively, one can construct the period domain for $F_\Co$ directly.
Following [@DK13 Prop. 3.1] almost verbatim, let $S$ be the blowup of $\PP^2$ along 10 $A_1$ singularities of a rational sextic curve $C$.
The double branched cover $f:X\to S$ branched along the proper transform of $C$ contains the pullback of ten exceptional classes $E_1,\cdots, E_{10}$ over the ten $A_1$ singularities, as well as $E_0$, the pullback of a hyperplane class.
Since $E_i^2 = -2$ for $1\leq i \leq 10$, and one can show that $E_0^2 = 2$, the $E_i$ generate a lattice isometric to

$$
S_\Co \da \gens{2}\oplus \gens{-2}^{10} = \latI_{1, 10}(2) = (11, 11, 1)_1 \cong \gens{-2} \oplus E_{10}(2)
.
$$

This follows from the fact that $S_{\Co}$ is a 2-elementary lattice of signature $(1, 10)$ with discriminant group $(\bZ/2\bZ)^{11}$ and thus uniquely determined up to isometry by its invariants $(r,a,\delta)$.
Similarly, its orthogonal complement $T_{\Co}$ in the K3 lattice $\lkt$ is a 2-elementary lattice of signature $(2, 9)$ and satisfies $q_{S_{\Co}} = -q_{T_{\Co}}$.
The isomorphism class of $q_{T_{\Co}}$ determines $T_\Co$, and thus one has

$$
T_\Co \da S_\Co^{\perp \lkt} = (11, 11, 1)_2 \cong \gens{2} \oplus E_{10}(2)
.
$$

Alternatively, this follows immediately from the mirror move $S\leadsto T$ of [@AE22 Thm. 5.10] applied to $S_\Co =(11, 11, 1)_1$.
We obtain $F_\Co$ as an open subset of the period domain $D_{T_\Co}/\Orth^+(T_\Co)^*$, a normal quasiprojective variety of dimension 9, by [@DK13 Prop. 3.2] and an application of the Torelli theorem for algebraic K3 surfaces from [@PS71]. We note that [@DK13] shows that $F_\Co$ is rational by relating it to a codimension one subvariety of a moduli space of certain $A_2$-singular quintics in $\PP^2$.

## The sextic moduli construction

::: {.Remark}
### Orientation

The constructions above start from the surface: from the Coble surface $S$ and
its K3 cover, or from the Enriques period domain in which the Coble locus is a
Heegner divisor.
A third route starts from the *branch curve* and never mentions $S$: one takes the
moduli space of plane sextics of a fixed singularity type, and maps it to an
arithmetic quotient by the periods of the associated K3.
Yu--Zheng--Zhong carry this out for every singular type $T$ of plane sextic with
simple singularities [@YZZ25], and the Coble case is the type $T = 10A_1$.
What this route supplies that the two above do not is a compactification of the
open moduli space by geometry of the curves, namely the geometric invariant theory
quotient, together with an identification of that compactification in arithmetic
terms.
:::

::: {.Notation #not:sextic-singular-type}
### Moduli of sextics of a fixed singular type

For a singular type $T$ with root lattice $R$, write $\cV_T$ for the space of
sextic curves $Z\subset\PP^2$ with singularities exactly of type $T$, and
$$
\cM_T \da \PP\cV_T \modmod \SL_3
$$
for the moduli space of such curves, the quotient being taken in the sense of
geometric invariant theory [@YZZ25 §2.1].
Let $\wh X$ be the double cover of $\PP^2$ branched along $Z$, let $X$ be its
minimal resolution --- a K3 surface --- and let $H\in\Pic(X)$ be the pullback of
the line class, so $H^2 = 2$.
The exceptional curves of $X\to\wh X$ span a copy $L\containedin\Pic(X)$ of the
root lattice $R$, with the exceptional classes as a base $\Delta$.
Write $P$ for the primitive hull of $\gens H\oplus L$ in $H^2(X;\ZZ)$ and
$Q \da P^{\perp}$, of signatures $(1,\rank R)$ and $(2, 19 - \rank R)$
[@YZZ25 §2.3].
For a general member of $\cV_T$ one has $\Pic(X) = P$ [@YZZ25 §3.3].
:::

::: {.Proposition #prop:coble-is-the-ten-nodal-sextic-type}
### The Coble lattices are the lattices of the type $10A_1$

Let $Z$ be an irreducible sextic of type $T = 10A_1$, so that $Z$ is rational by
[the ten-nodal-sextic lemma](#lem:rational_sextic_ten_nodes), and $X$ is the K3 cover of the Coble
surface $S = X/\iota$.
Then
$$
P = \gens{H}\oplus A_1^{\oplus 10} \cong \latI_{1,10}(2) = S_\Co,
\qquad
Q = P^{\perp\lkt} = T_\Co
.
$$
In particular $\dim D(Q) = 9$.
:::

::: {.proof}

The saturation of $\gens H\oplus L$ inside $H^2(X;\ZZ)$ is
$(\ZZ/2)^{l'-1}$, where $l'$ is the number of irreducible components of $Z$
[@YZZ25 §5.3]; for an irreducible sextic $l' = 1$, so no saturation occurs and
$P = \gens H\oplus L$.
With $H^2 = 2$ and $L = A_1^{\oplus 10} = \gens{-2}^{\oplus 10}$ this is
$\gens 2\oplus\gens{-2}^{\oplus 10} = \latI_{1,10}(2)$, which is $S_\Co$ by
[the Coble invariant-lattice proposition](#prop:coble-invariant-lattice).
Taking orthogonal complements in $\lkt$ gives $Q = T_\Co$, and
[the polarized-K3 dimension corollary](#cor:m-polarized-k3-dimension) gives the dimension.
:::

::: {.Remark}
### The involution acts trivially on the root lattice

For a general singular type the covering involution $\iota$ acts on $L$ by
$-w_0(L)$, where $w_0$ is the longest element of $W(L)$ [@YZZ25 §5.2], and this
action folds the root lattice.
For $L$ of type $A_1$ one has $-w_0 = \id$, so in the type $10A_1$ the involution
fixes $L$ pointwise and no folding occurs; the sublattice of $H^2(S;\ZZ)$ spanned
by the exceptional classes of $S\to\PP^2$ then becomes $L$ after scaling by $2$
[@YZZ25 §5.3].
That is the same twist by $2$ recorded geometrically in
[the K3-cover twist remark](#rmk:k3-cover-twist): the Coble Picard lattice is the blowup lattice
$\latI_{1,10}$ scaled by $2$, with no folding correction.
:::

::: {.Theorem #thm:occult-period-map-sextics}
### The occult period map and its image

Let $\Gamma_T$ be the image of
$$
\Orth\bigl(H^2(X;\ZZ),\, \Delta,\, H\bigr) \too \Orth(Q)
,
$$
restricted to the subgroup preserving a chosen component $D(Q)$; it is arithmetic
of finite index in $\Orth(Q)$, and contains every isometry of $Q$ acting trivially
on $A_Q$ [@YZZ25 §3.1].
The **occult period map**
$$
\mathscr P_T\colon \cM_T \too \Gamma_T\backslash D(Q)
$$
is an algebraic open embedding with image
$\Gamma_T\backslash\bigl(D(Q) - \cH_T\bigr)$, where $\cH_T$ is the arrangement of
hyperplanes $r^{\perp}$ for roots $r$ orthogonal to $H$ and not lying in $L$.
When $T$ is a nodal type, $\mathscr P_T$ is moreover an isomorphism of orbifolds
onto $P\Gamma_T\backslash(D(Q) - \cH_T)$
[@YZZ25 §1, §3.2, §3.3, §6.2].
The description of the image restates, at the level of moduli spaces, the
equisingular deformation theory of Urabe [@Ura88].
:::

::: {.Theorem #thm:git-equals-looijenga}
### The GIT compactification is a Looijenga compactification

Let $\Lambda_1 \da H^{\perp\lkt}$, of signature $(2,19)$ with
$A_{\Lambda_1}\cong\ZZ/2$, and let $\Gamma_1$ be the arithmetic group of the
degree-$2$ K3 moduli space $\Gamma_1\backslash D(\Lambda_1)$.
The roots of $\Lambda_1$ fall into two $\Gamma_1$-orbits, of divisibility $1$ and
$2$, cutting out arrangements $\cH_\Delta$ and $\cH_\infty$; the roots of $L$ all
have divisibility $1$, so they contribute to $\cH_\Delta$ only [@YZZ25 §4.1, §4.2].
Set
$$
\cH^{*}_T \da \cH_\infty \intersect D(Q) \containedin \cH_T
.
$$
Then $\mathscr P_T$ extends to an isomorphism
$$
\wh{\cM}_T \;\cong\; \overline{\Gamma_T\backslash D(Q)}^{\,\cH^{*}_T}
$$
between the GIT compactification of $\cM_T$ and the Looijenga compactification
([the Looijenga-compactification definition](#def:looijenga-compactification)) of
$\Gamma_T\backslash(D(Q) - \cH^{*}_T)$, compatibly with the corresponding
statement of Shah and Looijenga for the whole space of sextics,
$\overline{\cM}\cong\overline{\Gamma_1\backslash D(\Lambda_1)}^{\,\cH_\infty}$
[@Sha80; @Loo02]; the two vertical maps of the resulting square are
normalizations onto their images [@YZZ25 §4.2].
:::

::: {.Remark}
### The arithmetic group as a normalizer

$\Gamma_T$ admits a second description: it is the restriction to $Q$ of the
normalizer of the Weyl group $W(L)$ inside $\Gamma_1$ [@YZZ25 §4.2].
For $T = 10A_1$ this reads
$$
W(L) = \ts{\pm 1}^{10},
\qquad
\Gamma_{10A_1} = \Gamma_W|_{Q},
\qquad
\Gamma_W = N_{\Gamma_1}\bigl(\ts{\pm1}^{10}\bigr)
,
$$
and the normalizer contains the permutations of the ten nodes, so the induced
action on $A_P\cong(\ZZ/2)^{11}$ is through $\mathfrak S_{10}$.
This is a description of an arithmetic group acting on $D(T_\Co)$ obtained from
the ambient degree-$2$ K3 group rather than from the Enriques side, and it is
therefore independent of the description of $\Gamma_\Co$ as a stabilizer and
centralizer inside $\Orth(T_\En)$ recorded in the Open Problems section.
:::

::: {.Question #que:sextic-group-comparison}
### Which quotient of $D(T_\Co)$ is $F_\Co$?

$F_\Co$ is defined above as an open subset of $D(T_\Co)/\Orth^+(T_\Co)^*$, a
quotient by the stable orthogonal group, whereas $\cM_{10A_1}$ is a quotient by
$\Gamma_{10A_1}$, which contains $\Orth^+(T_\Co)^*$ and may be strictly larger.
Identifying the two constructions of the Coble moduli space therefore requires the
comparison
$$
\Orth^+(T_\Co)^* \;\containedin\; \Gamma_{10A_1} \;\containedin\; \Orth(T_\Co)
,
$$
together with the comparison of both against the polarized group
$\Gamma_{\Co,2}$.
Until the first inclusion is shown to be an equality, $\cM_{10A_1}$ and $F_\Co$ are
two arithmetic quotients of the same period domain by two different groups, not
the same space under two names.
:::

::: {.Remark}
### The other singular types

The same theorems hold for every singular type of plane sextic with simple
singularities, of which the root lattices have been classified by Urabe
[@Ura88] and Yang [@Yan96]: the maximal rank is $19$, and the number of root
lattices of rank $19$, $18$, $17$, $16$ is $519$, $987$, $975$, $782$
respectively [@YZZ25 §1].
Each such type therefore carries both an arithmetic model of its moduli space and
a Looijenga model of its GIT compactification.
The Coble families with $n$ boundary components are indexed by the number of
irreducible components of the branch sextic ([the Coble lattice table](coble-lattice-table.md)) rather
than by its singular type, so which type $T$ carries which family is a question
this section does not settle.
:::

## KSBA spaces

::: {.Remark}

By [the Baily--Borel extension lemma](#lem:locally_closed_embedding_BB), there are morphisms
$\overline{\fco}^{\bb} \to \overline{\fen}^{\bb}$ and
$\overline{\fco}^{\bb} \to \overline{F_{(2,2,0)}}^{\bb}$ which induce
correspondences between the boundary cusps.
:::

::: {.Remark}

We set up the moduli space of KSBA stable pairs for Coble surfaces, possibly
using the ramification divisor of the K3 involution (which is in this case not
fixed-point free).
The above embeddings should allow us to take closures of stable pairs in
already existing moduli spaces.
:::
