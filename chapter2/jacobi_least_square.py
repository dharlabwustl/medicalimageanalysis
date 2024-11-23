def jacobi_least_squares(x, y, tol=1e-6, max_iterations=100):
    """
    Solve Ax = y for A in an overdetermined system using Jacobi iteration.
    """
    import numpy as np
    n = len(x)
    A = np.zeros((n, n))  # Initialize A as zero

    for _ in range(max_iterations):
        A_new = np.copy(A)
        for i in range(n):
            for j in range(n):
                if x[j] != 0:
                    sigma = sum(A[i, k] * x[k] for k in range(n) if k != j)
                    A_new[i, j] = (y[i] - sigma) / x[j]

        # Check for convergence
        if np.linalg.norm(A_new - A, ord='fro') < tol:
            return A_new
        A = A_new

    raise ValueError("Jacobi method did not converge.")

# Example Usage
x = [1, 2, 3]
y = [4, 7, 3]
A = jacobi_least_squares(x, y)
print("Solution Matrix A (Overdetermined):")
print(A)
