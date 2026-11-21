
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load customer segmentation data
df = pd.read_csv("data/customer_segments.csv")

# Set graph style
sns.set_theme(style="whitegrid")

# Create output folder
import os
os.makedirs("visualizations", exist_ok=True)

# GRAPH 1: Customer count by segment
plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Customer_Segment",
    hue="Customer_Segment",
    order=df["Customer_Segment"].value_counts().index,
    palette="viridis",
    legend=False
)

plt.title("Customer Count by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("visualizations/customer_count.png")
plt.show()

# GRAPH 2: Customer segment percentage
plt.figure(figsize=(8, 8))

df["Customer_Segment"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Customer Segment Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("visualizations/customer_percentage.png")
plt.show()

# GRAPH 3: Revenue by customer segment
plt.figure(figsize=(10, 6))

sns.barplot(
    data=df,
    x="Customer_Segment",
    y="Monetary",
    hue="Customer_Segment",
    estimator="sum",
    errorbar=None,
    palette="magma",
    legend=False
)

plt.title("Total Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Total Revenue")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("visualizations/revenue_by_segment.png")
plt.show()

print("ALL GRAPHS CREATED SUCCESSFULLY!")
