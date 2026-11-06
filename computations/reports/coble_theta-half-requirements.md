# #647, the θ half: what it needs, stated as two requirements

Provider pin sage-extensions `15db925b0c92e525f769fcbf57135f1391263a9e`. This is a statement of
requirements, not a computation; the one probe below is the only run behind it.

## How the Heegner half was settled, step by step

`prop:gamma-co-heegner-strict` proves `ρ_T(Γ^Hdg_Co) = G_Co` and hence index exactly
`|W(E8)|`. Every step of it is available on the Heegner side and it is worth naming them,
because the θ side is exactly the list of what is missing:

1. `ρ_{T_Co}: O(T_Co) → O(q_{T_Co})` is onto — `thm:two-elementary-surjectivity`, which applies
   because `T_Co` is even, indefinite and 2-elementary. This is shared: the θ article needs it
   too and it holds.
2. Every isometry of `q_{T_Co}` fixes `ζ/2`, so the representation factors through
   `O(q|_{A^0})` and `A^0` is identified with the other side's discriminant group —
   `prop:coble-discriminant-group`. Shared.
3. An isometry fixing the gluing class extends over the index-two overlattice —
   `cor:liftable-automorphisms`. Shared as a technique.
4. **The image of the ambient group is the transport of the image of an integral stabilizer**:
   on the Heegner side this is the sentence of `prop:gamma-en-two-gluing` that identifies the
   image of `gent` in `O(q_{T_En})` with the `γ`-transport of the image of
   `Stab_{O(S_En)}(h)`. This is the step that turns a class of `O(q)` into an *integral*
   isometry of `T_Co` with a partner, and **it has no Coble-side counterpart on the page**.
5. An integral stabilizer whose discriminant image is nontrivial —
   `lem:polarization-stabilizer-discriminant-nontrivial`. The Coble-side analogue would be a
   nontrivial class in `ρ_{S_Co}(Stab_{O(S_Co)}(h̃_Co))`, which nobody has exhibited.

So the θ half needs **two** things, and neither is a Sage call I am allowed to invent:

- **(A) A Coble-side gluing statement**, the analogue of item 4: that the image of
  `Z_{O(Λ)}(θ_Co) ∩ Stab_{O(Λ)}(h̃_Co)` in `Orth(q_{T_Co})` is the `γ_Co`-transport of the
  image of `Stab_{O(S_Co)}(h̃_Co)`, so that a class of `O(q_{T_Co})` known to come from the
  `S_Co` side is realised by an isometry of `T_Co` that glues to it and fixes `h̃_Co`. That is
  a theorem about the Coble embedding, and it is item 1 of `@prob:group-identification`.
- **(B) Generators of that centralizer intersection**, i.e. the explicit isometries of `Λ`
  commuting with `θ_Co` and fixing `h̃_Co`. With (A) in hand this is a finite computation in
  `Orth(A_{T_Co}, q_{T_Co})`, the same shape as the one that settled #688.

## The operation, if the owner is to supply (B) rather than the page proving (A)

    centralizer_generators(ambient, involutions, fixed) -> generating set of isometries

in: a lattice `Λ` (here the K3 lattice `II_{3,19}`) with a finite list of isometries to commute
with (here `θ_Co`) and a vector to fix (here `h̃_Co`), each given as an owned isometry of `Λ`;
out: a generating set of `Z_{O(Λ)}(θ_Co) ∩ Stab_{O(Λ)}(h̃_Co)`, presented as integral
isometries of `Λ`, not as a predicate and not by enumeration;
certifies: each generator is an isometry of `Λ`, commutes with every listed involution and
fixes the listed vector — all decidable by the owner's existing validators — and completeness
by a stated index, which here would be the order of the image in `Orth(q_{T_Co})` against
`|O(q_{T_Co})| = 46 998 591 897 600`.

`O_plus` and `spinor_norm` are not the obstruction: the probe below shows the discriminant
forms of the two sides are of different orders (`1024` against `2048`) when the wrong pair is
compared, which is why the pair must be `A_{S_Co} → A_{T_Co}(-1)` and not `A_{S_En} → A_{T_Co}`.

## The probe

```
|A_T| = 2048 |A_S| = 1024
  A_S.is_isometric_to(A_T(-1))     RAISED TypeError: bad operand type for unary -: ...
  A_S.isometry_to(A_T(-1))         RAISED TypeError: bad operand type for unary -: ...
  A_S.is_isometric_to(A_T)         -> False
```

Recorded because it rules out a shortcut: the sign twist `A_T(-1)` has no expression on a
torsion form here, so an anti-isometry has to be built as an isometry to a form carrying the
negated value module, and `A_{S_En} → A_{T_Co}` is the wrong comparison in the first place —
the two sides of the Coble gluing are `A_{S_Co}` and `A_{T_Co}`, both of order 2048.
