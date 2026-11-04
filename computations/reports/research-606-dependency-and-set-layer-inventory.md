# research#606 — dependency state and reconciliation against the actual public API

> Governing caveat (recorded after this file): the migration language below is #606's
> wording, not an independently established mandate for research-side implementation.
> See [research-606-intent-conflict-review.md](research-606-intent-conflict-review.md):
> this repo consumes maintained public interfaces; implementation belongs upstream.
> Nothing in this file was acted on as rearchitecture.

Supersedes and corrects this file's inventory section. The earlier draft claimed the set
layer was unreferenced ("vacated") because `rg SetsCategory|set_categories` over `src/`
found nothing. That inference was wrong: the surface research consumers import is a
star-reexport, so names need not appear under `src/` at all. The corrected reconciliation
below is grounded in the source shown.

## The actual public surface

`src/dzack_research/preamble/all.py` (the session module research notebooks import) says
of itself (line 4-9): *"The session namespace ... belong to `sage_extensions.all`. This
module re-exports it ... and registers that name so the parser treats its star import as
the complete session."* and it does:

```python
from sage_extensions import language_runtime as _language_runtime
from sage_extensions.all import *                    # noqa: F401,F403
from sage_extensions.categories.group.groups import OwnedGroups as Groups
_language_runtime.register_session_module(__name__)
```

`sage_extensions.all` (provider snapshot `.scratch/se-provider-6ad7a5ea`) then re-exports
the set layer in bulk, `all.py:406-439`:

> `Sets, CountableSets, CountablyInfiniteSets, EnumeratedSets, FiniteSets,
> FinitePowerSets, PowerSets, PartiallyOrderedSets, TotallyOrderedSets, WellOrderedSets,
> CartesianProductsOfSets, CoproductsOfSets, UncountableSets, InfiniteSets, ...`

and those classes live in
`sage_extensions/categories/sets/set_categories.py` (7048 lines) as `OwnedCategory`
subclasses: `EnumeratedSets` (314), `Sets` (1265), `PowerSets` (3320), `FinitePowerSets`
(3856), `CartesianProductsOfSets` (4758), `CoproductsOfSets`(5581), `PartiallyOrderedSets`
(6741), `TotallyOrderedSets` (6838), `WellOrderedSets` (6981), with `OwnedCategory` based
in `sage_extensions/owned_category.py`.

So the transitional Python set category, with the provider ordering and cooperative
initialization #606 names, **is** research's live public API today. The prior "vacuity"
statement is withdrawn.

## Acceptance reconciliation

`research#606`'s bullets, checked against this surface:

1. **Each set-layer operation reconciled to its formal catalogue declaration or the
   precise missing input with its owner.** The population is the exposed list above. From
   earlier source inspection of the formal owner (`lean-categories` at `fc6d3d6`, checked
   by build, now read-only for this session): `Sets`, products/coproducts, diagram limits
   and colimits (incl. filtered) are registered and green; powersets, cardinality and
   ordinals (incl. the Hessenberg product) are registered and green; finite subsets with
   `directImage` and the PO/TO categories exist (issues #95, #98 delivered-side, though
   open). **Missing**: `lean-categories#97` (`WellOrderedSets`, `E_mon`, forgetful chain,
   order type) and `lean-categories#96` (selected ranking `rank : X ≃ Fin n` / `≃ ℕ` with
   laws) — #96's body defers its order contract to #97. These are the precise missing
   formal inputs, and they belong to that upstream owner.
2. **Public research consumers obtain the set-layer constructions and operations through
   the catalogue-derived language, with complete data and result types, and the migrated
   path has no local provider ordering or cooperative initializer.** **Not met.** Today's
   path is exactly its negation: `preamble.all → sage_extensions.all → set_categories.py
   (OwnedCategory)`. Meeting it needs the catalogue-derived session surface, whose owners
   are `lean-cas-dsl` (kernel) and `lean-categories` (declarations), and additionally need
   #97/#96 for the ordered part.
3. **Every computation on that path is an opaque leaf registration; existing specimens
   preserved; terminal execution and independent acceptance under
   `sage-extensions#234/#498` under `DEV-58`.** External to this repository.
4. **`research#384` retains removal of shared transitional Python machinery after the last
   dependent layer migrates.** Open and downstream of the above.

## Exact external dependencies

- `lean-categories#97`, then `#96` — open, owned by `lean-categories`; this session is
  barred by authorization from authoring or checking out that repo.
- the `lean-cas-dsl` catalogue-derived session surface — the kernel this reconciliation's
  consumers must adopt; external repository.
- `sage-extensions#234/#498` (`DEV-58`) — terminal execution and independent acceptance;
  external repository issues.
- publication: the prepared `lean-categories#95` inclusion-registration artifact and the
  ordinal natural-product patch wait for the owner's publishing route; research issues are
  read-only through the connected GitHub route, so neither #606 nor #219 can be closed
  from here.

## Research-side work done in this pass

Corrected this record. No other work was started: any further research-side step on #606
(adding catalogue-derived names to `preamble.all`, shrinking the exposed transitional
surface, or touching `archives/`) would either change behavior under acceptance the issue
has not yet enabled, or duplicate work owned upstream.
