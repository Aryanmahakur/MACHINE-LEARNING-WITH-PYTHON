import numpy as np
from sklearn.metrics import r2_score

# Dataset
x = np.array([1,2,3,4,5])
y = np.array([3,5,7,9,11])

# Parameters
m = 0
b = 0

# Hyperparameters
lr = 0.01
epochs = 1000

n = len(x)

for i in range(epochs):

    # One sample at a time
    for j in range(n):

        # Step 1: Prediction
        y_pred = m*x[j] + b

        # Step 2: Gradient
        dm = -2 * x[j] * (y[j] - y_pred)
        db = -2 * (y[j] - y_pred)

        # Step 3: Update
        m = m - lr*dm
        b = b - lr*db

    # Cost after one epoch
    y_pred_all = m*x + b
    cost = np.mean((y-y_pred_all)**2)

    if i%100==0:
        print(f"Epoch {i}: Cost={cost:.2f}, m={m:.2f}, b={b:.2f}")

print("\nSlope:",m)
print("Intercept:",b)

print("R²:",r2_score(y,y_pred_all))