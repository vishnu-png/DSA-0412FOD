import pandas as pd
import matplotlib.pyplot as plt

weather_data = pd.read_csv('weather_data.csv')  
weather_data['Date'] = pd.to_datetime(weather_data['Date'])
weather_data.set_index('Date', inplace=True)

seasonal_avg_temp = weather_data.resample('M').mean()  
seasonal_avg_temp['Temperature'].plot(figsize=(10, 6))
plt.title('Average Temperature Trends Over Seasons')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

weather_data['Precipitation'].plot(figsize=(10, 6))
plt.title('Precipitation Patterns Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
weather_data['Temperature'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)

extreme_temperatures = weather_data[(weather_data['Temperature'] < -10) | (weather_data['Temperature'] > 35)]
plt.scatter(extreme_temperatures.index, extreme_temperatures['Temperature'], color='red', label='Extreme Events')
plt.legend()
plt.show()
