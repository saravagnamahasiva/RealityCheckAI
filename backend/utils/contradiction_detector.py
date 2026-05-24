def detect_contradictions(observations):

    contradictions = []

    text = " ".join(
        observations
    ).lower()

    # CONTRADICTION RULES

    if (
        "higher fare survived more" in text
        and
        "fare has no impact" in text
    ):

        contradictions.append(
            "Contradiction detected in fare analysis."
        )

    if (
        "females survived more" in text
        and
        "males survived more" in text
    ):

        contradictions.append(
            "Contradiction detected in gender analysis."
        )

    if len(contradictions) == 0:

        contradictions.append(
            "No contradictions detected."
        )

    return contradictions