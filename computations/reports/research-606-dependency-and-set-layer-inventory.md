# research#606 — dependency state and the research-side set layer

Recorded under the authorization boundary in force: this research session does not author
or check out `dzackgarza/lean-categories`; missing formal inputs stay with that upstream
owner. Everything below is either read from research's own tree or is issue evidence.

## Ordered leaf and its real dependencies

`#46 → #417 → #384 → #606` is the only open path: `#417` has 20 children, 19 closed and
only `#384` open; `#384` has exactly one child, `#606`, which has no sub-issues.

`#606` is blocked by four `lean-categories` issues, all open, each with `blocked_by: 0` and
`blocking: 1`: `#95`, `#96`, `#97`, `#98`. Read against the `lean-categories` tip that was
inspected earlier (`fc6d3d6`), the state is:

| issue | requirement | state at that tip |
| --- | --- | --- |
| #95 | `P_fin : Sets ⥤ Sets` with laws and the natural inclusion into `𝒫` | declarations present; the inclusion registration was missing — artifact prepared in `leancategories-95-finite-subsets-inclusion.patch` |
| #96 | selected ranking `rank : X ≃ Fin n` / `≃ ℕ` with inverse laws and total accessors | absent |
| #97 | `WellOrderedSets`, the wide subcategory `E_mon`, `E_mon → WellOrderedSets`, forgetful chain, order type | absent |
| #98 | `PartiallyOrderedSets`, `TotallyOrderedSets` with monotone maps and routes | present |

So the genuinely missing formal inputs are **#97, then #96** (`#96`'s own body defers its
order contract to `#97`). Both belong to the `lean-categories` owner; this session cannot
author, check out or publish there.

## Research-side set layer

`#606`'s second acceptance bullet requires that public research consumers obtain the set
layer through the catalogue-derived language and that the migrated path has no local
provider ordering or cooperative initializer. Checked in this tree:

- the set layer is at `archives/preamble/categories/sets/` — `sets.sage`, `owned_sets.py`,
  `cardinals.py`, `ordinals.py` — not under `src/`;
- `rg` over `src/` finds **no** reference to `SetsCategory`, `set_categories`,
  `EnumeratedSets` or `PartiallyOrderedSets`;
- `OwnedCategory` survives in live code only through three utilities:
  `src/dzack_research/utilities/category_graph.py`, `megadoc.py`,
  `construction_universe.py` (plus the `archives/preamble/owned_category*.py` definitions
  and `docs/preamble-graph.json`).

Consequence for #606: there is no live `src/` consumer of the set-layer provider path to
migrate, so the migration half of the issue is not blocked on kernel work in this
repository — what remains is the formal half (#97, #96) and the utilities' use of the
`OwnedCategory` machinery, which is shared transitional machinery that `research#384`
retains for removal after the last dependent layer migrates.

## Publication blockers (exact)

- `lean-categories`: authoring/checkout/push from this session is withdrawn by
  authorization. Prepared artifacts remain in this repository for the owner or the
  coordinator to publish; nothing was pushed there and no credentials were created.
- research issues: read-only through the connected GitHub route, so `#606` and `#219`
  cannot be closed or commented from here.
