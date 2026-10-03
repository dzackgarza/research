# Lattice database: agent guidance

`README.md` owns the schema, the commands and the conventions. This file states the purpose that
governs every change to the database.

## Four independent workflows

Seeding reads a stored source and writes a permanent `lattices/<TAG>.md` card from its defining
data, source identity and citation. It uses the assigned tag. It does not load other cards, derive
invariants or run verification.

Authoring writes or edits the same card format without a stored source row. It does not run
verification. A sparse card is a site card.

Enrichment computes further fields on existing cards and records the computations in
`certificates.yaml`. It does not decide whether a card may enter the site.

Verification is read-only. The modules in `src/latticedb/checks/` inspect stored cards, relations
and sources in scheduled CI and report errors. The site build reads cards and renders pages.

## The database stores every computation

The database exists to store and cache the computations about lattices: every invariant, every
identification, every map and every transcription of a source. A result that was computed and
then thrown away is a defect, whatever the computation was done for.

So a computation done for a record, or for a check of a record, lands in the database in the same
change:

| What was computed | Where it is stored |
| --- | --- |
| An invariant of one lattice: a genus symbol, a class number, the order of $O(L)$, a root system | A field of the record, in the block of its hypothesis |
| A relation between two records: a twist, a dual, an orthogonal complement, a gluing | A `related` entry of each record, and the prose |
| A map between lattices: an embedding, an isometry, a generator of a group action | A morphism file `morphisms/<S>-<T>.md` |
| An isometry from a tagged lattice to its scaled dual, whose dual has no separate tag | A morphism file `morphisms/dual/<slug>.md`, with the dual basis and scale stated |
| What a source states: a table, a list of Gram tensors, a basis in other coordinates | `sources/<source>/`, read by a source module; comparison with cards belongs to `src/latticedb/checks/` |
| An identification of a record with an entry of a source | The reference of the record, with the locator of the entry, and the prose that states the argument |

When a result has no place in the schema, the schema gains one: a field in `model.py` with its
validator, its row in `README.md`, and the value on every record that the computation covers.
It is never left in a scratch script, a terminal or a chat.

A script that produced stored data is itself part of the database. Its source reader can seed
cards. An independent check module can compare source claims with the cards later.

## A certified computation never runs again

`certificates.yaml` records each computation that the database has carried out, with the digest of
its inputs. A computation with a certificate for its present inputs is never carried out again: the
stored value is the result, and computing it again to "re-prove" it spends hours and proves nothing
new. Only a change of the inputs, or a removed certificate, starts it again.

The scheduled verification job runs in CI, never during seeding, authoring or site rendering.
Enrichment runs as its own workflow. A test computes on one small specimen, such as $A_2$ (record
`0012`); it never runs a derivation or a SageMath computation over every record.

A new computation gets a certificate name in `certificates.py` and a step in `latticedb enrich`
before it stores its first value.
