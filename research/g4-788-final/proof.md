# Status

PROVED #2. The argument was checked by: model. Finite computations were also independently recomputed. See `ledger gate research/g4-788-final` for the exact entries.

# Result

For the even indefinite 2-elementary lattice T_Co = <h> + E_10(2), h^2 = 2, and delta = tilde-e - tilde-f in T_En = U + E_10(2):

1. Every phi in O(T_Co) extends uniquely to phi oplus id_delta in O(T_En) fixing delta.
2. The image R_gent of Stab_{Gamma_{En,2}}(delta) under restriction is bar-rho^{-1}(P), for P the stabilizer of the decomposition [h/2]^perp = A_U(2) + A_E8(2).
3. [O(T_Co):R_gent] = [O(q_TCo):P] = 2^7*17*31 = 67456.

The stable restricted stabilizer is Otilde^+(T_Co). The B2 and G5 citation uses are correct after distinguishing Stab_gent(delta) from its restriction image R. No geometric monodromy equality is asserted or used.

# Argument and evidence

The glue H = <(h/2,delta/2)> is even and isotropic, and (h+delta)/2 = tilde-e. The quotient H^perp/H has unique representatives (0,y,0), giving an isometry kappa from A_E10(2). The common dual representatives prove kappa intertwines the discriminant actions.

On the discriminant group, 2-elementarity makes q mod 1 linear. The three explicit blocks give the unique characteristic class w=[h/2], fixed by every discriminant isometry; their pairings prove nondegeneracy. Nikulin Corollary 1.5.2 therefore gives the unique extension. AEGS Definition 2.6 and Sterk Proposition 2.7 identify the degree-two arithmetic group; kappa transfers its summand condition to P.

The ten-dimensional finite quadratic space has 528 singular and 496 nonsingular classes. There are 527*256/2 = 67456 hyperbolic decompositions. Ordered hyperbolic bases independently give |O(q_TCo)| = 46998591897600 and |P| = 696729600, hence the same quotient. The orbit fills the independently counted set, and Nikulin Theorem 3.6.3 transfers the index to the lattice.

The new exhaustive check `checks/independent-finite-check.py` confirms these finite claims, every complement's plus type, the characteristic identity on all 2048 classes, and |H^perp/H|=1024. Eight independently directed Kimi reviews were read and checked, not accepted by vote.

# Primary sources read

- Nikulin, Proposition 1.5.1 and Corollary 1.5.2 (printed p.111): primitive gluing and compatible extension.
- Nikulin, Theorem 3.6.2 (printed p.144): even indefinite 2-elementary classification; signature (2,9), a=11, coparity 1.
- Nikulin, Theorem 3.6.3 (statement p.144, proof p.145): discriminant surjectivity for the same hypotheses.
- Nikulin, Section 3.9 (printed pp.149-150), read as source context; the final page proof derives the characteristic class directly instead of relying on a section-level citation.
- Nikulin, Theorem 1.14.4 (printed p.126): primitive-embedding uniqueness, not used for extension. Its AEGS Lemma 2.4 application satisfies all hypotheses; the exceptional 2-primary condition is vacuous because 12 != ell(A_{M_2})=10.
- AEGS, Definition 2.6 (printed p.587) and Lemma 2.4 (p.586).
- Sterk, Proposition 2.7 (printed p.6, proof p.7) and Remark 2.12 (p.8).

Printed pages are review evidence only and were not added to repository citations.

# Repairs

- Replaced the malformed Nikulin `Section 3.9--150` locators with direct proofs of nondegeneracy and the characteristic class; numbered the unused Theorem 1.14.4 citation correctly.
- Corrected B2's false literal inclusion R <= gent and its double-coset notation. The Enriques stabilizer acts on tilde-Y_k; its restriction image R acts on Y_k.

# Checks and skipped checks

- Independent finite program: exit 0; complete output at `checks/independent-finite-check-output.txt`.
- `pandoc` parsed both edited pages successfully.
- `scripts/docs_check.py --source` reported 29 missing-bibliography findings, all pre-existing and on untouched material; none concerns the edited proof/consumer citations.
- `tests/engineering/test_coble_788_arithmetic_group_naming.py`: 11/12. The sole failure is the pre-existing wording assertion `test_no_page_asserts_non_membership_that_is_the_open_question` on unchanged `ksba.md`, not a regression from these edits.
- One-page Quarto renders were not run: `just`, `uvx`, and `quarto` are unavailable. No full-book build or CI result is claimed.
- Lean was skipped: there is no Lean statement of this result and none was requested. The engineering/Sage suite was not run.

# Boundary

This proves arithmetic G4 and its citation obligation only. It does not prove G5, identify a geometric monodromy group, or decide any quotient's cusp counts for a monodromy group rather than R_gent.
