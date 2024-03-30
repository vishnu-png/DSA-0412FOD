import numpy as np
from scipy import stats

group1_scores = np.array([85, 90, 88, 92, 89, 87, 84, 91, 86, 88])
group2_scores = np.array([78, 82, 80, 81, 79, 85, 83, 81, 84, 82])

mean_group1 = np.mean(group1_scores)
mean_group2 = np.mean(group2_scores)

sem_group1 = stats.sem(group1_scores)
sem_group2 = stats.sem(group2_scores)


ci_group1 = stats.norm.interval(0.95, loc=mean_group1, scale=sem_group1)
ci_group2 = stats.norm.interval(0.95, loc=mean_group2, scale=sem_group2)

print("Group 1 Mean Score:", mean_group1)
print("Group 1 95% Confidence Interval:", ci_group1)
print()
print("Group 2 Mean Score:", mean_group2)
print("Group 2 95% Confidence Interval:", ci_group2)

t_stat, p_value = stats.ttest_ind(group1_scores, group2_scores)
alpha = 0.05

print()
print("Hypothesis Test:")
print("Null Hypothesis: There is no significant difference between the two groups.")
print("Alternative Hypothesis: There is a significant difference between the two groups.")
print("Significance Level (alpha):", alpha)
print("p-value:", p_value)

if p_value < alpha:
    print("Result: Reject the null hypothesis. There is a significant difference between the two groups.")
else:
    print("Result: Fail to reject the null hypothesis. There is no significant difference between the two groups.")
