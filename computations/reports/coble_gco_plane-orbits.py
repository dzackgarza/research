"""Orbits of G_Co on the totally singular planes of A_{S_En}, and on planes decorated by a star.

A_{S_En} = C/2C with C = U + E8(-1) and S_En = C(2).  The discriminant form is
Q(x) = (x,x)_C / 2 mod 2, with polar form beta(x, y) = (x,y)_C mod 2.  The nine generators of
G_Co are the discriminant images of the reflections of S_En in u_0 - w_0 and in the eight simple
roots of E8(2).  Each such root r has (r,r)_C = -2, so the reflection acts on C/2C as the
transvection x -> x + beta(x,r) r.

For a totally singular plane J, the quotient J^perp/J is a six-dimensional quadratic space of
plus type, and its isometry group is S_8.  A star is a set of seven nonsingular vectors of
J^perp/J that are pairwise non-orthogonal; there are eight stars, and they form the natural
S_8-set.  A star is stored as the set of the 28 elements of A_{S_En} in its seven cosets of J.

To verify the stars of the seven actual integral representatives returned by
sage-extensions workflow 43556671111, save its log to the ignored path
`.tmp/coble-public-incidence-gh.log` and execute in the Sage environment:

    sage -c 'VERIFY_PUBLIC_PLANES=True; exec(compile(open("computations/reports/coble_gco_plane-orbits.py").read(), "computations/reports/coble_gco_plane-orbits.py", "exec"))'

The optional path uses the integral primitive perpendicular quotient and its
seven norm-minus-one basis vectors; it does not infer the star from the
incidence graph. It also maps all thirteen separately returned integral flag
witnesses to their actual finite (J,star,c)-orbits. The recorded output is
coble_gco_plane-orbits-public-run.txt.
"""
import itertools

import numpy as np
from sage.all import GF, PermutationGroup, matrix as sage_matrix

E8_EDGES = [(1, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (2, 4)]
G = np.zeros((10, 10), dtype=int)
G[0, 1] = G[1, 0] = 1
for i in range(8):
    G[2 + i, 2 + i] = -2
for a, b in E8_EDGES:
    G[1 + a, 1 + b] = G[1 + b, 1 + a] = 1
VEC = np.array([[(n >> k) & 1 for k in range(10)] for n in range(1024)])
GRAM = VEC @ G @ VEC.T
Q = [int(GRAM[n, n]) // 2 % 2 for n in range(1024)]
BETA = GRAM % 2

ROOTS = [0b11] + [1 << (2 + i) for i in range(8)]
GENS = [tuple(n ^ (r if BETA[n, r] else 0) for n in range(1024)) for r in ROOTS]
for g in GENS:
    assert all(Q[g[n]] == Q[n] for n in range(1024))
    assert (BETA[np.ix_(g, g)] == BETA).all()

SINGULAR = [n for n in range(1, 1024) if Q[n] == 0]
PLANES = {frozenset((u, v, u ^ v)) for u in SINGULAR for v in SINGULAR
          if u < v and BETA[u, v] == 0 and Q[u ^ v] == 0}
print("nonzero singular vectors:", len(SINGULAR), " totally singular planes:", len(PLANES))

# An independent Schreier--Sims order computation certifies the size of the
# *generated* finite group, not just the orbit partitions of its generators.
# Restriction to the nonzero singular vectors is faithful: those vectors
# span the full 10-dimensional F_2-space (verified below), so an isometry
# acting trivially on them is the identity.
assert sage_matrix(GF(2), [VEC[n].tolist() for n in SINGULAR]).rank() == 10
singular_index = {n: i + 1 for i, n in enumerate(SINGULAR)}
generated_group = PermutationGroup([
    [singular_index[g[n]] for n in SINGULAR] for g in GENS
])
generated_order = int(generated_group.order())
assert generated_order == 696729600
print("order of nine-generator finite G_Co image:", generated_order)


def orbits(points, act):
    """The orbits of G_Co on a finite invariant set, as a list of sets."""
    remaining, result = set(points), []
    while remaining:
        start = remaining.pop()
        orbit, todo = {start}, [start]
        while todo:
            x = todo.pop()
            for g in GENS:
                y = act(g, x)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        remaining -= orbit
        result.append(orbit)
    return result


vector_orbits = orbits(SINGULAR, lambda g, x: g[x])
size_of = {x: len(o) for o in vector_orbits for x in o}
print("G_Co-orbit sizes on nonzero singular vectors:", sorted(len(o) for o in vector_orbits))

plane_orbits = orbits(PLANES, lambda g, P: frozenset(g[x] for x in P))
for o in sorted(plane_orbits, key=len):
    kinds = {tuple(sorted(size_of[x] for x in P)) for P in o}
    print(f"  plane orbit of size {len(o):5d}; vector-orbit sizes of its nonzero classes: {sorted(kinds)}")


def stars(J):
    """The eight stars of J^perp/J."""
    span = [0, *J]
    perp = [n for n in range(1024) if all(BETA[n, j] == 0 for j in J)]
    cosets = {frozenset(n ^ j for j in span) for n in perp}
    nonsingular = [c for c in cosets if Q[min(c)] == 1]
    assert len(cosets) == 64 and len(nonsingular) == 28
    meets = {a: {b for b in nonsingular if BETA[min(a), min(b)] == 1} for a in nonsingular}
    found = set()
    for a in nonsingular:
        for b in meets[a]:
            common = meets[a] & meets[b]
            star = {a, b} | {x for x in common if meets[x] & common}
            if len(star) == 7 and all(y in meets[x] for x, y in itertools.combinations(star, 2)):
                found.add(frozenset(x for c in star for x in c))
    assert len(found) == 8
    return found


decorated = {(J, s) for o in plane_orbits for J in [next(iter(o))] for s in stars(J)}
decorated_orbits = orbits(decorated, lambda g, d: (frozenset(g[x] for x in d[0]), frozenset(g[x] for x in d[1])))
flags = {(J, s, c) for (J, s) in {d for o in decorated_orbits for d in [next(iter(o))]} for c in J}
flag_orbits = orbits(flags, lambda g, f: (frozenset(g[x] for x in f[0]), frozenset(g[x] for x in f[1]), g[f[2]]))
assert sum(len(o) for o in decorated_orbits) == 8 * len(PLANES)
assert sum(len(o) for o in flag_orbits) == 24 * len(PLANES)
print("star-decorated plane orbits:", len(decorated_orbits), sorted(len(o) for o in decorated_orbits))
print("star-decorated flag orbits:", len(flag_orbits), sorted(len(o) for o in flag_orbits))
for orbit_family in (vector_orbits, plane_orbits, decorated_orbits, flag_orbits):
    assert all(generated_order % len(o) == 0 for o in orbit_family)
print("orbit-stabilizer divisibility for all four finite orbit families:", True)

# Resolve the integral orbit fibres over the five *undecorated* finite-plane
# types, rather than inferring the seven integral orbits from their total.
finite_plane_type = {J: len(o) for o in plane_orbits for J in o}
decorated_over_finite = {len(o): [] for o in plane_orbits}
for orbit in decorated_orbits:
    finite_size = finite_plane_type[next(iter(orbit))[0]]
    assert all(finite_plane_type[d[0]] == finite_size for d in orbit)
    decorated_over_finite[finite_size].append(len(orbit))
print("decorated-plane orbit sizes over each finite-plane orbit:")
for finite_size, sizes in sorted(decorated_over_finite.items()):
    sizes.sort()
    assert sum(sizes) == 8 * finite_size
    print("  finite plane size %5d: %d decorated orbits, sizes %s" %
          (finite_size, len(sizes), sizes))

# Each integral plane orbit contributes between one and three flag orbits.
# The map forgetting c is equivariant, so an entire flag orbit lies above
# exactly one decorated-plane orbit. Count its fibres without relying on
# equality of the total number of flag orbits and endpoint-incidence edges.
plane_orbit_index = {d: i for i, o in enumerate(decorated_orbits) for d in o}
flags_over_plane_orbit = {i: [] for i in range(len(decorated_orbits))}
for o in flag_orbits:
    i = plane_orbit_index[next(iter(o))[:2]]
    assert all(plane_orbit_index[f[:2]] == i for f in o)
    flags_over_plane_orbit[i].append(len(o))
print("flag orbit sizes over each decorated-plane orbit:")
for i, plane_orbit in sorted(enumerate(decorated_orbits), key=lambda t: len(t[1])):
    sizes = sorted(flags_over_plane_orbit[i])
    assert sum(sizes) == 3 * len(plane_orbit)
    print("  plane size %6d: %d flag orbits, sizes %s" % (len(plane_orbit), len(sizes), sizes))

# Endpoint incidence is the image of the flag-orbit set under the
# equivariant projection (J,s,c) -> (orbit(J,s), orbit(c)).
# Compute that image separately: equal total counts do not by themselves
# imply that the projection is injective.
incidence = {}
for orbit in flag_orbits:
    rep = next(iter(orbit))
    endpoint = (plane_orbit_index[rep[:2]], size_of[rep[2]])
    assert all((plane_orbit_index[f[:2]], size_of[f[2]]) == endpoint for f in orbit)
    incidence[endpoint] = incidence.get(endpoint, 0) + 1
print("endpoint incidence by decorated-plane orbit (vector orbit sizes):")
for i, plane_orbit in sorted(enumerate(decorated_orbits), key=lambda t: len(t[1])):
    edges = sorted((v, multiplicity) for (j, v), multiplicity in incidence.items() if j == i)
    print("  plane size %6d: %s" % (len(plane_orbit), edges))
print("endpoint edges:", len(incidence), "flag orbits:", len(flag_orbits))
assert len(incidence) == len(flag_orbits) == 13
assert all(multiplicity == 1 for multiplicity in incidence.values())

# The kernel incidence graph is not the 13-edge G_Co quotient graph. Its
# vertices are the 527 individual nonzero isotropic classes c and all 189720
# individual decorated planes (J,s); its edges are exactly c in J. Check
# both vertex degrees directly from the full finite-plane enumeration. This
# provides an independent expected degree sequence for the public kernel
# incidence operation, without pretending to return its integral witnesses.
line_degrees = {c: 0 for c in SINGULAR}
for J in PLANES:
    assert len(J) == 3
    for c in J:
        line_degrees[c] += 8
assert len(line_degrees) == 527
assert set(line_degrees.values()) == {1080}
kernel_plane_count = sum(len(o) for o in decorated_orbits)
kernel_edge_count = 3 * kernel_plane_count
assert kernel_plane_count == 189720
assert kernel_edge_count == 569160 == sum(line_degrees.values())
print("kernel incidence: line vertices %d degree %d; plane vertices %d degree 3; edges %d" %
      (len(line_degrees), next(iter(line_degrees.values())), kernel_plane_count, kernel_edge_count))

# Optional exact lift of the *public integral plane representatives* to their
# stars, not just their undecorated finite-plane types. Invoke this script
# through Sage with VERIFY_PUBLIC_PLANES=True after saving the public workflow
# log to .tmp/coble-public-incidence-gh.log. The quotient is the primitive
# negative-definite unimodular lattice P^perp/P in B=T_Co(1/2); its seven
# norm-minus-one vectors modulo sign determine the characteristic star.
if globals().get("VERIFY_PUBLIC_PLANES", False):
    import ast
    import hashlib
    import re
    from pathlib import Path

    from sage.all import ZZ, CartanMatrix, block_diagonal_matrix, identity_matrix, matrix, vector

    public_log = Path(".tmp/coble-public-incidence-gh.log").read_text()
    print("public workflow log sha256:", hashlib.sha256(public_log.encode()).hexdigest())
    public_planes = re.findall(
        r"\[Gamma_\{Co,2\}\] plane cusp (\d+): (\(\(.*?\)\))", public_log
    )
    assert len(public_planes) == 7
    B = block_diagonal_matrix(
        matrix(ZZ, [[1]]), matrix(ZZ, [[0, 1], [1, 0]]),
        -CartanMatrix(["E", 8]),
    )
    # Independently certify that each of the nine integer-coordinate
    # formulas below is a unimodular isometry of B and that its reduction
    # agrees on all 1024 classes with the finite generator used in the
    # orbit enumeration. This checks the actual homomorphism input, not
    # only its action on the seven chosen integral plane representatives.
    for generator_index, finite_reflection in enumerate(GENS):
        integral_matrix = identity_matrix(ZZ, 11)
        if generator_index == 0:
            integral_matrix[1, 1] = integral_matrix[2, 2] = 0
            integral_matrix[1, 2] = integral_matrix[2, 1] = 1
        else:
            root_index = generator_index - 1
            integral_matrix[3 + root_index, 3 + root_index] = -1
            for a, b in E8_EDGES:
                if a == generator_index:
                    integral_matrix[3 + root_index, 2 + b] = 1
                if b == generator_index:
                    integral_matrix[3 + root_index, 2 + a] = 1
        assert abs(integral_matrix.det()) == 1
        assert integral_matrix.transpose() * B * integral_matrix == B
        for n in range(1024):
            coordinates = vector(ZZ, (0, *(int((n >> k) & 1) for k in range(10))))
            image = integral_matrix * coordinates
            assert sum((int(image[k + 1]) % 2) << k for k in range(10)) == finite_reflection[n]
    print("all nine integral generator matrices preserve B and reduce to their finite actions:", True)
    finite_orbit_of = {d: len(o) for o in decorated_orbits for d in o}
    assert len(finite_orbit_of) == 8 * len(PLANES)

    def decorated_plane_of_integral_rows(p, q):
        """Canonical finite (J,star) from an integral primitive isotropic plane."""
        P = (vector(ZZ, p), vector(ZZ, q))
        K = matrix(ZZ, 2, 11, [list(B * x) for x in P]).right_kernel().basis_matrix()
        C = matrix(ZZ, 2, 9)
        for i, x in enumerate(P):
            coordinates = K.transpose().solve_right(x)
            assert all(a in ZZ for a in coordinates)
            C.set_row(i, coordinates)
        D, _, V = C.smith_form()
        assert list(D.diagonal()[:2]) == [1, 1]
        R = matrix(ZZ, V.inverse().rows()[2:])
        quotient_basis = R * K
        Qquot = quotient_basis * B * quotient_basis.transpose()
        assert Qquot.det() == -1 and Qquot.nrows() == 7
        U = (-Qquot).LLL_gram()
        assert U.transpose() * (-Qquot) * U == matrix.identity(ZZ, 7)
        negative_units = U.transpose() * quotient_basis
        assert negative_units * B * negative_units.transpose() == -matrix.identity(ZZ, 7)
        assert all(int(negative_units[t, 0]) % 2 == 1 for t in range(7))
        assert all(int(x[0]) % 2 == 0 for x in P)
        j1, j2 = (sum((int(x[k + 1]) % 2) << k for k in range(10)) for x in P)
        J = frozenset((j1, j2, j1 ^ j2))
        assert len(J) == 3 and all(Q[j] == 0 for j in J)
        span = (0, j1, j2, j1 ^ j2)
        star_masks = []
        for i in range(7):
            six_sum = sum((negative_units.row(t) for t in range(7) if t != i),
                          vector(ZZ, 11))
            assert six_sum[0] % 2 == 0
            star_masks.append(sum((int(six_sum[k + 1]) % 2) << k for k in range(10)))
        assert len(set(star_masks)) == 7
        characteristic_star = frozenset(mask ^ j for mask in star_masks for j in span)
        assert len(characteristic_star) == 28
        assert characteristic_star in stars(J)
        # Signed permutations are exactly the orthogonal norm-minus-one
        # bases of -I_7. Verify basis independence constructively, not only
        # through the abstract uniqueness of the seven norm-minus-one lines.
        altered_units = matrix(ZZ, [(-1 if t % 2 else 1) * negative_units.row(6 - t)
                                    for t in range(7)])
        assert altered_units * B * altered_units.transpose() == -matrix.identity(ZZ, 7)
        altered_masks = [sum(
            (int(sum(altered_units[t, k + 1] for t in range(7) if t != i)) % 2) << k
            for k in range(10)
        ) for i in range(7)]
        assert frozenset(mask ^ j for mask in altered_masks for j in span) == characteristic_star
        return J, characteristic_star

    print("integral public plane -> finite decorated-plane orbit size:")
    observed_sizes = {}
    for index, source in public_planes:
        p, q = ast.literal_eval(source)
        invariant = decorated_plane_of_integral_rows(p, q)
        # Changing the primitive Z-basis of the same plane must not change
        # its finite decorated-plane datum. Swap, elementary shear and sign
        # change generate GL_2(Z), so these checks exercise its generators.
        assert decorated_plane_of_integral_rows(q, p) == invariant
        assert decorated_plane_of_integral_rows(tuple(a + b for a, b in zip(p, q)), q) == invariant
        assert decorated_plane_of_integral_rows(tuple(-a for a in p), q) == invariant
        # Reflection in the norm-one generator of B=<1>+U+E8(-1)
        # negates coordinate zero and fixes the other ten. It is an
        # integral isometry congruent to the identity modulo 2B, so the
        # canonical (J,star) must be unchanged even when P itself moves.
        assert decorated_plane_of_integral_rows(
            (-p[0], *p[1:]), (-q[0], *q[1:])
        ) == invariant
        # The nine generators are the U-swap and eight E8 simple-root
        # reflections. Compare their exact integral actions with *each*
        # of the nine independently constructed finite transvections.
        for generator_index, finite_reflection in enumerate(GENS):
            reflected_p, reflected_q = list(p), list(q)
            if generator_index == 0:
                reflected_p[1], reflected_p[2] = p[2], p[1]
                reflected_q[1], reflected_q[2] = q[2], q[1]
            else:
                root_index = generator_index - 1
                adjacent = [b - 1 for a, b in E8_EDGES if a == generator_index]
                adjacent += [a - 1 for a, b in E8_EDGES if b == generator_index]
                for old, reflected in ((p, reflected_p), (q, reflected_q)):
                    reflected[3 + root_index] = (
                        -old[3 + root_index] + sum(old[3 + j] for j in adjacent)
                    )
            assert decorated_plane_of_integral_rows(reflected_p, reflected_q) == (
                frozenset(finite_reflection[x] for x in invariant[0]),
                frozenset(finite_reflection[x] for x in invariant[1]),
            )
        orbit_size = finite_orbit_of[invariant]
        assert int(index) not in observed_sizes
        observed_sizes[int(index)] = orbit_size
        print("  P%s: %d" % (index, orbit_size))
    assert set(observed_sizes) == set(range(7))
    assert sorted(observed_sizes.values()) == sorted(len(o) for o in decorated_orbits)
    print("all seven public integral planes occupy distinct finite decorated orbits:", True)
    print("canonical stars invariant under swap, shear and sign changes of all seven plane bases:", True)
    print("canonical stars invariant under discriminant-trivial positive-unit reflection:", True)
    print("canonical stars equivariant under all nine integral G_Co generators:", True)

    # The workflow returns a *separate integral flag witness* for each edge.
    # Classify that witness by its actual quotient star and divided line
    # class; this is stronger than identifying the endpoints of the edge.
    public_flags = re.findall(
        r"\[Gamma_\{Co,2\}\] edge (\d+): L(\d+) < P(\d+); line=(\(\(.*?\),\)); plane=(\(\(.*?\)\))",
        public_log,
    )
    assert len(public_flags) == 13
    public_lines = re.findall(
        r"\[Gamma_\{Co,2\}\] line cusp (\d+): (\(\(.*?\),\))", public_log
    )
    assert len(public_lines) == 4
    line_orbit_sizes = {}
    for index, source in public_lines:
        (v,) = ast.literal_eval(source)
        assert int(v[0]) % 2 == 0
        c = sum((int(v[k + 1]) % 2) << k for k in range(10))
        line_orbit_sizes[int(index)] = size_of[c]
    assert set(line_orbit_sizes) == set(range(4))
    assert sorted(line_orbit_sizes.values()) == sorted(len(o) for o in vector_orbits)
    seen_flag_orbits = set()
    print("integral public edge witness -> finite (plane,vector,flag) orbit sizes:")
    for edge, line_index, plane_index, line_source, plane_source in public_flags:
        (v,) = ast.literal_eval(line_source)
        p, q = ast.literal_eval(plane_source)
        J, characteristic_star = decorated_plane_of_integral_rows(p, q)
        c = sum((int(v[k + 1]) % 2) << k for k in range(10))
        assert int(v[0]) % 2 == 0 and c in J
        triple = (J, characteristic_star, c)
        containing_orbits = [i for i, orbit in enumerate(flag_orbits) if triple in orbit]
        assert len(containing_orbits) == 1
        flag_orbit_index = containing_orbits[0]
        assert flag_orbit_index not in seen_flag_orbits
        seen_flag_orbits.add(flag_orbit_index)
        plane_size = finite_orbit_of[(J, characteristic_star)]
        assert plane_size == observed_sizes[int(plane_index)]
        assert size_of[c] == line_orbit_sizes[int(line_index)]
        print("  edge %s L%s<P%s: (%d,%d,%d)" %
              (edge, line_index, plane_index, plane_size, size_of[c],
               len(flag_orbits[flag_orbit_index])))
    assert seen_flag_orbits == set(range(len(flag_orbits)))
    print("all thirteen public integral flag witnesses occupy distinct finite flag orbits:", True)
