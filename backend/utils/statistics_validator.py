def statistical_claim_verifier(
    df,
    claim
):

    claim = claim.lower()

    results = []

    # AGE VS SURVIVAL
    if (
        "age" in claim
        and "survival" in claim
    ):

        if (
            "age" in df.columns
            and "survived" in df.columns
        ):

            correlation = (
                df["age"]
                .corr(df["survived"])
            )

            if correlation < 0:

                results.append({

                    "message":
                    f"Claim supported. Correlation = {round(correlation, 3)}",

                    "strength":
                    "Negative Correlation"
                })

            else:

                results.append({

                    "message":
                    f"Claim weakly supported. Correlation = {round(correlation, 3)}",

                    "strength":
                    "Weak Relationship"
                })

    # FARE VS SURVIVAL
    elif (
        "fare" in claim
        and "survival" in claim
    ):

        if (
            "fare" in df.columns
            and "survived" in df.columns
        ):

            correlation = (
                df["fare"]
                .corr(df["survived"])
            )

            if correlation > 0:

                results.append({

                    "message":
                    f"Claim supported. Correlation = {round(correlation, 3)}",

                    "strength":
                    "Positive Correlation"
                })

            else:

                results.append({

                    "message":
                    f"Claim not supported. Correlation = {round(correlation, 3)}",

                    "strength":
                    "No Positive Relationship"
                })

    else:

        results.append({

            "message":
            "No statistical verification rule available.",

            "strength":
            "Unknown"
        })

    return results