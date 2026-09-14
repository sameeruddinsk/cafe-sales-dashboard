import pandas as pd
import numpy as np

# -----------------------------
# 1. Load data
# -----------------------------

df = pd.read_csv("dirty_cafe_sales.csv")

print("Original shape:", df.shape)


# -----------------------------
# 2. Replace invalid values
# -----------------------------

df = df.replace(["ERROR", "UNKNOWN", ""], np.nan)


# -----------------------------
# 3. Convert numeric columns
# -----------------------------

numeric_columns = [
    "Quantity",
    "Price Per Unit",
    "Total Spent"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")


# -----------------------------
# 4. Convert date
# -----------------------------

df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"],
    errors="coerce"
)


# -----------------------------
# 5. Handle missing values
# -----------------------------

# Item
df["Item"] = df["Item"].fillna("Unknown")

# Payment Method
df["Payment Method"] = df["Payment Method"].fillna("Unknown")

# Location
df["Location"] = df["Location"].fillna("Unknown")


# -----------------------------
# 6. Fill numeric missing values
# -----------------------------

df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)

df["Price Per Unit"] = df["Price Per Unit"].fillna(
    df["Price Per Unit"].median()
)


# -----------------------------
# 7. Recalculate Total Spent
# -----------------------------

df["Total Spent"] = (
    df["Quantity"] * df["Price Per Unit"]
)


# -----------------------------
# 8. Remove invalid dates
# -----------------------------

df = df.dropna(
    subset=["Transaction Date"]
)


# -----------------------------
# 9. Remove duplicate transactions
# -----------------------------

df = df.drop_duplicates(
    subset=["Transaction ID"]
)


# -----------------------------
# 10. Save cleaned data
# -----------------------------

df.to_csv(
    "cleaned_cafe_sales.csv",
    index=False
)


print("Cleaned shape:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

print("\nCleaning completed!")