#!/usr/bin/env python3
"""The index comparison that answers research#797's question about Gamma_{Co,2}.

Question (qst:coble-monodromy-equality): is Gamma_{Co,2} = R_gent cap O^+(T_Co)?

The answer is no, and no computation of orbits is needed: the volume already
carries two indices in O^+(T_Co),

    [O^+(T_Co) : R_gent cap O^+(T_Co)] = [O(q_{T_Co}) : P]   (prop:gamma-co-images(3))
    [O^+(T_Co) : Gamma_{10A_1}]        = |O(q_{T_Co})| / 10!  (thm:gamma-co-sextic-group(3))

and the containment Gamma_{Co,2} <= Gamma_{10A_1} (prop:d2b-index-exact(3)).
If the equality held, R_gent cap O^+(T_Co) would be contained in Gamma_{10A_1},
and a subgroup of index 67 456 cannot be contained in one of index 12 951 552.

Every number below is derived from the two published orders
    |O(q_{T_Co})| = 46 998 591 897 600      (computations/reports/coble_orthogonal_group_orders.g)
    [O(q_{T_Co}) : P] = 2^7*17*31 = 67 456  (prop:gamma-co-images(3))
and from 10! = |Theta| (thm:gamma-co-sextic-group(1)).
"""
from math import factorial

OQ = 46_998_591_897_600          # |O(q_{T_Co})|, the GAP record coble_orthogonal_group_orders.g
INDEX_P = 2**7 * 17 * 31         # [O(q) : P], prop:gamma-co-images(3)
TEN = factorial(10)              # |Theta| = 10!, thm:gamma-co-sextic-group(1)
INDEX_10A1 = OQ // TEN           # [O^+ : Gamma_{10A1}], thm:gamma-co-sextic-group(3)

assert INDEX_P == 67_456, INDEX_P
assert TEN == 3_628_800, TEN
assert OQ % INDEX_P == 0 and OQ % TEN == 0
P = OQ // INDEX_P                # |P| = [R_gent cap O^+ : Otilde^+]
assert P == 696_729_600, P
assert INDEX_10A1 == 2**13 * 3 * 17 * 31 == 12_951_552, INDEX_10A1

print(f"|O(q_Tco)|                   = {OQ}")
print(f"[O(q):P] = 2^7*17*31        = {INDEX_P}   (index of R_gent cap O^+ in O^+)")
print(f"|P| = |O(q)|/[O(q):P]       = {P}   (= [R_gent cap O^+ : Otilde^+])")
print(f"|Theta| = 10!               = {TEN}")
print(f"[O^+:Gamma_10A1] = |O(q)|/10! = {INDEX_10A1} = 2^13*3*17*31")
print(f"ratio |P|/10!               = {P // TEN}   (exact: {P % TEN == 0})")
print()
# The two orders, and the containment that the equality would force.
print("The refutation:  Gamma_{Co,2} <= Gamma_10A1  (prop:d2b-index-exact(3)).")
print("If Gamma_{Co,2} = R_gent cap O^+, then R_gent cap O^+ <= Gamma_10A1.")
print("For subgroups of a group, A <= B implies [G:B] <= [G:A]; here that would give")
print(f"    [O^+:Gamma_10A1] = {INDEX_10A1}  <=  [O^+:R_gent cap O^+] = {INDEX_P},")
print(f"which is {'FALSE' if INDEX_10A1 > INDEX_P else 'true'}: {INDEX_10A1} > {INDEX_P}.")
assert INDEX_10A1 > INDEX_P
print("Hence R_gent cap O^+ is NOT contained in Gamma_10A1, and the equality is false.")
print()
print("The sharpened index, under (U) (Gamma_{Co,2} <= R_gent cap O^+):")
print(f"    [R_gent cap O^+ : Gamma_{{Co,2}}] >= |P|/|Theta| = {P // TEN}")
assert P // TEN == 192 and P % TEN == 0
print(f"    and [R_gent : Gamma_{{Co,2}}] >= 2*{P // TEN} = {2 * (P // TEN)}")
print()
print("Coincidence worth recording: |P| = 696 729 600 = |W(E_8)|.")
