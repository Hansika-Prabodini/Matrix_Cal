"""
2x2 Matrix Multiplication Module

This module provides a simple function-based interface for multiplying 2x2 matrices
using pure Python without external dependencies.
"""


def multiply(matrix_a, matrix_b):
    """
    Multiply two 2x2 matrices using nested loops.
    
    This function performs standard matrix multiplication on two 2x2 matrices
    represented as 2D lists. The result C = A × B is calculated where each element
    C[i][j] is the dot product of row i from matrix A and column j from matrix B.
    
    Args:
        matrix_a: A 2D list representing a 2x2 matrix (e.g., [[1, 2], [3, 4]])
        matrix_b: A 2D list representing a 2x2 matrix (e.g., [[5, 6], [7, 8]])
    
    Returns:
        A 2D list containing the multiplication result as a 2x2 matrix.
        
    Raises:
        TypeError: If inputs are not lists or contain non-numeric elements
        ValueError: If matrices don't have exactly 2 rows and 2 columns
    
    Example:
        >>> a = [[1, 2], [3, 4]]
        >>> b = [[5, 6], [7, 8]]
        >>> result = multiply(a, b)
        >>> print(result)
        [[19, 22], [43, 50]]
        
        Explanation:
        - result[0][0] = 1*5 + 2*7 = 5 + 14 = 19
        - result[0][1] = 1*6 + 2*8 = 6 + 16 = 22
        - result[1][0] = 3*5 + 4*7 = 15 + 28 = 43
        - result[1][1] = 3*6 + 4*8 = 18 + 32 = 50
    """
    # Validate that inputs are lists
    if not isinstance(matrix_a, list):
        raise TypeError("matrix_a must be a list")
    if not isinstance(matrix_b, list):
        raise TypeError("matrix_b must be a list")
    
    # Validate number of rows (must be exactly 2)
    if len(matrix_a) != 2:
        raise ValueError(f"matrix_a must have exactly 2 rows, got {len(matrix_a)}")
    if len(matrix_b) != 2:
        raise ValueError(f"matrix_b must have exactly 2 rows, got {len(matrix_b)}")
    
    # Validate that each row is a list and has exactly 2 columns
    for i, row in enumerate(matrix_a):
        if not isinstance(row, list):
            raise TypeError(f"matrix_a row {i} must be a list")
        if len(row) != 2:
            raise ValueError(f"matrix_a row {i} must have exactly 2 columns, got {len(row)}")
    
    for i, row in enumerate(matrix_b):
        if not isinstance(row, list):
            raise TypeError(f"matrix_b row {i} must be a list")
        if len(row) != 2:
            raise ValueError(f"matrix_b row {i} must have exactly 2 columns, got {len(row)}")
    
    # Validate that all elements are numeric
    for i in range(2):
        for j in range(2):
            if not isinstance(matrix_a[i][j], (int, float)):
                raise TypeError(f"matrix_a[{i}][{j}] must be numeric (int or float), got {type(matrix_a[i][j]).__name__}")
            if not isinstance(matrix_b[i][j], (int, float)):
                raise TypeError(f"matrix_b[{i}][{j}] must be numeric (int or float), got {type(matrix_b[i][j]).__name__}")
    
    # Perform matrix multiplication using nested loops
    result = []
    for i in range(2):
        row = []
        for j in range(2):
            # Calculate dot product of row i from matrix_a and column j from matrix_b
            value = 0
            for k in range(2):
                value += matrix_a[i][k] * matrix_b[k][j]
            row.append(value)
        result.append(row)
    
    return result


# Usage Examples
if __name__ == "__main__":
    # Example 1: Basic multiplication
    print("Example 1: Basic 2x2 matrix multiplication")
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    result = multiply(a, b)
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"A × B = {result}")
    print()
    
    # Example 2: Identity matrix multiplication
    print("Example 2: Multiplication with identity matrix")
    a = [[2, 3], [4, 5]]
    identity = [[1, 0], [0, 1]]
    result = multiply(a, identity)
    print(f"A = {a}")
    print(f"I = {identity}")
    print(f"A × I = {result}")
    print()
    
    # Example 3: Using floating point numbers
    print("Example 3: Multiplication with floating point numbers")
    a = [[1.5, 2.5], [3.5, 4.5]]
    b = [[0.5, 1.0], [1.5, 2.0]]
    result = multiply(a, b)
    print(f"A = {a}")
    print(f"B = {b}")
    print(f"A × B = {result}")
    print()
    
    # Example 4: Zero matrix
    print("Example 4: Multiplication with zero matrix")
    a = [[1, 2], [3, 4]]
    zero = [[0, 0], [0, 0]]
    result = multiply(a, zero)
    print(f"A = {a}")
    print(f"Zero = {zero}")
    print(f"A × Zero = {result}")
