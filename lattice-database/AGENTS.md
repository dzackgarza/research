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

There is no preamble-free architectural layer inside `latticedb`. Database code
may import and call `dzack_research.preamble` wherever orchestration needs a
mathematical construction, invariant, recognition, comparison, or validation.
The boundary is ownership, not importability: lattice-db owns cards, schemas,
source collation, computation scheduling, serialization, caching, certificates,
indices and publication; the preamble owns the mathematics those workflows ask
for.  A database module must delegate a mathematical operation to the preamble
rather than reimplementing it locally.

`just test`, enrichment, verification, certification, source collation,
construction validation and site generation may therefore run with the preamble
available.  A particular workflow may remain structural-only because that is its
job, not because database code is forbidden from importing the preamble.

## Independent workflows

Seeding reads a stored source and writes a permanent `lattices/<TAG>.md` card from its defining
data, source identity and citation. It uses the assigned tag. A row whose Gram tensor a card already
states joins that card instead, because a Gram tensor determines its lattice and a lattice has one
card. Seeding does not derive invariants or run verification.

Authoring writes or edits the same card format without a stored source row. It does not run
verification. A sparse card is a site card.

Enrichment requests further fields from preamble-owned operations and writes their returned values
without certifying them. It contains no lattice algorithm of its own and does not decide whether a
card may enter the site.

Certification is a separate CI phase. It asks the preamble to compute each uncertified value from
the card's defining mathematical input. If an authored or seeded value disagrees, the preamble
result replaces it. The
resulting card value then receives a certificate hash, and `certificates.yaml` records that hash
with computation provenance. A value that a seeded source proves, such as the regularity of a form
in the Jagy–Kaplansky–Schiemann list, is certified when it is seeded: its certificate names the
source's citation as provenance, and certification never computes it.

Verification is read-only. The modules in `src/latticedb/checks/` inspect stored cards and relations,
check structural/reference/certificate coherence, and may construct the corresponding preamble
objects and morphisms to validate stored mathematical claims. The mathematics remains owned by
the preamble; verification only orchestrates those public operations and reports disagreements.
Source-to-card collation is a separate provenance workflow. The site build reads cards and may
request the values that publication needs from preamble operations.

No module under `src/latticedb` may import Sage, PARI/cypari2, python-flint or another mathematical
engine directly. Preamble imports are the computational boundary and are expected wherever database
orchestration needs mathematics. Pure-Python reimplementations of lattice/root/group/polytope
algorithms are equally forbidden: moving an algorithm out of an engine call does not make it database
code.

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

**The schema lands first.** Work that adds invariants to the database starts with the schema: each
field in `model.py` with its validator, its `README.md` row, and its certificate name and request
wiring, committed before any preamble operation is probed or implemented. The committed schema is
the specification that the preamble work then fills. A worker that probes the preamble or an engine
before that commit is selecting work by what already computes, not by what the database must store.
On 2026-10-09 a worker on `definite-theta-series-modular-decomposition` spent its first hours
reading Sage's local-density and Siegel-product sources with no field committed.

A script that produced stored data is itself part of the database. Its source reader can seed
cards. Source-intake tests may check that the importer copied or transformed that source as intended;
agreement with the archived source is not evidence that the resulting mathematical claim is true.

## Certification certifies values; a procedure need not terminate

An invariant is computable here when a procedure produces its value. The procedure does not have
to decide the general problem or terminate on every input. Vinberg's algorithm computes
`hyperbolic.reflective`; the search of `L.is_regular()` computes `definite.regular`.

Certification certifies the values that appear. A value that a procedure produced, or that a cited
source proves, gets a certificate. A field with no value claims nothing: its value is unknown, and
that is a correct card state. A procedure that does not terminate on a card certifies nothing for
that card, so it can never put a false claim on it.

So these are never reasons to call an invariant uncomputable, to request it on fewer cards, to remove
or weaken its operation, or to report it as a gap:

- the general problem is undecidable or not known to be decidable;
- the procedure does not terminate on some cards;
- the procedure is slow.

A gap is an invariant for which no procedure produces the value that a card would state. The CI
certification job, about six hours, is the only time bound, and each run certifies more values. A
local run only shows correct values on small nontrivial specimens, or finds a performance defect
after a CI timeout.

## A certified computation never runs again

The lattice card is the only store of a computed value. Its `certifications` map cites a SHA-256
certificate hash that commits to the computation name, the Gram tensor and that stored result.
`certificates.yaml` stores the same hash with computation provenance, never a second copy of the
result. A matching completed certificate is permanent: implementation/version changes do not make
it stale. Changing the Gram tensor or result breaks the hash and requires a new computation.
A timeout or unfinished computation has no certificate. A computation that ran for a whole
certification job without finishing is logged in `exceeded.yaml` and is never requested again,
so the nightly job does not spend each run on the same computation.

The scheduled certification job runs in CI, never during seeding, authoring, enrichment or site
rendering. A test computes on one small specimen, such as $A_2$ (record `0012`); the full
certification computation runs only in CI.

A new certifiable computation gets a certificate name and a step in `latticedb certify`
before it stores its first value.
