# Examples & Worked Problems

## Example 1 — Addition
A = [[1,2],[3,4]]
B = [[2,0],[1,3]]
A + B = [[3,2],[4,7]]

## Example 2 — Multiplication
A = [[1,2],[3,4]]
B = [[2,0],[1,3]]
A dot B = [[1*2+2*1, 1*0+2*3],
           [3*2+4*1, 3*0+4*3]]
        = [[4,6],[10,12]]

## Example 3 — Determinant (2x2)
A = [[a,b],[c,d]]
det(A) = a*d - b*c
For A = [[1,2],[3,4]], det = 1*4 - 2*3 = -2

## Example 4 — Inverse (2x2)
If det(A) != 0, inverse of [[a,b],[c,d]] is (1/det)*[[d,-b],[-c,a]]
For A = [[1,2],[3,4]], inverse = (-1/2)*[[4,-2],[-3,1]] = [[-2,1],[1.5,-0.5]]

## Example 5 — Row reduction to solve Ax = b
A = [[2,1],[1,1]], b = [3,2]
Solve using row reduction or inverse as shown in `USAGE.md`.

## Tip
Include unit tests for these examples to ensure the implementation matches the documentation.
