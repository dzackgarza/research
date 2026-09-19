## Lattice Theory {#sec:chapter-2}

Compactifications of $\fent$, and more generally moduli spaces of K3 surfaces, rely on the arithmetic and combinatorial structure of even indefinite (and often hyperbolic) lattices.
This chapter discusses the lattice-theoretic techniques used in such problems, emphasizing both theoretical results and explicit computational techniques.

Of particular importance is the structure theory of *2-elementary* lattices: even integral lattices whose discriminant group is an $\FF_2$-module.
In the context of $\fent$, the sublattice $\ten$ associated to the Enriques involution $\ien$ on a K3 cover $X$ is 2-elementary of signature $(2,10)$.
The invariants $(r, a, \delta)$, recording the rank, length of the discriminant group, and *coparity*, completely determine the isometry classes of such lattices, as well as their embedding properties.
The results of @Nik79 yield existence and uniqueness of the relevant period domains $\halfpd{\ten}$, their arithmetic quotients $\fent$, and the structure of boundary strata in various compactifications.

A major theme is the connection between the geometry of the period domain and the arithmetic of $\ten$: the construction of $\fent$ relies on an arithmetic subgroup $\gent$, and the $\gent$-orbits of primitive isotropic vectors $\eta$ and primitive isotropic planes $I$ in $\ten$ index the rational boundary components of the Baily-Borel compactification $\bbcpt{\fent}$, called *cusps*. It has has $0$-cusps and $1$-cusps indexed by such $\eta$ and $I$ respectively.
This chapter details the lattice-theoretic methods classically used to find the five $0$-cusps of $\fent$.
We begin with definitions and standard constructions:

- Properties of even lattices, dual lattices, discriminant groups, and genus;

- The hyperbolic plane $U$, indefinite root lattices $A_n, D_n, E_8$ and their twists, and particularly their duals and discriminant groups;

- Criteria for primitively embedding one lattice into another, including Nikulin’s theorems on extensions, embeddings, and overlattices, as well as his classification of 2-elementary lattices.

Special focus is given Nikulin's work: explicit determination of invariants, criteria for primitive embeddings into even unimodular lattices such as $\lkt$ and $\len$, and explicit discriminant group techniques that can be used to reduce the aforementioned orbit problems to the study of finitary, computable objects.
In later chapters, we will see how the the explicit classification of isotropic sublattices of $\ten$ determines the structure of $\bd\bbcpt{\fent}$ and consequently that of semitoroidal compactifications $\semitorcpt{\fent}$, and by the main theorem, provide an inroad into studying the boundary $\bd\cpt{\fent}$ of the KSBA compactification.
