def generate_final_verdict(

    contradictions,

    hallucinations,

    trust_score,

    weak_evidence_count,

    overconfident_count
):

    risk_points = 0

    # CONTRADICTIONS
    if (
        "No contradictions detected."
        not in contradictions
    ):

        risk_points += 2

    # HALLUCINATIONS
    if len(hallucinations) > 0:

        risk_points += 2

    # LOW TRUST SCORE
    if trust_score < 60:

        risk_points += 2

    # WEAK EVIDENCE
    risk_points += weak_evidence_count

    # OVERCONFIDENCE
    risk_points += overconfident_count

    # FINAL VERDICT
    if risk_points <= 2:

        return {
            "verdict":
            "TRUSTED",

            "message":
            "AI outputs appear reliable."
        }

    elif risk_points <= 5:

        return {
            "verdict":
            "PARTIALLY TRUSTED",

            "message":
            "AI outputs require human verification."
        }

    else:

        return {
            "verdict":
            "UNRELIABLE",

            "message":
            "AI outputs are not fully trustworthy."
        }