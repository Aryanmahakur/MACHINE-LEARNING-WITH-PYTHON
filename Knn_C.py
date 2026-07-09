# ======================================================
# K-Nearest Neighbors (KNN) Classification
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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# =========================
# 2. Create Dataset
# =========================

dataset = pd.DataFrame({
    "Gender": [
        1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0
    ],

    "Age": [
        19,22,25,27,30,32,35,37,40,42,
        45,47,50,52,55,57,29,34,38,60
    ],

    "EstimatedSalary": [
        19000,25000,30000,35000,45000,
        50000,65000,70000,80000,85000,
        90000,95000,100000,110000,
        120000,130000,40000,60000,
        75000,140000
    ],

    "Purchased": [
        0,0,0,0,0,
        0,1,1,1,1,
        1,1,1,1,1,
        1,0,1,1,1
    ]
})

print("========== DATASET ==========\n")
print(dataset)

# =========================
# 3. Features & Target
# =========================

X = dataset.drop("Purchased", axis=1)
y = dataset["Purchased"]

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
# 6. Train KNN Model
# =========================

knn = KNeighborsClassifier(
    n_neighbors=5,
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

print("Actual Values")
print(y_test.values)

print("\nPredicted Values")
print(y_pred)

print("\nAccuracy")
print(accuracy_score(y_test, y_pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# =========================
# 9. Predict New Customer
# =========================

new_customer = pd.DataFrame({
    "Gender":[1],
    "Age":[39],
    "EstimatedSalary":[85000]
})

new_customer = scaler.transform(new_customer)

prediction = knn.predict(new_customer)

print("\n========== NEW CUSTOMER ==========\n")

if prediction[0] == 1:
    print("Prediction : Purchased")
else:
    print("Prediction : Not Purchased")

# ======================================================
# 10. Decision Boundary
# (Only Age & Salary are used for visualization)
# ======================================================

X_vis = dataset.drop(["Gender", "Purchased"], axis=1)
y_vis = dataset["Purchased"]

scaler_vis = StandardScaler()
X_vis = scaler_vis.fit_transform(X_vis)

knn_vis = KNeighborsClassifier(
    n_neighbors=5,
    metric="minkowski",
    p=2
)

knn_vis.fit(X_vis, y_vis)

# Mesh Grid

x_min = X_vis[:,0].min() - 1
x_max = X_vis[:,0].max() + 1

y_min = X_vis[:,1].min() - 1
y_max = X_vis[:,1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.01),
    np.arange(y_min, y_max, 0.01)
)

Z = knn_vis.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# =========================
# 11. Plot
# =========================

plt.figure(figsize=(8,6))

plt.contourf(xx, yy, Z, alpha=0.3, cmap="coolwarm")

plt.scatter(
    X_vis[:,0],
    X_vis[:,1],
    c=y_vis,
    cmap="coolwarm",
    edgecolors="black",
    s=80
)

plt.title("KNN Decision Boundary")
plt.xlabel("Age (Scaled)")
plt.ylabel("Estimated Salary (Scaled)")

plt.show()