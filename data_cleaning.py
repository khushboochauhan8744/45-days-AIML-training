import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# Standardize column names
customers.columns = customers.columns.str.lower()
products.columns = products.columns.str.lower()
orders.columns = orders.columns.str.lower()

# Remove duplicates
customers.drop_duplicates(inplace=True)
products.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)

# Check null values
customers.fillna("Unknown", inplace=True)
products.fillna("Unknown", inplace=True)
orders.fillna(0, inplace=True)

print(customers)
print(products)
print(orders)

print("Data Cleaned Successfully")