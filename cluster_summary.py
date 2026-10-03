import pandas as pd

# Load segmented dataset
df = pd.read_excel("customer_segments.xlsx")

# Create cluster summary
summary = df.groupby("Cluster").agg(
    Customers=("CustomerID", "count"),
    Average_Income=("Income", "mean"),
    Average_Frequency=("Frequency", "mean"),
    Average_Monetary=("Monetary", "mean")
).round(2)

print("\nCUSTOMER SEGMENT SUMMARY")
print("========================")
print(summary)

# Save summary
summary.to_excel("cluster_summary.xlsx")

print("\nSummary saved as: cluster_summary.xlsx")