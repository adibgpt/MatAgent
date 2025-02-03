import pandas as pd

# Load the dataset with low_memory=False to avoid dtype warning
# and specifying on_bad_lines='skip' to skip problematic lines
data = pd.read_csv('superconduct_train new.csv', low_memory=False, on_bad_lines='skip')

# Identify columns with non-numeric values and attempt to convert them
for column in data.columns:
    # Attempt to convert to numeric, coercing errors to NaN
    data[column] = pd.to_numeric(data[column], errors='coerce')

# Drop rows with NaN values resulted from conversion errors
data_cleaned = data.dropna()

# Save the cleaned dataset for further processing
data_cleaned.to_csv('superconduct_train_cleaned.csv', index=False)

# Output the shape of the cleaned dataset
data_cleaned.shape