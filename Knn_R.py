# ======================================================
# K-Nearest Neighbors (KNN) Regression
# Using Manual Dataset (Without iloc)
# ======================================================

# =========================
# 1. Import Libraries
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# =========================
# 2. Create Dataset
# =========================

dataset = pd.DataFrame({
    "Gender":[
        1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0
    ],

    "Age":[
        19,22,25,27,30,32,35,37,40,42,
        45,47,50,52,55,57,29,34,38,60
    ],

    "Experience":[
        0,1,2,3,5,6,8,10,12,14,
        16,18,20,22,25,28,4,7,11,30
    ],

    "Salary":[
        20000,25000,30000,35000,45000,
        50000,65000,70000,80000,85000,
        90000,95000,100000,110000,
        120000,130000,40000,60000,
        75000,140000
    ]
})

print("========== DATASET ==========\n")
print(dataset)

# =========================
# 3. Features & Target
# =========================

X = dataset.drop("Salary", axis=1)
y = dataset["Salary"]

# =========================
# 4. Train-Test Split
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =========================
# 5. Feature Scaling
# =========================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================
# 6. Train KNN Regression Model
# =========================

knn = KNeighborsRegressor(
    n_neighbors=3,
    metric="minkowski",
    p=2
)

knn.fit(X_train, y_train)

# =========================
# 7. Prediction
# =========================

y_pred = knn.predict(X_test)

# =========================
# 8. Evaluation
# =========================

print("\n========== RESULTS ==========\n")

print("Actual Salary")
print(y_test.values)

print("\nPredicted Salary")
print(y_pred)

print("\nMean Absolute Error")
print(mean_absolute_error(y_test, y_pred))

print("\nMean Squared Error")
print(mean_squared_error(y_test, y_pred))

print("\nR2 Score")
print(r2_score(y_test, y_pred))

# =========================
# 9. Predict New Employee Salary
# =========================

new_employee = pd.DataFrame({
    "Gender":[1],
    "Age":[39],
    "Experience":[13]
})

new_employee = scaler.transform(new_employee)

prediction = knn.predict(new_employee)

print("\n========== NEW EMPLOYEE ==========\n")
print("Predicted Salary =", prediction[0])

# ======================================================
# 10. Regression Visualization
# (Age vs Salary)
# ======================================================

X_vis = dataset[["Age"]]
y_vis = dataset["Salary"]

scaler_vis = StandardScaler()
X_vis_scaled = scaler_vis.fit_transform(X_vis)

knn_vis = KNeighborsRegressor(
    n_neighbors=3
)

knn_vis.fit(X_vis_scaled, y_vis)

# Create Smooth Line

X_grid = np.arange(
    X_vis_scaled.min(),
    X_vis_scaled.max(),
    0.01
).reshape(-1,1)

y_grid = knn_vis.predict(X_grid)

# =========================
# 11. Plot
# =========================

plt.figure(figsize=(8,6))

plt.scatter(
    X_vis_scaled,
    y_vis,
    color="blue",
    label="Actual Data"
)

plt.plot(
    X_grid,
    y_grid,
    color="red",
    linewidth=2,
    label="KNN Regression"
)

plt.title("KNN Regression")
plt.xlabel("Age (Scaled)")
plt.ylabel("Salary")

plt.legend()

plt.show()