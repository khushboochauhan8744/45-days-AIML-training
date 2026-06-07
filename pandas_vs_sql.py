import pandas as pd
import sqlite3

orders = pd.read_csv("orders.csv")

print("PANDAS")

print(
orders.groupby("customer_id")["sales"].sum()
)

conn = sqlite3.connect("sales.db")

orders.to_sql(
"orders",
conn,
if_exists="replace",
index=False
)

print()

print("SQL")

query = """
SELECT customer_id,
SUM(sales)
AS TotalSales
FROM orders
GROUP BY customer_id
"""

print(
pd.read_sql(
query,
conn
)
)

conn.close()

print()

print("Comparison Completed")