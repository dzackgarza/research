---
title: Records
summary: Source files, computed values, declared values, and values that are not decided.
order: 1
---

## Records {#records}

Each lattice of the catalogue has a permanent tag and a source file `lattices/<TAG>.md`. Its YAML front matter stores the [Gram tensor](lattices.html#gram-tensor) in the chosen basis and the invariants, in the [fields](../fields.html) of the schema.
Its Markdown body holds the notes: the construction of the lattice, the source of each declared value, and the proofs of the statements that are not computed.

## Computed values {#computed}

Each invariant on the page of a lattice is computed from the Gram tensor with exact arithmetic, except a declared value.
The genus symbol is computed with `Genus` of SageMath, and the order of the isometry group with `qfauto` of PARI/GP.

## Declared values {#declared}

::: {.definition}
A value marked *declared* is not computed; the notes cite its source.
:::

## Values that are not decided {#not-decided}

::: {.definition}
A value that the source file does not state is *not decided*, and the page of the lattice shows it so.
:::

Not decided does not mean that the property fails.
