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
O-T on the reading whose second slot is I_En. That is the reading the rank computations
*handled*, a conditional reading and not an original datum: the original text
(cons:reflection-twist) names only I_Co, and this record does not call any other slot
'original'. On that reading the pair is separated from the construction's pair by the
joint character multiplicities (3,8,0,11) vs (10,1,0,11) and the product's
anti-invariant rank 8 vs 1; the type of S_Co,b is separately a theorem by Nikulin
classification and matches the twist's S_Co-type, and the finds do not depend on the
chosen slot.  The original second-slot datum stays, by its text, as an open authoring
question, and the reflected-pair candidate (w_alpha I_En, w_alpha I_dP) keeps its own
remaining question, the labelled embedding/gluing, which abstract type does not decide.

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

## Completion of `smw0dbvr6`
All eight members' dispositions are complete; the swarm ended solved.  Final closed items:
O-S decided (index 1, det 8) by five accepted derivations plus the late independent Nikulin
route from m7-d4 (its predecessor section route having been rejected); O-T on the reading
whose second slot is I_En, answered as not conjugate (eigenrank multiset {11,3,14} vs
{11,10,21}) -- a conditional reading the rank computations handled, with no slot called
original anywhere in this record, because the original text names only I_Co.  The
reflected-pair candidate (w_alpha I_En, w_alpha I_dP) survives with fully matching
piecewise data and its only remaining question the labelled embedding/gluing; the
second-slot datum stays open as its own question by the original text, not supplied by
any rank computation; k=0 = U(2) (not U) by-product; k>=2 and the E_8(-2)-vs-<-2>^8
orbit case open.  Everything else in this record, the manuscript's A21 state-of-record and its
named open derivations (the fourth bullet semantics, R4 recovery, embedding/gluing, second
slot, $k>=2$ saturation) stands at that scope.

## Scope note on `reflected_pair_pieces.py`
`reflected_pair_pieces.py` is **ordinary exploratory matrix arithmetic** (handwritten E8
Gram, bespoke permutation/reflection construction, plain-matrix kernels and sig-checks via
floating-point `eigvalsh`): it is not a certificate, and no manuscript or verdict-line relies
on it. The object it sketched is now computed at the maintained tier by
`computations/reports/coble_reflected_pair.py` (+ run log), which follows
`coble_aegs_involutions.py`'s style at the same provider pin (`Lattices(ZZ)`, 
`L.reflection(alpha)` maintained reflection, `sublattice_from`, `determinant`,
`signature_pair`, `is_even`, and `is_isometric_to` for each joint-eigenspace piece against
an independently built maintained counterpart), giving: `(++) is U(2) perp <-2>`,
`(+-) is E8(-2)`, `(-+) = 0`, `(--) is <2> perp U(2) perp E8(-2)`, ranks (3,8,0,11), with
I-reflection products verified integral.  The same run then prints, still at the maintained
contract, the joint-piece spectral action of `J_Co` on the `(++)`, `(+-)`, `(--)` piece
bases (3, 8, 11 vectors) and the placed Gram data of `H = Delta(e)+Delta(f)` and
`alpha = e-f` (`H^2 = 4`, `alpha^2 = -2`, `H.alpha = 0`): input data for the
operator-extension obligation, with no type, gluing, or membership conclusion drawn from
it.  That is the piecewise lattice match only; the
labelled embedding/gluing and the AEGS-vs-construction identification of the del Pezzo
involution of the Coble K3 cover (the note `coble_aegs_involutions-run.txt` keeps at its
end) remain the open questions they were; nothing in the run answers a chamber question.

## `smw0gfl0i` outcome register (operator-preserving labelled extension, lattice level)
`smwg_operator-extension.md` is the full proof, with exact verbatim source statements,
hypothesis checks, the referee-supplied steps, the uniformity table, and the tier discipline
recorded: obligation 8(d)(1) of the A21 comparison is established **at lattice level, for every
(irreducible) one-node member b** — $g\in O(L_{K3})$ conjugating the reflected pair to a
one-node member's pair and carrying $(H,\alpha)\mapsto(H_b,\alpha_b)$. Chain: m2's Theorem A
(double coset collapses via Nikulin Thm 3.6.3, verified verbatim in the repo's primary note
`references/literature/lattice-research/nikulin1979integral.md` :1595) + the symplectic-coinvariant
closure of the $(+-)$-type (Nikulin [Ni1] Thm 4.7 via van Geemen–Sarti §§1.1–1.3, uniform in $b$)
+ the derived construction-side corner identification ($H_b=e_b+f_b$, $\alpha_b=[D_b]$,
index 1 from `@prop:det-saturation-del-pezzo`) + the proved marked-orbit and flag-stabilizer
gluing compatibility. Companion maintained artifact: `coble_joint_flag_premises.py` + `-run.txt`
(transplanted, deduplicated m3 check at the pin, reproducing its original log except three corrected
evidence-label lines, all recorded in its header: the false discriminant-image note, the honest
reflection construction (now the provider's own `L.reflection(alpha)` with a `w(alpha)=-alpha`
behaviour check, replacing the hand-built matrix), and the product line relabelled from a
nonidentity test that had been printed as "symplectic" — the symplectic reading is supported
separately by the cited geometric proofs, not by the matrix); it certifies the joint pieces, their types via `is_isometric_to`, the 2-elementarity and
indefiniteness hypothesis rows, the full-graph index, and the corner placement of $(H,\alpha)$ in
the maintained basis); two defects caught in review are repaired in the proof document (the
rank-11 block's (co)invariant identification against the sign table, and the $E_8(-2)$
discriminant-action remark, whose original trivial-image form was false and is replaced by the
correct classical mod-2 Weyl reduction statement, used nowhere). Accepted swarm solutions: m2 (d7), m3 (d5, independent second derivation),
m4 (d3, the chamber/period dichotomy); audits m5 (d6, premise audit: no impossible entry, residue
isolated as exactly the surjectivity statement) and m6 (d8) retained with their bespoke exact
scripts demoted to exploratory, per tier discipline. Still open, unchanged: the chamber clause
(m4's dichotomy), the authored second slot's text, (O1)/(O2), R4, $k\ge2$ saturation, the m7
depreaudit sites.

**m7 (d4) accepted, swarm ended solved**: m7's reduction made the pair-class question exactly the
discriminant double coset (every anti-isometry admissible, since all piece discriminants are
exponent-2 elementary, so both sign-changes always extend), proved the summand-level statements
(`Aut(q_P) = Z/2` realised by the $U(2)$-swap that *fixes both labels*; $\mathrm{im}(O(E_8(-2))) =
\mathrm{Aut}$, order $348\,364\,800 = |O_8^+(2)|$ with $q$-level orbits) and honestly isolated its
one open statement (D), the surjectivity on $O(S_\mathrm{Co})$ — which the verbatim-verified Nikulin
Thm 3.6.3 discharges directly ($S_\mathrm{Co}$ even, indefinite $(1,10)$, 2-elementary; likewise
$T_\mathrm{Co}$). Accepted as a further independent derivation; bespoke enumerations kept
exploratory-tier. The run `smw0gfl0i` then ended **solved** with seven accepted solutions
(m4 framing dichotomy; m2, m3, m7 extension proofs; m8's near-complete line; m5 audit; m6
structural analysis; m1 forcing-lemma closure) plus m8's triaged findings.

**m8 (d1) termination, findings assessed**: the direction ended `abandoned` at limits with no
submission and no report to judge; its five board findings were read and triaged. Kept at proved
scope: f15 (each block has a unique primitive embedding into $L_{K3}$ by Nikulin Thm 1.14.4 with
Rem. 1.14.5 — a correct cross-check, unused by the proof); f16 (discriminant-level transitivity of
admissible split summands via strict $b$-orthogonality — consistent; its own flagged gaps are
already closed by the accepted chain: its H1(i) follows from the verified N1 (Thm 3.6.3) on both
$U(2)$-summand lattices, and H1(ii)/H2 are what the accepted Theorem A + flag-stabilizer/Theorem B
do); f17's maintained cross-checks kept ($M=(+-)^\perp\cong U^3+E_8(-2)$ `is_isometric_to` True,
matching N4's invariant type; $\Gamma_3$ of order 2048) with one correction recorded: its
"index $[(++):\langle H,\alpha\rangle]^2=1$ ... span the (++) piece" line is a cross-rank
determinant-ratio artifact ($|\det\langle H,\alpha\rangle|=8$ vs $|\det(++)|=8$ giving a ratio 1
with no rank content), not a spanning
statement; the accepted placement datum (primitive, complement of square $-4$, index 2 with the
complement) stands at its verified scope. No mathematical obstruction arises from any of it. f18
records its own dead route (the $V_Z$/Witt plane count 67456, not to be used). f19 re-verifies a
real provider limitation at this pin: torsion discriminant forms expose predicates
(`is_anti_isometric`, normal forms, value module) but NO composable isometry constructor
(`isometry_to` raises `AttributeError`) — the third independent confirmation of the gap already
recorded by `coble_gluing_discriminants-run.txt`; it does not block the published proof, which
builds no gluing arrows (the full-graph property plus the verbatim-verified surjectivity lift do
the work predicated-free). m7 (d4) continues running; nothing is restarted.  **Provenance
currency (kept current so the gap is not misreported):** the constructor gap above belongs to pin
`c546077d`'s era.  The validated maintained provider `6ad7a5ea396da6e758ee28f3dea10a35baee0266`
supplies `DS.isometry_to(DT.twist(-1))` with typed inverse/composition and the original Coble
semantic tests, so no argument may rest on a capability blocker from the old pin. (Local note for
re-runners: this VM's live image still prints the historical `AttributeError` on a bare
`DS.isometry_to(...)`; the validated-pin capability is cited at the pin, and the checkout's
lattice-level sanctioned constructors `glue_map` / `Isom(...).an_element()` cover the gluing the
corpus actually presents.)

## `smw0kq02h` status register (M1 member/period + chamber bridge)
`smwg_chamber-bridge.md` is the published dossier for the two remaining questions, with its own
premise ledger and hostile-reader checklist: **(Q1) existence** — the authored single operator
$I_\Co := w_\alpha I_\En$ is realized on a smooth, nonempty, unobstructed 9-dimensional family
(deformation arguments proved in place; the open locus stated exactly as the wall complement of the
amplitude condition, with `Pic = S_Co` kept Baire-general, never Zariski-open); the reflected pair
is realized by commuting automorphisms on it (effective Torelli with $A = 2H - \alpha$), while
$w_\alpha, I_\En, I_{dP}$ are *never* geometric there (they send $A \mapsto 2H+\alpha$ with
$(2H+\alpha)\cdot\alpha = -2 < 0$), and the authored companion fails the construction's joint
multiplicities $(10,1,0,11)$ vs $(3,8,0,11)$. **Adjunction**: the reflection's whole algebraic
content is adjoining one root (rootless AEGS pair $(2,8,0,12)$ with $\alpha \in V_{--}$ to the
rooted one-node pair $(3,8,0,11)$ with $\alpha \in V_{++}$) — eigenlattice arithmetic, *not* a
geometric degeneration construction. **(M1) determination**: proved non-determination — the
realization family carries models with both clause-verdicts ($b_0$ side holds, $b_\star$ side
fails by Theorem 9), so the twist-vs-construction chamber clause is not well-posed from the
original data; root-sign blindness (Theorem D1) shows effectivity/chamber are not lattice data at
all. **(Q2)**: the Hodge + $2H-\alpha$-ample + effective-Torelli bridge is the *sufficient* route;
necessity is not available and in general false by the `prop:chamber-conditional` mechanism
(generic pairs can share chambers without Hodge); the certified obstruction is preserved verbatim
with its consequences derived by contraposition. Accepted solutions so far: m8, m1, m4, m6, m2,
m7 (six of seven directions; m3, m5 still running).  Referee scope corrections are folded into the
dossier where they bind (Theorem R's fixedness hypothesis, Theorem 4(a)'s Torelli dependence,
the $(Lat)\nRightarrow(Chm)\nRightarrow(Hdg)$ one-sided readings, the corrected Lefschetz
normalization census, and the current provider pin's constructor capability).


## `smw0o7jbf` outcome register (A20 direct period theorem: image and monodromy)
`smwo_direct-period.md` is the published dossier for the original `@prob:B24`/`@prob:B25`
obligations.  From the run `smw0o7jbf`: **six accepted solutions** (m2, m1, m3, m4, m5, m6, m7;
**m8 rejected** with three recorded gaps); referee records `REFEREE-verdict-m{1,..,8}.md` are in the
swarm's directory.  The dossier's current state (pass 2) is:
- **Theorem A** (pointwise exclusion of the whole $T_\Co$ $(-2)$-arrangement from every construction
  member's period, three independent proofs accepted):
  **arrangement = $\{\delta^\perp:\delta\in T_\Co,\delta^2=-2\}$, excluded pointwise, not generically**;
  the image *meets* the $(-6)$-Heegner locus (the special member $F'$ has $[C_1-C_2]\in T_\Co$ of
  square $-6$), so nothing larger is excluded.
- **Theorem B** (the "missing geometric realisation" of the corpus's :1015 closed at the exact
  chamber hypothesis "$2H-\alpha$ Kähler" — fixed-class effectivity + global Torelli; the earlier
  flagged input (R) is replaced by the anchored PSS/realization statements, anchors verified
  verbatim (`huybrechts_k3_lectures.md` :9480, :10227-:10240, :5167, :3536, :737, :1027)).
- **Theorem C** (the quotient reconstruction is arithmetic, not rigid; pass 2 proves every
  quotient-side input publicly): $\chi(\mathrm{Fix}) = 2\mathrm{rk}\,S_\iota - 20$ conventions
  ($-14$ for $\iota_{\mathrm{dP}}$; the pass-1 "$2\mathrm{rk}-22$" was the trace, corrected);
  the quotient lattice $\pi^*H^2(Y^\circ) = S_{\mathrm{dP}}$ at **index one proved** by the
  transfer/determinant argument (not the corpus's member-side prop alone); $\alpha$ descends to the
  irreducible $(-1)$-curve $e'$ with $\widetilde B \cdot e' = 2$ transverse at two points (proved);
  the contraction yields $Y \cong \mathbb P^1\times\mathbb P^1$ by the degree-$8$ classification
  with the nef square-$2$ class ($a^2-m^2=2$ unsolvable; $\mathbb F_2$ killed by ampleness), the
  branch being the irreducible one-node-$(4,4)$ curve ($B_1\cdot B_2 \ge 4$ against the node), and
  $\tau$ product with a $\tau$-fixed node; the unique degree-$7$ del Pezzo (Demazure, LNM 777) is
  the only classification input used; **no rigidity of smooth rational surfaces is used**.
- **Theorem D** $\operatorname{im}(p) = O/\Gamma_L$ with
  $O = \{\sigma : \exists\ \text{marked } (X,\psi) \text{ at } \sigma \text{ with } \psi(2H-\alpha) \text{ ample}\}$,
  proved member-by-member (Section L: the full (F1)-(F5) census, Lemma 4 (one contracted curve),
  Lemma 4b (frame inequality, repaired publicly — its written form was circular; the derivation now
  uses only ampleness of $A$, RR, negativity of the algebraic part of $T_\Co$, primitivity of
  $e,f$), Lemma 5 (pencils); Section QC: the reconstruction). B24's three markers: the arrangement
  excluded pointwise; the chamber the single condition "$2H-\alpha$ ample" (sign constancy on the
  component, no $A$-null root of $S_\Co$, frame inequality at every $\sigma\in O$); the exceptional
  root $\alpha$ a function of $(S_\Co, H, A)$. The corpus's open-image statement stands (the walls
  are locally finite, never dense; m8's contrary claim was rejected with its proof).
- **Theorem E** (B25 **scoped to what is proved**): deck group of the marking cover $= G_1$
  (covering theory; the labelled trivialising cover is normal by construction);
  $G_1 \subseteq \Gamma_L = G_5$ and $G_1 \subseteq \Gamma^{\dir}_{\Co,2} = G_2$ (flat labels);
  computed generators $W_{\mathrm{node}} = \langle w_\delta, (w_s, w_e)\rangle \subseteq G_1$ from
  the two wall types (second $\tau$-fixed point, nodal pair); **$G_1 = G_2$ is OPEN** with the two
  missing statements named: (D1) monodromy-maximality, (D2) generation (by wall reflections and the
  discriminant-automorphism image, owner-undecided for $T_\Co$); $\Gamma^\dir = \Gamma_L$ is
  separately open (chamber determination); $G_3, G_4$ untouched; **no group equality is asserted
  anywhere**, and `@prob:group-identification` of the four groups stands unchanged.
- **(T-mixed), at its completed census and pairing table**: the wall-forming mixed classes are
  (F2),(F3) at $s^2 = t^2 = -4$ and (F4) at $(s^2,t^2)=(-2,-6)$, with (F1) collapsed into a pure
  root and (F5) subsumed in $NL_2$; counts are machine-corroborated (bounded exact enumeration,
  self-stability asserted across two box sizes; exploratory tier): the `E8/2E8` class split is the
  standard `120/136`, `BAD_S = 121` (the 120 (F3) root-classes plus the one (F2) class),
  `BAD_T = 496` at norm $-4$ (`3*120 + 136`) and $528$ at norm $-6$; m8-round2's Theorem 2.1
  (verified) identifies every glued mixed wall with an ordinary $T_\Co$-Heegner divisor of its
  $t$-part. `|BAD_S| \le |NOTBAD_T|`, so no *counting* argument forces a pairing; existence of a
  glue avoiding every pairing is *not* certified by the comparison alone and is left open (to be
  exhibited through the maintained discriminant-form constructor of the validated pin when
  available), separately from the pinned-glue question itself. So the mixed walls are
  **glue-dependent** on the pinned Coble glue (the recorded open datum at report :661 item 7), in
  exactly three families: if no (F2),(F3),(F4) pairing occurs, B24 holds verbatim with
  $O = D_\Co^o$; if some occur, the image misses those $T_\Co$-Heegner pieces — (F2),(F3) by
  $A$-null Riemann–Roch effectivity (ampleness fails), (F4) by alpha-reducibility (the A2-split,
  the named tacnode alternative, outside the tuple's exceptional bullet) — and B24 stands with the
  corrected explicit complement. The brick probe's two mixed wall classes show both branches live;
  the brick glue is not claimed to be the Coble glue. (An earlier hand-sketch asserting a forced
  pairing is retracted as a miscount.)

Still untouched here: the same-run adjudications of the four-group equality
(`@prob:group-identification`), the certified negative pair with its verified scope, and the
conditional Hodge bridge; the checklist of the dossier's own remaining obligations is in its last
section.
