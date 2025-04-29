import psycopg2

def load(df,conn_params):
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    for _,row in df.iterrows():
        cursor.execute(
            "INSERT INTO sales (order_id, product, quantity, price, order_date, total) VALUES (%s, %s, %s, %s, %s, %s)",
            (row['order_id'], row['product'], row['quantity'], row['price'], row['order_date'], row['total'])
        )
    conn.commit()
    cursor.close()
    conn.close()