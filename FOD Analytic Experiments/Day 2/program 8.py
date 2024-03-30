import matplotlib.pyplot as plt
import numpy as np

# Monthly sales data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [12323, 2132, 3123, 2132, 23123, 23312, 23232, 2323, 4232, 2332, 3234, 2342]

# Create a figure and axis object
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Line plot
ax1.plot(months, sales, marker='o', color='b', linestyle='-')
ax1.set_title('Monthly Sales Data (Line Plot)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales')
ax1.grid(True)

# Bar plot
ax2.bar(months, sales, color='g')
ax2.set_title('Monthly Sales Data (Bar Plot)')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')
ax2.grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()
