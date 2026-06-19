import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
data={
    "hours" :[1,2,3,4,5,6,7,8,9,10],
    "marks":[10,18,28,42,60,75,85,90,94,96]
}
df=pd.DataFrame(data)
x=data["hours"]
y=data["marks"]

plt.scatter(x,y)
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Hours vs Marks")
print(df)
poly=PolynomialFeatures(degree=2)
x_poly=poly.fit_transform(df.iloc[:,0:1])
lr=LinearRegression()
lr.fit(x_poly,df.iloc[:,1:2])
y_pred=lr.predict(x_poly)
print(y_pred)
plt.plot(x,y_pred)
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Hours vs Marks")
plt.show()