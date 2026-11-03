# Audit addendum: the invariance argument at the corpus's own semantics, and the corrected (D2) bookkeeping

Second edition, revised under the owner's two corrections. (1) The first edition claimed that
marking-transport bookkeeping *proves* that an arbitrary label stabiliser fixes the original
chamber. It does not: the bookkeeping shows the pinning formula is *covariant* under transport
(the transported formula returns the transported chamber), and invariance of the tuple's own
chamber needs one more implication, named **(INV)** below and kept **open** unless the stabiliser
is shown to preserve the member's model-effective arrangement. What remains proved without (INV):
the pinning at the unchanged full tuple (only `alpha_b^perp` passes within `1/sqrt 2` of `H_b`),
and the group equality at the *labels'-own lattice* reading (m4's Theorem CH(a), accepted).
(2) The `(D2) <=> (RI)` equivalence is re-stated at its exact formal content: a normalised
set-theoretic section supplies a normal form only *one* direction for free; the group-generation
reading needs the relations step **(REL)**, which is named and kept open. The first edition's
sentence "every use of (D2) in this repository is recorded at that reading" is retracted; the
repository's (D2) is the generation reading.

Sources and definitions are those of `smw0_ch-direction-audit.md`; notation as in
`computations/reports/smwo_direct-period.md`. The five groups `G1..G5` keep their original
definitions and scope throughout; nothing below substitutes one group for another.

## 1. The chamber argument at the unchanged full tuple: what is proved, what is open

*Base object.* `cc` is the tuple's chamber: at a member `X_b` it is the component of the positive
cone containing the Kahler cone, cut at the member's effective algebraic roots
(`@def:direct-cover-datum` item 6, `writing/coble/heegner-report/coble-heegner-research-report.md`
: 889-896; `@rmk:chamber-not-transported`'s own reading: "the chamber containing the Kahler cone",
the corpus's adopted semantics).

*Pinning (proved, unchanged).* At every member, `cc` is recovered from `(H_b, alpha_b)` by the
formula "the unique `alpha_b`-positive component whose closure contains `H_b`". Reason:
@lem:face-at-H (the-heegner-line :621-:639) says the *only* effective `(-2)`-wall through `H_b` is
`alpha_b^perp`; and every other effective root `delta` has `H_b.delta in Z \ {0}` (integrality), so
`dist(H_b, delta^perp) = |H_b.delta|/|delta| >= 1/sqrt 2` for every such root
(`smw0_ch-direction-audit.md`'s Theorem CH.2, as audited). Around `H_b` the arrangement is a
single hyperplane with two sides; the `alpha_b`-positive side is `cc_b`, and it contains the
Kahler cone (`H_b` ample at the member; `Kahler . alpha_b > 0` since `alpha_b` is effective).
At any `sigma in O` (not only a member), the same pin holds by the dossier's Lemma 4 (only
`pm alpha` is an effective H-null root there). This uses no accumulation hypothesis anywhere.

*The covariance bookkeeping (proved, but weaker than invariance).* Let `g` be any
`O(L_K3)`-element fixing `(H, alpha)` and commuting with the two involutions; apply it to a
realization pair `(X, psi)` of a member, giving the transported pair `(X, psi g^{-1})`.
Effectivity of a model class is a property of the pair: `y` is effective at `(X, psi g^{-1})` iff
`psi(g^{-1} y)` is effective at `(X, psi)`. So the transported model-effective arrangement equals
the `g^{-1}`-translate of the old one, and the pinning formula applied to the transported pair
outputs `g^{-1}(cc)` (closure and positivity conditions are `g`-equivariant, and `g` fixes
`(H, alpha)`).

*The missing implication (open).* Invariance of the *tuple's own* chamber means `g cc = cc` for
every such `g`. The bookkeeping above outputs `g^{-1}(cc)` for the transported pair and `cc` for
the original; identifying the two outputs requires the formula's value to be *independent of the
member's effective arrangement beyond `(H, alpha)`* — i.e. it requires:

> **(INV).** Every `g in Z_{O(L_K3)}(I_Co, I_dP)_{H,alpha}` preserves the tuple's model-effective
> `(-2)`-root arrangement (`g` permutes `psi^{-1}` of the member's effective algebraic roots).
> Equivalently, `g cc = cc` at the item-6 semantics for every such `g`.

(INV) is exactly the assertion that an *abstract* label isometry respects a *geometric* datum
(effectivity on the member). No step in the transport bookkeeping proves it, and the step in the
first edition that concluded `g cc = cc` from the covariance of the formula is identified here as
the gap named by the owner: covariance under transport is equivariance, not fixedness. The first
edition's claim that "no hypothesis says `g` is a Hodge automorphism or an automorphism of `X`, and
invariance is proved at the marking-transport bookkeeping alone" is **retracted**; invariance is
now conditional on (INV), which is open.

*What (INV) would need.* Any of: (i) `g` lifts to an automorphism of `X` (an effective-Torelli
input, not available for arbitrary lattice isometries and not claimed anywhere in the corpus);
(ii) a lattice-level characterization of the member's effective roots that `g` visibly preserves;
(iii) a proof that the pinning formula's output is the same chamber for *any* two arrangements
sharing the single wall `alpha_b^perp` within `1/sqrt 2` of `H_b` (false in general: far walls
change the chamber's boundary even when they do not come near `H_b`; the *germ* at `H_b` is pinned,
the chamber is not thereby pinned as a set). Note the pinning *formula* is genuinely a function of
`(H_b, alpha_b)` at every tuple; the determination question is whether `g` fixes the set it
selects.

*The standing narrower theorem (kept at its scope).* At the *labels'-own lattice* reading of the
chamber — walls cut from the labels' own lattice `S_Co` (m4's Theorem CH(a)) — every
`g in A = O(S_dP)_{H,alpha} x O(E8(2))` permutes the labels' own `(-2)`-walls automatically
(`g` is an isometry of the lattice), fixes `H` and `alpha`, and the unique `alpha`-positive chamber
with `H` in closure is then fixed: `A_cc = A`, hence `Gamma^dir_{Co,2} = Gamma_L` at that reading,
with the structure display `G5 = rho_T^{-1}(gamma rho_S(A) gamma^{-1})` and
`|P| = |rho_S(A)| = |W(E8)| = 696729600` (all proved in m4's file, accepted at
`.ultramath/smw0uqe8g/REFEREE-verdict-m4.md`, full proofs published at
`computations/reports/smw0_accepted-proofs.md` §I). Readings (b) (full-lattice) and (c)
(period-domain) remain disproved counter-readings with the explicit witnesses recorded there.
At the item-6 (unchanged full tuple) semantics, `Gamma^dir = Gamma_L` is now stated *conditionally
on* (INV). The cross-member transport fork of the corpus's fourth bullet is untouched by all of
this and stays open as it stood.

## 2. (D2) at its exact formal content: the normal form, and the relations step

*With the definitions of @def:direct-group and `@prob:group-identification`, and writing*

  `Z := Z_{O(L_K3)}(I_Co, I_dP)_{H,alpha}`,   `G5 := im(Z -> O(T_Co))`,
  `rho_T : O(T_Co) -> O(A_{T_Co}, q)`,          `W := <w_delta : delta in T_Co, delta^2 = -2>`,

the bookkeeping (proved, unchanged) is:

(a) `G5 = rho_T^{-1}(P)` with `P = gamma rho_S(A) gamma^{-1}` (`A = O(S_dP)_{H,alpha} x O(E8(2))`),
    from the accepted m4 direction's structure theorem; lifts of `P` exist (`rho_T` is surjective
    by the accepted m2 direction).
(b) `W subset ker rho_T subset G5`: every `h in ker rho_T` lifts to the pair `(id_S, h)` because
    the glue condition for that pair reads `gamma = rho_T(h) gamma`, i.e. is exactly
    `rho_T(h) = 1`. Likewise every `w_delta` has `rho_T = id` (because `[delta]` is zero as a
    class in `A_{T_Co}`; reflections in a *lattice vector* act trivially on the discriminant form).
(c) `ker(Z -> G5) = { (g, id_T) : g in ker rho_S(A) }` — the elements of `Z` acting trivially on
    `T_Co`. Their image in `G5` is the identity; they do NOT produce a subgroup of `G5` at all.
    The first-edition formulation of a kernel-side "(J)" obligation — stated as `ker rho_S(A)`
    surviving "as a nontrivial T-trivial factor in the image" — was a projection artifact
    conflating `ker(Z -> G5)` with `ker rho_T cap G5`; it is retracted. There is no such
    obligation.

At these definitions, take a **normalised** set-theoretic section `sigma : P -> G5` of `rho_T`
with `sigma(1) = 1` (exists by (a)). The two now-distinct statements are:

* **Normal-form shape (NF):** `G5 = W . sigma(P)` *as a set*.
* **Generation shape (GEN), the repository's actual (D2):** `G5 = < W, sigma(P) >`, the subgroup
  generated by the wall reflections and the lifts — the shape of "generation of `Gamma^dir`
  by the wall reflections together with the discriminant-automorphism image" in the published
  dossier.

**Lemma A ((RI) => (NF), proved).** If (RI) `ker rho_T = W` holds, then for every `y in G5`:

    y = [ y . sigma(rho_T(y))^{-1} ] . sigma(rho_T(y)),

where the bracket lies in `ker rho_T = W`. Hence `G5 = W . sigma(P)`. `square`
(This one-line factorisation *is* the normal form; it needs only (RI) and the section property.)

**Lemma B ((NF) => (RI), proved).** If `k in G5 cap ker rho_T` and (NF) holds, write
`k = w . sigma(p)`; then `p = rho_T(k) = 1` (using `rho_T(w) = 1` from (b) and the section
property), so `sigma(p) = sigma(1) = 1` and `k = w in W`. Hence `ker rho_T = W`. `square`

**The relations step (REL) (open).** Generation does *not* by itself supply the normal form:
`< W, sigma(P) > = W . sigma(P)` requires closing products under the two relation families

> **(REL).** (i) `sigma(p) w sigma(p)^{-1} in W` for all `p in P, w in W`, and
> (ii) `sigma(p) sigma(q) sigma(p q)^{-1} in W` for all `p, q in P`.

(i) is the normality statement `W` is conjugation-stable under the section; (ii) is the 2-cocycle
statement. Under (RI), both hold trivially (`ker rho_T = W` is normal in `rho_T^{-1}(O(q))` and the
cocycles lie in `ker rho_T`); conversely (REL) plus any one of the directions upgrades (GEN) to
(NF). The first edition's phrases "the converse direction is not on this foundation" (for the
un-normalised reading) and "both directions have the genuine subgroup proof" are now stated at
their exact content: the proved content is (RI) => (NF) => (GEN), with (REL) as the step that
would make (GEN) and (NF) coincide in general, and (REL) is **not proved here**. In particular the
equivalence `(D2) <=> (RI)` at the generation reading is *conditional on (REL)*; at the
normal-form reading it is Lemma A + Lemma B as displayed. Neither (RI) nor (REL) is decided; the
original (D2) of the published dossier stays open exactly at them.

**Retraction.** The first edition's sentence "Every use of (D2) in this repository is recorded at
that reading" is retracted: the repository's (D2) is the generation reading, and no survey
substantiated the universal claim.

## 3. What remains open, named only

* (INV): stabiliser preservation of the tuple's model-effective arrangement (equivalently,
  `g cc = cc` at the item-6 semantics for every `g in Z_{H,alpha}`); the determination
  `Gamma^dir = Gamma_L` at the unchanged full tuple is conditional on it. At the labels'-own
  reading the equality stands (m4, accepted).
* (D1): monodromy-maximality, untouched.
* (RI) itself: `ker rho_T = W` for `T_Co = <2> + U(2) + E8(-2)` — a reflection-generation statement
  about the root system of `T_Co`, untouched.
* (REL): the normality/2-cocycle relations of the normalised section, named above; needed for the
  generation reading of (D2).
* Application of `(D2) <=> (RI)` with (RI) and (REL) open.

No group equality by notation anywhere; `G3, G4` untouched.
