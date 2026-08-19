# Online Provenance: GAP crystallographic stack (2026-02-17 UTC)

## Scope

Source survey for first-class checklist/reference surfaces covering:

- `Cryst`
- `CARATInterface`
- `CrystCat`

Current-phase cursory package-surface check:

- no additional clear in-scope bilinear-form lattice package surface was identified in this pass; focus remained on Goal 2 contract fidelity for existing crystallographic surfaces.

## Canonical and supporting URLs used

- Cryst package page:
  `https://gap-packages.github.io/cryst/`
- GAP Cryst package manual (space-group selector argument semantics):
  `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm`
- GAP package install/index page with package listings and short descriptions:
  `https://www.math.rwth-aachen.de/~Greg.Gamble/gap4r3/pkg/inst.htm`
- GAP Reference Manual, CARAT chapter section (canonical signatures for `Bravais*`, `Carat*`, normalizer/centralizer methods):
  `https://docs.gap-system.org/doc/ref/chap44.html`
- CARATInterface package manual (signature confirmation for CARAT methods):
  `https://www.math.rwth-aachen.de/~GAP/WWW2/PackagePages/caratinterface/doc/manual.pdf`
- GAP3 Cryst chapter mirror (supporting detailed selector semantics):
  `https://webusers.imj-prg.fr/~jean.michel/gap3/htm/chap061.htm`

## Evidence extraction summary

- Package-level existence and role evidence:
  - package listings include entries for `CARATInterface`, `Cryst`, and `CrystCat`.
- Canonical method-surface evidence:
  - Cryst docs provide selector-domain semantics for
    `SpaceGroupsByPointGroupOnRight(P[, normedQclass[, orbitsQclass]])`:
    `normedQclass` is `false` or a list of normalizer elements, and `orbitsQclass` is
    boolean (`true` requests all representatives in each orbit).
  - GAP ref chapter 44.6 and CARATInterface manual expose one-argument signatures for
    `BravaisGroup`, `PointGroupsBravaisClass`, `BravaisSubgroups`, `BravaisSupergroups`,
    `NormalizerInGLnZ`, and `CentralizerInGLnZ` in the active contract surface.

## Signature-fidelity closure in this pass

- Replaced placeholder method signatures (`...`) in the crystallographic stack reference/checklist with canonical forms from GAP Reference chapters 35 and 44.
- Added canonical methods missing from previous checklist/reference surface:
  - `WyckoffNormalClosure(G, p)`
  - `IsBravaisEquivalent(R, S)`
  - `CaratZClass(R)` / `CaratQClass(R)`
  - `IsCaratZClass(R)` / `IsCaratQClass(R)`
- Reclassified `CrystCatZClass(...)`, `CrystCatQClass(...)`, and `CrystCatQClasses(...)` as legacy-alias triage items pending explicit confirmation in canonical current docs.

## Selector-domain closure (2026-02-18)

- Lifted explicit value-domain constraints for `normedQclass` / `orbitsQclass` from Cryst
  package docs into the crystallographic stack reference/checklist surfaces.
- Demoted selectorized CARAT signatures with `f`/`s`/`k` as non-canonical in this surface;
  current ref/manual evidence used for active contracts exposes one-argument forms.

## Network retrieval note

- 2026-02-18T00:34:39Z UTC: attempted direct retrieval of
  `https://docs.gap-system.org/pkg/cryst/htm/CHAP002.htm` twice via web open; both attempts
  timed out. The same URL remained source-backed through indexed snippet evidence, and the
  unresolved retrieval issue is tracked as environment-access (`timeout`) rather than source
  non-existence.

## Local docs linked

- `docs/crystallographic_stack_methods_checklist.md`
- `docs/crystallographic_stack/lattice/research_readme.md`
