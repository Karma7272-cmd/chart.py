import matplotlib.pyplot as plt
import numpy as np

# Data
sales_data = {'Sale': 2000000, 'Fund': 2000000 * 0.02, 'Loss': 20000, 'Sold': 3425}
labels = sales_data.keys()
sizes = sales_data.values()
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Explode the first slice (Sale)
explode = (0.1, 0, 0, 0)

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add title
plt.title('Sales Dashboard')

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Show the plot
plt.show()
