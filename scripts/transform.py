def transfor(df):
    df = df.dropna()
    df['total'] = df['quantity'] * df['price']
    return df