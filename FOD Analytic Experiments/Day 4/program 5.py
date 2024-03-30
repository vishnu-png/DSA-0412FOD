import pandas as pd
import numpy as np
from scipy import stats

data = {
    'id': [13423, 23234, 34234],
    'name': ['vishnu', 'varun', 'yash'],
    'brand_categories': ['pooma', 'adidas', 'titan'],
    'manufacturer': ['pooma', 'adidas', 'titan'],
    'manufacturer_number': [23213, '213123f2e', '312312v'],
    'review_date': ['01/12/2022', '02/02/2022', '03/02/2022'],
    'review_rating': [5, 2, 3],
    'review_text': ['good', 'better', 'good']
}

df = pd.DataFrame(data)


category = 'pooma'
category_data = df[df['brand_categories'] == category]

mean_rating = category_data['review_rating'].mean()
std_dev = category_data['review_rating'].std()
n = len(category_data)
sem = std_dev / np.sqrt(n)

confidence_level = 0.95
t_score = stats.t.ppf((1 + confidence_level) / 2, df=n - 1)
margin_of_error = t_score * sem
ci_lower = mean_rating - margin_of_error
ci_upper = mean_rating + margin_of_error

print(f"Product Category: {category}")
print(f"Mean Rating: {mean_rating:.2f}")
print(f"Confidence Interval ({confidence_level * 100}%): ({ci_lower:.2f}, {ci_upper:.2f})")
