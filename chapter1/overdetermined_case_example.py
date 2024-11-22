
# Overdetermined Systems: Solve A = Y X^+ using pseudo-inverse

# Define X and Y
X = [[1, 2], [3, 4], [5, 6]]  # 3x2 matrix
Y = [[2, 4], [6, 8], [10, 12]]  # 3x2 matrix

# Compute X^T X
XT = [[X[0][0], X[1][0], X[2][0]], [X[0][1], X[1][1], X[2][1]]]  # Transpose of X
XT_X = [[sum(XT[i][k] * X[k][j] for k in range(3)) for j in range(2)] for i in range(2)]

# Compute the determinant of XT_X
det_XT_X = XT_X[0][0] * XT_X[1][1] - XT_X[0][1] * XT_X[1][0]

if det_XT_X != 0:
    # Compute the inverse of XT_X
    XT_X_inv = [[XT_X[1][1] / det_XT_X, -XT_X[0][1] / det_XT_X],
                [-XT_X[1][0] / det_XT_X, XT_X[0][0] / det_XT_X]]

    # Compute X^+ = (X^T X)^-1 X^T
    X_plus = [[sum(XT_X_inv[i][k] * XT[k][j] for k in range(2)) for j in range(3)] for i in range(2)]

    # Compute A = Y X^+
    A = [[sum(Y[i][k] * X_plus[k][j] for k in range(2)) for j in range(2)] for i in range(3)]

    print("Solution: A =")
    for row in A:
        print(row)
else:
    print("No solution: X^T X is singular and not invertible.")
