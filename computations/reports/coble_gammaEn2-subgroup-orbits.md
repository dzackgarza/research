# $\Gamma_{\En,2}$ through the public preimage route

Script: `coble_gammaEn2-subgroup-orbits.py`; transcript `coble_gammaEn2-subgroup-orbits-run.txt`.
Revisions the run prints for itself: `sage-indefinite-port` `991b88b095a42a1e3679569ea42328c900c120f6`
(`.scratch/port-held`) with `sage-extensions` `cdafca84065405cb810bba047f8a965299b03762` (the pin that
port declares, bound at `/prov`), Sage `11.0.beta5`.

## The route, and why no anti-isometry has to be built

The library carries the constructor this needs — `O_L.discriminant_preimage(H)`, which returns
$\rho_L^{-1}(H)$ as a predicate subgroup of $\Orth(L)$ with the finite character datum
`{"discriminant_preimages": (H,)}` (`lattice_morphisms.discriminant_preimage`, consumed by
`orthogonal_quotients.OrthogonalCharacterQuotient` and `PredicateSubgroups.character_data`). So
$\gent = \rho_{\ten}^{-1}(M)$ is expressible without listing a single generator of $\gent$.

The remaining question was how to name $M \le \Orth(A_{\ten},q_{\ten})$. By
`@lem:gamma-transport-identity` in `writing/coble/lattices-and-moduli/lattices.md` no transport is
needed: $A_{\sen}$ and $A_{\ten}$ agree summand by summand ($A_U = 0$), both forms are
$\ZZ/2\ZZ$-valued, so $q_{\ten} = q_{\sen}$ and the gluing anti-isometry can be taken to be the
identity. The nine generators of `@prop:polarization-stabilizer-enriques` — the reflection in
$u_0-w_0$ and the eight reflections in the simple roots of $E_8(2)$ — are isometries of $\ten$ itself,
so their discriminant images are elements of $O(A_{\ten},q_{\ten})$ that the library can build, and
$M$ is the subgroup they generate.

## What the run decides, and how

| call | what it must return, and why |
|---|---|
| `O_T.subgroup(images)`, `\|M\|` | $696\,729\,600 = \abs{W(E_8)}$ (`@thm:coble-heegner-finite-orbits`): a check on the group, not a result of it |
| `T.Aut().discriminant_preimage(M)` | the predicate subgroup $\rho_{\ten}^{-1}(M) = \gent$, with complete character data |
| `\gent.isotropic_orbit_representatives(1)` | the $\gent$-orbits of primitive isotropic **lines**, i.e. the $0$-cusps of $\fen$: published **five** [@AEGS25 §3.3 p. 590; @Ste91 Prop. 4.2.3 p. 16] |
| `\gent.isotropic_orbit_representatives(2)` | the $\gent$-orbits of primitive isotropic **planes**, i.e. the $1$-cusps: published **nine** [@AEGS25 §3.3 p. 590] |
| the same two for `T.Aut()` | the full-group counts, so the collapse from $\Orth(\ten)$-orbits to $\gent$-orbits is visible in one run: two of rank one (AEGS §3.2, reproduced as job `jmw6ab5wm`), and the rank-two number that job `jmw69fxhq` is computing |

These are lattice orbits with stabilizers, not discriminant walks; the finite strata of
`coble_gammaEn2-card-run.txt` (`1 + 4 + 5` over image dimension $0,1,2$, against nine published
$1$-cusps) are the finite-shadow computation and are not summed into a count.

## The marking, checked rather than assumed

`coble_gammaEn2-marking.py` makes the choice of $\gamma$ explicit and tests it. In each of $\sen$ and
$	en$ it computes the summand subspace $A_{U(2)}\subseteq A$ from the $U(2)$ slots ($4$ classes) and
its orthogonal complement $A_{E_8(2)}$ ($256$ classes), then reads off the nine generators' images:

- the eight $E_8(2)$-root reflections must fix $A_{U(2)}$ pointwise and preserve $A_{E_8(2)}$;
- the $U(2)$ reflection in $u_0-w_0$ must fix $A_{E_8(2)}$ pointwise.

If both hold on both lattices, the summand-wise identification is the canonical marking: the two
nine-element families correspond generator by generator under it, $\gamma$ is the identity on each
summand, and $
ho_	en(\gent)$ is the group computed from isometries of $	en$ itself. The script
also prints the $M$-orbit partition on the $528$ isotropic classes on each side.

**Equal orbit-size multisets do not identify the two marked actions**, and an earlier version of this
paragraph said they do. Two separate statements are needed, and only the second is what a count
requires:

*Identification.* What makes the $\sen$-side family and the $\ten$-side family the *same* family is a
generator-level statement: with $\gamma$ the summand-wise map, one must have
$\gamma\rho_{\sen}(g_i)\gamma^{-1} = \rho_{\ten}(g_i)$ on all $1024$ classes, generator by
generator. The summand-fixing tests in the script are the first half of that check — they show each
generator acts on the correct summand — and not the whole of it.

*Invariance of the count.* This is all the cusp number needs, and it does not need identification: two
admissible anti-isometries differ by an isometry $\tau\in\Orth(A_\ten,q_\ten)$, since
$q_\ten(\gamma'\gamma^{-1}y) = q_\ten(y)$ for both being anti-isometries; then
$M' = \tau M\tau^{-1}$, and conjugating by an isometry permutes the orbit partition pointwise, so the
number of orbits — hence the predicted number of cusps — is the same for every admissible marking.

It also prints the revision *sources* rather than the module paths: the port clone's `git rev-parse
HEAD`, the provider snapshot's declared version line, and a `sha256` of
`orthogonal_quotients.py` — the file that owns `discriminant_preimage` and the character-data
machinery the result rests on.

## The first marking run, collected

Job `jmw6bcuf0` finished (exit 0, 21 min 42 s) and printed, for both lattices, the $M$-orbit partition
on the 528 isotropic classes:

```
S_En: A_{U(2)} = 4 classes; isotropic classes 528
  M-orbits on the isotropic classes: 5, sizes [270, 135, 120, 2, 1]
T_En: A_{U(2)} = 4 classes; isotropic classes 528
  M-orbits on the isotropic classes: 5, sizes [270, 135, 120, 2, 1]
```

That is the same partition as `coble_gco_orbit-decomposition-run.txt` and `coble_gammaEn2-card-run.txt`,
and it is *not* an identification: equal multisets, as the section above says, do not identify two
marked actions.

Two of that run's three structural checks were also invalid as coded: `A_{E8(2)}` was tested as the
**set** complement of `A_{U(2)}` (1020 classes) rather than as its **orthogonal** complement (256
classes), so "the eight root reflections preserve $A_{E8(2)}$" was vacuous and "the $U(2)$ swap fixes
$A_{E8(2)}$ pointwise" reported `False` about the wrong set. The script has been rewritten: it now
computes $A_{E8(2)}$ as the span of the $E_8(2)$-slot classes, builds the anti-isometry $\gamma$
explicitly as the $10\times10$ matrix over $F_2$ matching the ten summand generators slot by slot,
checks that $\gamma$ preserves $q$ on all 1024 classes, and then tests the identification itself:

$$\gamma\,\rho_{\sen}(g_i)\,\gamma^{-1} = \rho_{\ten}(g_i)\quad\text{on all 1024 classes, for } i = 1,\dots,9,$$

together with the pointwise agreement of the two orbit partitions under $\gamma$ rather than their
multisets. That run is job `jmw6c9xfj`; its transcript is `coble_gammaEn2-marking-run.txt`.

## The identification, computed

The corrected rerun of the marking script in the foreground built $\gamma$ explicitly and tested the
generator-level statement. Attribution: the first background job `jmw6c9xfj` **failed** (exit 1) on the
column/bit-mask bug in the same script, not completed; the successful output recorded here comes from
the corrected foreground run, and that run's exit status was 0. Calling the failed job's status
"exit 0" in the earlier version of this note was wrong.

```
S_En: ten generator classes span 1024 classes (rank 10); A_{U(2)} order 4
T_En: ten generator classes span 1024 classes (rank 10); A_{U(2)} order 4
  coordinate matrices of the ten generators: det(S) = 1, det(T) = 1
  gamma as a 10 x 10 matrix over F_2: invertible = True
  gamma preserves q on all 1024 classes: True

the identification, generator by generator
  generator 1 ... 9: transported equals the T_En counterpart on all 1024 classes: True
  identification holds for all nine: True
  gamma maps the isotropic classes onto the isotropic classes: True
```

So the transport is not merely *an* admissible anti-isometry: there is an explicit $\gamma$, carrying
the ten summand generators of $A_{\sen}$ to the ten summand generators of $A_{\ten}$ slot by slot,
which preserves $q$ on all 1024 classes and satisfies

$$\gamma\,\rho_{\sen}(g_i)\,\gamma^{-1} = \rho_{\ten}(g_i)\qquad (i = 1,\dots,9)$$

on all 1024 classes. The two nine-generator groups are therefore the same subgroup of the same
orthogonal group under this identification, and $\rho_\ten(\gent) = M$ *is* the transport of
$\rho_{\sen}(\Stab_{\Orth(\sen)}(h))$ — the geometric identification of `@lem:gamma-transport-identity`,
now checked generator by generator rather than inferred from equal orbit sizes.

## Status

The numbers are being produced by the three jobs named in the commit that added this file:
`jmw6b7spz` (this script), `jmw6ab5wm` (`cusps(1)` and the stabilizer images), `jmw69fxhq`
(`cusps(2)`). They are folded in here as they land, and only then does the vector/plane comparison
become a result rather than a route. Nothing above is a count.
