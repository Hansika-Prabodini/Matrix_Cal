"""
3x3 Matrix Multiplication Module

This module provides a simple function-based interface for multiplying 3x3 matrices
using pure Python without external dependencies.
"""


def multiply(matrix_a, matrix_b):
    """
    Multiply two 3x3 matrices using nested loops.
    
    This function performs standard matrix multiplication on two 3x3 matrices
    represented as 2D lists. The result C = A × B is calculated where each element
    C[i][j] is the dot product of row i from matrix A and column j from matrix B.
    
    Args:
        matrix_a: A 2D list representing a 3x3 matrix (e.g., [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        matrix_b: A 2D list representing a 3x3 matrix (e.g., [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    Returns:
        A 2D list containing the multiplication result as a 3x3 matrix.
        
    Raises:
        TypeError: If inputs are not lists or contain non-numeric elements
        ValueError: If matrices don't have exactly 3 rows and 3 columns
    
    Example:
        >>> a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        >>> result = multiply(a, b)
        >>> print(result)
        [[30, 24, 18], [84, 69, 54], [138, 114, 90]]
        
        Explanation:
        - result[0][0] = 1*9 + 2*6 + 3*3 = 9 + 12 + 9 = 30
        - result[0][1] = 1*8 + 2*5 + 3*2 = 8 + 10 + 6 = 24
        - result[0][2] = 1*7 + 2*4 + 3*1 = 7 + 8 + 3 = 18
        - result[1][0] = 4*9 + 5*6 + 6*3 = 36 + 30 + 18 = 84
        - (and so on...)
    """
    # Validate that inputs are lists
    if not isinstance(matrix_a, list):
        raise TypeError("matrix_a must be a list")
    if not isinstance(matrix_b, list):
        raise TypeError("matrix_b must be a list")
    
    # Validate number of rows (must be exactly 3)
    if len(matrix_a) != 3:
        raise ValueError(f"matrix_a must have exactly 3 rows, got {len(matrix_a)}")
    if len(matrix_b) != 3:
        raise ValueError(f"matrix_b must have exactly 3 rows, got {len(matrix_b)}")
    
    # Validate that each row is a list and has exactly 3 columns
    for i, row in enumerate(matrix_a):
        if not isinstance(row, list):
            raise TypeError(f"matrix_a row {i} must be a list")
        if len(row) != 3:
            raise ValueError(f"matrix_a row {i} must have exactly 3 columns, got {len(row)}")
    
    for i, row in enumerate(matrix_b):
        if not isinstance(row, list):
            raise TypeError(f"matrix_b row {i} must be a list")
        if len(row) != 3:
            raise ValueError(f"matrix_b row {i} must have exactly 3 columns, got {len(row)}")
    
    # Validate that all elements are numeric
    for i in range(3):
        for j in range(3):
            if not isinstance(matrix_a[i][j], (int, float)):
                raise TypeError(f"matrix_a[{i}][{j}] must be numeric (int or float), got {type(matrix_a[i][j]).__name__}")
            if not isinstance(matrix_b[i][j], (int, float)):
                raise TypeError(f"matrix_b[{i}][{j}] must be numeric (int or float), got {type(matrix_b[i][j]).__name__}")
    
    # Perform matrix multiplication using nested loops
    result = []
    for i in range(3):
        row = []
        for j in range(3):
            # Calculate dot product of row i from matrix_a and column j from matrix_b
            value = 0
            for k in range(3):
                value += matrix_a[i][k] * matrix_b[k][j]
            row.append(value)
        result.append(row)
    
    return result


# Usage Examples
if __name__ == "__main__":
    # Example 1: Basic multiplication
    print("Example 1: Basic 3x3 matrix multiplication")
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    result = multiply(a, b)
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"A × B = {result}")
    print()
    
    # Example 2: Identity matrix multiplication
    print("Example 2: Multiplication with identity matrix")
    a = [[2, 3, 4], [5, 6, 7], [8, 9, 10]]
    identity = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    result = multiply(a, identity)
    print(f"A = {a}")
    print(f"I = {identity}")
    print(f"A × I = {result}")
    print()
    
    # Example 3: Using floating point numbers
    print("Example 3: Multiplication with floating point numbers")
    a = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5], [7.5, 8.5, 9.5]]
    b = [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]
    result = multiply(a, b)
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"A × B = {result}")
    print()
    
    # Example 4: Zero matrix
    print("Example 4: Multiplication with zero matrix")
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    zero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = multiply(a, zero)
    print(f"A = {a}")
    print(f"Zero = {zero}")
    print(f"A × Zero = {result}")
