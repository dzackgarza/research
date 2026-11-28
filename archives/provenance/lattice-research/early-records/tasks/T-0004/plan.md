# T-0004: plan.md

## Decomposition

### Step 1: Construct the quadratic form q_T over F_2

- Define q_T(x) = (1/2)·wt(x) mod 2Z for x ∈ F_2^11
- Isotropic condition: wt(x) ≡ 0 mod 2 (even weight)
- Verify: exactly 1024 isotropic elements

### Step 2: Construct O(q_T) as a matrix group in GAP

- O(q_T) = {g ∈ GL(11, F_2) : q_T(g·x) = q_T(x) for all x}
- Use GAP's built-in orthogonal group construction or generate from reflections
- Verify group order matches known |O^±(11, 2)|

### Step 3: Enumerate isotropic elements

- Generate all 2048 elements of F_2^11
- Filter to isotropic elements (even weight)
- Verify count = 1024

### Step 4: Compute orbits using GAP Orbits

- Apply GAP `Orbits(G, isotropic_elements, OnPoints)`
- Record: representative, orbit size, stabilizer size for each orbit
- Verify: sum of orbit sizes = 1024

### Step 5: Cross-check and certificate

- Verify each orbit representative is isotropic
- Verify each orbit element is isotropic
- Write results to output file with machine-readable format

## Delegation

- Single subagent in isolated worktree T-0004-work
- Implementation: GAP script (or Sage script calling GAP)
- SELF_CHECK: independent agent verifies output format, counts, and assertions
- ADVERSARIAL_AUDIT: independent agent attacks the O(q_T) construction and orbit
  computation

## Verification Path

- Theoretical: |O(q_T)| known from finite group theory
- Computational: GAP Orbits is exact for finite groups
- Cross-check: sum of orbit sizes must equal 1024
