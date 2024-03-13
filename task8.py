# Date: 18 Feb 2024
# Title: Day 26 Python Assignment Task 8
# done by Sora
# Using the matplotlib library, create a line plot that shows the trend of temperature over a period of 7 days. Assume the temperature data is stored in a list.

import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np

# sample data for date and temperature
date = np.array([11, 12, 13, 14, 15, 16, 17])
temperature = np.array([25, 28, 22, 30, 26, 29, 27])

# plotting the temperature trend over the specified dates
plt.plot(date, temperature)

# display the plot
plt.show()