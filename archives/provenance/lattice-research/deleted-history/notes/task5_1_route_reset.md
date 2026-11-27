# Task 5.1 route reset

This note replaces the disproved “guess two eigenspace embeddings and build θ by change
of basis” route.

## What failed

The current Task 5.1 output does **not** define an involution in `O(Λ_K3)`.

Current evidence:

- `θ^T G θ = G: False`
- `G θ = θ^T G: False`
- `V_+ ⟂ V_-: False`

So the present matrix is not a lattice isometry, even though its eigenspaces happen to
have the target signatures and determinants.

## Correct mathematical route

The route should start from the standard primitive-embedding / orthogonal-complement
picture, not from an ad hoc basis splice.

### Step 1: primitive embedding first

- Choose one target lattice, preferably `S_Co`, and construct a **primitive embedding**
  `S_Co -> Λ_K3`.
- The complement is then defined as `T := S_Co^⊥` inside `Λ_K3`.

### Step 2: complement and gluing second

- Verify that `T` has the expected rank, signature, determinant, and discriminant form.
- Use Nikulin's discriminant-form framework to confirm that the gluing data matches the
  intended `T_Co` / `S_Co` pair.

### Step 3: define θ only after the lattice decomposition is real

- Once `S` and `T=S^⊥` are genuinely orthogonal primitive sublattices of `Λ_K3`, define
  `θ` by `+1` on `T` and `-1` on `S`.
- Only then verify integrality and `θ ∈ O(Λ_K3)`.

## Role of CARAT

CARAT is **not** the main tool for the full indefinite rank-22 problem.

It may still help on reduced auxiliary subproblems, for example:

- finite positive-definite orthogonal-group searches attached to a quotient or auxiliary
  lattice;
- stabilizer / normalizer / orbit calculations after the main indefinite problem has
  been reduced to a finite exact matrix-group computation.

This matches `notes/carat_capabilities.md` and avoids treating CARAT as a black-box
solver for the whole `Λ_K3` involution problem.

## Immediate next implementation target

The next computational target is **not** “search for another θ matrix.”
That route has now been replaced by the exact glued-model implementation in
`computations/task5_1_involution.sage`, which:

- builds a primitive `S_Co -> Λ_K3` model;
- computes the true orthogonal complement;
- checks exact lattice invariants and the induced sign involution;
- verifies integrality and `θ ∈ O(Λ_K3)` on that explicit ambient lattice.

The next repo task is therefore no longer raw lattice construction.
It is to keep the repo prose and claim boundaries aligned with what this verified model
proves, while separating that exact lattice result from broader geometric claims that
still belong to the literature layer.
