
# Union of 2 transverse lines in AA^2, A_1 singularity
R.<x,y> = PolynomialRing(CC, 2)
f(x,y) = (x-y) * (x+y)
assert f.gradient() == vector(R, [2*x, -2*y])
X = Variety(f) # Automatically convert to ideal
# NB: union of x=y and x=-y, two lines, SNC at zero.
assert X.is_affine() and not X.is_projective()
assert X.ambient_variety() == AA^2(CC) and X.is_subset_of(AA^2(CC)) and X.is_subvariety_of(AA^2(CC))
assert X.is_hypersurface() # In AA^2_CC naturally
p = X([0,0]) # Affine point
assert p.is_singular()
X_sing = X.singular_locus()
X_sm = X.smooth_locus()
assert p in X_sing and p not in X_sm
assert X_sing == set([p]) and X_sing.is_finite() and X_sing.is_closed() # Points are closed in the Zariski topology
assert X_sing = Variety((x-0, y-0)) # V((x-p,y-q)) = (p,q)
assert X_sing.union(X_sm) == X
assert X_sing.complement() == X_sm and X_sm.complement() == X_sing
assert X - X_sing == X_sm and X - X_sm == X_sing # Convenience
assert X_sm.is_smooth() and not X_sm.is_singular()
assert not X_sing.is_smooth() and X_sing.is_singular()
assert not X.is_smooth() and X.is_singular()

assert p.singularity_type() == Singularities("A1")
assert p.is_node() and p.is_ordinary_double_point()
assert p.canonical_form() == Variety(xy).point([0,0]) # Local standard form: uv=0
assert not p.is_cusp()

assert X.is_snc()

# TODO: assert on X.blowup(p)
# TODO: assert X.blowup(p).is_smooth(), is_normal(), equals X.resolution()
assert X.coordinate_ring() == CC


assert p.local_ring() == X.local_ring(p) # TODO: what is this ring?
R = p.local_ring()

# Single line in AA^2
X = Variety(x-y)
assert X.is_smooth() and not X.is_singular() and X.smooth_locus() == X and X.singular_locus() == Variety.empty()
assert X.is_snc()
assert X.is_isomorphic_to(AA^1(CC)) # TODO: isomorphism witness.
assert X.resolution() == X == X.normalization() # Resolutions for curves are just normalizations


# (0,0) in AA^2
X = Variety((x-y, x+y))
assert X.cardinality() == 1 and X == X.point((0,0)) and AA^2(CC).point((0,0)) in X and AA^2(CC).point((1,1)) not in X
p = X.point((0,0))
R = p.local_ring()
assert R.is_local() and R.is_regular() and R.dimension() == 0 and R.is_field() and R == CC
assert X.singular_locus() == Variety.empty() and X.smooth_locus() == X and X.is_smooth() and X == X.resolution() and X.dimension() == 0

# A_2 singularity
X = Variety(y^2-x^3)
p = X((0,0)) # Convenience method for points.
assert X.is_singular() and X.singular_locus() == p # Convenience: treat a finite list of points as a variety.
assert p.singularity_type() == Singularities("A2")
assert not p.is_node() and p.is_cusp()


# A_n singularities
for n in range(10):
	X = Variety(y^2-x^n)
	p = X((0,0))
	assert p.singularity_type() == Singularities(f"A{n}")

# TODO: standard forms for types D and E
