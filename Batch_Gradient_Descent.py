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



# Dataset (2 Features)
x1 = np.array([1, 2, 3, 4, 5])
x2 = np.array([2, 3, 4, 5, 6])

y = np.array([8, 13, 18, 23, 28])

# Parameters (Weights and Bias)
w1 = 0
w2 = 0
b = 0

# Hyperparameters
learning_rate = 0.01
epochs = 1000

n = len(x1)

for i in range(epochs):

    # Step 1: Predictions
    y_pred = w1 * x1 + w2 * x2 + b

    # Step 2: Cost (MSE)
    cost = np.mean((y - y_pred) ** 2)

    # Step 3: Calculate Gradients
    dw1 = (-2 / n) * np.sum(x1 * (y - y_pred))
    dw2 = (-2 / n) * np.sum(x2 * (y - y_pred))
    db = (-2 / n) * np.sum(y - y_pred)

    # Step 4: Update Parameters
    w1 = w1 - learning_rate * dw1
    w2 = w2 - learning_rate * dw2
    b = b - learning_rate * db

    # Print every 100 iterations
    if i % 100 == 0:
        print(f"Epoch {i}: Cost={cost:.4f}, w1={w1:.4f}, w2={w2:.4f}, b={b:.4f}")

print("\nFinal Parameters")
print("Weight 1:", w1)
print("Weight 2:", w2)
print("Bias:", b)