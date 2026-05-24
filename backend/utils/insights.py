def generate_insights(
    missing,
    anomalies,
    duplicates
):

    insights = []

    for col, val in missing.items():

        if val > 100:

            insights.append(
                f"{col} column has heavy missing values."
            )

    if anomalies > 100:

        insights.append(
            "Dataset contains high anomaly records."
        )

    if duplicates > 50:

        insights.append(
            "Dataset contains many duplicate rows."
        )

    if len(insights) == 0:

        insights.append(
            "Dataset looks healthy."
        )

    return insights