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
| An isometry from a tagged lattice to its scaled dual, whose dual has no separate tag | A morphism file `morphisms/dual/<slug>.md`, with the dual basis and scale stated |
| What a source states: a table, a list of Gram tensors, a basis in other coordinates | `sources/<source>/`, read by a module `src/latticedb/<source>.py` with a `check` that compares the source with the records |
| An identification of a record with an entry of a source | The reference of the record, with the locator of the entry, and the prose that states the argument |

When a result has no place in the schema, the schema gains one: a field in `model.py` with its
validator, its row in `README.md`, and the value on every record that the computation covers.
It is never left in a scratch script, a terminal or a chat.

A script that produced stored data is itself part of the database: it becomes the module that
reads the source and checks it, so that `latticedb certify` derives every claim of the prose from
stored data, once.

## A certified computation never runs again

`certificates.yaml` records each computation that the database has carried out, with the digest of
its inputs. A computation with a certificate for its present inputs is never carried out again: the
stored value is the result, and computing it again to "re-prove" it spends hours and proves nothing
new. Only a change of the inputs, or a removed certificate, starts it again.

Heavy computation runs in the nightly CI job `.github/workflows/lattice-database-certify.yml`, never
on this machine over the corpus. A test computes on one small specimen, such as $A_2$ (record
`0012`); it never runs a check, a derivation or a SageMath computation over every record. Locally,
`latticedb certify --tag <tag>` runs for one new record at most, and `latticedb check` computes
nothing.

A new computation gets a certificate name in `certificates.py` and a step in `latticedb certify`
before it stores its first value.
