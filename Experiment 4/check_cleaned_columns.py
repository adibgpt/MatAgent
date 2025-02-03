import pandas as pd

# Load the dataset
data = pd.read_csv('Alloy_Yield_Strength.csv')

# Clean column names by stripping whitespace and converting to lowercase
cleaned_columns = data.columns.str.strip().str.lower()
data.columns = cleaned_columns

# Print cleaned column names
print(data.columns.tolist())