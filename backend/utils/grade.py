def generate_grade(trust_score):

    if trust_score >= 90:

        return "A"

    elif trust_score >= 75:

        return "B"

    elif trust_score >= 60:

        return "C"

    elif trust_score >= 40:

        return "D"

    else:

        return "F"