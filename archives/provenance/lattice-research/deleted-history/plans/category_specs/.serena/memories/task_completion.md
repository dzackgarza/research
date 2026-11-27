# Task Completion Workflow

Before considering a task complete, ensure the following steps are taken:

1. **Verification**:
   - Run `just smoke` to ensure basic functionality is intact.
   - Run `just test` to verify no regressions were introduced and new specifications are met.
   - Spot-check at runtime to ensure refined objects have all expected methods.

2. **Cleanup**:
   - Remove any temporary test files or debug artifacts.
   - The `just test` and `just smoke` recipes handle `.sage.py` cleanup automatically.

3. **Documentation**:
   - Update `INVENTORY.md` or `TRIAGE.md` if the task involved tracking progress on specific implementations.
   - Ensure `AGENTS.md` tasks are checked off if applicable.

4. **Git**:
   - Commit changes with a descriptive message.
   - Follow the Read -> Commit Checkpoint -> Edit -> Verify (git diff) workflow.
