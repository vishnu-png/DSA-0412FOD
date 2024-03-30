import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

placebo_group = np.array([82, 78, 85, 79, 81, 77, 80, 79, 83, 81])
treatment_group = np.array([75, 72, 78, 73, 76, 74, 77, 75, 79, 76])

# Perform hypothesis test (two-sample t-test)
t_stat, p_value = stats.ttest_ind(placebo_group, treatment_group)
alpha = 0.05

# Visualization
plt.figure(figsize=(8, 6))

# Boxplot
plt.boxplot([placebo_group, treatment_group], labels=['Placebo', 'Treatment'])

# Add p-value to the plot
plt.text(1.1, np.max([np.max(placebo_group), np.max(treatment_group)]) - 1, f'p-value: {p_value:.4f}', fontsize=12)

# Add title and labels
plt.title('Boxplot of Placebo and Treatment Groups')
plt.xlabel('Group')
plt.ylabel('Scores')

plt.grid(False)
plt.show()

print("Hypothesis Test:")
print("Null Hypothesis: There is no statistically significant difference in the effectiveness of the treatment compared to the placebo.")
print("Alternative Hypothesis: There is a statistically significant difference in the effectiveness of the treatment compared to the placebo.")
print("Significance Level (alpha):", alpha)
print("p-value:", p_value)

if p_value < alpha:
    print("Result: Reject the null hypothesis. The treatment has a statistically significant effect compared to the placebo.")
else:
    print("Result: Fail to reject the null hypothesis. There is no statistically significant difference in the effectiveness of the treatment compared to the placebo.")
