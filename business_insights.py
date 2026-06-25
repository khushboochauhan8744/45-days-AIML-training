import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers,on="customer_id")
merged = merged.merge(products,on="product_id")

print("BUSINESS INSIGHTS")
print()

print("1. Total Revenue :", merged["sales"].sum())

print("2. Average Order Value :", merged["sales"].mean())

print()

print("3. Region Wise Sales")
print(merged.groupby("region")["sales"].sum())

print()

print("4. Category Wise Sales")
print(merged.groupby("category")["sales"].sum())

print()

print("5. Top Selling Product")
print(
merged.groupby("product_name")["sales"]
.sum()
.sort_values(ascending=False)
.head(1)
)

print()

print("6. Month Wise Sales")
print(
merged.groupby("month")["sales"].sum()
)

print()

print("Assignment Insights Generated Successfully")