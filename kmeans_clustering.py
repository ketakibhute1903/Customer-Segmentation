import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load cleaned dataset
df = pd.read_excel("customer_segmentation_cleaned.xlsx")

# Select features
features = ["Income", "Frequency", "Monetary"]

X = df[features]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means with 4 clusters
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

# Create cluster labels
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Display number of customers in each cluster
print("\nNumber of customers in each cluster:")
print(df["Cluster"].value_counts().sort_index())

# Display cluster characteristics
print("\nCluster characteristics:")
cluster_summary = df.groupby("Cluster")[features].mean()
print(cluster_summary)

# Save clustered dataset
df.to_excel("customer_segments.xlsx", index=False)

print("\nCustomer segmentation completed!")
print("File saved as: customer_segments.xlsx")

# Visualize clusters
# Visualize customer segments
plt.figure(figsize=(10, 6))

for cluster in sorted(df["Cluster"].unique()):
    cluster_data = df[df["Cluster"] == cluster]

    plt.scatter(
        cluster_data["Income"],
        cluster_data["Monetary"],
        s=60,
        label=f"Cluster {cluster}"
    )

plt.xlabel("Annual Income")
plt.ylabel("Monetary Value")
plt.title("Customer Segmentation using K-Means")
plt.legend()
plt.grid(True)

plt.show()