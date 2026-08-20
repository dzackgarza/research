# Category-design corpora

Design and planning records for the category tree that became the preamble
(`src/dzack_research/preamble/`). The documents were written in two external
Coxeter working trees (`~/gitclones/Coxeter`, `~/gitclones/Coxeter-v2`) and
landed here on 2026-08-20 by the Coxeter-corpora enrichment migration
(vault plan `PLAN-coxeter-deletion-audit-registry`).

Every file keeps its original content. Only an origin header was prepended,
naming the source path and the copy date.

## What these documents are

They state an **intended interface**: a category, its objects, its morphisms,
the methods each level owns, and the hypotheses under which each method is
defined. They are not documentation of the built preamble, and several of
them describe a design the preamble deliberately did not take. Where the
audit identified such a divergence, the corpus INDEX records it. **A recorded
divergence is a finding, not a defect to repair.** The design rationale stays
readable precisely because the difference between plan and build is legible.

Some documents also contain mathematical errors that the audit found and
recorded. Those are listed in the INDEX of the corpus that holds them, so the
error cannot be re-derived from the document by a later reader.

## Corpora

| Directory | Content |
|---|---|
| `bilinear-module-tower/` | The tower $R\text{-Mod} \to$ bilinear form modules $\to$ symmetric $\to$ integral lattices, with the definite / indefinite / hyperbolic / degenerate / parabolic subcategory scheme, the 2-elementary and Coxeter-lattice branches, and the form-morphism hierarchy. |
| `core-category-theory/` | Abelian and concrete categories, diagram/cone machinery, limits and colimits as Kan extensions, internal algebraic objects, symmetric monoidal structure. |
| `conventions/` | The sign, notation, and construction conventions the corpora were written under, chiefly the negative-definite Gram convention $B_{ij} = 2\cos(\pi/m_{ij})$. |
| `n-category-tower/` | A specification tower for a toy model of $(\infty,n)$-categories from `gitclones/integral_lattice/cat/` (landed 2026-08-20, PLAN-corpora-audit-registry R4): iterated hom-enrichment — an $n$-morphism is a $0$-morphism of an iterated hom-category, with suspension as its adjoint direction; the corpus calls this "the dimension shift" — Hom/End/Aut and functor-category families, named categories, the homotopy toolkit, and the proof-carrying truth-value design. Candidacy for `categories/abstract_categories/` and the audit's error catalogue are in its INDEX. |
| `chain-complexes/` | The category $\mathrm{Ch}(\mathcal{C})$ as a Sage category — exactness, homology, cone and shift asked of the complex — plus the attempt to attach a bilinear form in each degree. The prerequisite for any $\mathrm{Ext}$ or $\mathrm{Tor}$ here; nothing of it is built. |
| `prior-art-hott/` | Two formalized category-theory libraries (Coq-HoTT, Lean 3 HoTT) read for design: hom-types indexed by object pairs, truncation levels, comma categories, Kan extensions, and universal properties with an explicit witness object. |
| `sage-gaps/` | The survey the preamble was built against: what SageMath's $R$-modules and notation lack. Most rows are now owned; $\mathrm{Ext}$/$\mathrm{Tor}$, exact-sequence tooling and syzygies are the ones that are not. |
| `fp-modules-axiom-scheme/` | Two drafts of a finitely-presented-modules category organized by declared axioms (Free/Torsion/Cyclic/Finite, Endset/Autset on homsets) with the standard functors as functors, from `gitclones/integral_lattice/FPModules{,PID}/` (landed 2026-08-20, PLAN-corpora-audit-registry R3). The axiom scheme is the recorded candidacy; the functor tier is owned prior art. |

The corrected roster of lattice-theoretic categories from that corpus's
`sage_integration.md` is `lattice-categories-roster.md` in this directory,
restated as a coverage check against the owned lattice tree.

`lattice-dsl-prior-attempt.md` reads the written specification of the *first*
lattice DSL (`~/gitclones/lattice-research`, landed 2026-08-20,
PLAN-corpora-audit-registry R2): its own definition of a bilinear $R$-module,
its ruling that lattices live in a product category $R\text{-Mod} \times
\mathrm{Bil}_R$ — which the preamble rejects in favour of added structure —
and the four design rulings that survived. The files it reads are at
`computations/scripts/lattice-research/written-spec/`.

`integral-lattice-bridge-residue.md` closes the same corpus's bridge layer
(`gitclones/integral_lattice/*.py`): the lattice expression grammar and the
random-lattice construction, which stay records rather than preamble code,
plus a table naming where every other notion of that layer landed.

Three source generations appear under `bilinear-module-tower/`, named by
origin tree rather than by date:

- `api-planning/` — `Coxeter/tmp_restore/docs/api-planning/`, the earliest
  interface specifications (the audit calls these the generation-1 files).
- `implementation-planning/` — `Coxeter/implementation/planning/`, the later
  revision, with the same subcategory scheme restated against a concrete
  Sage implementation plan.
- `sage-planning-modules-bak/` — `Coxeter-v2/archive/.../modules_bak/`, a
  third pass that reorganised the tower under `RMod/BilRMod/SymBilRMod`.

Where two generations hold a byte-identical file, it was landed once; the
alias is recorded in the owning INDEX. Fifteen files in
`sage-planning-modules-bak` were empty placeholders that were never written;
they were not landed, and the INDEX names them.
