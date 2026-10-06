# Lattice database: agent guidance

`README.md` owns the schema, the commands and the conventions. This file states the purpose that
governs every change to the database.

## The preamble owns lattice mathematics

`latticedb` consumes the lattice mathematics presented by
`dzack_research.preamble`.  It does not define an independent determinant,
signature, discriminant form, genus, root, isometry, theta-series, overlattice,
or other lattice invariant.  A missing shared operation is repaired at its
preamble owner and then consumed here; it is never implemented as a leaf-local
algorithm.  This is the cross-repository contract recorded by
`HANDOFF.md` and by the corresponding foundational complaint in the research
repository.

The schema/data-model layer (`model`, `catalogues`, `geometric`, `graphs`, `corpus`)
is deliberately preamble-free and must parse/validate under ordinary CPython.
`just test` exercises only that fast coherence layer. Workflows that compute or
verify mathematical lattice claims (`enrich`, `verify`, certification and CI
validation) run under the repository's Sage Python with both `../src` and this
package's `src` on `PYTHONPATH` and consume the preamble operations.

## Independent workflows

Seeding reads a stored source and writes a permanent `lattices/<TAG>.md` card from its defining
data, source identity and citation. It uses the assigned tag. It does not load other cards, derive
invariants or run verification.

Authoring writes or edits the same card format without a stored source row. It does not run
verification. A sparse card is a site card.

Enrichment computes further fields on existing cards without certifying them. It does not decide
whether a card may enter the site.

Certification is a separate CI phase. It computes each uncertified value from the card's defining
mathematical input. If an authored or seeded value disagrees, the computed value replaces it. The
resulting card value then receives a certificate hash, and `certificates.yaml` records that hash
with computation provenance.

Verification is read-only. The modules in `src/latticedb/checks/` inspect stored cards and relations
and report structural or certificate-consistency errors. Source-to-card collation is a separate
provenance workflow. The site build reads cards and renders pages.

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
| A map whose domain is a lattice card: an embedding, an isometry, a generator of a group action | A `morphisms` entry on that source lattice card; the entry names its target |
| A Lie group such as $O(p,q)$ | A `lie-groups/<slug>.md` card |
| $O(L)$ or another arithmetic subgroup attached to a lattice | An `arithmetic-groups/<slug>.md` card, referenced by the lattice card |
| The dual lattice $L^*$ | `dual_gram_tensor = G_L^{-1}` on the card of $L$; never a second lattice card |
| A chosen isometry $L\to L^*(k)$, when one is recorded | Morphism data on the card of $L$, with the derived dual target described there; never a separate morphism card |
| What a source states: a table, a list of Gram tensors, a basis in other coordinates | `sources/<source>/`, read by a source module; source-to-card comparison is importer/provenance testing only, never mathematical verification |
| An identification of a record with an entry of a source | The reference of the record, with the locator of the entry, and the prose that states the argument |

When a result has no place in the schema, the schema gains one: a field in `model.py` with its
validator, its row in `README.md`, and the value on every record that the computation covers.
It is never left in a scratch script, a terminal or a chat.

A script that produced stored data is itself part of the database. Its source reader can seed
cards. Source-intake tests may check that the importer copied or transformed that source as intended;
agreement with the archived source is not evidence that the resulting mathematical claim is true.

## A certified computation never runs again

The lattice card is the only store of a computed value. Its `certifications` map cites a SHA-256
certificate hash that commits to the computation name, the Gram tensor and that stored result.
`certificates.yaml` stores the same hash with computation provenance, never a second copy of the
result. A matching completed certificate is permanent: implementation/version changes do not make
it stale. Changing the Gram tensor or result breaks the hash and requires a new computation.
A timeout or unfinished computation has no certificate.

The scheduled certification job runs in CI, never during seeding, authoring, enrichment or site
rendering. A test computes on one small specimen, such as $A_2$ (record `0012`); the full
certification computation runs only in CI.

A new certifiable computation gets a certificate name and a step in `latticedb certify`
before it stores its first value.
