import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

x, y, coefficient = make_regression(
    n_samples=200,
    n_features=2,
    noise=15,
    coef=True,
    random_state=42,
    n_targets=1
)
df=pd.DataFrame({

    'features_1 ':x[:,0],
    'features_2 ':x[:,1],
    'output ':y
})
print("datas",df.head())
fig =plt.figure(figsize=(10,10))
ax=fig.add_subplot(121,projection='3d');
ax.scatter(
    x[:,0],
    x[:,1],
    y
)
ax.set_xlabel("f1")
ax.set_ylabel("f2")
ax.set_zlabel("op")
plt.show()
lr = LinearRegression()

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=2
)

lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)

print(y_pred)
figs =plt.figure(figsize=(10,10))
axs=figs.add_subplot(122,projection='3d');
axs.scatter(
    x_test[:,0],
    x_test[:,1],
    y_pred
)
axs.set_xlabel("f1")
axs.set_ylabel("f2")
axs.set_zlabel("op")
plt.show()