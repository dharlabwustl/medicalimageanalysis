# Singular Value Decomposition (SVD) for Solving Ax = y

# Example data
A = [[1, 0], [0, 1], [1, 1]]
y = [1, 1, 2]

# Compute SVD
def svd_decompose(A):
    import math

    # Transpose of A
    def transpose(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    # Matrix multiplication
    def matmul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

    # Placeholder for SVD (simplified for educational purposes)
    U = [[1 / math.sqrt(2), 0, 1 / math.sqrt(2)],
         [0, 1, 0],
         [1 / math.sqrt(2), 0, -1 / math.sqrt(2)]]

    Sigma = [[math.sqrt(2), 0],
             [0, 1],
             [0, 0]]

    V_T = [[1 / math.sqrt(2), 1 / math.sqrt(2)],
           [-1 / math.sqrt(2), 1 / math.sqrt(2)]]

    return U, Sigma, V_T

def svd_solve(A, y):
    # Decompose A
    U, Sigma, V_T = svd_decompose(A)

    # Compute U^T * y
    U_T_y = [sum(U[j][i] * y[j] for j in range(len(U))) for i in range(len(U[0]))]

    # Compute pseudo-inverse of Sigma
    Sigma_plus = [[0] * len(U_T_y) for _ in range(len(Sigma[0]))]
    for i in range(len(Sigma[0])):
        if Sigma[i][i] != 0:
            Sigma_plus[i][i] = 1 / Sigma[i][i]

    # Compute z = Sigma^+ * (U^T * y)
    z = [sum(Sigma_plus[i][j] * U_T_y[j] for j in range(len(U_T_y))) for i in range(len(Sigma_plus))]

    # Compute x = V * z
    x = [sum(V_T[j][i] * z[j] for j in range(len(z))) for i in range(len(V_T[0]))]

    return x

# Solve Ax = y
x_solution = svd_solve(A, y)
print("Solution x:", x_solution)
