# Mathematical Code Refactoring Guidelines

When refactoring or modifying mathematical code, strictly adhere to the following operational guidelines to ensure perfect algorithmic fidelity.

## 1. Algorithmic Preservation
- **Do not invent or intuitively rewrite algorithms**: Mathematical correctness takes absolute precedence over code elegance or performance.
- **Copy exactly**: Preserve the exact computational steps, underlying logic, and mathematical libraries of the original implementation. Do not attempt to "optimize" or "simplify" the mathematics.
- **Complete Feature Preservation**: Do not stub out advanced or lesser-used methods (e.g., using `NotImplementedError`, `pass`, or `TODO`) while only implementing core functionalities. All original mathematical functionality must remain fully operational.

## 2. Mandatory Verification Workflow
Before claiming completion on any mathematical refactoring, you must systematically execute the following steps:

1. **Extract Original Code First**: Use tools (`grep`, `rg`, `probe search`) to locate and extract the precise original implementations before writing any new code.
2. **Sequential Verification**: Use `mcp__sequential__sequentialthinking` to document your comparison strategy for every method line-by-line.
3. **Line-by-Line Comparison**: Systematically compare the refactored code against the original using diff tools to identify any deviations:
   ```bash
   diff -u <(probe search "def method_name" original.py) \
           <(probe search "def method_name" refactored.py)
   ```
4. **External Audit**: Use `mcp__zen__codereview` to verify algorithmic fidelity. Always start with `confidence="low"` or `"exploring"` for mathematical code. Look specifically for missing operations or library substitutions.
5. **Challenge Assumptions**: Use `mcp__zen__challenge` when any algorithmic difference is found, or to actively challenge the assumption that your new implementation is flawless.

## 3. Error Handling and Escalation
- **Assume User Correctness**: If a user reports mathematical errors, immediately assume the refactored implementation introduced an algorithmic deviation.
- **Immediate Reversion**: Stop coding, use `mcp__zen__debug` or sequential thinking to find where algorithms were rewritten, and replace the modified code with the original logic. 
- **No Iterative Patching**: Do not attempt to iteratively patch an altered algorithm; restore its original mathematical logic first.