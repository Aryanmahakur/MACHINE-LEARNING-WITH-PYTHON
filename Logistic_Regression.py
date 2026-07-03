import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# -----------------------------
# Simple Dataset
# -----------------------------

# Hours studied
X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])

# 0 = Fail, 1 = Pass
y = np.array([0, 0, 0, 1, 1, 1])

# -----------------------------
# Split Dataset
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42
)

# -----------------------------
# Create Model
# -----------------------------

model = LogisticRegression()

# Train Model
model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------

y_pred = model.predict(X_test)

print("Actual Labels:")
print(y_test)

print("\nPredicted Labels:")
print(y_pred)

# -----------------------------
# Prediction Probabilities
# -----------------------------

y_prob = model.predict_proba(X_test)

print("\nPrediction Probabilities:")
print(y_prob)

# -----------------------------
# Predict New Student
# -----------------------------

new_student = np.array([[5.5]])

prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("\nNew Student (5.5 hours studied)")
print("Prediction:", prediction)
print("Probability:", probability)


#FROM NUMPY
import numpy as np

# -------------------------
# Dataset
# -------------------------

X = np.array([[1],
              [2],
              [3],
              [4],
              [5],
              [6]], dtype=float)

y = np.array([[0],
              [0],
              [0],
              [1],
              [1],
              [1]], dtype=float)

# -------------------------
# Parameters
# -------------------------

w = 0.0
b = 0.0

lr = 0.1
epochs = 1000

# -------------------------
# Sigmoid Function
# -------------------------

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# -------------------------
# Training
# -------------------------

n = len(X)

for epoch in range(epochs):

    # Linear Equation
    z = X * w + b

    # Sigmoid Output
    y_pred = sigmoid(z)

    # Gradients
    dw = (1 / n) * np.sum((y_pred - y) * X)
    db = (1 / n) * np.sum(y_pred - y)

    # Update Parameters
    w = w - lr * dw
    b = b - lr * db

# -------------------------
# Results
# -------------------------

print("Weight:", w)
print("Bias:", b)

# -------------------------
# Predictions
# -------------------------

print("\nPredictions")

for hour in X:

    z = hour * w + b
    probability = sigmoid(z)

    prediction = 1 if probability >= 0.5 else 0

    print(
        f"Hours = {hour[0]} | Probability = {probability[0]:.4f} | Prediction = {prediction}"
    )

# -------------------------
# New Student
# -------------------------

new_student = 5.5

z = new_student * w + b
probability = sigmoid(z)
prediction = 1 if probability >= 0.5 else 0

print("\nNew Student")
print("Hours Studied:", new_student)
print("Probability:", probability)
print("Prediction:", prediction)