
# Matrix Case: Solve A = Y X^-1 for a square matrix X

# Define X and Y matrices
X = [[1, 2], [3, 4]]
Y = [[2, 4], [6, 8]]

# Compute the determinant of X
det_X = X[0][0] * X[1][1] - X[0][1] * X[1][0]

if det_X != 0:
    # Compute the inverse of X
    X_inv = [[X[1][1] / det_X, -X[0][1] / det_X],
             [-X[1][0] / det_X, X[0][0] / det_X]]

    # Compute A = Y * X^-1
    A = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            A[i][j] = sum(Y[i][k] * X_inv[k][j] for k in range(2))

    print("Solution: A =")
    for row in A:
        print(row)
else:
    print("No solution: X is singular and not invertible.")
