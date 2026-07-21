# NormalizedCategoryGraph (Lean)

Lean foundation for the normalized category graph.
**Not complete** under the full contract (Lean-authoritative 179-row graph, typed registry reflection covering the ledger, complete Sage bijection).

## What is true now

| Piece | Status |
| --- | --- |
| Classifier + `Classifier.reindex` via Mathlib `CategoricalPullback` | Implemented |
| ForMathlib reindex id/comp equivalences | Sorry-free |
| `MagmasWithTwoOperations` | Categorical pullback `MagmaCat ×_Type MagmaCat` |
| `Rings` | Refinement tower over M2O (not defeq to the host) |
| `DivisionRings` | `Rings.Division` via M2O division classifier (not Magmas.Inverse) |
| `Unital` / `Inverse` | Structure classifiers (unit-/inv-preserving Homs), not `GrpCat` |
| `Module.Finite` | Realizes **finitely generated**, not `FiniteRank` |
| `ModulesFamily` | `RingCat` as base-ring category; fibre still provisional `ModuleCat ℤ` |
| `evalCategory` | Interprets atoms + Magmas/Modules/Sets/M2O refinements via pullback |
| `ncg-export` | Lean specimen JSON |
| `ncg-export-full` | `importModules` + `getRegistry` → `source: lean-registry` (no `SeedData`) |
| Lean ledger gate | `ledger_check_from_lean_export.py` on exporter stdout (noncircular) |

## What is not true (withdrawn claims)

- “Stages 1–10 complete”
- “179/179 constructible **from Lean**” — Lean specimen is a vertical slice; full coverage is incomplete
- Full Sage 179 bijection authored as Lean declarations
- `FiniteRank` realized
- `Modules(R)` as a fully threaded functor `Rings ⥤ Cat` at every call site

## Layers

| Layer | Path | Role |
| --- | --- | --- |
| Core | `Core/` | Ids, Classifier, CategoricalPullback, Expr, Normalize, `project` |
| Model | `Model/` | `AtomicModel`, `evalCategory` |
| Categories | `Categories/Algebra/` | Magmas / Rings symbolic ownership |
| Registry | `Registry/` | Env extension + entry types |
| Specimen | `Specimen/` | Lean-authored vertical slice + `Register` into env |
| Tools | `Tools/` | `ncg-export`, `ncg-export-full` |
| Spec | `Spec/` | Python migration dump (`SeedData`) — **not** export SSOT |
| Realization | `Realization/` | Separate Mathlib / Sage roots |

## Commands

```bash
lake build NormalizedCategoryGraph ncg-export ncg-export-full
./.lake/build/bin/ncg-export            # viability specimen JSON
./.lake/build/bin/ncg-export-full | python3 scripts/ledger_check_from_lean_export.py
# Python seed tooling (oracle / migration — not Lean authority):
python3 scripts/generate_seed_spec.py
sage -python scripts/ledger_check_from_lean_manifest.py  # Python-seed constructibility only
```
