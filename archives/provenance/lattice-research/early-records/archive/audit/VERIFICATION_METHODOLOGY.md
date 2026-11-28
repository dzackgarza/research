# Verification Methodology: Separation of Duties

## The Circular Verification Problem

**INVALID**: Any single entity doing both:
1. Defining what "correct" means (writing assertions/expectations)
2. Checking if something is correct (running verification)

This is circular reasoning and proves nothing.
It's equivalent to:
- Defining your own salary and auditing yourself
- Running a restaurant and being your own health inspector
- Managing investments and being your own fiscal watchdog
- Running an insurance company and auditing your own claim approvals

## What Happened in This Repo (2026-03-30)

**Circular verification pattern that was used:**
1. Run computation script → produces output file
2. Write verification note from output file
3. Compare verification note to output file
4. Declare "VERIFIED ✓"

**Why this is worthless:** The verification note was written FROM the output, so
comparing them just checks "does my output match my output?"

**Attempted fix that was ALSO circular:**
- Delegate to Prover: "read literature, write assertions, run repo code, report
  verification"
- Still circular: same agent defines correctness AND checks correctness

## Valid Verification Requires Separation of Duties

### Option 1: Independent Implementation

- **Agent A** (blind to repo code): Read literature → implement from scratch
- **Agent B** (blind to Agent A): Run repo implementation
- **Agent C**: Compare A's results vs B's results → report discrepancies

### Option 2: Literature-Based Assertions (Separated)

- **Agent A** (blind to repo): Read literature → extract requirements → write assertions
- **Agent B** (blind to Agent A's assertions): Run repo code → report raw results
- **Agent C**: Check if B's results satisfy A's assertions

### Option 3: Formal Proof

- Use Aristotle/Lean to prove theorems from first principles
- Proof checker is independent verifier
- No circular reasoning possible

### Option 4: Literature Citation

- Find the result already proven in published papers
- Cite it properly
- No independent verification needed (trust published literature)

## What Does NOT Constitute Valid Verification

❌ **Self-auditing**: Same entity writes code and writes tests ❌ **Circular comparison**:
Compare output to documentation written from that output ❌ **Single-agent
verification**: One agent reads literature, writes assertions, runs code, reports
results ❌ **Spot-checking without independence**: Check if output "looks reasonable"
based on expectations derived from that output

## Mandatory Verification Protocol Going Forward

For any mathematical claim in this repo:

1. **Identify verification method** (Options 1-4 above)
2. **Document separation of duties**: Who defines correctness?
   Who checks it? Are they independent?
3. **Execute with blind agents**: Agents must not see both sides
4. **Report discrepancies**: Any mismatch is a FAILURE, not a "close enough"

## Reference This Document

Any time verification is discussed, reference this document:
- "Per VERIFICATION_METHODOLOGY.md, we need separation of duties"
- "This violates VERIFICATION_METHODOLOGY.md Section X"
- "Following VERIFICATION_METHODOLOGY.md Option 2..."

## Current Status (2026-03-30)

**Actually verified:**
- Task 1.1 (partial): Prover independently recomputed one sextic example

**NOT verified (circular):**
- Tasks 1.2, 1.3, 2.1, 2.2, 3.1, 3.2, 4.1, 5.1, 6.1

**In progress:**
- Aristotle formalization (project e6220c8e-83dd-4651-9c54-dd74849e692b)

## Action Items

1. Stop all circular verification immediately
2. For each unverified task, choose Option 1, 2, 3, or 4
3. Execute with proper separation of duties
4. Document which option was used and how separation was maintained
