# lexicon — the centralized type surface of the spike

One stub subtree from which all code draws its types.
Two layers:

- **`../typings/sage/`** (sibling of this package — a stub tree cannot live inside a checked package, mypy would map each file to two module names) — PEP 561-style `.pyi` stubs for exactly the `sage.*` modules this package imports.
  They give `Parent`, `Element`, `Matrix`, `Integer`, … real types (Sage ships none), which is the only fix for the `subclass of Any` / `no-any-return` error families.
  Stubs declare the surface the repo uses, typed in lexicon terms; they are verified against the running Sage by `verify_against_sage.py`.
- **runtime modules** (`foundations.py`, `algebra.py`, `geometry.py`, `interop.py`) — declaration-only, importable vocabulary: semantic mathematical nouns (researcher-facing) and `Sage*` interop nouns (dev-facing, only where Sage's object differs from ours).
  No logic lives here.

`INVENTORY.md` is the catalogue and the normative naming/representation policy.
Read it before adding or using a noun.
`__init__.py` re-exports the whole lexicon, including the owned lattice tower from `..algebra.domain_algebra`, so downstream signatures need one import:

```python
from ..lexicon import Lattice, Matrix, ExactScalar, FiniteAbelianGroup
```

## Checking

```
just lexicon-check    # from the spike root
```

runs (1) `mypy --strict` over this package with `../typings/` as the stub path, and (2) the Sage identifier verification.
Both must pass before any lexicon change lands.

## Traps

Known Sage typing pitfalls (category methods are copied not inherited; the abstract element markers; no `__iter__` on vectors; stub-tree placement; QC auto-activation) are recorded once, in the agent-memory vault: `projects/github.com__dzackgarza__research/traps/sage-type-surface-traps-for-the-lexicon-stub-tree`. Read it before concluding the verifier or mypy is wrong.

## Extending

- New noun → catalogue it in `INVENTORY.md` Part II first, then declare it in the one module the catalogue names, following the Part III representation priority (owned class → alias → union → protocol → NewType).
  Never `Any`.
- New Sage surface → extend the relevant `.pyi` (add the module if new), then add the identifiers to `verify_against_sage.py`. Do not hand-write a protocol at the use site.

## Migration status (M1–M4 executed 2026-07-08)

- **M1 — QC stub path: active by upstream convention.** The upstream `mypy-global.ini` sets `mypy_path = typings` relative to the project dir, so the stub tree at the spike root is picked up by the project QC run automatically.
  Stubs replace `Any` with real types, so they *surface* latent package errors; the stubs themselves are never QC targets (QC checks `*.py` only) — the buck stops here by construction.
- **M2 — import surface: done.** All `as *Carrier` renames are gone; every package module draws its type nouns from `..lexicon`. The superseded partial protocols (`SageRing`, `SageFreeModule`, `SageModuleElement`, `MatrixGroupLike`, `PermutationGroupLike`, `FundamentalChamberLike`) are deleted from `domain_algebra`, which now takes its type-level nouns from the lexicon under `TYPE_CHECKING` (keeping its no-runtime-Sage-import rule).
- **M3 — codecs: done.** `ExactScalar` is the `foundations` union; `GramMatrix` is a NewType over the real `Matrix`; `MorphismMatrix` is retired outright (a morphism's matrix is an ordinary `Matrix`; the morphism object is the validation witness).
- **M4 — honest renames: done.** `FiniteAbelianGroup` is the runtime base class of the discriminant tower (`DiscriminantForm` remains a transitional alias); `fundamental_chamber` → `Polyhedron`; `Genus.local_symbol(s)` → `SageLocalGenusSymbol`; the enumeration mixins lost their Kernel/Host names (`_PositiveDefiniteEnumeration`, `_NegativeDefiniteEnumeration`, `_RootGeneratedProvenance`, `_*Self` type-checking self-types).

Outstanding follow-up: per-site re-annotation of deprecated bare `DiscriminantForm` signatures — each site migrates to the object it actually means: `FiniteAbelianGroup` (torsion ℤ-module G), `BilinearDiscriminantForm` (pair (G, b)), or `QuadraticDiscriminantForm` (pair (G, q)); the bilinear and quadratic theories are distinct over ℤ and the choice is deliberate per site (INVENTORY.md II.2 ontology note).
