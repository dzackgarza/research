"""#760: the point A_{U(2)} can be named in the discriminant module; the preimage that needs it is killed.

The mod-2 triple test decides the pair when it fails: an element of Gent carrying the class of r12 to
that of r13 while fixing delta and the eta_5 line would have to carry the triple
(r12, delta, eta_5) mod 2T_En to the target triple, and any element of Gamma_Co,2 = R_Gent does fix
delta and lies in Gent.  Running that test needs a complete generating family of Gent, which is
rho_L^{-1} of the stabilizer in O(A_L) of the decomposition A_{U(2)} + A_{E8(-2)}.

This record settles the first half of that and reports the second half failing.

(1) The point CAN be named.  ``L.discriminant_group()`` is the presented module Z^12 / G Z^12, so an
    integer coordinate vector names a class; the classes of the two U(2) dual basis vectors are
    e_3 and e_4, and the quadratic form confirms it: q(e_3) = q(e_4) = 0 and q(e_3 + e_4) = 1/2, the
    hyperbolic plane of order 4 that A_{U(2)} is.  (Rational covector representatives are refused:
    ``d(vector(QQ, d3))`` raises TypeError, so this integer route is the one that works.)

(2) The preimage is KILLED.  ``L.Aut().discriminant_point_stabilizer(point)`` --- the call that turns
    that point into rho_L^{-1}(P) with generators --- does not return: the process was killed with
    exit code 137 after 625 s, at the memory ceiling, printing nothing.  This is the failure the
    method's own docstring records for a sibling route ("the joint discriminant image of the preimage
    entered that enumeration and was killed at 4282 MiB without returning in 2400 s").

So Gent's complete generating family is not obtainable through this call on T_En, and with it the
mod-2 triple test above.  Two ways out, both naming a unit rather than a milestone: make
``discriminant_point_stabilizer`` return for this point (it is a memory/complexity defect, reproducible
by running this file), or supply the mod-2 orthogonal group's stabilizer computation directly, since
Gent/Gamma(2) is a subgroup of {sigma in O(qbar) : sigma(A_L) = A_L, sigma(A_{U(2)}) = A_{U(2)}} and a
negative answer for that larger group is already decisive.  Nothing here is a substitute for either,
and no statement on the page is read off this record.

    usage: python3 computations/reports/coble_760-gent-family-probe.py     (killed, ~10 min)
"""
import sys, time
sys.stdout.reconfigure(line_buffering=True)
t0 = time.time()
def say(*a): print("[%6.1fs]" % (time.time()-t0), *a, flush=True)

from sage.all import ZZ, QQ, matrix, vector
from sage.env import SAGE_VERSION   # noqa: E402
src = open('/repo/computations/reports/coble_760-witness-13-14.py').read()
exec(src.split('Hre = matrix')[0].split('print("the cusp symmetries')[0])
Mgram = matrix(ZZ, G)
from sage_extensions.all import Lattices   # noqa: E402
L = Lattices(ZZ)([[int(G[i, j]) for j in range(N)] for i in range(N)])
d = L.discriminant_group()
print("the point A_{U(2)} in the discriminant module, and the preimage that is needed to name Gent")
print("Sage %s; sage-extensions at commit 1488acf" % SAGE_VERSION)
print()
print("(1) the discriminant module:", d)
def cls(coords):
    v = [0] * N
    for i in coords:
        v[i] = 1
    return d(v)
p3, p4 = cls([2]), cls([3])
print("    class e_3 -> q = %s ; class e_4 -> q = %s ; class e_3 + e_4 -> q = %s"
      % (p3.q(), p4.q(), d([0, 0, 1, 1] + [0] * 8).q()))
print("    (0, 0, 1/2 is the hyperbolic plane A_{U(2)}: the point is the right one)")
print()
print("(2) the preimage:")
say("    calling discriminant_point_stabilizer(point).group_generators()")
fam = L.Aut().discriminant_point_stabilizer(frozenset([p3, p4]))
gens = list(fam.group_generators())
say("    returned %d generators" % len(gens))
print()
print("PYEXIT=0")
