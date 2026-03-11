"""
Unit tests for EXAMPLES.md - verifies all documented examples work correctly.

This test file demonstrates bugs and fixes in the matrix calculation examples.
Specifically, Example 5 should demonstrate solving a system Ax = b.
"""
import unittest


class Matrix:
    """Simple Matrix class implementation for testing."""
    
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0
    
    def __add__(self, other):
        """Matrix addition."""
        if self.shape != other.shape:
            raise ValueError("Dimension mismatch")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)
    
    def dot(self, other):
        """Matrix multiplication."""
        if self.cols != other.rows:
            raise ValueError("Incompatible dimensions for multiplication")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                val = sum(self.data[i][k] * other.data[k][j] 
                         for k in range(self.cols))
                row.append(val)
            result.append(row)
        return Matrix(result)
    
    def determinant(self):
        """Calculate determinant for 2x2 matrix."""
        if self.rows != self.cols or self.rows != 2:
            raise ValueError("Determinant only defined for 2x2 matrices")
        a, b = self.data[0]
        c, d = self.data[1]
        return a * d - b * c
    
    def inverse(self):
        """Calculate inverse for 2x2 matrix."""
        if self.rows != self.cols or self.rows != 2:
            raise ValueError("Inverse only defined for square matrices")
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is singular, cannot invert")
        a, b = self.data[0]
        c, d = self.data[1]
        scalar = 1 / det
        # Formula: (1/det) * [[d, -b], [-c, a]]
        return Matrix([[scalar*d, scalar*(-b)], 
                       [scalar*(-c), scalar*a]])
    
    @property
    def shape(self):
        return (self.rows, self.cols)
    
    def __eq__(self, other):
        """Compare matrices with small floating point tolerance."""
        if self.shape != other.shape:
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if abs(self.data[i][j] - other.data[i][j]) > 1e-10:
                    return False
        return True
    
    def __repr__(self):
        return f"Matrix({self.data})"


class TestExamples(unittest.TestCase):
    """Test all examples from EXAMPLES.md."""
    
    def test_example1_addition(self):
        """Example 1: Matrix Addition
        A = [[1,2],[3,4]]
        B = [[2,0],[1,3]]
        A + B = [[3,2],[4,7]]
        """
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[2, 0], [1, 3]])
        result = A + B
        expected = Matrix([[3, 2], [4, 7]])
        self.assertEqual(result, expected)
    
    def test_example2_multiplication(self):
        """Example 2: Matrix Multiplication
        A = [[1,2],[3,4]]
        B = [[2,0],[1,3]]
        A dot B = [[4,6],[10,12]]
        """
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[2, 0], [1, 3]])
        result = A.dot(B)
        expected = Matrix([[4, 6], [10, 12]])
        self.assertEqual(result, expected)
    
    def test_example3_determinant(self):
        """Example 3: Determinant
        For A = [[1,2],[3,4]], det = 1*4 - 2*3 = -2
        """
        A = Matrix([[1, 2], [3, 4]])
        det = A.determinant()
        self.assertEqual(det, -2)
    
    def test_example4_inverse(self):
        """Example 4: Inverse
        For A = [[1,2],[3,4]], inverse = [[-2,1],[1.5,-0.5]]
        
        Verification: A * A_inv should equal identity matrix
        """
        A = Matrix([[1, 2], [3, 4]])
        A_inv = A.inverse()
        
        # The inverse should be [[-2, 1], [1.5, -0.5]]
        expected_inv = Matrix([[-2, 1], [1.5, -0.5]])
        self.assertEqual(A_inv, expected_inv)
        
        # Verify: A * A_inv = I
        identity = A.dot(A_inv)
        expected_identity = Matrix([[1, 0], [0, 1]])
        self.assertEqual(identity, expected_identity)
    
    def test_example5_solve_system(self):
        """Example 5: Solve Ax = b using inverse
        
        THIS EXAMPLE WAS INCOMPLETE IN ORIGINAL DOCUMENTATION!
        
        A = [[2,1],[1,1]], b = [3,2]
        
        We want to solve Ax = b, where x is the solution.
        Using the method: x = A^(-1) * b
        
        Solution: x = [[1], [1]]  (i.e., x=1, y=1)
        """
        A = Matrix([[2, 1], [1, 1]])
        A_inv = A.inverse()
        
        # b as a column vector
        b = Matrix([[3], [2]])
        
        # Solve x = A^(-1) * b
        x = A_inv.dot(b)
        
        # Expected solution: x = [[1], [1]]
        expected = Matrix([[1], [1]])
        self.assertEqual(x, expected)
        
        # Verify: A * x should equal b
        verification = A.dot(x)
        self.assertEqual(verification, b)
    
    def test_example5_step_by_step_calculation(self):
        """Detailed calculation for Example 5 showing the steps.
        
        This demonstrates the bug: EXAMPLES.md did not show the solution!
        It only said "Solve using row reduction or inverse as shown in USAGE.md"
        but USAGE.md doesn't contain this information.
        """
        # A = [[2,1],[1,1]]
        # b = [3,2]
        A = Matrix([[2, 1], [1, 1]])
        
        # Calculate determinant
        det_A = A.determinant()
        self.assertEqual(det_A, 1)  # 2*1 - 1*1 = 1
        
        # Calculate inverse using formula: (1/det) * [[d, -b], [-c, a]]
        # For A = [[2,1],[1,1]]: a=2, b=1, c=1, d=1
        # A^(-1) = (1/1) * [[1, -1], [-1, 2]] = [[1, -1], [-1, 2]]
        A_inv = A.inverse()
        expected_inv = Matrix([[1, -1], [-1, 2]])
        self.assertEqual(A_inv, expected_inv)
        
        # Now solve: x = A^(-1) * b
        b = Matrix([[3], [2]])
        x = A_inv.dot(b)
        
        # x = [[1, -1], [-1, 2]] * [[3], [2]]
        #   = [[1*3 + (-1)*2], [(-1)*3 + 2*2]]
        #   = [[3-2], [-3+4]]
        #   = [[1], [1]]
        expected_x = Matrix([[1], [1]])
        self.assertEqual(x, expected_x)


if __name__ == '__main__':
    unittest.main()
