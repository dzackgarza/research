# lrslib Online Provenance Snapshot (2026-02-17 UTC)

Scope: first-class checklist/reference surface creation for the missing `lrslib` package surface.

---

## 1. Sources surveyed

Canonical upstream pages:

- `https://cgm.cs.mcgill.ca/~avis/C/lrslib/USERGUIDE.html`
- `https://cgm.cs.mcgill.ca/~avis/C/lrslib/lrslib.html`
- `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrs.1`
- `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/mplrs.1`
- `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/lrsnash.1`
- `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/man1/fel.1`

Supplemental mirrors (used for man-page surfaces not fetchable from the canonical man index in this environment):

- `https://www.mankier.com/1/polyv`
- `https://manpages.debian.org/testing/lrslib/xref.1.en.html`
- `https://www.mankier.com/1/lrsscripts`

---

## 2. Extracted command/method surface

From user-guide/package/man-page sources:

- Core commands: `lrs`, `mplrs`, `redund`, `minrep`, `lrsnash`, `nash`, `2nash`, `fel`, `xref`, `hvref`, `polyv`.
- Parallel controls in `mplrs`: `-processes`, `-scale`, `-maxtreesize`, `-maxdepth`, `-mindepth`, `-checkfrequency`, `-stop`, `-estimatelimit`, `-cache`.
- `lrs` keyword/option surfaces: arithmetic backend selectors, optimization controls, projection/elimination/extraction/truncation options, enumeration output controls (`allbases`, `printcobasis`, `printslack`, `maxoutput`, `maxcobases`), restart/seed/time-estimate controls.
- Script tooling documented in `lrsscripts`: `projred`, `mfel`, `mlrs`, `tlrs`, `plotV`, `plotR`, `plotL`.

---

## 3. Environment access notes

- The canonical man directory index URL was discoverable but not directly openable through this environment's web fetch path:
  - `https://cgm.cs.mcgill.ca/~avis/C/lrslib/man/`
- Individual canonical man pages (`lrs.1`, `mplrs.1`, `lrsnash.1`, `fel.1`) were retrievable directly and were treated as primary source.
- For helper pages where canonical fetch-path access was incomplete (`polyv`, `xref/hvref`, `lrsscripts`), mirrored man-page sources were used with explicit labeling.

---

## 4. Domain notes captured for docs

- lrslib is a polyhedral reverse-search/lattice-point workflow stack.
- It is not a quadratic-form genus/discriminant/isometry API surface.
