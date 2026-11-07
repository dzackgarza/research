# The Enriques group and its plane classification, from the published part I

Sources, read directly: `tmp/sources/sterk-1991-period-space-i.pdf` (H. Sterk,
*Compactifications of the period space of Enriques surfaces. I*, Math. Z. 207 (1991) 1-36), and
`tmp/sources/sterk-1988-thesis.pdf` (Sterk's Nijmegen thesis of 1988, matching content with the
section numbers shifted by one). The thesis that Zotero files under part II is the 1988 thesis and
is cited as such, not under that attachment label.

## The group, identified against $\Gamma_{\En,2}$ and not confused with $\Orth(\ten)$

Sterk §2 (pp. 6-8) writes $L = L^+\oplus L^-$ for the eigendecomposition associated to an
Enriques involution $I$, and defines **F** as the image in $\Orth(L^-)$ of
$\{g\in\Orth(L): g\circ I = I\circ g,\; g(e+f,e+f,0) = (e+f,e+f,0)\}$, which is AEGS Def. 2.6's
definition of $\Gamma_{\En,2}$ (my $\gent$).

**Proposition 2.7 (Sterk, p. 7).** That image $F$ is exactly the set of isometries of $L^-$ whose
induced map on $L_-^*/L_-\cong\tfrac12 H(2)/H(2)\cong E_8(-2)/E_8(-2)$ **respects the decomposition
into the two summands**. Its proof proceeds by lifting integral isometries through the invariant
lattice and its polarization stabilizer, exactly the gluing route of `@prop:gamma-en-two-gluing`.

**Remark 2.8 (Sterk, p. 8).** Contrary to what one might hope, $F$ does not equal
$\{g\in\Orth(L^-): g\ \text{stabilizes } \langle e'-f'\rangle + L\}$. A Siegel-Eichler transformation is
exhibited that stabilizes that line and lies in $F$.

This is the canonical published identification and it *cannot* be replaced by the
$\Stab_{\Orth(\ten)}(h)$ of the earlier batch, which Sterk 2.8 excludes by name; it also matches the
infinite-index argument already on file.

The Enriques group itself is $\Gamma_\En = \Orth(L^-)$, **not** $F$; the degree-$2$ polarized group
used to classify the cusps of $\fen$ is $F = \Gamma_{\En,2}$.

## How the classification of vectors and planes proceeds (§4.2-§4.3)

- **§4.2.** The zero-dimensional boundary components are the $F$-orbits of primitive isotropic
  *rank-one sublattices* of $L_-$ — lines, as my record now states and proves from $-\mathrm{id}$.
- **Lemma 4.3.4.** For each of the five representatives $v$ of Prop. 4.2.3, $v^\perp/\ZZ v$ is the
  hyperbolic lattice needed for Vinberg: $H\oplus E_8(-2)$ (i.e. $H(+)$ in the notation of Sterk p. 7)
  for $v\neq e$, and $H(2)\oplus E_8(-2)$ for $v=e$.
- **§4.3.1.** If $\mathcal F$ is a primitive isotropic plane containing $v$, then $\mathcal F$
  determines an isotropic line of $v^\perp/\ZZ v$; hence the planes are computed by the maximal
  parabolic subdiagrams of the chamber diagrams of the reflection groups $G_v$, per v.
- **§4.3.15.** Whether two primitive isotropic vectors can combine to form a plane is decided by
  type: "the first isotropic vector of the list (4.2.3) can be combined with any of the other four
  types to yield a primitive isotropic plane, but there is no isotropic plane all of whose primitive
  isotropic elements are equivalent to $e$."

## The nine one-cusps and their boundary groups

$\mathcal F(F)$ denotes $N_F(\mathcal F)/Z_F(\mathcal F)$, the group acting on the half-plane of an
isotropic plane. Two classes of cases:

- **§4.3.16:** the four types **$E_8$, $D_8$, $A_7\oplus A_1$, $E_7\oplus A_1$**, each built from
  non-equivalent vectors, whose boundary components are half-planes over the level-2 modular groups
  with no identification of cusps;
- **§4.3.17:** the remaining five, computed via Siegel-Eichler transformations, with
  | type | group $\mathcal F(F)\cap SL(\mathcal F)$ |
  |---|---|
  | $\{2,4,5\}$ | $\Gamma(2)$ |
  | $\{4,5\}$ | $\Gamma_1(2)$ |
  | $\{3,5\}$ | $E_1(2)$ |
  | $\{3,4\}$ | $F_1(2)$ |
  | $\{5,5\}$ | $SL_2(\ZZ)$ |

(Labels read from §4.3.17 as printed; $\Gamma(2)$ is the level-2 subgroup, $\Gamma_1(2)$ has the
$b$-entry even. Notation 3.1 of AEGS follows this same closure labelling.)

## What enters the arithmetic-fibre criterion

Consequence for the plane side of #748: the published classification splits the planes by *type*
(the parabolic diagram, the vectors each plane contains, and the group $\mathcal F(F)$), not by a
single scalar invariant like $\varPi^*/\varPi$. The same finite plane image can therefore carry
several types, and only a theorem about the stabilizer of a chosen lift decides whether they are
identified by $\gent$. This is why the finite plane strata cannot be summed into a cusp count, and why
a search by $B$ in rank $4$ would not establish it anyway.

The operation that decides the question on the full lattice remains
`Gamma_En,2.isotropic_orbit_representatives(rank=2)` for the group constructed as
`T_En.Aut().discriminant_preimage(M)` with $|M| = 696\,729\,600$ [@thm:coble-heegner-finite-orbits];
it is running as `jmw6b7spz`, and a failure there would be filed with that call and its traceback.
Nothing here is a count.
