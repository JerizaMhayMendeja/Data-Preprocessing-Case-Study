"""
Chapter 6: Dealing with Outliers
"""
import numpy as np
import pandas as pd
from scipy import stats

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# ----------------------------------------------------------------------
# 1. Z-Score Method
# ----------------------------------------------------------------------
section("Outlier Detection: Z-Score Method")

# example data
data = np.array([10, 12, 12, 15, 20, 21, 22, 100])
print("Data Array:", data)

# calculate z-scores
z_scores = stats.zscore(data)
print("\nz_scores =", z_scores)

# find outliers
outliers = data[np.abs(z_scores) > 3]
print("\nOutliers:", outliers)

# ----------------------------------------------------------------------
# 2. Interquartile Range (IQR) Method
# ----------------------------------------------------------------------
section("Outlier Detection: IQR Method")

# example data (reusing same numbers, but as a pandas Series)
data_series = pd.Series([10, 12, 12, 15, 20, 21, 22, 100])
print("Data Series (head):\n", data_series.head())

# calculate IQR
Q1 = data_series.quantile(0.25)
Q3 = data_series.quantile(0.75)
IQR = Q3 - Q1
print("\nIQR =", IQR)

# find outliers
outliers_iqr = data_series[(data_series < (Q1 - 1.5 * IQR)) | (data_series > (Q3 + 1.5 * IQR))]
print("\nOutliers:\n", outliers_iqr)

# ----------------------------------------------------------------------
# Note on Strategies for Handling Outliers:
# 1. Capping & Flooring: Set boundaries and replace extreme outliers with the nearest boundary value.
# 2. Log Transformation: Compresses skewed data to reduce outlier impact.
# 3. Removing Outliers: Delete extreme values entirely (use only if error/irrelevant).
# ----------------------------------------------------------------------