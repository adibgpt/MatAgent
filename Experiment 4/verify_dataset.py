import pandas as pd

# Load the dataset
data = pd.read_csv('Alloy_Yield_Strength.csv')

# Clean column names by stripping whitespace and converting to lowercase
cleaned_columns = data.columns.str.strip().str.lower()
data.columns = cleaned_columns

# Verify the presence of the target column
if 'ys (mpa)' in data.columns:
    print("Target column 'ys (mpa)' is present.")
else:
    print("Target column 'ys (mpa)' is missing.")

# Check the first few rows of the dataset
data.head()