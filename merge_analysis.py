import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers,on="customer_id")
merged = merged.merge(products,on="product_id")

print(merged)

print("\nTotal Revenue")
print(merged["sales"].sum())

print("\nAverage Order Value")
print(merged["sales"].mean())

print("\nTop Selling Products")
print(
merged.groupby("product_name")["sales"].sum().sort_values(ascending=False)
)