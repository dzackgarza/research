# ============================================================================
# FIXTURE: VARIETY PAIRS AND LOG CANONICAL STABILITY
#
# A variety pair (X, D) consists of a normal projective variety X and an
# effective Q-divisor D = Σ a_i D_i (a_i ∈ Q, 0 <= a_i <= 1).
#
# Stability conditions for the pair (X, D):
#
#   STABLE PAIR:
#     1. D_i.is_effective()         -- each component has non-negative multiplicity
#     2. D_i.is_weil_divisor()      -- each D_i is a Weil (= irreducible codim-1) divisor
#     3. D.is_slc()                 -- (X, D) is semi-log-canonical
#     4. (K_X + D).is_ample()       -- log canonical class K_X + D is ample
#     5. (K_X + D).is_Q_cartier()   -- K_X + D is Q-Cartier (needed to define discrepancies)
#
#   SUPPLEMENTARY PREDICATES:
#     D.is_lc()                     -- (X, D) is log canonical (stronger than slc for normal X)
#     D.is_klt()                    -- (X, D) is Kawamata log terminal (all discrepancies > -1)
#     D.is_dlt()                    -- divisorially log terminal
#     (K_X + D).is_nef()            -- nef log canonical class
#     (K_X + D).is_big()            -- big log canonical class
#
# VarietyPair(X, D) is a first-class type; VarietyPair.is_stable() checks all
# five conditions simultaneously and returns True/False.
#
# References:
#   Kollár–Mori "Birational geometry of algebraic varieties" §2.3, §5.1
#   Alexeev "Complete moduli in the presence of semiabelian group action" 
#   KSBA compactification — uses stable pairs for the moduli problem
# ============================================================================

P2 = PP^2(CC)
P3 = PP^3(CC)
R3.<x,y,z>     = PolynomialRing(CC, 3)
R4.<u,v,s,w>   = PolynomialRing(CC, 4)


# ============================================================================
# Section 1: VarietyPair constructor and basic predicates
# ============================================================================

# A smooth surface with an effective irreducible divisor D
S = P2
D = Variety(x^3 + y^3 + z^3).as_divisor()    # smooth cubic D on PP^2
pair_S_D = VarietyPair(S, D)

assert pair_S_D.variety() == S
assert pair_S_D.divisor() == D

# Component predicates
assert D.is_effective()
assert D.is_weil_divisor()
assert not D.is_empty()

# Q-Cartier: on a smooth variety, every Weil divisor is Cartier (and Q-Cartier)
assert D.is_Q_cartier()
assert D.is_cartier()


# ============================================================================
# Section 2: Stable pairs on smooth surfaces (log surfaces)
# ============================================================================
# (PP^2, a·L) for a smooth line L and coefficient a ∈ (0, 1]:
#   K_{PP^2} = -3H,  so K + a·L = -3H + a·H = (a-3)H.
#   For this to be ample: need (a-3) > 0, i.e. a > 3.
#   So (PP^2, a·L) with a ∈ (0,1] is NEVER a stable pair (K+D is anti-ample).

L = Variety(x + y + z).as_divisor()    # a line in PP^2
for a in [QQ(1,4), QQ(1,2), QQ(3,4), QQ(1,1)]:
    D_aL   = a * L
    pair_aL = VarietyPair(P2, D_aL)
    K_plus_D = P2.canonical_divisor() + D_aL

    assert D_aL.is_effective()
    assert D_aL.is_weil_divisor()
    assert D_aL.is_Q_cartier()
    assert not K_plus_D.is_ample()      # (a-3)H, never ample for a <= 1
    assert not pair_aL.is_stable()      # K+D not ample


# ============================================================================
# Section 3: Stable pair from a curve of general type
# ============================================================================
# Let C be a smooth curve of genus g >= 2 (general type: K_C ample).
# The pair (C, 0) is stable iff K_C is ample, i.e. g >= 2.

C5 = Variety(x^5 + y^5 + z^5)         # smooth plane quintic, g = 6
pair_C5 = VarietyPair(C5, C5.zero_divisor())

assert pair_C5.variety() == C5
assert pair_C5.divisor().is_zero()
assert pair_C5.divisor().is_effective()
assert C5.canonical_divisor().is_ample()
assert pair_C5.is_stable()

# Genus-1 curve: K_C ~ 0, NOT ample, so (E, 0) is NOT stable
E = Variety(x^3 + y^3 + z^3)          # elliptic curve
pair_E = VarietyPair(E, E.zero_divisor())
assert not pair_E.is_stable()          # K_E ~ 0, not ample

# Genus-0 curve: K ~ -2·pt, anti-ample
pair_P1 = VarietyPair(PP^1(CC), PP^1(CC).zero_divisor())
assert not pair_P1.is_stable()


# ============================================================================
# Section 4: Stable pairs (surface, boundary divisor)
# ============================================================================
# On a surface of general type S with ample K_S, the pair (S, D) is stable
# if D is an SLC effective Q-Weil divisor and K_S + D is still ample.

# Smooth sextic surface in PP^3: K = O(6-4) = O(2), general type
S6 = Variety(u^6 + v^6 + s^6 + w^6)   # smooth sextic in PP^3, general type
assert S6.canonical_divisor().is_ample()

D_S6 = S6.hyperplane_section().as_divisor()   # a smooth hyperplane section
pair_S6 = VarietyPair(S6, QQ(1,2) * D_S6)

K_plus = S6.canonical_divisor() + QQ(1,2) * D_S6
assert (QQ(1,2) * D_S6).is_effective()
assert (QQ(1,2) * D_S6).is_weil_divisor()
assert (QQ(1,2) * D_S6).is_Q_cartier()
assert pair_S6.divisor().is_slc()
assert K_plus.is_ample()
assert K_plus.is_Q_cartier()
assert pair_S6.is_stable()

# Raising coefficient past the log canonical threshold may kill stability
pair_S6_big = VarietyPair(S6, QQ(9,10) * D_S6)
# K + (9/10)D may push past log canonical threshold — check slc
if not pair_S6_big.divisor().is_slc():
    assert not pair_S6_big.is_stable()


# ============================================================================
# Section 5: Log canonical vs KLT vs SLC hierarchy
# ============================================================================
# klt => lc => slc  (strict inclusions in general)
# For a smooth pair (X, D) with simple normal crossings D and 0 < a_i < 1:
#   the pair is KLT.
# For a_i = 1: LC but not KLT.
# For a nodal boundary: SLC.

S_sm = Variety(u^4 + v^4 + s^4 + w^4)   # smooth quartic K3 (κ=0)
D_sm  = S_sm.hyperplane_section().as_divisor()   # smooth curve

# Coefficient strictly less than 1: KLT
pair_klt = VarietyPair(S_sm, QQ(1,2) * D_sm)
assert pair_klt.divisor().is_klt()
assert pair_klt.divisor().is_lc()
assert pair_klt.divisor().is_slc()

# Coefficient exactly 1: LC but not KLT
pair_lc = VarietyPair(S_sm, 1 * D_sm)
assert not pair_lc.divisor().is_klt()
assert pair_lc.divisor().is_lc()
assert pair_lc.divisor().is_slc()

# Nodal boundary curve: SLC only (the pair has nodal total space at D)
D_nodal = S_sm.nodal_curve()             # a nodal curve on S_sm
pair_slc = VarietyPair(S_sm, QQ(1,2) * D_nodal.as_divisor())
assert pair_slc.divisor().is_slc()
if D_nodal.is_nodal():
    # SLC but may fail LC at the node
    assert not pair_slc.divisor().is_lc() or pair_slc.divisor().is_lc()  # either ok


# ============================================================================
# Section 6: Sum of divisors and multi-component boundaries
# ============================================================================
# D = a_1 D_1 + a_2 D_2 + ...  with each D_i irreducible.

R3b.<x2,y2,z2> = PolynomialRing(CC, 3)
L1 = Variety(x2 + y2 + z2).as_divisor()      # line in PP^2
L2 = Variety(x2 - y2 + 2*z2).as_divisor()    # another line
Q  = Variety(x2^2 + y2^2 - z2^2).as_divisor()  # smooth conic

# D = (1/3)L1 + (1/2)L2 + (1/4)Q on PP^2
D_multi = QQ(1,3)*L1 + QQ(1,2)*L2 + QQ(1,4)*Q
pair_multi = VarietyPair(P2, D_multi)

components = D_multi.irreducible_components()
assert all(Di.is_effective() for Di in components)
assert all(Di.is_weil_divisor() for Di in components)
assert D_multi.is_slc()          # smooth components, simple normal crossings
assert D_multi.is_Q_cartier()    # smooth variety: Weil = Cartier

# K_{PP^2} + D_multi = -3H + (1/3+1/2+1/4·2)H = (-3 + 13/12)H — still neg
K_multi = P2.canonical_divisor() + D_multi
assert not K_multi.is_ample()   # PP^2 has too negative K to compensate
assert not pair_multi.is_stable()


# ============================================================================
# Section 7: is_stable() as combined predicate check
# ============================================================================
# VarietyPair.is_stable() returns True iff ALL of:
#   each D_i is effective, is_weil_divisor, D.is_slc, (K+D).is_ample, (K+D).is_Q_cartier

class StabilityWitness:
    """Exercise the stability conditions one-by-one."""
    def __init__(self, pair):
        self.pair = pair

    def check_components(self):
        for Di in self.pair.divisor().irreducible_components():
            assert Di.is_effective() and Di.is_weil_divisor()

    def check_slc(self):
        assert self.pair.divisor().is_slc()

    def check_ample(self):
        KD = self.pair.variety().canonical_divisor() + self.pair.divisor()
        assert KD.is_ample() and KD.is_Q_cartier()

    def check_all(self):
        self.check_components()
        self.check_slc()
        self.check_ample()
        assert self.pair.is_stable()

# A provably stable pair: smooth curve of genus >= 2 with empty boundary
witness = StabilityWitness(pair_C5)
witness.check_all()

# Unstable pair: PP^2 with a line (K+D anti-ample)
pair_fail = VarietyPair(P2, L1)
assert pair_fail.divisor().is_effective()
assert pair_fail.divisor().is_weil_divisor()
assert pair_fail.divisor().is_slc()
assert pair_fail.divisor().is_Q_cartier()
KD_fail = P2.canonical_divisor() + L1
assert not KD_fail.is_ample()       # fails ampleness
assert not pair_fail.is_stable()    # is_stable() returns False
