import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

# -------------------------
# Load Dataset
# -------------------------

df = pd.read_csv(r"C:\Users\ARYAN MAHAKUR\Downloads\spam mail.csv")

print(df.head(5))
print(df.shape)
print(df.isnull().sum().sum())

# -------------------------
# Data Cleaning
# -------------------------

df = df.drop_duplicates()
print(df.duplicated().sum())

df = pd.get_dummies(df, columns=["Category"])

print(df.head(5))

# -------------------------
# Feature Extraction
# -------------------------

cv = CountVectorizer()

x = cv.fit_transform(df["Masseges"])
y = df["Category_spam"]

print(x)
print(df.head(5))

# -------------------------
# Train/Test Split
# -------------------------

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    random_state=42,
    test_size=0.2
)

# -------------------------
# Train Model
# -------------------------

lr = LogisticRegression()

lr.fit(x_train, y_train)

# -------------------------
# Prediction
# -------------------------

yy_pred = lr.predict(x_test)

# -------------------------
# User Input
# -------------------------

mess = input("Enter a sentence to check: ")

mess = cv.transform([mess])

print(lr.predict(mess))
print(lr.predict_proba(mess))