import pandas as pd

# Load CSV files
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# Display datasets
print("CUSTOMERS")
print(customers)

print("\nPRODUCTS")
print(products)

print("\nORDERS")
print(orders)

# Shape
print("\nCustomers Shape:", customers.shape)
print("Products Shape:", products.shape)
print("Orders Shape:", orders.shape)

# Columns
print("\nCustomer Columns")
print(customers.columns)

print("\nProduct Columns")
print(products.columns)

print("\nOrder Columns")
print(orders.columns)

# Data Types
print("\nCustomer Info")
print(customers.info())

print("\nProduct Info")
print(products.info())

print("\nOrder Info")
print(orders.info())

# Missing Values
print("\nMissing Values")
print(customers.isnull().sum())
print(products.isnull().sum())
print(orders.isnull().sum())

# Duplicate Rows
print("\nDuplicates")
print(customers.duplicated().sum())
print(products.duplicated().sum())
print(orders.duplicated().sum())

# Unique Values
print("\nUnique Regions")
print(customers["region"].unique())

print("\nUnique Segments")
print(customers["segment"].unique())

print("\nUnique Categories")
print(products["category"].unique())

print("\nUnique Months")
print(orders["month"].unique())