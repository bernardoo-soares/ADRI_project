import numpy as np

# Create a 4x4 matrix with two almost linearly independent columns
X = np.array([
    [1.0, 2.0, 3.0, 7.0],
    [2.0, 4.0, 6.0, 21.0],
    [1.0, 1.9, 3.0, 11.0],
    [2.0, 3.9, 6.0, 17.0]
])

# Calculate singular values
singular_values = np.linalg.svd(X, compute_uv=False)

# Calculate the condition number
condition_number = np.max(singular_values) / np.min(singular_values)

# Print singular values and condition number
print("Singular Values:", singular_values)
print("Condition Number:", condition_number)
