user_interactions = ['anime', 'movies', 'heroines', 'facts', 'politics']
likes_per_post = [100, 100, 122, 3231, 23123]

frequency_distribution = {}

for category, likes in zip(user_interactions, likes_per_post):
    if category in frequency_distribution:
        frequency_distribution[category].append(likes)
    else:
        frequency_distribution[category] = [likes]

for category, likes_list in frequency_distribution.items():
    print("Category:", category)
    print("Frequency Distribution:", likes_list)
    print("Total Posts in Category:", len(likes_list))
    print("Total Likes in Category:", sum(likes_list))
    print()
  
