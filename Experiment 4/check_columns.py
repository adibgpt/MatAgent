import pandas as pd

# Load the dataset
data = pd.read_csv('Alloy_Yield_Strength.csv')

# Display the column names
print(data.columns.tolist())