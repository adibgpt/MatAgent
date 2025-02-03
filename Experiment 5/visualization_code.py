import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data for optimization strategies and their efficiencies
strategies = ['Minimize Parasitic Resistance', 'Enhance Light Management', 'Optimize Device Geometry', 'Advanced Material Composition']
efficiencies = [18.5, 20.3, 20.45, 24.5]  # hypothetical efficiency percentages with a filled value

# Create a DataFrame
df = pd.DataFrame({'Strategy': strategies, 'Efficiency': efficiencies})

# Set the style of seaborn
sns.set(style='whitegrid')

# Create a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Strategy', y='Efficiency', data=df, palette='viridis')

# Add titles and labels
plt.title('Efficiency of Optimization Strategies for Perovskite Solar Cells', fontsize=16)
plt.xlabel('Optimization Strategy', fontsize=14)
plt.ylabel('Efficiency (%)', fontsize=14)
plt.xticks(rotation=15)

# Save the figure
plt.tight_layout()
plt.savefig('optimization_strategy_efficiencies.png')
plt.show()