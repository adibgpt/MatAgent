import matplotlib.pyplot as plt
import pandas as pd

# Sample data for efficiency improvements
strategies = ['Strategy A', 'Strategy B', 'Strategy C']
efficiency = [18.5, 20.1, 22.3]

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(strategies, efficiency, color=['blue', 'orange', 'green'])
plt.title('Efficiency Improvements of Perovskite Solar Cells')
plt.xlabel('Optimization Strategies')
plt.ylabel('Efficiency (%)')
plt.ylim(0, 25)

# Save the figure
plt.savefig('efficiency_improvements_perovskite_solar_cells.png')
plt.show()