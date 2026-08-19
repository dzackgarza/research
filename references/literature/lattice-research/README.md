# Literature extractions from the lattice-research corpus

Third-party published sources, converted to markdown (OCR/extraction) inside
the `~/gitclones/lattice-research` corpus and migrated here on 2026-08-20.
These files are the citation authority the migrated theory notes point at
(`notes/topics/coble-enriques-lattice-theory/reference-map.md` and
`claim-map.md` resolve their `theory/references/literature/` paths here).
They are reference material by external authors — never edited as repo
mathematics, never held to repo prose policy.

| file | source |
| --- | --- |
| `aegs_2023.md` | Alexeev–Engel–Garza–Schaffler, compact moduli of Enriques surfaces (bib key `aegs2023compact`) |
| `bailyborel1966.md` | Baily–Borel, *Compactification of arithmetic quotients of bounded symmetric domains*, Ann. Math. 84 (1966) |
| `conway1988mass.md` | Conway–Sloane, *Low-dimensional lattices IV: the mass formula*, Proc. R. Soc. A 419 (1988) |
| `conway1999sphere.md` | Conway–Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed. (1999) |
| `dawes2022orbits_source_notes.md` | Locally authored source notes on Dawes, *Orbits in Lattices* (arXiv:2205.10601) |
| `dolgachev_kondo_2013.md` | Dolgachev–Kondō on Coble surfaces and Enriques surfaces |
| `huybrechts_k3_lectures.md` | Huybrechts, *Lectures on K3 Surfaces* |
| `milnor1973symmetric.md` | Milnor–Husemoller, *Symmetric Bilinear Forms* (1973) |
| `nikulin1979integral.md` | Nikulin, *Integer symmetric bilinear forms and some of their geometric applications* (1979) |
| `pieroni_2026_coble_surfaces.md` | Pieroni, on Coble surfaces |
| `popa_kodaira.md` / `popa_kodaira.pdf` | Popa, Kodaira dimension notes (extraction plus the source PDF) |
| `thas_1994.md` | Thas, *A rational sextic associated with a Desargues configuration*, Geom. Dedicata 51 (1994) |
| `vinberg1972units.md` | Vinberg, on units of quadratic forms (1972) |
| `vinberg1975arithmetical.md` | Vinberg, *Some arithmetical discrete groups in Lobachevskii spaces* (1975) |
| `vinberg1983two.md` | Vinberg, *The two most algebraic K3 surfaces* (1983) |
| `peters-sterk_symmetric-quadratic-forms.md` | Peters–Sterk, *Symmetric and Quadratic Forms, with Applications to Coding Theory, Algebraic Geometry and Topology*, TU Eindhoven, version June 2024. OCR conversion; the source corpus recorded no URL for it, and none is fabricated here — the authorship, institution, and version line are the file's own front matter. |

Not migrated:

- `ocr-response.json` — the raw OCR service response behind one extraction,
  superseded by its committed markdown (registry disposition WRONG).
- `wikipedia_vinbergs_algorithm.md` — a summary of Vinberg's algorithm the
  preamble already owns in full
  (`hyperbolic_lattices.sage :: vinberg_algorithm`); registry disposition
  REPRESENTED.
- Three symlinked extractions whose targets (`~/pdfs/arxiv/2108.06236/paper.md`,
  `~/pdfs/arxiv/2205.10601/paper.md`,
  `~/pdfs/other/sterk_1991_period_enriques_I/content.md` — Dawes 2021, Dawes
  2022, Sterk 1991 part I) are broken on this machine: the content does not
  exist to copy. The bibliographic identities survive in `references.bib` and
  the reference map; re-fetch from arXiv 2108.06236, arXiv 2205.10601, and
  Sterk, Math. Z. 208 (1991) 1–36 when the extractions are needed.
