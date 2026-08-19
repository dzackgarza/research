# COMPREHENSIVE TOOL DOCUMENTATION

This file documents external software tools used in the Coble project, sourced from
official documentation URLs.

* * *

## Oscar.jl: Integer Lattices

**Source:**
https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/integer_lattices/

### Constructors

```julia
using Oscar

# From Gram matrix
L = integer_lattice(gram = matrix(ZZ, [2 -1; -1 2]))

# From basis matrix
B = matrix(ZZ, [1 0; 0 1])
L = integer_lattice(B)

# Root lattices
L = root_lattice(:A, n)
L = root_lattice(:D, n)
L = root_lattice(:E, 8)

# Leech lattice
L = leech_lattice()

# Niemeier lattice
N = maximal_even_lattice(R)
L, v, h = leech_lattice(N)

# K3 lattice
L = k3_lattice() # Signature (3, 0, 19)

# Mukai lattice
L = mukai_lattice(:K3)
L = mukai_lattice(:Ab)
L = mukai_lattice(; extended = true)

# Hyperkaehler lattices
L = hyperkaehler_lattice(:K3; n = 2)
L = hyperkaehler_lattice(:Kum; n = 2)
L = hyperkaehler_lattice(:OG6)
L = hyperkaehler_lattice(:OG10)
```

### Attributes

```julia
# Basis and Gram matrix
B = basis_matrix(L)
G = gram_matrix(L)

# Ambient space
V = ambient_space(L)

# Rational span
V_rat = rational_span(L)
```

### Invariants

```julia
# Basic invariants
r = rank(L)
d = det(L)
s = scale(L)
l = level(L)
n = norm(L)

# Tests
is_even(L)
is_integral(L)
is_primary(L, p)
is_primary_with_prime(L) # Returns (Bool, p)
is_elementary(L, p)
is_elementary_with_prime(L) # Returns (Bool, p)

# Genus
G = genus(L)
m = mass(L)
reps = genus_representatives(L)
```

### Rescaling

```julia
# Rescale quadratic form
L_rescaled = rescale(L, r) # r rational number
```

* * *

## Oscar.jl: Lattices with Isometry

**Source:**
https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/latwithisom/

### Constructors

```julia
using Oscar

# From lattice and isometry matrix
Lf = integer_lattice_with_isometry(L, f)

# Check if f is isometry (default: check=true)
Lf = integer_lattice_with_isometry(L, f; check = true)

# Ambient representation (default: true)
Lf = integer_lattice_with_isometry(L, f; ambient_representation = true)

# Identity isometry
Lf = integer_lattice_with_isometry(L)

# Negative identity isometry
Lf = integer_lattice_with_isometry(L; neg = true)

# From quadratic space with isometry
Vf = quadratic_space_with_isometry(V, f)
Lf = lattice(Vf)

# From quadratic space with isometry and basis matrix
B = matrix(QQ, [...])
Lf = lattice(Vf, B)

# Lattice in same ambient space
I = lattice_in_same_ambient_space(Lf, B)
```

### Attributes

```julia
# Basic lattice attributes (all work on Lf)
basis_matrix(Lf)
gram_matrix(Lf)
rank(Lf)
det(Lf)
degree(Lf)
discriminant(Lf)
genus(Lf)

# Isometry attributes
isometry(Lf) # The isometry f
order_of_isometry(Lf) # Order of f
ambient_isometry(Lf) # Isometry of ambient space

# Polynomials
characteristic_polynomial(Lf)
minimal_polynomial(Lf)

# Tests
is_definite(Lf)
is_even(Lf)
is_integral(Lf)
is_primary(Lf, p)
is_primary_with_prime(Lf)
is_elementary(Lf, p)
is_elementary_with_prime(Lf)
is_unimodular(Lf)
```

### Invariant and Coinvariant Lattices

```julia
# Invariant lattice L^f (fixed sublattice)
Lf_inv = invariant_lattice(Lf)

# Coinvariant lattice (orthogonal complement of invariant lattice)
Lf_coinv = coinvariant_lattice(Lf)

# Both at once
Lf_inv, Lf_coinv = invariant_coinvariant_pair(Lf)
```

### Operations

```julia
# Power of isometry
Lf_pow = Lf^n

# Direct sum
Lf_sum, emb, proj = direct_sum(Lf1, Lf2)

# Dual lattice with induced isometry
Lf_dual = dual(Lf)

# Rescale
Lf_rescaled = rescale(Lf, r)

# LLL reduction
Lf_lll = lll(Lf)
```

### Type and Classification

```julia
# Type of lattice with isometry
type_info = type(Lf)

# Check if of specific type
is_of_type(Lf, t)
is_of_same_type(Lf1, Lf2)

# Hermitian type
is_of_hermitian_type(Lf)
is_hermitian(t)

# Hermitian structure
H = hermitian_structure(Lf)
```

### Discriminant Group with Isometry

```julia
# Discriminant group and induced isometry
DL, Df = discriminant_group(Lf)

# As TorQuadModuleWithIsom
Df_iso = discriminant_group(TorQuadModuleWithIsom, Lf)

# Image of centralizer in O(D_L)
G, phi = image_centralizer_in_Oq(Lf)

# Discriminant representation
pi = discriminant_representation(L, G)
```

### Signatures

```julia
# Signatures of eigenspaces
sigs = signatures(Lf)
# Returns Dict with signatures for each eigenvalue
```

### Spinor Norm

```julia
# Rational spinor norm
sp = rational_spinor_norm(Lf)

# With respect to b*Phi
sp = rational_spinor_norm(Lf; b = b)
```

* * *

## Oscar.jl: Primitive Embeddings

**Source:** https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/primembed/

### Primitive Embeddings

```julia
using Oscar

# Embed M primitively into L (L must be unique in its genus)
exists, embeddings = primitive_embeddings(L, M)

# Returns: [(L', M', N')] where:
# - L' ≅ L
# - M' ⊂ L' with M' ≅ M (primitive embedding)
# - N' = M'^⊥ in L'

# With classification control
exists, embeddings = primitive_embeddings(L, M; classification = :sub)
# :none - just test existence
# :first - return one embedding
# :sub - classify up to O(M) and O(q)
# :emb - classify up to O(q) only

# From genus instead of lattice
exists, embeddings = primitive_embeddings(G, M)
# G is genus, M embeds into some L ∈ G

# From discriminant form + signature
exists, embeddings = primitive_embeddings(q, sign, M)
# q = discriminant form
# sign = (n₊, n₋) signature tuple
```

### Primitive Extensions

```julia
# Find primitive extensions M ⊕ N ⊂ L
exists, extensions = primitive_extensions(M, N)

# Returns: [(L, M', N')] where M' ≅ M, N' ≅ N, M' ⊕ N' ⊂ L primitive

# With constraints
exists, extensions = primitive_extensions(M, N;
 glue_order = [2, 4], # [L : M⊕N]
 form_over = [target_q], # desired D(L)
 even = true, # force even lattices
 classification = :subsub) # up to O(M)×O(N)

# Classification levels:
# :subsub - up to O(M) × O(N)
# :subemb - up to O(M) only
# :embsub - up to O(N) only
# :embemb - no quotient (finest)
```

### Equivariant Primitive Extensions

```julia
# With isometries on M and N
Mf = integer_lattice_with_isometry(M, fM)
Nf = integer_lattice_with_isometry(N, fN)

exists, extensions = equivariant_primitive_extensions(Mf, Nf)
# Returns: [(Lf, Mf', Nf')] where f_L preserves M' and N'

# With options
exists, extensions = equivariant_primitive_extensions(Mf, Nf;
 glue_order = [2],
 form_over = [target_q],
 even = true,
 classification = :subsub,
 compute_bar_Gf = true, # compute image of O(L,f) → O(D_L,D_f)
 first_fitting_isometry = false) # extend conjugacy class reps
```

### Admissible Equivariant Extensions

```julia
# For p-admissible triples ((A,f_A), (B,f_B), (C,f_C))
# Returns reps of double coset G_B \ S / G_A
extensions = admissible_equivariant_primitive_extensions(Af, Bf, Cf, p, q)
# p, q are primes (default q = p)
# Requires: type(D, f_D^q) = type(C, f_C)
```

* * *

## Oscar.jl: Discriminant Groups

**Source:**
https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/discriminant_group/

### Discriminant Group

```julia
using Oscar

# Discriminant group D(L) = Lˇ/L
D = discriminant_group(L)

# With modulus
D = discriminant_group(L, n)

# Bilinear form
b = bilinear_form(D)

# Quadratic form
q = quadratic_form(D)
```

* * *

## Oscar.jl: Genera of Integer Lattices

**Source:** https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/Zgenera/

### Genus

```julia
using Oscar

# Genus of lattice
G = genus(L)

# Local genus symbol at prime p
S = local_symbol(G, p)

# Canonical symbol
symbol = canonical_symbol(G)

# Representatives
reps = representatives(G)

# Class number
h = class_number(G)

# Mass
m = mass(G)
```

* * *

## Singular: brnoeth.lib (Hamburger-Noether, Brill-Noether)

**Source:** https://www.singular.uni-kl.de/Manual/4-3-0/sing_2254.htm

### Adjunction Divisor and Genus

```singular
LIB "brnoeth.lib";

// Compute adjunction divisor and genus
// f must be polynomial in 2 variables
list C = Adj_div(f);

// Example: genus computation
ring r = 0, (x,y), lp;
list C = Adj_div(x3*y + y3 + x);
// Output: "The genus of the curve is 3"
```

### Non-Singular Places

```singular
// Find non-singular places up to degree n
// C is output from Adj_div
C = NSplaces(n, C);

// Places of degree 1 to m
C = NSplaces(1..m, C);

// Example
list C = Adj_div(x3y+y3+x);
C = NSplaces(1..4, C); // Places of degree 1,2,3,4
```

### Brill-Noether (Riemann-Roch Spaces)

```singular
// Compute Riemann-Roch space L(D)
// G = intvec of divisor multiplicities at places in C
// C = output from NSplaces
list LG = BrillNoether(G, C);

// Example
intvec G = 0, 0, 0, 0; // Divisor with mult 0 at first 4 places
list LG = BrillNoether(G, C);
// Returns: basis of L(D) as vector space
```

### Hamburger-Noether Expansion

```singular
// HNexpansion computes Hamburger-Noether expansion
// Returns matrix with expansion data
list HN = HNexpansion(C, i); // At i-th singular point

// From HN expansion, compute:
// - Characteristic exponents
// - Puiseux pairs
// - Conductor degree
// - Delta invariant
// - Semigroup generators
```

### Parametrization

```singular
// Primitive parametrization up to given order
list param = Param(C, n); // Order n

// Returns parametrization of curve singularity
```

### Complete Example

```singular
LIB "brnoeth.lib";
ring r = 0, (x,y), lp;

// Define curve
list C = Adj_div(x3*y + y3 + x);

// Find places up to degree 4
C = NSplaces(1..4, C);

// Define divisor (multiplicities at each place)
intvec G = 0, 0, 0, 0;

// Compute Riemann-Roch space
list LG = BrillNoether(G, C);
```

* * *

## Singular: solve.lib (Polynomial System Solving)

**Source:** https://www.singular.uni-kl.de/Manual/4-3-0/sing_2398.htm

### Solving Polynomial Systems

```singular
LIB "solve.lib";

// Define system
ring r = 0, (x(1)..x(n)), dp;
ideal i = f1, f2, ..., fm;

// Compute Groebner basis
ideal si = std(i);

// Dimension of solution set
int dim = dim(si); // 0 = isolated solutions

// Number of solutions (with multiplicities)
int nroots = vdim(si);

// Numerical solutions (all complex)
list sols = solve(i, precision);
// precision = number of digits

// Real solutions only
list real_sols = solve(i, precision, 0, 1);

// With multiplicities
list sols_mult = solve(i, precision, 1);
```

### Isolated Solutions

```singular
// Isolated solutions only
list iso = isolate(i, precision);

// Real isolated solutions
list real_iso = isolate(i, precision, 0, 1);
```

### Triangular Decomposition

```singular
LIB "triang.lib";

// Triangular decomposition (Lazard method)
list tri = triangLf(i);

// Number of components
int ncomp = size(tri);

// Solve triangular systems
list sols = triang_solve(tri, precision);

// Regular chains
list reg = regDecomp(i);
```

* * *

## Macaulay2: Schubert2 Blowup

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Schubert2/html/_blowup.html

### Blow Up Abstract Variety

```macaulay2
-- Blow up Y along X (given by inclusion map i: X → Y)
(Ytilde, PN, PNmap, Ymap) = blowup(i)

-- Returns:
-- Ytilde: the blowup (abstract variety)
-- PN: exceptional divisor (projectivization of normal bundle)
-- PNmap: inclusion PN → Ytilde
-- Ymap: map Ytilde → Y

-- Example: Blowup of P² at point
P2 = abstractProjectiveSpace(2)
pt = point P2
i = map(pt, P2, ...)
(Ytilde, PN, PNmap, Ymap) = blowup(i)

-- Exceptional divisor class
Ediv = chern(1, exceptionalDivisor Ytilde)

-- Self-intersection
integral(Ediv^2) -- = -1 for blowup of surface at point
```

### Exceptional Divisor

```macaulay2
-- Get exceptional divisor as sheaf
Ediv = exceptionalDivisor Ytilde

-- Chern class of exceptional divisor
Eclass = chern(1, Ediv)

-- Intersection numbers
integral(Eclass^dim Ytilde)
```

* * *

## Macaulay2: Varieties Package (Tangent Sheaf)

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_tangent__Sheaf.html

### Tangent and Cotangent Sheaves

```macaulay2
-- Tangent sheaf T_X
T = tangentSheaf(X)

-- Cotangent sheaf Ω¹_X
Omega1 = cotangentSheaf(X)

-- Exterior powers Ω^p_X
OmegaP = cotangentSheaf(p, X)

-- Example: Verify Gauss-Bonnet on plane quartic (K3 surface)
X = Proj QQ[x_0..x_3]/ideal(x_0^4+x_1^4+x_2^4+x_3^4)
T = tangentSheaf(X)
c2 = chern(2, T)
euler_number = integrate(c2) -- = 24 for K3
```

### Cohomology of Sheaves

```macaulay2
-- Sheaf cohomology HH^i(X, F)
H = HH^i(F)

-- Dimension
h = dim HH^i(F)

-- Hodge numbers h^{p,q} = dim HH^q(Ω^p_X)
h11 = dim HH^1(cotangentSheaf(1, X))
h20 = dim HH^0(cotangentSheaf(2, X))
```

* * *

## Macaulay2: Polyhedra Package (Cones)

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Polyhedra/html/_cone_lp__Polyhedron_rp.html

### Cones over Polyhedra

```macaulay2
-- Cone over polyhedron P
C = cone(P)

-- Properties
dim C
isSimplicial C
isSmooth C
rays C

-- Dual cone
C_dual = dual(C)
```

* * *

## Macaulay2: Schubert2 Lines on Hypersurfaces

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Schubert2/html/___Lines_spon_sphypersurfaces.html

### Lines on Cubic Surface (27 lines)

```macaulay2
G = grassmannian(2, 4)
S = tautologicalSubbundle(G)
E = symmetricPower(3, dual(S))
num_lines = integrate(chern(4, E)) -- 27
```

### Lines on Quintic Threefold (2875 lines)

```macaulay2
G = grassmannian(2, 5)
S = tautologicalSubbundle(G)
E = symmetricPower(5, dual(S))
num_lines = integrate(chern(6, E)) -- 2875
```

* * *

## GAP: GRAPE Chapter 8 (Automorphism Groups)

**Source:** https://gap-packages.github.io/grape/htm/CHAP008.htm

### Automorphism Group of Graph

```gap
LoadPackage("grape");

# Automorphism group
aut := AutomorphismGroup(gamma);

# With specified group
aut := AutomorphismGroup(gamma, G);

# Isomorphism testing
IsIsomorphic(gamma1, gamma2);

# Canonical form
CanonicalForm(gamma);
```

* * *

## GAP: Digraphs Chapter 7 (Bliss Algorithm)

**Source:** https://docs.gap-system.org/pkg/digraphs/doc/chap7.html

### Bliss Automorphism Algorithm

```gap
LoadPackage("digraphs");

# Automorphism group via bliss
aut := BlissAutomorphismGroup(digraph);

# With vertex colors
aut := BlissAutomorphismGroup(digraph, vertex_colors);

# With vertex and edge colors
aut := BlissAutomorphismGroup(digraph, vertex_colors, edge_colors);

# Canonical labeling
canon := BlissCanonicalLabelling(digraph);
canon := BlissCanonicalLabelling(digraph, colors);
```

* * *

## Sage: Affine Curves

**Source:**
https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/affine_curve.html

### Affine Plane Curves

```python
# Affine plane curve
A2.<x,y> = AffineSpace(QQ, 2)
C = Curve(y^2 - x^3 - x)

# Or directly
C = AffinePlaneCurve(y^2 - x^3 - x)

# Affine curve in higher dimension
A4.<x,y,z,w> = AffineSpace(QQ, 4)
C = Curve([y^2 - x^3, z - x^2, w - y^2])
```

### Function Field (Integral Curves over Finite Fields)

```python
# Over finite field
F = GF(5)
A2.<x,y> = AffineSpace(F, 2)
C = AffinePlaneCurve(y^9 - x^8 - x^6 - x^5 - x^4 - x^3 - x)

# Function field
K = C.function_field()

# Closed points
points = C.closed_points()
points_d = C.closed_points(d) # Degree d points
```

* * *

## Buildings.sage: Tits Buildings

**Source:** https://github.com/m-dawes/buildings

### Usage

```python
load("src/external/buildings.sage")

H = SubGp_A2t()
H.building()
```

### SubGp_A2t — Õ⁺(2U + A₂)

```python
load("src/external/buildings.sage")

H = SubGp_A2t()
H.building()
```

**Returns:** `[lines, planes, incid]`
- `lines` — list of orbits of totally isotropic lines
- `planes` — list of orbits of totally isotropic planes
- `incid` — list of `(i,j)` pairs where plane `i` is incident to line `j`

**Attributes set by `H.building()`:**
- `H.lines` — orbit representatives for isotropic lines
- `H.planes` — orbit representatives for isotropic planes

### SubGp_GK — Õ⁺(2U + ⟨-6⟩ + ⟨-2⟩)

```python
H = SubGp_GK()
H.building()
```

### SubGp_UU2A2t — Õ⁺(U + U(2) + A₂)

```python
H = SubGp_UU2A2t()
H.building()
```

### SubGp_UUmA2t — Õ⁺(U + U(m) + A₂)

```python
H = SubGp_UUmA2t(m, N) # m, N positive integers
H.building()
```

### Key methods (all SubGp classes)

```python
# Compute building (orbits + incidence)
H.building() # Returns [lines, planes, incid]

# Get isotropic line orbit representatives
H.identify_bc_e() # Returns [g_i] such that [g_i·e] are inequivalent lines

# Get isotropic plane orbit representatives
H.identify_bc_E() # Returns [g_i] such that [g_i·E] are inequivalent planes

# Get incidence relations
H.incid_rels() # Returns [(i,j), ...] pairs

# Test if plane E contains vector equivalent to g·e under SubGp
H.line_plane_incid(e1, e2, gk, u)
```

* * *

## CARAT: Positive-Definite Lattice Groups

**Source:** System package (see carat_capabilities.md)

### Key Capabilities

```bash
# Automorphism groups
CARAT:Aut_grp(matrix_group)

# Isometry testing
CARAT:Isometry(L1, L2)

# Normalizer computation
CARAT:Normalizer(G)

# Orbit enumeration (finite sets)
CARAT:Orbit(G, vectors)

# Shortest vectors (positive-definite only)
CARAT:Shortest(L)

# Z-equivalence
CARAT:Z_equiv(L1, L2)
```

### Limitations

- **REQUIRES POSITIVE-DEFINITE FORMS** for Aut_grp, Isometry, Shortest
- Normalizer, Orbit, Z_equiv work with any finite matrix group
- Dimensions up to 6 (documented sweet spot)
- Depends on GMP headers/libraries

* * *

## GAP: Finite Group Actions (Chapter 41)

**Source:** https://docs.gap-system.org/pkg/grape/htm/CHAP004.htm

### Orbit and Stabilizer

```gap
# Orbit of point under group action
orbit := Orbit(G, point, action);

# All orbits
orbits := Orbits(G, set, action);

# Stabilizer of point
stab := Stabilizer(G, point, action);

# With specific action function
orbit := Orbit(G, point, OnPoints);
orbit := Orbit(G, point, OnSets);
orbit := Orbit(G, point, OnTuples);
orbit := Orbit(G, point, OnLines);
```

### OrbitsDomain

```gap
# Create orbits domain structure
od := OrbitsDomain(G, points, action);

# Iterate over orbits
for orb in od do
    # orb is list of points in this orbit
od;

# Number of orbits
Size(od);

# Representative of each orbit
reps := List(od, o -> o[1]);
```

### GAP Action Functions

```gap
# Standard action functions
OnPoints       # permute points of a set
OnSets         # permute subsets
OnTuples       # permute tuples
OnLines        # action on lines (projective)
OnRight        # multiply vectors on right
OnLeft         # multiply vectors on left

# Custom action functions
act := function(p, g)
    return p^g;  # define custom action
end;

# Use with Orbit, Stabilizer, etc.
orbit := Orbit(G, point, act);
```

* * *

* * *

## Macaulay2: Sheaf Hom and Ext

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_hom.html

### Sheaf Hom

```macaulay2
-- Sheaf Hom
Hom(F, G)
F ** G  -- sheaf tensor

-- Hom between sheaves
HH^i(Hom(F, G))

-- Ext groups
Ext^i(F, G)
```

### Pushforward and Pullback

```macaulay2
-- Pushforward under morphism
f_* F

-- Pullback
f^* F

-- Direct image
pushforward(f, F)

-- Inverse image
pullback(f, F)
```

* * *

## Macaulay2: Hilbert Polynomial

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_hilbert__Polynomial.html

### Computing Hilbert Polynomial

```macaulay2
-- Hilbert polynomial of sheaf
P = hilbertPolynomial(F)

-- Reduced Hilbert polynomial
P = hilbertPolynomial(F, Reduce => true)

-- Hilbert series
series = hilbertSeries(F)
```

* * *

## Macaulay2: Geometric Genus and Arithmetic Genus

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_geometric__Genus.html

### Genus Computation

```macaulay2
-- Geometric genus pg(X)
pg = geometricGenus(X)

-- Arithmetic genus pa(X)
pa = arithmeticGenus(X)

-- Irregularity q(X)
q = irregularity(X)
```

* * *

## GAP: GRAPE Chapter 7 (Graph Algorithms)

**Source:** https://gap-packages.github.io/grape/htm/CHAP007.htm

### Complete Subgraphs and Cliques

```gap
LoadPackage("grape");

# Complete subgraphs of given size
cliques := CompleteSubgraphs(gamma, k);
# Returns all complete subgraphs with k vertices

# Maximum clique
max_clique := MaximumClique(gamma);
max_clique := MaximumClique(gamma, colors); # with vertex colors

# Clique number (size of largest clique)
cn := CliqueNumber(gamma);
cn := CliqueNumber(gamma, colors);

# All maximal cliques
max_cliques := AllMaximalCliques(gamma);
```

### Graph Operations

```gap
# Complement graph
gamma_comp := Complement(gamma);

# Join of graphs
gamma_join := Join(gamma1, gamma2);

# Union of graphs
gamma_union := Union(gamma1, gamma2);

# Intersection
gamma_int := Intersection(gamma1, gamma2);
```

* * *

## Macaulay2: Ideal Sheaf

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_ideal__Sheaf.html

### Creating Ideal Sheaves

```macaulay2
-- Ideal sheaf of a subvariety
I = idealSheaf(X) -- X a subscheme

-- Or from an ideal
I = idealSheaf(Ideal) -- Ideal in coordinate ring
```

### Operations

```macaulay2
-- Sheaf associated to an ideal
F = sheaf(Module)

-- Pushforward under closed immersion
i_* I

-- Pullback under morphism
f^* F
```

* * *

## Macaulay2: Coherent Sheaf

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_coherent__Sheaf.html

### Creating Coherent Sheaves

```macaulay2
-- Sheaf of modules
F = sheaf(Module)

-- Structure sheaf
O = OO_X

-- Torsion sheaf
F = sheaf(Module) ** OO_X
```

### Operations

```macaulay2
-- Hom sheaf
Hom(F, G)

-- Tensor product
F ** G

-- Direct sum
F ++ G

-- Sheaf cohomology
HH^i(F)
h^i(F)

-- Full cohomology module
HH^i(F)

-- Just dimension
h = dim HH^i(F)

-- List all cohomology groups
coh = cohomology(F, m, n) -- HH^m through HH^n

-- Tor groups
Tor^i(M, N)
```

* * *

## Macaulay2: Weil Divisors (BasicDivisor)

**Source:** https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/BasicDivisors/html/

### Basic Divisors

```macaulay2
-- Create Weil divisor
D = divisor({1, 2, 3}, CoefficientList => true)

-- From polynomial
D = divisor(f)

-- Prime Weil divisors
P = primeDivisor(X, Y)
```

### Divisor Operations

```macaulay2
-- Addition
D1 + D2

-- Subtraction
D1 - D2

-- Scalar multiplication
2*D

-- Intersection
D1 * D2

-- Is effective?
isEffective(D)

-- Is principal?
isPrincipal(D)
```

* * *

## Macaulay2: Divisors (WeilDivisors Package)

**Source:** https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/WeilDivisors/html/

### Creating Divisors

```macaulay2
-- Weights on irreducible divisors
D = divisor({1, 2, 3}, CoefficientList => true)

-- From a Cartier divisor (line bundle)
D = divisor(L) -- L a line bundle

-- Prime divisors (codimension 1 components)
P = primeDivisor(X, Y)
```

### Operations

```macaulay2
-- Intersection number
D * E

-- Linear equivalence
D == E

-- Arithmetic genus
pa(D)

-- Geometric genus
pg(D)
```

* * *

## Macaulay2: Canonical Divisor

**Source:**
https://macaulay2.com/doc/Macaulay2-1.22/share/doc/Macaulay2/Divisor/html/_canonical__Divisor.html

### Canonical Divisor

```macaulay2
-- Compute canonical divisor K_X for variety X
K = canonicalDivisor(X)

-- For a specific variety
K = canonicalDivisor( projectiveSpace(2) )
```

### Properties

```macaulay2
-- Is the divisor Cartier?
isCartier(K)

-- Is it principal?
isPrincipal(K)

-- As a Weil divisor
K_weil = WeilDivisor K
```

* * *

## Macaulay2: Testing Very Ampleness

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_is__Very__Ample.html

### Testing Properties

```macaulay2
-- Is the sheaf/line bundle very ample?
isVeryAmple(L)

-- Is ample?
isAmple(L)

-- Is globally generated?
isGeneratedByGlobalSections(L)

-- Is nef?
isNef(L)
```

* * *

## Macaulay2: Fano Varieties Tutorial

**Source:** https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/FanoVarieties/html/

### Fano Varieties

```macaulay2
-- Fano variety of lines through a point
X = Fano(2, 1) -- Fano variety of lines on P^2

-- Grassmannians (Fano of dimension d)
G = grassmannian(2, 4) -- Gr(2,4)

-- Fano variety of degree d in P^n
X = FanoFromGushelMukai(d, n)
```

* * *

## Macaulay2: Index of Varieties Package

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_varieties.html

### Index Functions

```macaulay2
-- Index of sheaf cohomology
index(F)

-- Regularity
regularity(M)

-- Depth
depth(M)

-- Projective dimension
pd(M)
```

* * *

## Indefinite.jl: Automorphism Groups

**Source:** See `theory/backends/indefinite-jl`

### Automorphism Groups

```julia
using IndefiniteForms

# Automorphism group of indefinite lattice
aut = automorphism_group(L)

# Isometry testing
iso = is_isometric(L1, L2)

# Orbit representatives
orbits = orbit_representatives(L, action)
```

### Limitations

- Cannot handle indefinite forms for some computations
- Use CARAT for positive-definite cases

* * *

## Oscar.jl: Vinberg Algorithm

**Source:** https://docs.oscar-system.org/stable/NumberTheory/vinberg/

### Basic Usage

```julia
using Oscar

# From Gram matrix
Q = matrix(ZZ, [1 0 0; 0 -1 0; 0 0 -1])
v0 = matrix(ZZ, [1 0 0])
roots = vinberg_algorithm(Q, upper_bound; v0 = v0, root_lengths = [-2])
```

### Parameters

```julia
# Control vector with v0² > 0
v0 = matrix(ZZ, [1, 0, 0, ...])

# Root lengths to find
root_lengths = [-2] # for even lattice
root_lengths = [-1, -2] # for odd lattice

# Direction vector
direction_vector = matrix(ZZ, [0 1 0])

# Divisibilities
divisibilities = Dict(-2 => 1)
```

### Lattice Interface

```julia
# From lattice
S = integer_lattice(gram = Q)
roots = vinberg_algorithm(S, upper_bound; v0 = v0, root_lengths = [-2])
```

### Output

```julia
# roots = simple roots of fundamental chamber
# These generate the Weyl group
# Maximal parabolic subdiagrams correspond to subsets of simple roots
```

* * *

* * *

## GAP: Groups and Homomorphisms (Chapter 4)

**Source:** https://docs.gap-system.org/pkg/grape/htm/CHAP004.htm

### Group Creation

```gap
# Create group from generators
G := Group(g1, g2, ...);

# Cyclic group
C5 := CyclicGroup(5);

# Symmetric group
S5 := SymmetricGroup(5);

# Alternating group
A5 := AlternatingGroup(5);

# Direct product
G := DirectProduct(G1, G2);

# Semidirect product
G := SemidirectProduct(N, H, hom);
```

### Group Properties

```gap
# Order
Size(G);

# Is abelian?
IsAbelian(G);

# Is solvable?
IsSolvable(G);

# Is nilpotent?
IsNilpotent(G);

# Is simple?
IsSimple(G);

# Center
Center(G);

# Commutator subgroup
CommutatorSubgroup(G, H);
```

### Homomorphisms

```gap
# Create homomorphism
phi := GroupHomomorphismByImages(G, H, gens_G, gens_H);

# Kernel
K := Kernel(phi);

# Image
Im := Image(phi);

# Isomorphism
iso := IsomorphismGroups(G, H);
```

* * *

## GAP: Orbits and Actions (Chapter 5)

**Source:** https://docs.gap-system.org/pkg/grape/htm/CHAP005.htm

### Orbiting Points

```gap
# Orbit under group action
orb := Orbit(G, point, act);

# All orbits
orbits := Orbits(G, points, act);

# Orbit representative
rep := Representative(G, point, act);

# Is point in orbit?
point in Orbit(G, other_point, act);
```

* * *

* * *

## Oscar.jl: Intersection Theory and Chern Classes

**Source:** https://docs.oscar-system.org/stable/Schemes/intersection_theory/

### Chern Classes

```julia
using Oscar

# Total Chern class
c = total_chern(F) # F a sheaf or bundle

# Individual Chern class
c_i = chern(i, F)

# Chern roots
roots = chern_roots(F)

# Chern character
ch = chern_character(F)

# Todd class
td = todd_class(F)
```

### Intersection Products

```julia
# Intersection number
int = intersect(C1, C2)

# Cup product
c = cup(c1, c2)

# Poincaré duality
dual = poincare_dual(c)
```

### Virtual Classes

```julia
# Virtual fundamental class
virt = virtual_fundamental_class(X)

# Virtual structure sheaf
O_virt = virtual_structure_sheaf(X)

# Virtual Euler characteristic
chi_virt = virtual_euler_characteristic(X)
```

* * *

## Oscar.jl: Root Lattice Recognition

**Source:** https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/root_lattices/

### Root Lattice Recognition

```julia
using Oscar

# ADE type from Gram matrix
ADE_type(gram_matrix(A3)) # (:A, 3)

# Recognize root lattice (definite required)
ADE_types, sublattices = root_lattice_recognition(L)

# Fundamental lattice recognition
root_subl, ADE_types, sublattices = root_lattice_recognition_fundamental(L)
```

### Coxeter Data

```julia
# Coxeter number
coxeter_number(:A, 3)
coxeter_number(:D, 4)
coxeter_number(:E, 8)

# Highest root
highest_root(:A, n)
highest_root(:E, 6)
```

* * *

## Oscar.jl: Blowups and Projections

**Source:** https://docs.oscar-system.org/stable/Schemes/blowups/

### Blow Up

```julia
using Oscar

# Blow up along center
Bl, inc, proj = blowup(X, center)

# Exceptional divisor
E = exceptional_divisor(Bl)

# Blow up of projective space at point
Bl = blowup(projective_space(2), point)
```

### Controlled Blowups

```julia
# Blow up with specified exceptional divisor class
Bl = blowup(X, I, J) # I ideal, J coefficient ideal

# Information preserving blowup
Bl = blowup(X, center, attribute = :preserve)
```

* * *

## Sage: Projective Curves

**Source:**
https://doc.sagemath.org/html/en/reference/curves/sage/schemes/curves/plane_projective_curve.html

### Projective Plane Curves

```python
# Projective plane curve
P2.<x,y,z> = ProjectiveSpace(QQ, 2)
C = Curve(x^3*y + y^3*z + z^3*x)

# Degree and genus
deg = C.degree()
g = C.genus()

# Singular points
sing = C.singular_points()
nodes = C.nodes()
```

### Curve Properties

```python
# Is smooth?
C.is_smooth()

# Is irreducible?
C.is_irreducible()

# Is reduced?
C.is_reduced()

# Geometric genus
pg = C.geometric_genus()

# Arithmetic genus
pa = C.arithmetic_genus()
```

### Plane Curve Singularities

```python
# Singular locus
singular_locus = C.singular_locus()

# Singularity types
for p in C.singular_points():
    delta = p.delta()
    mul = p.multiplicity()
    etale = p.tangent_cone()
```

* * *

## Sage: Function Fields

**Source:**
https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/function_field.html

### Function Fields

```python
# Function field of curve
K = C.function_field()

# Rational function field
K = FunctionField(QQ, 'x')

# Algebraic extension
K.<y> = FunctionField(f) # f polynomial
```

### Field Operations

```python
# Define rational functions
x = K.gen()
f = x^2 + 1

# Pole and zero order
valuation(f, p) # valuation at place p

# Places
places = K.places()
places_deg_d = K.places(d) # degree d places
```

* * *

## Singular: Algebraic Curves (jacob.lib)

**Source:** https://www.singular.uni-kl.de/Manual/4-3-0/sing_1883.htm

### Jacobian and Hession

```singular
LIB "jacob.lib";

// Jacobian matrix
matrix J = jacob(I); // I ideal

// Jacobian of curve
ideal Jc = jacob(C); // C polynomial

// Hession matrix
matrix H = hessian(I);

// Hession of curve
ideal Hc = hessian(C);
```

### Critical Points

```singular
// Critical points of map
ideal crit = critical_points(F); // F : C -> P^1

// Determinant of Jacobian
ideal dj = det_jacob(I);
```

* * *

## Singular: Resolutions (resbin.lib)

**Source:** https://www.singular.uni-kl.de/Manual/4-3-0/sing_2300.htm

### Minimal Resolution

```singular
LIB "resbin.lib";

// Minimal resolution of singularities
list res = minbase(I);

// Full resolution
list res = nres(I); // minimal number of generators

// BETTI numbers
betti(res);
```

### Resolution Data

```singular
// Extract resolution
matrix m1 = res[1][1]; // first map
matrix m2 = res[2][1]; // second map

// Length of resolution
int len = size(res) - 1;
```

* * *

## GAP: Polycyclic Groups (Example)

**Source:** https://docs.gap-system.org/pkg/grape/htm/CHAP005.htm

### Creating Polycyclic Groups

```gap
# Subgroups of GL(n,Z) are polycyclic
G := SL(2, Integers);

# Finite quotient
Q := G / NormalSubgroup;

# Series
der := DerivedSeries(G);
low := LowerCentralSeries(G);
upp := UpperCentralSeries(G);
```

* * *

## Oscar.jl: Moduli of Curves

**Source:** https://docs.oscar-system.org/stable/AlgebraicGeometry/Moduli/

### Moduli Spaces

```julia
using Oscar

# M_g - moduli of curves of genus g
M = moduli_space_of_curves(g)

# Picards group
Pic = picard_group(M)

# tautological class
kappa = tautological_class(M)
```

* * *

## Oscar.jl: K3 Surfaces

**Source:** https://docs.oscar-system.org/stable/AlgebraicGeometry/K3Surfaces/

### K3 Surface Data

```julia
using Oscar

# Generic K3 surface
X = k3_surface()

# From genus and degree
X = k3_surface(g, d) # genus g, degree d

# Picard number
rho = picard_number(X)

# Neron-Severi group
NS = neron_severi_group(X)
```

* * *

## Macaulay2: BoijSoederberg

**Source:** https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/BoijSoederberg/html/

### Betti Diagrams

```macaulay2
-- Betti table
B = betti(resolution M)

-- Pure Betti numbers
pure_betti(table)

-- Boij-Soederberg decomposition
decompose B
```

* * *

## Macaulay2: ChainComplexExtras

**Source:**
https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/ChainComplexExtras/html/

### Complex Operations

```macaulay2
-- Tensor product of complexes
C ** D

-- Hom complex
Hom(C, D)

-- Cone
cone(f)

-- Mapping cone
mappingCone(f)
```

* * *

## REFERENCES: Complete URL Collection

All source URLs for the documentation above, extracted from user-provided Qwen session:

### Oscar.jl

- https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/integer_lattices/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/latwithisom/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/primembed/
- https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/discriminant_group/
- https://docs.oscar-system.org/stable/Hecke/manual/quad_forms/Zgenera/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/vinberg/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/genus_representatives/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/intersection_theory/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/root_lattice_recognition/
- https://docs.oscar-system.org/stable/NumberTheory/QuadFormAndIsom/Classification/
- https://docs.oscar-system.org/stable/AlgebraicGeometry/Schemes/moduli/
- https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicSurfaces/K3Surfaces/
- https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicSurfaces/EnriquesSurfaces/
- https://docs.oscar-system.org/stable/AlgebraicGeometry/AlgebraicCurves/curve_hilbert_scheme/

### Singular

- https://www.singular.uni-kl.de/Manual/4-3-0/sing_2254.htm (brnoeth.lib)
- https://www.singular.uni-kl.de/Manual/4-3-0/sing_2398.htm (solve.lib)
- https://www.singular.uni-kl.de/Manual/4-3-0/sing_1735.htm (jacob.lib)
- https://www.singular.uni-kl.de/Manual/4-3-0/sing_2282.htm (resbin.lib)
- https://www.singular.uni-kl.de/Manual/4-3-0/sing_2400.htm (triang.lib)

### Macaulay2

- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Schubert2/html/_blowup.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_tangent__Sheaf.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Polyhedra/html/_cone_lp__Polyhedron_rp.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Schubert2/html/___Lines_spon_sphypersurfaces.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_hom.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_hilbert__Polynomial.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_geometric__Genus.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_ideal__Sheaf.html
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_coherent__Sheaf.html
- https://macaulay2.com/doc/Macaulay2/BasicDivisors/html/
- https://macaulay2.com/doc/Macaulay2/WeilDivisors/html/
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_is__Very__Ample.html
- https://macaulay2.com/doc/Macaulay2/FanoVarieties/html/
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Varieties/html/_varieties.html
- https://macaulay2.com/doc/Macaulay2/BoijSoederberg/html/
- https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/ChainComplexExtras/html/
- **https://macaulay2.com/doc/Macaulay2-1.22/share/doc/Macaulay2/Divisor/html/_canonical__Divisor.html**

### GAP

- https://gap-packages.github.io/grape/htm/CHAP008.htm
- https://docs.gap-system.org/pkg/digraphs/doc/chap7.html
- https://www.gap-system.org/Manuals/doc/htm/ref/CHAP041.htm
- https://www.gap-system.org/Manuals/doc/htm/ref/CHAP004.htm
- https://www.gap-system.org/Manuals/doc/htm/ref/CHAP005.htm

### Sage

- https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/curves/affine_curve.html
- https://doc.sagemath.org/html/en/reference/schemes/sage/schemes/curves/projective_curve.html
- https://doc.sagemath.org/html/en/reference/function_fields/

### Buildings.sage

- https://github.com/m-dawes/buildings

### CARAT

- (CARAT is a standalone C package, no single URL)

### Indefinite.jl

- https://github.com/oscar-system/Indefinite.jl
