def detect_bias(df):

    bias_results = []

    # CHECK GENDER BIAS
    if "sex" in df.columns:

        gender_counts = (
            df["sex"]
            .value_counts(normalize=True)
        )

        if len(gender_counts) > 0:

            max_ratio = gender_counts.max()

            if max_ratio > 0.80:

                bias_results.append(
                    "Potential gender bias detected."
                )

    # CHECK CLASS IMBALANCE
    if "survived" in df.columns:

        target_counts = (
            df["survived"]
            .value_counts(normalize=True)
        )

        if len(target_counts) > 0:

            max_ratio = target_counts.max()

            if max_ratio > 0.85:

                bias_results.append(
                    "Target variable is highly imbalanced."
                )

    if len(bias_results) == 0:

        bias_results.append(
            "No major bias detected."
        )

    return bias_results