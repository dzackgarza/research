# NormalizedCategoryGraph (Lean)

Lean foundation for the normalized category graph. **Not complete** under the
full contract (Lean-authoritative 179-row graph, typed registry reflection,
complete Sage bijection). See PR review remediation.

## What is true now

| Piece | Status |
| --- | --- |
| Classifier + `Classifier.reindex` via Mathlib `CategoricalPullback` | Implemented |
| ForMathlib reindex id/comp equivalences | Sorry-free |
| `MagmasWithTwoOperations` | Categorical pullback `MagmaCat ×_Type MagmaCat` |
| `Rings` | Refinement tower over M2O (not defeq to the host) |
| `Unital` / `Inverse` | Structure classifiers (unit-/inv-preserving Homs), not `GrpCat` |
| `Module.Finite` | Realizes **finitely generated**, not `FiniteRank` |
| `evalCategory` | Interprets atoms + Magmas/Modules/Sets/M2O refinements via pullback |
| `ncg-export` | Lean specimen JSON |
| `ncg-export-full` | Lean specimen registry JSON (**does not** read Python `SeedData`) |

## What is not true (withdrawn claims)

- “Stages 1–10 complete”
- “179/179 constructible **from Lean**” — the Python ledger checker still proves
  constructibility from the **Python semantic seed**, not from Lean declarations
- Full semantic export from a reflected Lean environment covering the authored ledger
- `Modules(R)` as a genuine family (current Mathlib fibre is `ModuleCat ℤ`)
- `DivisionRings := Rings.Division` (classifier not yet realized)

## Layers

| Layer | Path | Role |
| --- | --- | --- |
| Core | `Core/` | Ids, Classifier, CategoricalPullback, Expr, Normalize, `project` |
| Model | `Model/` | `AtomicModel`, `evalCategory` |
| Categories | `Categories/Algebra/` | Magmas / Rings symbolic ownership |
| Registry | `Registry/` | Env extension + entry types |
| Specimen | `Specimen/` | Lean-authored vertical slice + registry seed |
| Tools | `Tools/` | `ncg-export`, `ncg-export-full` |
| Spec | `Spec/` | Python migration dump (`SeedData`) — **not** export SSOT |
| Realization | `Realization/` | Separate Mathlib / Sage roots |

## Commands

```bash
lake build NormalizedCategoryGraph ncg-export ncg-export-full
./.lake/build/bin/ncg-export            # viability specimen JSON
./.lake/build/bin/ncg-export-full       # Lean registry specimen JSON
# Python seed tooling (oracle / migration — not Lean authority):
python3 scripts/generate_seed_spec.py
python3 scripts/crosscheck_hand_dot.py
sage -python scripts/ledger_check_from_lean_manifest.py  # Python-seed constructibility
```
