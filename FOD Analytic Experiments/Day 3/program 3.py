import matplotlib.pyplot as plt
import numpy as np

exam_scores = np.random.randint(40, 101, size=50)  

plt.hist(exam_scores, bins=10, color='skyblue', edgecolor='black', alpha=0.7)

plt.xlabel('Exam Scores')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Scores')
mean_score = np.mean(exam_scores)
plt.axvline(mean_score, color='red', linestyle='dashed', linewidth=1, label='Mean Score: {:.2f}'.format(mean_score))
plt.legend()

plt.show()

