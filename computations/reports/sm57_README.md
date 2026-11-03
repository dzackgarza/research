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

The companion `sm57_matrices_gen.txt` and the file `sm57_lean-report.md` document a
pd-Baire *membership list with the convention of ẑ2 class-times* — that report's "mod
$2\mathbb{Z}$" is Sage's `is_square(...) mod 2` output, not the corpus's coset membership
in $\mathbb{Q}/2\mathbb{Z}$. **That list's δ-attributions are not used anywhere in the
manuscript**; the $\delta$ baked into the report's text is the argument of
`prop:cobble-transcendental`'s tail, not this file.

## 2. Sage via the maintained provider (pin `c546077d`)
Witness and lattice computations: `sm57_verify_special_member.py` + `.log` (the $F'$
witness), `sm57_member_b0_full.py`, `sm57_verify_witness.py`, `sm57_verify_charts.py`,
`sm57_verify_members.py` + `.log` (m6 member B, NL strata), `sm57_matrices_gen.txt`,
`sm57_verify_witness-m1.py` + `sm57_verification-log.txt`, `sm57_verify-run.txt`.
These are run by the *maintained* lattice provider (`sage-extensions` at pin `c546077d`):
their outputs are certificates of what they print.

## 3. Ordinary scripts and annotations (not certificates)
`sm57_verify-run.txt` and `sm57_verify_witness-m1.py` contents are ordinary sympy or custom
scripts; statements proven elsewhere (for example, the structure classification of their
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
