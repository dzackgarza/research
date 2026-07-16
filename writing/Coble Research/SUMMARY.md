---
title: Coble Moduli Project — Current State Summary
date: 2026-05-16
status: post-audit (May 11, 2026)
tags:
  - project/status
  - audit/may2026
  - section7/blockers
---

# Coble Moduli Project — Current State Summary

**Last Updated:** May 16, 2026 **Based on:** May 11, 2026 NotebookLM self-audit (knowledge/INBOX/)

## Executive Summary

This project establishes the moduli theory and compactifications of Coble surfaces (rational surfaces arising from plane sextics with 10 nodes).
The unpolarized case (Sections 1-4) is largely complete with rigorous proofs.
The polarized case (Section 7) has a conceptual framework but **5 critical unresolved obstacles** blocking completion.

## What's Proven (Sections 1-4)

### Unpolarized Coble Moduli $F_{\text{Co}}$

**Complete results:**
- Coble lattice: $T_{\text{Co}} = (11, 11, 1)_2 \cong \langle 2 \rangle \oplus E_{10}(2)$
- Primitive lattice embedding chain: $T_{\text{Co}} \hookrightarrow T_{\text{En}} \hookrightarrow T_{\text{dP}} \hookrightarrow \Lambda_{\text{K3}}$
- Period domain construction: $F_{\text{Co}} = \mathcal{H}_{-2} / O(T_{\text{En}})$
- Dimension: 9-dimensional rational quasiprojective variety
- Baily-Borel compactification structure

**Cusp correspondence (proven):**
- **1 zero-cusp**: $(9,9,1)_1 \cong \langle 2 \rangle \oplus E_8(2)$ (Type III boundary, disc $\mathbb{D}^2$)
- **1 one-cusp**: $(7,7,1)_0 \cong A_1^{\oplus 7}$ (modular curve)

Maps to Enriques cusps:
- $(9,9,1)_1 \mapsto (10,8,0)_1$
- $(7,7,1)_0 \mapsto (8,6,0)_0$

**Key technique:** Divisibility invariants of isotropic vectors (all have $\text{div} = 2$ in $T_{\text{Co}}$).

## What's Unproven (Section 7)

### Polarized Coble Moduli $F_{\text{Co},2}$ — 5 Major Blockers

#### 1. **Root Orbit Uniqueness** (CRITICAL BLOCKER)

**Status:** Unproven **Issue:** Need to prove $\Gamma_{\text{Co},2}$ acts transitively on the $(-2)$-curves in the polarized boundary.
**Why critical:** This is the foundation for all other Section 7 claims.
Without it, the cusp count and trace fan identity cannot be established.
**Known as:** The Vinberg trap

#### 2. **Cusp Classification**

**Status:** Conjectured but not computed **Issue:** The polarized cusp count is asserted without numerical verification.
**Note:** All numerical claims from pre-May 2026 work were reclassified as conjectures in the audit.

#### 3. **Trace Fan Identity**

**Status:** Unproven **Issue:** Whether $\text{Tr}(D_{\text{Co},2}) = D_{\text{En}}$ is asserted without proof.
**Connection:** Relates to the $\Gamma_{\text{Co},2}$ fundamental domain structure.

#### 4. **No-Moduli-Loss**

**Status:** Conceptual gap **Issue:** Need to verify the KSBA boundary captures all geometric degenerations without spurious points or missing components.

#### 5. **IAS Construction Gaps**

**Status:** Incomplete **Issue:** The compactification chain Baily-Borel → semitoroidal → KSBA → coarse moduli has conceptual gaps at each arrow.
**Missing:** Explicit IAS construction, boundary divisor verification, semitoroidal fan computation.

## Conjectural Claims (May 11, 2026 Audit)

The May 11, 2026 NotebookLM audit transitioned the project from "research program" to "rigorous proof framework" and reclassified the following as **conjectures lacking proof:**

- Numerical cusp counts for the polarized case
- Explicit root system orbit decompositions for $\Gamma_{\text{Co},2}$
- Computational verification of the $\Gamma_{\text{Co},2}$ fundamental domain
- The trace fan identity $\text{Tr}(D_{\text{Co},2}) = D_{\text{En}}$
- All claims about IAS boundary structure without explicit construction

**Key realization:** Sections 1-4 (unpolarized) are rigorous.
Section 7 (polarized) mixes proven lattice-theoretic setup with conjectural/computational claims that lack verification.

## Outstanding Computational Tasks

From `knowledge/meta/computational_hurdles.md`:

1. **Explicit Coble curve equations** — construct the rational sextics explicitly
2. **Isotropic orbit enumeration** — enumerate $\Gamma_{\text{Co},2}$ orbits on $\Delta_{\text{Co},2}$
3. **$\Gamma_{\text{Co},2}$ generators** — find explicit generators for the arithmetic group
4. **Fundamental domain construction** — build the Dirichlet domain for $\Gamma_{\text{Co},2}$
5. **Cusp counting** — compute the polarized cusp count numerically
6. **Verify $W(E_n)$ cusp representatives** — check the claimed cusp representatives
7. **Check $\text{Tr}(D_{\text{Co}}) = D_{\text{En}}$ numerically** — verify the trace fan identity by explicit computation

**Status:** None of these have been completed as of May 2026.

## Connection to Recent Work

### YZZ25 Paper (Added May 16, 2026)

**Reference:** Yang-Yin-Zhang, "Moduli spaces of sextic curves with simple singularities" (arXiv:2505.16727) **Extracted to:** `knowledge/papers/YZZ25.md`

**Relevance:** Coble surfaces arise from plane sextics with 10 nodes (ADE singularities).
The YZZ25 paper studies:
- GIT moduli of sextics with simple singularities
- Stability conditions for sextic degenerations
- Compactification theory for sextic moduli

**Potential applications:**
- Alternative compactification comparisons (GIT vs KSBA)
- Cusp structure insights from sextic degeneration theory
- Stability conditions that might relate to KSBA stability for Coble surfaces

## Critical Path Forward

**Immediate priorities (in order):**

1. **Resolve root orbit uniqueness** — this unblocks everything else
2. **Complete computational tasks** — numerical verification of Section 7 conjectures
3. **Fill IAS construction gaps** — explicit semitoroidal compactification
4. **Prove or refute trace fan identity** — requires either computational proof or theoretical argument
5. **Verify no-moduli-loss** — boundary analysis of KSBA compactification

**Section 7 cannot be published in current form** until at least obstacles #1-#3 are resolved.

## Repository Structure

- **knowledge/**: Research knowledge base
  - **INBOX/**: May 11, 2026 NotebookLM audit (9 markdown files)
  - **papers/**: Extracted papers (YZZ25, others)
  - **meta/**: Original SUMMARY.md, AUDIT.md, computational_hurdles.md, mathematical_gaps.md
  - **MOC.md**: Map of content
  - **Narrative MOC.md**: Section completion status
- **content_latex/**: LaTeX source for the paper
- **content_pandoc/**: Pandoc markdown source

## Document History

- **June 2024**: Original `knowledge/meta/SUMMARY.md` created (pre-audit state)
- **May 11, 2026**: NotebookLM self-audit identified 5 major blockers and reclassified numerical claims as conjectures
- **May 16, 2026**: This top-level SUMMARY.md created to reflect post-audit state
