# Bug Fix Report

## Bug Found and Fixed

**Location:** `INSTALLATION.md`, line 11

**Bug Description:**
The documentation provided an incorrect virtual environment activation command for Windows PowerShell users.

**Original (Incorrect) Code:**
```bash
venv\Scripts\activate    # Windows (PowerShell)
```

**Fixed Code:**
```bash
venv\Scripts\Activate.ps1    # Windows (PowerShell)
```

## Why This Was a Bug

In Windows PowerShell, the virtual environment activation script has a `.ps1` extension (PowerShell script extension). The command `venv\Scripts\activate` without the extension works in Windows Command Prompt (cmd.exe), but not in PowerShell. 

When PowerShell users followed the documentation as written, they would encounter an error because:
1. PowerShell requires explicit script extensions
2. The correct activation script for PowerShell is `Activate.ps1`
3. The comment explicitly stated "(PowerShell)" but the command would only work in cmd.exe

## Impact

This bug would cause confusion and failures for users attempting to set up their Python virtual environment using PowerShell, which is the default terminal in modern Windows installations and Visual Studio Code on Windows.

## Unit Test

A comprehensive unit test suite was created in `test_documentation.py` that:

1. **Tests the bug fix specifically** - `test_windows_powershell_activation_command()`:
   - Reads INSTALLATION.md
   - Finds the Windows PowerShell activation line
   - Verifies it contains `Activate.ps1` (not just `activate`)
   - **This test would FAIL before the patch** (because the original used just `activate`)
   - **This test PASSES after the patch** (because it now uses `Activate.ps1`)

2. **Tests mathematical accuracy** - Additional tests verify that all matrix operation examples in EXAMPLES.md are mathematically correct:
   - Matrix addition (Example 1)
   - Matrix multiplication (Example 2)
   - Determinant calculation (Example 3)
   - Inverse matrix calculation (Example 4)

## Running the Tests

To verify the fix:

```bash
# Run the unit tests
python test_documentation.py

# Or with verbose output
python test_documentation.py -v
```

**Before the patch:** The `test_windows_powershell_activation_command` test would fail with an assertion error stating that 'Activate.ps1' was not found in the PowerShell activation line.

**After the patch:** All tests pass successfully, confirming that the documentation is now accurate.

## Test Output Example

```
test_determinant_example (test_documentation.TestExamplesDocumentation) ... ok
test_inverse_example (test_documentation.TestExamplesDocumentation) ... ok
test_matrix_addition_example (test_documentation.TestExamplesDocumentation) ... ok
test_matrix_multiplication_example (test_documentation.TestExamplesDocumentation) ... ok
test_windows_powershell_activation_command (test_documentation.TestInstallationDocumentation) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.001s

OK
```
