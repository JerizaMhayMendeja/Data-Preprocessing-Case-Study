"""
Chapter 8: Constructing a Preprocessing Pipeline
Dataset: Titanic (train.csv)
"""
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# ----------------------------------------------------------------------
# Step 1 & 2: Loading the Dataset
# ----------------------------------------------------------------------
section("Step 2: Loading the Dataset")

# Load the data (make sure train.csv is in your VS Code folder)
data = pd.read_csv('train.csv')
print("Successfully loaded train.csv")

section("Dataset Exploration")
print("\n--- First 5 Rows ---")
print(data.head())

print("\n--- Statistical Summary ---")
print(data.describe())

print("\n--- Dataset Info ---")
data.info()

# ----------------------------------------------------------------------
# Step 3: Splitting the Dataset into Features and Target Variables
# ----------------------------------------------------------------------
section("Step 3: Splitting Dataset (X and y)")

# Split the data into features (X) and target variable (y)
X = data.drop('Survived', axis=1)
y = data['Survived']

print("Features (X) shape:", X.shape)
print("Target (y) shape:", y.shape)

# ----------------------------------------------------------------------
# Step 4: Defining and Applying the Preprocessing Pipeline
# ----------------------------------------------------------------------
section("Step 4: Defining and Applying the Pipeline")

# Define preprocessing pipeline for imputation and scaling
pipeline = Pipeline(steps=[
    ('imputation', SimpleImputer(strategy='mean')),
    ('scaling', StandardScaler())
])

# Apply pipeline specifically to the 'Age' and 'Fare' columns
preprocessor = ColumnTransformer(transformers=[
    ('age_fare', pipeline, ['Age', 'Fare'])
])

# Fit and transform the data
X_transformed = preprocessor.fit_transform(X)

print("Pipeline successfully applied!")
print("\nTransformed Data Array (First 5 rows of Age & Fare):")
print(X_transformed[:5])