"""
Unit tests for documentation content validation.

This test suite ensures that documentation provides correct information,
particularly for platform-specific commands.
"""

import re


def test_windows_powershell_venv_activation_command():
    """
    Test that INSTALLATION.md provides the correct venv activation command for Windows PowerShell.
    
    This test would FAIL before the patch because the documentation incorrectly showed:
        venv\Scripts\activate    # Windows (PowerShell)
    
    which is the Command Prompt activation script, not PowerShell.
    
    After the patch, the documentation correctly shows:
        venv\Scripts\Activate.ps1     # Windows (PowerShell)
    """
    with open('INSTALLATION.md', 'r') as f:
        content = f.read()
    
    # Check that PowerShell activation command is correct
    # The correct PowerShell command should end with .ps1
    powershell_pattern = r'venv\\Scripts\\Activate\.ps1\s+#.*Windows.*PowerShell'
    
    assert re.search(powershell_pattern, content, re.IGNORECASE), \
        "INSTALLATION.md must contain the correct PowerShell activation command (venv\\Scripts\\Activate.ps1)"
    
    # Also verify that Command Prompt activation is documented separately
    cmd_pattern = r'venv\\Scripts\\activate\.bat\s+#.*Windows.*Command Prompt'
    
    assert re.search(cmd_pattern, content, re.IGNORECASE), \
        "INSTALLATION.md should also document the Command Prompt activation command (venv\\Scripts\\activate.bat)"


def test_windows_activation_commands_are_distinct():
    """
    Test that Windows PowerShell and Command Prompt activation commands are documented as separate entries.
    
    Before the patch, only one Windows command was shown with an incorrect label.
    After the patch, both Windows activation methods are properly documented.
    """
    with open('INSTALLATION.md', 'r') as f:
        content = f.read()
    
    # Count occurrences of Windows-related activation commands
    windows_commands = re.findall(r'venv\\Scripts\\[Aa]ctivate[^#]*#.*Windows', content)
    
    assert len(windows_commands) >= 2, \
        f"Expected at least 2 Windows activation commands (PowerShell and Command Prompt), found {len(windows_commands)}"


def test_macos_linux_activation_unchanged():
    """
    Test that macOS/Linux activation command remains correct.
    
    This ensures the bug fix didn't inadvertently change the correct Unix activation command.
    """
    with open('INSTALLATION.md', 'r') as f:
        content = f.read()
    
    # Check that Unix activation command is present and correct
    unix_pattern = r'source venv/bin/activate\s+#.*(?:macOS|Linux)'
    
    assert re.search(unix_pattern, content, re.IGNORECASE), \
        "INSTALLATION.md must contain the correct macOS/Linux activation command (source venv/bin/activate)"


if __name__ == '__main__':
    # Run tests
    print("Running documentation validation tests...")
    
    try:
        test_windows_powershell_venv_activation_command()
        print("✓ test_windows_powershell_venv_activation_command PASSED")
    except AssertionError as e:
        print(f"✗ test_windows_powershell_venv_activation_command FAILED: {e}")
    
    try:
        test_windows_activation_commands_are_distinct()
        print("✓ test_windows_activation_commands_are_distinct PASSED")
    except AssertionError as e:
        print(f"✗ test_windows_activation_commands_are_distinct FAILED: {e}")
    
    try:
        test_macos_linux_activation_unchanged()
        print("✓ test_macos_linux_activation_unchanged PASSED")
    except AssertionError as e:
        print(f"✗ test_macos_linux_activation_unchanged FAILED: {e}")
    
    print("\nAll tests completed!")
