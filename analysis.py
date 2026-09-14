import pandas as pd

df = pd.read_csv("cleaned_cafe_sales.csv")

# Convert date
df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"]
)


# -----------------------------
# KPI
# -----------------------------

total_revenue = df["Total Spent"].sum()

total_transactions = df["Transaction ID"].nunique()

total_items = df["Quantity"].sum()

average_transaction = df["Total Spent"].mean()


print("Total Revenue:", total_revenue)

print("Total Transactions:", total_transactions)

print("Total Items Sold:", total_items)

print("Average Transaction:", average_transaction)


# -----------------------------
# Sales by Item
# -----------------------------

item_sales = (
    df.groupby("Item")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\nSales by Item:")
print(item_sales)


# -----------------------------
# Quantity by Item
# -----------------------------

item_quantity = (
    df.groupby("Item")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\nQuantity by Item:")
print(item_quantity)


# -----------------------------
# Payment Method
# -----------------------------

payment_sales = (
    df.groupby("Payment Method")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\nPayment Method:")
print(payment_sales)


# -----------------------------
# Location
# -----------------------------

location_sales = (
    df.groupby("Location")["Total Spent"]
    .sum()
    .sort_values(ascending=False)
)

print("\nLocation:")
print(location_sales)


# -----------------------------
# Monthly Sales
# -----------------------------

df["Month"] = df["Transaction Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Total Spent"]
    .sum()
)

print("\nMonthly Sales:")
print(monthly_sales)