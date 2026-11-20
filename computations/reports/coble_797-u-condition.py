#!/usr/bin/env python3
"""research#797, item 3: condition (U) of Dolgachev for M = S_Co, by [@Dol96, Prop. 5.1].

Run from the repository root:
    python3 computations/reports/coble_797-u-condition.py

[@Dol96, Prop. 5.1]: for an even lattice S of signature (1,t), t <= 19, a primitive
embedding S -> L into the K3 lattice exists if

    l(A(S)) <= 20 - t   OR   t <= 10,

and it is unique up to an isometry of L if, for every prime p != 2, the p-primary
component of A(S) has length at most 19 - t, and if l(A(S)_2) = 21 - t then A(S)_2
contains the discriminant form of U(2) as a direct summand.

For S = S_Co = <2> + <-2>^10 one has t = 10 and l(A(S)) = 11, so the first disjunct
fails and the second holds; A(S) is a 2-group, so the condition at odd primes is
vacuous; l(A(S)_2) = 11 = 21 - t, so the U(2) condition is active and is checked here.

A(S_Co) = (Z/2)^11 with basis e_0 (from <2>) and e_1, ..., e_10 (from <-2>), and
q(sum a_i e_i) = a_0^2/2 - sum_{i>=1} a_i^2/2  (mod 2Z), with values in {0, 1/2, 3/2}.
"""
from fractions import Fraction
from itertools import product

N = 11


def q(a):
    return Fraction(a[0] * a[0], 2) - sum(Fraction(a[i] * a[i], 2) for i in range(1, N))


def b(a, c):
    """Bilinear form of the discriminant form, modulo 2Z."""
    return q(tuple((a[i] + c[i]) % 2 for i in range(N))) - q(a) - q(c)


def red(x):
    return x % 2


def main():
    e0 = [1] + [0] * 10
    e1 = [0, 1] + [0] * 9
    e2 = [0, 0, 1] + [0] * 8
    u = [(e0[i] + e1[i]) % 2 for i in range(N)]
    v = [(e0[i] + e2[i]) % 2 for i in range(N)]
    print("q(e_0) = %s, q(e_1) = %s   (mod 2Z)" % (red(q(e0)), red(q(e1))))
    print("q(u) = %s, q(v) = %s, b(u,v) = %s" % (red(q(u)), red(q(v)), red(b(u, v))))
    assert red(q(u)) == 0 and red(q(v)) == 0 and red(b(u, v)) == 1
    print("so <u,v> has the form q(a,b) = ab, that of A(U(2)) = (Z/2)^2")
    comp = [w for w in product(range(2), repeat=N)
            if red(b(u, w)) == 0 and red(b(v, w)) == 0]
    print("|orthogonal complement of <u,v>| = %d = 2^9" % len(comp))
    assert len(comp) == 512
    print("<u,v> is a nondegenerate orthogonal summand of A(S_Co)")
    print()
    print("existence: l(A(S)) = 11 <= 20 - t = 10 is FALSE, but t = 10 <= 10 is TRUE")
    print("uniqueness: odd p vacuous (A(S) is a 2-group); l(A(S)_2) = 11 = 21 - 10,")
    print("            and the U(2) summand is exhibited above")
    print("so [@Dol96, Prop. 5.1] gives existence, and uniqueness up to an isometry of L.")
    print("Corollary (5.2) needs t <= 9, so its non-emptiness conclusion is not available.")


if __name__ == "__main__":
    main()
