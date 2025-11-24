# Usage

This document gives examples for using the Matrix Calculation App via CLI and as a library.

## CLI examples (generic)
- Add two matrices from files:
  ```bash
  matrix-app add --matrix-a a.csv --matrix-b b.csv --out result.csv
  ```
- Multiply matrices:
  ```bash
  matrix-app multiply --matrix-a a.csv --matrix-b b.csv --out product.csv
  ```
- Compute determinant:
  ```bash
  matrix-app det --matrix matrix.csv
  ```

## Library usage (Python examples)
```python
from matrix_app import Matrix

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[2, 0], [1, 3]])

C = A + B               # matrix addition
D = A.dot(B)            # matrix multiplication
detA = A.determinant()  # determinant
invA = A.inverse()      # inverse (if invertible)
```

## Input formats
- CSV: comma-separated rows
- JSON: nested lists `[[...],[...]]`
- Plain text: whitespace-separated values by row

## Output formats
- CSV, JSON, pretty-printed text

## Error handling
- Dimension mismatches raise errors for incompatible operations.
- Determinant/inverse operations on singular matrices return a clear error message.
