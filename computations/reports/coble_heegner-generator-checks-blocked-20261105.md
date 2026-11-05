# B7 (#722): the proposed check cannot be set up, at the same call site as #272

One line, as agreed: **#722 reaches `_torsion_form_isometry` before its first assertion**, so it
is recorded here and skipped rather than attempted.

The proposal's first step is the discriminant image of one of the 1984 stabilizer generators.
Constructing that image is the call that dzackgarza/sage-extensions#272 breaks, on `S_En`
exactly as on `T_Co`:

```
nine reflections built: 9 | each fixes h: True
rho built: OwnedGroupMor_with_category_with_category.ArrowType
step 1 of the proposal: the discriminant image of one generator
  RAISED TypeError: TorsionFormOrthogonalGroup._element_constructor_() got an unexpected keyword argument 'check'
```

reproduced at the declared provider `sage-extensions` `6ad7a5ea` with

```
S = Lattices(ZZ)(2*(U + E8(-1)).gram())      # S_En = C(2)
gens = [S.reflection(u_0 - w_0)] + [S.reflection(a_i) for i in 1..8]
rho = S.discriminant_representation()
rho(gens[0])                                  # <- the TypeError above
```

So no `TorsionFormIsometry` exists to hand to `validate_form_preservation()`, under
`strict_checking(True)` or otherwise, and the 528-point `q`-scan it was meant to replace cannot
be compared against it either. Behind the same step sits the second recorded stop: the group
route (`discriminant_quadratic_form().orthogonal_group()`) is probe 2 of
`coble_owner_gap-blockers.sh`, which ends the interpreter in GAP. Both defects are as recorded
in `coble_owner_gap-blockers-20261105.md`; the decision the issue asks for — apply the proposal
or refuse it with the reason — is not taken here, because neither branch can be tested.
