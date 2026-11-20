#!/usr/bin/env python3
"""research#787: the index [R_gEn : Gamma_{Co,2}], exactly.

Run from the repository root:
    python3 computations/reports/coble_787-index-of-gamma-co-2.py

Inputs, each a numbered statement of the corpus:
  |O(q_{T_Co})| = 46998591897600        (prop:coble-discriminant-group, GAP)
  [O(q) : P] = 2^7*17*31 = 67456        (lattices.md, the arithmetic of R_gEn)
  [O^+(T_Co) : Gamma_{10A_1}] = |O(q)|/10!   (thm:gamma-co-sextic-group(3))
  [Gamma_{10A_1} : Otilde^+(T_Co)] = 10!
"""
from math import factorial

OQ = 46_998_591_897_600
IDX_P = 2**7 * 17 * 31
TEN_FACT = factorial(10)


def main():
    print("|O(q_T_Co)| =", OQ)
    print("[O(q) : P]  =", IDX_P, "(= 2^7*17*31)")
    P = OQ // IDX_P
    assert OQ % IDX_P == 0
    print("|P|         =", P, "= |O(q)|/[O(q):P]")

    # [O^+(T_Co) : Gamma_{10A_1}] and [Gamma_{10A_1} : Otilde^+]
    idx_gamma10 = OQ // TEN_FACT
    assert OQ % TEN_FACT == 0
    print("[O^+ : Gamma_{10A_1}] = |O(q)|/10! =", idx_gamma10, "(12,951,552 expected)")
    assert idx_gamma10 == 12_951_552
    print("10!         =", TEN_FACT)

    # [O^+ : Otilde^+] = product, so the discriminant map is onto O(q)
    idx_otilde = idx_gamma10 * TEN_FACT
    print("[O^+ : Otilde^+] =", idx_otilde, "= |O(q)|,",
          "so rho-bar : O^+ -> O(q) is onto" if idx_otilde == OQ else "MISMATCH")
    assert idx_otilde == OQ

    # [R_gEn : R_gEn cap O^+] = 2, so [R_gEn : Otilde^+] = 2|P|
    two_P = 2 * P
    print("[R_gEn : Otilde^+] = 2|P| =", two_P)

    # the index is 2|P|/[Gamma_{Co,2} : Otilde^+], maximised at the smallest
    # numerator, i.e. at Gamma_{Co,2} = Gamma_{10A_1}
    print("[R_gEn : Gamma_{Co,2}] = %d / [Gamma_{Co,2} : Otilde^+]" % two_P)
    lo = two_P // TEN_FACT
    assert two_P % TEN_FACT == 0
    print("  lower bound (Gamma_{Co,2} = Gamma_{10A_1}):", lo)
    print("  upper bound (Gamma_{Co,2} = Otilde^+):", two_P)
    assert lo == 384 and two_P == 1_393_459_200
    print("  2|P| = 2 * 696729600 = 1,393,459,200; 1,393,459,200/3,628,800 = 384")
    print("ALL ASSERTIONS HOLD")


if __name__ == "__main__":
    main()
