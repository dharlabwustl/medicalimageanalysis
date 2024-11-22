# Gradient Descent for Least Squares

# Define X and y
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 2]

# Initialize parameters
A = [0, 0]  # Initial guess for A
eta = 0.01  # Learning rate
iterations = 100

# Perform gradient descent
for _ in range(iterations):
    # Compute the gradient: 2 * X^T (X * A - y)
    grad = [0, 0]
    for i in range(2):
        grad[i] = 2 * sum(X[k][i] * (sum(X[k][j] * A[j] for j in range(2)) - y[k]) for k in range(3))

    # Update A
    A = [A[i] - eta * grad[i] for i in range(2)]

print(f"Solution after {iterations} iterations: A = {A}")
