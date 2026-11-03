# Provenance of the `sm57_*` files

These were accepted along the swarm `smvz57fr3` (parallel-work campaign on the one-node
labeled Coble rigidity problem, June's UltraMath run) and moved here so that the corpus
cites tracked text and data rather than `.ultramath/` working directories. Three tiers of
reliability, and what each is used for:

## 1. Lean (compiled, no `sorry`, at its own scope)
`formalization/coble-enriques/A21Arithmetic.lean` and the log
`computations/reports/sm57_lean-verification_log.txt` verify the determinants, evenness
(diagonal Gram entries), `pinned` (degree-4 pinning in $U(2)\perp\langle-2\rangle$), and
the twist-root pinning. It has **no theorem about quotient membership, the discriminant
gluing, or any chamber claim**.

The companion `sm57_matrices_gen.txt` and `sm57_lean-report.md` record, among the
machine-checked facts, the published value lists `q_values = [0,1]` with `delta = 0` for
$U(2)$ and `q_values = [0,1/2]` with `delta = 1` for $\langle2\rangle$ — in the
convention of the corpus's original definition (`def:discriminant`,
`def:two-elementary-isotropic-types`): in $\mathbb{Q}/2\mathbb{Z}$ the canonical subgroup
$\mathbb{Z}/2\mathbb{Z}$ is $\{0+2\mathbb{Z},\,1+2\mathbb{Z}\}$ (the elements $x$
with $2x\in2\mathbb{Z}$ are $0$ and $1$; $1/2$ has order $4$ and lies outside it). These
published values agree with that definition on their face; an earlier paragraph of this
README that relabeled them as a different convention is retracted. The focused semantic
check, run through the maintained provider's discriminant-form API
(`computations/reports/tco_delta_semantic.py`, log alongside of it, in the grad-log
`tco_delta_semantic-run.txt`), confirms in the provider's own value module: $\langle2\rangle$
has values $\{0,1/2\}$ with $\eta\mapsto[1/2]$, and $U(2)$ has values $\{0,1\}$ with
$e+f\mapsto[1]$ — so $\delta(T_\Co)=1$ from the $\langle2\rangle$ component alone,
exactly as `prop:coble-transcendental`'s tail now records.

## 2. Sage via the maintained provider (pin `c546077d`)
Witness and lattice computations: `sm57_verify_special_member.py` + `.log` (the $F'$
witness), `sm57_verify_witness.py`, `sm57_verify_charts.py`,
`sm57_verify_members.py` + `.log` (m6 member B, NL strata), `sm57_matrices_gen.txt`,
`sm57_verify_witness-m1.py` + `sm57_verification-log.txt`, `sm57_verify-run.txt`.
These are run by the *maintained* lattice provider (`sage-extensions` at pin `c546077d`):
their outputs are certificates of what they print.

## 3. Ordinary scripts and annotations (not certificates)
`sm57_member_b0_full.py` (sympy; repaired: `sp.factor_list(D)`'s scalar is `fac[0]`, not
`fac[0][0]`; its successful run is now tracked at `sm57_member_b0_full-run.txt` and
reproduces exactly the two reported claims: singular locus exactly $\{p\}$ in all four
charts, and each ruling discriminant equal to (the node's ruling coordinate)$^2$ times a
squarefree polynomial of degree $22$ — hence no reducible fibre away from the node's
rulings), `sm57_verify-run.txt` and `sm57_verify_witness-m1.py` contents are ordinary
sympy or custom scripts; statements proven elsewhere (for example, the structure classification of their
output) are cited through them as evidence, not as automatic verification. m2's audit
(`sm57_audit-one-node-m2.md`) and the m5/m6/m8 argument documents
(`sm57_proof-m5.md`, `sm57_chamber-obstruction-m6.md`, `sm57_obstruction-m8.md`) are the
accepted member arguments, kept as what they are.

## Limits named on purpose
No bespoke self-check is presented as a certificate, no "printed gluing" claim, no proof
of the chamber-conditional by artifact-reading, and no naming of Lean in areas Lean did
not verify. Unmet obligations that remain: the twist identification of the construction's
involution pair with the reflection twist; the saturation of $M$ in $S_{\mathrm{dP}}$; the
four downstream citation sites the dependency audit names
(`sm57_depaudit-ledger.tsv` + `sm57_depaudit.py`); the surviving semantics question about
the fourth bullet (which the parallel run reduced to two named interpretations, and the
manuscript now reports as a fork rather than a fact).

## Incorporation note (second UltraMath pass, `smw0b9kmo`)
The witness-membership audit (`sm00_witness-membership-audit.md`, with
`sm00_audit_witnesses.py` / `sm00_audit-witnesses-run.txt`) is now the reference for the
tracked witnesses, and supplies four tracked errata:
C1 — `sm57_chamber-obstruction-m6.md`'s displayed `f_B` is a documented typo: `a33 = -1`
against `-4` (the maintained log's own value);
C2 — `sm57_verify_witness.py`'s bitangent member and `sm57_verify_members.py`'s member B
are distinct certified members (bitangency roots `{1,3}` vs `{1,-1}`);
C3 — the node-ruling fibre is `I_2` with degrees `0,2` only when `a20 a02 != 0`; on the
complement it is Kodaira `IV` with degrees `1,1,0` and `chi = 4` (Theorem A of the audit).
The referee addendum to `sm57_proof-m5.md` is restricted accordingly; both members it
compares sit on the `I_2` side, only `F'` on the `IV` side;
C4 — corner-dependent claims are transferred between the four tau-fixed corners by the
tau-preserving automorphism.
The accepted positive half is tracked as
`sm00_positive-half-A21.md` (+ `sm00_verify_one_node.py/.log`, `sm00_verify_ample.txt`):
its ampleness lemma (Nakai-Moishezon on $\Bl_p Y$), openness proof, and the
period-rank-9-by-fibre-dimension argument supersede the corresponding manuscript steps.

## Errata and adjudication register (referee pass, third cycle)
* **Square of $2H-\alpha$.** The referee-issued acceptance text for the positive half said
  "square $7$" for $2H-\alpha$ on the K3 side. That was the downstairs value:
  $(2A-e)^2 = 4A^2-4A\cdot e+e^2 = 8-0-1 = 7$ on $\Bl_p Y$. Upstairs,
  $(2H-\alpha)^2 = 4H^2-4H\cdot\alpha+\alpha^2 = 16-0-2 = 14$, the degree-two pullback's
  scaling: $(\hat\pi^*(2A-e))^2 = \deg\hat\pi\,(2A-e)^2 = 2\cdot7 = 14$. The tracked
  member evidence (`sm00_verify_ample.txt`) has these values correctly; only the
  referee's phrasing was wrong, and it is corrected here.
* **The node-ruling fibre, adjudicated with a maintained-level check.** m5/d7's earlier
  universal claim that every node-ruling fibre is $D+D'$ of degrees $0$ and $2$ is false for
  the *original* family: on the stratum $a_{02}=0$ the fibre is Kodaira $\mathrm{IV}$
  ($C_1+C_2+D$, degrees $1,1,0$, $\chi=4$) by m3's Theorem A. The decisive computation is
  now maintained at `computations/reports/fibre_dichotomy_check.py` (+ run log): the branch
  divisor of $\pi^*C^\sim$ is the zero divisor of $a_{02}+a_{04}Y^2$, nonzero discriminant
  on the $\mathrm{I_2}$ side (corpus, $b_0$, $b_\star$, $B$), zero discriminant on the
  $\mathrm{IV}$ side ($F'$). Both strata belong to the original one-node family ($F'$ has
  one node at a $\tau$-fixed corner, smooth elsewhere — certified), so the quantifier
  *includes* the $\mathrm{IV}$ side, and the m5 Lemma 5.1 final sentence ("some ruling other
  than the node's") is to be read as false there: $F'$'s two degree-$1$ classes live at the
  node fibre itself. The obstruction pair ($b_0$, $b_\star$) is on the certified $\mathrm{I_2}$
  side, so the $\nu$-obstruction diff stands as proven on its stated inputs; and $F'$'s role
  in the general-vs-witness argument is consistent, its extra classes being the
  anti-invariant $C_1,C_2$ of the $\mathrm{IV}$ configuration.
## Reclamation errata (third cycle; the m7 semantics document)
* The chamber is not literally a product $c = \operatorname{Amp} \times N$ as `sm00_semantics.md`'s
  Theorem 5(2) stated: its own assumption $p^{-1}(c_\text{alg}) \subseteq \mathcal P$ is false for
  $n$ of large negative norm, as the incorporation review flagged. Corrected shape: open-ball fibres
  with the quadratic truncation $(u+n)^2>0$ over the trace chamber. The trace bijection survives in
  that form; the walls still see only the trace. Correction is written into the file as a referee
  reclamation.
* In the full $H^2$ of signature $(3,19)$ the claimed "translation-invariance subspace $= N_V$"
  detector is unsupported: negative-norm directions of $N_V$ exit the positive set across the quadric,
  not across a wall. The R4 forcing row (chamber equality forces Pic-identification) survives instead
  via the accepted census argument of `sm00_chamber-negative-half.md`, which is already stated in the
  ambient full-$H^2$ reading and needs no translation-invariance detector.
* The ambient-signature assumption for the hyperbolic wall-distance formula is recorded: it is
  signature-independent and is used only on the integral centre $y$ with $y^2 = 24$; that is its
  scope.
* Direction d2 (fibre audit) ended without a solution; the charter is covered by m3's accepted
  witness-membership audit (Theorem A, the I-2/IV dichotomy and the chi-bookkeeping) and by the
  negative half's elimination tests for the only numbers the corpus uses ($\nu(b_0) = 0$,
  $\nu(b_\star) = 4$). Nothing in the outcome depends on d2.

## Complete verdict register of the second run (`smw0b9kmo`, ended solved)
- d4 (m8) positive half: ACCEPTED. Labels conjugate for every pair; rho >= 11 on every member;
  period map rank 9 by the fibre-dimension theorem (ruling swap named; my prior injectivity phrasing superseded).
- d6 (m3) witness authenticity: ACCEPTED. All five tracked witnesses certified; Theorem A (I_2/IV),
  the chi bookkeeping, and four tracked errata (C1-C4).
- d5 (m2) negative half: ACCEPTED. The chamber clause is false for the certified pair in every
  member-determined reading (R2-R5), for every label-preserving isometry, with Grauert-free facet
  (y = 2H - alpha + C_+ + e_b, y^2 = 24) and the hyperbolic wall-distance bound; nu(b0) = 0 and
  nu(b*) >= 4 exact.
- d3 (m4) contraction/facet chain: ACCEPTED. Artin 1962 Thm 2.3 supplies the projective contraction
  (hypotheses checked: negative-definite pair matrix, p_a(mC) = 1 - m^2 <= 0); Lemma A1 supplies the
  wall-free ball; the Pic^perp signature correction (2, 20 - rho) is applied.
- d1 (m7) cone semantics: ACCEPTED with the referee reclamation above (the literal product and the
  V-detector were wrong as stated; corrected shape and the census route to R4 stand in their place,
  and the title table chamber-false-in-R1-R5 / true-in-R6 survives).
- d8 (m1) arithmetic core: ACCEPTED. The (degree-4 class, root) pair carries no freedom and no
  distinguishing arithmetic (root pinning Thm 3; <4>|<-2> cannot embed in U(2); ten gluings, one
  invariant), and names the residue: class number 1 of the genus {rank 20, sig (2,18), form -q_N}
  and transitivity of O(K) on the gluing anti-isometries, both genuinely open.
- d7 (m5) premise ledger: ACCEPTED on resubmission after the PL-7 rejection; now
  dichotomy-quantified (a_02 != 0 gives I_2, a_02 = 0 gives Kodaira IV), PL-8/PL-9 re-scoped, and
  Appendix A carries the corrected universal census with the indicator terms, matched against the
  independently audited values (F': nu = 2).
- d2 (m6) fibre audit: ENDED WITHOUT A SOLUTION; charter discharged by d6's audit and d5's
  elimination tests (the only two numbers the corpus uses).

Open items, named and not concluded anywhere in this register: the fourth bullet's semantics fork
(member-determined readings R1-R5, where the clause is false, versus the label-own R6, where it is
true; the authoring choice is not made); the twist identification of the construction's involution
pair; the saturation of Lambda in S_dP (det candidate {8,2}); and d8's two arithmetic residues
above. Nothing in this register asserts a completion beyond the listed acceptances.
## Reclamation errata, second entry (fourth cycle)
* The earlier entry's phrase "signature-independent" for the hyperbolic wall-distance formula is
  withdrawn.  Scope as now recorded in sm00_semantics.md'S S-1 entry: rigorous inside the signature
  (1, .) fibres (W = H^{1,1} and NS_R), where it supplies the wall-free ball; extended to the full
  H^2 space of signature (3,19) only through the product structure of algebraic walls
  (delta-perp = (delta-perp cap NS_R) perp N_V), with the positive-square condition handled as the
  open condition it is.  At its fibre scope it remains the accepted negative half's ball; nothing
  further uses it.
* The universal inference chamber-equality -> Picard recovery is withdrawn outside its proved
  scope: it holds generally for readings R1/R2 (span = NS), R3 (span = W), R5, but is OPEN in the
  full-V reading R4 of the fourth bullet, where the census argument is exactly pair-specific -- the
  accepted theorem that the certified pair is not conjugate with the chamber, which is what A21's
  chamber clause needs -- and a universal R4 recovery theorem is named as an open question
  (the R4 recovery question), not assumed anywhere.

## Verdict register of the twist-identification run (`smw0dbvr6`)
- d6 (m4) ambient saturation: ACCEPTED (with the nef-plus-fibration completion of its
  Lemma 1 checked by the referee).
- d2 (m6) fibre-span primitivity + readings analysis: ACCEPTED.
- d7 (m8) Nikulin fixed-locus route + types: ACCEPTED (route 1; the (3,3,1) and (11,11,1)
  invariants, T-type, and the pair-fail on the literal slot via multiplicity tables).
- d3 (m2) RR-verticality + literal-slot refutation: ACCEPTED.
- d5 (m3): REJECTED at Lemma 3 (`no irreducible curve of H-degree 1`): false on the
  certified split-ruling members (b*, B) and the IV-stratum member (F'). Its Lemmas 1-2
  (lattice bound, RR-nef) survive as reusable.
O-S is decided (S_dP = Lambda = U(2)+<-2>, index 1) independently by four accepted routes;
O-T is settled on the corpus's original slot (partner = I_En): NEGATIVE, with the joint
character multiplicities (3,8,0,11) vs (10,1,0,11) and the product's anti-invariant rank
8 vs 1, and with H1 discharged anyway by Nikulin's classification (the type of S_Co,b is
the twist's S_Co-type). The persistent alternatives kept at scope: the auxiliary reading
(w_alpha I_En, w_alpha I_dP), whose residue is the labelled embedding/gluing question,
which abstract type does not decide.

## Scope note on `smtw_certify_lattices.py` and its log
That script is re-labelled with its actual reliability class: **ordinary exploratory arithmetic**
(it reimplements determinants, signatures, quadratic values and Gram operations from Fraction/itertools
and hand-builds E8, with no maintained semantic API underneath). It is not a computational certificate,
and acceptance texts in this record do not rely on it. Where computational validation matters, what is
used here is the maintained provider's own lattice/discriminant/saturation APIs — here the
`sdp_discriminant_referee.py` run at pin `c546077d` and its log, which is also the only
computational line the manuscript's saturation proposition cites. Any further validation of a
specific member's lattice type that someone needs should also go through those APIs in the shared
development image (and their docs/tests first), not by patching algorithms locally; otherwise that
validation is left open here, by design.

## Verdict register, final dispositions of `smw0dbvr6`
- d1 (m5, rebuilt): ACCEPTED (the divisibility criterion with two certified witnesses, one
  per ruling: b_star's C_+·f_b = 1, and f_dag's split {y=1}-ruling with C'_±·e_b = 1; flat
  rulings then propagate the omission over the connected node-at-(0,0) locus; k=0 = U(2),
  k>=2 as named open question).
- d8 (m1): ACCEPTED (RR-vertical O-S at the accepted fibre-span scope; O-T refuted on the
  eigenrank multiset {11,3,14} vs {11,10,21} plus the labelled alpha action).
- d5 (m3, corrected): ACCEPTED (fibre-span primitivity with the withdrawal of the first
  version's H-degree-1 lemma recorded).
- d4 (m7): REJECTED at its section route ("split over D" => "D intersect B-tilde empty" --
  false at the certified bitangent witnesses; an even but nonempty branch divisor is the
  general case). The Nikulin fixed-locus route in the same document stands at the m8
  acceptance level; its O-T content is registered at the literal-negative scope plus the
  named remaining obligations (embedding/gluing, and the E_8(-2)-vs-<-2>^8 orbit case).
  Not used in any manuscript line: the "accepted" text above at that paragraph keeps only
  the proposition's own argument and the maintained census.
