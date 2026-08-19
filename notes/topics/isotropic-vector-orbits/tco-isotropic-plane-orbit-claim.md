# The isotropic-plane orbit claim for T_Co — open, with its obstruction recorded

Migrated 2026-08-20 from the lattice-research corpus
(`lean/CobleResearchLean/IsotropicPlanes.lean`, every proof `sorry`), with the
two errors the corpora-audit registry records in that file corrected here.
The corpus's own notes mark the claim unverified; it stays an **open claim**.

## The claim

There is a unique $O(T_{\mathrm{Co}})$-orbit of primitive totally isotropic
planes $J \subset T_{\mathrm{Co}}$ — equivalently, the Baily–Borel
compactification of the Coble period space has a unique 1-cusp — and for such
$J$ the isotropic reduction is

$$J^{\perp}/J \;\cong\; A_1^{\oplus 7},$$

negative definite of rank 7 (consistent with Witt index 2 for signature
$(2,9)$: $11 - 2\cdot 2 = 7$).

## Corrections to the source (recorded errors, landed as corrected mathematics)

1. **The source's model is the wrong lattice.** The Lean file modeled
   $T_{\mathrm{Co}}$ as $\mathbb Z^{11}$ with the diagonal form
   $\operatorname{diag}(2, 2, -2, \dots, -2)$. That form is
   $I_{2,9}(2)$, a different lattice:
   $T_{\mathrm{Co}} = \langle 2\rangle \oplus E_{10}(2)
   = \langle 2\rangle \oplus U(2) \oplus E_8(2)$ (catalogue `TCo`), and
   $U(2)$ and $E_8(2)$ are not diagonalizable over $\mathbb Z$. The diagonal
   model belongs on the algebraic side —
   $S_{\mathrm{Co}} = I_{1,10}(2)$ — and even there the signature is
   $(1,10)$, not $(2,9)$. Any verification against the diagonal model
   verifies nothing about $T_{\mathrm{Co}}$.

2. **The proof sketch's invariant does not classify.** The sketch classified
   isotropic-plane orbits by the Arf invariant on the discriminant group and
   concluded a single orbit from all planes having Arf invariant $0$. The
   same corpus's glossary (WARNING section of
   `notes/topics/coble-enriques-lattice-theory/reflective-two-elementary-lattices.md`)
   records the correction: the Arf invariant is defined only for
   $\mathbb F_2$-valued forms, is a strict weakening of the discriminant
   form, and does not classify integral lattices up to isometry. The
   invariant that governs here is the discriminant quadratic form
   $q: A_L \to \mathbb Q/2\mathbb Z$ together with the signature.

## What a proof or computation now looks like

The owned surface for the question is
`Aut(TCo).isotropic_plane_orbit_representatives()`
(`isotropic_orbits.sage`, engine behind the seam): the claim is exactly that
this tuple has one entry, and that the isotropic reduction
(`I_perp_mod_I`) of that entry's plane is isometric to the catalogue's
$A_1^{\oplus 7}$ (negative definite, per the AG sign convention). The related
*standard-target* computation — $O(A_N, q_N)$ orbits $[1, 527]$ on the 528
isotropic classes for $N = T_{\mathrm{Co}}$ — is the migrated script
`computations/scripts/coble-discriminant/coble_standard_target_discriminant_orbits.sage`
and its note
`notes/topics/coble-enriques-lattice-theory/coble-standard-target-discriminant-form.md`;
transitivity on primitive isotropic *vectors* (the 0-cusp count) is argued
there via $O(N) = O(B)$, $B \cong I_{2,9}$ (Milnor), and Dawes Alg. 4.4.
The plane statement remains open until the orbit enumeration runs on the
correct lattice.

The proved sibling in the same Lean tree — the Hessian rank bound at a
singular point of a ternary form (`NodeCriteria.lean`, no `sorry`) — is
unaffected and stays in the Lean tree, cited from the Coble sextic notes.
