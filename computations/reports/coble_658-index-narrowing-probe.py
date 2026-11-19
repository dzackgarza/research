"""research#658 item 1e: the item is an index dividing 696,729,600, not an infinite question.

LEMMA.  Assume Gamma_Co <= Gamma_{Co,2} (thm:gamma-co-2-comparison(4), conditional on conj:gamma-co-stable)
and let rho = rho_{T_Co}.  Then [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| divides
|P| = 696,729,600, and item 1e holds if and only if that index is 1.

PROOF.  Gamma_{Co,2} = rho^{-1}(P) by def:gamma-co-groups(5), so rho(Gamma_Co) <= P.  By
lem:monodromy-is-spinor-positive Gamma_Co <= O^+(T_Co), so Gamma_Co cap O~+(T_Co) = ker(rho|_{Gamma_Co})
and the first isomorphism theorem gives the index as |rho(Gamma_Co)|.  The order of P follows from the
book's two numbers -- |O(q_{T_Co})| = 46,998,591,897,600 (prop:coble-discriminant-group) and
[O(T_Co) : R_{gent}] = 2^7*17*31 = 67,456 (thm:gamma-co-2-comparison(3)) -- and the probe checks the
division and the factorizations exactly.  []

What the probe computes: 46,998,591,897,600 / 67,456 = 696,729,600 exactly, its factorization
2^14 * 3^5 * 5^2 * 7, and the factorization of 67,456 as 2^7 * 17 * 31, so the book's two numbers are
consistent with the definition of P.

Usage: python3 computations/reports/coble_658-index-narrowing-probe.py
"""

from __future__ import annotations

ORDER_OQ = 46_998_591_897_600        # |O(q_{T_Co})|, prop:coble-discriminant-group
INDEX_R = 67_456                     # [O(T_Co) : R_{gent}] = 2^7 * 17 * 31, thm:gamma-co-2-comparison(3)


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def show(n):
    return " * ".join("%d^%d" % (p, e) if e > 1 else "%d" % p for p, e in sorted(factor(n).items()))


def main():
    print("|O(q_{T_Co})| = %d  = %s   [prop:coble-discriminant-group]" % (ORDER_OQ, show(ORDER_OQ)))
    print("[O(T_Co) : R_{gent}] = %d  = %s          [thm:gamma-co-2-comparison(3)]" % (INDEX_R, show(INDEX_R)))
    assert ORDER_OQ % INDEX_R == 0
    order_p = ORDER_OQ // INDEX_R
    print("|P| = %d / %d = %d  = %s" % (ORDER_OQ, INDEX_R, order_p, show(order_p)))
    assert INDEX_R * order_p == ORDER_OQ
    assert order_p == 696_729_600
    print()
    print("|P| = |W(E_8)| = 696,729,600, which is the bound the book proves for rho(Gamma^Hdg_Co).")
    print()
    print("verdict: the lemma holds.  Item 1e is the statement that the index")
    print("  [Gamma_Co : Gamma_Co cap O~+(T_Co)] = |rho(Gamma_Co)| equals 1; it is a divisor of")
    print("  696,729,600 = 2^14 * 3^5 * 5^2 * 7, so the question is finite and, by the sign lemma,")
    print("  purely about the image of Gamma_Co in O(A_{T_Co}).")


if __name__ == "__main__":
    main()
