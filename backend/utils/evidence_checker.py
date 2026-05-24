def evaluate_evidence(
    support_score
):

    if support_score >= 85:

        return {
            "evidence_level":
            "Strong Evidence",

            "verdict":
            "AI conclusion is well supported."
        }

    elif support_score >= 60:

        return {
            "evidence_level":
            "Moderate Evidence",

            "verdict":
            "AI conclusion has partial support."
        }

    else:

        return {
            "evidence_level":
            "Weak Evidence",

            "verdict":
            "AI conclusion lacks strong evidence."
        }