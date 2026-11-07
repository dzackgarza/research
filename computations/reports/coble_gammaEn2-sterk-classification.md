# The Enriques group and its plane classification, from the published part I

Sources, read directly: `tmp/sources/sterk-1991-period-space-i.pdf` (H. Sterk,
*Compactifications of the period space of Enriques surfaces. I*, Math. Z. 207 (1991) 1-36), and
`tmp/sources/sterk-1988-thesis.pdf` (Sterk's Nijmegen thesis of 1988, matching content with the
section numbers shifted by one). The thesis that Zotero files under part II is the 1988 thesis and
is cited as such, not under that attachment label.

## The group, identified against $\Gamma_{\En,2}$ and not confused with $\Orth(\ten)$

Sterk §2 (pp. 6-8) introduces $F$ as the image in $\Orth(L^-)$ of
$\{g\in\Orth(L): g\circ I = I\circ g,\; g(e+f,e+f,0) = (e+f,e+f,0)\}$, which is AEGS Def. 2.6's
definition of $\gent$. **The containment is not a direct sum**: $L^+\oplus L^-\subsetneq L$, and the
embedding is of finite index, $[L:L^+\oplus L^-]=\abs{A_{S_\En}} = 2^{10}$ by the discriminant-form
gluing. In particular $L$ is not integrally $L^+\oplus L^-$.

**Proposition 2.7 (Sterk, p. 7).** That image $F$ is exactly the set of integral isometries of $L^-$
whose induced map on the discriminant described there, $L_-^*/L_-\cong
\tfrac12 H(2)/H(2)\ \oplus\ \tfrac12 E_8(-2)/E_8(-2)$, **respects the decomposition into two
summands**. Its proof proceeds by lifting integral isometries through the invariant lattice and its
polarization stabilizer (the same gluing route as `@prop:gamma-en-two-gluing`), and uses the
decomposition $(e+f)^\perp = \ZZ(e-f)\oplus E_8(-2)\cong A_1(-2)\oplus E_8(-2)$ displayed on that page.

**Remark 2.8 (Sterk, p. 7).** $F$ does not equal the set of stabilizers of the *discriminant element*
$\tfrac12(e'-f')+L_-$: the transformation computed there satisfies $\psi(\tfrac12(e'-f')+L_-)
= \tfrac12(e'-f')+L_-$ and yet $\psi\notin\Gamma$. This is a statement about a **finite**
discriminant-element stabilizer, not about an integral vector stabilizer; it says that preserving the
class of that vector does not put an isometry in $F$.
It is not a statement about the integral polarization stabilizer of the gluing construction, and is
not used here to reject that construction: the integral statement has its own reason for not being
$F$ (infinite index in $\Orth(\ten)$, established earlier from the index $2^7\cdot17\cdot31$), and is
independent of this remark. The remark does rule out using $\Stab_{\Orth(q_\ten)}([h/2])$ as the group
to count with, because that is exactly the discriminant-element stabilizer that is too big.

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
  | $\{4,5\}$ | $\Gamma^1(2)$ |
  | $\{3,5\}$ | $\Gamma^1(2)$ |
  | $\{3,4\}$ | $\Gamma^1(2)$ |
  | $\{5,5\}$ | $SL_2(\ZZ)$ |

(Read off the summary table in the page image on p. 28: $\Gamma(2)$, and $\Gamma^1(2)$ with the
superscript 1, not OCR's $E_1(2)$ / $F_1(2)$.)

## What enters the arithmetic-fibre criterion

Consequence for the plane side of #748: the published classification splits the planes by *type*
(the parabolic diagram, the vectors each plane contains, and the group $\mathcal F(F)$), not by a
single scalar invariant like $\varPi^*/\varPi$. Each plane has its own datum and its own boundary
group, and identities between types must be decided by the stabilizers of lifts, not by summing
finite-plane orbits. Whether any two types share a finite plane image is a separate check, by
constructing those representatives' images; it is not inferred here, and is not used as a premise for
a cusp count.

The operation that decides the question on the full lattice remains
`Gamma_En,2.isotropic_orbit_representatives(rank=2)` for the group constructed as
`T_En.Aut().discriminant_preimage(M)` with $|M| = 696\,729\,600$ [@thm:coble-heegner-finite-orbits];
it is running as `jmw6b7spz`, and a failure there would be filed with that call and its traceback.
Nothing here is a count.

## Worked computation under §4.3.16, in the full lattice

For $E = \ZZ e\oplus\ZZ f'$ (the generator $e$ of the unscaled $U$, $f'$ of $U(2)$):

- the primitive-image hypothesis is exactly $(e,\ten) = \ZZ$ and $(f',\ten) = 2\ZZ$, so any integral
  normalizer has odd first-row entry and even second-row entry, giving $\mathcal F(E)\cap SL(E)
  \cong \Gamma^1(2)$ (printed), a level-2 modular subgroup;
- the Smith normal form of the basis-times-Gram matrix has elementary divisors $1,2$, while the
  basis itself has primitivity index 1. **$\abs{E^*/E} = 2$** and $E$ is primitive.
- a rank-4 direct calculation shows $E^* = \ZZ e\oplus \ZZ(f'/2)$, making the discriminant datum the
  order-two subgroup generated by $[f'/2]$; a vector $a e + b f'$ pairs integrally with the whole
  lattice iff $a\in\ZZ$ and $b\in\tfrac12\ZZ$;
- the orthogonal complement of $E$ inside $U\oplus U(2)$ is $E$ itself, whence
  $E^\perp/E$ is the full $E_8(2)$-summand: that is one of the four types of §4.3.16, namely type
  $E_8$, with no cusp identification and half-plane component over $\Gamma^1(2)$.

This ties the source's datum, quotient lattice and normalizer together for **one** published type,
and it places that type in the dimension-one stratum of the finite-plane data, as Lemma 4.3.15 and
the example of §4.3.16 say it should be. It is not a classification of the other eight types nor a
claim about any other finite plane image.

## Run defect report

`jmw6ab5wm` (the `cusps(1)` + stabilizer-image run) has ended (exit status 0 after 1 h 32 min), but
its complete captured output is only

```
|A| = 1024, |O(q)| = 46998591897600, isotropic classes 528
cusps(1): 2 records   (729 s)

cusp 0: representative Integral lattice of rank 1 and signature (0, 0)
  generator v: square 0, div 1, class q = [0]
```

After `T.cusps(1)` returned two records in 729 s and the first representative's vector data was
printed, the wrapper ended. It reported exit 0 with no traceback. No `probe_stab2` process survives;
`ps` shows only the other two jobs. So the call `rec.stabilizer_generators()` never returned an
answer through the wrapper; the exit status is a wrapper status, not the completion of the
computation, and `--exit 0` must not be read as a computed stabilizer image. No public-operation
result is claimed absent on that basis: the criterion's two remaining inputs are exactly that image
and the class stabilizer, and the other two jobs are alive and computing the orbit pieces.
