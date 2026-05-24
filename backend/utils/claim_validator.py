def validate_claim(df, claim):

    claim = claim.lower()

    results = []

    # CLAIM 1
    if (
        "female" in claim
        and "survived" in claim
    ):

        if (
            "sex" in df.columns
            and "survived" in df.columns
        ):

            female_rate = df[
                df["sex"] == "female"
            ]["survived"].mean()

            male_rate = df[
                df["sex"] == "male"
            ]["survived"].mean()

            if female_rate > male_rate:

                results.append({

                    "message":
                    f"Claim supported. Female survival rate = {round(female_rate * 100, 2)}%",

                    "support_score":
                    round(female_rate * 100, 2)
                })

            else:

                results.append({

                    "message":
                    "Claim not supported.",

                    "support_score":
                    round(male_rate * 100, 2)
                })

    # CLAIM 2
    elif (
        "higher fare" in claim
        and "survived" in claim
    ):

        if (
            "fare" in df.columns
            and "survived" in df.columns
        ):

            high_fare = df[
                df["fare"] > df["fare"].mean()
            ]

            survival_rate = (
                high_fare["survived"]
                .mean()
            )

            if survival_rate > 0.7:

                results.append({

                    "message":
                    f"Claim partially supported. Survival rate = {round(survival_rate * 100, 2)}%",

                    "support_score":
                    round(survival_rate * 100, 2)
                })

            else:

                results.append({

                    "message":
                    f"Claim weakly supported. Survival rate = {round(survival_rate * 100, 2)}%",

                    "support_score":
                    round(survival_rate * 100, 2)
                })

    else:

        results.append({

            "message":
            "No validation rule available.",

            "support_score":
            0
        })

    return results