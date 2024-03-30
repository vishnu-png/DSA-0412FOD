import numpy as np
import matplotlib.pyplot as plt

age = np.array([20, 25, 30, 35])
weight = np.array([40, 45, 50, 55])

mean_age = np.mean(age)
mean_weight = np.mean(weight)

variance_age = np.var(age)
variance_weight = np.var(weight)

covariance = np.cov(age, weight)[0, 1]

correlation_coefficient = np.corrcoef(age, weight)[0, 1]

print("Mean Age:", mean_age)
print("Mean Weight:", mean_weight)
print("Variance of Age:", variance_age)
print("Variance of Weight:", variance_weight)
print("Covariance:", covariance)
print("Correlation Coefficient:", correlation_coefficient)

plt.figure(figsize=(8, 6))
plt.scatter(age, weight, color='blue')
plt.title('Scatter Plot of Age vs Weight')
plt.xlabel('Age')
plt.ylabel('Weight')
plt.grid(False)
plt.show()
