# Test Coverage Playbook

This playbook outlines the process for ensuring high-quality and comprehensive test coverage within the lattice_interface project, adhering to the standards defined in `TEST_QUALITY.md`.

## Goals

1.  **Mathematical Nontriviality:** Assertions must be mathematically nontrivial (invariants, identities, equivalence classes, exact roundtrips).
2.  **Contract-Correctness:** Use precise, contract-correct input/output types; avoid vague `Any`/`object`.
3.  **Diagnostic Clarity:** Keep assertions direct and diagnostically clear.
4.  **Oracle Assertions:** Add independent mathematical oracle assertions alongside interoperability checks.
5.  **No Masking:** Avoid `xfail`/expected-failure masking, alias-crediting/token-map coverage shortcuts, or hidden blacklist/module-prefix narrowing.

## Workflow

1.  **Identify Test Gaps:**
    *   Review `method:` tags in documentation to identify explicitly tested or triaged methods.
    *   Analyze code for methods lacking adequate test coverage.
    *   Consult `TEST_QUALITY.md` for test quality requirements.

2.  **Design Test Cases:**
    *   For each method, design test cases that cover:
        *   Valid inputs and expected outputs.
        *   Edge cases and boundary conditions.
        *   Error handling (if applicable).
        *   Mathematically nontrivial assertions (invariants, identities).
    *   Ensure test inputs and expected outputs use precise, contract-correct types.

3.  **Implement Tests:**
    *   Write tests using the project's chosen testing framework (e.g., `pytest`).
    *   Place tests in the `tests/` directory, following existing naming conventions.
    *   Implement clear and direct assertions, avoiding tuple-wrapper ceremony.
    *   Integrate independent mathematical oracle assertions where appropriate.

4.  **Run and Verify Tests:**
    *   Execute tests using `just test` or `just test-full` (for in-progress wrapper tests).
    *   For targeted testing in a Sage environment: `HOME=/tmp/sage-home conda run -n sage python -m pytest -q <path_or_test>`.
    *   Ensure all new tests pass and do not introduce regressions.
    *   Verify that no `xfail`/expected-failure masking or other coverage shortcuts are used.

5.  **Review and Refine:**
    *   Review tests for adherence to `TEST_QUALITY.md` standards.
    *   Refine test cases and assertions to improve clarity and coverage.

## Best Practices

*   **TDD Approach:** Consider using a Test-Driven Development (TDD) approach for new features.
*   **Isolation:** Ensure tests are isolated and do not depend on external state where possible.
*   **Readability:** Write clear, concise, and maintainable tests.
*   **Regular Execution:** Run tests frequently during development.
