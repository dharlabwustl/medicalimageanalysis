# Define data
X = [1, 2, 3]
y = [1, 2, 1]

# Define the negative log-likelihood function
def neg_log_likelihood(A):
    A0, A1 = A
    lambda_values = [A0 + A1 * x for x in X]
    # Ensure all lambda values are positive
    for l in lambda_values:
        if l <= 0:  # Log is undefined for non-positive values
            return float('inf')
    # Compute the negative log-likelihood
    nll = 0
    for i in range(len(y)):
        nll += -y[i] * (lambda_values[i]).__log__() + lambda_values[i]
    return nll

# Gradient descent for optimization
def gradient_descent(f, A_init, learning_rate=0.01, tolerance=1e-6, max_iter=10000):
    A = A_init
    for _ in range(max_iter):
        grad_A0 = (f([A[0] + tolerance, A[1]]) - f(A)) / tolerance
        grad_A1 = (f([A[0], A[1] + tolerance]) - f(A)) / tolerance
        A_new = [A[0] - learning_rate * grad_A0, A[1] - learning_rate * grad_A1]
        if abs(A_new[0] - A[0]) < tolerance and abs(A_new[1] - A[1]) < tolerance:
            break
        A = A_new
    return A

# Initial guess for A0 and A1
initial_guess = [1.0, 0.5]

# Perform optimization using gradient descent
optimal_A = gradient_descent(neg_log_likelihood, initial_guess)
print(f"Optimal A = {optimal_A}")
