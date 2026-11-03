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
