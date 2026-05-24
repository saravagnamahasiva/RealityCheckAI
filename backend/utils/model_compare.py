from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder

import pandas as pd


def compare_models(df):

    if "survived" not in df.columns:

        return {
            "message":
            "No target column found."
        }

    clean_df = df.dropna().copy()

    if len(clean_df) < 50:

        return {
            "message":
            "Not enough clean data."
        }

    # CONVERT ALL NON-NUMERIC COLUMNS
    for col in clean_df.columns:

        if clean_df[col].dtype == "object":

            le = LabelEncoder()

            clean_df[col] = le.fit_transform(
                clean_df[col].astype(str)
            )

    # BOOLEAN → INTEGER
    bool_cols = clean_df.select_dtypes(
        include=["bool"]
    ).columns

    for col in bool_cols:

        clean_df[col] = clean_df[col].astype(int)

    # KEEP ONLY NUMERIC
    clean_df = clean_df.select_dtypes(
        include=["number"]
    )

    X = clean_df.drop(
        "survived",
        axis=1
    )

    y = clean_df["survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # LOGISTIC REGRESSION
    lr = LogisticRegression(
        max_iter=1000
    )

    lr.fit(X_train, y_train)

    lr_pred = lr.predict(X_test)

    lr_acc = accuracy_score(
        y_test,
        lr_pred
    )

    # RANDOM FOREST
    rf = RandomForestClassifier()

    rf.fit(X_train, y_train)

    rf_pred = rf.predict(X_test)

    rf_acc = accuracy_score(
        y_test,
        rf_pred
    )

    agreement = (
        lr_pred == rf_pred
    ).mean() * 100

    return {

        "logistic_accuracy":
        round(lr_acc * 100, 2),

        "randomforest_accuracy":
        round(rf_acc * 100, 2),

        "agreement_score":
        round(agreement, 2)
    }