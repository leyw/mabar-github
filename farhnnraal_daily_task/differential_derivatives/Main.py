import numpy as np
import matplotlib.pyplot as plt

def population(time_interval):
    return 1000 * np.exp(0.05 * time_interval)

def derivatives(time_interval):
    return 50 * np.exp(0.05 * time_interval)

# Time Interval
time_interval = np.linspace(0, 100, 1000)

# Calculate population and its derivatives
population = population(time_interval)
growth_rate = derivatives(time_interval)

# Plotting
plt.plot(time_interval, population, label='Population')
plt.plot(time_interval, growth_rate, label='Growth Rate')
plt.xlabel('Time (hours)')
plt.ylabel('Population / Growth Rate')
plt.legend()
plt.show()


# Find maximum growth rate and time
max_growth_index = np.argmax(growth_rate)
max_growth_time = time_interval[max_growth_index]
max_growth_rate = growth_rate[max_growth_index]

print(f"Maximum growth rate: {max_growth_rate} bacteria/hour")
print(f"Time of maximum growth: {max_growth_time} hours")
