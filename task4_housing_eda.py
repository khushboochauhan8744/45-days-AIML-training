import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")

# Dataset load (make sure housing.csv is in same folder)
df = pd.read_csv("housing.csv")

print("\nDataset Loaded Successfully!\n")

# -----------------------------
# 1. Basic Info
# -----------------------------
print("\n--- SHAPE ---")
print(df.shape)

print("\n--- INFO ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- STATISTICS ---")
print(df.describe())

# -----------------------------
# 2. Correlation Heatmap
# -----------------------------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# 3. House Price Distribution
# -----------------------------
plt.figure(figsize=(8,5))
sns.histplot(df["median_house_value"], bins=30, kde=True)
plt.title("Distribution of House Prices")
plt.show()

# -----------------------------
# 4. Income vs House Value
# -----------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="median_income", y="median_house_value", alpha=0.5)
plt.title("Income vs House Value")
plt.show()

# -----------------------------
# 5. Location Plot
# -----------------------------
plt.figure(figsize=(8,6))
sns.scatterplot(
    data=df,
    x="longitude",
    y="latitude",
    hue="median_house_value",
    palette="viridis",
    alpha=0.6
)
plt.title("House Prices by Location")
plt.show()