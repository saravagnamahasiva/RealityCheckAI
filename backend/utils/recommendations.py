def generate_recommendations(
    missing,
    duplicates,
    anomalies,
    trust_score
):

    recommendations = []

    # MISSING VALUES
    for col, val in missing.items():

        if val > 0:

            recommendations.append(
                f"Fill missing values in {col} column."
            )

    # DUPLICATES
    if duplicates > 0:

        recommendations.append(
            "Remove duplicate rows."
        )

    # ANOMALIES
    if anomalies > 100:

        recommendations.append(
            "Investigate anomaly records before training AI models."
        )

    # TRUST SCORE
    if trust_score < 70:

        recommendations.append(
            "Dataset quality is low. Data cleaning is recommended."
        )

    if len(recommendations) == 0:

        recommendations.append(
            "Dataset looks good for AI training."
        )

    return recommendations