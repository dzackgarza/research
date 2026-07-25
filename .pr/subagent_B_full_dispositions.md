# B full dispositions for PR 177

## PRRT_kwDOTBB78M6Qt9WO

Path: computations/scripts/HayStack_Doc_Search.py:287 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578396333 Outdated: true Pre-filter: Gate 1 real syntax/correctness issue -> in-scope, no short-circuit; GitHub marks the thread outdated.
Disposition: Outdated (underlying claim accepted as written, but the reviewed diff location is stale) Claim disposition: true Remediation disposition: not applicable Policy/source basis: Python 3 grammar does not allow `except OSError, ValueError:` for grouping exceptions; live GitHub thread is marked outdated.
Evidence required before closure: Superseding commit hash or current-diff evidence showing the invalid Python 2 exception syntax is absent from the PR.

## PRRT_kwDOTBB78M6QuNMS

Path: writing/Coble Research/knowledge/03_Compactifications/Generalized Coxeter Semifans.md:21 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485373 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary: this is evidence that the PR damaged corpus source; the diff hunk shows correct `_` subscript syntax replaced by `*` in math mode.
Evidence required before closure: Commit hash proving the PR-caused LaTeX corruption in this file is no longer present.

## PRRT_kwDOTBB78M6QuNMX

Path: writing/Coble Research/knowledge/01_Lattices/Genus of a Lattice.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485381 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the diff hunk shows `\mathbf{Z}_p`, `L_{2, ...}`, and `L_{1, ...}` subscript notation corrupted to `*` forms.
Evidence required before closure: Commit hash proving the PR-caused LaTeX subscript corruption in this definition is no longer present.

## PRRT_kwDOTBB78M6QuNMZ

Path: writing/Coble Research/knowledge/01_Lattices/Lattice Morphisms and Embeddings.md:26 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485383 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the live thread identifies multiple `_` to `*` substitutions in mathematical notation, and the diff shows broad authored-line rewriting.
Evidence required before closure: Commit hash proving the PR-caused subscript corruption in this file is no longer present.

## PRRT_kwDOTBB78M6QuNMq

Path: writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Enriques_Surface_Cusps.md:11 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485407 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the live thread and diff hunk show caption subscript notation changed from `_` semantics to literal `*` syntax.
Evidence required before closure: Commit hash proving the PR-caused caption subscript corruption is no longer present.

## PRRT_kwDOTBB78M6QuNMv

Path: writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Enriques_Surface_Cusps.md:7 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485413 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies a caption math-mode `_` to `*` substitution that changes subscript rendering.
Evidence required before closure: Commit hash proving the PR-caused Coxeter-diagram caption corruption is no longer present.

## PRRT_kwDOTBB78M6QuNMy

Path: writing/Coble Research/knowledge/01_Lattices/E_n root lattices.md:17 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485415 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies `\operatorname{Ann}*{E_8}` as a PR-introduced broken subscript form.
Evidence required before closure: Commit hash proving the PR-caused `Ann` subscript corruption is no longer present.

## PRRT_kwDOTBB78M6QuNM3

Path: writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Cusp_Diagram_Calculations.md:5 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485425 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus mathematical meaning damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies subscript loss in lattice-type and moduli notation, changing mathematical rendering and meaning.
Evidence required before closure: Commit hash proving the PR-caused math-subscript corruption on this line is no longer present.

## PRRT_kwDOTBB78M6QuNM6

Path: writing/Coble Research/knowledge/01_Lattices/2-Elementary Lattices.md:36 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485430 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies signature subscript notation corrupted from `_{n_+}` to a literal-asterisk form.
Evidence required before closure: Commit hash proving the PR-caused signature-notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNM_

Path: writing/Coble Research/knowledge/01_Lattices/Root lattice.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485435 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the diff hunk shows a definition callout collapsed and math subscripts changed to `*` forms.
Evidence required before closure: Commit hash proving the PR-caused root-lattice definition corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNC

Path: writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Coble_Surface_Cusps.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485439 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread reports repeated math-mode `*` substitutions in running text over the changed paragraphs.
Evidence required before closure: Commit hash proving the PR-caused running-text subscript corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNF

Path: writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Coble_Surface_Cusps.md:11 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485443 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies inconsistent caption subscript rendering introduced by the PR. Evidence required before closure: Commit hash proving the PR-caused figure-caption subscript corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNI

Path: writing/Coble Research/content_pandoc/sections/Cusp_Correspondence/Coble_Surface_Cusps.md:9 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485447 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies figure-caption subscript syntax changed to literal `*` forms.
Evidence required before closure: Commit hash proving the PR-caused caption LaTeX corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNJ

Path: writing/Coble Research/knowledge/03_Compactifications/Coble Surface Cusps.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485449 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies PR-caused `_` to `*` substitutions in Coble-surface notation.
Evidence required before closure: Commit hash proving the PR-caused Coble-surface notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNL

Path: writing/Coble Research/knowledge/01_Lattices/Gram Matrix.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485453 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies multiple subscript sites in one mathematical line corrupted from `_` to `*` syntax.
Evidence required before closure: Commit hash proving the PR-caused Gram-matrix notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNO

Path: writing/Coble Research/content_pandoc/sections/Coble_Surfaces/Coble_Surface_Basics.md:70 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485456 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Pandoc rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the live thread states the PR split footnote continuation out of the footnote definition, making later content render as a code block instead of authored footnote content.
Evidence required before closure: Commit hash proving the PR-caused footnote-structure damage is no longer present.

## PRRT_kwDOTBB78M6QuNNS

Path: writing/Coble Research/knowledge/03_Compactifications/Mirror Moves.md:17 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485459 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies PR-caused subscript corruption in the changed bullet text.
Evidence required before closure: Commit hash proving the PR-caused Mirror Moves notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNV

Path: writing/Coble Research/knowledge/01_Lattices/Type I Unimodular Lattices.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485463 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies display-math matrix notation corrupted from subscript syntax to literal `*` syntax.
Evidence required before closure: Commit hash proving the PR-caused Type I matrix notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNZ

Path: writing/Coble Research/knowledge/03_Compactifications/Coxeter Groups and Polytopes.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485470 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the diff hunk shows an Obsidian definition callout collapsed so authored body material becomes callout-title material.
Evidence required before closure: Commit hash proving the PR-caused callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNNe

Path: writing/Coble Research/knowledge/03_Compactifications/Hyperbolic Lattices and Polytopes.md:19 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485478 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies Klein-model notation with PR-caused subscript loss.
Evidence required before closure: Commit hash proving the PR-caused Klein-model notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNk

Path: writing/Coble Research/knowledge/02_Moduli/ADE and BC Surfaces.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485484 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies callout body text collapsed into the `[!definition]` title line by the PR. Evidence required before closure: Commit hash proving the PR-caused ADE/BC callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNNl

Path: writing/Coble Research/knowledge/01_Lattices/Enriques lattice.md:19 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485487 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies PR-caused subscript corruption in Enriques-lattice notation.
Evidence required before closure: Commit hash proving the PR-caused Enriques-lattice notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNn

Path: writing/Coble Research/knowledge/02_Moduli/Noether-Lefschetz Locus for Enriques Surfaces.md:15 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485492 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies PR-caused nested subscript corruption in Noether-Lefschetz notation.
Evidence required before closure: Commit hash proving the PR-caused line-15 Noether-Lefschetz notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNq

Path: writing/Coble Research/knowledge/02_Moduli/Noether-Lefschetz Locus for Enriques Surfaces.md:12 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485495 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies the same nested subscript corruption at a second changed location.
Evidence required before closure: Commit hash proving the PR-caused line-12 Noether-Lefschetz notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNNx

Path: writing/Coble Research/knowledge/01_Lattices/Type II Unimodular Lattices.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485505 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies PR-caused subscript corruption in Type II lattice notation.
Evidence required before closure: Commit hash proving the PR-caused Type II notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNN3

Path: writing/Coble Research/knowledge/01_Lattices/Coble lattice table.md:19 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485512 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies table-wide math notation corrupted from subscript syntax to literal `*` syntax while another row still shows the intended convention.
Evidence required before closure: Commit hash proving the PR-caused Coble lattice table notation corruption is no longer present.

## PRRT_kwDOTBB78M6QuNN6

Path: writing/Coble Research/knowledge/01_Lattices/A_n root lattice.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485515 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus display-math rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies display math embedded into a blockquote paragraph where the authored display equation no longer has its own display structure.
Evidence required before closure: Commit hash proving the PR-caused display-math structure damage is no longer present.

## PRRT_kwDOTBB78M6QuNN9

Path: writing/Coble Research/knowledge/01_Lattices/Torsion Bilinear and Quadratic Forms.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485521 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies definition body text collapsed into an Obsidian callout header line by the PR. Evidence required before closure: Commit hash proving the PR-caused torsion-form callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNOB

Path: writing/Coble Research/knowledge/02_Moduli/Moduli space of degree 2 numerically polarized Enriques surfaces.md:12 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485526 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies definition body content merged into the callout title so only later text remains body content.
Evidence required before closure: Commit hash proving the PR-caused moduli-space callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNOP

Path: justfile:110 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485541 Outdated: false Pre-filter: Gate 1 QC/proof-surface gap -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Repository AGENTS QC integration says pre-push runs `just test-ci` and root recipes run umbrella hygiene plus every spike-owned justfile; POLICY.GLOBAL_QC_AUTHORITY and POLICY.NO_ADMIN_COMPLETION forbid a CI path that bypasses owned gates.
Evidence required before closure: Commit hash proving `test-ci` no longer bypasses the repository hygiene loop and spike-owned gates.

## PRRT_kwDOTBB78M6QuNOW

Path: writing/Coble Research/knowledge/01_Lattices/Gluing Overlattices.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485551 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies proposition body opening collapsed into the Obsidian callout title line by the PR. Evidence required before closure: Commit hash proving the PR-caused gluing-overlattices callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNOo

Path: writing/Coble Research/content_pandoc/sections/Lattices_and_Moduli/Coble_Moduli_Basics.md:21 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485572 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Pandoc structure damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies a Pandoc fenced-div opening split so the div is no longer parsed as the authored structure.
Evidence required before closure: Commit hash proving the PR-caused Pandoc fenced-div structure damage is no longer present.

## PRRT_kwDOTBB78M6QuNOt

Path: writing/Coble Research/knowledge/01_Lattices/Eichler-Siegel transformations on U+U.md:12 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485580 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies theorem body text collapsed into the callout title line by the PR. Evidence required before closure: Commit hash proving the PR-caused Eichler-Siegel callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNOz

Path: writing/Coble Research/knowledge/01_Lattices/Symmetric Bilinear Form.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485586 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies definition content collapsed into the callout heading by the PR. Evidence required before closure: Commit hash proving the PR-caused symmetric-bilinear-form callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNO5

Path: writing/Coble Research/knowledge/01_Lattices/Geometric Identification of the Dual Lattice.md:12 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485593 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies theorem body text collapsed into the callout title line, causing authored content to lose its body placement.
Evidence required before closure: Commit hash proving the PR-caused dual-lattice callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNO9

Path: writing/Coble Research/knowledge/01_Lattices/B_n and C_n root systems.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485596 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies example body text collapsed into the callout title line by the PR. Evidence required before closure: Commit hash proving the PR-caused B/C root-system callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNPA

Path: writing/Coble Research/knowledge/03_Compactifications/Orbit_Classification_in_T_U_oplus_overline_T_eta.md:13 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485603 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian and LaTeX rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the diff hunk shows theorem body text collapsed into the callout title and subscript notation corrupted in the same changed line.
Evidence required before closure: Commit hash proving the PR-caused orbit-classification callout and notation damage is no longer present.

## PRRT_kwDOTBB78M6QuNPF

Path: writing/Coble Research/knowledge/02_Moduli/The K3 Double Cover construction.md:11 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485607 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies remark body text collapsed into the callout title line by the PR. Evidence required before closure: Commit hash proving the PR-caused K3 double-cover callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNPI

Path: writing/Coble Research/knowledge/01_Lattices/Nikulin's lattices V_k and U_k.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485615 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies definition body text collapsed into the callout title line by the PR. Evidence required before closure: Commit hash proving the PR-caused Nikulin-lattices callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6QuNPO

Path: writing/Coble Research/knowledge/03_Compactifications/Cusp Diagrams.md:14 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485621 Outdated: false Pre-filter: Gate 1 PR-caused authored-corpus Obsidian rendering damage -> in-scope, no short-circuit.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Authored Markdown boundary; the thread identifies definition body text collapsed into the callout title line by the PR. Evidence required before closure: Commit hash proving the PR-caused Cusp Diagrams callout title/body collapse is no longer present.

## PRRT_kwDOTBB78M6Qt9XF

Path: computations/experiments/sage_lattice_category_spike/objects/categories.py:168 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578396411 Outdated: false Pre-filter: Gate 1 public API correctness issue -> in-scope, no short-circuit; thread is already resolved in the live GitHub payload.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Literal owner comment states `A/B/C workflow disposition: accepted-remediated`; the reviewed surface is a public `index` method rather than an internal invariant-only assertion site.
Evidence required before closure: Already resolved live; final ledger still needs the remediation commit hash if no closure stamp already records it.

## PRRT_kwDOTBB78M6QuNOi

Path: computations/experiments/sage_lattice_category_spike/typings/z3/**init**.pyi:3 URL: https://github.com/dzackgarza/research/pull/177#discussion_r3578485566 Outdated: false Pre-filter: Gate 1 external-library type/proof-surface correctness issue -> in-scope, no short-circuit; thread is already resolved in the live GitHub payload.
Disposition: Accepted as written Claim disposition: true Remediation disposition: aligned Policy/source basis: Literal owner/bot thread comments state this is already accepted-remediated on the branch; known-solution-first applies because z3 public behavior owns the signature contract.
Evidence required before closure: Already resolved live; final ledger still needs the remediation commit hash and external-contract/source-backed audit anchor if no closure stamp already records them.
