def detect_mode(df):

    model_output_cols = [
        "actual",
        "predicted",
        "confidence"
    ]

    if all(col in df.columns for col in model_output_cols):

        return "model_output"

    else:

        return "dataset"