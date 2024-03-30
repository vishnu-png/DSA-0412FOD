def most_common_weather(conditions):
    
    frequency = {}
    
 
    for condition in conditions:
        if condition in frequency:
            frequency[condition] += 1
        else:
            frequency[condition] = 1
    
    most_common = max(frequency, key=frequency.get)
    
    return most_common

weather_conditions = [
    'Sunny', 'Sunny', 'Rainy', 'Cloudy', 'Rainy', 'Sunny', 'Cloudy', 'Cloudy', 'Rainy', 'Sunny'
]

most_common_weather_type = most_common_weather(weather_conditions)
print("The most common weather type is:", most_common_weather_type)
