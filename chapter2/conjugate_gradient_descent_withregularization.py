def conjugate_gradient_regularized(x, y, lambda_reg=0.01, tol=1e-6, max_iterations=100):
    """
    Solve Ax = y for A using Conjugate Gradient with regularization.

    Parameters:
        x (list of floats): Input vector (known).
        y (list of floats): Output vector (known).
        lambda_reg (float): Regularization parameter.
        tol (float): Tolerance for convergence.
        max_iterations (int): Maximum number of iterations.

    Returns:
        list of list of floats: Solution matrix A.
    """
    import numpy as np
    n = len(x)
    A = np.zeros((n, n))  # Initialize A as a zero matrix

    r = y - np.dot(A, x)  # Initial residual
    p = r.copy()  # Initial search direction

    for iteration in range(max_iterations):
        # Compute step size
        Ap = np.dot(A, p) + lambda_reg * p  # Add regularization to A * p
        alpha = np.dot(r, r) / np.dot(p, Ap)

        # Update A
        A_new = A + alpha * np.outer(p, x)

        # Update residual
        r_new = r - alpha * Ap

        # Check for convergence
        if np.linalg.norm(r_new) < tol:
            return A_new

        # Compute new search direction
        beta = np.dot(r_new, r_new) / np.dot(r, r)
        p = r_new + beta * p

        # Update variables
        A = A_new
        r = r_new

    raise ValueError("Conjugate Gradient method did not converge.")

# Example Usage
x = [1, 2, 3]
y = [4, 7, 3]

# Solve Ax = y with regularization
solution = conjugate_gradient_regularized(x, y, lambda_reg=0.1)
print("Solution Matrix A (Regularized):")
print(solution)
