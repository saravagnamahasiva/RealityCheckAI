def validate_claim_confidence(
    claim,
    ai_confidence,
    statistical_support
):

    # OVERCONFIDENCE CHECK
    if (
        ai_confidence > 90
        and statistical_support < 70
    ):

        return (
            "Model appears overconfident."
        )

    # UNDERCONFIDENCE CHECK
    elif (
        ai_confidence < 50
        and statistical_support > 80
    ):

        return (
            "Model confidence may be too low."
        )

    else:

        return (
            "Confidence level appears reasonable."
        )