def detect_hallucinations(text):

    suspicious_patterns = [

        "100% accurate",

        "always correct",

        "never fails",

        "40 states in india",

        "humans can live 500 years",

        "earth is flat"
    ]

    detected = []

    lower_text = text.lower()

    for pattern in suspicious_patterns:

        if pattern in lower_text:

            detected.append(
                f"Suspicious claim detected: {pattern}"
            )

    if len(detected) == 0:

        detected.append(
            "No obvious hallucinations detected."
        )

    return detected