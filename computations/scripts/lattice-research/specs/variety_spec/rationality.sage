# ============================================================================
# FIXTURE: RATIONALITY AND UNIRATIONALITY
#
# Rational:    birational to PP^n
# Unirational: dominant rational map PP^n --> X
# Rational => Unirational (but not conversely in general)
#
# Curves: rational iff genus = 0
# Surfaces: classical results (Cayley-Salmon for cubics, etc.)
# ============================================================================

R3.<x,y,z> = PolynomialRing(CC, 3)
R4.<x4,y4,z4,w4> = PolynomialRing(CC, 4)

P1     = PP^1(CC)
conic  = Variety(x^2 + y^2 + z^2)        # degree 2, g=0
elliptic      = Variety(x^3 + y^3 + z^3) # degree 3, g=1
quartic_curve = Variety(x^4 + y^4 + z^4) # degree 4, g=3
Q  = Variety(x4^2 + y4^2 + z4^2 + w4^2) # smooth quadric in PP^3
S3 = Variety(x4^3 + y4^3 + z4^3 + w4^3) # smooth cubic surface
S4 = Variety(x4^4 + y4^4 + z4^4 + w4^4) # K3 quartic
S5 = Variety(x4^5 + y4^5 + z4^5 + w4^5) # general type quintic
Y  = EnriquesSurface(...)

# Curves: rational iff genus 0
assert P1.is_rational() and P1.is_unirational()
assert conic.is_rational() and conic.is_unirational()
assert not elliptic.is_rational() and not elliptic.is_unirational()   # g=1
assert not quartic_curve.is_rational() and not quartic_curve.is_unirational()  # g=3

# Surfaces: classical rationality results
assert Q.is_rational() and Q.is_unirational()    # smooth quadric ≅ PP^1 × PP^1
assert S3.is_rational() and S3.is_unirational()  # smooth cubic surface (Cayley-Salmon)
assert not S4.is_rational()   # K3 surface (Kodaira dim 0, non-trivial 2-form)
assert not S5.is_rational() and not S5.is_unirational()  # general type
assert not Y.is_rational()    # Enriques surface
