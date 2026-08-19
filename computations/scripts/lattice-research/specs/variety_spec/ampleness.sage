# ============================================================================
# FIXTURE: AMPLENESS, NEF-NESS, BIG-NESS
#
# Ample <=> Kodaira embedding theorem (positive curvature)
# Nef   <=> D·C >= 0 for all effective curves C
# Big   <=> h^0(nD) grows like n^dim
#
# Ample => Nef, Ample => Big.  Nef + Big does NOT imply Ample.
# ============================================================================

# Re-declare the needed varieties (this file is self-contained).
R4.<x,y,z,w> = PolynomialRing(CC, 4)
P3 = PP^3(CC)

S4 = Variety(x^4 + y^4 + z^4 + w^4)   # K3: K = 0
H_S4 = S4.hyperplane_class()
S5 = Variety(x^5 + y^5 + z^5 + w^5)   # general type: K = H
S3 = Variety(x^3 + y^3 + z^3 + w^3)   # del Pezzo: K = -H
Q  = Variety(x^2 + y^2 + z^2 + w^2)   # quadric: K = -2H

p0 = PP^2(CC).point([0, 0, 1])
pi1 = PP^2(CC).blowup(p0)
E1 = pi1.exceptional_divisor()
K_dP8 = pi1.domain().canonical_divisor()

Y = EnriquesSurface(...)
K_Y = Y.canonical_divisor()


# H on PP^n: ample, nef, big
H3_amp = P3.hyperplane_class()
assert H3_amp.is_ample() and H3_amp.is_nef() and H3_amp.is_big()
assert (-H3_amp).is_anti_ample() and not (-H3_amp).is_nef()

# K3 surface (S4): K = 0 is nef but not ample, not big; H|_{S4} is the ample polarisation
assert S4.canonical_divisor().is_nef()
assert not S4.canonical_divisor().is_ample() and not S4.canonical_divisor().is_big()
assert H_S4.is_ample() and H_S4.is_nef() and H_S4.is_big()

# Quintic (S5): K = H ample
assert S5.canonical_divisor().is_ample() and S5.canonical_divisor().is_big()

# Cubic surface (S3): K anti-ample; -K ample
assert S3.canonical_divisor().is_anti_ample()
assert (-S3.canonical_divisor()).is_ample() and (-S3.canonical_divisor()).is_nef()

# Quadric (Q): K = -2H anti-ample
assert Q.canonical_divisor().is_anti_ample()
assert (-Q.canonical_divisor()).is_ample()

# Blowup Bl_1 PP^2: E not nef; -K ample
assert not E1.as_divisor().is_nef()
assert (-K_dP8).is_ample() and (-K_dP8).is_nef() and (-K_dP8).is_big()

# Enriques surface: K nef but not ample, not big
assert K_Y.is_nef() and not K_Y.is_ample() and not K_Y.is_big()
