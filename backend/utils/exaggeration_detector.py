def detect_exaggeration(
    claim,
    support_score
):

    claim = claim.lower()

    exaggeration_words = [

        "always",
        "never",
        "all",
        "100%",
        "completely"
    ]

    for word in exaggeration_words:

        if word in claim:

            if support_score < 95:

                return (
                    f"Exaggeration detected بسبب '{word}'."
                )

    return (
        "No exaggeration detected."
    )