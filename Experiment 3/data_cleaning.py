import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'IZA_cp.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print('Missing values in each column:')
print(missing_values)

# Handle missing values by filling with the mean of the numeric columns
df.fillna(df.mean(numeric_only=True), inplace=True)

# Check for duplicates
duplicates = df.duplicated().sum()
print(f'Total duplicates: {duplicates}')

# Remove duplicates if any
if duplicates > 0:
    df.drop_duplicates(inplace=True)

# Check for inconsistent data types
print(df.dtypes)

# Convert data types if necessary (e.g., ensure numeric columns are floats)
for col in df.columns[1:]:  # Skip the first column which is 'name'
    try:
        df[col] = df[col].astype(float)
    except ValueError:
        print(f'Column {col} could not be converted to float.')  

# Display cleaned data
print('Cleaned Data:')
print(df.head())

# Save the cleaned data to a new CSV file
cleaned_file_path = 'cleaned_IZA_cp.csv'
df.to_csv(cleaned_file_path, index=False)
print(f'Cleaned data saved to {cleaned_file_path}')