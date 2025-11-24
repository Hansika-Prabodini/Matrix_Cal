# API Reference (library-style)

Below are language-agnostic descriptions for the core library functions / methods.

## Matrix class
### Constructors
- `Matrix(data)` — create a matrix from nested lists `data` where each inner list is a row.

### Properties
- `shape` — `(rows, cols)`

### Basic operations
- `A + B` — matrix addition (same shape)
- `A - B` — matrix subtraction (same shape)
- `A.dot(B)` — matrix multiplication (A.cols == B.rows)
- `A.T` or `A.transpose()` — transpose
- `A.scalar_multiply(s)` — multiply by scalar

### Advanced operations
- `A.determinant()` — returns determinant (only for square matrices)
- `A.inverse()` — returns inverse matrix or raises if not invertible
- `A.rank()` — numeric rank
- `A.row_reduce()` — returns row-reduced form (RREF)
- `A.eigenvalues()` — returns eigenvalues (numeric)
- `A.lu_decompose()` — returns (L, U) factorization

### I/O utilities
- `Matrix.from_csv(path)`
- `Matrix.to_csv(path)`
- `Matrix.from_json(path)`
- `Matrix.to_json(path)`

### Exceptions / Errors
- `DimensionError` — for incompatible shapes
- `SingularMatrixError` — when inverse/determinant impossible

## CLI (suggested commands)
- `matrix-app add --matrix-a PATH --matrix-b PATH --out PATH`
- `matrix-app multiply --matrix-a PATH --matrix-b PATH --out PATH`
- `matrix-app det --matrix PATH`
- `matrix-app inverse --matrix PATH --out PATH`
