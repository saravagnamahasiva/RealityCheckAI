def check_missing_values(df):

    missing = df.isnull().sum()

    return missing.to_dict()