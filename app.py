import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Cafe Sales Dashboard",
    page_icon="☕",
    layout="wide"
)


# -----------------------------
# Load Data
# -----------------------------

df = pd.read_csv("cleaned_cafe_sales.csv")

df["Transaction Date"] = pd.to_datetime(
    df["Transaction Date"]
)


# -----------------------------
# Title
# -----------------------------

st.title("☕ Cafe Sales Dashboard")

st.markdown(
    "Interactive analysis of cafe sales transactions"
)


# -----------------------------
# KPIs
# -----------------------------

total_revenue = df["Total Spent"].sum()

total_transactions = df["Transaction ID"].nunique()

total_items = df["Quantity"].sum()

average_transaction = df["Total Spent"].mean()


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Revenue",
        f"${total_revenue:,.2f}"
    )


with col2:
    st.metric(
        "Transactions",
        f"{total_transactions:,}"
    )


with col3:
    st.metric(
        "Items Sold",
        f"{total_items:,.0f}"
    )


with col4:
    st.metric(
        "Avg Transaction",
        f"${average_transaction:,.2f}"
    )


# ----------------------------- Adding filters -----------------------------

st.sidebar.header("Filters")


# Item filter
items = ["All"] + sorted(
    df["Item"].dropna().unique().tolist()
)

selected_item = st.sidebar.selectbox(
    "Select Item",
    items
)


# Location filter
locations = ["All"] + sorted(
    df["Location"].dropna().unique().tolist()
)

selected_location = st.sidebar.selectbox(
    "Select Location",
    locations
)


# Payment filter
payments = ["All"] + sorted(
    df["Payment Method"].dropna().unique().tolist()
)

selected_payment = st.sidebar.selectbox(
    "Payment Method",
    payments
)


# Apply filters

filtered_df = df.copy()


if selected_item != "All":
    filtered_df = filtered_df[
        filtered_df["Item"] == selected_item
    ]


if selected_location != "All":
    filtered_df = filtered_df[
        filtered_df["Location"] == selected_location
    ]


if selected_payment != "All":
    filtered_df = filtered_df[
        filtered_df["Payment Method"] == selected_payment
    ]


#-----------------------------sales Trend-----------------------------


st.subheader("📈 Sales Trend")

daily_sales = (
    filtered_df
    .groupby("Transaction Date")["Total Spent"]
    .sum()
    .reset_index()
)

fig = px.line(
    daily_sales,
    x="Transaction Date",
    y="Total Spent",
    title="Daily Sales"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


#-----------------------------Item Analysis-----------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("☕ Sales by Item")

    item_sales = (
        filtered_df
        .groupby("Item")["Total Spent"]
        .sum()
        .reset_index()
        .sort_values(
            "Total Spent",
            ascending=False
        )
    )

    fig = px.bar(
        item_sales,
        x="Item",
        y="Total Spent",
        title="Revenue by Item"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    st.subheader("📦 Items Sold")

    item_quantity = (
        filtered_df
        .groupby("Item")["Quantity"]
        .sum()
        .reset_index()
        .sort_values(
            "Quantity",
            ascending=False
        )
    )

    fig = px.bar(
        item_quantity,
        x="Item",
        y="Quantity",
        title="Quantity Sold by Item"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

#-----------------------------Payment Method Analysis-----------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("💳 Payment Methods")

    payment_data = (
        filtered_df
        .groupby("Payment Method")["Total Spent"]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        payment_data,
        names="Payment Method",
        values="Total Spent",
        title="Revenue by Payment Method"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    st.subheader("📍 Location Sales")

    location_data = (
        filtered_df
        .groupby("Location")["Total Spent"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        location_data,
        x="Location",
        y="Total Spent",
        title="Revenue by Location"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )