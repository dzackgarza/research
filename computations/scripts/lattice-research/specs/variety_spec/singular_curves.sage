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
# 4A. REDUCIBLE PROJECTIVE CONIC: UNION OF TWO LINES
# ============================================================================

# The projective closure of the affine node (x-y)(x+y)=0 is the reducible conic
# V((x-y)(x+y)) ⊂ PP^2.  It is the union of two copies of PP^1 meeting
# transversely in one node, hence a simple normal crossing curve with
# arithmetic genus 0 and geometric genus 0.

two_lines_affine = Variety((x2 - y2) * (x2 + y2))
two_lines_proj = two_lines_affine.projective_closure()
t_proj = polygen(QQ, 't_proj')

assert two_lines_proj.ambient_space() == PP^2(CC)
assert two_lines_proj.is_projective() and not two_lines_proj.is_affine()
assert two_lines_proj.degree() == 2 and two_lines_proj.dimension() == 1
assert two_lines_proj.is_singular() and two_lines_proj.is_nodal()
assert not two_lines_proj.is_cuspidal()
assert two_lines_proj.is_snc()
assert two_lines_proj == Variety((x - y) * (x + y))

two_lines_sing = two_lines_proj.singular_locus()
assert two_lines_sing.cardinality() == 1
q_two_lines = two_lines_sing.points()[0]
assert q_two_lines.is_node() and q_two_lines.singularity_type() == Singularity("A1")

two_lines_components = list(two_lines_proj.irreducible_components())
assert len(two_lines_components) == 2
assert all(comp.is_isomorphic_to(PP^1(CC)) for comp in two_lines_components)

assert two_lines_proj.arithmetic_genus() == 0
assert two_lines_proj.geometric_genus() == 0
assert two_lines_proj.irregularity() == 0
assert two_lines_proj.holomorphic_euler_characteristic() == 1
assert two_lines_proj.topological_euler_characteristic() == 3
assert two_lines_proj.hilbert_polynomial(t_proj) == 2*t_proj + 1
assert [two_lines_proj.plurigenus(n) for n in range(5)] == [1, 0, 0, 0, 0]
assert two_lines_proj.kodaira_dimension() == -Infinity


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


# ============================================================================
# 6. EXPLICIT NORMALIZATION EQUATIONS
# ============================================================================
# The normalization of a singular curve comes with an explicit parametrization.
# For a rational curve the normalization is PP^1 and the normalization map is
# given by an explicit polynomial parametrization (a morphism PP^1 → C).

# Normalization of the nodal cubic y^2*z - x^2*(x-z) = 0:
#   parametrized by [s:t] ↦ [s*t^2 : t^3*(s-1)/? : ... ] (affine: x=t^2, y=t^3-t)
# In affine chart z=1: y^2 = x^2*(x-1), parametrize by t ↦ (t^2, t*(t^2-1)^{1/2}) doesn't work.
# Better: in affine chart x=u, y=u*v; substituting y=u*v: u^2*v^2 = u^2*(u-1), v^2 = u-1.
# Standard normalization: v ↦ (v^2+1, v*(v^2+1)) -- check: y^2 = v^2*(v^2+1)^2 = (v^2+1)^2*(v^2+1-1) ✓
# Projective: [s:t] ↦ [s^2+t^2 : s*(s^2+t^2) : t^2]  (in chart t=1: s ↦ (s^2+1, s*(s^2+1)) ✓)

nu_node = nodal_cubic.normalization()
assert nu_node.is_isomorphic_to(PP^1(CC))
assert nu_node.is_smooth()

nu_map_node = nodal_cubic.normalization_map()   # VarietyMorphism  PP^1 → nodal_cubic
assert nu_map_node.codomain() == nodal_cubic
assert nu_map_node.domain().is_isomorphic_to(PP^1(CC))
assert nu_map_node.is_birational()
assert nu_map_node.is_finite()

# The normalization map is an isomorphism away from the node
assert nu_map_node.is_isomorphism_over(nodal_cubic.smooth_locus())

# Explicit parametrization of the nodal cubic y^2 = x^2*(x-1) (affine, z=1):
#   t ↦ (t^2+1, t*(t^2+1))   checks: y^2 = t^2*(t^2+1)^2 = (t^2+1)^2*(t^2+1-1) ✓
Raff.<t_aff> = PolynomialRing(CC)
param_x = t_aff^2 + 1
param_y = t_aff * (t_aff^2 + 1)
f_affine_node = y2^2 - x2^2 * (x2 - 1)
assert f_affine_node(param_x, param_y) == 0    # curve equation satisfied

# Normalization of the cuspidal cubic y^2 = x^3 (affine, z=1):
#   t ↦ (t^2, t^3)  checks: (t^3)^2 = t^6 = (t^2)^3 ✓
param_cusp_x = t_aff^2
param_cusp_y = t_aff^3
f_affine_cusp = y2^2 - x2^3
assert f_affine_cusp(param_cusp_x, param_cusp_y) == 0

nu_map_cusp = cuspidal_cubic.normalization_map()
assert nu_map_cusp.domain().is_isomorphic_to(PP^1(CC))
assert nu_map_cusp.is_birational()
assert nu_map_cusp.is_finite()

# The normalization of a cusp is an isomorphism over the smooth locus
assert nu_map_cusp.is_isomorphism_over(cuspidal_cubic.smooth_locus())

# The fiber of the normalization map over the cusp is a single point (unibranch)
preimage_cusp = nu_map_cusp.preimage(p_cusp)
assert preimage_cusp.cardinality() == 1     # one preimage: cusp is unibranch

# The fiber of the normalization map over the node has two preimages (two branches)
preimage_node = nu_map_node.preimage(p_node)
assert preimage_node.cardinality() == 2     # two preimages: node has two branches


# ============================================================================
# 7. CYCLE OF RATIONAL CURVES (Ã_n configuration)
# ============================================================================
# An Ã_n cycle: n copies of PP^1, each meeting the next in exactly one node,
# arranged in a cycle.  This is the dual graph of the minimal resolution of a
# type Ã_n (extended A_n) singularity.  It also arises as a "type I_n" Kodaira
# fiber in an elliptic fibration.
#
# Arithmetic genus: for n rational components in a cycle with n nodes,
#   p_a = 1  (the loop contributes one to genus regardless of n).
# Geometric genus: p_g = 0 (all components are rational).

# Construct Ã_2: three PP^1s in a triangle, meeting pairwise in 3 nodes.
# In PP^2: the union of three lines L_1, L_2, L_3 in general position.
# Each pair meets in one point, so we get 3 nodes.

R_cyc.<x_c, y_c, z_c> = PolynomialRing(CC, 3)
# L_1 = V(x), L_2 = V(y), L_3 = V(z); triangle
f_triangle = x_c * y_c * z_c
C_triangle = Variety(f_triangle)

assert C_triangle.irreducible_components().length() == 3
assert all(comp.genus() == 0 for comp in C_triangle.irreducible_components())
assert all(comp.is_isomorphic_to(PP^1(CC)) for comp in C_triangle.irreducible_components())

# Three nodes: {(x=y=0), (x=z=0), (y=z=0)} in PP^2
sing_tri = C_triangle.singular_locus()
assert sing_tri.cardinality() == 3
assert all(p_t.is_node() for p_t in sing_tri)

# Arithmetic genus p_a = 1 (one cycle)
assert C_triangle.arithmetic_genus() == 1
# Geometric genus p_g = 0 (rational components)
assert C_triangle.geometric_genus() == 0

# The dual graph: 3 vertices (one per component), 3 edges (one per node).
# This is the graph Ã_2 = the cycle C_3.
dual_graph = C_triangle.dual_graph()
assert dual_graph.num_vertices() == 3
assert dual_graph.num_edges() == 3
assert dual_graph.is_cycle()

# Construct Ã_1: two PP^1s meeting in 2 nodes (a "banana").
# In PP^1 × PP^1: take two members of |F| (fibers) — but simpler via PP^2:
# The two components of the union V(x*y): x=0 and y=0 in AA^2 don't give two nodes.
# Instead: V(x^2 - y^2) = V((x-y)(x+y)) gives two lines meeting in one node.
# For two nodes (Ã_1): need two lines meeting at two distinct points, not possible in PP^2.
# The Ã_1 banana lives naturally in a ruled surface or as a complete intersection.
# In PP^1 × PP^1: take s*(1-s) = 0 as the curve — two fibers of each ruling.
C_banana = VarietyCurve.banana(CC)     # Two PP^1s meeting at two points
assert C_banana.irreducible_components().length() == 2
assert all(comp.is_isomorphic_to(PP^1(CC)) for comp in C_banana.irreducible_components())
sing_ban = C_banana.singular_locus()
assert sing_ban.cardinality() == 2
assert all(p_b.is_node() for p_b in sing_ban)
assert C_banana.arithmetic_genus() == 1
assert C_banana.geometric_genus() == 0

dual_ban = C_banana.dual_graph()
assert dual_ban.num_vertices() == 2
assert dual_ban.num_edges() == 2
assert dual_ban.is_cycle()


# ============================================================================
# 8. DUAL COMPLEX OF RESOLUTION (Dynkin type)
# ============================================================================
# For an ADE surface singularity, the minimal resolution has exceptional
# divisor whose dual graph (components as vertices, intersections as edges)
# is the corresponding Dynkin diagram.
#
# Specifically, if p ∈ X is an A_n (resp D_n, E_n) singularity, then the
# minimal resolution f: X̃ → X has exceptional locus E = E_1 ∪ ... ∪ E_k
# with each E_i ≅ PP^1, E_i^2 = -2, and the dual graph is A_n (resp D_n, E_n).
# The dual complex of the resolution = the Dynkin diagram.

# A_2 singularity: y^2 - x^3 (cusp), minimal resolution has one -2 curve (E_1^2 = -2)
# Wait, A_2 requires 2 blowups: the first gives a -1 curve which is not minimal.
# After full minimal resolution: E has 2 components E_1, E_2 with E_1*E_2=1, E_1^2=E_2^2=-2.
# The dual graph is the A_2 Dynkin diagram: o—o.

res_A2 = cuspidal_cubic.resolution()
E_A2 = res_A2.exceptional_locus()
assert E_A2.irreducible_components().length() == 2
E_A2_comps = list(E_A2.irreducible_components())
assert all(Ei.self_intersection() == -2 for Ei in E_A2_comps)
assert all(Ei.is_isomorphic_to(PP^1(CC)) for Ei in E_A2_comps)
# E_1 meets E_2 in exactly 1 point
assert E_A2_comps[0].intersection_number(E_A2_comps[1]) == 1

dc_A2 = res_A2.dual_complex()
assert dc_A2.dynkin_type() == DynkinDiagram("A2")

# A_1 singularity (node): minimal resolution has one -2 curve
res_A1 = nodal_cubic.resolution()
E_A1 = res_A1.exceptional_locus()
assert E_A1.irreducible_components().length() == 1
E_A1_comp = list(E_A1.irreducible_components())[0]
assert E_A1_comp.self_intersection() == -2
assert E_A1_comp.is_isomorphic_to(PP^1(CC))

dc_A1 = res_A1.dual_complex()
assert dc_A1.dynkin_type() == DynkinDiagram("A1")

# D_4 singularity: x^3 + y^4 (E_6)... wait, D_4 = x^2*y + y^3
# Use D_n from the loop above: D_4 equation is x^3 + x*y^2 (n=4 => x^(n-1) + x*y^2 = x^3 + x*y^2)
# but let's use the standard xy^2 + x^n form.
# D_4: x^2*y + y^3 = y*(x^2 + y^2): three lines through origin, tangent to y-axis.
# Alternatively x^3 + x*y^2 = x*(x^2+y^2): tangent intersection.
# Use the conventional D_4 form to be explicit:
Raff2.<xa2, ya2> = PolynomialRing(CC, 2)
C_D4 = Variety(xa2^2*ya2 + ya2^3)   # y*(x^2+y^2), equivalent to xa2^3 + xa2*ya2^2
p_D4 = C_D4((0, 0))
assert p_D4.singularity_type() == Singularity("D4")

res_D4 = C_D4.resolution()
E_D4 = res_D4.exceptional_locus()
E_D4_comps = list(E_D4.irreducible_components())
assert len(E_D4_comps) == 4
assert all(Ei.self_intersection() == -2 for Ei in E_D4_comps)

dc_D4 = res_D4.dual_complex()
assert dc_D4.dynkin_type() == DynkinDiagram("D4")

# E_6 singularity:  dual graph is E_6 (6 components)
C_E6 = Variety(xa2^3 + ya2^4)
res_E6 = C_E6.resolution()
dc_E6 = res_E6.dual_complex()
assert dc_E6.dynkin_type() == DynkinDiagram("E6")
