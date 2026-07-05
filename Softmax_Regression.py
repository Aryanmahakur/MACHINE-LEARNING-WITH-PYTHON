from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    multi_class="multinomial",
    solver="lbfgs"
)

model.fit(X_train, y_train)

prediction = model.predict(X_test)

prob = model.predict_proba(X_test)


// the only diffrce
