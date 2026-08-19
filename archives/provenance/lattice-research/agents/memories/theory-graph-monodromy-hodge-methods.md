# Graph Monodromy And Hodge Tool Methods

Trigger: implementing graph automorphism/subgraph-orbit specs, Coxeter diagram symmetry, monodromy of algebraic families, or reusable Hodge/Picard-Fuchs tooling.

Weighted graph automorphism store:

- Weights are colors. Encode vertex weights as vertex color classes or integer color arrays; encode edge weights either as separate graphs whose automorphism groups are intersected or as edge colors in GAP Digraphs/bliss.
- Use GAP GRAPE for undirected graphs and vertex-colored automorphisms. Stored calls: `LoadPackage("grape")`, `Graph(...)`, `AutomorphismGroup(gamma, color_classes)`, `GeneratorsOfGroup(aut)`, `Size(aut)`, `Action`, `ActionHomomorphism`.
- For edge-weighted undirected graphs in GRAPE, create one graph per edge weight and take `Intersection(aut_w1, aut_w2, ...)`.
- Use GAP Digraphs/bliss for directed graphs, edge colors, loops, and canonical labeling. Stored calls: `LoadPackage("digraphs")`, `Digraph(adj)`, `HasLoops`, `Loops`, `BlissAutomorphismGroup(dig, vertex_colors, edge_colors)`, `BlissCanonicalLabelling(dig, vertex_colors, edge_colors)`.
- Self-loops can encode vertex weights when the graph model makes that simpler, but colored vertices are clearer for spec/API work.
- Coxeter diagrams with root labels/edge multiplicities should use colored graph automorphism methods rather than plain unweighted graph automorphisms.

Subgraph orbit store:

- GRAPE owns clique/complete-subgraph enumeration: `CompleteSubgraphs(gamma)`, `CompleteSubgraphs(gamma,k)`, `CompleteSubgraphs(gamma,k,0)` for one representative per automorphism orbit, and `CompleteSubgraphs(gamma,k,2)` for reps plus orbit data.
- Weighted clique enumeration uses `CompleteSubgraphsOfGivenSize(gamma, k, alls, maxi, col, weights)`.
- Maximum clique methods: `MaximumClique(gamma)` and `CliqueNumber(gamma)`.
- Independent sets are cliques in `ComplementGraph(gamma)` or direct `IndependentSet(gamma)`.
- General k-vertex subgraph orbits: enumerate `Combinations(Vertices(gamma),k)` and compute `Orbits(aut, subsets, OnSets)`.
- Pairwise orbit membership: `RepresentativeAction(aut, S1, S2, OnSets)` returns a witnessing group element or `fail`.
- For quotient posets of subgraphs, elements are automorphism orbits of subgraphs; order `[H] <= [K]` iff some representative of `[H]` is contained in some representative of `[K]`. Use canonical labeling via Digraphs/bliss to avoid repeated isomorphism tests.

Monodromy store:

- For one-parameter families of curves `f(z,w,t)=0`, use Sage `RiemannSurface` chaining. The per-fiber call is `Curve(f_t).riemann_surface(prec=100)` or `RiemannSurface(f_zw, prec=prec)`.
- Use a loop in `QQ[i]`, e.g. `1 -> -i -> -1 -> i -> 1` scaled to avoid critical values. Between consecutive points, compute `S_k.symplectic_isomorphisms(S_{k+1})` and choose the matrix closest to identity as local parallel transport. Compose local matrices to get total monodromy.
- `symplectic_isomorphisms` relies on period matrices and LLL; use high precision such as `prec=100` or more for genus at least `2`.
- For surface/K3 families, use Picard-Fuchs ODE monodromy if the ODE is known. The stored tool is `ore_algebra.analytic.monodromy.monodromy_matrices(dop, base)`, but `ore_algebra` was not installed in the theory note and requires a Cython build.
- Computing Picard-Fuchs ODEs is the hard step; route through Macaulay2 `PeriodIntegrals`, Singular deformation/Gauss-Manin tools, or literature tabulation. Do not pretend Sage alone computes K3 Picard-Fuchs equations.
- Stored examples: Legendre family monodromy around `t=0`/`t=1` gives unipotent generators such as `[[1,0],[-2,1]]` and `[[1,2],[0,1]]` depending on basis/orientation; cuspidal family `y^2=x^3-t` has unipotent monodromy with `N^2=0`.

Foliation/Hodge tool store:

- `foliation.lib` is valuable for explicit computational Hodge theory, not for trivial helpers. Do not extract/reimplement `Monomials`, `RandomPoly`, `GoodMinor`, `InsertNew`, or similar small utilities.
- Reusable high-value procedure names: `HodgeNumber`, `MixedHodgeFermat`, `PeriodMatrix`, `IntersectionMatrix`, `Matrixpij`, `DimHodgeCycles`, `BasisHodgeCycles`, `TranCoho`, `LinearCoho`, `PeriodLinearCycle`, `ListPeriodLinearCycle`, `SumTwoLinearCycle`, `SumThreeLinearCycle`, `mTwoLinearCycle`, `mLinearCycle`.
- Noether-Lefschetz/explicit-cycle procedure names: `CodComInt`, `CodComIntZar`, `CodRuledCubic`, `CodQuarticScroll`, `CodVeronese`, `TwoCI`.
- IVHS/Hodge-locus procedure names: `HodgeLocusIdeal`, `SmoothReduced`, `EquHodge`, `InterTang`, `DeformSpace`, `ConstantRank`, `DistinctHodgeLocus`.
- Gauss-Manin/Picard-Fuchs procedure names: `gaussmanin`, `gaussmaninvf`, `gaussmaninmatrix`, `PFequ`, `PFeq`, `sysdif`, `dbeta`.

Source anchors: `theory/algorithms/graph-automorphisms`, `theory/algorithms/subgraph-orbits`, `theory/algorithms/monodromy-computations`, `theory/backends/foliation-lib-reusable-procedures`.

Verification: future graph/monodromy/Hodge work should name the exact stored function family above and state whether the output is a group, orbit representatives, canonical labels, monodromy matrix, period data, Hodge locus ideal, or Picard-Fuchs differential equation.
