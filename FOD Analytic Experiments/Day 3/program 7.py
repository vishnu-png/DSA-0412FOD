import numpy as np
import matplotlib.pyplot as plt

time_spent = [8, 12, 5, 15, 10, 20, 7, 18, 25, 8, 12, 22, 15, 10, 30, 7, 18, 15, 20, 12]

median_time_spent = np.median(time_spent)
print("Median time spent on the website:", median_time_spent)

quartiles = np.percentile(time_spent, [25, 75])
Q1 = quartiles[0]
Q3 = quartiles[1]
print("First Quartile (Q1):", Q1)
print("Third Quartile (Q3):", Q3)

IQR = Q3 - Q1
print("Interquartile Range (IQR):", IQR)

plt.boxplot(time_spent)
plt.title('Box plot of Time Spent on Website')
plt.ylabel('Time Spent (minutes)')
plt.show()
