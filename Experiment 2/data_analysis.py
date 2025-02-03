import pandas as pd

# Load the dataset
data = pd.read_csv('superconduct_train new.csv')

# Display basic information about the dataset
data_info = data.info()

# Check for missing values
missing_values = data.isnull().sum()

# Display the first few rows of the dataset
head_data = data.head()

# Output the results
data_info, missing_values, head_data