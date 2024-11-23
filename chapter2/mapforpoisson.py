# MAP Estimation using Gradient Descent with Basic Python

# Data
X = [1, 2, 3]
y = [1, 2, 1]

# Hyperparameters
sigma_A = 2  # Variance of Gaussian prior
learning_rate = 0.01
tolerance = 1e-6
max_iterations = 10000

# Negative log-posterior function
def neg_log_posterior(A):
    A0, A1 = A
    lambda_values = [A0 + A1 * x for x in X]
    # Ensure all lambda values are positive
    if any(l <= 0 for l in lambda_values):
        return float('inf')
    likelihood = sum(-y[i] * (lambda_values[i].__log__()) + lambda_values[i] for i in range(len(y)))
    prior = (A0**2 + A1**2) / (2 * sigma_A**2)
    return likelihood + prior

# Gradient of the negative log-posterior
def gradient(A):
    A0, A1 = A
    grad_A0 = grad_A1 = 0
    for i in range(len(y)):
        lambda_i = A0 + A1 * X[i]
        if lambda_i <= 0:
            return [float('inf'), float('inf')]
        grad_A0 += -y[i] / lambda_i + 1
        grad_A1 += -y[i] * X[i] / lambda_i + X[i]
    grad_A0 += A0 / sigma_A**2
    grad_A1 += A1 / sigma_A**2
    return [grad_A0, grad_A1]

# Gradient descent algorithm
def gradient_descent(initial_guess):
    A = initial_guess
    for _ in range(max_iterations):
        grad = gradient(A)
        A_new = [A[i] - learning_rate * grad[i] for i in range(2)]
        if all(abs(A_new[i] - A[i]) < tolerance for i in range(2)):
            return A_new
        A = A_new
    return A

# Initial guess
initial_guess = [1.0, 0.5]

# Perform optimization
A_MAP = gradient_descent(initial_guess)
print(f"MAP Estimate: {A_MAP}")
