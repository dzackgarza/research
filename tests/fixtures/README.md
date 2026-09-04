# Cited mathematical facts

`DEV-41` says verified mathematical facts are **data, not test code**: they live
here, organised by mathematical topic, each carrying its value, its citation and
its verification status, and importing nothing from the code under test. The
consuming test is a thin parametrised driver containing no literal expected
values.

## Why the separation

An expectation written inline beside the object it checks has no source. When
the object and the expectation were transcribed in the same sitting -- a Gram
matrix and its signature, a block recipe and its invariants -- the assertion
compares one transcription against another and cannot detect the error it was
copied from. Moving the expectation here forces the question *where did this
number come from* to have an answer, and makes the answer greppable.

## Schema

Each fact is a row carrying:

| field | meaning |
| --- | --- |
| `value` | the fact itself, as plain Python data |
| `citation` | a key that resolves in `~/.pandoc/bib/references.bib` |
| `locator` | where in the source: a figure, table, theorem or page |
| `verified` | whether a human has checked this row **against the source** |

`verified` is the honest part. A row copied out of the implementation and given
a citation is `verified = False` until someone reads the paper: the citation
says where the fact is supposed to come from, and the flag says whether anyone
has confirmed it does. `just test-fixtures` reports both the rows whose citation
does not resolve and the rows that remain unverified, so neither state is
silent.

## Rules

- A fixture module imports **nothing** from `dzack_research`. It holds data.
- A citation key must resolve in the bibliography; `just test-fixtures` checks.
- A new fact arrives with its citation, or it does not arrive.
- Values are never harvested by running the implementation and recording what it
  printed. That is not an oracle.
