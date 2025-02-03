import pandas as pd

# Load the dataset
data = pd.read_csv('Alloy_Yield_Strength.csv')

# Display basic information about the dataset
data_info = data.info()

data_info