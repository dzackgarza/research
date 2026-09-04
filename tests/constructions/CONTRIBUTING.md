# The construction tests

This subtree records what a mathematician expects to be able to build in a
session, and what they expect to be able to ask of it.  The preamble is
measured against these expectations.  The expectations are not measured
against the preamble.

## What a test here is

A test here is one expectation, written the way it would be typed into a
notebook by someone who knows the mathematics and has never read the
preamble's source:

```python
def test_the_group_algebra_of_the_symmetric_group(build, name) -> None:
    algebra = GroupAlgebra(build(name), Groups.S(3))
    assert algebra.rank() == 6
    assert algebra.center().rank() == 3
```

The claim is a known truth: a textbook value, a standard identity, or a
relation between two constructions that holds over every ring.  The spelling
is the natural one.  Whether the preamble has a name for the construction,
accepts the input, or returns the right answer is exactly what the test
finds out.

## The rules

**Write from the mathematics, never from the implementation.**  Do not read
the preamble's source to learn what it accepts, what it refuses, or how it
spells things.  The exported names and the generated megadoc
(`docs/preamble-megadoc.md`) are the vocabulary a session offers, and they
may be consulted the way a user consults documentation.  When the natural
spelling of a construction is absent from that vocabulary, write the natural
spelling anyway.  The star import of `dzack_research.preamble.all` lets an
undefined name fail inside its own test, and that failure is the finding: the
universe lacks a word.

**Use the notebook spelling.**  Integer literals are integers.  `QQ[G]` is a
group algebra, `M / N` is a quotient, `Hom(M, N)` is a Hom module,
`K.class_group()` is the class group.  Do not wrap, cast, or translate an
input into a form the implementation happens to want.  A test that has to
say `ring(ZZ(2))` to be accepted has recorded a defect in the ring, not in
the test.

**Red is the deliverable.**  A failing test is a dead end a working
mathematician would hit.  Do not run the tests while writing them in order
to shape them; that couples the expectation to the implementation and
defeats the subtree.  Never weaken, skip, mark expected-failure, or delete a
test because it fails.  Never add a fallback to make a line pass: no `or`
between two spellings, no `hasattr`, no branch on what the object turned
out to be.  A test goes green when, and only when, the preamble meets the
expectation.

**One expectation per red line.**  Bundle related claims about one object
in one test, but split off anything whose failure would hide the rest.  A
red row must name one construction or one operation, so the person reading
the failure knows the single thing that is missing.

**Prefer relations to tables.**  `coker(R \xrightarrow{2} R) \cong R/2R`
is one line that is true over every commutative ring; a table of
cardinalities per ring is many lines that are each true once.  Use a table
when the value is a fact about one object (the order of $O(E_8)$, the class
number of $\mathbb Q(\sqrt{-23})$), and a relation when the value is a
consequence of the definition.

**Range over the catalogue.**  `tests/conftest.py` holds the named specimen
families: fields, discrete valuation rings, principal ideal domains,
Dedekind domains, Noetherian domains, non-domains, noncommutative rings, and
the local, complete, Artinian, finite, number-field and maximal-order
families that cut across them.  A test asks for a family by its fixture name
(`pid`, `field`, `local_ring`, ...) and runs once per member.  A
construction expected over every principal ideal domain is written once.
Members are added to a family because the mathematics puts them there,
never because the implementation handles them; a member that fails to build
is a finding, not a row to drop.

## What does not belong here

- A test of how the preamble does something.  Internals, class names,
  storage, backends and helper functions are not expectations.
- A test derived from current behaviour.  If the only reason a line asserts
  a value is that the implementation returns it, the line is not a
  mathematical claim.
- A test that compares the preamble against Sage.  The oracle is the
  mathematics; Sage is an engine the preamble may use.
- A skipped or expected-failure test.  The suite's colour is the report.

## Growing the subtree

Add a test the moment you find yourself expecting something of a session
that no test asks for.  Add a family fixture when a class of rings appears
in several expectations.  Adding a name or a capability to the preamble
never requires touching a test; a test that turns green stays exactly as it
was, because it is now a proof that the expectation is met.

The sibling subtree `tests/user_simulations/` follows the same rules in a
different form: each test there is one long research session, parameterized
over natural inputs, where most of the proof is that the session runs to
the end.  Both subtrees share the catalogue in `tests/conftest.py`.
