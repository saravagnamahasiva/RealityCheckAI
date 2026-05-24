def audit_model_outputs(df):

    required_columns = ["actual", "predicted", "confidence"]

    for col in required_columns:
        if col not in df.columns:
            return {
                "status": "Not Available",
                "message": "Upload CSV with actual, predicted, and confidence columns.",
                "accuracy": None,
                "wrong_predictions": None,
                "overconfident_errors": None,
                "model_trust": "Unknown"
            }

    total = len(df)

    correct = (
        df["actual"] == df["predicted"]
    ).sum()

    accuracy = round(
        (correct / total) * 100,
        2
    )

    wrong_predictions = total - correct

    overconfident_errors = df[
        (df["actual"] != df["predicted"])
        &
        (df["confidence"] >= 0.80)
    ]

    overconfident_count = len(
        overconfident_errors
    )

    if accuracy >= 85 and overconfident_count == 0:
        model_trust = "Trusted"

    elif accuracy >= 70:
        model_trust = "Partially Trusted"

    else:
        model_trust = "Unreliable"

    return {
        "status": "Available",
        "message": "Model output audit completed.",
        "accuracy": accuracy,
        "wrong_predictions": int(wrong_predictions),
        "overconfident_errors": int(overconfident_count),
        "model_trust": model_trust
    }