import numpy as np
from scipy import stats

product1_lifespans = np.array([120, 125, 118, 130, 122, 128, 115, 123, 127, 121])
product2_lifespans = np.array([110, 115, 108, 112, 120, 116, 118, 114, 113, 117])

mean_product1 = np.mean(product1_lifespans)
mean_product2 = np.mean(product2_lifespans)

sem_product1 = stats.sem(product1_lifespans)
sem_product2 = stats.sem(product2_lifespans)

ci_product1 = stats.norm.interval(0.90, loc=mean_product1, scale=sem_product1)
ci_product2 = stats.norm.interval(0.90, loc=mean_product2, scale=sem_product2)

print("Product 1 Mean Lifespan:", mean_product1)
print("Product 1 90% Confidence Interval:", ci_product1)
print()
print("Product 2 Mean Lifespan:", mean_product2)
print("Product 2 90% Confidence Interval:", ci_product2)

t_stat, p_value = stats.ttest_ind(product1_lifespans, product2_lifespans)
alpha = 0.05

print()
print("Hypothesis Test:")
print("Null Hypothesis: There is no statistically significant difference in lifespans between the two products.")
print("Alternative Hypothesis: There is a statistically significant difference in lifespans between the two products.")
print("Significance Level (alpha):", alpha)
print("p-value:", p_value)

if p_value < alpha:
    print("Result: Reject the null hypothesis. There is a statistically significant difference in lifespans between the two products.")
else:
    print("Result: Fail to reject the null hypothesis. There is no statistically significant difference in lifespans between the two products.")
