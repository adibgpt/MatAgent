import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
cleaned_file_path = 'cleaned_IZA_cp.csv'
df = pd.read_csv(cleaned_file_path)

# Set the style of seaborn
sns.set(style='whitegrid')

# Create histograms for gravimetric heat capacities at different temperatures
plt.figure(figsize=(15, 10))
for i, temp in enumerate([250, 275, 300, 325, 350, 375, 400]):
    plt.subplot(3, 3, i + 1)
    sns.histplot(df[f'Cv_gravimetric_{temp}.00_mean'], bins=20, kde=True)
    plt.title(f'Histogram of Cv_gravimetric at {temp}°C')
    plt.xlabel('Cv_gravimetric_mean')
    plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histograms_gravimetric_heat_capacity.png')
plt.show()

# Create scatter plots for molar vs gravimetric heat capacities
plt.figure(figsize=(15, 10))
for i, temp in enumerate([250, 275, 300, 325, 350, 375, 400]):
    plt.subplot(3, 3, i + 1)
    sns.scatterplot(x=df[f'Cv_gravimetric_{temp}.00_mean'], y=df[f'Cv_molar_{temp}.00_mean'])
    plt.title(f'Scatter plot of Cv_gravimetric vs Cv_molar at {temp}°C')
    plt.xlabel('Cv_gravimetric_mean')
    plt.ylabel('Cv_molar_mean')
plt.tight_layout()
plt.savefig('scatter_plots_heat_capacity.png')
plt.show()

# Create a correlation heatmap
plt.figure(figsize=(12, 10))
correlation = df.select_dtypes(include=['float64', 'int64']).corr()
sns.heatmap(correlation, annot=True, fmt='.2f', cmap='coolwarm', square=True)
plt.title('Correlation Heatmap of Heat Capacities')
plt.savefig('correlation_heatmap.png')
plt.show()