# Posets Subtree

This subtree specifies order-theoretic categories promoted out of `sets/`.
Here, a lattice is a poset in which every pair of elements has a meet and a join.
It is unrelated to module lattices or quadratic-form lattices.

HomCategory, EndCategory, and AutCategory refinements live in `homsets.py`. Their
elements are order-preserving maps, poset endomorphisms, and poset automorphisms; the
generic aut-category construction is inherited from the root `homsets/` subtree.
