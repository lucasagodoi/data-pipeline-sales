"""
Data Pipeline Sales Project

Author: Lucas Abreu Godoi
Description: ETL pipeline for cleaning and transforming sales data using Python and Pandas.
"""
import pandas as pd

# Extract
df = pd.read_csv("data/raw_sales.csv")

print("Raw data loaded:")
print(df.head())
print("\nInitial shape:", df.shape)

# Transform

# Remove duplicates
df = df.drop_duplicates()

# Drop rows with missing critical values
df = df.dropna(subset=["units_sold", "unit_price", "date"])

# Standardize text columns
df["product"] = df["product"].str.title()
df["category"] = df["category"].str.title()
df["region"] = df["region"].str.title()

# Convert data types
df["units_sold"] = df["units_sold"].astype(int)
df["unit_price"] = df["unit_price"].astype(float)
df["date"] = pd.to_datetime(df["date"])

# Create revenue column
df["revenue"] = df["units_sold"] * df["unit_price"]

print("\nCleaned data preview:")
print(df.head())
print("\nFinal shape:", df.shape)

# Load
df.to_csv("output/clean_sales.csv", index=False)

print("\nClean data saved to output/clean_sales.csv")