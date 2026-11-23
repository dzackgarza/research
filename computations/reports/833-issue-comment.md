# research#833 — intended issue comment (not posted: the issue connector is read-only)

Landed on `main` as `1bf48f93361b9310604e1b286433f6b975589bb` (`1bf48f9336`), rebased on `3295605f2e`.

**(U2), (C4), (C5) are proved.** `writing/coble/lattices-and-moduli/integral-line-and-plane-lifting.md` now has

* `lem:o2-explicit-transversal` — for `S = <F>`, `F` finite symmetric, `rho: S -> H` into a finite group acting on a set, `W` a point, `P = Stab_H(W)`, `K = S cap rho^{-1}(P)`: the orbit `{rho(s)^{-1}W}` is a finite set of left cosets of `K`; one stored word `t_V` per state satisfies `t_V f t_{rho(f)^{-1}V}^{-1} in K` for every `f in F` and, by telescoping, these generate `K`. Nothing is lifted from the finite image except through an actual element of `S`.
* `thm:o2-congruence-family` — applied to `S = Stab_O(e_1)` with `thm:o2-line-family` and to `S = Stab_O(P_0)` with `thm:o2-plane-family`: line `|W_x| = 256`, `9728` entries, `1306` identities, `948` distinct matrices, plus `-id_B` for `Stab_{R_Gamma}(Z e_1)`; plane `|W_x| = 768`, `46080` entries, `4130` identities, `2957` distinct matrices.
* ledger: `(C4)`, `(C5)`, `(U2)` now read *proved*; the consumer table and "what is not covered" say what remains unchanged.

**Certificate** `computations/reports/coble_833-congruence-schreier.py`, with `-run.txt` and a `.json` holding the two transversals (the exact integral matrices `t_V`, indexed by the three nonzero vectors of `V`) and every family member as a `(state, generator)` pair. It records: `527` nonzero isotropic classes and `67 456` plus-type two-dimensional subspaces of `A` (the index `[O(q):P]` of `prop:gamma-co-images(3)`); the orbits of `P` on the classes, of sizes `2, 120, 270, 135`, matching `prop:coble-cong-point-stabilizer(2)`; Gram preservation and the fixed object for every input generator; the two determinant-`2` bases (`D^ev`, `K_ev`); the words in `W, A` for the standard `GL_2(Z)` generators; Gram, fixed-object and `W`-stability of all Schreier members; and the telescoping identity reproduced exactly on random elements of `K`.

**What the theorem does not claim.** The completeness of the two input families is `thm:o2-line-family` (transport of HR14 Thm 2.1) and `thm:o2-plane-family` (parabolic decomposition), not the certificate; and no monodromy group is touched — `R_Gamma = rho^{-1}(P)` is the arithmetic congruence group only.

**One point recorded rather than hidden.** `rmk:o2-which-summand`: the model `B = I_{2,9}`, `T_Co = B(2)` fixes `A_{U(2)}` only up to swapping the two hyperbolic summands, since `2K = I_{1,8}(2)` is isometric to `<2> perp E_8(2)`. With `W = <[e_1/2],[f_1/2]>` the certificate gives the four published orbit sizes with `[e_1/2]` in the two-element orbit (which is `W cap C`, i.e. `O_2 = {u_1,u_2}`); with `W' = <[e_2/2],[f_2/2]>` the same script gives `|W_x| = 17 280` for the line (its class then in the `135`-orbit) and `768` for the plane, with its own family. The construction is insensitive to the choice; the subgroup it outputs is not, so the page states which summand it names and why.

Not done: no independent review of this round yet; the issue is not closed and this comment is not posted.
