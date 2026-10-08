"""
Data Preprocessing: Chapters 1-3 (integrated)
Dataset: Video Game Sales
"""
 
import numpy as np
import pandas as pd
 
# Show all columns when printing (so describe()/head() don't get cut off)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
 
CSV_PATH = "vgsales.csv"  # change this if your file is somewhere else
 
 
def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)
 
 
# ----------------------------------------------------------------------
# CHAPTER 2: Loading, Understanding, and Exploring Data
# ----------------------------------------------------------------------
section("CHAPTER 2 | Step 3: Loading Data")
df = pd.read_csv(CSV_PATH)
print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns.")
 
section("CHAPTER 2 | Step 4: Understanding Data Types")
# 'object' = string/categorical, 'int64'/'float64' = numeric
print(df.dtypes)
 
section("CHAPTER 2 | Step 5: Basic Data Exploration")
 
print("\n# First five rows")
print(df.head())
 
print("\n# Statistical summary")
print(df.describe())
 
print("\n# Brief overview")
df.info()  # info() prints by itself; no need to wrap it in print()
 
 
# ----------------------------------------------------------------------
# CHAPTER 3: Cleaning Your Data
# ----------------------------------------------------------------------
section("CHAPTER 3 | Step 2: Locate Missing Values")
print(df.isnull().sum())
 
section("CHAPTER 3 | Step 3: Handle Missing Values")
 
# Imputation
#   Year (numeric)         -> mean imputation
#   Publisher (categorical) -> mode (most frequent) imputation
# Note: we assign back to the column instead of using inplace=True,
# which avoids the pandas FutureWarning (inplace on a column won't
# work in pandas 3.0).
df["Year"] = df["Year"].fillna(df["Year"].mean())
df["Publisher"] = df["Publisher"].fillna(df["Publisher"].mode()[0])
 
# Deletion (alternative to imputation, shown for reference).
# Use this INSTEAD of imputing Publisher if you prefer to drop those rows:
# df = df[df["Publisher"].notna()]
 
# Prediction (using ML models to estimate missing values) is the third
# strategy. It is more complex, so it is not applied here.
 
section("CHAPTER 3 | Step 5: Confirm Your Results")
print(df.isnull().sum())
print("\nMissing values in 'Year' and 'Publisher' should now be zero.")
 
section("CHAPTER 3 | Step 6: Eliminate Redundancies")
 
# Duplicate entries
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicates after: ", df.duplicated().sum())
 
# Irrelevant features: drop the Rank column
df = df.drop(["Rank"], axis=1)
 
# Noisy data: treat games with Global_Sales > 40M as outliers and remove them
df = df[df["Global_Sales"] <= 40]
 
section("CHAPTER 3 | Step 4: Validate Your Results")
print(df.head())
print(f"\nFinal shape: {df.shape[0]} rows, {df.shape[1]} columns")
 
# Optional: save the cleaned data to a new CSV file
# df.to_csv("vgsales_cleaned.csv", index=False)
 
