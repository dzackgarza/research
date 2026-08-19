# Subgraph enumeration and orbits under Aut(G)

**Purpose:** Enumerate subgraphs of a graph G, compute orbits under Aut(G), obtain quotient of subgraph poset by automorphism action.

---

## GAP: GRAPE package

**Documentation:** https://gap-packages.github.io/grape/

### Complete subgraphs (cliques)

```gap
LoadPackage("grape");

# Construct graph
gamma := JohnsonGraph(5, 2);

# All maximal complete subgraphs
cliques := CompleteSubgraphs(gamma);
# Returns: List of vertex sets, e.g., [[1,2,3,4], [1,2,5]]

# Complete subgraphs of size k
cliques_k := CompleteSubgraphs(gamma, k);
# Returns: All complete subgraphs with exactly k vertices

# Complete subgraphs of size k, with orbit control
# alls = 0: one representative per orbit
# alls = 1: all subgraphs
# alls = 2: orbit representatives + orbit info
cliques_orbits := CompleteSubgraphs(gamma, k, 0);
# Returns: One representative per Aut(gamma)-orbit

cliques_orbits := CompleteSubgraphs(gamma, k, 2);
# Returns: Record with orbit representatives and orbit data
```

### Complete subgraphs with vertex weights

```gap
# Vertex weights (for weighted subgraph enumeration)
weights := [1, 1, 2, 2, 3];  # One weight per vertex

# Complete subgraphs where sum of weights = k
cliques_weighted := CompleteSubgraphsOfGivenSize(gamma, k, alls, maxi, col, weights);
# alls: orbit control (0/1/2)
# maxi: true = only maximal subgraphs
# col: use vertex coloring optimization (default true)
# weights: vertex weights list
```

### Maximum clique

```gap
# Find maximum clique (largest complete subgraph)
max_clique := MaximumClique(gamma);
# Returns: Vertex set of maximum clique

# Clique number (size of largest clique)
omega := CliqueNumber(gamma);
# Returns: Integer
```

### Independent sets (complement of cliques)

```gap
# Independent set (no two vertices adjacent)
indset := IndependentSet(gamma);

# Independent set containing specific vertices
indset := IndependentSet(gamma, required_vertices);

# Independent sets = cliques in complement graph
gamma_complement := ComplementGraph(gamma);
indep_cliques := CompleteSubgraphs(gamma_complement);
```

---

## General subgraph orbits

### Method 1: Induced subgraphs + Orbits

```gap
LoadPackage("grape");

# Graph with automorphism group
gamma := Graph(...);
aut := AutomorphismGroup(gamma);

# Enumerate all k-vertex subsets
k := 4;
subsets := Combinations(Vertices(gamma), k);

# Compute induced subgraphs
induced_subgraphs := List(subsets, S -> InducedSubgraph(gamma, S));

# Compute orbits under Aut(gamma)
# Use canonical labeling for isomorphism testing
orbits := Orbits(aut, subsets, OnSets);

# Orbit representatives
reps := List(orbits, o -> o[1]);

# Corresponding induced subgraphs
rep_subgraphs := List(reps, S -> InducedSubgraph(gamma, S));
```

### Method 2: RepresentativeAction for isomorphism testing

```gap
# Test if two subgraphs are in same orbit
S1 := [1, 2, 3, 4];
S2 := [2, 3, 5, 6];

# Find g in aut mapping S1 to S2
g := RepresentativeAction(aut, S1, S2, OnSets);

if g <> fail then
    Print("S1 and S2 are in same orbit\n");
else
    Print("S1 and S2 are in different orbits\n");
fi;
```

### Method 3: OrbitsDomain for closed domains

```gap
# If you have a closed set of subgraphs (e.g., all k-cliques)
cliques := CompleteSubgraphs(gamma, k, 1);  # All k-cliques

# Orbits under automorphism group
clique_orbits := Orbits(aut, cliques, OnSets);

# Number of orbits
Length(clique_orbits);

# Representatives
clique_reps := List(clique_orbits, o -> o[1]);
```

---

## Quotient of subgraph poset by Aut(G)

The quotient poset has:
- **Elements:** Aut(G)-orbits of subgraphs
- **Order:** [H] ≤ [K] iff ∃ H' ∈ [H], K' ∈ [K] with H' ⊆ K'

### Computing the quotient poset

```gap
LoadPackage("grape");

gamma := Graph(...);
aut := AutomorphismGroup(gamma);
n := OrderGraph(gamma);

# Step 1: Enumerate subgraphs by size
all_subgraph_orbits := [];
for k in [1..n] do
    subsets := Combinations(Vertices(gamma), k);
    orbits := Orbits(aut, subsets, OnSets);
    reps := List(orbits, o -> o[1]);
    Add(all_subgraph_orbits, reps);
od;

# Step 2: Compute quotient poset relations
# [H] ≤ [K] iff H is subgraph of some K' in orbit [K]
quotient_relations := [];
for i in [1..Length(all_subgraph_orbits)] do
    for j in [i+1..Length(all_subgraph_orbits)] do
        for H_rep in all_subgraph_orbits[i] do
            for K_rep in all_subgraph_orbits[j] do
                # Check if H_rep is subgraph of some K' in orbit of K_rep
                for g in aut do
                    K_image := OnSets(K_rep, g);
                    if IsSubset(K_image, H_rep) then
                        Add(quotient_relations, [i, j]);
                        break;
                    fi;
                od;
            od;
        od;
    od;
od;
```

### Efficient quotient computation (using canonical labeling)

```gap
LoadPackage("digraphs");

# For each subgraph, compute canonical form
canonical_reps := [];
for k in [1..n] do
    subsets := Combinations(Vertices(gamma), k);
    orbits := Orbits(aut, subsets, OnSets);
    
    for orbit in orbits do
        rep := orbit[1];
        subgraph := InducedSubgraph(gamma, rep);
        
        # Convert to digraph for bliss canonical labeling
        adj := AdjacencyMatrix(subgraph);
        dig := Digraph(adj);
        
        # Canonical labeling
        canon := BlissCanonicalLabelling(dig);
        
        Add(canonical_reps, [k, canon, orbit]);
    od;
od;

# Subgraphs with same canonical form are in same orbit
# Quotient poset elements = unique canonical forms
```

---

## Weighted subgraph enumeration

### Vertex-weighted subgraphs

```gap
# Assign weights to vertices
weights := [1, 2, 1, 3, 2, ...];

# Find subgraphs with total weight = W
target_weight := 10;

# Enumerate subsets with correct weight sum
valid_subsets := Filtered(
    Combinations([1..n], k),
    S -> Sum(List(S, i -> weights[i])) = target_weight
);

# Compute orbits
orbits := Orbits(aut, valid_subsets, OnSets);
```

### Edge-weighted subgraphs

```gap
# Encode edge weights as separate graphs
gamma_w1 := Graph(...);  # Weight 1 edges
gamma_w2 := Graph(...);  # Weight 2 edges

# Find subgraphs preserving edge weight structure
# (subgraph must have same weight pattern)
```

---

## Complete example: Orbit enumeration of 4-vertex subgraphs

```gap
LoadPackage("grape");

# Petersen graph
gamma := PetersenGraph();
aut := AutomorphismGroup(gamma);
verts := Vertices(gamma);

# Enumerate all 4-vertex induced subgraphs
k := 4;
subsets := Combinations(verts, k);
Print("Total ", Length(subsets), " subsets of size ", k, "\n");

# Compute orbits under Aut(gamma)
orbits := Orbits(aut, subsets, OnSets);
Print("Number of orbits: ", Length(orbits), "\n");

# Orbit representatives
reps := List(orbits, o -> o[1]);

# Display orbit sizes
for i in [1..Length(orbits)] do
    Print("Orbit ", i, ": size ", Length(orbits[i]), 
          ", representative: ", reps[i], "\n");
od;

# Compute induced subgraph for each representative
rep_subgraphs := List(reps, S -> InducedSubgraph(gamma, S));

# Classify by isomorphism type (using canonical forms)
LoadPackage("digraphs");
canonical_forms := [];
for subgraph in rep_subgraphs do
    adj := AdjacencyMatrix(subgraph);
    dig := Digraph(adj);
    canon := BlissCanonicalLabelling(dig);
    Add(canonical_forms, canon);
od;

# Subgraphs with same canonical form are isomorphic
iso_types := Set(canonical_forms);
Print("Number of isomorphism types: ", Length(iso_types), "\n");
```

---

## Summary

| Task | GAP function |
|------|--------------|
| Maximal cliques | `CompleteSubgraphs(gamma)` |
| k-cliques | `CompleteSubgraphs(gamma, k)` |
| k-clique orbit reps | `CompleteSubgraphs(gamma, k, 0)` |
| Maximum clique | `MaximumClique(gamma)` |
| Clique number | `CliqueNumber(gamma)` |
| Independent sets | `IndependentSet(gamma)` |
| Induced subgraph | `InducedSubgraph(gamma, V)` |
| Subgraph orbits | `Orbits(aut, subsets, OnSets)` |
| Orbit representative | `Representative(orbit)` |
| Isomorphism test | `RepresentativeAction(aut, S1, S2, OnSets)` |
| Canonical labeling | `BlissCanonicalLabelling(dig)` |

**Recommended workflow:**
1. Use `CompleteSubgraphs` for cliques with orbit control
2. Use `Orbits(aut, subsets, OnSets)` for general subgraph orbits
3. Use `BlissCanonicalLabelling` for isomorphism classification
4. Quotient poset = orbit representatives with inclusion relations
