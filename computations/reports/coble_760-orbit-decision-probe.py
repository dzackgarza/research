"""#760, item 7: whether the library can decide the Gamma_Co,2-orbit question at cusp 5.

The question.  Roots 12, 13, 14 of Sterk's cusp-5 diagram have pairwise distinct classes in
K_5 and all three cut one cone of the restricted semifan, so the counterexample the issue wants
turns on a single fact: are two of them in the same orbit under Gamma_Co,2 = Stab_{O(T_En)}(Z
delta)?  The acting family on K_5 is the stabilizer of eta_5 in that group.

What the library offers, and what it does not (probed here, not asserted from notes):

  * ``L.primitive_isotropic_subobject(eta_5).isotropic_reduction()`` builds K_5 itself, in
    about a second --- the record prints rank, signature and determinant;
  * ``K.primitive_orbit_series(bound=4)`` and ``K.discriminant_orbit_series(bound=4)`` are the
    orbit-deciding operations the library carries: orbit series for the standard orthogonal
    subgroups of the lattice.  The record calls the first; it does not return within the bound
    the wrapper puts on it, and the wrapper prints the bound and the exit status rather than
    leaving a silence;
  * no reduction or normal form is exposed for an infinite reflection or stabilizer subgroup:
    ``chamber_complexes`` carries chamber adjacency (``wall_root``, ``transporter``) and no
    reduction, so an orbit of a root under such a subgroup cannot be decided by enumeration
    either --- the orbit is infinite;
  * ``stabilizer_of_element`` exists on an orthogonal group, at the cost already measured in
    this repository: computations/reports/coble_TEn-gammaEn2-orbits.py, line 55, records it at
    about 2190 s per call, and its orbit enumeration over a 2048-class module never finished.

So the input item 7 needs is not a bigger search but a reduction for the stabilizer of eta_5 in
Gamma_Co,2: orbit invariants that decide equality of orbits, or a fundamental domain with a
normal form.  This record establishes that by running what exists against a stated bound.

    usage: sh computations/reports/coble_760-orbit-decision-probe.sh > ...-run.txt
"""
import sys
import time

sys.stdout.reconfigure(line_buffering=True)

from sage_extensions.all import NamedLattices, Sterk  # noqa: E402

t0 = time.time()
L = NamedLattices.TEn
print("the orbit-decision probe for #760 item 7")
print("T_En: %s" % L)
eta = Sterk.selected_isotropic_vectors()["Sterk_5"]
print("eta_5 as the library holds it: %s" % eta)
line = L.primitive_isotropic_subobject(eta)
K = line.isotropic_reduction()
print("K_5 = eta_5^perp / Z eta_5: %s (%.1f s)" % (K, time.time() - t0))
print("rank %d, determinant %s" % (K.rank(), K.determinant()))
print()
print("the orbit-deciding operations the library exposes on K_5:")
for name in ("primitive_orbit_series", "discriminant_orbit_series"):
    print("   %-26s %s" % (name, hasattr(K, name)))
print("a reduction or normal form for a subgroup:")
for name in ("fundamental_domain", "reduce", "normal_form", "orbit_invariants"):
    print("   %-26s %s" % (name, hasattr(K, name)))
print()
print("calling K.primitive_orbit_series(bound=4); the wrapper bounds it, and a bound reached")
print("without a return is the finding")
sys.stdout.flush()
t1 = time.time()
series = K.primitive_orbit_series(bound=4)
print("returned after %.1f s: %s" % (time.time() - t1, series))
print("elapsed %d s" % (time.time() - t0))
print("PYEXIT=0")
