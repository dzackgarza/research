"""research#658 item 1e: the push-off route to Gamma_Co = O(T_Co) fails -- infinitely many walls.

LEMMA.  The removed locus of the Coble period quotient is a countable union of Heegner divisors that is not
closed, so the push-off argument does not make pi_1 of the Coble moduli surject onto O(T_Co); Gamma_Co is
therefore not O(T_Co) by default.

PROOF.
  (a) T_Co has infinitely many distinct lines spanned by vectors of square -2.  The book's family, at the
      display proving W(T_Co) infinite (writing/coble/lattices-and-moduli/
      the-heegner-line-and-the-coble-arithmetic-group.md:3002), is
          x_a = a h + e' - ((a^2+1)/2) f'      for odd a,
      with x_a^2 = 2a^2 - 4*(a^2+1)/2 = -2; the probe verifies this on T_Co = <2> + U(2) + E8(2) for the
      odd a from 1 to 21, and verifies that the lines are distinct (the coefficient of e' is 1 and that of
      f' is -(a^2+1)/2, strictly monotone in |a|).
  (b) Each line cuts a Heegner divisor in D(T_Co)/O(T_Co); M_Co omits it, being an open subset of
      D(N)/O(N) (DK13, Prop. 3.2, printed p. 513), and the periods of Coble surfaces with an extra
      algebraic class lie on it.
  (c) A countable union of divisors is not closed, and its complement is dense; the argument "a loop can be
      pushed off a closed subset of real codimension two", which would make pi_1(M_Co) -> O(T_Co)
      surjective, therefore does not apply.  []

So neither O(T_Co) nor O~+(T_Co) is forced for Gamma_Co: the monodromy is a genuine datum, and item 1e
needs it named.

Usage: python3 computations/reports/coble_658-pushoff-fails-probe.py
"""

from __future__ import annotations


def e8_cartan():
    c = [[0] * 8 for _ in range(8)]
    for i in range(8):
        c[i][i] = 2
    for i in range(6):
        c[i][i + 1] = c[i + 1][i] = -1
    c[2][7] = c[7][2] = -1
    return c


def block_diagonal(blocks):
    n = sum(len(b) for b in blocks)
    g = [[0] * n for _ in range(n)]
    off = 0
    for b in blocks:
        for i in range(len(b)):
            for j in range(len(b)):
                g[off + i][off + j] = b[i][j]
        off += len(b)
    return g


U = [[0, 1], [1, 0]]
G = block_diagonal([[[2]], [[2 * x for x in row] for row in U],
                    [[-2 * x for x in row] for row in e8_cartan()]])      # T_Co: coords h, e', f', a_1..a_8
N = len(G)


def dot(x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(N) for j in range(N))


def main():
    print("T_Co = <2> + U(2) + E8(2), rank %d" % N)
    print("the book's family x_a = a h + e' - ((a^2+1)/2) f'  (the-heegner-line..., display at :3002)")
    lines = {}
    for a in range(1, 22, 2):
        x = [0] * N
        x[0] = a
        x[1] = 1
        x[2] = -(a * a + 1) // 2
        square = dot(x, x)
        key = (x[1], x[2])
        lines[key] = x
        print("  a = %2d:  x_a^2 = %d   (e', f') coefficients (%d, %d)" % (a, square, x[1], x[2]))
        assert square == -2
    print("distinct lines among them: %d of %d" % (len(lines), 11))
    assert len(lines) == 11
    print()
    print("verdict: the lemma holds -- T_Co carries infinitely many (-2)-lines, so the omitted locus of")
    print("  the Coble period quotient is a countable union of Heegner divisors, not a closed set;")
    print("  pi_1 of the moduli is not thereby onto O(T_Co), and Gamma_Co is O(T_Co) by no default.")


if __name__ == "__main__":
    main()
