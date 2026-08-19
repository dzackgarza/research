# Finiteness of O(L)-Orbits of Fixed-Norm Vectors in Indefinite Lattices

## Result

For an integral lattice $L$, the number of $O(L)$-orbits of vectors of fixed norm $n$ is **finite**.

This is treated as part of the theory of representations of an integer $n$ by an indefinite quadratic form.

## Key References

### Classical (Siegel / Kitaoka)

- **Siegel's Main Theorem** on representations of integers by quadratic forms — see Schulze-Pillot (2004), especially pp. 305–306.
- **Kitaoka**, *Arithmetic of Quadratic Forms* — treatment of Siegel's theorems and representation by indefinite forms.

Key idea: for positive-definite forms, the mass-formula approach counts representations by each class in the genus, divided by automorph counts. For **indefinite** forms, one instead counts orbits under the integral orthogonal group $O(L)$, and shows each representation set splits into finitely many such orbits. This is independent of dimension.

### Quantitative / Asymptotic Results

- **Ratcliffe–Tschantz**: asymptotic formula for the Lorentzian case $Q = I_{n,1}$.
- **Lauret (2014)**: extended Ratcliffe–Tschantz to more general indefinite quadratic or Hermitian forms of signature $(n,1)$.
- **Gorodnik–Nevo**: lattice-point counting for solutions $X \in \mathbb{Z}^{(p+q) \times q}$ satisfying $I_{p,q}[X] = -L$ where $L$ is positive definite.

These ergodic/lattice-point approaches give alternative proofs of finiteness and quantitative counting results.

## Informal Summary

1. $S_n = \{v \in L : Q(v) = n\}$ is an integral quadratic-affine algebraic set.
2. The integral orthogonal group $O(L)$ acts on $S_n$.
3. Classical results (Siegel/Kitaoka) show $S_n$ decomposes into a finite union of $O(L)$-orbits.
4. Intuitively: integral solutions with bounded denominators/heights fall into finitely many arithmetic equivalence classes; reduction theory / mass formulas / arithmetic groups make this precise.
5. Modern ergodic methods (Gorodnik–Nevo, Ratcliffe–Tschantz, Lauret) give alternative proofs and quantitative counting results.

## Stack Exchange Sources

- "Orbits of automorphism group for indefinite lattices" — MathOverflow, Misha Verbitsky, 15 upvotes.
- "Upper bounds for lattice points in orbits, and representations of binary quadratic forms" — MathOverflow, Simon L. Rydin Myerson.
