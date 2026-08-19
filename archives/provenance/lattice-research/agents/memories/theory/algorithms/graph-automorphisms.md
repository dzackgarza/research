# Graph automorphisms with weighted nodes and edges

**Purpose:** Compute automorphism groups of graphs where nodes and/or edges have weights. Automorphisms must preserve weights.

**Key insight:** Weights = colors. Use color-preserving automorphisms.

---

## GAP: GRAPE package

**Documentation:** https://gap-packages.github.io/grape/

### Vertex-weighted graphs (vertex colors)

```gap
LoadPackage("grape");

# Construct graph
gamma := Graph(
    SymmetricGroup(5),
    [[1,2]],
    OnSets,
    function(x,y) return Intersection(x,y) = []; end
);

# Vertex weights as color classes
# Vertices with same weight → same color class
color_classes := [
    [1, 2, 3],   # Weight 1 vertices
    [4, 5],      # Weight 2 vertices
];

# Automorphism group preserving vertex weights
aut := AutomorphismGroup(gamma, color_classes);
# Returns: Permutation group preserving graph AND color classes

# Get generators
gens := GeneratorsOfGroup(aut);

# Group order
Size(aut);
```

### Edge-weighted graphs

**Method:** Encode edge weights as separate graphs, intersect automorphism groups.

```gap
LoadPackage("grape");

# Suppose weighted adjacency matrix:
# Weight 0 = no edge, Weight 1, 2, 3 = different edge types

# Create separate graph for each weight class
gamma1 := Graph(...);  # Edges with weight 1
gamma2 := Graph(...);  # Edges with weight 2
gamma3 := Graph(...);  # Edges with weight 3

# Compute automorphism group for each
aut1 := AutomorphismGroup(gamma1);
aut2 := AutomorphismGroup(gamma2);
aut3 := AutomorphismGroup(gamma3);

# Intersection = automorphisms preserving ALL weights
aut := Intersection(aut1, aut2, aut3);
```

### Vertex AND edge weighted graphs

```gap
LoadPackage("grape");

# Vertex weights
vertex_colors := [[1,2], [3,4,5]];  # Two weight classes

# Edge weights (via separate graphs)
gamma_w1 := Graph(...);  # Weight 1 edges
gamma_w2 := Graph(...);  # Weight 2 edges

# Automorphisms preserving vertex colors
aut_v := AutomorphismGroup(gamma_w1, vertex_colors);

# Further restrict to preserve edge weights
aut_e := AutomorphismGroup(gamma_w2);

# Intersection preserves everything
aut := Intersection(aut_v, aut_e);
```

### Self-loops as vertex weights

```gap
LoadPackage("grape");

# Directed graph with self-loops
gamma := Graph(
    SymmetricGroup(n),
    [[1,1], [2,3], ...],  # [1,1] = self-loop at vertex 1
    OnPairs,
    ...
);

# Self-loop at vertex i encodes weight w_i
# Automorphisms must preserve loops → preserve weights

aut := AutomorphismGroup(gamma);
```

### Permutation representations

```gap
# Action on vertices (default)
Action(aut, [1..n], OnPoints);

# Action on edges
edges := Edges(gamma);
Action(aut, edges, OnPairs);

# Action on color classes
Action(aut, color_classes, OnSets);

# Faithful permutation representation
phi := ActionHomomorphism(aut, [1..n], OnPoints);
Image(phi);
```

---

## GAP: Digraphs package (bliss algorithm)

**Documentation:** https://docs.gap-system.org/pkg/digraphs/doc/

### Directed graphs with loops

```gap
LoadPackage("digraphs");

# From adjacency list (loops allowed)
dig := Digraph([[1], [2, 3], [3], [1, 2, 3]]);
# Vertex 1 has loop, vertex 3 has loop, etc.

# Check for loops
HasLoops(dig);
Loops(dig);  # List of vertices with loops
```

### Vertex-colored automorphisms

```gap
# Vertex colors (integer list, one per vertex)
vertex_colors := [1, 1, 2, 2, 3];  # 5 vertices, 3 colors

# Automorphism group preserving vertex colors
aut := BlissAutomorphismGroup(dig, vertex_colors);

# Returns: Permutation group
```

### Edge-colored automorphisms

```gap
# Edge colors (integer list, one per edge)
# Edges ordered lexicographically by (source, target)

# For n-vertex digraph, edge (i,j) comes before (k,l) if i<k or (i=k and j<l)
edge_colors := [1, 2, 1, 2, 1, ...];  # One color per edge

# Automorphism group preserving edge colors
aut := BlissAutomorphismGroup(dig, [], edge_colors);
```

### Vertex AND edge colored

```gap
# Both vertex and edge colors
aut := BlissAutomorphismGroup(dig, vertex_colors, edge_colors);
```

### Self-loops as vertex weights (alternative)

```gap
# Assign self-loop with weight w_i to vertex i
# bliss preserves loops → preserves weights

dig := Digraph(adjacency_with_loops);
aut := BlissAutomorphismGroup(dig);
```

### Canonical labeling (isomorphism testing)

```gap
# Canonical form
canon := BlissCanonicalLabelling(dig);

# With colors
canon := BlissCanonicalLabelling(dig, vertex_colors, edge_colors);

# Two colored digraphs isomorphic iff same canonical labeling
```

---

## Encoding schemes

### Weights → Colors

| Weight type | Encoding |
|-------------|----------|
| Vertex weights | `vertex_colors[i] = weight of vertex i` |
| Edge weights | `edge_colors[e] = weight of edge e` |
| Self-loop weights | Loop at vertex i with color = weight |

### Continuous weights → Discrete colors

```gap
# If weights are real numbers, discretize
weights := [1.0, 1.2, 1.8, 2.1, 2.9];

# Bin into color classes
bins := [1.0..1.5, 1.5..2.0, 2.0..2.5, 2.5..3.0];
colors := List(weights, w -> FindBin(w, bins));
# colors := [1, 1, 2, 3, 4]
```

---

## Complete example: Weighted graph from adjacency matrix

```gap
LoadPackage("grape");

# Weighted adjacency matrix
W := [
    [0, 1, 2, 0],
    [1, 0, 1, 3],
    [2, 1, 0, 1],
    [0, 3, 1, 0]
];
n := 4;

# Vertex weights (diagonal, or separate array)
vertex_weights := [1, 1, 2, 2];

# Create color classes from vertex weights
color_classes := [];
for w in Set(vertex_weights) do
    Add(color_classes, Positions(vertex_weights, w));
od;
# color_classes = [[1,2], [3,4]]

# Create graphs for each edge weight
gamma_1 := NullGraph(SymmetricGroup(n), false);
gamma_2 := NullGraph(SymmetricGroup(n), false);
gamma_3 := NullGraph(SymmetricGroup(n), false);

for i in [1..n] do
    for j in [i+1..n] do
        if W[i][j] = 1 then AddEdge(gamma_1, [i,j]); fi;
        if W[i][j] = 2 then AddEdge(gamma_2, [i,j]); fi;
        if W[i][j] = 3 then AddEdge(gamma_3, [i,j]); fi;
    od;
od;

# Compute automorphism groups
aut_1 := AutomorphismGroup(gamma_1, color_classes);
aut_2 := AutomorphismGroup(gamma_2, color_classes);
aut_3 := AutomorphismGroup(gamma_3, color_classes);

# Intersection preserves all weights
aut := Intersection(aut_1, aut_2, aut_3);

Print("Automorphism group order: ", Size(aut), "\n");
Print("Generators: ", GeneratorsOfGroup(aut), "\n");
```

---

## Summary

| Feature | GRAPE | Digraphs (bliss) |
|---------|-------|------------------|
| Vertex weights (colors) | ✓ | ✓ |
| Edge weights (colors) | ✓ (via intersection) | ✓ |
| Self-loops | ✓ (directed) | ✓ |
| Loops as weights | ✓ | ✓ |
| Permutation rep | ✓ | ✓ |
| Canonical labeling | ✗ | ✓ |

**Recommended:** 
- **GRAPE** for undirected graphs, vertex-colored automorphisms
- **Digraphs/bliss** for directed graphs, edge-colored automorphisms, canonical labeling
