import matplotlib.pyplot as plt
import numpy as np

# Sample data for RMSE and R-squared values
models = ['Linear Regression', 'Random Forest', 'Gradient Boosting']
rmse_values = [2.5, 1.8, 1.9]
r2_values = [0.85, 0.90, 0.88]

# Create a figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create bar chart for RMSE
color = 'tab:blue'
ax1.set_xlabel('Models')
ax1.set_ylabel('RMSE', color=color)
ax1.bar(models, rmse_values, color=color, alpha=0.6, label='RMSE')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for R-squared
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('R-squared', color=color)  
ax2.plot(models, r2_values, color=color, marker='o', label='R-squared')
ax2.tick_params(axis='y', labelcolor=color)

# Title and legends
plt.title('Model Performance Comparison')
fig.tight_layout()  # to ensure the right y-label is not slightly clipped

# Save the figure
plt.savefig('model_performance_comparison.png')
plt.show()