from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        return 0

    model = IsolationForest()

    predictions = model.fit_predict(numeric_df)

    anomalies = (predictions == -1).sum()

    return int(anomalies)