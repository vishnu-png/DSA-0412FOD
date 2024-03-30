import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('stopwords')
nltk.download('punkt')

df = pd.DataFrame({
    'Feedback': [
        "I love this product!", "Positive", "Twitter", "2023-06-15 09:23:14", "@user123", "New York", 0.85,
        "This movie is amazing!", "Positive", "IMDb", "2023-06-15 14:10:22", "moviefan789", "London", 0.92,
        "Just had the best meal of my life!", "Positive", "TripAdvisor", "2023-06-16 08:50:59", "foodie22", "Paris", 0.88,
        "The food at this restaurant was disappointing. Not worth the price.", "Negative", "Zomato", "2023-07-15 15:45:32", "foodcritic246", "Mumbai", 0.68,
        "This playlist is perfect for relaxation. Soothing and calming!", "Positive", "Spotify", "2023-07-15 18:20:17", "relaxmusiclover", "Berlin", 0.91,
        "I had an incredible experience at the theme park. So much fun!", "Positive", "Trip Report", "2023-07-03 14:40:05", "thrillseeker1", "Orlando", 0.89
    ]
})

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    tokens = word_tokenize(text)

    filtered_tokens = [word for word in tokens if word not in stop_words]
    return filtered_tokens

feedbacks = df[df.index % 7 == 0]['Feedback']

preprocessed_feedbacks = [preprocess_text(feedback) for feedback in feedbacks]

all_words = [word for sublist in preprocessed_feedbacks for word in sublist]


word_freq = Counter(all_words)

top_n = int(input("Enter the number of top words to display: "))

top_words = word_freq.most_common(top_n)
print("Top", top_n, "most frequent words:")
for word, freq in top_words:
    print(word, ":", freq)

words, frequencies = zip(*top_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top {} Most Frequent Words'.format(top_n))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
