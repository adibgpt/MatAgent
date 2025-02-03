import matplotlib.pyplot as plt
import numpy as np

# Sample data for current-voltage characteristics
voltage = np.linspace(0, 1, 100)  # Voltage from 0 to 1V
current = 1.5 * (1 - np.exp(-10 * (voltage - 0.5)))  # Simulated current values

# Create the I-V characteristic curve
plt.figure(figsize=(8, 5))
plt.plot(voltage, current, label='I-V Characteristic', color='blue')
plt.title('Current-Voltage Characteristics of Perovskite Solar Cells')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.grid(True)
plt.legend()
plt.savefig('iv_characteristics_perovskite_solar_cells.png')
plt.show()