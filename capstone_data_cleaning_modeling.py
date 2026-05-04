"""
Housing Affordability in Maricopa County

This script cleans the PolicyMap housing dataset, prepares it for analysis,
creates a price-to-income ratio, checks for outliers, calculates correlation,
exports a cleaned CSV file, and creates Python visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# 1. Load Raw Dataset
# -----------------------------

raw_file = "maricopa_housing_data.csv"

df = pd.read_csv(raw_file)

print("Initial dataset preview:")
print(df.head())

print("\nDataset information:")
print(df.info())


# -----------------------------
# 2. Rename Columns
# -----------------------------

df = df.rename(columns={
    "Zip Code Tabulation Area, 2020": "zip_code",
    "Estimated median income of a household, between 2020-2024.": "median_income",
    "Estimated median value of an owner-occupied home, between 2020-2024.": "median_home_value"
})

print("\nColumns after renaming:")
print(df.columns)


# -----------------------------
# 3. Clean Data Types
# -----------------------------

df["zip_code"] = df["zip_code"].astype(str)

df["median_income"] = pd.to_numeric(df["median_income"], errors="coerce")
df["median_home_value"] = pd.to_numeric(df["median_home_value"], errors="coerce")


# -----------------------------
# 4. Handle Missing Values
# -----------------------------

print("\nMissing values before cleaning:")
print(df[["median_income", "median_home_value"]].isnull().sum())

df = df.dropna(subset=["median_income", "median_home_value"])

print("\nMissing values after cleaning:")
print(df[["median_income", "median_home_value"]].isnull().sum())


# -----------------------------
# 5. Create Price-to-Income Ratio
# -----------------------------

df["price_to_income_ratio"] = df["median_home_value"] / df["median_income"]


# -----------------------------
# 6. Summary Statistics
# -----------------------------

print("\nSummary statistics:")
print(df[["median_income", "median_home_value", "price_to_income_ratio"]].describe())


# -----------------------------
# 7. Outlier Detection Using IQR
# -----------------------------

def identify_iqr_outliers(dataframe, column_name):
    q1 = dataframe[column_name].quantile(0.25)
    q3 = dataframe[column_name].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = dataframe[
        (dataframe[column_name] < lower_bound) |
        (dataframe[column_name] > upper_bound)
    ]

    return outliers, lower_bound, upper_bound


home_value_outliers, home_lower, home_upper = identify_iqr_outliers(
    df,
    "median_home_value"
)

print("\nHome value outlier bounds:")
print(f"Lower bound: {home_lower}")
print(f"Upper bound: {home_upper}")

print("\nPotential home value outliers:")
print(home_value_outliers[[
    "zip_code",
    "median_income",
    "median_home_value",
    "price_to_income_ratio"
]])


# -----------------------------
# 8. Correlation Analysis
# -----------------------------

correlation = df["median_income"].corr(df["median_home_value"])

print("\nCorrelation between median income and median home value:")
print(round(correlation, 3))


# -----------------------------
# 9. Export Cleaned Dataset
# -----------------------------

cleaned_file = "maricopa_housing_data_cleaned.csv"
df.to_csv(cleaned_file, index=False)

print(f"\nCleaned dataset saved as: {cleaned_file}")


# -----------------------------
# 10. Scatter Plot
# -----------------------------

plt.figure(figsize=(8, 6))
plt.scatter(df["median_income"], df["median_home_value"])
plt.xlabel("Median Household Income ($)")
plt.ylabel("Median Home Value ($)")
plt.title("Median Household Income vs. Median Home Value")
plt.grid(True)
plt.tight_layout()
plt.savefig("income_vs_home_value_scatter.png", dpi=300)
plt.show()


# -----------------------------
# 11. Top 10 Home Values Bar Chart
# -----------------------------

top_10_home_values = df.sort_values(
    by="median_home_value",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_10_home_values["zip_code"],
    top_10_home_values["median_home_value"]
)
plt.xlabel("Median Home Value ($)")
plt.ylabel("ZIP Code")
plt.title("Top 10 ZIP Codes by Median Home Value")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_home_values_by_zip.png", dpi=300)
plt.show()


# -----------------------------
# 12. Top 10 Price-to-Income Ratios
# -----------------------------

top_10_ratios = df.sort_values(
    by="price_to_income_ratio",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
plt.barh(
    top_10_ratios["zip_code"],
    top_10_ratios["price_to_income_ratio"]
)
plt.xlabel("Price-to-Income Ratio")
plt.ylabel("ZIP Code")
plt.title("Top 10 ZIP Codes by Price-to-Income Ratio")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_10_price_to_income_ratios.png", dpi=300)
plt.show()


print("\nPython analysis complete.")