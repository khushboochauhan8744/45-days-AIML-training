import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers,on="customer_id")
merged = merged.merge(products,on="product_id")

print("Region Wise Sales")
print(merged.groupby("region")["sales"].sum())

print()

print("Category Wise Sales")
print(merged.groupby("category")["sales"].sum())

print()

print("Segment Wise Sales")
print(merged.groupby("segment")["sales"].sum())

print()

print("Region and Category")
print(merged.groupby(["region","category"])["sales"].sum())