def detect_drift(df):

    drift_results = []

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns

    for col in numeric_cols:

        mean_val = df[col].mean()

        if mean_val > 1000:

            drift_results.append(
                f"{col} shows unusual distribution shift."
            )

    if len(drift_results) == 0:

        drift_results.append(
            "No major data drift detected."
        )

    return drift_results