import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

gene_expression_data = np.random.normal(loc=0, scale=1, size=1000)

skewness = stats.skew(gene_expression_data)
kurtosis = stats.kurtosis(gene_expression_data)

asymmetry_index = skewness * kurtosis

log_transformed_data = np.log(gene_expression_data + 1)
sqrt_transformed_data = np.sqrt(gene_expression_data)

plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.hist(gene_expression_data, bins=30, color='skyblue', edgecolor='black')
plt.title('Original Data')

plt.subplot(1, 3, 2)
plt.hist(log_transformed_data, bins=30, color='skyblue', edgecolor='black')
plt.title('Log-transformed Data')

plt.subplot(1, 3, 3)
plt.hist(sqrt_transformed_data, bins=30, color='skyblue', edgecolor='black')
plt.title('Square Root-transformed Data')

plt.tight_layout()
plt.show()
