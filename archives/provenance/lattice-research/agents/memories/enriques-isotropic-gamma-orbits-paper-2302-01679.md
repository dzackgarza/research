# Enriques Isotropic Gamma Orbits Paper 2302 01679

Paper: Dutour Sikirić and Hulek, arXiv:2302.01679, "Moduli of polarized Enriques surfaces -- computational aspects".

## Key Facts

- In the section on the Tits building, `0`- and `1`-cusps of `M_{En,h} = Gamma_h^+ \ D_N` are identified with `Gamma_h^+`-orbits of isotropic lines and isotropic planes in `N = U + U(2) + E_8(-2)`.
- For unpolarized Enriques surfaces, `O^+(N)` has two isotropic-line and two isotropic-plane orbits, with explicit representatives `L1 = Z e1`, `L2 = Z e3`, `P1 = Z e1 + Z e3`, and `P2 = Z(2e1 + 2e2 + w) + Z e3`.
- For subgroup `Gamma_h`, orbit splitting is done by double cosets: if `xG` is an ambient orbit and `G_x` its stabilizer, then `xG` decomposes into `x_i Gamma_h` corresponding to `G = union G_x h_i Gamma_h`.
- The computation reduces to a finite quotient via `U = \widetilde{O}(N)`, the kernel of the discriminant action. Because `U` is normal and `U \subset Gamma_h`, double cosets in `O(N)` reduce to double cosets in `O(N) / \widetilde{O}(N) \cong O^+(F_2^{10})`.
- The practical cusp algorithm therefore uses ambient full-group orbits, stabilizer images in the finite quotient, and finite double-coset decomposition. It does not require explicit generators of `Gamma_h` as an infinite subgroup of `O(L)`.
- `Gamma_h` is defined as `pi_N^{-1}(pi_M(O(M,h)))` and `Gamma_h^+ = Gamma_h \cap O^+(N)`.
- Table 1 case 1, the degree-2 polarization case, has `#I_1 = 5` and `#I_2 = 9`. The paper explicitly says Sterk section 4.4 proves five `0`-cusps and nine `1`-cusps for this case.
- Section 6 gives the general isotropic algorithms. Primitive isotropic vectors are handled by the `beta = 0` case using approximate models and degenerate-complement isomorphism lifting. Isotropic `k`-plane stabilizer and equivalence, and orbit enumeration by induction, are treated there as well.

## Repo Implication

- The existing Dawes backend is non-isotropic only and is not the right engine for Sterk's five-cusp claim.
- A correct `Sterk` or `Gamma_{En,2}` implementation can likely reuse ambient isotropic-line and isotropic-plane orbit enumeration plus stabilizers from Dutour code, then split orbits to `Gamma` using finite quotient or discriminant-image data and subgroup membership in that quotient.
