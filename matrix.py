"""
Matrix Calculation Library

This module provides a Matrix class for basic matrix operations including
addition, subtraction, and multiplication with proper error handling.
"""


class DimensionError(Exception):
    """Exception raised for dimension mismatch errors in matrix operations."""
    pass


class Matrix:
    """
    A class representing a mathematical matrix with basic operations.
    
    The Matrix class supports:
    - Matrix addition and subtraction (same dimensions)
    - Matrix multiplication (compatible dimensions)
    - String representation for display
    """
    
    def __init__(self, data):
        """
        Initialize a Matrix from a 2D list.
        
        Args:
            data: A 2D list where each inner list represents a row
            
        Raises:
            ValueError: If input is empty or not rectangular
        """
        if not data:
            raise ValueError("Matrix data cannot be empty")
        
        if not all(isinstance(row, list) for row in data):
            raise ValueError("Matrix data must be a list of lists")
        
        if not data[0]:
            raise ValueError("Matrix rows cannot be empty")
        
        # Validate rectangular structure
        first_row_length = len(data[0])
        if not all(len(row) == first_row_length for row in data):
            raise ValueError("Matrix must be rectangular (all rows same length)")
        
        # Store data as a list of lists (copy to avoid external modification)
        self._data = [row[:] for row in data]
        self._rows = len(data)
        self._cols = first_row_length
    
    @property
    def rows(self):
        """Return the number of rows in the matrix."""
        return self._rows
    
    @property
    def cols(self):
        """Return the number of columns in the matrix."""
        return self._cols
    
    def __add__(self, other):
        """
        Add two matrices element-wise.
        
        Args:
            other: Another Matrix instance
            
        Returns:
            A new Matrix representing the sum
            
        Raises:
            DimensionError: If matrices have different dimensions
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only add Matrix to Matrix")
        
        if self.rows != other.rows or self.cols != other.cols:
            raise DimensionError(
                f"Cannot add matrices with dimensions ({self.rows}x{self.cols}) "
                f"and ({other.rows}x{other.cols})"
            )
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self._data[i][j] + other._data[i][j])
            result.append(row)
        
        return Matrix(result)
    
    def __sub__(self, other):
        """
        Subtract two matrices element-wise.
        
        Args:
            other: Another Matrix instance
            
        Returns:
            A new Matrix representing the difference
            
        Raises:
            DimensionError: If matrices have different dimensions
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only subtract Matrix from Matrix")
        
        if self.rows != other.rows or self.cols != other.cols:
            raise DimensionError(
                f"Cannot subtract matrices with dimensions ({self.rows}x{self.cols}) "
                f"and ({other.rows}x{other.cols})"
            )
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self._data[i][j] - other._data[i][j])
            result.append(row)
        
        return Matrix(result)
    
    def dot(self, other):
        """
        Multiply this matrix with another matrix.
        
        Args:
            other: Another Matrix instance
            
        Returns:
            A new Matrix representing the product
            
        Raises:
            DimensionError: If dimensions are incompatible (self.cols != other.rows)
        """
        if not isinstance(other, Matrix):
            raise TypeError("Can only multiply Matrix with Matrix")
        
        if self.cols != other.rows:
            raise DimensionError(
                f"Cannot multiply matrices with dimensions ({self.rows}x{self.cols}) "
                f"and ({other.rows}x{other.cols}): columns of first must equal rows of second"
            )
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                # Calculate dot product of row i from self and column j from other
                value = 0
                for k in range(self.cols):
                    value += self._data[i][k] * other._data[k][j]
                row.append(value)
            result.append(row)
        
        return Matrix(result)
    
    def __str__(self):
        """
        Return a readable string representation of the matrix.
        
        Returns:
            A formatted string showing the matrix structure
        """
        return "[" + ",".join(str(row) for row in self._data) + "]"
    
    def __repr__(self):
        """
        Return a detailed string representation of the matrix.
        
        Returns:
            A string that can be used to recreate the matrix
        """
        return f"Matrix({self._data})"
