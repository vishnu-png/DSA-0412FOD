import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [30, 35, 36, 36, 40, 36, 35, 34, 30, 30, 30, 30]  
rainfall = [70, 20, 0, 0, 29, 50, 67, 77, 88, 70, 77, 88]  

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

ax1.plot(months, temperature, marker='o', color='b', linestyle='-')
ax1.set_title('Monthly Temperature Data')
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (°C)')
ax1.grid(True)

ax2.scatter(months, rainfall, color='g')
ax2.set_title('Monthly Rainfall Data')
ax2.set_xlabel('Month')
ax2.set_ylabel('Rainfall (%)')
ax2.grid(True)


plt.tight_layout()

plt.show()
