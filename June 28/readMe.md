### np.info()

- inline documentation

### steps

1. generate random matrix of n x n
2. take transpose of it
3. then compare both matrix for each element create two new matrix. first one will have maximum of them and another one will have minimum of them.
4. finally find the difference between maximum and minimum matrix

eg
[1 2]
[3 4]

[1 3]
[2 4]

[1 3]
[3 4]

### Matrices Multiplication

1.  matrix multiplication
2.  dot product
3.  inner product
4.  scalar product

x + y = 8
x - y = 4

Question
You are given the following system of linear equations representing a simple electrical circuit with 3 loops:

text
10i₁ - 2i₂ - i₃ = 25
-2i₁ + 8i₂ - 3i₃ = 15
-i₁ - 3i₂ + 6i₃ = 20
where i₁, i₂, i₃ are the loop currents in amperes.

Part (a):
Use np.linalg.solve to find the currents i₁, i₂, i₃.

Part (b):
Verify that A @ x equals b (within numerical precision) using np.allclose().

Part (c):
If the coefficient matrix A is singular (i.e., not invertible), what exception does np.linalg.solve raise? Modify the matrix to make it singular and demonstrate this behavior.

Part (d):
Compare np.linalg.solve vs. np.linalg.inv for solving the system. Which method is more numerically stable and efficient for large systems, and why?

Expected Output:

A solution vector x (currents).

A boolean verification from np.allclose.

A demonstration of the LinAlgError when solving a singular system.

A conceptual explanation comparing solve vs. inv.

This tests:

Correct usage of np.linalg.solve

Error handling (singular matrix)

Numerical verification

Understanding of numerical stability vs. matrix inversion

dataframe, series, apply method
