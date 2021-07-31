def f_fillna(df):
    for x in df:
        df[x] = df[x].fillna(0)

    return df