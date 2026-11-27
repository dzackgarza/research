# AGENTS.md — topological_spaces/tests

Tests in this subtree should use named set constructors such as
`Sets().Constructors().RealLine()` or `Sets().Constructors().OpenRealInterval(...)`
when the test object is a named set that refines into `TopologicalSpaces()`.
Use `TopologicalSpaces().Constructors()` only for constructors whose primary output is
a topological space rather than a named set.
