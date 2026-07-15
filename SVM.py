import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# -----------------------------
# Dataset
# -----------------------------
X = np.array([
    [2, 2],
    [2, 3],
    [3, 2],
    [7, 7],
    [8, 8],
    [8, 7]
])

y = np.array([0, 0, 0, 1, 1, 1])

# -----------------------------
# Train Linear SVM
# -----------------------------
model = SVC(kernel="linear", C=1.0)
model.fit(X, y)

# -----------------------------
# Plot Data
# -----------------------------
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1],
            color="blue", label="Class 0")

plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1],
            color="red", label="Class 1")

# -----------------------------
# Decision Boundary
# -----------------------------
ax = plt.gca()

xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)

YY, XX = np.meshgrid(yy, xx)

xy = np.vstack([XX.ravel(), YY.ravel()]).T

Z = model.decision_function(xy).reshape(XX.shape)

# Decision Boundary and Margins
plt.contour(
    XX,
    YY,
    Z,
    levels=[-1, 0, 1],
    colors="black",
    linestyles=["--", "-", "--"]
)

# -----------------------------
# Support Vectors
# -----------------------------
plt.scatter(
    model.support_vectors_[:, 0],
    model.support_vectors_[:, 1],
    s=180,
    facecolors="none",
    edgecolors="green",
    linewidth=2,
    label="Support Vectors"
)

plt.title("Linear SVM")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.grid(True)

plt.show()