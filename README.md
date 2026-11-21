# 🛒 E-Commerce Customer Segmentation Using RFM Analysis

## 📌 Project Overview

This project focuses on analyzing e-commerce customer purchasing behaviour using **RFM Analysis and K-Means Clustering**.

The main objective is to identify different types of customers based on their purchasing history and spending patterns.

This analysis helps businesses understand their customers and make better marketing decisions.

## 🎯 Project Objectives

- Analyze customer purchasing behaviour.
- Identify high-value customers.
- Calculate Recency, Frequency and Monetary values.
- Group customers into different segments.
- Apply K-Means clustering using Machine Learning.
- Create an interactive Power BI dashboard.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Power BI

## 📊 Project Features

1. Data Cleaning and Preprocessing
2. RFM Analysis
3. RFM Customer Scoring
4. Customer Segmentation
5. K-Means Clustering
6. Data Visualization
7. Power BI Dashboard

## 📂 Project Structure

```text
E-Commerce-Customer-Segmentation/
│
├── data/
│   ├── cleaned_ecommerce.csv
│   ├── rfm_analysis.csv
│   ├── rfm_scored.csv
│   ├── customer_segments.csv
│   └── kmeans_customer_segments.csv
│
├── visualizations/
│   ├── customer_count.png
│   ├── customer_percentage.png
│   ├── revenue_by_segment.png
│   └── kmeans_clusters.png
│
├── data_analysis.py
├── visualization.py
├── clustering.py
├── Ecommerce_Customer_Dashboard.pbix
└── README.md
```

## 📈 RFM Analysis

RFM stands for:

- **Recency:** How recently a customer made a purchase.
- **Frequency:** How frequently a customer makes purchases.
- **Monetary:** How much money a customer spends.

## 👥 Customer Segments

The project identifies five customer groups:

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk
- Lost Customers

## 🤖 Machine Learning

K-Means clustering is applied to group customers based on their Recency, Frequency and Monetary values.

The data is standardized before applying the clustering algorithm.

## 📊 Power BI Dashboard

The interactive dashboard includes:

- Total Customers
- Total Revenue
- Average Customer Spending
- Customer Distribution by Segment
- Revenue by Customer Segment
- Customer Segment Percentage
- K-Means Customer Clustering

## ▶️ How to Run the Project

### Step 1: Install libraries

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn
```

### Step 2: Run data analysis

```bash
python data_analysis.py
```

### Step 3: Generate visualizations

```bash
python visualization.py
```

### Step 4: Run K-Means clustering

```bash
python clustering.py
```

### Step 5: Open Power BI Dashboard

Open `Ecommerce_Customer_Dashboard.pbix` using Power BI Desktop.

## 💡 Business Benefits

- Helps identify valuable customers.
- Supports customer retention strategies.
- Helps businesses understand purchasing patterns.
- Supports targeted marketing campaigns.
- Helps improve customer relationships.

## 👩‍💻 Author

**Raspreet Kaur**

BTech – Artificial Intelligence and Machine Learning

## ⭐ Conclusion

This project demonstrates the use of Data Analytics and Machine Learning techniques to understand e-commerce customer behaviour and perform customer segmentation.
