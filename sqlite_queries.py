import pandas as pd
import sqlite3

# Load CSV files
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# Create Database
conn = sqlite3.connect("sales.db")

# Store tables
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)

print("Database Created Successfully\n")

# Query 1
print("CUSTOMERS TABLE")
print(pd.read_sql("SELECT * FROM customers", conn))

# Query 2
print("\nORDERS WITH SALES > 5000")
print(pd.read_sql(
    "SELECT * FROM orders WHERE sales > 5000",
    conn
))

# Query 3
print("\nTOTAL SALES BY CUSTOMER")
print(pd.read_sql(
    """
    SELECT customer_id,
    SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
    """,
    conn
))

# Query 4
print("\nJOIN QUERY")
print(pd.read_sql(
    """
    SELECT
    o.order_id,
    c.customer_name,
    o.sales
    FROM orders o
    JOIN customers c
    ON o.customer_id = c.customer_id
    """,
    conn
))

# Query 5
print("\nTOP SALES")
print(pd.read_sql(
    """
    SELECT *
    FROM orders
    ORDER BY sales DESC
    """,
    conn
))

conn.close()

print("\nSQL Assignment Completed")