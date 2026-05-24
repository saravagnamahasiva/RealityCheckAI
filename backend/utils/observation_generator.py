def generate_observations(df):

    observations = []

    # FEMALE SURVIVAL
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

            observations.append(
                "All females survived"
            )

    # FARE ANALYSIS
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

        if survival_rate > 0.5:

            observations.append(
                "Passengers with higher fare survived more"
            )
            observations.append(
    "Fare has no impact on survival"
)

    if len(observations) == 0:

        observations.append(
            "No major observations generated."
        )

    return observations