# Automorphism lifting through a gluing {#sec:automorphism-lifting}

::: {.Remark}

Let $L$ be an even overlattice of $M\oplus N$ in which $M$ and $N$ are primitive,
and let $\varphi_M\in\Orth(M)$ and $\varphi_N\in\Orth(N)$.
The pair acts on $M\oplus N$, hence on $L\tensor\QQ$, but need not preserve $L$.
This section decides when it does.
The answer is a stabilizer condition on the isotropic subgroup that
\longref{thm:nikulin-gluing} attaches to the overlattice, so it is a statement
about the gluing datum, equivalently about the pair of primitive inclusions, and
not about either lattice on its own.
:::

## The discriminant representation

::: {.Notation #not:discriminant-representation}
### Notation for the discriminant representation

For a lattice $L$ the induced homomorphism
$$
\rho_L\colon \Orth(L)\too \Orth(q_L)
$$
of the Lattice Theory section, sending an isometry to its action on the
discriminant form, is the **discriminant representation** of $L$.
Its kernel is the stable orthogonal group $\tilde\Orth(L)$, and we write
$\bar\varphi\da\rho_L(\varphi)$.
The homomorphism exists because an isometry of $L$ extends to a $\ZZ$-module
isomorphism of $L\dual$ and so descends to $A_L = L\dual/L$
[@Nik80 §1.4].
:::

::: {.Remark}

For an orthogonal direct sum, $A_{M\oplus N} = A_M\oplus A_N$ and
$\rho_{M\oplus N}(\varphi_M\oplus\varphi_N) = \bar\varphi_M\oplus\bar\varphi_N$,
by the additivity of discriminant groups recorded in the Lattice Theory
section.
:::

## The lifting criterion

::: {.Definition #def:gluing-datum-of-a-pair}
### The gluing datum of a pair of primitive inclusions

Let $\iota_M\colon M\injects L$ and $\iota_N\colon N\injects L$ be primitive
inclusions with $\iota_N(N) = \iota_M(M)^{\perp L}$, so that $L$ is an even
overlattice of $M\oplus N$.
The **gluing datum** of the pair is the isotropic subgroup
$$
H \da L/(M\oplus N) \ \leq\ A_M\oplus A_N
$$
attached to $L$ by \longref{thm:nikulin-gluing}, together with the two
inclusions themselves.
By \longref{rmk:embedding-gluing-data} the subgroup $H$ is the graph of an
anti-isometry $\gamma\colon H_M\iso H_N$ between subgroups $H_M\leq A_M$ and
$H_N\leq A_N$, and $L$ is recovered as the preimage of $H$ under the quotient map
$(M\oplus N)\dual\to A_M\oplus A_N$.
:::

::: {.Theorem #thm:automorphism-lifting-criterion}
### When a pair of isometries lifts

Let $L$, $M$, $N$ and $H$ be as in [the gluing-datum definition](#def:gluing-datum-of-a-pair), and let
$\varphi_M\in\Orth(M)$ and $\varphi_N\in\Orth(N)$.
Then $\varphi_M\oplus\varphi_N$ extends to an isometry of $L$ if and only if
$$
\left(\bar\varphi_M\oplus\bar\varphi_N\right)(H) = H
.
$$
The extension is then unique, and it restricts to $\varphi_M$ on $M$ and to
$\varphi_N$ on $N$.
:::

::: {.proof}

Write $\psi\da\varphi_M\oplus\varphi_N\in\Orth(M\oplus N)$.
An isometry of $M\oplus N$ extends uniquely to a $\ZZ$-module isometry $\psi\dual$
of $(M\oplus N)\dual$ inside $(M\oplus N)\tensor\QQ$, so the only candidate
extension to $L$ is $\ro{\psi\dual}{L}$, and uniqueness follows.
Since $M\oplus N\containedin L\containedin(M\oplus N)\dual$ by
\longref{def:overlattice}, the candidate maps $L$ into
$(M\oplus N)\dual$ always, and preserves $L$ exactly when it preserves the image
of $L$ in the quotient $A_{M\oplus N} = A_M\oplus A_N$.
That image is $H$, and the induced action of $\psi\dual$ on
$A_{M\oplus N}$ is $\bar\varphi_M\oplus\bar\varphi_N$, giving the stated
condition.
Conversely, if the condition holds then $\ro{\psi\dual}{L}$ is a bijection of $L$
preserving the form inherited from $(M\oplus N)\tensor\QQ$, hence an isometry of
$L$.
:::

::: {.Corollary #cor:liftable-automorphisms}
### The liftable subgroup

With the notation of [the lifting criterion](#thm:automorphism-lifting-criterion), fix
$\varphi_N = \id_N$ and let $\Gamma\leq\Orth(M)$ be any subgroup.
The isometries of $M$ that extend over $L$ fixing $N$ pointwise form the subgroup
$$
\rho_M\inv\Bigl(\Stab_{\Orth(q_M)}(H)\Bigr)\ \intersect\ \Gamma
\ \leq\ \Gamma
,
$$
where $\Stab_{\Orth(q_M)}(H)$ is the stabilizer of $H$ for the action of
$\Orth(q_M)$ on subgroups of $A_M\oplus A_N$ through the first summand.
In particular the liftable subgroup contains $\tilde\Orth(M)\intersect\Gamma$,
and it has finite index in $\Gamma$ whenever
$\rho_M(\Gamma)$ is finite.
:::

::: {.proof}

Apply [the lifting criterion](#thm:automorphism-lifting-criterion) with
$\bar\varphi_N = \id$, so that the condition reads
$(\bar\varphi_M\oplus\id)(H) = H$; the set of $\bar\varphi_M$ satisfying it is by
definition the stabilizer, which is a subgroup of $\Orth(q_M)$, and its preimage
under the homomorphism $\rho_M$ is a subgroup of $\Orth(M)$.
The stable orthogonal group is the kernel of $\rho_M$
([the discriminant-representation notation](#not:discriminant-representation)) and so acts trivially on $H$.
Finiteness of the index follows because $\Orth(q_M)$ is finite, $A_M$ being
finite.
:::

::: {.Remark}
### The operation belongs to the arrow

The datum consumed by [the lifting criterion](#thm:automorphism-lifting-criterion) is $H$,
equivalently the pair of primitive inclusions of
[the gluing-datum definition](#def:gluing-datum-of-a-pair).
Neither $M$ nor $N$ determines it: the same lattice $M$ occurs in many gluings,
and each one imposes its own condition.
Liftability is therefore a property of the inclusions, and the subgroup of
[the liftable-subgroup corollary](#cor:liftable-automorphisms) is attached to them.

The hypotheses are morphism-level for the same reason.
An inclusion is primitive when its cokernel is torsion-free
(\longref{prop:primitive-characterization}), and saturation and index are
properties of the inclusion; a determinant or a greatest common divisor of
matrix entries recognizes primitivity only under hypotheses that the definition
itself does not state.
:::

## The unimodular case and its two specimens

::: {.Corollary #cor:lifting-unimodular}
### Lifting across a unimodular overlattice

Suppose in addition that $L$ is unimodular.
Then $H$ is the graph of an anti-isometry $\gamma\colon A_M\iso A_N$ defined on
all of $A_M$, and $\varphi_M\oplus\varphi_N$ extends to $L$ if and only if
$$
\bar\varphi_N\circ\gamma = \gamma\circ\bar\varphi_M
.
$$
:::

::: {.proof}

Unimodularity of $L$ forces $H_M = A_M$ and $H_N = A_N$ in
\longref{rmk:embedding-gluing-data}, so $H$ is the graph
$\ts{(x, \gamma x) \mid x\in A_M}$ of an anti-isometry defined on all of $A_M$.
A pair preserves that graph exactly when
$\bar\varphi_N(\gamma x) = \gamma(\bar\varphi_M x)$ for every $x$, which is the
displayed identity.
:::

::: {.Remark}
### Two computations in this book are instances

[The unimodular lifting corollary](#cor:lifting-unimodular) is the mechanism behind two statements proved
elsewhere in this part, both for the unimodular $\lkt$.

The discriminant description of the degree-$2$ Enriques group
(\longref{prop:gamma-en-two-gluing}) is the liftable-subgroup computation of
[the liftable-subgroup corollary](#cor:liftable-automorphisms) for the gluing
$\sen\oplus \ten\containedin\lkt$, with the extra condition $g_S(h) = h$ cutting
$\Gamma\leq\Orth(\sen)$ down to the stabilizer of the polarization; the
commutation identity $\bar g_T\circ\gamma = \gamma\circ\bar g_S$ appearing there
is exactly the criterion above.

The Coble folding involution (\longref{prop:theta-co-exists}) is the same
criterion applied to the pair $(-\id_{S_\Co}, \id_{T_\Co})$ for the gluing
$S_\Co\oplus T_\Co\containedin\lkt$: because both discriminant groups are
$2$-elementary, $\overline{-\id} = \overline{\id}$ on each, and the identity
holds trivially, so the pair lifts.
:::
