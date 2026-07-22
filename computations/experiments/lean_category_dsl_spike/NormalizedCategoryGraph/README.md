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
| `FiniteRank` | Free with finite basis index (`IsFiniteRank`) — distinct from fg |
| `ModulesFamily` / `ModulesOf` | `RingCat` + fibre at `R`; default fibre still `ModuleCat ℤ` |
| Magmas one-tower | `Additive`/`Multiplicative` role classifiers; additive specimen tower |
| `evalCategory` | Interprets atoms + Magmas/Modules/Sets/M2O refinements via pullback |
| `ncg-export-full` | Lean registry JSON (**does not** read Python semantic-seed data) |
| Lean ledger gate | `ledger_check_from_lean_export.py` on exporter stdout (noncircular) |

## What is not true (withdrawn claims)

- “Stages 1–10 complete”

- “179/179 constructible **from Lean**” — Lean specimen is a vertical slice; full coverage is incomplete

- Full Sage 179 bijection authored as Lean declarations

- `Modules(R)` as a fully threaded `Rings ⥤ Cat` functor at every call site (fibre witness `ModulesOf` exists; default fibre still `ℤ`)

- Full path-equation certificates in the Python constructibility engine (role `along=` + collision detection only)

## Layers

| Layer | Path | Role |
| --- | --- | --- |
| Core | `Core/` | Ids, Classifier, CategoricalPullback, Expr, Normalize, `project` |
| Model | `Model/` | `AtomicModel`, `evalCategory` |
| Categories | `Categories/Algebra/` | Magmas / Rings symbolic ownership |
| Registry | `Registry/` | Env extension + entry types |
| Specimen | `Specimen/` | Lean-authored vertical slice + `Register` into env |
| Tools | `Tools/` | `ncg-export-full` |
| Spec | `Spec/` | Python migration manifest — **not** export SSOT and not compiled into Lean |
| Realization | `Realization/` | Separate Mathlib / Sage roots |

## Commands

```bash
lake build NormalizedCategoryGraph ncg-export-full
./.lake/build/bin/ncg-export-full | python3 scripts/ledger_check_from_lean_export.py
# Python seed tooling (oracle / migration — not Lean authority):
python3 scripts/generate_seed_spec.py
sage -python scripts/ledger_check_from_lean_manifest.py  # Python-seed constructibility only
```
