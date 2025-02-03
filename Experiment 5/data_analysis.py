import numpy as np
import pandas as pd

# Sample data for optimization strategies and their efficiencies
strategies = ['Minimize Parasitic Resistance', 'Enhance Light Management', 'Optimize Device Geometry', 'Advanced Material Composition']
efficiencies = [18.5, 20.3, np.nan, 24.5]  # hypothetical efficiency percentages with a missing value

# Create a DataFrame
df = pd.DataFrame({'Strategy': strategies, 'Efficiency': efficiencies})

# Function to handle missing data by filling with the mean of the column
def handle_missing_data(df):
    df['Efficiency'].fillna(df['Efficiency'].mean(), inplace=True)
    return df

# Function to perform basic statistical analysis
def statistical_analysis(df):
    description = df['Efficiency'].describe()
    return description

# Handle missing data
df_clean = handle_missing_data(df)

# Perform statistical analysis
analysis_results = statistical_analysis(df_clean)

analysis_results.to_dict()