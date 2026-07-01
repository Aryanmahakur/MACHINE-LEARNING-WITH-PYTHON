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
batch_size = 2

n = len(x)

for i in range(epochs):

    for j in range(0, n, batch_size):

        # Current batch
        x_batch = x[j:j+batch_size]
        y_batch = y[j:j+batch_size]

        # Prediction
        y_pred = m*x_batch + b

        # Cost
        cost = np.mean((y_batch-y_pred)**2)

        # Gradients
        dm = (-2/len(x_batch))*np.sum(x_batch*(y_batch-y_pred))
        db = (-2/len(x_batch))*np.sum(y_batch-y_pred)

        # Update
        m = m-lr*dm
        b = b-lr*db

    if i%100==0:
        print(f"Epoch {i}: Cost={cost:.2f}, m={m:.2f}, b={b:.2f}")

y_pred = m*x+b

print("\nSlope:",m)
print("Intercept:",b)

print("R²:",r2_score(y,y_pred))