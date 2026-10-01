---
title: Records
summary: What a record states, which values the build computes, and which values a person declares.
order: 1
---

## Records {#records}

Each lattice of the catalogue has a permanent tag and one record, the file `lattices/<TAG>.md`. Its front matter states the [Gram tensor](lattices.html#gram-tensor) in the basis of the record and the invariants; the [fields page](../fields.html) gives the schema.
Its Markdown body holds the notes: the construction of the lattice, the source of each declared value, and the proofs that the build does not check.

## Computed values {#computed}

The build computes each invariant on the page of a lattice from the Gram tensor, and it rejects a record that states another value.

## Declared values {#declared}

A value marked *declared* is one that a person declared, and the notes give its source.
The build does not compute it.

## Values that are not decided {#not-decided}

A record that does not state a value leaves it *not decided*. The page of the lattice says so; it does not say that the property fails.
