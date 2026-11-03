# Audit addendum: the invariance argument at the corpus's own semantics, and the corrected (D2) bookkeeping

This addendum stakes out two corrections to `smw0_ch-direction-audit.md`, both at the referee's
request. (1) The earlier text's presentation rested the group equality on a *label-own* uniqueness
of the chamber: replaced below by the full chamber-semantics invariance argument, in which the
stabiliser's invariance is proved by tracking transported effectivity between markings, with no
uniqueness-at-one-member hypothesis doing the work. (2) The earlier bookkeeping for the kernel-side
of the (D2) analysis is corrected: the projection artifact is retracted, and the equivalence
`(D2) <=> (RI)` is stated and proved only at the normalised-section reading.

Sources and definitions are those of that audit file; notation as in
`computations/reports/smwo_direct-period.md`.

## 1. The chamber-invariance argument, at its hypotheses

*Base object.* `c` is the tuple's chamber: at a Member `X_b` it is the component of the positive
cone containing the Kahler cone, cut at the member's effective algebraic roots
(`@def:direct-cover-datum` item 6, `writing/coble/heegner-report/coble-heegner-research-report.md`
: 889-896; `@rmk:chamber-not-transported`'s own reading: "the chamber containing the Kahler cone",
the corpus's adopted semantics).

*Pinning.* At every member, `c` is a function of `(H_b, alpha_b)` alone. Reason:
@lem:face-at-H (the-heegner-line :621-:639) says the *only* effective `(-2)`-wall through `H_b` is
`alpha_b^perp`; and every other effective root `delta` has `H_b.delta in Z \ {0}` (integrality), so
`dist(H_b, delta^perp) = |H_b.delta|/|delta| >= 1/sqrt 2` for every such root (`smw0_ch-direction-audit.md`'s Theorem CH.2, as audited). So around `H_b` the arrangement near `H_b` is a single hyperplane with two sides; the component whose closure contains `H_b` and which is `alpha`-positive is unique, and it is the component containing the Kahler cone. At any `sigma` in `O` (not only at a member), the same pin holds by the dossier's Lemma 4 (only `pm alpha` is an effective H-null root).

*Invariance under a label stabiliser.* Let `g` be any `O(L_K3)`-element fixing `(H, alpha)` and commuting with the two involutions (@def:direct-group's exact condition). Apply it to a realization pair `(X, psi)` of a member: the transported pair is `(X, psi g^{-1})`. Effectivity of a model class is a property of the pair, transferred classwise: a class `y` is effective at `(X, psi g^{-1})` iff `psi(g^{-1} y)` is effective at `(X, psi)`. So the transported effective arrangement equals the `g^{-1}`-translate of the old arrangement, and the pinning formula just proved — the unique `alpha`-positive, `H`-closure component with `H` in closure — outputs exactly `g^{-1}(c)`. Since `g` fixes `(H, alpha)`, the formula evaluated at the transported pair returns the same `c` as the old one transported: at the level of the tuple, `g c = c`.

No hypothesis elsewhere in this argument says `g` is a Hodge automorphism or an automorphism of `X`:
it is an arbitrary lattice isometry preserving the model data, and invariance is proved at the
marking-transport bookkeeping alone. That is the answer, at the geometry side, to the question
whether an arbitrary `O(L_K3)` label isometry preserves the member's Picard/Hodge structure or
effective-root arrangement: it is *not* thereby claimed; and it is not needed, because the chamber
is a function of the pair's realized effective data, whose transport is tracked exactly.

*Trivial normalisation of chamber data afterward (the same argument as before).* From the displayed
structure theorem: `Gamma^dir_{Co,2} = Gamma_L` (`@def:direct-group`, heegner-report :976-981, at
created labels). The counter-readings (full-lattice and period-domain chambers) concern other
chambers than item 6's; they remain recorded as distinct objects.

## 2. Corrected kernel bookkeeping for (D2), and the equivalence at its section reading

*With the definitions of @def:direct-group and `@prob:group-identification`, and writing*

  `Z := Z_{O(L_K3)}(I_Co, I_dP)_{H,alpha}`,   `G5 := im(Z -> O(T_Co))`,
  `rho_T : O(T_Co) -> O(A_{T_Co}, q)`,          `W := <w_delta : delta in T_Co, delta^2 = -2>`,

the correct bookkeeping is:

(a) `G5 = rho_T^{-1}(P)` with `P = gamma rho_S(A) gamma^{-1}` (`A = O(S_dP)_{H,alpha} x O(E8(2))`),
    from the structure theorem of the accepted m4 direction, with existence of lifts of `P`
    verified.
(b) `W subset ker rho_T subset G5`: every `h in ker rho_T` lifts to the pair `(id_S, h)` because
    the glue condition for that pair reads `gamma = rho_T(h) gamma`, i.e. is exactly
    `rho_T(h) = 1`. Likewise every `w_delta` has `rho_T = id` (because `[delta]` is zero as a
    class in `A_{T_Co}`; reflections in a *lattice vector* act trivially on the discriminant form).
(c) `ker(Z -> G5) = { (g, id_T) : g in ker rho_S(A) }` — the elements of `Z` acting trivially on
    `T_Co`. Their image in `G5` is the identity; they do NOT produce a subgroup of `G5` at all.
    The previous formulation of a kernel-side "(J)" obligation — stated as `ker rho_S(A)` surviving
    "as a nontrivial T-trivial factor in the image" — was a projection artifact conflating
    `ker(Z -> G5)` with `ker rho_T cap G5`; it is retracted. There is no such obligation.

At these definitions, the equivalence is a genuine subgroup argument in both directions, with the
lift-family taken as a **normalised** set-theoretic section `sigma : P -> G5` of `rho_T` with
`sigma(1) = 1` (existence from (a)):

* (RI) `ker rho_T = W` IMPLIES `(D2)` in the shape "generated by wall reflections together with
  the lifts of the discriminant-image": for every `y in G5`,
  `y = [y sigma(rho_T(y))^{-1}] . sigma(rho_T(y))`, where the bracket lies in `ker rho_T = W`.
  So `G5 = W . sigma(P)`.
* and conversely the shape with a normalised section IMPLIES (RI): for `k in G5 cap ker rho_T`,
  `k = w.sigma(p)` with `p = rho_T(k) = 1`, so `sigma(p) = sigma(1) = 1` and `k = w in W`.

Un-normalised "any family of lifts" readings of (D2) do NOT have the converse direction: if the
lift of `1 in P` is chosen as a nontrivial element of `ker rho_T`, the displayed shape can hold
with `W` strictly smaller than `ker rho_T`. This is exactly the audit point at m4's D2' phrasing
("lifts of P"): it is now pinned to the normalised reading above, where the equivalence has the
subgroup proof just given. Every use of (D2) in this repository is recorded at that reading.

## 3. What remains open, named only

* (D1): monodromy-maximality, untouched.
* (RI) itself: `ker rho_T = W` for `T_Co = <2> + U(2) + E8(-2)` — a reflection-generation statement
  about the root system of `T_Co`, untouched.
* Application of `(D2) <=> (RI)` at the normalised-section reading, with (RI) open.

No group equality by notation anywhere; `G3, G4` untouched.
