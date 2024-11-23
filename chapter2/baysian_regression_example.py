# Bayesian Regression

# Define X and y
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 2]

# Define hyperparameters
sigma_y = 1  # Observation noise
sigma_A = 2  # Prior uncertainty

# Compute X^T X and X^T y
XT_X = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        XT_X[i][j] = sum(X[k][i] * X[k][j] for k in range(3))

XT_y = [sum(X[k][i] * y[k] for k in range(3)) for i in range(2)]

# Add regularization term
lambda_inv = [[XT_X[i][j] + (1 / sigma_A**2 if i == j else 0) for j in range(2)] for i in range(2)]

# Compute posterior mean
det = lambda_inv[0][0] * lambda_inv[1][1] - lambda_inv[0][1] * lambda_inv[1][0]
lambda_inv_inv = [[lambda_inv[1][1] / det, -lambda_inv[0][1] / det],
                  [-lambda_inv[1][0] / det, lambda_inv[0][0] / det]]

A_posterior = [sum(lambda_inv_inv[i][j] * XT_y[j] / sigma_y**2 for j in range(2)) for i in range(2)]

print(f"Posterior Mean of A = {A_posterior}")
