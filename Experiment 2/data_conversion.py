import pandas as pd

# Load the dataset again
data = pd.read_csv('superconduct_train new.csv')

# Convert all columns to numeric, coercing errors to handle non-numeric data
numeric_data = data.apply(pd.to_numeric, errors='coerce')

# Check for any remaining missing values after conversion
missing_after_conversion = numeric_data.isnull().sum()

# Fill missing values with the mean of each column
numeric_data_filled = numeric_data.fillna(numeric_data.mean())

# Verify that there are no missing values left
final_missing_check = numeric_data_filled.isnull().sum().sum()

# Output the results
missing_after_conversion, final_missing_check