# Candidate Construction Families for 10-Nodal Rational Sextics

## Overview

This report identifies mathematically grounded construction methods for generating
additional explicit rational plane sextics with 10 nodes, beyond the three ad hoc
generic parametrization examples currently in the repo.

* * *

## 1. Halphen Pencil Construction (Index 2)

### Mathematical Background

A **Halphen pencil of index 2** is a pencil of plane curves of degree $3n = 6$ with nine
$n$-tuple base points.
For $n=2$, we have:
- Base points $P_1, \dots, P_9$ (possibly including infinitely near points)
- All base points lie on a cubic curve (the base locus)
- The pencil is of the form $\lambda F + \mu G = 0$ where $F, G$ are sextics sharing
  nine double points

The blowup of $\mathbb{P}^2$ at the nine base points gives a Halphen surface.
The general member is a rational curve of genus 1 (an elliptic curve), but special
members can be rational.

### Why It Produces 10-Nodal Rational Sextics

When a Halphen pencil of index 2 has a rational sextic member, that sextic automatically
acquires nodes at the nine base points plus one additional node—giving exactly 10 nodes.
This is because:
- The arithmetic genus of a degree-6 curve is $g_a = (6-1)(6-2)/2 = 10$
- Each double point reduces genus by 1
- With 9 base double points + 1 extra node: $10 - 9 - 1 = 0$, giving rationality

### Practical Computational Route

1. **Select 9 base points** in $\mathbb{P}^2$ lying on a cubic curve
2. **Construct the pencil**: Find two sextics $F, G$ with the same nine double points at
   the base
3. **Solve for rational member**: Find $(\lambda:\mu)$ such that $C_{\lambda,\mu} =
   \lambda F + \mu G$ is irreducible and rational
4. **Verify 10 nodes**: The 9 base points plus check for additional node

```python
# Pseudocode for SageMath implementation
R.<x,y,z> = PolynomialRing(QQ)
# Select 9 base points on a cubic
base_points = [...]  
# Find sextics passing through these with specified multiplicities
# Solve linear system for coefficients
# Extract the rational member
```

### Main Mathematical Risk

- **Risk**: Not every choice of 9 base points produces a rational sextic member.
  The condition for rationality is subtle—it requires the sum of the contributions from
  nodes to equal the arithmetic genus exactly.
- **Mitigation**: Start with known explicit configurations from the literature (e.g.,
  the 9 base points in special position from classical examples).

* * *

## 2. Steiner Sextic Construction

### Mathematical Background

A **Steiner sextic** is a rational plane sextic that can be described as the image of a
conic under a certain transformation.
Classically, given:
- A conic $Q \subset \mathbb{P}^2$
- A line bundle of degree 6 on $Q$ (equivalently, a degree-6 effective divisor)
- The complete linear system gives a map $Q \to \mathbb{P}^2$

The image is a rational sextic with specific node configurations.
Steiner sextics are images of conics under the Cremona transformation.

### Why It Produces 10-Nodal Rational Sextics

- The source curve is a conic (genus 0), so the image is automatically rational
- For generic choice, the map has exactly 10 branch points, each giving a node in the
  image
- This is the "double plane" construction in reverse: instead of projecting from a K3 to
  $\mathbb{P}^2$, we embed a conic via a degree-6 line bundle

### Practical Computational Route

1. **Start with a conic**: $Q: xz = y^2$ or similar
2. **Choose 6 points** on $Q$ (or a degree-6 effective divisor)
3. **Construct the linear system**: $|6L|$ where $L$ is a point on $Q$
4. **Compute the map**: $\varphi_{|6L|}: Q \to \mathbb{P}^2$
5. **Implicit equation**: Compute resultant to get sextic equation
6. **Verify nodes**: Check that there are exactly 10 nodes

```python
# Pseudocode
Q = Conic(x*z - y^2)  # or specify with parameters
P.<s,t> = PolynomialRing(QQ)
# Parametrize the conic: [s^2 : 2st : t^2]
# Choose degree-6 divisor: 6*p or sum of 6 points
# Compute the map to P^2 and get implicit equation
```

### Main Mathematical Risk

- **Risk**: The map may not be an embedding—it could have degree > 1, producing a
  covering rather than a rational curve.
- **Risk**: Special positions of the 6 points can cause degenerate images (fewer nodes,
  non-reduced components).
- **Mitigation**: Use generic choice of points in sufficiently general position, verify
  birationality.

* * *

## 3. Projection from a Rational Surface (Del Pezzo)

### Mathematical Background

Start with a rational surface $S$ (e.g., $\mathbb{P}^1 \times \mathbb{P}^1$, or a del
Pezzo surface of degree $d$) and consider:
- A linear system $|D|$ of curves of degree $6$ in $\mathbb{P}^2$
- Project from $S$ to $\mathbb{P}^2$

Particularly relevant: **del Pezzo surfaces of degree 1** are obtained by blowing up 8
points on $\mathbb{P}^2$. The anticanonical system $|-K_S|$ is a pencil of cubics.
A member of $|m(-K_S)|$ for $m=2$ gives a sextic.

### Why It Produces 10-Nodal Rational Sextics

- The blowup $\mathbb{P}^2 \to S$ at the 10 nodes gives a Coble surface
- Conversely, starting from a del Pezzo surface, the image of a curve under a projection
  can produce nodal sextics
- The geometry is controlled: the 10 nodes correspond to exceptional curves on the
  blowup

### Practical Computational Route

1. **Construct del Pezzo surface**: Blow up 8 points on $\mathbb{P}^2$
2. **Choose anticanonical curve**: $| -K_S |$ is a pencil of cubics
3. **Take double cover**: Cover by K3 surface branched over the sextic
4. **Extract the branch sextic**: The image curve in $\mathbb{P}^2$
5. **Verify 10 nodes**: Confirm exactly 10 ordinary double points

### Main Mathematical Risk

- **Risk**: The resulting sextic might have fewer than 10 nodes or have degenerate
  singularities.
- **Mitigation**: Choose generic blowup points; verify node count rigorously.

* * *

## 4. Double Cover Construction (K3 Branch)

### Mathematical Background

A Coble surface is the blowup of $\mathbb{P}^2$ at the 10 nodes of a sextic $C$. The
**K3 double cover** is: $$X: w^2 = F(x,y,z) \subset \mathbb{P}(1,1,1,3)$$

This is a K3 surface with 10 $A_1$ singularities (above the 10 nodes).
The construction can be reversed:
- Start with a K3 surface with specific properties
- Find an involution $X \to X$ with fixed points
- Quotient by the involution gives $\mathbb{P}^2$
- The branch curve is the image sextic

### Why It Produces 10-Nodal Rational Sextics

- The quotient $X/\langle \iota \rangle \cong \mathbb{P}^2$
- The branch divisor is a sextic with nodes at the images of the 10 fixed points
- By construction, this is a Coble curve

### Practical Computational Route

1. **Start with a specific K3 surface**: E.g., the generic K3 with Picard number 11
2. **Find an involution**: With exactly 10 fixed points (all $A_1$)
3. **Compute quotient**: $X \to X/\iota = \mathbb{P}^2$
4. **Extract equation**: Compute the branch curve equation
5. **Verify**: Check 10 nodes, rationality

### Main Mathematical Risk

- **Risk**: Finding explicit equations for K3 surfaces with the right involution is
  computationally challenging.
- **Mitigation**: Use known explicit examples from the literature (e.g.,
  Dolgachev-Kondō).

* * *

## 5. Cremona Transformation / Rational Surface Surgery

### Mathematical Background

Apply a **Cremona transformation** (birational map $\mathbb{P}^2 \dashrightarrow
\mathbb{P}^2$) to a known 10-nodal sextic:
- Start with one of the existing 3 examples
- Apply a quadratic Cremona transformation centered at 3 non-nodal points
- The image curve will again be a degree-6 curve
- The node count may change, but for generic choices remains 10

### Why It Produces 10-Nodal Rational Sextics

- Cremona transformations preserve rationality
- The transform of a nodal curve is again nodal
- Under generic conditions, nodes map to nodes

### Practical Computational Route

1. **Take existing sextic** $C$ from repo examples
2. **Choose 3 points** $p_1, p_2, p_3$ not on nodes
3. **Apply Cremona**: $(x:y:z) \mapsto (yz : xz : xy)$ centered at these points
4. **Compute image**: Substitute in the equation
5. **Simplify**: Clear denominators, find irreducible sextic factor

```python
# Example: quadratic Cremona centered at [1:0:0], [0:1:0], [0:0:1]
# Transformation: (x:y:z) -> (1/x : 1/y : 1/z) = (yz : xz : xy)
# Apply to existing F(x,y,z), clear denominators
```

### Main Mathematical Risk

- **Risk**: The transform might produce a non-reduced curve or change the node count.
- **Risk**: Points chosen too close to nodes can create higher singularities.
- **Mitigation**: Verify the result has 10 ordinary double points after transformation.

* * *

## Summary Table

| Construction | Mathematical Basis | Expected Node Count | Complexity |
| --- | --- | --- | --- |
| Halphen Pencil (index 2) | Pencil of sextics with 9 double base points | 10 (9 base + 1 extra) | Medium |
| Steiner Sextic | Image of conic under degree-6 map | 10 (generic) | Low-Medium |
| Del Pezzo Projection | Anticanonical system on rational surface | 10 | Medium |
| K3 Double Cover | Branch divisor of involution on K3 | 10 (by construction) | High |
| Cremona Transform | Birational image of existing sextic | 10 (generically) | Low |

* * *

## Recommended Priority

1. **Highest priority**: Halphen pencil construction — this is the most directly
   relevant to Coble surfaces and is a classical construction with known explicit
   examples in the literature.

2. **Second priority**: Steiner sextic construction — computationally straightforward
   starting point, connects to classical Steiner theory.

3. **Third priority**: Cremona transformation of existing examples — lowest
   computational overhead, can generate new examples quickly from existing ones.

* * *

## References

- Coble (1919): "The Ten Nodes of the Rational Sextic and of the Cayley Symmetroid"
- Dolgachev & Kondō (2013): "The rationality of the moduli spaces of Coble surfaces and
  of nodal Enriques surfaces"
- Dolgachev: "Classical Algebraic Geometry", Section 8.4
- Arbarello, Cornalba, Griffiths: "Geometry of Algebraic Curves", Volume II — Halphen
  pencils
- Cossec & Dolgachev: "Enriques Surfaces" — Halphen surfaces
