# Examples & Worked Problems

## Example 1 — Addition
A = [[1,2],[3,4]]
B = [[2,0],[1,3]]
A + B = [[3,2],[4,7]]

## Example 2 — Multiplication
A = [[1,2],[3,4]]
B = [[2,0],[1,3]]
A · B = [[1*2+2*1, 1*0+2*3],
         [3*2+4*1, 3*0+4*3]]
      = [[4,6],[10,12]]

## Example 3 — Determinant (2×2)
A = [[a,b],[c,d]]
det(A) = ad - bc

For A = [[1,2],[3,4]]:
det(A) = 1*4 - 2*3 = -2

## Example 4 — Inverse (2×2)
If det(A) ≠ 0, the inverse of [[a,b],[c,d]] is:
A⁻¹ = (1/det(A)) * [[d,-b],[-c,a]]

For A = [[1,2],[3,4]] with det(A) = -2:
A⁻¹ = (-1/2) * [[4,-2],[-3,1]]
    = [[-2,1],[1.5,-0.5]]

## Example 5 — Solving Linear Systems
Given Ax = b where:
A = [[2,1],[1,1]], b = [[3],[2]]

Solution methods:
- Row reduction (Gaussian elimination)
- Matrix inverse: x = A⁻¹b

See `USAGE.md` for detailed implementation steps.

## Tip
Include unit tests for these examples to ensure the implementation matches the documentation.