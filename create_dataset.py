import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "customer_name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "region": ["North", "South", "East", "West", "North"],
    "segment": ["Consumer", "Corporate", "Home Office", "Consumer", "Corporate"]
})

products = pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105],
    "product_name": ["Laptop", "Phone", "Tablet", "Mouse", "Keyboard"],
    "category": ["Technology", "Technology", "Technology", "Accessories", "Accessories"]
})

orders = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "customer_id": [1, 2, 3, 4, 5],
    "product_id": [101, 102, 103, 104, 105],
    "sales": [50000, 30000, 20000, 1500, 2500],
    "quantity": [1, 2, 1, 3, 2],
    "month": ["Jan", "Feb", "Mar", "Apr", "May"]
})

customers.to_csv("customers.csv", index=False)
products.to_csv("products.csv", index=False)
orders.to_csv("orders.csv", index=False)

print("All CSV files created successfully!")