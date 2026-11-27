# ============================================================================
# FIXTURE: SINGULAR PLANE CURVES
#
# Covers:
#   - Nodal and cuspidal cubics (A1, A2 singularities)
#   - Rational sextic with 10 nodes
#   - Projective closure of affine curves; is_nodal / is_cuspidal
#   - ADE singularity loops: A_n (n=1..10), D_n (n=4..10), E_6,E_7,E_8
#   - Milnor fibre topology: homotopy_type, Wedge of spheres, homology
# ============================================================================

R3.<x,y,z> = PolynomialRing(CC, 3)
R.<x2,y2>  = PolynomialRing(CC, 2)   # affine ring for projective-closure examples


# ============================================================================
# 1. NODAL CUBIC: y^2*z - x^2*(x - z) = 0
# ============================================================================

# Affine equation y^2 = x^2*(x-1); node at [0:0:1] with singularity type A1.
# p_a = 1 (from degree), p_g = p_a - #nodes = 0.
# Normalization: PP^1.  Resolution: blowup at the node.

f_node = y^2*z - x^2*(x - z)
nodal_cubic = Variety(f_node)
p_node = nodal_cubic([0, 0, 1])

assert nodal_cubic.is_projective() and nodal_cubic.is_hypersurface()
assert nodal_cubic.ambient_variety() == PP^2(CC)
assert nodal_cubic.degree() == 3 and nodal_cubic.dimension() == 1
assert nodal_cubic.is_singular() and not nodal_cubic.is_smooth()
assert nodal_cubic.is_nodal() and not nodal_cubic.is_cuspidal()

N_sing = nodal_cubic.singular_locus()
N_sm   = nodal_cubic.smooth_locus()
assert p_node in N_sing and p_node not in N_sm
assert N_sing.cardinality() == 1
assert N_sing.is_finite() and N_sing.is_closed()
assert N_sm.is_smooth() and not N_sm.is_singular()
assert not N_sing.is_smooth() and N_sing.is_singular()
assert N_sing.union(N_sm) == nodal_cubic
assert nodal_cubic - N_sing == N_sm

assert p_node.is_singular()
assert p_node.singularity_type() == Singularity("A1")
assert p_node.is_node() and p_node.is_ordinary_double_point()
assert not p_node.is_cusp()
assert p_node.milnor_number() == 1

# p_a from degree; p_g = p_a - #nodes
assert nodal_cubic.arithmetic_genus() == 1
assert nodal_cubic.geometric_genus() == 0
assert nodal_cubic.irregularity() == 0
assert nodal_cubic.normalization().is_isomorphic_to(PP^1(CC))
assert nodal_cubic.normalization().is_smooth()

# blowup at node resolves the singularity
f_res = nodal_cubic.blowup(p_node)
assert f_res.domain().is_smooth()

# Hodge diamond uses p_g, q: same as PP^1 (rational normalization)
assert nodal_cubic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert nodal_cubic.kodaira_dimension() == -Infinity
assert [nodal_cubic.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# ============================================================================
# 2. CUSPIDAL CUBIC: y^2*z - x^3 = 0
# ============================================================================

# Affine equation y^2 = x^3; cusp at [0:0:1] with singularity type A2.
# p_a = 1, p_g = 0.  Normalization: PP^1.  Two blowups needed to resolve.

f_cusp = y^2*z - x^3
cuspidal_cubic = Variety(f_cusp)
p_cusp = cuspidal_cubic([0, 0, 1])

assert cuspidal_cubic.is_projective() and cuspidal_cubic.is_hypersurface()
assert cuspidal_cubic.degree() == 3 and cuspidal_cubic.dimension() == 1
assert cuspidal_cubic.is_singular() and not cuspidal_cubic.is_smooth()
assert cuspidal_cubic.is_cuspidal() and not cuspidal_cubic.is_nodal()

P_sing = cuspidal_cubic.singular_locus()
P_sm   = cuspidal_cubic.smooth_locus()
assert p_cusp in P_sing and p_cusp not in P_sm
assert P_sing.cardinality() == 1
assert P_sing.union(P_sm) == cuspidal_cubic
assert cuspidal_cubic - P_sing == P_sm

assert p_cusp.is_singular()
assert p_cusp.singularity_type() == Singularity("A2")
assert p_cusp.is_cusp() and not p_cusp.is_node()
assert p_cusp.milnor_number() == 2

assert cuspidal_cubic.arithmetic_genus() == 1
assert cuspidal_cubic.geometric_genus() == 0
assert cuspidal_cubic.normalization().is_isomorphic_to(PP^1(CC))

f_res_cusp = cuspidal_cubic.blowup(p_cusp)
assert f_res_cusp.domain().is_singular()  # one blowup does not fully resolve A2

assert cuspidal_cubic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert cuspidal_cubic.kodaira_dimension() == -Infinity
assert [cuspidal_cubic.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# ============================================================================
# 3. RATIONAL SEXTIC WITH 10 NODES
# ============================================================================

# A degree-6 curve with p_g = 0 must have p_a - p_g = 10 - 0 = 10 nodes.
# (Same curve as in variety_interface_spec.sage, section 7.)
# p_a = (6-1)(6-2)/2 = 10, p_g = 10 - 10 = 0.

F_sextic = (
    137*x^6
    - 79*x^5*y - 61*x^5*z
    - 244*x^4*y^2 - 423*x^4*y*z - 134*x^4*z^2
    - 438*x^3*y^3 - 585*x^3*y^2*z - 128*x^3*y*z^2 + 19*x^3*z^3
    - 279*x^2*y^4 - 606*x^2*y^3*z - 395*x^2*y^2*z^2 - 61*x^2*y*z^3 + 7*x^2*z^4
    - 137*x*y^5 - 386*x*y^4*z - 550*x*y^3*z^2 - 479*x*y^2*z^3 - 212*x*y*z^4 - 34*x*z^5
    + 9*y^6 - 54*y^5*z - 256*y^4*z^2 - 385*y^3*z^3 - 276*y^2*z^4 - 97*y*z^5 - 13*z^6
)
rational_sextic = Variety(F_sextic)

assert rational_sextic.is_projective() and rational_sextic.is_hypersurface()
assert rational_sextic.degree() == 6 and rational_sextic.dimension() == 1
assert rational_sextic.is_singular() and not rational_sextic.is_smooth()
assert rational_sextic.is_nodal() and not rational_sextic.is_cuspidal()

RS_sing = rational_sextic.singular_locus()
RS_sm   = rational_sextic.smooth_locus()
assert RS_sing.cardinality() == 10
assert RS_sing.is_finite() and RS_sing.is_closed()
assert RS_sing.union(RS_sm) == rational_sextic
assert rational_sextic - RS_sing == RS_sm

assert all(q.is_node() and q.singularity_type() == Singularity("A1") for q in RS_sing)
assert all(q.milnor_number() == 1 for q in RS_sing)

assert rational_sextic.arithmetic_genus() == 10
assert rational_sextic.geometric_genus() == 0
assert rational_sextic.normalization().is_smooth()
assert rational_sextic.normalization().geometric_genus() == 0
assert rational_sextic.normalization().is_isomorphic_to(PP^1(CC))

assert rational_sextic.hodge_diamond() == Matrix(ZZ, [[1, 0], [0, 1]])
assert rational_sextic.kodaira_dimension() == -Infinity
assert [rational_sextic.plurigenus(n) for n in range(4)] == [1, 0, 0, 0]


# ============================================================================
# 4. PROJECTIVE CLOSURE
# ============================================================================

# The affine nodal curve y^2 = x^2*(x-1) in AA^2 has projective closure
# y^2*z = x^2*(x-z) in PP^2, which is our nodal_cubic above.  Verify the
# projective_closure() constructor and is_nodal / is_cuspidal attributes.

R2.<xa,ya> = PolynomialRing(CC, 2)
C_aff_nodal  = Variety(ya^2 - xa^2 * (xa - 1))    # affine nodal cubic
C_aff_cusp   = Variety(ya^2 - xa^3)               # affine cuspidal cubic

C_proj_nodal = C_aff_nodal.projective_closure()
C_proj_cusp  = C_aff_cusp.projective_closure()

assert not C_aff_nodal.is_projective() and C_proj_nodal.is_projective()
assert C_proj_nodal.ambient_space() == PP^2(CC)
assert C_proj_nodal.is_nodal() and not C_proj_nodal.is_cuspidal()
assert C_proj_nodal.degree() == 3

assert not C_aff_cusp.is_projective() and C_proj_cusp.is_projective()
assert C_proj_cusp.is_cuspidal() and not C_proj_cusp.is_nodal()


# ============================================================================
# 5. ADE SINGULARITIES AND MILNOR FIBRES
# ============================================================================

# Standard ADE forms:
#   A_n: y^2 - x^{n+1}  (n >= 1)
#   D_n: x^{n-1} + x*y^2  (n >= 4)
#   E_6: x^3 + y^4
#   E_7: x^3 + x*y^3
#   E_8: x^3 + y^5
#
# Milnor number mu equals the ADE rank.
# Milnor fibre MF has the homotopy type of a wedge of mu circles,
# giving H_0 = ZZ, H_1 = ZZ^mu, H_k = 0 for k >= 2.

Ra.<xa,ya> = PolynomialRing(CC, 2)

# --- A_n: y^2 - x^{n+1} ---------------------------------------------------
for n in range(1, 11):
    X = Variety(ya^2 - xa^(n+1))   # A_n: y^2 = x^{n+1}
    p = X((0, 0))

    assert X.is_singular()
    assert p.singularity_type() == Singularity(f"A{n}")
    assert p.milnor_number() == n

    if n == 1:
        assert p.is_node() and not p.is_cusp()
    if n == 2:
        assert p.is_cusp() and not p.is_node()

    MF = p.milnor_fibre()
    assert MF.is_connected()
    assert MF.homotopy_type() == Wedge([Sphere(1)] * n)
    assert MF.homology(0).rank() == 1
    assert MF.homology(1).rank() == n
    assert all(MF.homology(k).rank() == 0 for k in range(2, MF.dimension() + 1))

# --- D_n: x^{n-1} + x*y^2  (n >= 4) --------------------------------------
for n in range(4, 11):
    X = Variety(xa^(n-1) + xa*ya^2)
    p = X((0, 0))

    assert X.is_singular()
    assert p.singularity_type() == Singularity(f"D{n}")
    assert p.milnor_number() == n

    MF = p.milnor_fibre()
    assert MF.is_connected()
    assert MF.homotopy_type() == Wedge([Sphere(1)] * n)
    assert MF.homology(0).rank() == 1
    assert MF.homology(1).rank() == n
    assert all(MF.homology(k).rank() == 0 for k in range(2, MF.dimension() + 1))

# --- E_6, E_7, E_8 ----------------------------------------------------------
E_forms = {
    "E6": xa^3 + ya^4,
    "E7": xa^3 + xa*ya^3,
    "E8": xa^3 + ya^5,
}

for name, g in E_forms.items():
    X = Variety(g)
    p = X((0, 0))
    mu = Integer(name[1:])

    assert X.is_singular()
    assert p.singularity_type() == Singularity(name)
    assert p.milnor_number() == mu

    MF = p.milnor_fibre()
    assert MF.is_connected()
    assert MF.homotopy_type() == Wedge([Sphere(1)] * mu)
    assert MF.homology(0).rank() == 1
    assert MF.homology(1).rank() == mu
    assert all(MF.homology(k).rank() == 0 for k in range(2, MF.dimension() + 1))
