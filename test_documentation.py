"""
Unit tests for documentation correctness.

This test file verifies that the documentation contains correct commands and examples.
"""
import unittest
import re


class TestInstallationDocumentation(unittest.TestCase):
    """Test that INSTALLATION.md contains correct commands."""

    def setUp(self):
        """Read the INSTALLATION.md file."""
        with open('INSTALLATION.md', 'r') as f:
            self.installation_content = f.read()

    def test_windows_powershell_activation_command(self):
        """
        Test that the Windows PowerShell virtual environment activation
        command is correct.
        
        This test would FAIL before the patch because the documentation
        incorrectly showed 'venv\\Scripts\\activate' for PowerShell.
        
        After the patch, it passes because it correctly shows
        'venv\\Scripts\\Activate.ps1' for PowerShell.
        """
        # The documentation should mention the correct PowerShell activation script
        self.assertIn('Activate.ps1', self.installation_content,
                      "PowerShell activation script should be 'Activate.ps1'")
        
        # Check that the PowerShell comment is associated with the correct command
        lines = self.installation_content.split('\n')
        for i, line in enumerate(lines):
            if 'PowerShell' in line and 'activate' in line.lower():
                # This line should contain Activate.ps1
                self.assertIn('Activate.ps1', line,
                              f"Line mentioning PowerShell should have 'Activate.ps1': {line}")
    
    def test_windows_cmd_activation_command(self):
        """
        Test that Windows cmd activation is also documented.
        
        The documentation should include the cmd.exe activation as well.
        """
        # The documentation should mention activate.bat or just activate for cmd
        self.assertIn('activate.bat', self.installation_content,
                      "Windows cmd activation script should be mentioned")
    
    def test_all_platform_activations_present(self):
        """
        Test that all major platform activation commands are present.
        """
        # Check for macOS/Linux
        self.assertIn('source venv/bin/activate', self.installation_content,
                      "macOS/Linux activation command should be present")
        
        # Check for Windows (either cmd or PowerShell)
        has_windows_activation = (
            'venv\\Scripts\\activate' in self.installation_content or
            'venv\\Scripts\\Activate.ps1' in self.installation_content
        )
        self.assertTrue(has_windows_activation,
                       "Windows activation command should be present")


class TestExamplesDocumentation(unittest.TestCase):
    """Test that EXAMPLES.md contains correct mathematical calculations."""

    def setUp(self):
        """Read the EXAMPLES.md file."""
        with open('EXAMPLES.md', 'r') as f:
            self.examples_content = f.read()

    def test_matrix_addition_example(self):
        """Test that the matrix addition example is correct."""
        # The example shows: [[1,2],[3,4]] + [[2,0],[1,3]] = [[3,2],[4,7]]
        self.assertIn('[[3,2],[4,7]]', self.examples_content,
                      "Matrix addition result should be [[3,2],[4,7]]")

    def test_matrix_multiplication_example(self):
        """Test that the matrix multiplication example is correct."""
        # The example shows: [[1,2],[3,4]] dot [[2,0],[1,3]] = [[4,6],[10,12]]
        self.assertIn('[[4,6],[10,12]]', self.examples_content,
                      "Matrix multiplication result should be [[4,6],[10,12]]")

    def test_determinant_calculation(self):
        """Test that the determinant calculation is correct."""
        # For [[1,2],[3,4]], det = 1*4 - 2*3 = -2
        self.assertIn('= -2', self.examples_content,
                      "Determinant should be -2")


if __name__ == '__main__':
    unittest.main()
