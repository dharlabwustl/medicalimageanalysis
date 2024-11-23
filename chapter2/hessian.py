# Hessian Calculation Using Finite Differences
def hessian(func, x, h=1e-5):
    """
    Compute the Hessian matrix of a scalar function func at point x.

    Parameters:
        func: function
            A scalar-valued function.
        x: list
            A list of input variables at which to compute the Hessian.
        h: float
            Step size for finite differences.

    Returns:
        list of lists: Hessian matrix.
    """
    n = len(x)  # Number of input variables
    H = [[0] * n for _ in range(n)]  # Initialize Hessian matrix

    for i in range(n):  # Loop over input variables
        for j in range(n):
            x_forward_i = x[:]
            x_forward_i[i] += h
            x_forward_j = x[:]
            x_forward_j[j] += h
            x_both = x[:]
            x_both[i] += h
            x_both[j] += h

            f = func(x)
            f_i = func(x_forward_i)
            f_j = func(x_forward_j)
            f_both = func(x_both)

            H[i][j] = (f_both - f_i - f_j + f) / (h**2)

    return H

# Example Usage: Function f(x, y) = x^2 + y^2
def example_scalar_func(x):
    return x[0]**2 + x[1]**2

point = [1.0, 2.0]  # Point at which to compute the Hessian
hessian_matrix = hessian(example_scalar_func, point)
print("Hessian Matrix:", hessian_matrix)
