# Jacobi Iteration for Solving Ax = y

def jacobi(A, y, tol=1e-6, max_iterations=100, initial_guess=None):
    """
    Solve Ax = y using Jacobi iteration.

    Parameters:
        A (list of list of floats): Coefficient matrix.
        y (list of floats): Right-hand side vector.
        tol (float): Tolerance for convergence.
        max_iterations (int): Maximum number of iterations.
        initial_guess (list of floats): Initial guess for the solution.

    Returns:
        list of floats: Solution vector x.
    """
    n = len(A)
    if initial_guess is None:
        x = [0] * n  # Start with zeros
    else:
        x = initial_guess[:]

    for iteration in range(max_iterations):
        x_new = x[:]  # Create a copy to store new values
        for i in range(n):
            # Compute the updated value for x[i]
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (y[i] - sigma) / A[i][i]

        # Check for convergence
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new

    raise ValueError("Jacobi method did not converge within the maximum number of iterations.")

# Example Usage
A = [[4, 1, 2],
     [3, 5, 1],
     [1, 1, 3]]

y = [4, 7, 3]

# Solve Ax = y
solution = jacobi(A, y)
print("Solution:", solution)
