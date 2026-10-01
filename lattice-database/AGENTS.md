# Lattice database: agent guidance

`README.md` owns the schema, the commands and the conventions. This file states the purpose that
governs every change to the database.

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
| What a source states: a table, a list of Gram tensors, a basis in other coordinates | `sources/<source>/`, read by a module `src/latticedb/<source>.py` with a `check` that compares the source with the records |
| An identification of a record with an entry of a source | The reference of the record, with the locator of the entry, and the prose that states the argument |

When a result has no place in the schema, the schema gains one: a field in `model.py` with its
validator, its row in `README.md`, and the value on every record that the computation covers.
It is never left in a scratch script, a terminal or a chat.

A script that produced stored data is itself part of the database: it becomes the module that
reads the source and checks it, so that `latticedb check` derives every claim of the prose from
stored data again.
