def discover_relationships(df):

    relationships = []

    numeric_df = df.select_dtypes(
        include=["number"]
    )

    if numeric_df.shape[1] < 2:

        return [
            {
                "message": "Not enough numeric columns to discover relationships.",
                "feature_1": None,
                "feature_2": None,
                "correlation": 0,
                "strength": "Unknown"
            }
        ]

    corr_matrix = numeric_df.corr()

    checked_pairs = set()

    for col1 in corr_matrix.columns:

        for col2 in corr_matrix.columns:

            if col1 == col2:
                continue

            pair = tuple(sorted([col1, col2]))

            if pair in checked_pairs:
                continue

            checked_pairs.add(pair)

            corr_value = corr_matrix.loc[col1, col2]

            if abs(corr_value) >= 0.2:

                if abs(corr_value) >= 0.7:
                    strength = "Strong"
                elif abs(corr_value) >= 0.4:
                    strength = "Moderate"
                else:
                    strength = "Weak"

                direction = (
                    "positive"
                    if corr_value > 0
                    else "negative"
                )

                relationships.append({
                    "message": f"{col1} and {col2} have a {strength.lower()} {direction} relationship.",
                    "feature_1": col1,
                    "feature_2": col2,
                    "correlation": round(corr_value, 3),
                    "strength": strength
                })

    if len(relationships) == 0:

        relationships.append({
            "message": "No meaningful numeric relationships detected.",
            "feature_1": None,
            "feature_2": None,
            "correlation": 0,
            "strength": "Low"
        })

    return relationships