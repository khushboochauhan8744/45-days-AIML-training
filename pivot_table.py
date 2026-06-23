import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers,on="customer_id")
merged = merged.merge(products,on="product_id")

print("Region vs Month")

pivot1 = pd.pivot_table(
merged,
values="sales",
index="region",
columns="month",
aggfunc="sum"
)

print(pivot1)

print()

print("Category vs Segment")

pivot2 = pd.pivot_table(
merged,
values="sales",
index="category",
columns="segment",
aggfunc="sum"
)

print(pivot2)