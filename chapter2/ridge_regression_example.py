
# Ridge Regression (L2 Regularization)

# Define X and y
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 2]
lambda_ = 1  # Regularization parameter

# Compute X^T X
XT_X = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        XT_X[i][j] = sum(X[k][i] * X[k][j] for k in range(3))

# Add lambda * I to X^T X
XT_X_reg = [[XT_X[i][j] + (lambda_ if i == j else 0) for j in range(2)] for i in range(2)]

# Compute X^T y
XT_y = [sum(X[k][i] * y[k] for k in range(3)) for i in range(2)]

# Compute inverse of (X^T X + lambda * I) (assuming it's invertible)
det = XT_X_reg[0][0] * XT_X_reg[1][1] - XT_X_reg[0][1] * XT_X_reg[1][0]
XT_X_reg_inv = [[XT_X_reg[1][1] / det, -XT_X_reg[0][1] / det],
                [-XT_X_reg[1][0] / det, XT_X_reg[0][0] / det]]

# Compute A
A = [sum(XT_X_reg_inv[i][j] * XT_y[j] for j in range(2)) for i in range(2)]
print(f"Solution: A = {A}")
