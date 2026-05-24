def calculate_trust_score(missing, anomalies):

    score = 100

    missing_columns = len(
        [v for v in missing.values() if v > 0]
    )

    score -= missing_columns * 5

    score -= anomalies * 0.1

    return round(max(score, 0), 2)