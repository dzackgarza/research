# sage-gaps — corpus INDEX

Four documents, landed 2026-08-20 from
`gitclones/Coxeter/research/explorations/implementation-notes/` under
`PLAN-coxeter-deletion-audit-registry` (readers H, P2). They are the survey
the preamble was built against: what a mathematician expects of $R$-modules
and of mathematical notation, measured against what SageMath supplies.

Two of them enumerate absences; two propose what to do about them.

## The documents

- `sagemath_rmodule_deficiencies.md` — module theory. Rows: no
  `M.tensor_product(N)` for general $R$-modules; no $\mathrm{Hom}_R(M,N)$ as
  an $R$-module; no $\mathrm{Ext}$/$\mathrm{Tor}$; no saturation of a
  submodule; no syzygies or minimal presentations; finitely presented modules
  over a general ring largely absent.
- `sagemath_notation_deficiencies.md` — notation. Rows: $M \oplus N$ spelled
  `M.direct_sum(N)`; no $M^{*}$ for the dual module; no $f^{-1}(y)$ for a
  preimage;
  no $\langle v, w\rangle$ pairing spelling; sums of a family spelled as a
  loop rather than `sum([...])`.
- `alternative_notation_implementations.md` — the experiments behind the
  second: a `__pow__`-with-string dual (`V^'*'`), an ASCII preprocessing
  layer, operator overloads. The record of what was tried, including what the
  preamble later rejected.
- `rmod_implementation_assessment.md` — the feasibility study for a new
  `RModules` category: Sage's `AbelianCategory` base, `TensorProductsCategory`
  as the monoidal structure (concluding no separate `SymmetricMonoidalCategory`
  is needed), and `FreeModule_generic` versus `CombinatorialFreeModule` as the
  concrete parent to reuse.

## Disposition against the preamble

This survey is the requirement list the preamble answered, so most rows are
now owned:

- tensor products of $R$-modules — `categories/modules/tensors.sage`;
- the dual — `dual_module` on the module categories, `dual_lattice` on
  `integrallattice/integral_lattices.sage` (each duality functor named, per
  the naming rule; a bare `dual` is banned);
- finitely presented modules and their invariants —
  `modules/framed/finitely_generated/finitely_presented_modules.sage`;
- saturation, index, sum and intersection of submodules — `subobjects.sage`,
  asked of the carried inclusion morphism;
- the free/forgetful adjunction and base change as *functors* —
  `categories/functors/free_forgetful_adjunction.sage`,
  `base_change_adjunction.sage`;
- the notation rows: $\oplus$ is `L + M` and `sum([...])`, $n$-fold sum is
  `L ** n`, the form evaluates as `v * w`. These are asserted by
  `tests/test_preamble_algebra_syntax.sage` and
  `test_lattice_generator_syntax.sage`.

Still absent, and stated only here: $\mathrm{Ext}$ and $\mathrm{Tor}$;
exact-sequence tooling; syzygies and minimal presentations. The first two
wait on a complexes node (`../chain-complexes/`).

Rejected rather than absent: the `V^'*'` dual of
`alternative_notation_implementations.md`. A bare `dual` is ill-defined once
an object sits in several categories, and the preamble names the duality
functor instead. The document is kept because the divergence is legible only
against it.

## The complementary survey

This corpus says what Sage *lacks*. What Sage *has*, and where, is surveyed by
the atlas from the lattice-research tree at
`computations/scripts/lattice-research/specs/sage_spec/`: which named Sage
categories equal which chained subcategories
(`Rings().Fields() == Rings().Commutative().Fields()`,
`GcdDomains == IntegralDomains().Gcd()`, and so on), the containment hierarchy
among them, and where `ZZ`, `QQ`, `AA`, `QQbar`, `RR`, `CC`, $\mathbb Z_p$,
$\mathbb F_p$ and localizations sit in that graph. It is data for the
fiber/capability map of the Sage bridge, and has no owner in the preamble yet.

## Errors recorded

None recorded against these four files by the audit. Note that
`rmod_implementation_assessment.md` reports Sage's own class layout as of the
source tree's Sage version; treat its API claims as dated observations, not
as current fact.
