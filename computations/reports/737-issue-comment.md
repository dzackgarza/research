Intended orchestrator follow-up for research#737 (the issue connector is read-only; not posted).

The mechanism page is repaired and on main at 97b340e87a1ef19a29380a0c81fe126d6c938507 (commits
1eddea9eed, 97b340e87a on 59617433dc), one file touched:
writing/coble/computations/discriminant-form-descent.md.

The defect was cor:sign-sensitive-splitting (lines 930-944 at 4aa55b0): it quantified over
Gamma-orbits contained in a fixed-datum fibre and counted the Gamma_1-orbits in that fibre, but
Gamma need not preserve a fibre. The fibre is Orth(L)-orbit data, and the group that acts on the
fibre over D is Gamma_D = Gamma cap rho^{-1}(Stab_Q(D)); the sign refinement is taken at
Gamma_D^+ = Gamma_D cap Gamma_1. The two indices can differ, and the witness is U(2): with
D(Z e) = <[e/2]> and D(Z f) = <[f/2]> distinct, the swap exchanging them, ker rho_L = {+-id},
Gamma = Orth(L) and chi = det, the full orbit splits into two while det is trivial on the
fixed-datum subgroup {+-id}, so the fibre does not split and the old count read 1 = 0 + 0.

What is new on the page: lem:sign-kernel-orbits ([chi(A):chi(Stab_A(x))], proved by the double
coset bijection), cor:sign-sensitive-splitting restated as a full-orbit item and a fixed-datum
item with the exact preservation criterion rho(Gamma) <= Stab_Q(D) <=> Gamma_D = Gamma,
ex:sign-sensitive-splitting-u2 (the witness, with the enumeration of O(U(2)) proved on the page),
and rmk:descent-fibre-scope (which group acts where, and that the forgetting maps commute with
the reduction). thm:joint-double-coset(1) now states the A_1-orbits rather than the Gamma_1-orbits
of a fixed-datum fibre; prop:descent-inputs-enriques-coble covers primitive isotropic vectors and
routes its Coble spinor clause through thm:cusp-lifting(1)-(4) instead of a hypothesis that
theorem does not state; cor:coble-heegner-integral-plane-descent now checks
Otilde^+(T_Co) <= Gamma explicitly; [@DH23, Lemma 3.6] is [@SH23, Lemma 3.6], the key the
bibliography has, with the lemma's hypotheses read in arXiv:2302.01679v2.

Not done: no independent read of the repaired page, so #737 is not certifiable here; the same
@DH23 key remains at the-heegner-line-and-the-coble-arithmetic-group.md:2246 (another page's
text, flagged not edited); scripts/docs_check.py --source cannot run in this container because
the shared writing/.book/.assets/references.bib is absent, so no citation-key, render or
cross-reference gate was executed; CI was not observed. No numerical orbit count, no public
operation, no lattice-database card and no geometric monodromy statement is asserted by this
page, and the counts of #667, research#748, sage-extensions#294/#286 and lattice-database#7 are
untouched.

See computations/reports/737-acceptance-item-by-item.txt.
