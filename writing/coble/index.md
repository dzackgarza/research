# Coble surfaces

A Coble surface is a smooth projective rational surface $S$ with $\lvert -K_S \rvert = \emptyset$ but $\lvert -2K_S \rvert \neq \emptyset$.
This part is the moduli theory of such surfaces: the construction of $F_{\mathrm{Co}}$, its Baily--Borel and semitoroidal compactifications, the correspondence between its cusps and those of the Enriques moduli spaces, and the KSBA stable limits.

It is one vault rather than a paper and a set of notes kept apart.
Each page is one topic, and the mathematics that is written up sits beside the computational results and the open questions that produced it.

## How the part is ordered

The parts below run in one direction: geometry, then the lattices that encode it, then the moduli space, then its boundary, and finally what the boundary is made of.

**Surfaces and their K3 covers** fixes the three surface classes and the K3 double cover through which every later lattice statement is made.

**Lattice theory** is the general machinery --- root systems, discriminant forms and the genus, embeddings and overlattices, invariant and coinvariant sublattices --- stated for an arbitrary lattice and complete before any particular one is named.
**The Coble lattice** then applies it to this project's own lattice: the orbits of its discriminant form, the Heegner line and the arithmetic group cut out along it, and the criterion for lifting an automorphism through a gluing.

**Moduli spaces and period domains** builds $F_{\mathrm{Co}}$ from that arithmetic, by GIT, through the Horikawa model, and as a quotient of a type IV domain.

**Reflection groups and compactifications** supplies the boundary machinery: Vinberg's algorithm, the classification of Coxeter systems, hyperbolic Coxeter polytopes, and the toroidal and semitoroidal compactifications built from them.
**Degenerations**, **the cusp correspondence** and **stable limits** are the boundary itself, read geometrically, combinatorially and in the KSBA sense.
**Results for $F_{\mathrm{En},2}$** states what all of it proves.

**Computational methods** are reusable --- a toolchain, a table of which lattice algorithm applies in which signature, the fundamental chamber as a polyhedral cone, isotropic orbits and the Tits building, and periods and local monodromy.
**Computed results** are what those methods produced for this project: CoxIter certificates, root vectors and folded Sterk diagrams, chamber counts, integral-affine data, isotropic candidates.

**Open problems and research programs** is everything still conjectural, kept together so the boundary between what is proved here and what is not is visible in the structure rather than only in the prose.

It closes with the **Heegner report**, a standalone survey of the whole program with its own bibliography and status ledger.

**Reference** holds the formula sheets, the diagram conventions and the extracted references.

Sources and reference material sit beside the vault rather than in it: `papers/` holds the extracted third-party papers, and `reference/` the source PDFs and the last built version of the paper, from 24 July 2026.
