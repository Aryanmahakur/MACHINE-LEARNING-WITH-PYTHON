#GRADIENT DESCENT(Batch)

import numpy as np

# Dataset
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

# Parameters (initial values)
m = 0
b = 0

# Hyperparameters
learning_rate = 0.01
epochs = 1000

n = len(x)

for i in range(epochs):

    # Step 1: Predictions
    y_pred = m * x + b

    # Step 2: Calculate Cost (MSE)
    cost = np.mean((y - y_pred) ** 2)

    # Step 3: Calculate Gradients
    dm = (-2 / n) * np.sum(x * (y - y_pred))
    db = (-2 / n) * np.sum(y - y_pred)

    # Step 4: Update Parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

    # Print every 100 iterations
    if i % 100 == 0:
        print(f"Epoch {i}: Cost={cost:.4f}, m={m:.4f}, b={b:.4f}")

print("\nFinal Parameters")
print("Slope (m):", m)
print("Intercept (b):", b)

#GRADIENT DESCENT(Batch Multiple Features)