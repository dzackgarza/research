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
summand, and $ho_	en(\gent)$ is the group computed from isometries of $	en$ itself. The script
also prints the $M$-orbit partition on the $528$ isotropic classes on each side, which must agree as
a multiset — the two lattices' discriminants are distinct quadratic spaces a priori, and this is what
identifies them.

It also prints the revision *sources* rather than the module paths: the port clone's `git rev-parse
HEAD`, the provider snapshot's declared version line, and a `sha256` of
`orthogonal_quotients.py` — the file that owns `discriminant_preimage` and the character-data
machinery the result rests on.

## Status

The numbers are being produced by the three jobs named in the commit that added this file:
`jmw6b7spz` (this script), `jmw6ab5wm` (`cusps(1)` and the stabilizer images), `jmw69fxhq`
(`cusps(2)`). They are folded in here as they land, and only then does the vector/plane comparison
become a result rather than a route. Nothing above is a count.
