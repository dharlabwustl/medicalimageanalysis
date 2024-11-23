# Jacobian Calculation Using Finite Differences
def jacobian(func, x, h=1e-5):
    """
    Compute the Jacobian matrix of a vector-valued function func at point x.

    Parameters:
        func: function
            A vector-valued function that returns a list of outputs.
        x: list
            A list of input variables at which to compute the Jacobian.
        h: float
            Step size for finite differences.

    Returns:
        list of lists: Jacobian matrix.
    """
    n = len(x)  # Number of input variables
    m = len(func(x))  # Number of output variables
    J = [[0] * n for _ in range(m)]  # Initialize Jacobian matrix

    for i in range(n):  # Loop over input variables
        x_forward = x[:]
        x_forward[i] += h  # Increment the i-th variable
        f_forward = func(x_forward)
        f = func(x)

        for j in range(m):  # Loop over output variables
            J[j][i] = (f_forward[j] - f[j]) / h

    return J

# Example Usage: Function F(x, y) = [x^2 + y, x + y^2]
def example_func(x):
    return [x[0]**2 + x[1], x[0] + x[1]**2]

point = [1.0, 2.0]  # Point at which to compute the Jacobian
jacobian_matrix = jacobian(example_func, point)
print("Jacobian Matrix:", jacobian_matrix)
