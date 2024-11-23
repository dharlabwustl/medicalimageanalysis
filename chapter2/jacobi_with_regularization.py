def jacobi_with_regularization(x, y, tol=1e-6, max_iterations=100, lambda_reg=0.01):
    """
    Solve Ax = y for noisy systems using Jacobi iteration with regularization.

    Parameters:
        x (list of floats): Input vector (known).
        y (list of floats): Output vector (known).
        tol (float): Tolerance for convergence.
        max_iterations (int): Maximum number of iterations.
        lambda_reg (float): Regularization parameter.

    Returns:
        list of list of floats: Solution matrix A.
    """
    import numpy as np
    n = len(x)
    A = np.zeros((n, n))  # Initialize A as a zero matrix

    for iteration in range(max_iterations):
        A_new = np.copy(A)
        for i in range(n):
            for j in range(n):
                if x[j] != 0:
                    sigma = sum(A[i, k] * x[k] for k in range(n) if k != j)
                    A_new[i, j] = (y[i] - sigma) / x[j]

        # Apply regularization
        A_new = A_new - lambda_reg * A_new

        # Check for convergence
        if np.linalg.norm(A_new - A, ord='fro') < tol:
            return A_new
        A = A_new

    raise ValueError("Jacobi method did not converge.")

# Example Usage
x = [1, 2, 3]
y = [4, 7, 3]
solution = jacobi_with_regularization(x, y, lambda_reg=0.1)
print("Solution Matrix A with Regularization:")
print(solution)
