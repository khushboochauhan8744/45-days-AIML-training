import pandas as pd
import matplotlib.pyplot as plt

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

merged = orders.merge(customers,on="customer_id")
merged = merged.merge(products,on="product_id")

# Histogram

plt.hist(merged["sales"])
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot

plt.scatter(merged["quantity"],merged["sales"])
plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")
plt.show()

# Bar Chart

merged.groupby("region")["sales"].sum().plot(kind="bar")
plt.title("Region Wise Sales")
plt.show()

# Line Chart

merged.groupby("month")["sales"].sum().plot()
plt.title("Monthly Sales")
plt.show()

# Box Plot

plt.boxplot(merged["sales"])
plt.title("Sales Boxplot")
plt.show()

# Heatmap

pivot = pd.pivot_table(
merged,
values="sales",
index="region",
columns="month",
aggfunc="sum"
)

plt.imshow(pivot)
plt.colorbar()
plt.title("Heatmap")
plt.show()