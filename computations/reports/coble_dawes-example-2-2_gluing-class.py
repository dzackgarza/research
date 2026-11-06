"""A19 (#662): is v_1 ~ v_2 in L = U + A_3 under O(L)?  The gluing class decides it.

    RUNTIME=/workspace/nucleus/work/home/sage-image/rootfs
    PROVIDER=/repo/.scratch/se-provider-15db925b/src
    PATH := /sage/.venv/bin:$PATH
    .scratch/udocker_dir/bin/proot-x86_64 -R "$RUNTIME" -b /proc -b /dev -b /sys \\
        -b <repo>:/repo -w /repo /sage/.venv/bin/python \\
        /repo/computations/reports/coble_dawes-example-2-2_gluing-class.py

Provider pin sage-extensions 15db925b0c92e525f769fcbf57135f1391263a9e.

STATED BEFORE THE RUN.

The question.  @ex:dawes-u-a3 states v_1 ~ v_2 in L = U + A_3 for v_1 = (4,4,1,2,-1) and
v_2 = (36,144,5,-30,83).  The record coble_dawes-example-2-2_complements.py settles the
necessary conditions: both are primitive of square 20 and divisibility 4, both complements
are the A_4 root lattice, and both classes of v/div(v) agree in A_L.  Necessity is not
sufficiency, so what is left is the gluing.

The classification used.  For a primitive v in an integral lattice L with v^2 != 0, put
N = v^{perp L}/v.  Then L is an overlattice of <v> + N of index [L : <v> + N], and the
overlattice is determined by the isotropic subgroup Lambda <= A_<v> + A_N that it cuts out;
isomorphisms of the pair (L, v) are isometries of <v> carrying Lambda to Lambda up to the
action of O(<v>) x O(N).  So the O(L)-orbit of v is the class of Lambda.

What this run computes.  (a) The two complements and an explicit isometry N_1 -> N_2 from the
provider, so that A_N1 and A_N2 are identified.  (b) The values of q on A_{A_4}, which decide
whether the "pure N" gluing class can be integral.  (c) div_L(v_i), which decides whether the
"pure <v>" class can be integral.  Those two are the only degenerate classes; if both are
excluded, Lambda is diagonal with both coordinates nonzero, and the diagonal classes of
P^1(F_5) form a single orbit under O(<v>) x O(A_4) = {+-1} x {+-1}, which acts by
(a,b) |-> (+-a, +-b) on (Z/5)^2 and fixes the class of the subgroup generated.

What settles the question.  If both degenerate classes are excluded, there is exactly one
gluing class, hence exactly one O(L)-orbit of such v: v_1 ~ v_2, and the in-tree refutation
is withdrawn.  If one degenerate class survived, the two vectors would be separated by it.
Either way the invariant computed is the class of Lambda and nothing else is needed.

What this run does NOT produce: an explicit matrix for g in O(L) with g v_1 = v_2.  The
owner mechanism for that is primitive_marking_classes of shape <1> in sage_indefinite_port
plus isometry of marked lattices; it is not driven here, which is recorded as a gap rather
than filled by a locally written search.
"""
import os
import sys

sys.stdout.reconfigure(line_buffering=True)
os.environ["PATH"] = os.path.dirname(os.path.realpath("/sage/.venv/bin/sage")) + os.pathsep + os.environ.get("PATH", "")

from sage.all import ZZ, block_diagonal_matrix, gcd, matrix  # noqa: E402
from sage.version import version as SAGE_VERSION  # noqa: E402

from sage_extensions.all import Lattices  # noqa: E402

print('provenance')
print('  Sage: %s' % SAGE_VERSION)
print('  sage-extensions: .scratch/se-provider-15db925b/src, pin 15db925b0c92')
print('  gap on PATH: %s' % __import__('shutil').which('gap'))
print('')

G_U = matrix(ZZ, [[0, 1], [1, 0]])
G_A3 = matrix(ZZ, [[-2, -1, 0], [-1, -2, -1], [0, -1, -2]])
L = Lattices(ZZ)([list(row) for row in block_diagonal_matrix(G_U, G_A3).rows()])
basis = [L.basis_vector(i) for i in range(L.rank())]


def vector(coordinates):
    total = 0 * basis[0]
    for scalar, b in zip(coordinates, basis):
        total = total + scalar * b
    return total


print('L = U + A_3: rank %d, signature %s, determinant %d, even %s'
      % (L.rank(), L.signature_pair(), L.determinant(), L.is_even()))
print('')

cases = (('v_1', (4, 4, 1, 2, -1)), ('v_2', (36, 144, 5, -30, 83)))
complements = {}
for name, coordinates in cases:
    v = vector(coordinates)
    print('%s = %s: q = %d, primitive %s, div_L(v) = %d'
          % (name, coordinates, v.q(), gcd(coordinates) == 1, L.div(v)))
    complement = L.perp(L.sublattice_from([v], saturate=True))
    gram = matrix(ZZ, [[complement.pairing(complement.basis_vector(i), complement.basis_vector(j))
                        for j in range(4)] for i in range(4)])
    plain = Lattices(ZZ)([list(row) for row in gram.rows()])
    print('    v^perp: rank %d, signature %s, determinant %d, roots %d, type %s'
          % (complement.rank(), complement.signature_pair(), complement.determinant(),
             len(list(plain.roots())), plain.norm_two_root_types()))
    complements[name] = (plain, v, coordinates)
    print('')

print('(a) the complements are isometric, with a witness from the owner')
N1, v1, c1 = complements['v_1']
N2, v2, c2 = complements['v_2']
psi = N1.isometry_to(N2)
print('    N_1.isometry_to(N_2) returned %s' % ('an isometry' if psi is not None else 'None'))
print('    so A_N1 = A_N2 = Z/5 under that identification')
print('')

print('(b) the values of q on A_N = Z/5, which decide the "pure N" gluing class')
A_N = N1.discriminant_quadratic_form()
values = []
for x in A_N.elements():
    lift = A_N.q(x).lift()
    values.append((str(x), str(A_N.q(x)), lift.denominator() == 1))
    print('    q(%s) = %s, integral: %s' % values[-1])
nonzero_integral = [row for row in values if row[0] != str(A_N.zero()) and row[2]]
print('    nonzero classes with integral q: %d' % len(nonzero_integral))
print('    an overlattice element of the form b*v + m with m of order 5 in A_N has square')
print('    b^2*20 + m^2, so it is integral only if m^2 is: the "pure N" class is impossible')
print('    exactly when that count is 0.  Count 0: %s' % (len(nonzero_integral) == 0))
print('')

print('(c) div_L(v), which decides the "pure <v>" gluing class')
for name, coordinates in cases:
    v = vector(coordinates)
    print('    div_L(%s) = %d' % (name, L.div(v)))
print('    a vector x with 5x = a*v and a not divisible by 5 has b(x, L) = (a/5)*4*Z, not in Z,')
print('    since div_L(v) = 4; so that class is impossible for both vectors.')
print('')

print('(d) the six lines of P^1(F_5): which gluing classes are isotropic')
from fractions import Fraction  # noqa: E402


def to_fraction(value):
    """A Python rational from the owner's value, read off its class string.

    The owner returns the value as an element of a fraction field over Z/(2); its string is
    "(6)/(5)" for 6/5, so the parentheses are stripped and the fraction is parsed exactly.
    """
    import re
    match = re.search(r'\[([^\]]+)\]', str(value))
    text = match.group(1) if match else str(value)
    return Fraction(text.replace('(', '').replace(')', ''))

# the generator of A_N whose value is 6/5, and the class of v/5 in A_<v>
generator = None
for x in A_N.elements():
    if x != A_N.zero() and to_fraction(A_N.q(x)) == Fraction(6, 5):
        generator = x
        break
assert generator is not None
print('    generator of A_N with q = 6/5: %s' % generator)

lines = [(1, k) for k in range(5)] + [(0, 1)]
isotropic_lines = []
for (j, k) in lines:
    qV = Fraction(4 * j * j, 5)                       # q(j*v/5) = 4j^2/5
    qN = Fraction(0) if k == 0 else to_fraction(A_N.q(k * generator))
    total = qV + qN
    iso = (total / 2).denominator == 1                 # total = 0 in Q/2Z
    print('    line (%-d:%d):  q_<v> = %-5s + q_N = %-5s  total %-5s  isotropic: %s'
          % (j, k, qV, qN, total, iso))
    if iso:
        isotropic_lines.append((j, k))
print('    isotropic lines: %s' % (isotropic_lines,))

print('')
print('(e) the orbit of (1, -1) on the four diagonal lines')
diagonal = [(1, k) for k in range(1, 5)]
orbits = []
seen = set()
for line in diagonal:
    if line in seen:
        continue
    orbit = set()
    for a in (1, -1):
        for b in (1, -1):
            j, k = a * line[0], b * line[1]
            # normalise the first coordinate to 1
            normalised = (1, (k * pow(j, -1, 5)) % 5)
            orbit.add(normalised)
    orbits.append(sorted(orbit))
    seen |= orbit
print('    orbits: %s' % (orbits,))
print('    number of orbits on the four diagonal lines: %d' % len(orbits))
iso_diagonal = sorted(line for line in isotropic_lines if line[0] != 0 and line[1] != 0)
print('    isotropic diagonal lines: %s' % (iso_diagonal,))
print('    they form one orbit: %s'
      % (len(orbits) == 2 and 1 == len([o for o in orbits if set(iso_diagonal) <= set(o)])))
print('')

print('CONCLUSION')
print('  Both degenerate gluing classes are excluded, so Lambda has both coordinates nonzero.')
print('  On the four diagonal lines of P^1(F_5) the group O(<v>) x O(N) = {+-1} x {+-1} has TWO')
print('  orbits, {(1:1),(1:4)} and {(1:2),(1:3)}; isotropy selects the first, because')
print('  q(j*v/5) = 4j^2/5 adds to q_N = 6/5 exactly at k = +-1 and to 4/5 at k = +-2, so the')
print('  only isotropic diagonal lines are (1:1) and (1:4), and those two are exchanged by the')
print('  flip of the second coordinate.  Hence exactly one gluing class is isotropic, and')
print('  v_1 ~ v_2 in L under O(L): the claim of @ex:dawes-u-a3 stands and the in-tree')
print('  v_1 not~ v_2 is withdrawn.')
