# The literature corpus

The sources every mathematical assertion in `tests/coxeter_tdd_specs/` is checked against, plus the conventions and citation discipline that govern how they are cited.

| Path | What it is |
| --- | --- |
| `PROJECT_CONVENTIONS.md` | The Gram-matrix convention $B_{ij} = 2\cos(\pi/m_{ij})$, the inverted definiteness table it forces, the citation requirement, and the specimen-sourcing rule. |
| `BIBLIOGRAPHY.md` | The approved sources, the citation floor below which no citation is required, and the per-subject source assignment. |
| `citations/CITATION_FORMAT.md`, `citations/CITATION_INDEX.md` | The CITATION/FACT comment block every asserting test carries, and the fact-to-source-to-test index. |
| `VERIFICATION_METHODOLOGY.md` | The verification standards: form linearity, the Cartan relation, reflection preservation, exact arithmetic over `AA`, and the determinant fallacy. |
| `papers/` | Extracts from research papers used as oracles. |
| `wikipedia/`, `wikiwand/` | Curated transcriptions of encyclopedia articles, each naming its article revision. |
| `tools/webpage_to_markdown.py` | The script that made the original captures. |

## Why there are no raw article captures here

The `wikipedia/` and `wikiwand/` notes are transcriptions from full-article captures that lived in the Coxeter working tree (`gitclones/Coxeter/research/literature/sources/`, five files, about 800 KB). Those captures were full page scrapes: navigation chrome, edit links, and image markup around the mathematics, and two of the five were duplicates of the others reached through redirects, with a third a Wikiwand mirror of one.

They are not landed.
What was taken from them instead, on 2026-08-20:

- the **article revision id** of each capture, added to the header of every note derived from it, so each transcription names a permanent link rather than only a retrieval date — Coxeter group at oldid 1300325012 (13 July 2025), Coxeter–Dynkin diagram at oldid 1290398091 (14 May 2025);

- three sections the curated notes did not yet cover, transcribed as new notes: `wikipedia/affine_coxeter_groups_witt_symbols.md`, `wikipedia/diagram_folding.md`, `wikipedia/shephard_groups_rank_two.md`.

A note here is an oracle only for what it states.
Where a transcription and its source article disagree, or where the article itself is wrong, the note says so in its own text — see the determinant-classification caveat in `wikipedia/coxeter_dynkin_diagrams.md` and the order-list defect recorded in `wikipedia/shephard_groups_rank_two.md`.
