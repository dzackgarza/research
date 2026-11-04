# lean-categories#95 — the finite-subset inclusion registered (patch artifact)

Artifact block for parent publication review. Prepared and tested locally in the shared
clone at `$HOME/gitclones/lean-categories`, which is left clean at its original tip.

## Exact source and base

| field | value |
| --- | --- |
| repository | `dzackgarza/lean-categories` |
| base branch | `main` |
| base commit | `fc6d3d6961223c75290c93da540c87f17a926cc7` |
| base tree | the tip above; the clone was clean before and after |
| artifact | `computations/reports/leancategories-95-finite-subsets-inclusion.patch` (2133 bytes, sha256 `21449635a827a45e88eb63355175e52513c4a7db9115ff7056df62e3cb14a46e`) |
| local commit | `6ae8c8d6d78a81dc3850070f9c3d9a919f2135c8` |
| commit tree | `8bffb43bccc2b26b2d1b8f341dced98eafe62c70` |
| proposed target branch | `agent/95-finite-subsets-inclusion` (not created anywhere; needs the publishing channel) |

The patch applies to pristine `fc6d3d6` (`git apply --check` verified after the clone was
reset).

## What #95 asked for, and what was already there

`lean-categories#95` requires `P_fin : Sets ⥤ Sets`, `X ↦ Finset X`, `f ↦ Finset.image f`,
with functor laws, "natural inclusion into the full powerset (where variance is
appropriate)", and a registration at the formal owner.

Read against the base tip, almost all of it already exists in
`LeanCategories/Catalogue/Semantics/Foundation/FiniteSubsets.lean`:

- `directImage : SetsCat.{0} ⥤ SetsCat.{0}` with `map := Finset.image` and its laws
  (`Finset.image_image`, etc.) — line 35;
- `inclusion (X) : finiteSubsets X ⟶ powerSet X` — line 51;
- `inclusion_natural` — the naturality square of that inclusion against direct image;
- `instance inclusion_mono (X) : Mono (inclusion X)` — already declared;
- the functor registration `fun.sets.finite_subsets.direct_image`.

The one piece missing was the **registration of the inclusion itself**, so the catalogue
never exposed the natural transformation #606's consumer reads. That is the entire
content of this patch:

```lean
normalized_registry .inclusion
  { id := ⟨"incl.sets.finite_subsets"⟩, category := CategoryId.sets
    sub := ⟨"obj.sets.finite_subsets"⟩, super := ⟨"obj.sets.power_set"⟩
    declaration := `CasCatalogue.Foundation.FiniteSubsets.inclusion
    mono := `CasCatalogue.Foundation.FiniteSubsets.inclusion_mono }
```

No declaration, theorem, statement or existing registration is modified; the patch adds
five lines at the end of the file's `CasCatalogue` namespace.

## Acceptance evidence

- `lake build LeanCategories.Catalogue.Semantics.Foundation.FiniteSubsets` — **green,
  2744 jobs**, with the entry present.
- The `normalized_registry` command runs `validateInclusion` at elaboration time, so the
  green build is the validator's acceptance: the category `CategoryId.sets` resolves, both
  `obj.sets.finite_subsets` and `obj.sets.power_set` are registered objects of it, the
  declaration is a morphism of that category, its endpoints use the shared parameter, and
  `inclusion_mono` proves `Mono` of that exact arrow.
- A first attempt added a duplicate `inclusion_mono` theorem; the build rejected it
  ("already been declared") and it was removed. The shipped patch adds no proof.

## Scope not claimed

- This does not discharge #95 by itself: closing needs the entry published at the owner
  and the owner's confirmation. It also does not touch `SetsCat.{0}`'s universe
  restriction, which the issue does not raise.
- No cross-owner acceptance is claimed, no credentials were created, and nothing was
  pushed to `dzackgarza/lean-categories` from this VM.

## Publication request

Create a commit on `dzackgarza/lean-categories` whose parent is
`fc6d3d6961223c75290c93da540c87f17a926cc7`, applying the patch above, on branch
`agent/95-finite-subsets-inclusion`, and open it for review rather than merging blind:
the registration is checkable by building
`LeanCategories.Catalogue.Semantics.Foundation.FiniteSubsets`.
