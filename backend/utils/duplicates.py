def detect_duplicates(df):

    duplicates = df.duplicated().sum()

    return int(duplicates)