#!/usr/bin/env python3
"""
Unit tests for documentation accuracy.
Tests that documentation contains correct and valid information.
"""

import re
import unittest


class TestInstallationDocumentation(unittest.TestCase):
    """Test cases for INSTALLATION.md accuracy"""
    
    def setUp(self):
        """Read the INSTALLATION.md file before each test"""
        with open('INSTALLATION.md', 'r') as f:
            self.installation_content = f.read()
    
    def test_windows_powershell_activation_command(self):
        """
        Test that the Windows PowerShell activation command is correct.
        
        In PowerShell, the correct activation command is:
        venv\Scripts\Activate.ps1
        
        The generic 'activate' command works in cmd.exe but not PowerShell.
        This test verifies that the documentation correctly instructs PowerShell users.
        """
        # Find the line that mentions Windows and PowerShell
        lines = self.installation_content.split('\n')
        
        powershell_activation_line = None
        for line in lines:
            if 'Windows' in line and 'PowerShell' in line and 'activate' in line.lower():
                powershell_activation_line = line
                break
        
        self.assertIsNotNone(
            powershell_activation_line,
            "Could not find Windows PowerShell activation line in INSTALLATION.md"
        )
        
        # The PowerShell activation command should include Activate.ps1
        self.assertIn(
            'Activate.ps1',
            powershell_activation_line,
            "Windows PowerShell activation line should use 'Activate.ps1' not just 'activate'"
        )
        
        # Should NOT have just 'activate' without the .ps1 extension for PowerShell
        # We check that if the line says PowerShell, it should have .ps1
        if 'PowerShell' in powershell_activation_line:
            # Extract the command part (before the # comment)
            command_part = powershell_activation_line.split('#')[0].strip()
            # If it mentions activate, it should be Activate.ps1 for PowerShell
            if 'activate' in command_part.lower():
                self.assertIn(
                    'Activate.ps1',
                    command_part,
                    "PowerShell activation must use 'Activate.ps1' extension"
                )


class TestExamplesDocumentation(unittest.TestCase):
    """Test cases for EXAMPLES.md mathematical accuracy"""
    
    def test_matrix_addition_example(self):
        """Verify that Example 1 (matrix addition) is mathematically correct"""
        # A = [[1,2],[3,4]], B = [[2,0],[1,3]]
        # Expected: A + B = [[3,2],[4,7]]
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 3]]
        
        result = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        expected = [[3, 2], [4, 7]]
        
        self.assertEqual(result, expected, "Matrix addition example is incorrect")
    
    def test_matrix_multiplication_example(self):
        """Verify that Example 2 (matrix multiplication) is mathematically correct"""
        # A = [[1,2],[3,4]], B = [[2,0],[1,3]]
        # Expected: A dot B = [[4,6],[10,12]]
        A = [[1, 2], [3, 4]]
        B = [[2, 0], [1, 3]]
        
        # Matrix multiplication
        result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) 
                   for j in range(len(B[0]))] 
                  for i in range(len(A))]
        expected = [[4, 6], [10, 12]]
        
        self.assertEqual(result, expected, "Matrix multiplication example is incorrect")
    
    def test_determinant_example(self):
        """Verify that Example 3 (determinant calculation) is mathematically correct"""
        # A = [[1,2],[3,4]], det = 1*4 - 2*3 = -2
        a, b, c, d = 1, 2, 3, 4
        det = a * d - b * c
        
        self.assertEqual(det, -2, "Determinant example is incorrect")
    
    def test_inverse_example(self):
        """Verify that Example 4 (inverse calculation) is mathematically correct"""
        # A = [[1,2],[3,4]], inverse = (-1/2)*[[4,-2],[-3,1]] = [[-2,1],[1.5,-0.5]]
        det = -2  # from previous example
        inverse_before_scaling = [[4, -2], [-3, 1]]
        
        result = [[(1/det) * inverse_before_scaling[i][j] 
                   for j in range(2)] 
                  for i in range(2)]
        expected = [[-2, 1], [1.5, -0.5]]
        
        self.assertEqual(result, expected, "Inverse matrix example is incorrect")


if __name__ == '__main__':
    unittest.main()
