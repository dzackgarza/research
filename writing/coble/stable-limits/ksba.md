# KSBA stable limits

## How a stable limit is obtained

::: {.Remark}

A KSBA stable limit here is never constructed directly. The pair is
$(Z, \varepsilon R_Z)$ for an Enriques or Coble surface $Z$ and $0 < \varepsilon \ll 1$,
and $Z$ is a quotient of its K3 cover; the stable limits are correspondingly the
*quotients of the stable limits of the K3 pairs $(X, \varepsilon R)$ by the involution*
[@AEGS25 §7.3]. So the work happens upstairs, on the K3 side, where Kulikov models and
their dual complexes are available ([the singular-IAS definition](#def:singular_ias)), and the Enriques or Coble limit
is read off by descending along $\iota_\En$.
:::

::: {.Remark}

Which limit one obtains is determined by combinatorics rather than by geometry. Over a
$0$-cusp the semifan is a generalized Coxeter fan, and its cones are indexed by
subdiagrams of the folded Coxeter diagram of that cusp [@AEGS25 §5.1]:

- a **Type III** limit corresponds to an *elliptic* subdiagram. Each relevant connected
  component contributes an ADE surface, and the limit is their union glued along the
  double curves [@AEGS25 §7.1].

- a **Type II** limit corresponds to a *maximal parabolic* subdiagram. After the
  irrelevant components are discarded, each remaining component is an
  $\widetilde{A}\widetilde{D}\widetilde{E}$ diagram [@AEGS25 §7.2].

The irrelevant roots are exactly those the generalized Coxeter semifan collapses, which
is why the compactification is toroidal over some cusps and strictly semitoroidal over
the rest.
:::

::: {.Remark}

For the Coble locus one further restriction applies, and it is the content of the rest of
this chapter. A polarized Coble surface is an Enriques surface whose period lies on the
Heegner divisor cut by an admissible root $\delta$, so its stable limits are those
Enriques limits lying over $\delta^{\perp}$. Making that precise means restricting the
semifan $\semifan{F}_{\mathrm{ram}}$ along $\bD(\delta^{\perp})$, which is
[the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan), and identifying the resulting singularity
type, which is [the quarter-singularity conjecture](#conj:coble_quarter_singularity).
:::

## A worked integral affine structure

::: {.Example #ex:type-ii-ias-41}
### The Type II ray at the $1$-cusp $41$

Take the monodromy invariant with barycentric coordinates
$$
\ell = (0^6, 1, 0^7, 1, 0^5, 2, 2)
$$
at $0$-cusp $4$. The resulting integral affine sphere agrees with the one built at
$0$-cusp $1$ from $(0, 0, 1, 0^7, 1, 0^9, 2, 2)$, which is what it means for this ray to
be shared: it is the Type II ray corresponding to the $1$-cusp labelled $41$, and it
occurs as a limit of $\ias$ at either of the two $0$-cusps it joins
[@AEGS25 Ex. 4.16].

Being Type II, the dual complex $\Gamma(\cX_0)$ is a segment rather than a sphere, here of
length one, and the central fiber is
$$
\cX_0 = \widetilde{V}_1 \union_E \widetilde{V}_2 ,
$$
two copies of the same $\widetilde{D}_8$ involution pair glued along the elliptic curves
$E \in \abs{-K_{\widetilde{V}_1}}$ with a twist by $2$-torsion.
:::

::: {.Warning}
The Enriques involution *flips* this segment. So the Enriques equator is not a
subcomplex of $\Gamma(\cX_0)$, which is what the equivariant-triangulation machinery
usually assumes: this ray is one of the cases where that hypothesis has to be dropped
[@AEGS25 Ex. 4.16]. Compare [the equivariant-triangulation question](#que:equivariant_triangulation).
:::


## The polarized Coble locus and its branches

::: {.Remark}

The stable limits below compactify the polarized Coble locus, which we realize inside the moduli space $\fentwo$ of degree-$2$ numerically polarized Enriques surfaces: one takes the Coble Heegner divisor cut out inside $\fentwo$ and normalizes it.
Because the polarized arithmetic group $\gent$ has finite index in the full Enriques group $\Gamma_\En$, a single unpolarized root orbit can split into several polarized orbits.
Until root-orbit uniqueness is established for $\gent$, the polarized Coble locus is therefore described as a union of *branchwise* quotients, one attached to each orbit of admissible Coble roots, rather than as a single global quotient.
:::

::: {.Remark}

Each branch carries its own arithmetic group.
Fixing an admissible Coble root $\delta$ -- a primitive $(-2)$-vector in the polarized Enriques period lattice -- the group governing the corresponding branch is the image in $\Orth(\delta^\perp)$ of the stabilizer of $\bZ\delta$ inside $\gent$; this is the minimal group making the period-domain inclusion
$$
\bD(\delta^\perp) \injects \bD(\ten)
$$
equivariant.
Since $T_\Co \cong \delta^{\perp \ten}$ for a $(-2)$-vector $\delta$ [@DK13], this refines the arithmetic group $\Gamma_{\Co, 2}$ of the moduli summary, and the two descriptions agree exactly when the polarized root orbit is unique.

::: {.Remark #rmk:gamma-co-2-two-definitions}
### The two definitions of $\Gamma_{\Co, 2}$ agree on lines, not on vectors

The branchwise notes define $\Gamma_{\Co, 2}$ as the image in $\gent$ of the
stabilizer of a marked Coble root $\delta$; [Constructions of the moduli space](moduli-construction.md)
defines it as $\Stab_{\Orth(\ten)}(T_\Co)$. These agree,
and the bridge is $T_\Co \cong \delta^{\perp \ten}$ above.

An isometry of $\ten$ fixing $\delta$ preserves $\delta^{\perp} = T_\Co$, so
$\Stab(\delta) \containedin \Stab(T_\Co)$. Conversely an isometry
preserving $T_\Co$ preserves its orthogonal complement in $\ten$, which is the rank-one
lattice $\gens{\delta}$, so it sends $\delta \mapsto \pm\delta$. Hence
$$
\Stab_{\Orth(\ten)}(T_\Co) \;=\; \Stab_{\Orth(\ten)}(\gens{\delta})
\;\supseteq\; \Stab_{\Orth(\ten)}(\delta)
$$
with index at most $2$, the two differing exactly by whether $-1$ on $\gens{\delta}$ is
admitted. The stabilizer of the *line* is the right object: it is what acts on the period
domain $\bD(\delta^{\perp})$, on which $\pm\delta$ have the same effect.
:::
:::

::: {.Question #que:coble_root_orbit_uniqueness}

Is the orbit of admissible Coble roots under $\gent$ unique, so that the branchwise polarized Coble locus collapses to a single normalized divisor?
Two routes to an affirmative answer are available: an arithmetic double-coset computation for the polarized subgroup $\Gamma_{\En, 2}$, or a geometric argument that the $D_4$-symmetry of the Horikawa model acts transitively on the torus-fixed-point branches.

::: {.Warning}
The root-orbit uniqueness is Namikawa's [@Nam85], and is stated there modulo the full
Enriques group $\Gamma_\En$. It does not settle the corresponding question for the
finite-index subgroup $\Gamma_{\En,2}$, which is what the polarized problem needs.
:::
:::

## The KSBA stable pair

::: {.Remark}

The ambient degree-$2$ Enriques picture is settled.
For a degree-$2$ numerically polarized Enriques surface $(Z, [\mathcal L_Z])$, the ramification divisor $R_Z$ of the associated double cover of a quartic del Pezzo surface is ample, $\QQ$-Cartier, and lies in the polarizing system, so the pair $(Z, \varepsilon R_Z)$ is log canonical for $0 < \varepsilon \ll 1$ and $\fentwo$ admits a KSBA compactification $\ksbacpt{\fentwo}$ [@CDL25; @AEGS25]. The Coble stable pair is the descent of this picture along the quotient by the Enriques involution $\ien$, which for Coble surfaces is *not* fixed-point free.
:::

::: {.Remark}

The intended KSBA boundary object is a pair
$$
(\bar S, \varepsilon R_{\bar S}), \qquad 0 < \varepsilon \ll 1,
$$
where $\bar S$ is the stable quotient surface and $R_{\bar S}$ is the descended ramification divisor.
The divisor is identified; establishing that this pair is KSBA stable remains a research program with the following open obligations:

- that $R_{\bar S}$ is $\QQ$-Cartier;

- that $R_{\bar S}$ is ample -- expected to follow by descending the ample ramification divisor from the K3 cover, that is, by pulling back $K_{\bar S} + \varepsilon R_{\bar S}$ to $\varepsilon R_X$ with $R_X$ coming from the $(2,2)$-divisor on $Y = \PP^1 \times \PP^1$, rather than by asserting stability of the quotient directly;

- that $(\bar S, \varepsilon R_{\bar S})$ is slc, for which one proposed route runs through the du Val singularities on the K3 cover and a finite quasi-étale quotient in codimension one;

- and a controlled account of how the anti-bicanonical $(-4)$-curve is seen on the smooth resolution versus on the stable model.
:::

::: {.Conjecture #conj:coble_quarter_singularity}

On the stable quotient $\bar S$, an $A_1$-node of the K3 cover fixed by $\iota_\En$ descends to a cyclic quotient singularity of type $\frac{1}{4}(1,1)$, and the anti-bicanonical $(-4)$-curve on the smooth Coble resolution is the curve contracted to this point.
In the Horikawa model on $Y = \PP^1 \times \PP^1$ with $\tau(x,y) = (-x,-y)$ [@Hor77], the local input producing the $A_1$-node on the double cover is a $\tau$-invariant $(4,4)$-curve passing through a $\tau$-fixed point with nondegenerate quadratic term.
:::

::: {.Remark}

The local singularity package of [the quarter-singularity conjecture](#conj:coble_quarter_singularity) is central to the program, but it is currently a migrated research claim rather than a proven statement; it is precisely the input awaited by the slc and ampleness verifications above.
:::

## The restricted ramification semifan

::: {.Conjecture #conj:restricted_ramification_semifan}

The semitoroidal model of the polarized Coble locus is obtained by restricting the Enriques ramification semifan of the degree-$2$ compactification problem to the hyperplane cut out by the Coble root, and keeping exactly those walls whose relative interiors meet the Coble positive cone.
Under this restriction, a Coble wall is irrelevant precisely when every Enriques wall restricting to it is already irrelevant.
:::

::: {.Remark}

Proving that this restriction defines the semitoroidal fan requires showing that no extra roots appear after restriction, that no essential Enriques wall collapses or restricts trivially, and that running Vinberg's algorithm on the restricted lattice is not conflated with a proof of the fan itself.
:::

## Comparison with the KSBA compactification

::: {.Remark}

The KSBA stable limits sit inside the K3 stable-pair family of the degree-$(2,2,0)$ problem via [the Baily--Borel embedding lemma](#lem:locally_closed_embedding_BB). The proposed comparison proceeds by restricting the universal K3 stable-pair family over $F_{(2,2,0)}$ to the Coble Noether-Lefschetz locus $\bD(r^\perp)$, extending the Enriques involution over the stable limits by uniqueness of KSBA limits, descending the ramification divisor, and matching the induced boundary stratification against [the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan).
:::

::: {.Conjecture #conj:ksba_semitoroidal_comparison}

After normalization, the KSBA compactification of the polarized Coble locus agrees with the semitoroidal compactification induced by the restricted ramification semifan.
:::

::: {.Conjecture #conj:no_moduli_loss}

The stable quotient remembers the marked Coble root.
Geometrically, this memory is carried by the $\frac{1}{4}(1,1)$ singularity of [the quarter-singularity conjecture](#conj:coble_quarter_singularity) -- equivalently, by the contracted anti-bicanonical $(-4)$-curve on the resolution -- so that degenerations differing only by their marked root are not identified.
Without this memory the restricted semifan would be too fine for the actual KSBA boundary, and [the KSBA--semitoroidal comparison conjecture](#conj:ksba_semitoroidal_comparison) would fail.
:::

::: {.Remark}

[The KSBA--semitoroidal comparison conjecture](#conj:ksba_semitoroidal_comparison) remains open on four counts: root-orbit uniqueness ([the root-orbit uniqueness question](#que:coble_root_orbit_uniqueness)), the ramification-semifan restriction identity ([the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan)), [the no-moduli-loss conjecture](#conj:no_moduli_loss), and the exact cusp enumeration.
The boundary dictionaries and cusp tables appearing in preliminary work remain unverified pending the restriction theorem and an explicit cusp computation.
:::

::: {.Remark}

A second semitoroidal model of the *unpolarized* Coble period domain is available
and is not an input to any of the four: the GIT compactification of the moduli of
ten-nodal sextics is a Looijenga compactification
([the GIT--Looijenga theorem](#thm:git-equals-looijenga)), whose semifan is determined by an
arrangement of hyperplanes rather than by degenerations of stable pairs.
Its semifan and the restricted ramification semifan of
[the restricted-ramification-semifan conjecture](#conj:restricted_ramification_semifan) are computed from unrelated data,
so neither determines the other.
:::

## Boundary cusp data

::: {.Remark}

The boundary is organized by cusp pairs marked with a Coble root.
A $0$-cusp is modeled by an orbit of a pair $(I, r)$ consisting of an isotropic line $I$ and a compatible Coble root $r$, and a $1$-cusp by an orbit of a pair $(J, r)$ consisting of an isotropic plane $J$ and the same root, with incidence recorded by the containment $I \subset J$ preserving $r$.
A root $r$ is *admissible* at a cusp when it lifts to a primitive $(-2)$-root of the ambient Enriques lattice lying in the designated Coble orbit; this is the datum that promotes plain Enriques cusp data to polarized Coble cusp data, and it must be preserved along the incidence $I \subset J$.
:::

::: {.Question #que:coble_cusp_admissibility}

What is the precise admissibility test for Coble roots at a cusp, formulated against the folded K3-to-Enriques Coxeter data?
Sterk cusps $3$ and $5$ are the delicate cases where additional reflection data may intervene.
:::

::: {.Remark}

Any actual cusp count must reduce to explicit lattice-orbit work -- through Sterk's representatives (five $0$-cusps and nine $1$-cusps for the Enriques space [@Ste91]) together with their stabilizers, or direct period-domain enumeration -- and discriminant-form shortcuts suggest candidates but do not by themselves prove the cusp diagram.
One durable exclusion is nonetheless available: since primitive isotropic vectors of $T_\Co$ pair evenly in the ambient Enriques lattice, they have divisibility $2$ ([the divisibility lemma](#lem:divisibilityAlwaysTwoTco)), so the divisibility-one Sterk cusp $1$ does not occur on the polarized Coble boundary and only the divisibility-two Sterk cusps $2$--$5$ are in play.
This is consistent with [the cusp-correspondence theorem](#thm:cusp_correspondence), under which the unique Coble $0$-cusp corresponds to a divisibility-two Enriques cusp.
:::
