# Bug Fix Documentation

## Bug Found and Fixed

**Location:** `INSTALLATION.md`, line 11

**Bug Description:**
The Windows PowerShell virtual environment activation command was incorrect. The documentation showed:
```
venv\Scripts\activate    # Windows (PowerShell)
```

However, this command is for Windows Command Prompt, NOT PowerShell. The correct PowerShell command is:
```
venv\Scripts\Activate.ps1    # Windows (PowerShell)
```

**Impact:**
Users attempting to activate a Python virtual environment on Windows using PowerShell would encounter an error or unexpected behavior if they followed the original documentation.

## The Patch

**File:** `INSTALLATION.md`

**Change:**
```diff
-   venv\Scripts\activate    # Windows (PowerShell)
+   venv\Scripts\Activate.ps1    # Windows (PowerShell)
```

## Unit Test

**File:** `test_installation_docs.py`

This test suite validates that the installation documentation contains correct commands for different platforms.

### Key Test Cases:

1. **`test_windows_powershell_activation_command`** - Verifies the correct PowerShell activation command is present
2. **`test_no_incorrect_windows_cmd_labeled_as_powershell`** - Ensures the bug doesn't exist (Command Prompt command mislabeled as PowerShell)
3. **`test_unix_activation_command_present`** - Validates Unix/Linux/macOS commands
4. **`test_activation_section_structure`** - Ensures multi-platform documentation

### Running the Test

Before the patch (with the bug):
```bash
python test_installation_docs.py
```
**Result:** FAIL - Test `test_no_incorrect_windows_cmd_labeled_as_powershell` would detect the bug

After the patch (bug fixed):
```bash
python test_installation_docs.py
```
**Result:** PASS - All tests pass

### Expected Output (After Patch):

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

## Why This Bug Matters

1. **User Experience:** New Python developers on Windows using PowerShell would be confused
2. **Platform-Specific:** Windows has multiple shells (CMD, PowerShell, PowerShell Core), each with different activation syntax
3. **Documentation Accuracy:** Technical documentation must be precise about platform-specific commands

## Additional Context

Virtual environment activation commands by platform:
- **Linux/macOS:** `source venv/bin/activate`
- **Windows Command Prompt:** `venv\Scripts\activate.bat`
- **Windows PowerShell:** `venv\Scripts\Activate.ps1`
- **Windows Git Bash:** `source venv/Scripts/activate`
