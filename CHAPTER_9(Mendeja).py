"""
Chapter 9: Real-World Application: Data Preprocessing (Complete)
Dataset: Titanic (train.csv)
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Filter warnings for a cleaner terminal output
warnings.filterwarnings('ignore')

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# ----------------------------------------------------------------------
# Step 2: Import the Necessary Libraries and Load the Data
# ----------------------------------------------------------------------
section("Step 2: Load Data")
data = pd.read_csv('train.csv')

print("--- First 5 rows ---")
print(data.head())
print("\n--- Statistical summary ---")
print(data.describe())
print("\n--- Brief overview ---")
data.info()

# ----------------------------------------------------------------------
# Step 3 & 4: Defining and Combining Preprocessing Steps
# ----------------------------------------------------------------------
section("Step 3 & 4: Building the Pipeline")

# Preprocessing for numerical columns
numerical_features = ['Age', 'Fare']
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Preprocessing for categorical columns
categorical_features = ['Embarked', 'Sex', 'Pclass']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine into a single preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])
print("Pipeline built successfully.")

# ----------------------------------------------------------------------
# Step 5: Applying the Preprocessing Pipeline
# ----------------------------------------------------------------------
section("Step 5: Applying the Pipeline")

# Fit and transform the data
titanic_preprocessed = preprocessor.fit_transform(data)
print("\nPreprocessed Data Array (First 2 rows):")
print(titanic_preprocessed[:2])

# ----------------------------------------------------------------------
# Evaluation of Preprocessed Data
# ----------------------------------------------------------------------
section("Evaluation: Data Quality Report")

# Convert preprocessed NumPy array back to DataFrame for evaluation
titanic_preprocessed_df = pd.DataFrame(
    titanic_preprocessed,
    columns=preprocessor.get_feature_names_out()
)

print("\nMissing values after preprocessing:")
print(titanic_preprocessed_df.isnull().sum())

# ----------------------------------------------------------------------
# Visualizations & Discretization
# ----------------------------------------------------------------------
section("Visualizations")
print("NOTE: Close each popup window to let the script continue to the next graph!")

# 1. Histogram (Before Discretization)
plt.figure()
plt.hist(data['Age'].dropna(), alpha=0.5, label='Before discretization')
plt.title("Age Distribution (Before)")
plt.legend()
plt.show()

# 2. Histogram (After Pipeline Transformation - Plotted exactly as course shows)
plt.figure()
plt.hist(titanic_preprocessed[:, 2], alpha=0.5, label='After discretization')
plt.title("Pipeline Transformation (Column 2)")
plt.legend()
plt.show()

# Data Discretization: Convert Age into bins for the remaining Seaborn plots
bins = [0, 12, 50, 200]
labels = ['Child', 'Adult', 'Elderly']
data['Age'] = pd.cut(data['Age'], bins=bins, labels=labels)

# 3. Survival count plot
plt.figure()
sns.countplot(x='Survived', data=data)
plt.title("Survival Count (0 = Did not survive, 1 = Survived)")
plt.show()

# 4. Survival by Passenger Class
plt.figure()
sns.countplot(x='Pclass', hue='Survived', data=data)
plt.title("Survival by Passenger Class")
plt.show()

# 5. Age Distribution of Survivors vs Non-Survivors
plt.figure(figsize=(10,6))
sns.histplot(data=data, x='Age', hue='Survived', bins=30, kde=True)
plt.title("Age Distribution by Survival")
plt.show()

# 6. Fare Distribution by Survival
plt.figure(figsize=(10,6))
sns.boxplot(x='Survived', y='Fare', data=data)
plt.title("Fare vs Survival")
plt.show()

# 7. Embarkation Port & Survival
plt.figure()
sns.countplot(x='Embarked', hue='Survived', data=data)
plt.title("Survival by Embarkation Port")
plt.show()

# 8. Family Size Effect
plt.figure()
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
sns.countplot(x='FamilySize', hue='Survived', data=data)
plt.title("Survival by Family Size")
plt.show()

# 9. Correlation Heatmap (numeric columns only)
plt.figure(figsize=(10,8))
sns.heatmap(data.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()