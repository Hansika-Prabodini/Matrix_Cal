# Bug Report and Fix

## Bug Found

**Location:** `EXAMPLES.md`, Example 5 (lines 24-26)

**Bug Type:** Incomplete Example / Missing Documentation

### Description

Example 5 is titled "Row reduction to solve Ax = b" but it:
1. **Does not show the actual solution** - it only gives the problem setup
2. **References non-existent documentation** - it says "Solve using row reduction or inverse as shown in `USAGE.md`" but USAGE.md does not contain instructions for solving linear systems

### Original Code (Broken)

```markdown
## Example 5 — Row reduction to solve Ax = b
A = [[2,1],[1,1]], b = [3,2]
Solve using row reduction or inverse as shown in `USAGE.md`.
```

**Problems with this:**
- The reader is left without the solution
- The reference to USAGE.md doesn't point to existing content
- The example doesn't satisfy the Tip at the end: "Include unit tests for these examples..."
- It's impossible to verify that an implementation matches this incomplete example

## Fix Applied

**Patch File:** `EXAMPLES.md` (lines 24-38)

The Example 5 has been completed with:
1. Clear steps showing how to solve using matrix inverse
2. Detailed calculation showing det(A) = 1
3. Step-by-step inverse calculation: A^(-1) = [[1,-1],[-1,2]]
4. Final solution: x = 1, y = 1
5. Verification that the solution is correct (A*x = b)

### Updated Code (Fixed)

```markdown
## Example 5 — Row reduction to solve Ax = b
A = [[2,1],[1,1]], b = [3,2]

We solve using matrix inverse: x = A^(-1) * b

Step 1: Calculate det(A) = 2*1 - 1*1 = 1
Step 2: Calculate A^(-1) using formula (1/det)*[[d,-b],[-c,a]]
        A^(-1) = (1/1)*[[1,-1],[-1,2]] = [[1,-1],[-1,2]]
Step 3: Multiply x = A^(-1) * b
        x = [[1,-1],[-1,2]] * [[3],[2]]
          = [[1*3 + (-1)*2], [(-1)*3 + 2*2]]
          = [[1], [1]]

Solution: x = 1, y = 1
Verify: A*x = [[2,1],[1,1]]*[[1],[1]] = [[3],[2]] = b ✓
```

**Benefits of this fix:**
- ✅ Shows the complete solution
- ✅ Provides step-by-step work that can be verified
- ✅ Removes misleading reference to USAGE.md
- ✅ Can now be used as a reference for implementation testing
- ✅ Follows the pattern of Examples 1-4 with complete worked solutions

## Unit Test

A comprehensive unit test file `test_examples.py` has been created that:

1. **Implements a simple Matrix class** to demonstrate the expected behavior
2. **Tests all 5 examples** with assertions
3. **Specifically validates Example 5** with detailed step-by-step verification
4. **Includes documentation** of the bug and the fix

### Test Execution

Run the tests with:
```bash
python test_examples.py
```

### What the Test Demonstrates

- Before the patch: Example 5 had no expected output to test against
- After the patch: The test can verify the solution (x=1, y=1) and that A*x=b holds true

## Summary

| Aspect | Details |
|--------|---------|
| **Bug Type** | Incomplete documentation / missing content |
| **Severity** | Medium - prevents understanding and testing of Example 5 |
| **Root Cause** | Example was left incomplete without showing the actual solution |
| **Fix Type** | Documentation patch adding complete solution steps |
| **Test Coverage** | `test_examples.py` includes test_example5_solve_system() and test_example5_step_by_step_calculation() |
| **Breaking Changes** | None - only adds missing content |
| **Backward Compatibility** | Fully compatible - enhances without removing anything |
