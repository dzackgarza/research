# #807: the widened smooth-member Coble family

**Status**: PROVED #7. The argument was read only by the model that wrote it.

  self: PASS: self-reading covered statement scope, all examples, the E8 proof, deformation and connectedness inputs, and monodromy separation; not independent

Independent DeepSeek review is pending. Acceptance item 2 of the issue (an independent Kimi MET review) remains NOT MET.

## Decision

Over the complex numbers, let S be a Coble surface in the sense of Dolgachev–Zhang, Introduction, with |-2K_S|={C} and C one connected smooth curve, together with its anti-bicanonical double cover and involution. Then:

1. Non-classical objects exist. The surfaces S_Z8 and S_Z64 are objects of the cover-retaining stack, but neither has any presentation as the blow-up of P^2 at ten distinct ordinary nodes of an irreducible plane sextic.
2. The classical objects form an open, dense, connected, irreducible substack strictly smaller than the full stack. Every non-classical object is therefore a limit of classical objects. There is no additional connected or irreducible component.
3. Thus the issue's dichotomy (every object classical, or a further component) is false. No identity of the widened stack with the classical quotient is asserted.

## Decisive reduction

Smoothness implies reducedness. Dolgachev–Zhang Definition 6.1 puts every object in the K3-type case and Lemma 6.2 gives the normal K3 double cover, smooth in this case. Lemma 1.2(1) and adjunction give p_a(C)=0, C^2=-4 and K_S^2=-1; Proposition 6.4(2) gives terminality. Theorem 6.3 excludes rational type and Theorem 4.3 gives a birational morphism to P^2. The total-transform canonical-class calculation gives ten centres and an irreducible rational plane sextic, all of whose singular and infinitely near singular points are double points. It does not imply ten distinct centres or ordinary nodes.

Conversely, blowing up an irreducible rational sextic at its successive double points resolves it after ten blow-ups because a plane sextic has arithmetic genus 10 and each double-point blow-up lowers delta by one. The strict transform C satisfies C=-2K and C^2=-4, and it is the unique anti-bicanonical member; |−K| is empty.

Dolgachev–Zhang Theorem 6.7 is not a classification theorem: it adds elliptic, terminal, K3-type and invariant-Picard generality hypotheses and concludes finiteness of negative-curve orbits. The non-classical examples have anti-invariant classes, so that generality fails. Example 6.10 has the unique anti-bicanonical divisor R_1+...+R_4+2R_5: nonempty but non-reduced, hence outside the smooth-member family and outside K3 type. Empty, reduced-but-singular and uniquely non-reduced systems are kept distinct.

## Existence of non-classical objects

Z8 is

  (y^2 z - x^3 - 3xz^2 + 4z^3)^2
    + 8z^3(y^2 z - x^3 + 3xz^2 - 2z^3) = 0,

and Z64 is

  (y^2 z - x^3 + 15xz^2 - 22z^3)^2
    + 64z^3(y^2 z - x^3 + 12xz^2 - 16z^3) = 0.

Both are irreducible rational sextics. Their singularities are A_15+2A_1 and A_15+A_1+A_2, so the reduction above makes them objects. Eight resolution curves from the A_15 point and the strict transform of z=0 form an E_8 diagram of (-2)-curves, with R_i=E_i-E_{i+1} and L=H-E_1-E_2-E_3.

The general obstruction is prop:coble-e8-configuration-excludes-ten-distinct-centres. If ten disjoint (-1)-curves existed, unimodularity of E_8 would split Pic(S), a mod-two pigeonhole argument in its rank-three complement would give [E_i]-[E_j]=alpha+2x for an E_8 root alpha, and lifting to the K3 cover would produce a class Gamma of square -2. Riemann–Roch makes Gamma or -Gamma effective. Pushforward then forces E_j+pi_*G=E_i as divisors, impossible because E_i is the only effective divisor in its class. Hence no ten-distinct-point blow-down exists on either surface.

## Open, dense, connected and no new component

Grivaux Proposition 3.1 supplies completeness on the free PGL_3 configuration locus, proving that ten distinct centres and ordinary nodes persist locally. Huybrechts Chapter 6, Corollary 2.7, Remark 2.6, Proposition 2.8 and §2.4 supply the smooth universal deformation, the involution on its base, the local period isomorphism and the (1,1)-hyperplanes. The relative quotient construction turns the nine-dimensional fixed-involution deformation into a family of objects.

Every (-2)-curve or tangent (-1)-curve creates an anti-invariant class of square -4 or -6; without either obstruction every plane presentation is classical. The two norm conditions cut out locally finite proper analytic hypersurfaces, and the still larger countable Noether–Lefschetz union has dense complement. Therefore classical objects are dense in every such local family and every object is a limit of them.

Harris–Morrison §6.E, Initial reductions and (6.45), proves that V_6,0 is irreducible and that node monodromy is the full symmetric group. Hence the labelled classical configuration space is connected and its quotient images are connected and irreducible. With openness and density, this proves there is no further connected or irreducible component.

## Monodromy boundary

There is no extra component whose monodromy remains to be computed. The unconditional aggregate generated by transports in families and by isomorphisms of objects on the invariant lattice is W(E_10), but that aggregate is not automatically the monodromy of the universal stack local system. The stack-local-system clause remains conditional on its chart hypothesis. Nothing here determines Gamma_Co on the anti-invariant lattice, and no plane-model automorphism group replaces the cover-retaining stack.

## Checks and skipped checks

- Exact symbolic substitution and E_8 Gram determinant: PASS, `checks/exact-symbolic.txt`.
- Singular absolute-factor, genus and singularity rerun: PASS, `checks/singular-run.txt`.
- Pandoc parse: no warning.
- `docs_check.py --source`: byte-identical to detached main; 28 pre-existing bibliography findings on other pages, none on this page.
- Dependency graph: same 125 pre-existing findings as main after normalization; no new finding; one new block and 21 new edges.
- `git diff --check`: clean.
- Two targeted pytest commands did not run: collection fails because `dzack_research` is unavailable (pytest exit 4). No Sage suite, full engineering suite, render, or CI result is claimed.
- Independent model reports: pending; they will be recorded before the result is pushed.

Sources read for this result: Dolgachev–Zhang Introduction, §1.1–§1.10, §2.1, §4.1–§4.3, §6.1–§6.7 and Example 6.10; Grivaux Proposition 3.1; Harris Lemma (1.2); Harris–Morrison §6.E, Initial reductions and (6.45); Huybrechts Chapter 1 (2.5) and Chapter 6 Remark 2.6, Corollary 2.7, Proposition 2.8 and §2.4. All citations in the new text use author and numbered statement, not page locators.
