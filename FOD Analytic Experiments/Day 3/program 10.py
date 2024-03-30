import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

data = {
    'Age': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110],
    'BodyFatPercentage': [12, 15, 18, 20, 22, 25, 28, 30, 32, 33, 35, 36, 38, 39, 40, 41, 42, 43]
}
df = pd.DataFrame(data)

age_mean = df['Age'].mean()
age_median = df['Age'].median()
age_std = df['Age'].std()

fat_mean = df['BodyFatPercentage'].mean()
fat_median = df['BodyFatPercentage'].median()
fat_std = df['BodyFatPercentage'].std()

print("Age Statistics:")
print("Mean:", age_mean)
print("Median:", age_median)
print("Standard Deviation:", age_std)
print("\nBody Fat Percentage Statistics:")
print("Mean:", fat_mean)
print("Median:", fat_median)
print("Standard Deviation:", fat_std)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df['Age'].plot(kind='box')
plt.title('Boxplot of Age')
plt.subplot(1, 2, 2)
df['BodyFatPercentage'].plot(kind='box')
plt.title('Boxplot of Body Fat Percentage')
plt.show()

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(df['Age'], df['BodyFatPercentage'])
plt.xlabel('Age')
plt.ylabel('Body Fat Percentage')
plt.title('Scatter Plot')

plt.subplot(1, 2, 2)
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Age')

plt.tight_layout()
plt.show()
