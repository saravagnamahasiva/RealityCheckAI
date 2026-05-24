def check_consistency(df):

    issues = []

    # AGE CHECK
    if "age" in df.columns:

        invalid_age = df[df["age"] > 100]

        if len(invalid_age) > 0:

            issues.append(
                "Some rows contain unrealistic age values."
            )

    # FARE CHECK
    if "fare" in df.columns:

        invalid_fare = df[df["fare"] < 0]

        if len(invalid_fare) > 0:

            issues.append(
                "Negative fare values detected."
            )

    # AGE + FARE LOGIC
    if "age" in df.columns and "fare" in df.columns:

        suspicious = df[
            (df["age"] < 10)
            &
            (df["fare"] > 300)
        ]

        if len(suspicious) > 0:

            issues.append(
                "Suspicious age and fare combinations detected."
            )

    if len(issues) == 0:

        issues.append(
            "No consistency issues found."
        )

    return issues