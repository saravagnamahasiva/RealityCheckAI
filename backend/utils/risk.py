def calculate_risk(trust_score):

    if trust_score >= 80:

        return "Low Risk"

    elif trust_score >= 50:

        return "Medium Risk"

    else:

        return "High Risk"