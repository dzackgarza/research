Intended comment on research#807 (the connector is read-only; committed for the orchestrator to post).

---

Answered on the page, with one refinement that the issue's title does not survive as stated.

**Proved** (moduli-construction.md:725, proof :736, `thm:coble-smooth-antibicanonical-is-a-plane-blowup`): let S be a Coble surface [DZ99, Introduction] with |−2K_S| = {C}, C one connected smooth curve. Then C is rational, C² = −4, K_S² = −1; S is minimal as a Coble surface [DZ99, §1.1]; and S is *basic*: S ≅ Bl_{p_1,…,p_10} P² with −K_S = 3H − ΣE_i and C = 6H − 2ΣE_i. The image Z = π(C) is an irreducible plane sextic, C → Z its normalisation, Z has multiplicity 2 at the image of each centre and no other singularity, and δ(Z) = 10 = p_a(Z).

So the second alternative of the issue is **refuted**: no object of the functor lies outside the plane-model family, and the widening of the functor produces no further component of M_Co.

**Not proved**: the strict form, "the ten *nodes* of a sextic". When the ten centres are distinct, Z has exactly ten double points, each of δ = 1, each an ordinary node or an ordinary cusp. Two cases are left, both named rather than assumed away:

1. a double point that is an ordinary cusp — equivalently, by `lem:coble-double-point-of-the-sextic` (:748), a point at which C meets the exceptional curve in one point of multiplicity two, so that the preimage in the K3 double cover is a pair of (−2)-curves meeting once instead of one smooth (−2)-curve. In the plane model of [DZ99, Theorem 4.3] this is [DZ99, Theorem 2.5] with a non-multiple fibre of Kodaira type II; the classical ten-nodal sextic is type I_1;
2. two of the ten centres infinitely near, where the sextic has a double point with an infinitely near double point over it, of δ = 2.

The single lemma that closes it: the surfaces of cases 1 and 2 are (or are not) again the blow-up of the ten nodes of some irreducible plane sextic. Nothing on the page decides it; `rmk:coble-class-is-the-plane-class` (:762) records it.

Inputs, each a numbered statement read in the published text of DZ99: Introduction; §1.1; §1.2 (1.1); Lemma 1.2(1); Lemma 1.5(1); Lemma 1.10; Corollary 1.6; §2.1; Definition and Remark 2.9; Theorem 2.5; §4.1; Theorem 4.3; Remark 3.3; Definition 6.1; Theorem 6.3; Theorem 6.5; Proposition 6.4(1),(3). CD12 was not needed. No printed-page locator is used.

Acceptance item by item: "proved or refuted on a page of writing/" — MET. "read MET by a Kimi review" — NOT MET; no Kimi review of this work exists, and a review by the author of the proof is not an independent read. Details and the checks run: `computations/reports/807-acceptance-item-by-item.txt`.
