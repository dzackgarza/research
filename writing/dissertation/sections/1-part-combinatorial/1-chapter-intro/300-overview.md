### Structure and Overview {#section-1-3}

The thesis is organized into three parts, establishing the foundations and proving the main isomorphism theorem:

- @sec:part-1 develops the combinatorial and lattice-theoretic foundations:

  - @sec:chapter-1 introduces the main theorem, historical context, and key concepts including KSBA stable pairs and $\ADEBC$ surfaces.

  - @sec:chapter-2 establishes lattice-theoretic foundations, particularly Nikulin's theory of 2-elementary lattices, with applications to the invariant lattices $\lkt$, $\len$, $\ten$, and $\tdp$.
    This includes the classification of primitive embeddings and the structure of discriminant groups.

  - @sec:chapter-3 develops the theory of Enriques surfaces and their K3 covers, analyzing the period domains $\fent$ and $\fttz$, and classifying the five 0-cusps of $\bd\bbcpt{\fent}$ through explicit lattice-theoretic computations.

- @sec:part-2 constructs the compactifications:

  - @sec:chapter-4 presents the theory of KSBA, Baily-Borel, toroidal, and semitoroidal compactifications.
    It establishes the framework for stable pairs and recognizable divisors that enables the comparison between algebraic and analytic compactifications.

  - @sec:chapter-5 develops integral affine geometry and the theory of Kulikov models.
    It describes how Type III degenerations correspond to integral affine spheres with singularities ($\IAS^2$), and how these yield divisorial log terminal (dlt) models through explicit algorithms involving Coxeter polytopes and monodromy invariants.

- @sec:part-3 proves the main theorem and provides explicit computations:

  - @sec:chapter-6 establishes the isomorphism $\ksbacpt{\fent} \cong \semitorcpt{\fent}$ through:

    1. Embedding $\fent$ into the moduli space $\fttz$ of $(2,2,0)$-polarized K3 surfaces as a Noether-Lefschetz locus

    2. Showing the normalized closure $\normalize{B}$ inherits a semitoroidal structure from $\ksbacpt{\fttz}$

    3. Constructing the universal family of Enriques pairs via quotient by the Enriques involution

    4. Proving the classifying map $\normalize{B} \to \ksbacpt{\fent}$ is finite using geometric constraints on double curves

    5. Applying Zariski's Main Theorem to conclude the isomorphism

  - @sec:chapter-7 provides computational examples, constructing explicit dlt models for degenerations at each of the five 0-cusps of $\bd\bbcpt{\fent}$.
    It demonstrates the folding procedure that relates K3 degenerations to Enriques degenerations through the action of commuting involutions on $\IAS^2$ structures.
