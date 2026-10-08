"""
Chapter 5: Unfolding the Essentials of Data Scaling and Normalization
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# ----------------------------------------------------------------------
# Data Scaling: Leveling the Playing Field
# ----------------------------------------------------------------------
section("Data Scaling (StandardScaler)")

# example data
data = {
    'Study Hours': [10, 15, 8, 9, 12, 14, 13],
    'Grades': [85, 90, 76, 81, 87, 92, 88]
}
df = pd.DataFrame(data)
print("Original Data (head):")
print(df.head())

# scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

print("\nScaled Data Array:")
print(scaled_data)

# ----------------------------------------------------------------------
# Data Normalization
# ----------------------------------------------------------------------
section("Data Normalization (MinMaxScaler)")

# example data
data_2 = {
    'Study Hours': [10, 15, 8, 9, 12, 14, 13],
    'Grades': [85, 90, 76, 81, 87, 92, 88]
}
df_2 = pd.DataFrame(data_2)

# normalize the data
scaler_minmax = MinMaxScaler()
normalized_data = scaler_minmax.fit_transform(df_2)

print("\nNormalized Data Array:")
print(normalized_data)