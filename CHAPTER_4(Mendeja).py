"""
Chapter 4: Unleashing the Power of Data Through Transformation and Feature Engineering
Topic: Feature Engineering, Binning, Interaction, Polynomials, and Encoding
"""
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Reusing your section formatting for consistency
def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# ----------------------------------------------------------------------
# 1. Basics & Feature Engineering
# ----------------------------------------------------------------------
section("Feature Engineering: Lemonade per Degree")

# Sample data
data = {
    'Temperature': [75, 77, 82, 85, 89, 91, 95],
    'Lemonade Sold': [30, 35, 50, 55, 60, 65, 80]
}
df = pd.DataFrame(data)

# Create new feature
df['Lemonade per Degree'] = df['Lemonade Sold'] / df['Temperature']
print(df.head())

# ----------------------------------------------------------------------
# 2. Binning
# ----------------------------------------------------------------------
section("Binning: Temperature Categories")

# Define bins and labels
bins = [70, 75, 85, 95, 100]
labels = ['cool', 'warm', 'hot', 'very hot']

# Apply binning
df['Temperature Category'] = pd.cut(df['Temperature'], bins=bins, labels=labels)
print(df.head())

# ----------------------------------------------------------------------
# 3. Interaction Features
# ----------------------------------------------------------------------
section("Interaction Features: Ice Cubes per Degree")

# Add Ice Cubes data
df['Ice Cubes'] = [100, 110, 120, 130, 140, 150, 200]

# Create interaction feature
df['Ice Cubes per Degree'] = df['Ice Cubes'] / df['Temperature']
print(df.head())

# ----------------------------------------------------------------------
# 4. Polynomial Features
# ----------------------------------------------------------------------
section("Polynomial Features: Temperature Squared")

# Create polynomial feature
df['Temperature Squared'] = df['Temperature'] ** 2
print(df.head())

# ----------------------------------------------------------------------
# 5. Categorical Variable Encoding (One-hot Encoding)
# ----------------------------------------------------------------------
section("One-hot Encoding: Weather")

# Example data
data_2 = {'Weather': ['Sunny', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy']}
df_2 = pd.DataFrame(data_2)

# Apply one-hot encoding
df_encoded = pd.get_dummies(df_2, columns=['Weather'])
print(df_encoded.head())

# ----------------------------------------------------------------------
# 6. Categorical Variable Encoding (Ordinal Encoding)
# ----------------------------------------------------------------------
section("Ordinal Encoding: Ice Amount")

# Example data
data_3 = {'Ice': ['Little', 'Medium', 'Lots', 'Little', 'Lots']}
df_3 = pd.DataFrame(data_3)

# Create encoder
ord_enc = OrdinalEncoder(categories=[['Little', 'Medium', 'Lots']])

# Apply ordinal encoding
df_3['Ice_encoded'] = ord_enc.fit_transform(df_3[['Ice']])
print(df_3.head())