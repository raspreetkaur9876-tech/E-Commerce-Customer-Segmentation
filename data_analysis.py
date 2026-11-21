
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_ecommerce.csv")

# Convert Date into datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Convert Total_Amount into numeric format
df["Total_Amount"] = pd.to_numeric(
    df["Total_Amount"], errors="coerce"
)

# Remove invalid records if any
df = df.dropna(subset=["Customer_ID", "Date", "Order_ID", "Total_Amount"])

# Set reference date
reference_date = df["Date"].max() + pd.Timedelta(days=1)

# Calculate RFM values
rfm = df.groupby("Customer_ID").agg(
    Recency=("Date", lambda x: (reference_date - x.max()).days),
    Frequency=("Order_ID", "nunique"),
    Monetary=("Total_Amount", "sum")
).reset_index()

# Display RFM analysis
print("\nRFM ANALYSIS:")
print(rfm.head(10))

# Display summary
print("\nRFM SUMMARY:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe())

# Save RFM dataset
rfm.to_csv("data/rfm_analysis.csv", index=False)

print("\nRFM ANALYSIS COMPLETED!")
print("File saved as data/rfm_analysis.csv")


# STEP 8: Calculate RFM Scores

# Recency: lower days = better score
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    5,
    labels=[5, 4, 3, 2, 1]
).astype(int)

# Frequency: higher orders = better score
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

# Monetary: higher spending = better score
rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

# Combined RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# Display results
print("\nRFM CUSTOMER SCORES:")
print(rfm.head(10))

# Save scored dataset
rfm.to_csv("data/rfm_scored.csv", index=False)

print("\nRFM SCORING COMPLETED!")


# STEP 9: Customer Segmentation

def customer_segment(row):

    r = row["R_Score"]
    f = row["F_Score"]
    m = row["M_Score"]

    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"

    elif r >= 3 and f >= 4:
        return "Loyal Customers"

    elif r >= 4 and f <= 2:
        return "Potential Loyalists"

    elif r <= 2 and f >= 3:
        return "At Risk"

    else:
        return "Lost Customers"


# Apply segmentation
rfm["Customer_Segment"] = rfm.apply(
    customer_segment, axis=1
)

# Display customer segments
print("\nCUSTOMER SEGMENTATION:")
print(rfm[["Customer_ID", "RFM_Score", "Customer_Segment"]].head(20))

# Count customers in each segment
print("\nSEGMENT COUNTS:")
print(rfm["Customer_Segment"].value_counts())

# Save final segmented dataset
rfm.to_csv("data/customer_segments.csv", index=False)

print("\nCUSTOMER SEGMENTATION COMPLETED!")
