
# Least Squares Method

# Define X and y
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 2]

# Compute X^T X
XT_X = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        XT_X[i][j] = sum(X[k][i] * X[k][j] for k in range(3))

# Compute X^T y
XT_y = [sum(X[k][i] * y[k] for k in range(3)) for i in range(2)]

# Compute inverse of X^T X (assuming it's invertible)
det = XT_X[0][0] * XT_X[1][1] - XT_X[0][1] * XT_X[1][0]
XT_X_inv = [[XT_X[1][1] / det, -XT_X[0][1] / det],
            [-XT_X[1][0] / det, XT_X[0][0] / det]]

# Compute A
A = [sum(XT_X_inv[i][j] * XT_y[j] for j in range(2)) for i in range(2)]
print(f"Solution: A = {A}")
