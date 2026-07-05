#Project
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
df=pd.read_csv(r"C:\Users\ARYAN MAHAKUR\Downloads\IRIS.csv")
print(df.head(1))
print(df.isnull().sum().sum())
df=df.drop_duplicates()
print(df.duplicated().sum())
x=df.drop(columns="species")
y=df["species"]
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=46,test_size=0.2)
lr=LogisticRegression(
                      solver="lbfgs")
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
y_pred_prob=lr.predict_proba(x_test)
print(y_pred)
print(y_pred_prob)
print("Accuracy:", accuracy_score(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))
new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = lr.predict(new_flower)

print(prediction)