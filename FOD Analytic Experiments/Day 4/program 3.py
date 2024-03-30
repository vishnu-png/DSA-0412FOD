import numpy as np
from scipy import stats

# Sample data (replace with your actual data)
conversion_rate_design_A = np.array([0.12, 0.14, 0.11, 0.13, 0.15, 0.12, 0.13, 0.14, 0.13, 0.12])
conversion_rate_design_B = np.array([0.14, 0.16, 0.13, 0.15, 0.17, 0.14, 0.15, 0.16, 0.15, 0.14])

# Perform hypothesis test (two-sample t-test)
t_stat, p_value = stats.ttest_ind(conversion_rate_design_A, conversion_rate_design_B)
alpha = 0.05

print("Hypothesis Test:")
print("Null Hypothesis: There is no statistically significant difference in mean conversion rates between designs A and B.")
print("Alternative Hypothesis: There is a statistically significant difference in mean conversion rates between designs A and B.")
print("Significance Level (alpha):", alpha)
print("p-value:", p_value)

if p_value < alpha:
    print("Result: Reject the null hypothesis. There is a statistically significant difference in mean conversion rates between designs A and B.")
else:
    print("Result: Fail to reject the null hypothesis. There is no statistically significant difference in mean conversion rates between designs A and B.")
