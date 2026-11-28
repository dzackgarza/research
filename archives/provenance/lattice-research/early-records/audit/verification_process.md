# Canonical Verification Process

**Purpose**: Prevent assigning impossible tasks by mandating research and scoping phases
before delegation.

## The Correct Verification Loop

Every verification task must follow this structure:

### Phase 0: Mathematical Validity Review (BLOCKING GATES)

**Question**: Are the concepts we're using actually defined in this setting?

**MANDATORY REQUIREMENTS** (work cannot proceed without these):

#### Gate 1: Formal Definitions

For EVERY mathematical term used:
- Provide formal definition
- State the setting where it's defined (e.g., "quadratic forms over F_2", "integral
  lattices over Z")
- Cite source (textbook, paper, theorem number)

**BLOCKING**: Cannot proceed to implementation without definitions + citations for ALL
terms.

#### Gate 2: Concept Applicability

For EVERY "invariant", "classification", or "theorem":
- State EXACTLY what mathematical structure it applies to
- Verify our setting matches that structure
- If settings don't match: REJECT and find correct approach

**Example blocking questions**:
- "Arf invariant" → What is it defined for?
  (Answer: quadratic forms over F_2)
- Our setting? (Answer: discriminant forms over Z)
- Do these match? (Answer: NO → BLOCKED)

#### Gate 3: Literature Alignment

For EVERY proposed method:
- Find literature reference for this exact problem type
- **New requirement**: Check against Pieroni (2026) and Huybrechts K3 Lectures for
  Coble/K3 lattice problems
- Cite how experts solve it
- If proposing different method: explicit justification required

**BLOCKING**: Cannot use custom methods without literature justification.

#### Gate 4: Theorem Hypothesis Verification

For EVERY theorem invoked:
- State theorem hypotheses explicitly
- Verify EACH hypothesis holds in our case
- If any hypothesis fails: REJECT theorem application

**Output**: Mathematical validity clearance with ALL definitions, citations, and
verifications documented, OR rejection with explanation

**CRITICAL**: These are COMPILER-LEVEL gates, not linter suggestions.
Work CANNOT proceed past this phase without satisfying ALL requirements.

### Phase 1: Research

**Question**: What techniques exist?
What makes this hard?
What's known in literature?

**Actions**:
- Search literature for standard techniques
- Identify what experts do for similar problems
- Understand theoretical foundations
- Document what's known vs unknown

**Output**: Research summary with citations to relevant techniques

**Pivot trigger**: If literature reveals fundamental complexity, adapt scope

### Phase 2: Scope

**Question**: Is this computationally verifiable?
What prerequisites? What bounds are justified?

**Actions**:
- Identify prerequisites (finiteness arguments, bounds, invariants)
- Determine if computational verification is feasible
- Understand what would constitute valid evidence vs proof
- Identify gaps between claim and verifiable subclaims

**Output**: Scoping document stating what CAN be verified and what prerequisites are
needed

**Pivot trigger**: If prerequisites are missing or task is impossible, pivot to
achievable subtask

### Phase 3: Method

**Question**: What approach has mathematical justification?

**Actions**:
- Choose technique with theoretical backing
- Justify any bounds or search spaces
- Identify acceptance criteria
- Document expected computational cost

**Output**: Method specification with justification

**Pivot trigger**: If no justified method exists, pivot to evidence-gathering or
literature search

### Phase 4: Plan

**Question**: How do we break this into delegable subtasks?

**Actions**:
- Decompose into concrete subtasks
- Define clear acceptance criteria for each
- Identify dependencies
- Allocate to appropriate subagent types

**Output**: Structured plan with subtasks and acceptance criteria

### Phase 5: Delegate

**Question**: Execute with proper technique

**Actions**:
- Delegate to appropriate subagent (Prover for mathematical verification)
- Provide clear context and acceptance criteria
- Include method justification in prompt

**Output**: Subagent results

### Phase 6: Audit

**Question**: Do results meet acceptance criteria?

**Actions**:
- Review subagent transcript and outputs
- Check against acceptance criteria
- Verify mathematical correctness (not just execution success)
- **Mathematical validity check**: Are concepts used correctly?
- **Literature alignment check**: Does this match how literature solves this problem?
- **Concept applicability check**: Is every "invariant" or theorem actually
  defined/applicable in this setting?
- Identify any gaps or errors
- **Reject any work that invokes undefined concepts or misapplies theorems**

**Output**: Audit report with pass/fail determination

**Mandatory rejection triggers**:
- Uses concepts not defined in this setting
- Invokes theorems that don't apply
- Proposes "invariants" without literature backing
- Mathematical reasoning is nonsensical

### Phase 7: Pivot (if needed)

**Question**: What did we learn?
How should we adapt?

**Actions**:
- If complexity discovered: revise scope, add prerequisites
- If method failed: try alternative approach
- If claim false: document counterexample
- If evidence insufficient: gather more data

**Output**: Updated plan or new research direction

**Key principle**: Pivots are EXPECTED and NORMAL when complexity is discovered.
They are not failures.

## Anti-Patterns (DO NOT DO)

❌ **Skip research phase**: "Verify this claim" → delegate immediately ❌ **Assume
feasibility**: Treat all claims as equally verifiable ❌ **Ignore prerequisites**: Assign
tasks without checking if foundations exist ❌ **Treat pivots as failures**: Rigidly
stick to original plan when complexity discovered ❌ **Confuse evidence with proof**:
Computational results are evidence, not always proof ❌ **Print without assertion**:
Report results without validating them first

## Coding Standards for Verification Scripts

**Rule: Every print statement must be immediately preceded by an assertion**

```python
# BAD - prints unvalidated result
print(f"Total isotropic elements: {len(isotropic_elements)}")

# GOOD - validates before printing
assert len(isotropic_elements) == 528, \
    f"Expected 528 isotropic elements, got {len(isotropic_elements)}"
print(f"Total isotropic elements: {len(isotropic_elements)}")
```

**Rationale**: Print statements present results as if they're verified.
Without assertions, they're just "whatever the code computed" with no validation.
Assertions force explicit checking against expected values or invariants.

**Application**: All verification scripts must validate results before reporting them.
This applies to:
- Counts (number of orbits, elements, planes)
- Structural properties (rank, signature, determinant)
- Algebraic identities (θ² = I, orthogonality)
- Numerical values (coordinates, matrix entries)

## Mandatory Reporting Standards for Subagents

When delegating verification work, subagents MUST provide:

### 1. Algorithm Description (Step-by-Step)

Every computational approach must be explained algorithmically:
```
Algorithm: Enumerate isotropic orbits in discriminant group
1. Generate all 2048 elements of A_T ≅ (ℤ/2ℤ)^11
2. For each element v, compute q_T(v) mod 2ℤ
3. Filter to isotropic elements (q_T(v) = 0)
4. Compute orbits under O(q_T) action using [specific method]
5. Count orbit sizes
```

### 2. Explicit Classification (Mandatory Labels)

Every result must be labeled as one of:

**PROOF**: Mathematically rigorous argument with theorem citations
- Must cite specific theorems/results (e.g., "By Nikulin Prop 1.5.2...")
- No bare claims allowed
- Example: "By Nikulin's surjectivity theorem (Prop 1.5.2), O(T) → O(q_T) is surjective
  when r = a, therefore all isotropic elements form one orbit under O(q_T)"

**CONJECTURE**: Claim supported by computational evidence but not proven
- Must explicitly state what's conjectured
- Must describe supporting evidence
- Example: "CONJECTURE: All 15 primitive isotropic planes lie in one O(T_Co)-orbit.
  EVIDENCE: Bounded search in [-12,12]³ found 15 planes.
  Orbit computation via GAP not yet performed."

**EVIDENCE**: Computational data supporting a claim
- Must state what claim it supports
- Must describe limitations/bounds
- Example: "EVIDENCE for finiteness: Exhaustive search in [-12,12]³ found 15 planes, no
  additional planes found in expanded search to [-20,20]³"

### 3. Investigation Triggers

Any subagent output that fails to meet these standards triggers mandatory investigation:
- ❌ Algorithm not explained step-by-step → Investigate: What did the code actually do?
- ❌ Result not labeled PROOF/CONJECTURE/EVIDENCE → Investigate: Is this proven or
  conjectured?
- ❌ "Proof" without theorem citations → Investigate: What justifies this claim?
- ❌ Bare claims (e.g., "the orbit is unique") → Investigate: Why is this true?

### 4. Delegation Template

When delegating verification work, include these requirements explicitly:

```
Task: Verify [specific claim]

Requirements:
1. Describe all algorithms step-by-step
2. Label every result as PROOF/CONJECTURE/EVIDENCE
3. For PROOF: cite specific theorems/results
4. For CONJECTURE: describe supporting evidence and limitations
5. For EVIDENCE: state what claim it supports and what bounds were used

Report back with:
- Algorithm description
- Results with explicit labels
- Justification for any PROOF claims
```

## Examples

### Good: Task 2.1 Isotropic Orbits

1. **Research**: Nikulin's theory of discriminant groups, orbit classification
2. **Scope**: Finite discriminant group (2048 elements), computationally enumerable
3. **Method**: Exhaustive enumeration + orbit computation via group action
4. **Plan**: Enumerate A_T, compute q_T, find orbits under O(q_T)
5. **Delegate**: To Prover with clear acceptance criteria
6. **Audit**: Verified 2 orbits (1 zero + 527 nonzero)
7. **Result**: ✓ PASSED

### Bad: Task 3.2 Primitive Isotropic Planes (original attempt)

1. ~~**Research**: SKIPPED~~
2. ~~**Scope**: SKIPPED~~
3. ~~**Method**: SKIPPED~~
4. **Plan**: "Verify there are 15 primitive isotropic planes"
5. **Delegate**: Assigned impossible task (enumerate infinite lattice without bounds)
6. **Audit**: Discovered task was impossible
7. **Outcome**: Planning failure, not execution failure

### Good: Task 3.2 Primitive Isotropic Planes (corrected)

1. **Research**: Study literature techniques for enumerating primitive isotropic planes
2. **Scope**: Understand finiteness argument, identify proper bounds
3. **Method**: Identify justified enumeration technique
4. **Plan**: Break into research → finiteness → enumeration subtasks
5. **Delegate**: With proper prerequisites
6. **Audit**: Verify against acceptance criteria
7. **Pivot**: If needed based on research findings

## Usage

When creating any verification plan, explicitly include all 7 phases.
Document pivots as they occur.
Treat complexity discovery as valuable information, not failure.

Reference this document in all verification plans to ensure process compliance.
