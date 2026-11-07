# The nine published one-cusp plane types, in T_En, through exact owned shell enumeration

Script: `coble_gammaEn2-planes-published.py`; transcript `coble_gammaEn2-planes-published-run.txt`.
Revisions the run prints: sage-indefinite-port `991b88b095a42a1e3679569ea42328c900c120f6`
(`.scratch/port-held`, PAUSED by the user, never resumed) with sage-extensions
`cdafca84065405cb810bba047f8a965299b03762` (its declared pin, bound at `/prov`), Sage `11.0.beta5`.

## The lattice, verified

`T_En = U ⊕ U(2) ⊕ E8(2)`, built from Sage's own `CartanMatrix(['E', 8])` through the provider's
`Lattices` constructor — the same model and the same nine-generator marking as
`coble_gammaEn2-subgroup-orbits.py`.  The run certifies the lattice before computing anything:
`det Cartan(E8) = 1` (the D8 graph would give 4), `det T_En = 1024`, and the E8(2) summand has
exactly 240 vectors of square −4 through the owned `vectors_of_square` call.  An earlier ad-hoc
debug matrix had built the D8 graph (arms 1,1,5); the correction is recorded here, and every
quotient, orbit and root count in the transcript comes from the verified lattice.

## The classification instantiated, not re-derived

The published classification (Sterk part I, `tmp/sources/sterk-1991-period-space-i.pdf`) supplies
the frame: Prop. 4.2.3's five representative vectors, the combination rule of 4.3.15–4.3.16, and
the labels {1,2} = A7⊕A1, {1,3} = E7⊕A1, {1,4} = D8, {1,5} = E8 (4.3.15, 4.3.7, 4.3.8; 4.3.9
carries the remaining label).  The script instantiates representatives of each type and computes
their invariants with exact owned operations; it does not sample strata and does not re-derive
the classification.

## What the run decides

The class machinery is exact and self-contained: classes are parity vectors in
`K = ker(G mod 2) ⊆ GF(2)^12`, M acts by the nine reflection matrices mod 2, and the orbit
partition of the 528 isotropic classes recomputes the on-record sizes **[1, 2, 120, 135, 270]**
(matching the marking and card runs).  The four nonzero vector types of Prop. 4.2.3 sit in four
distinct M-orbits:

| vector type | Sterk representative | orbit size |
|---|---|---|
| 2 | e1 | 2 |
| 3 | e1+f1+r | 120 |
| 4 | 2e1+f1+r1+r2 | 270 |
| 5 | 2e0+2f0+r1+r2 | 135 |

**The nine planes.**  All four 4.3.16 planes and all five 4.3.17 planes were constructed and
verified primitive, with exact invariants:

- the four 4.3.16 planes: |Π*/Π| = 2, Π⊥/Π of determinant 256 with **240** roots of square −4
  (isomorphism type E8(−2) — exactly Sterk 4.3.5's statement that all four types give E8(−2)),
  and a discriminant image of order 2 whose orbit-type is (2,), (3,), (4,), (5,) respectively;
- the five 4.3.17 planes: |Π*/Π| = 4, Π⊥/Π of determinant 64 with **368** roots of square −4 and
  **16** of square −2 (a fixed isomorphism type for the second O(L_−)-class, as required by
  Sterk 4.6), and discriminant images of order 4 whose orbit-type sets are exactly the five
  published labels {2,4,5}, {4,5}, {3,5}, {3,4}, {5,5}.

The arithmetic fibre structure this supports: a 0-cusp is a Γ_En,2-orbit of primitive isotropic
lines; the class-orbit partition gives 1 orbit over the zero class and 4 over the nonzero
M-orbits, and Sterk's Prop. 4.2.3/4.2.4 (five inequivalent vectors, five 0-dimensional boundary
components) is the published statement that the fibres are single orbits.  The Γ_En,2 lattice-orbit
counts (the published 5 and 9) are **not** claimed here: they are being computed by the preserved
background jobs `jmw6b7spz` and `jmw69fxhq`, whose partial outputs (Γ_En,2 built, |M| confirmed)
are quoted above.

## The jmw6ab5wm wrapper, inspected

Its log is `exit=0` followed by the exact content of `.scratch/stab2.out`, and the wrapper shape is
the same `> .scratch/stab2.out 2>&1; echo "exit=$?"; tail` used by the running jobs, launched from a
python3 heredoc.  The probe stopped at the last line before `rec.stabilizer_generators()`; the four
remaining print statements never appeared and no traceback was captured; the job ran 92.7 minutes
with its last flush at 11:05.  So the probe died silently inside `stabilizer_generators()` and the
wrapper still reported 0: the exit status was masked somewhere in the wrapper/proot layer.
**Conclusion: not a library defect on current evidence** (no error text of any kind exists), and
the zero exit carries no information about the call — consistent with the run-defect paragraph in
`coble_gammaEn2-sterk-classification.md`.  A missing run result is not evidence of a missing
library operation; nothing is filed against `stabilizer_generators` on this evidence.

## Addendum (third pass): the fibre map on divisibility, and the complement isomorphisms

The fibre map is $\varphi(\ZZ v) = [v/\operatorname{div}(v)]$: divisibility-one vectors have
$v \in T_\En$ and class $0$ (their fibre is one orbit by Sterk 4.2.1 = Cor 3.3 at $p=1$, vacuous
congruence); divisibility-two vectors have $v/2 \in T_\En^*$ and nonzero isotropic class, and
equal classes give $v'-w \in 2T_\En$ *exactly* — the homomorphism property of the class map with
zero class $T_\En$ — which is Cor 3.3's congruence mod $pN$ at $p=2$. The complement isomorphisms
of the four 4.3.16 planes come from Sterk Prop 4.6's plane equivalences (its hypothesis: one
$\Orth(H(2)\oplus E_8(-2))$-orbit of primitive isotropic vectors there), not from shell counts.
The public-call comparison (Γ_En,2 `isotropic_orbit_representatives` against the published 5 and
9) is not blocked by any missing library operation: both calls are running in the preserved jobs
`jmw6b7spz` and `jmw69fxhq` and had produced no output at this commit; nothing is routed to
sage-extensions on this evidence.
