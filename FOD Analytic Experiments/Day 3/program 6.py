
DATE = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
WEATHER_CONDITION = ['Rainy', 'Cloudy', 'Rainy', 'Sunny', 'Sunny', 'Sunny', 'Rainy', 'Rainy', 'Rainy', 'Rainy', 'Smog', 'Smog']
COUNT_OF_TIMES = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

weather_frequency = {}

for condition, count in zip(WEATHER_CONDITION, COUNT_OF_TIMES):
    if condition in weather_frequency:
        weather_frequency[condition] += count
    else:
        weather_frequency[condition] = count

most_common_weather = max(weather_frequency, key=weather_frequency.get)

print("Frequency Distribution of Weather Conditions:")
for condition, count in weather_frequency.items():
    print(f"{condition}: {count}")

print("\nThe most common weather type is:", most_common_weather)
