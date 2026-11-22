# Review-C finding and repair

The first Review-C submission was rejected for one false display and three loose citations. The submission otherwise found no substantive gap in Dolgachev–Zhang scope or monodromy separation.

1. False display, MC step 3 of thm:coble-smooth-antibicanonical-is-a-plane-blowup. Old: -2K_S=-2pi^*K_Y-2E=pi^*(-2K_Y). Repaired to -2K_S=pi^*(-2K_Y)-2E, equivalently -2K_S+2E=pi^*(-2K_Y). Since pi_*E=0, C_Y=pi_*C still lies in |-2K_Y|. The subsequent arithmetic genus and section calculations already used the corrected C+2E form.
2. Halphen plane model. The clause now cites DZ99 §5.1, whose Halphen pencil and ten-nodal irreducible member are the actual plane-model statement, rather than Theorem 2.5's abstract surface-structure theorem.
3. Node/cusp proof. The reliance on DZ99 Remark 3.3 is removed. The page's own step 5 gives mult_p Z=C·E=2. Two points of C∩E give two smooth branches with distinct tangents (an ordinary node). One point with intersection multiplicity two gives an ordinary cusp; a higher A_{2k}, k>1, would remain singular after one blow-up.
4. n>1 lattice rank. The disjoint n components have total square -4n=4K_S^2, hence K_S^2=-n and the invariant rank is b_2(S)=10-K_S^2=10+n. This is now stated separately from the n=1 type (11,11,1), cited to DK13 §3. DZ99 Proposition 6.4(2) is used only for the divisor structure it actually supplies.

The false identity did not affect any downstream conclusion. The other three repairs replace weak citations with the actual supporting argument. This repaired page is the one supplied in checks/6-proof.md to the remaining reviewers and to Review-C for its recheck.
