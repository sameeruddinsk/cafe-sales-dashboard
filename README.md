# ☕ Cafe Sales Analysis & Interactive Dashboard

## 📌 Project Overview

This project analyzes cafe sales transaction data and presents the results through an interactive dashboard.

The raw dataset contains sales transactions with missing values, invalid entries, and inconsistent data. Python and Pandas were used to clean and transform the data before creating an interactive dashboard using Streamlit and Plotly.

The dashboard helps users understand sales performance, product performance, payment methods, and location-wise sales.

## 🎯 Objectives

* Clean and prepare raw cafe sales data
* Handle missing and invalid values
* Analyze sales and transaction trends
* Identify top-performing products
* Analyze payment methods
* Compare sales across locations
* Build an interactive dashboard
* Generate useful business insights

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data cleaning and analysis
* **NumPy** – Numerical operations
* **Plotly** – Interactive visualizations
* **Streamlit** – Dashboard development
* **Git & GitHub** – Version control and project hosting

## 📊 Dataset

The dataset contains cafe transaction information including:

* Transaction ID
* Item
* Quantity
* Price Per Unit
* Total Spent
* Payment Method
* Location
* Transaction Date

The dataset contains approximately **10,000 transaction records**.

## 🧹 Data Cleaning

The following data-cleaning steps were performed using Python and Pandas:

* Identified missing values
* Replaced invalid values such as `ERROR` and `UNKNOWN`
* Converted numeric columns to appropriate data types
* Converted transaction dates into datetime format
* Handled missing categorical values
* Handled missing numeric values
* Recalculated `Total Spent` using:

```text
Total Spent = Quantity × Price Per Unit
```

* Removed duplicate transactions
* Removed records with invalid transaction dates

## 📈 Dashboard Features

The interactive dashboard provides:

### KPI Metrics

* 💰 Total Revenue
* 🧾 Total Transactions
* 📦 Total Items Sold
* 💵 Average Transaction Value

### Visualizations

* 📈 Daily Sales Trend
* ☕ Revenue by Product
* 📦 Quantity Sold by Product
* 💳 Revenue by Payment Method
* 📍 Revenue by Location

### Interactive Filters

Users can filter the dashboard by:

* Product
* Location
* Payment Method

The charts and KPIs update based on the selected filters.

## 💡 Business Insights

The dashboard can help cafe management:

* Identify the highest-revenue products
* Understand sales trends over time
* Determine which locations perform best
* Understand customer payment preferences
* Compare product performance
* Identify opportunities to improve sales

## 📂 Project Structure

```text
Cafe-Sales-Dashboard/
│
├── app.py
├── clean_data.py
├── analysis.py
├── dirty_cafe_sales.csv
├── cleaned_cafe_sales.csv
├── requirements.txt
└── README.md
```

## 🚀 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/cafe-sales-dashboard.git
```

### 2. Navigate to the project folder

```bash
cd cafe-sales-dashboard
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 🌐 Live Dashboard

**Live Demo:**
Add your Streamlit deployment link here.

```text
https://cafe-sales-dashboard-by-sameeruddin.streamlit.app/
```

## 📸 Dashboard Preview

Add a screenshot of your dashboard here after deployment.
<p align="center">
  <img src="./Screenshot 2026-09-14 131548.png.png" width="100%" alt="Banner"/>
</p>
![Uploading Screenshot 2026-09-14 131548.png…]()

## 📚 Skills Demonstrated

This project demonstrates practical skills in:

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis
* Data Aggregation
* GroupBy Analysis
* KPI Development
* Data Visualization
* Dashboard Development
* Business Intelligence
* Python Programming
* Pandas
* Streamlit
* Plotly

## 👨‍💻 Author

**Shaik Sameeruddin**

B.Tech – Artificial Intelligence & Machine Learning

### 🔗 Connect With Me

* GitHub: Add your GitHub profile link
* LinkedIn: Add your LinkedIn profile link

---

⭐ If you find this project useful, consider giving the repository a star!
