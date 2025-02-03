import pandas as pd

# Load the dataset with specified data types and handle potential formatting issues
df = pd.read_csv('superconduct_train new.csv', dtype=str)

# Clean the data by removing any non-numeric characters and converting to float
df = df.apply(lambda x: x.str.replace(',', '').str.replace('.', '').astype(float), axis=0)

# Display basic information about the dataset
df_info = df.info()

# Generate descriptive statistics
descriptive_stats = df.describe()

# Check for missing values
missing_values = df.isnull().sum()

# Calculate correlation matrix
correlation_matrix = df.corr()

# Output the results
(df_info, descriptive_stats, missing_values, correlation_matrix)