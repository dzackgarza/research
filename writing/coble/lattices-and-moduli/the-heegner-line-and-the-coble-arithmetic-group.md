# The Heegner line and the Coble arithmetic group {#sec:heegner-line}

::: {.Remark}

The Coble locus is the $(-2)$ Heegner divisor $\cH_{-2}$ inside the Enriques
period domain, and the Coble period lattice is the orthogonal complement of a
$(-2)$ vector of $T_\En$.
Both statements are used throughout, and both are statements about a *choice* of
vector.
This section fixes that choice explicitly, shows it is unique up to the
degree-$2$ Enriques arithmetic group, and describes the subgroup of
$\Orth(T_\Co)$ that the choice produces.
The lattices are those of [Period domain embeddings and normalization](lattices.md),
and the arithmetic groups those of [Constructions of the moduli space](moduli-construction.md).
:::

## The Heegner vector inside $T_\En$

::: {.Lemma #lem:coble-heegner-vector}
### An explicit $(-2)$ vector with Coble complement

Write $T_\En = U\oplus U(2)\oplus E_8(2)$ and let $U = \ZZ u\oplus\ZZ w$ be the
unimodular hyperbolic summand, so $u^2 = w^2 = 0$ and $u\cdot w = 1$.
Set
$$
\delta \da u - w,
\qquad
\zeta \da u + w
.
$$
Then $\delta^2 = -2$, $\zeta^2 = 2$ and $\delta\cdot\zeta = 0$, and
$$
\delta^{\perp T_\En} = \ZZ\zeta\oplus U(2)\oplus E_8(2)
\cong \gens{2}\oplus U(2)\oplus E_8(2)
= \gens{2}\oplus E_{10}(2)
= T_\Co
.
$$
The sublattice $\ZZ\delta\oplus\delta^{\perp T_\En}$ has index $2$ in $T_\En$, the
missing generator being $u = \tfrac{1}{2}(\delta + \zeta)$, and the associated
gluing class in $A_{\delta^{\perp}}$ is $\tfrac{1}{2}\zeta$.
:::

::: {.proof}

The three pairings are immediate from $u^2 = w^2 = 0$ and $u\cdot w = 1$.
A vector $x\in T_\En$ decomposes as $x = au + bw + y$ with
$y\in U(2)\oplus E_8(2)$, and
$x\cdot\delta = a\,\bigl(u\cdot(u-w)\bigr) + b\,\bigl(w\cdot(u-w)\bigr) = -a + b$,
so $x\in\delta^{\perp}$ if and only if $a = b$, that is
$x\in\ZZ\zeta\oplus U(2)\oplus E_8(2)$.
Since $\zeta^2 = 2$ this sublattice is $\gens{2}\oplus E_{10}(2) = T_\Co$ by
[the Enriques-lattice definition](#def:enriques-lattice).

For the index, $\delta$ and $\zeta$ have coordinate matrix
$\begin{bmatrix}1 & -1\\ 1 & 1\end{bmatrix}$ of determinant $2$ in the basis
$(u, w)$, so $\ZZ\delta\oplus\ZZ\zeta$ has index $2$ in $U$ and hence
$\ZZ\delta\oplus\delta^{\perp}$ has index $2$ in $T_\En$; the class of
$u = \tfrac12(\delta+\zeta)$ generates the quotient.
By [Nikulin's gluing theorem](#thm:nikulin-gluing) the corresponding isotropic subgroup of
$A_{\ZZ\delta}\oplus A_{\delta^{\perp}}$ is the graph of the isometry sending
$\tfrac12\delta$ to $\tfrac12\zeta$, whose component in $A_{\delta^{\perp}}$ is
the stated class.
:::

::: {.Remark}

The primitive embedding $T_\Co\injects T_\En$ of
[the primitive-embedding lemma](#lem:primitive_embedding_eta) sends the generator $h$ of $\gens{2}$ to
$\tilde e + \tilde f$, which in the notation above is $\zeta = u + w$;
[the explicit Heegner-vector lemma](#lem:coble-heegner-vector) therefore identifies that embedding as the
inclusion of $\delta^{\perp T_\En}$ for the explicit Heegner vector
$\delta = u - w$, and supplies the gluing datum which
[the primitive-embedding lemma](#lem:primitive_embedding_eta) leaves implicit.
This is the explicit form of the statement, recorded in the Period Domains
section, that $T_\Co\cong v^{\perp T_\En}$ for a vector $v$ with $v^2 = -2$
[@DK13].
:::

## Uniqueness of the Heegner line

::: {.Theorem #thm:coble-heegner-line-unique}
### The Coble Heegner line is unique up to $\Gamma_{\En, 2}$

The line $\ZZ\delta\subset T_\En$ of [the explicit Heegner-vector lemma](#lem:coble-heegner-vector) represents
the unique $\Gamma_{\En,2}$-orbit of lines spanned by a $(-2)$ vector of $T_\En$.
:::

::: {.proof}

There is a single $\Orth(T_\En)$-orbit of $(-2)$ vectors in $T_\En$
[@AEGS25 §2], so it suffices to show that this orbit does not split under the
subgroup $\Gamma_{\En,2}\leq\Orth(T_\En)$.

Write $\mathcal A\da\im\bigl(\gent\to\Orth(A_{\ten}, q_{\ten})\bigr)$,
so that $\gent\containedin\Orth_{\mathcal A}(\ten)\da
\ts{\, g\in\Orth(T_\En) \mid \bar g\in\mathcal A \,}$.
Algorithm 2.2 of [@Daw22] decides $\Orth_{\mathcal A}(L)$-equivalence of
non-isotropic vectors under three hypotheses: the vector is non-isotropic, its
orthogonal complement is indefinite, and $\Orth(L)\to\Orth(q_L)$ is surjective.
All three hold here.
Indeed $\delta^2 = -2\neq 0$; the complement $\delta^{\perp} = T_\Co$ has
signature $(2,9)$; and $T_\En$ is an indefinite $2$-elementary lattice, so
$\Orth(T_\En)\to\Orth(q_{T_\En})$ is surjective by
[the two-elementary surjectivity theorem](#thm:two-elementary-surjectivity).
The test the algorithm applies is the discriminant-gluing condition of
[Nikulin's gluing theorem](#thm:nikulin-gluing) for the rank-one sublattice $\ZZ\delta$ and its
complement: an isometry of $\delta^{\perp}$ extends over the line $\ZZ\delta$
exactly when it preserves the gluing class
$\tfrac12\zeta\in A_{\delta^{\perp}}$ of [the explicit Heegner-vector lemma](#lem:coble-heegner-vector).

That condition is vacuous here.
The class $\tfrac12\zeta$ satisfies $q_{T_\Co}(\tfrac12\zeta) = \tfrac12$, and by
the proof of [the Coble discriminant-group proposition](#prop:coble-discriminant-group) every isometry of $q_{T_\Co}$
preserves the orthogonal decomposition
$A_{T_\Co} = \ZZ\tfrac12\zeta\perp A^0$ and fixes $\tfrac12\zeta$, so
$$
\Stab_{\Orth(A_{T_\Co}, q_{T_\Co})}\bigl(\tfrac12\zeta\bigr)
= \Orth(A_{T_\Co}, q_{T_\Co})
.
$$
The double coset set controlling the split of the full $\Orth(T_\En)$-orbit by
the preimage subgroup is therefore a singleton, and the orbit does not split.
:::

::: {.Remark}

The $(-2)$ divisor $\cH_{-2}$ is the discriminant divisor of the Enriques period
space, whose points parameterize quotients of nodal K3 surfaces by an involution
fixing a node, that is Coble surfaces with a $\tfrac14(1,1)$ singularity
[@AEGS25 §2].
[The Heegner-line uniqueness theorem](#thm:coble-heegner-line-unique) says that this divisor stays irreducible
after passing from $\Gamma_\En = \Orth(T_\En)$ to the degree-$2$ group
$\Gamma_{\En,2}$.
It is a statement about the negative vector $\delta$, and is independent of the
count of $\Gamma_{\En,2}$-orbits of primitive *isotropic* lines in $T_\En$, of
which there are five, one for each $0$-cusp of $\fentwo$
[@AEGS25 Cor. 3.12].
:::

## The Coble arithmetic group induced from the Enriques side

::: {.Definition #def:gamma-co-en}
### The induced Coble subgroup

For the Heegner vector $\delta$ of [the explicit Heegner-vector lemma](#lem:coble-heegner-vector), define
$$
\Gamma_\Co^\En(\delta)
\da \im\Bigl(
\Stab_{\gent}(\ZZ\delta)
\too
\Orth\bigl(\delta^{\perp \ten}\bigr) = \Orth(T_\Co)
\Bigr)
,
$$
the group of restrictions to $\delta^{\perp}$ of those elements of
$\Gamma_{\En,2}$ that preserve the line $\ZZ\delta$.
The condition is on the line, since a
component of the Heegner divisor is determined by $\ZZ\delta$ and not by a choice
of sign for $\delta$.
:::

::: {.Proposition #prop:gamma-en-two-gluing}
### Discriminant description of $\Gamma_{\En, 2}$

Let $\sen = U(2)\oplus E_8(2)$ and $\ten$ be the invariant and coinvariant
lattices of the Enriques involution on $\lkt$, and let
$$
\gamma\colon A_{\sen}\iso A_{\ten},
\qquad
q_{\ten}\circ\gamma = -q_{\sen}
$$
be the gluing anti-isometry supplied by [the embedding-gluing description](#rmk:embedding-gluing-data) for the
primitive embedding $\sen\injects\lkt$ with complement $\ten$.
Then
$$
\gent
= \ts{\,
g_T\in\Orth(\ten)
\;\middle|\;
\exists\, g_S\in\Orth(\sen) \text{ with } g_S(h) = h
\textand \bar g_T\circ\gamma = \gamma\circ\bar g_S
\,}
,
$$
where $h = e + f\in U(2) = \sdp\containedin \sen$ is the degree-$2$ polarization
vector, with $e^2 = f^2 = 0$ and $e\cdot f = 2$, so that $h^2 = 4$
[@AEGS25 Def. 2.5, Def. 2.6].
Equivalently, the image of $\Gamma_{\En,2}$ in $\Orth(q_{T_\En})$ is the
$\gamma$-transport of the image of $\Stab_{\Orth(S_\En)}(h)$ in
$\Orth(q_{S_\En})$.
:::

::: {.proof}

By definition $\Gamma_{\En,2}$ is the image in $\Orth(T_\En)$ of the isometries
of $\lkt$ that commute with $I_\En$ and fix $h$ [@AEGS25 Def. 2.6].
An isometry of $\lkt$ commuting with $I_\En$ is the same as a pair
$(g_S, g_T)\in\Orth(S_\En)\times\Orth(T_\En)$ preserving the two eigenlattices,
and by [Nikulin's gluing theorem](#thm:nikulin-gluing) such a pair extends over the overlattice $\lkt$
of $S_\En\oplus T_\En$ exactly when it preserves the graph of $\gamma$, that is
when $\bar g_T\circ\gamma = \gamma\circ\bar g_S$.
The polarization $h$ lies in $S_\En$, so the condition $g(h) = h$ on $\lkt$ is the
condition $g_S(h) = h$.
:::

::: {.Proposition #prop:polarization-stabilizer-enriques}
### The integral stabilizer of the degree-$2$ polarization

Write $S_\En = C(2)$ with $C = U\oplus E_8$ even unimodular of signature
$(1,9)$, and let $h\in S_\En$ be the polarization vector of
[the discriminant description of $\Gamma_{\En,2}$](#prop:gamma-en-two-gluing), so that $h = u_0 + w_0$ for a basis
$u_0, w_0$ of the $U$ summand of $C$ with $u_0\cdot w_0 = 1$.
Then restriction to $h^{\perp}$ gives an isomorphism
$$
\Stab_{\Orth(S_\En)}(h)
\;\iso\;
\Orth\bigl(\gens{-2}\oplus E_8\bigr)
= \ts{\pm 1}\times W(E_8)
,
$$
of order $2\abs{W(E_8)} = 1\,393\,459\,200$, and the element
$\id_U\oplus(-\id_{E_8})$ lies in the kernel of the reduction
$\Stab_{\Orth(S_\En)}(h)\to\Orth(A_{S_\En}, q_{S_\En})$.
:::

::: {.proof}

Twisting does not change the isometry group, so
$\Orth(S_\En) = \Orth(C)$ and $\Stab_{\Orth(S_\En)}(h) = \Stab_{\Orth(C)}(h)$.
Computing in $C$, one has $h^2 = 2$ and
$h^{\perp C} = \ZZ(u_0 - w_0)\oplus E_8$ with $(u_0-w_0)^2 = -2$, so
$h^{\perp C}\cong\gens{-2}\oplus E_8$.
An isometry fixing $h$ preserves $h^{\perp}$, giving the restriction homomorphism,
which is injective because $C_\QQ = \QQ h\oplus h_\QQ^{\perp}$.
It is surjective: $A_{h^{\perp}}\cong A_{\gens{-2}}\cong\ZZ/2\ZZ$ has trivial
automorphism group, so every isometry of $h^{\perp}$ preserves the gluing class
of the index-two overlattice $C$ of $\ZZ h\oplus h^{\perp}$ and extends over $C$
fixing $h$, by [Nikulin's gluing theorem](#thm:nikulin-gluing).
The lattice $\gens{-2}\oplus E_8$ is negative definite and generated by its
$(-2)$ vectors, whose root system is $A_1\oplus E_8$; no isometry mixes summands
of different ranks, so its isometry group is
$\Orth(\gens{-2})\times\Orth(E_8) = \ts{\pm1}\times W(E_8)$.

For the last claim, $\id_U\oplus(-\id_{E_8})$ fixes $h\in U$ and acts on
$A_{S_\En}\cong C/2C$ ([the twisted-unimodular discriminant proposition](#prop:twisted-unimodular-discriminant)) by the
identity on $U/2U$ and by $x\mapsto -x\equiv x$ on $E_8/2E_8$.
:::

::: {.Theorem #thm:coble-heegner-finite-orbits}
### The finite image and its isotropic orbits

With the notation of [the polarization-stabilizer proposition](#prop:polarization-stabilizer-enriques) and
[the explicit Heegner-vector lemma](#lem:coble-heegner-vector):

1.  the image of the integral stabilizer in the discriminant group,
    $$
    G \da \im\bigl(\Stab_{\Orth(S_\En)}(h)\to\Orth(A_{S_\En}, q_{S_\En})\bigr)
    ,
    $$
    has order $\abs{W(E_8)} = 696\,729\,600$, and is generated by the swap of the
    two isotropic generators of the $U$ summand of $C$, which fixes $h$, together
    with the reflections in the simple roots of the $E_8$ summand;

2.  the corresponding group $G_\Co\leq\Orth(A_{T_\Co}, q_{T_\Co})$, obtained by
    transporting $G$ along $\gamma$ and restricting to the Coble Heegner
    complement $\delta^{\perp} = T_\Co$, has order $\abs{W(E_8)}$ and acts on the
    $528$ isotropic classes of $A_{T_\Co}$ with orbit lengths
    $$
    [\,1,\ 2,\ 120,\ 135,\ 270\,]
    ;
    $$

3.  the finite stabilizer $\Stab_{\Orth(q_{T_\Co})}\bigl(\tfrac12\tilde h_\Co\bigr)$
    of the class of the transported polarization has order
    $94\,755\,225\,600$, contains $G_\Co$ with index $136$, and acts on the same
    $528$ isotropic classes with orbit lengths $[\,1,\ 255,\ 272\,]$.
:::

::: {.Remark}
### How the three orders are obtained

The generators named in (1) are the two evident families of isometries of $C$
fixing $h = u_0 + w_0$: the involution $u_0\leftrightarrow w_0$, and
$W(E_8)$ acting on the second summand.
By [the polarization-stabilizer proposition](#prop:polarization-stabilizer-enriques) these generate a group of order
$2\abs{W(E_8)}$ whose reduction has $\id_U\oplus(-\id_{E_8})$ in its kernel, so
the image has order at most $\abs{W(E_8)}$; the stated equality, and the two
orbit decompositions of (2) and (3), are exact computations in the finite
quadratic space $A_{T_\Co}\cong B/2B$ of
[the Coble mod-four form definition](#def:coble-mod-four-form), carried out by stabilizing the four fibers of $Q$
inside $\GL(B/2B)$ and then computing orbits of the resulting finite group on the
fiber $Q\inv(0)$.
The index $136 = 94\,755\,225\,600 / 696\,729\,600$ in (3), and the relation
$46\,998\,591\,897\,600 = 496\cdot 94\,755\,225\,600$ between the order of
[the Coble discriminant-group proposition](#prop:coble-discriminant-group) and that of the finite stabilizer, are
consistency checks: $\tfrac12\tilde h_\Co$ is a class with
$q_{T_\Co} = 1$, and $496$ is the number of such classes by
[the Coble $Q$-fiber proposition](#prop:coble-q-fibers).
:::

::: {.Remark}
### Reading the two orbit decompositions

The two decompositions in [the finite-image orbit theorem](#thm:coble-heegner-finite-orbits) answer different
questions, and their difference is the content of the theorem.
The coarser one, $[1, 255, 272]$, is the decomposition under the *whole* finite
stabilizer of the polarization class, the largest group the discriminant form
alone can distinguish.
The finer one, $[1, 2, 120, 135, 270]$, is the decomposition under the group that
actually arises from integral isometries of $S_\En$ fixing $h$, namely $G_\Co$.
Since the latter has index $136$ in the former, a calculation carried out purely
in $\Orth(q_{T_\Co})$ overestimates how much of $A_{T_\Co}$ a degree-$2$ Coble
period point can see.
The four nonzero orbit lengths $2, 120, 135, 270$ sum to $527$, the number of
nonzero isotropic classes of [the Coble $Q$-fiber proposition](#prop:coble-q-fibers), so both decompositions
refine the single nonzero orbit of [the isotropic-class orbit theorem](#thm:coble-isotropic-class-orbits).

Both are statements in the finite quadratic space $A_{T_\Co}$.
Neither is yet a classification of $\Gamma_\Co^\En(\delta)$-orbits of primitive
isotropic *vectors* of $T_\Co$, for the reason recorded in
[the primitive-isotropic-class proposition](#prop:coble-primitive-isotropic-classes): an integral parabolic stabilizer
may have proper image in the finite one, so a finite orbit can split.
:::

## The Coble folding involution

::: {.Proposition #prop:theta-co-exists}
### The sign involution of the Coble primitive embedding

Let $S_\Co\injects\lkt$ be the primitive embedding of
[the Coble invariant-lattice proposition](#prop:coble-invariant-lattice), with complement
$T_\Co = S_\Co^{\perp\lkt}$, and let
$$
\gamma_\Co\colon A_{S_\Co}\iso A_{T_\Co},
\qquad
q_{T_\Co}\circ\gamma_\Co = -q_{S_\Co}
$$
be the associated gluing anti-isometry.
Then the pair $(-\id_{S_\Co}, \id_{T_\Co})$ preserves the graph of $\gamma_\Co$
and therefore defines an isometry
$$
\theta_\Co\in\Orth(\lkt),
\qquad
\ro{\theta_\Co}{S_\Co} = -\id,
\qquad
\ro{\theta_\Co}{T_\Co} = \id
,
$$
whose $(+1)$ and $(-1)$ eigenlattices are $T_\Co$ and $S_\Co$.
An isometry of $\lkt$ commutes with $\theta_\Co$ if and only if it preserves both
eigenlattices.
:::

::: {.proof}

Both $A_{S_\Co}$ and $A_{T_\Co}$ are $2$-elementary, so $-\id$ and $\id$ agree on
each of them; the pair therefore acts as the identity on the graph of
$\gamma_\Co$ and by [Nikulin's gluing theorem](#thm:nikulin-gluing) extends over the overlattice $\lkt$
of $S_\Co\oplus T_\Co$.
The eigenlattice description is the definition of the extension.
For the last claim, an isometry commuting with an involution preserves its
eigenspaces, which by [the involution-eigenspace proposition](#prop:involution_eigenspaces) are the rational spans of
$T_\Co$ and $S_\Co$; conversely an isometry preserving both eigenlattices
commutes with $\theta_\Co$ on each of them and hence on $\lkt$.
:::

::: {.Remark}

[The folding-involution proposition](#prop:theta-co-exists) settles the existence of the folding involution
$\theta$ as a lattice isometry, and does so before any $22\times 22$ matrix is
written: the involution is determined by the primitive embedding and the gluing
anti-isometry.
What a matrix realization additionally supplies is a basis in which
$\theta_\Co$, the polarization class, and the roots of the Coxeter diagram can be
compared with one another.

Combining [the folding-involution proposition](#prop:theta-co-exists) with [the discriminant description of $\Gamma_{\En,2}$](#prop:gamma-en-two-gluing) gives
the Coble-side analogue of the discriminant description of $\Gamma_{\En,2}$: the
restriction to $T_\Co$ of the centralizer of $\theta_\Co$ inside the stabilizer of
a chosen polarization class $\tilde h_\Co\in S_\Co$ consists of those
$g_T\in\Orth(T_\Co)$ for which some $g_S\in\Orth(S_\Co)$ satisfies
$g_S(\tilde h_\Co) = \tilde h_\Co$ and
$\bar g_T\circ\gamma_\Co = \gamma_\Co\circ\bar g_S$.
Identifying that group with $\Gamma_\Co^\En(\delta)$ of [the induced Coble subgroup definition](#def:gamma-co-en)
requires an isometry between the Coble primitive embedding and the Enriques
Heegner complement carrying $\tilde h_\Co$ to the class $h = e+f$ of
[the discriminant description of $\Gamma_{\En,2}$](#prop:gamma-en-two-gluing).
The images of the two groups in $\Orth(q_{T_\Co})$ do agree, by
[the finite-image orbit theorem](#thm:coble-heegner-finite-orbits), but agreement of finite images is weaker
than an isomorphism of the lattice subgroups.
:::
