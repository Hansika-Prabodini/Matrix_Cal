"""
Unit tests for validating INSTALLATION.md documentation correctness.

This test suite ensures that the installation instructions contain
correct commands for different platforms, particularly for virtual
environment activation.
"""

import unittest
import re


class TestInstallationDocumentation(unittest.TestCase):
    """Test suite for INSTALLATION.md documentation validation."""
    
    def setUp(self):
        """Load the INSTALLATION.md file for testing."""
        with open('INSTALLATION.md', 'r') as f:
            self.installation_content = f.read()
    
    def test_windows_powershell_activation_command(self):
        """
        Test that Windows PowerShell activation command is correct.
        
        This test would FAIL before the patch because the old command was:
            venv\Scripts\activate    # Windows (PowerShell)
        
        The correct PowerShell command should be:
            venv\Scripts\Activate.ps1    # Windows (PowerShell)
        
        Note: venv\Scripts\activate is for Command Prompt, not PowerShell.
        """
        # Look for the Windows PowerShell activation line
        powershell_pattern = r'venv\\Scripts\\Activate\.ps1\s*#.*Windows.*PowerShell'
        
        self.assertIsNotNone(
            re.search(powershell_pattern, self.installation_content),
            "Windows PowerShell activation command should be 'venv\\Scripts\\Activate.ps1', not 'venv\\Scripts\\activate'"
        )
    
    def test_unix_activation_command_present(self):
        """Test that Unix/Linux/macOS activation command is present and correct."""
        unix_pattern = r'source venv/bin/activate\s*#.*macOS.*Linux'
        
        self.assertIsNotNone(
            re.search(unix_pattern, self.installation_content),
            "Unix/Linux/macOS activation command should be 'source venv/bin/activate'"
        )
    
    def test_no_incorrect_windows_cmd_labeled_as_powershell(self):
        """
        Test that we don't have the incorrect Command Prompt command 
        labeled as PowerShell command.
        
        This specifically catches the bug where 'venv\Scripts\activate' 
        (which is for Command Prompt) was incorrectly labeled as PowerShell.
        """
        # This pattern matches the INCORRECT combination that was the bug
        incorrect_pattern = r'venv\\Scripts\\activate\s*#.*Windows.*PowerShell'
        
        self.assertIsNone(
            re.search(incorrect_pattern, self.installation_content),
            "Bug detected: 'venv\\Scripts\\activate' is for Command Prompt, not PowerShell. "
            "PowerShell requires 'venv\\Scripts\\Activate.ps1'"
        )
    
    def test_python_venv_creation_command(self):
        """Test that Python virtual environment creation command is present."""
        self.assertIn(
            'python -m venv venv',
            self.installation_content,
            "Python venv creation command should be present"
        )
    
    def test_activation_section_structure(self):
        """Test that the activation section has commands for multiple platforms."""
        # Should contain references to different platforms
        self.assertIn('macOS', self.installation_content)
        self.assertIn('Linux', self.installation_content)
        self.assertIn('Windows', self.installation_content)
        self.assertIn('PowerShell', self.installation_content)


class TestInstallationCommandsValidation(unittest.TestCase):
    """Additional tests to validate other installation commands."""
    
    def setUp(self):
        """Load the INSTALLATION.md file for testing."""
        with open('INSTALLATION.md', 'r') as f:
            self.installation_content = f.read()
    
    def test_pip_install_example_present(self):
        """Test that pip install example is present."""
        self.assertIn('pip install', self.installation_content)
    
    def test_npm_install_example_present(self):
        """Test that npm install example is present for Node.js option."""
        self.assertIn('npm install', self.installation_content)
    
    def test_multiple_installation_options(self):
        """Test that multiple installation options are documented."""
        self.assertIn('Option A', self.installation_content)
        self.assertIn('Option B', self.installation_content)


if __name__ == '__main__':
    unittest.main()
