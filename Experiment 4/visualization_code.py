import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Alloy_Yield_Strength.csv'
df = pd.read_csv(file_path)

# Scatter plot for Yield Strength vs. Diff. Lattice Constants
plt.figure(figsize=(10, 6))
plt.scatter(df['Diff. Lattice Constants'], df['YS (MPa)'], color='blue', alpha=0.5)
plt.title('Yield Strength vs. Difference in Lattice Constants')
plt.xlabel('Difference in Lattice Constants')
plt.ylabel('Yield Strength (MPa)')
plt.grid(True)
plt.savefig('yield_strength_vs_diff_lattice_constants.png')
plt.close()

# Histogram for Yield Strength Distribution
plt.figure(figsize=(10, 6))
plt.hist(df['YS (MPa)'], bins=20, color='green', alpha=0.7)
plt.title('Distribution of Yield Strength')
plt.xlabel('Yield Strength (MPa)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig('yield_strength_distribution.png')
plt.close()