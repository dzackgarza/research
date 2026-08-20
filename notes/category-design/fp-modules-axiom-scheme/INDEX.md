# fp-modules-axiom-scheme — corpus INDEX

Landed 2026-08-20 from `gitclones/integral_lattice/FPModules/` and
`FPModulesPID/` by the integral_lattice enrichment migration
(PLAN-corpora-audit-registry, section R3). Two drafts of one design: a
category of finitely presented modules organized by a scheme of axioms,
with the standard functors declared as functors.

## The two drafts

- `finitely_presented_modules_category.py` — the first draft:
  `FinitelyPresentedModules` as a `CategoryWithAxiom_over_base_ring`, with
  `SubcategoryMethods` declaring the axiom scheme
  `Free / Torsion / Cyclic / Finite / Filtered / Graded / Super /
  WithGenerators`, the homset tier `Homsets → Endsets → Autsets` (Endset
  and Autset as *axioms on homsets*), and the functor tier: `FreeFunctor`,
  `ForgetfulFunctor`, `BaseChangeFunctor`, `tensor`, `Hom`,
  `DualObjects`, `DirectSums` — each declared as a functor or a
  covariant-construction category rather than as loose methods.
- `fpr_modules_pid_with_basis_category.py` — the second draft, restricted
  to PIDs, fields, and localizations of PIDs (the `__classcall_private__`
  dispatch refuses other rings), registering the axioms
  `Autset / Free / Torsion / Cyclic` in `all_axioms` and nesting
  `Torsion.Cyclic`; its `MorphismMethods` roster (kernel, cokernel, image,
  coimage, injectivity, surjectivity, inverse, lift) is the morphism
  contract.

## Disposition against the preamble

Owned already (the drafts are prior art for these, not sources):

- the free/forgetful adjunction and the free functor on a set —
  `categories/functors/free_forgetful_adjunction.sage`;
- base change — `categories/functors/base_change_adjunction.sage`;
- tensor products — `categories/functors/tensors.sage`;
- finitely presented modules with Smith-form invariants, torsion and
  torsion-free parts — `modules/framed/finitely_generated/
  finitely_presented_modules.sage` and neighbours;
- the morphism roster — `modules/module_morphisms/module_morphisms.sage`
  (kernel, cokernel, image, and — landed by this migration — coimage,
  equalizer, retraction, section).

**The genuinely absent notion this corpus supplies: the axiom scheme
itself.** The preamble's finitely-generated tier is a directory of
categories (`finitely_generated_free_modules`,
`finitely_presented_torsion_modules`, ...) rather than one category with
`Free`, `Torsion`, `Cyclic`, `Finite` as declared axioms reached by
`with_axiom`; and nothing owns `Endset`/`Autset` as axioms on the homset
tier. Under the categorical organization model (AGENTS.md: *axioms live
as high up as possible*), the drafts' scheme is the candidate shape: one
axiom declared once at the highest category that can state it, with the
property/data distinction deciding placement (freeness is a property; a
basis is structure — FOUNDATIONS §13.5/§13.7). The `Filtered/Graded/Super`
axioms are Sage-standard and would come along free.

Recorded, not adopted here: adopting the scheme is an architecture
decision on the live preamble tree (it re-homes existing categories), so
it stays candidacy in this corpus until ruled on, per the architecture
gate.
