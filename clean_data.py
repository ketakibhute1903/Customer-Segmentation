import pandas as pd

# Load dataset
df = pd.read_excel("customer_segmentation_dataset.xlsx")

print("Original dataset shape:", df.shape)

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("After removing duplicates:", df.shape)

# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Handle missing Gender
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])

# Handle missing Income
if "Income" in df.columns:
    df["Income"] = df["Income"].fillna(df["Income"].median())

# Check missing values after cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check duplicates again
print("\nDuplicates after cleaning:", df.duplicated().sum())

# Save cleaned dataset
df.to_excel("customer_segmentation_cleaned.xlsx", index=False)

print("\nCleaned dataset saved successfully!")
print("Final dataset shape:", df.shape)