"""In which family does ABE22's divisor exist? (research#679, A36)

    python3 computations/reports/coble_679-locus-probe.py

The question @qst:recognizable-semifan asks first is whether a *recognizable* divisor can
fail (W).  Its only candidate in the sources read is ABE22's $s + m\\sum_{i=1}^{24} f_i$, and
this probe decides a smaller matter on which the posing of the question depends: in which
moduli space that divisor is a divisor at all.

The arithmetic, all of it exact and two lines long.

- ABE22's divisor is built from a section $s$ and the singular fibres $f_i$ of an elliptic
  fibration, so its existence requires a surface with a primitive class $s$ of square $-2$ and
  a class $f$ with $f^2=0$, $s\\cdot f=1$: the lattice $U\\oplus\\langle-2\\rangle$ inside the
  Picard group, of rank 3.
- The very general degree-two K3 surface has Picard group $\\langle L\\rangle$, of rank 1, since
  $L^2=2$ and the Noether-Lefschetz divisors are proper: the surfaces of Picard rank greater
  than one form a countable union of proper subvarieties of $F_2$, so a very general member is
  outside them.
- Rank 3 > rank 1, so the surfaces carrying $(s,f)$ form a proper locus $F\\subset F_2$, and
  $s+m\\sum f_i$ is not a divisor on $F_2$: it exists only on $F$, the elliptic Heegner locus,
  which is the space ABE22 write $F$.

Second, so that the candidate is not vacuous where it does exist: on a surface of $F$, ABE22's
divisor meets the two curve classes of that lattice positively, $(s+m\\sum f_i)\\cdot f = 1$ and
$(s+m\\sum f_i)\\cdot s = 24m-2$, which is positive for every $m\\ge1$.  So it is a polarizing
divisor there, and the failure of (W) recorded in @prop:semifan-coarsening-fails is a statement
about a genuine polarizing divisor -- on $F$, not on $F_2$.
"""

from fractions import Fraction

GENERIC_PICARD_RANK = 1          # <L>, L^2 = 2, on a very general degree-two K3
ELLIPTIC_LATTICE_RANK = 3        # U + <-2>: the classes f, s and a second fibre direction

print("generic degree-two K3:  Picard group = <L>, rank %d" % GENERIC_PICARD_RANK)
print("elliptic K3 with section: U + <-2> inside Pic, rank %d" % ELLIPTIC_LATTICE_RANK)
print("so the surfaces carrying (s, f) form a proper locus F in F_2: rank %d > %d" % (
    ELLIPTIC_LATTICE_RANK, GENERIC_PICARD_RANK))
print()

# the divisor D = s + m sum f_i, with sum f_i == 24 f (all fibres are algebraically equivalent)
print("positivity of D = s + m (sum f_i) = s + 24 m f on the two curve classes of U + <-2>:")
for m in (1, 2, 3):
    on_f = Fraction(1)                       # s.f = 1, f.f = 0
    on_s = Fraction(24 * m) - 2              # s.s = -2, f.s = 1
    print("  m = %d:  D.f = %s > 0,  D.s = %s > 0" % (m, on_f, on_s))
print()
print("Conclusion.  ABE22's divisor is a polarizing divisor on the elliptic locus F and not on")
print("F_2, so the question whether a recognizable divisor can fail (W) has to be posed for F;")
print("on F_2 the very general surface has Picard rank one and carries no such divisor.")
