"""#720 (REL): the block-diagonal section, and the single membership query it leaves.

The register item (open-problems.md, item 3) asks whether
rho_{T_Co}: Gamma^cong_{Co,2} -> P = O(q_{U(2)}) x O(q_{E8(2)}) admits a section whose image
normalizes W(T_Co) and is a homomorphism modulo W(T_Co).  Normalization is automatic
(W(T_Co) is normal in Orth(T_Co)).  This record computes the order of the block-diagonal
candidate

    H_0 = <tau> x W(E_8)  inside  Orth(<2> + U(2) + E8(2)),

where tau swaps the two isotropic generators of the U(2) summand and W(E_8) acts on the E8(2)
summand and trivially on the other two.  On the discriminant blocks rho_{T_Co}(H_0) lies in
O(q_{U(2)}) x O(q_{E8(2)}), and this record shows it is all of it: the mod-2 image of W(E_8) on
E8/2E8 has order |O(q_{E8(2)})| = |W(E_8)|/2, with kernel of order 2.

So every section taken inside H_0 has its cocycle deviations in H_0 cap ker rho_{T_Co} = <-1>,
-1 being the block-diagonal -id on E8(2); and

    (REL) holds  IF  that -1 lies in W(T_Co),

which is one membership query against the missing operation recorded in
coble_rel-reflection-group-capability.py.  This is a sufficient condition and not an
equivalence: a section outside H_0 need not have its deviations in <-1>.

Run: `python3 computations/reports/coble_rel_block_diagonal_section.py` (sympy only, no
provider).  Transcript: coble_rel_block_diagonal_section-run.txt.
"""
import itertools

from sympy.combinatorics import Permutation, PermutationGroup

CARTAN = [[2, -1, 0, 0, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0, 0, 0],
          [0, -1, 2, -1, 0, 0, 0, -1], [0, 0, -1, 2, -1, 0, 0, 0],
          [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0],
          [0, 0, 0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 0, 0, 2]]
W_E8 = 696729600
O_Q_E8_2 = 348364800
O_Q_U_2 = 2


def main():
    n = 8
    vectors = [v for v in itertools.product((0, 1), repeat=n) if any(v)]
    index = {v: i for i, v in enumerate(vectors)}

    def reflect(i, v):
        b = sum(v[j] * CARTAN[j][i] for j in range(n))
        w = list(v)
        w[i] = (w[i] - b) % 2
        return tuple(w)

    gens = [Permutation([index[reflect(i, v)] for v in vectors]) for i in range(n)]
    image_order = PermutationGroup(gens).order()

    print('#720 (REL): the block-diagonal section')
    print('  |W(E_8)|                          =', W_E8)
    print('  |O(q_{E8(2)})| (register)         =', O_Q_E8_2, '=', W_E8 // 2)
    print('  |O(q_{U(2)})| (register)          =', O_Q_U_2)
    print('  order of the mod-2 image of W(E_8) =', image_order)
    print('  image = O(q_{E8(2)}):', image_order == O_Q_E8_2)
    print('  kernel order                       =', W_E8 // image_order)
    print('  |rho(H_0)| = |O(q_U(2))| * |image| =', O_Q_U_2 * image_order,
          '= |P|:', O_Q_U_2 * image_order == W_E8)
    print('')
    print('So rho(H_0) = P and H_0 cap ker rho = <-1>, and (REL) follows from')
    print('  the block-diagonal -1 on E8(2) lying in W(T_Co) --')
    print('one membership query against the missing operation, not an equivalence.')


if __name__ == '__main__':
    main()
