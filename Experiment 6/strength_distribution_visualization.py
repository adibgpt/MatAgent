import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
concrete_data = pd.read_csv('concrete.csv')

# Strength Distribution Plot
plt.figure(figsize=(10, 6))
sns.histplot(concrete_data['strength'], bins=30, kde=True)
plt.title('Distribution of Concrete Strength')
plt.xlabel('Concrete Strength')
plt.ylabel('Frequency')
plt.savefig('strength_distribution_plot.png')
plt.show()