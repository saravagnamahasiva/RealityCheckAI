def data_health_status(
    trust_score,
    anomalies
):

    if (
        trust_score >= 85
        and anomalies < 50
    ):

        return "Excellent"

    elif trust_score >= 70:

        return "Good"

    elif trust_score >= 50:

        return "Warning"

    else:

        return "Critical"