
# Vector Case: Solve A = y / x element-wise

# Given vectors
x = [2, 1, 4]
y = [10, 5, 20]

# Solve for A element-wise
A = []
for i in range(len(x)):
    if x[i] != 0:
        A.append(y[i] / x[i])
    else:
        A.append(None)  # None represents undefined (division by zero)

print(f"Solution: A = {A}")
