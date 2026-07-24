# KSBA stable limits

::: {.remark}

We describe the KSBA stable limits of Coble surfaces.
:::

::: {.remark}

We give an example of an integral affine structure for a degeneration of Coble
surfaces.
:::

\todo[inline]{Both sections above are outlines: the KSBA stable limits and the worked integral affine example remain to be written.}

## The polarized Coble locus and its branches

::: {.remark}

The stable limits below compactify the polarized Coble locus, which we realize
inside the moduli space $F_{\En, 2}$ of degree-$2$ numerically polarized Enriques
surfaces: one takes the Coble Heegner divisor cut out inside $F_{\En, 2}$ and
normalizes it.
Because the polarized arithmetic group $\Gamma_{\En, 2}$ has finite index in the
full Enriques group $\Gamma_\En$, a single unpolarized root orbit can split into
several polarized orbits.
Until root-orbit uniqueness is established for $\Gamma_{\En, 2}$, the polarized
Coble locus is therefore described as a union of *branchwise* quotients, one
attached to each orbit of admissible Coble roots, rather than as a single global
quotient.
:::

::: {.remark}

Each branch carries its own arithmetic group.
Fixing an admissible Coble root $\delta$ -- a primitive $(-2)$-vector in the
polarized Enriques period lattice -- the group governing the corresponding branch
is the image in $\Orth(\delta^\perp)$ of the stabilizer of $\bZ\delta$ inside
$\Gamma_{\En, 2}$; this is the minimal group making the period-domain inclusion
$$
\bD(\delta^\perp) \injects \bD(T_\En)
$$
equivariant.
Since $T_\Co \cong \delta^{\perp T_\En}$ for a $(-2)$-vector $\delta$ [@DK13],
this refines the arithmetic group $\Gamma_{\Co, 2}$ of the moduli summary, and the
two descriptions agree exactly when the polarized root orbit is unique.
\todo{note-vs-section discrepancy: the branchwise notes define $\Gamma_{\Co,2}$ as the stabilizer-image of a marked Coble root in $\Gamma_{\En,2}$, whereas the moduli summary defines it as $\mathrm{Stab}_{\Orth(T_\En)}(T_\Co)$; these should be reconciled through $T_\Co \cong \delta^{\perp T_\En}$.}
:::

::: {.question ref="que:coble_root_orbit_uniqueness"}

Is the orbit of admissible Coble roots under $\Gamma_{\En, 2}$ unique, so that the
branchwise polarized Coble locus collapses to a single normalized divisor?
Two routes to an affirmative answer are available: an arithmetic double-coset
computation for the polarized subgroup $\Gamma_{\En, 2}$, or a geometric argument
that the $D_4$-symmetry of the Horikawa model acts transitively on the
torus-fixed-point branches.
\todo{cite: Namikawa's root-orbit uniqueness, which is stated only modulo the full Enriques group $\Gamma_\En$ and does not settle the finite-index subgroup $\Gamma_{\En,2}$.}
:::

## The KSBA stable pair

::: {.remark}

The ambient degree-$2$ Enriques picture is settled.
For a degree-$2$ numerically polarized Enriques surface $(Z, [\mathcal L_Z])$, the
ramification divisor $R_Z$ of the associated double cover of a quartic del Pezzo
surface is ample, $\QQ$-Cartier, and lies in the polarizing system, so the pair
$(Z, \varepsilon R_Z)$ is log canonical for $0 < \varepsilon \ll 1$ and
$F_{\En, 2}$ admits a KSBA compactification $\overline{F_{\En, 2}}$ [@CDL25; @AEGS25].
The Coble stable pair is the descent of this picture along the quotient by the
Enriques involution $\iota_\En$, which for Coble surfaces is *not* fixed-point
free.
:::

::: {.remark}

The intended KSBA boundary object is a pair
$$
(\bar S, \varepsilon R_{\bar S}), \qquad 0 < \varepsilon \ll 1,
$$
where $\bar S$ is the stable quotient surface and $R_{\bar S}$ is the descended
ramification divisor.
The divisor is identified; establishing that this pair is KSBA stable remains a
research program with the following open obligations:

- that $R_{\bar S}$ is $\QQ$-Cartier;

- that $R_{\bar S}$ is ample -- expected to follow by descending the ample
  ramification divisor from the K3 cover, that is, by pulling back
  $K_{\bar S} + \varepsilon R_{\bar S}$ to $\varepsilon R_X$ with $R_X$ coming from
  the $(2,2)$-divisor on $Y = \PP^1 \times \PP^1$, rather than by asserting
  stability of the quotient directly;

- that $(\bar S, \varepsilon R_{\bar S})$ is slc, for which one proposed route runs
  through the du Val singularities on the K3 cover and a finite quasi-étale
  quotient in codimension one;

- and a controlled account of how the anti-bicanonical $(-4)$-curve is seen on the
  smooth resolution versus on the stable model.
:::

::: {.conjecture ref="conj:coble_quarter_singularity"}

On the stable quotient $\bar S$, an $A_1$-node of the K3 cover fixed by
$\iota_\En$ descends to a cyclic quotient singularity of type $\frac{1}{4}(1,1)$,
and the anti-bicanonical $(-4)$-curve on the smooth Coble resolution is the curve
contracted to this point.
In the Horikawa model on $Y = \PP^1 \times \PP^1$ with $\tau(x,y) = (-x,-y)$
[@Hor77], the local input producing the $A_1$-node on the double cover is a
$\tau$-invariant $(4,4)$-curve passing through a $\tau$-fixed point with
nondegenerate quadratic term.
:::

::: {.remark}

The local singularity package of \cref{conj:coble_quarter_singularity} is central
to the program, but it is currently a migrated research claim rather than a proven
statement; it is precisely the input awaited by the slc and ampleness
verifications above.
:::

## The restricted ramification semifan

::: {.conjecture ref="conj:restricted_ramification_semifan"}

The semitoroidal model of the polarized Coble locus is obtained by restricting the
Enriques ramification semifan of the degree-$2$ compactification problem to the
hyperplane cut out by the Coble root, and keeping exactly those walls whose
relative interiors meet the Coble positive cone.
Under this restriction, a Coble wall is irrelevant precisely when every Enriques
wall restricting to it is already irrelevant.
:::

::: {.remark}

Proving that this restriction defines the semitoroidal fan requires showing that
no extra roots appear after restriction, that no essential Enriques wall collapses
or restricts trivially, and that running Vinberg's algorithm on the restricted
lattice is not conflated with a proof of the fan itself.
:::

## Comparison with the KSBA compactification

::: {.remark}

The KSBA stable limits sit inside the K3 stable-pair family of the
degree-$(2,2,0)$ problem via the embeddings of
\cref{lem:locally_closed_embedding_BB}.
The proposed comparison proceeds by restricting the universal K3 stable-pair
family over $F_{(2,2,0)}$ to the Coble Noether-Lefschetz locus $\bD(r^\perp)$,
extending the Enriques involution over the stable limits by uniqueness of KSBA
limits, descending the ramification divisor, and matching the induced boundary
stratification against the restricted ramification semifan of
\cref{conj:restricted_ramification_semifan}.
:::

::: {.conjecture ref="conj:ksba_semitoroidal_comparison"}

After normalization, the KSBA compactification of the polarized Coble locus agrees
with the semitoroidal compactification induced by the restricted ramification
semifan.
:::

::: {.conjecture ref="conj:no_moduli_loss"}

The stable quotient remembers the marked Coble root.
Geometrically, this memory is carried by the $\frac{1}{4}(1,1)$ singularity of
\cref{conj:coble_quarter_singularity} -- equivalently, by the contracted
anti-bicanonical $(-4)$-curve on the resolution -- so that degenerations differing
only by their marked root are not identified.
Without this memory the restricted semifan would be too fine for the actual KSBA
boundary, and the comparison of \cref{conj:ksba_semitoroidal_comparison} would
fail.
:::

::: {.remark}

\cref{conj:ksba_semitoroidal_comparison} remains open on four counts:
root-orbit uniqueness (\cref{que:coble_root_orbit_uniqueness}), the
ramification-semifan restriction identity
(\cref{conj:restricted_ramification_semifan}), the no-moduli-loss statement
(\cref{conj:no_moduli_loss}), and the exact cusp enumeration.
The boundary dictionaries and cusp tables appearing in preliminary work remain
unverified pending the restriction theorem and an explicit cusp computation.
:::

## Boundary cusp data

::: {.remark}

The boundary is organized by cusp pairs marked with a Coble root.
A $0$-cusp is modeled by an orbit of a pair $(I, r)$ consisting of an isotropic
line $I$ and a compatible Coble root $r$, and a $1$-cusp by an orbit of a pair
$(J, r)$ consisting of an isotropic plane $J$ and the same root, with incidence
recorded by the containment $I \subset J$ preserving $r$.
A root $r$ is *admissible* at a cusp when it lifts to a primitive $(-2)$-root of
the ambient Enriques lattice lying in the designated Coble orbit; this is the datum
that promotes plain Enriques cusp data to polarized Coble cusp data, and it must be
preserved along the incidence $I \subset J$.
:::

::: {.question ref="que:coble_cusp_admissibility"}

What is the precise admissibility test for Coble roots at a cusp, formulated
against the folded K3-to-Enriques Coxeter data?
Sterk cusps $3$ and $5$ are the delicate cases where additional reflection data may
intervene.
:::

::: {.remark}

Any actual cusp count must reduce to explicit lattice-orbit work -- through Sterk's
representatives (five $0$-cusps and nine $1$-cusps for the Enriques space [@Ste91])
together with their stabilizers, or direct period-domain enumeration -- and
discriminant-form shortcuts suggest candidates but do not by themselves prove the
cusp diagram.
One durable exclusion is nonetheless available: since primitive isotropic vectors
of $T_\Co$ pair evenly in the ambient Enriques lattice, they have divisibility $2$
(\cref{lem:divisibilityAlwaysTwoTco}), so the divisibility-one Sterk cusp $1$ does
not occur on the polarized Coble boundary and only the divisibility-two Sterk cusps
$2$--$5$ are in play.
This is consistent with the cusp correspondence of
\cref{thm:cusp_correspondence}, under which the unique Coble $0$-cusp corresponds
to a divisibility-two Enriques cusp.
:::
