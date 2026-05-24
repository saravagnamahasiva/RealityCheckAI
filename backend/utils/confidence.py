def calculate_confidence(
    trust_score,
    anomalies,
    duplicates
):

    if (
        trust_score >= 80
        and anomalies < 50
        and duplicates < 20
    ):

        return "High Confidence"

    elif trust_score >= 50:

        return "Medium Confidence"

    else:

        return "Low Confidence"