"""
Chapter 7: Feature Selection
"""
import numpy as np
import pandas as pd
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
from sklearn.linear_model import LassoCV
import warnings

# We filter warnings here to keep the terminal output clean.
# Using 5-fold cross validation (cv=5) on a tiny 7-row dataset often triggers 
# "UndefinedMetricWarning" in sklearn, which is expected but messy to read.
warnings.filterwarnings("ignore")

def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

# ----------------------------------------------------------------------
# 1. Understanding Correlation
# ----------------------------------------------------------------------
section("1. Understanding Correlation")

# example data
data = {
    'Study Hours': [10, 15, 8, 9, 12, 14, 13],
    'Assignments Completed': [5, 7, 4, 5, 6, 7, 6],
    'Extracurricular Activities': [3, 1, 4, 2, 3, 1, 2],
    'Final Grade': [85, 90, 76, 81, 87, 92, 88]
}
df = pd.DataFrame(data)
print("Data Head:\n", df.head())

# calculate correlations
correlations = df.corr()
print("\nCorrelations Matrix:\n", correlations)

# ----------------------------------------------------------------------
# 2. Filter Methods
# ----------------------------------------------------------------------
section("2. Filter Methods")

# hypothetical data
data_2 = {
    'study hours': [10, 9, 8, 7, 10, 9, 8],
    'assignments completed': [10, 9, 8, 7, 10, 9, 8],
    'class participation': [8, 8, 7, 7, 8, 8, 7],
    'extracurricular activities': [2, 3, 2, 3, 2, 3, 2],
    'final grade': [90, 89, 78, 77, 90, 89, 78]
}
df_2 = pd.DataFrame(data_2)

# calculate correlations with 'final grade'
correlations_2 = df_2.corr()['final grade'].sort_values()
print("Correlations with Final Grade:\n", correlations_2)

# keep only features with correlation above 0.5
relevant_features = correlations_2[correlations_2 > 0.5]
print("\nRelevant Features (> 0.5):\n", relevant_features)

# ----------------------------------------------------------------------
# 3. Wrapper Methods
# ----------------------------------------------------------------------
section("3. Wrapper Methods (RFE)")

# create a model
estimator = SVR(kernel="linear")

# create the RFE object and compute a cross-validated score
selector = RFECV(estimator, step=1, cv=5)

# fit the data
selector = selector.fit(df_2.drop('final grade', axis=1), df_2['final grade'])

# print out the features selected
print("Selected Features (Wrapper):")
print(df_2.drop('final grade', axis=1).columns[selector.support_])

# ----------------------------------------------------------------------
# 4. Embedded Methods
# ----------------------------------------------------------------------
section("4. Embedded Methods (Lasso)")

X = df_2.drop('final grade', axis=1) # input features
y = df_2['final grade']              # target

# lasso acts as our "sculptor"
lasso = LassoCV(cv=5)
lasso.fit(X, y) # sculpting process

# importance of each feature
importance = np.abs(lasso.coef_)

# our final "statue"
important_features = X.columns[importance > 0]
print("Selected Features (Embedded):\n", important_features)