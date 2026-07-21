# NormalizedCategoryGraph (Lean)

Semantics-preserving compiler from the modular normalized specification to:

- categorical Lean terms (`Core/`, `Model/`)

- a reflected semantic manifest (`Spec/SeedData.lean` → `ncg-export-full`)

- cross-reference certificates (`scripts/crosscheck_hand_dot.py`)

- authored-ledger constructibility certificates (`scripts/ledger_check_from_lean_manifest.py`)

## Layers

| Layer | Path | Role |
| --- | --- | --- |
| Core | `Core/` | Ids, Classifier, CategoricalPullback, Expr, Normalize, `project` |
| Spec | `Spec/` | Generated seed ingest (`SeedData.lean`, `seed_manifest.json`) |
| Model | `Model/` | Universe-polymorphic `AtomicModel` / `FoundationAtoms` |
| Categories | `Categories/Algebra/` | Magmas / Rings ownership modules (symbolic) |
| Names | `Names/` | Spelling aliases (`CRings` → CommRings) |
| Registry | `Registry/` | Persistent env extension + entry types |
| Presentation | `Presentation/` | Hand-DOT sidecar (`dot_graph_id_sidecar.json`) |
| Specimen | `Specimen/` | Stage-5 vertical slice |
| Tools | `Tools/` | `ncg-export`, `ncg-export-full` |
| Realization | `Realization/` | Mathlib `AtomicModel` + Sage correspondence |
| ForMathlib | `ForMathlib/` | Sorry-free reindex id/comp equivalences |

## Commands

```bash
python3 scripts/generate_seed_spec.py   # regenerate Spec + sidecar from Python seed
python3 scripts/generate_sage_correspondence.py  # Sage ↔ stable-id Lean certificates
lake build NormalizedCategoryGraph ncg-export ncg-export-full
./.lake/build/bin/ncg-export            # viability specimen JSON
./.lake/build/bin/ncg-export-full       # full seed JSON (embedded Spec)
python3 scripts/crosscheck_hand_dot.py  # Stage 7
sage -python scripts/ledger_check_from_lean_manifest.py  # Stage 9 (179)
just ncg-check                          # gen-seed + Stages 7 and 9
```

## Completion gates (Stages 1–10)

- Viability specimen: one `CommutativeRings`, no `CRings` node, generated projections

- Full Spec ingest: 345 categories / 164 classifiers from semantic seed

- Hand-DOT crosscheck: `hard=0`, `soft=0` (every solid parent is structurally reachable; alias self-parents ignored)

- Authored ledger: **179/179** `EXACT_BASE|CONSTRUCTIBLE`, **0** `MISSING_SEED`, recomputed from Lean seed manifest

- Stage 10: `Realization.Mathlib.atomicModel` (Sets/Finite/Graded/Magmas + algebra/modules/exceptional); Sage correspondence; ForMathlib reindex equivalences
