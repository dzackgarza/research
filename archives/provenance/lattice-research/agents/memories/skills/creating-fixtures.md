---
title: Creating Fixtures
status: active
date: 2026-05-29
---
# Creating Fixtures

Fixtures are mathematical oracles, not snapshots of current code behavior.

Use this skill before adding or changing files under `tests/fixtures/` or any other
durable fixture data used by tests.

## Load with this skill

- Load `test-guidelines` before touching tests or test fixtures.
- Read `mem:skills/research-source-acquisition` when adding a source, citation key,
  extracted literature path, theorem, lemma, table, or line reference.
- Read `mem:skills/research-proof-auditing` when fixture properties support proof,
  acceptance, or mathematical claim validation.
- Load `research-software-wiring` when fixture construction or verification should route
  through Sage, GAP, Singular, Macaulay2, Oscar/Julia, CARAT, PARI/GP, or another exact
  backend.

## Core policy

- A fixture describes a mathematical object and known mathematical properties of that
  object.
- A fixture property must be sourceable, recalculable, or explicitly marked as derived
  from sourceable data.
- A mathematician should be able to read the fixture, identify the object, trace the
  sources, and in principle recalculate every recorded property.
- Existing fixture files are examples of shape, not proof of correctness.
  Do not cargo-cult them.
- Do not encode implementation quirks, temporary outputs, or "what the current code
  returns" as expected fixture truth.

## Acceptable fixture objects

A fixture object may be:

- Extremely standard and uniquely identified by notation, such as `U`, `E_8`,
  `II_{1,8}`, `\mathbb{P}^n`, or a named root lattice.
- Defined by explicit mathematical data, such as a Gram matrix, equation, generators,
  relations, divisor basis, or construction expression.
- Cited from a primary source, table, theorem, lemma, database, or extracted literature
  note.

Opaque data is not enough.
If a fixture includes a raw matrix, polynomial, list of generators, or glue vectors,
also include the mathematical name, construction, source, and intended interpretation.

## Property requirements

Each property must be one of:

- Directly cited from a source.
- A standard property of a standard named object.
- Derived from cited data with a stated derivation.
- Verified by an exact backend with the backend, command, and trust boundary recorded.

Good properties include:

- `rank`, `signature`, `determinant`, `is_even`, `is_unimodular`.
- `discriminant_group`, `discriminant_form`, `nikulin_invariants`, `genus_symbol`.
- `construction`, `gram_matrix`, `root_system`, `basis`, `generators`, `relations`.
- Geometry properties such as Picard rank, canonical class, divisor basis, branch data,
  singularity type, and known cohomology dimensions when sourced.

Bad properties include:

- `verified: true` with no verification path.
- `expected_output` copied from current code.
- Values inferred from filenames, comments, or chat history.
- Large opaque arrays with no mathematical interpretation.
- Properties included because they are easy to assert rather than mathematically useful.

## Source records

Prefer source records that include:

- `bibliographic_key` matching `theory/references/references.bib`.
- `file` under `theory/references/literature/` when an extracted source exists.
- Theorem, lemma, proposition, table, page, section, or line reference when known.
- For external databases, the URL, authors/maintainers, completeness statement, and any
  documented limitations.

If a property needs a new source, update the reference system through
`mem:skills/research-source-acquisition` before treating the fixture as authoritative.

## Structure guidance

There is no mandatory schema.
Use the local file's existing shape unless a human asks for a migration.

One acceptable pattern is:

```json
{
  "id": "ii_1_8",
  "object_type": "lattice",
  "object_name": "II_{1,8}",
  "construction": "even unimodular lattice of signature (1, 8)",
  "sources": [
    {
      "bibliographic_key": "source-key",
      "file": "theory/references/literature/source.md",
      "theorem": "Theorem or table label"
    }
  ],
  "properties": {
    "rank": 9,
    "signature": [1, 8],
    "is_even": true,
    "is_unimodular": true
  },
  "derived_properties": {
    "determinant": {
      "value": -1,
      "derivation": "Unimodular lattice of signature (1, 8)"
    }
  }
}
```

Arrays of property assertions are also acceptable when they are more readable, for
example `{"property": "rank", "value": 9, "source": "..."}`. Choose readability and
mathematical auditability over schema cleverness.

## Test usage

Tests should use fixtures as independent mathematical oracles.

- The test should prove repo-owned behavior against fixture truth.
- The fixture should not merely test that JSON can be loaded.
- The fixture should not assert dependency behavior unless the repo adds semantic
  boundary logic.
- The test should fail if the implementation gives mathematically wrong output for the
  fixture object.

## Stop conditions

Stop and file source or research work when:

- A property cannot be traced to a source or recalculated from included data.
- The object is not uniquely identified.
- The only available evidence is current code output.
- The fixture would require a backend capability that has not been routed through
  `research-software-wiring`.
- The source is secondary, OCR-derived, or ambiguous and the property is mathematically
  important.
