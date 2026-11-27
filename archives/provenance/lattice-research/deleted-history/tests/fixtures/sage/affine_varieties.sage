# ============================================================================
# FIXTURE: AFFINE VARIETIES
#
# Exercises the AA^n(CC) ambient space, affine Variety constructor, local
# algebra (coordinate rings, local rings), set-theoretic operations (union,
# complement, subtraction, subset/subvariety tests), and point coercion.
#
# Follows variety_interface_spec.sage sections 1-3 faithfully.
# ============================================================================

R.<x,y> = PolynomialRing(CC, 2)


# ============================================================================
# 1. AFFINE PLANE CURVE: UNION OF TWO LINES (A_1 node at origin)
# ============================================================================

# x^2 - y^2 = (x-y)(x+y); union of lines x=y and x=-y meeting at (0,0).
f = (x - y) * (x + y)

X = Variety(f)                  # Construct from affine equation
assert X.is_affine() and not X.is_projective()
assert X.is_hypersurface()      # codimension 1 in AA^2

assert X.ambient_variety() == AA^2(CC)
assert X.is_subset_of(AA^2(CC)) and X.is_subvariety_of(AA^2(CC))

# --- Point (0,0): the node ---------------------------------------------------
p = X([0, 0])                   # Affine point via coordinate list
assert p.is_singular()

X_sing = X.singular_locus()
X_sm   = X.smooth_locus()
assert p in X_sing and p not in X_sm

# X_sing is the single point {(0,0)}
assert X_sing.is_finite() and X_sing.is_closed()
assert X_sing == Variety([x, y])  # V(x,y) = {(0,0)}

# Set-theoretic operations: union, complement, subtraction
assert X_sing.union(X_sm) == X
assert X_sing.complement() == X_sm and X_sm.complement() == X_sing
assert X - X_sing == X_sm       and X - X_sm == X_sing

assert X_sm.is_smooth()  and not X_sm.is_singular()
assert not X_sing.is_smooth() and X_sing.is_singular()
assert not X.is_smooth()  and X.is_singular()

# --- Singularity type -------------------------------------------------------
assert p.singularity_type() == Singularity("A1")
assert p.is_node() and p.is_ordinary_double_point()
assert p.canonical_form() == Variety(x*y).point([0, 0])  # standard form uv=0
assert not p.is_cusp()

assert X.is_snc()   # Two transverse lines are simple normal crossing

f_blowup = X.blowup(p)
assert f_blowup.domain().is_smooth()

# --- Coordinate ring and local algebra --------------------------------------
# CC[x,y]/(x^2-y^2) in two equivalent notations
assert X.coordinate_ring() == CC['x','y'].quotient(f)
assert X.coordinate_ring() == CC['x', 'y'] / f

p_local = p.local_ring()
assert p_local == X.local_ring(p)
assert p_local.is_local()


# ============================================================================
# 2. SMOOTH AFFINE LINE: V(x - y)
# ============================================================================

X2 = Variety(x - y)
assert X2.is_affine() and X2.is_smooth()
assert X2.ambient_variety() == AA^2(CC)
assert X2.smooth_locus() == X2
assert X2.singular_locus() == Variety.empty()
assert X2.is_snc()

assert X2.is_isomorphic_to(AA^1(CC))

# For smooth X, resolution and normalization are identities.
assert X2.resolution().domain() == X2
assert X2.normalization() == X2


# ============================================================================
# 3. A SINGLE CLOSED POINT {(0,0)} IN AA^2
# ============================================================================

X3 = Variety([x - y, x + y])   # V(x-y, x+y) = V(x, y) = {(0,0)}
assert X3.cardinality() == 1

# Point membership via ambient space constructor
assert AA^2(CC).point((0, 0)) in X3
assert AA^2(CC).point((1, 1)) not in X3

p3 = X3.point((0, 0))
R_local = p3.local_ring()

# The local ring of a smooth point on a 0-dimensional variety over CC is CC.
assert R_local.is_local() and R_local.is_regular()
assert R_local.dimension() == 0 and R_local.is_field() and R_local == CC

assert X3.singular_locus() == Variety.empty() and X3.smooth_locus() == X3
assert X3.is_smooth() and X3.dimension() == 0
assert X3.resolution().domain() == X3
