
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load RFM data
df = pd.read_csv("data/rfm_analysis.csv")

# Select RFM columns
X = df[["Recency", "Frequency", "Monetary"]]

# Apply log transformation
X_log = X.apply(lambda col: __import__("numpy").log1p(col))

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_log)

# Apply K-Means clustering
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

# Display cluster information
print("\nCUSTOMER CLUSTERING RESULTS:")
print(df.head(10))

print("\nCUSTOMERS IN EACH CLUSTER:")
print(df["Cluster"].value_counts().sort_index())

print("\nCLUSTER SUMMARY:")
print(df.groupby("Cluster")[
    ["Recency", "Frequency", "Monetary"]
].mean().round(2))

# Save results
df.to_csv("data/kmeans_customer_segments.csv", index=False)

# Create clustering visualization
plt.figure(figsize=(10, 6))

plt.scatter(
    df["Frequency"],
    df["Monetary"],
    c=df["Cluster"],
    cmap="viridis",
    alpha=0.6
)

plt.title("K-Means Customer Clustering")
plt.xlabel("Purchase Frequency")
plt.ylabel("Total Spending")
plt.colorbar(label="Cluster")
plt.tight_layout()

import os
os.makedirs("visualizations", exist_ok=True)

plt.savefig("visualizations/kmeans_clusters.png")
plt.show()

print("\nK-MEANS CLUSTERING COMPLETED!")
