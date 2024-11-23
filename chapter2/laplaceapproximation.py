# Laplace Approximation for Bayesian Inference

# Data
X = [1, 2, 3]
y = [1, 2, 1]
sigma_A = 2
sigma_y = 1

# Negative log-posterior function
def neg_log_posterior(A):
    A0, A1 = A
    lambda_values = [A0 + A1 * x for x in X]
    if any(l <= 0 for l in lambda_values):
        return float('inf')
    likelihood = sum((y[i] - lambda_values[i])**2 / (2 * sigma_y**2) for i in range(len(y)))
    prior = (A0**2 + A1**2) / (2 * sigma_A**2)
    return likelihood + prior

# Gradient descent to find MAP estimate
def gradient_descent(initial_guess, learning_rate=0.01, tolerance=1e-6, max_iter=10000):
    A = initial_guess
    for _ in range(max_iter):
        grad_A0 = sum((A[0] + A[1] * X[i] - y[i]) / sigma_y**2 for i in range(len(y))) + A[0] / sigma_A**2
        grad_A1 = sum((A[0] + A[1] * X[i] - y[i]) * X[i] / sigma_y**2 for i in range(len(y))) + A[1] / sigma_A**2
        grad = [grad_A0, grad_A1]
        A_new = [A[i] - learning_rate * grad[i] for i in range(2)]
        if all(abs(A_new[i] - A[i]) < tolerance for i in range(2)):
            return A_new
        A = A_new
    return A

# Compute the Hessian (simplified for this problem)
def compute_hessian(A):
    H00 = sum(1 / sigma_y**2 for _ in X) + 1 / sigma_A**2
    H11 = sum(x**2 / sigma_y**2 for x in X) + 1 / sigma_A**2
    H01 = sum(x / sigma_y**2 for x in X)
    return [[H00, H01], [H01, H11]]

# Initial guess
initial_guess = [1.0, 0.5]

# Perform gradient descent to find MAP estimate
A_MAP = gradient_descent(initial_guess)

# Compute Hessian at MAP estimate
H = compute_hessian(A_MAP)

# Invert the Hessian to get the covariance matrix
det = H[0][0] * H[1][1] - H[0][1]**2
H_inv = [[H[1][1] / det, -H[0][1] / det],
         [-H[0][1] / det, H[0][0] / det]]

print(f"MAP Estimate: {A_MAP}")
print(f"Posterior Covariance: {H_inv}")
