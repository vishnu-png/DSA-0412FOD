import numpy as np
import matplotlib.pyplot as plt

scores = np.array([85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72])

mean_score = np.mean(scores)
print("Mean Score:", mean_score)

median_score = np.median(scores)
print("Median Score:", median_score)

quartiles = np.percentile(scores, [25, 50, 75])
print("First Quartile (Q1):", quartiles[0])
print("Median (Q2):", quartiles[1])
print("Third Quartile (Q3):", quartiles[2])

iqr = quartiles[2] - quartiles[0]
print("Interquartile Range (IQR):", iqr)

lower_bound = quartiles[0] - 1.5 * iqr
upper_bound = quartiles[2] + 1.5 * iqr
potential_outliers = scores[(scores < lower_bound) | (scores > upper_bound)]
print("Potential Outliers:", potential_outliers)

plt.boxplot(scores)
plt.title('Box plot of Scores')
plt.ylabel('Score')
plt.show()
