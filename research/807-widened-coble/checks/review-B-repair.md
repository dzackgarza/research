# Review-B findings and repairs

Review-B found no substantive gap in the deformation argument but reported two write-up defects and a third inequality defect in a named input.

1. Open period embedding. MC now proves that the fixed locus U is a complex submanifold, identifies its tangent space with the (+1)-eigenspace of d(iota_0), and uses local Torelli to identify that space with the tangent space of the 9-dimensional period domain. Hence d(P|U)_0 is an isomorphism and P(U) is open. This is the fact needed for every lattice hyperplane to meet P(U) properly.
2. Definition-only citation. The incidence statement no longer attaches irreducibility to HM98 Definition (1.48). Smoothness is cited to HM98 Theorem (1.49)(1), and irreducibility of the labelled configuration manifold follows from connectedness plus smoothness. The component theorem uses that clause directly.
3. Local finiteness inequality. In prop:the-coble-locus-in-the-period-domain(1), the old displayed lower bound did not imply finiteness. The proof now uses the other half of its already stated uniform two-sided equivalence: beta(delta) <= c beta_pi(delta) = c|delta|^2. Positive-definiteness of beta and discreteness of the lattice then give finiteness on every compact set.

These repairs do not change the deformation, density or monodromy assertions. They complete the proofs on which those assertions depend. The current checks/6-proof.md contains the repairs, and the local-finiteness block is appended there for inspection.
