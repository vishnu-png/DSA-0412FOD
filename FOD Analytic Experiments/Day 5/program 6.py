import pandas as pd
import numpy as np

# Generating example data
np.random.seed(0)  # for reproducibility
data = {
    'location': np.random.choice(['City A', 'City B', 'City C'], size=100),
    'listing_price': np.random.randint(100000, 500000, size=100),
    'number_of_bedrooms': np.random.randint(1, 6, size=100)  # assuming up to 5 bedrooms
}

# Creating DataFrame
property_data = pd.DataFrame(data)

# Display the first few rows of the DataFrame to understand its structure
print("First few rows of the property data:")
print(property_data.head())

# i. The average listing price of properties in each location
average_price_per_location = property_data.groupby('location')['listing_price'].mean()
print("\nAverage listing price of properties in each location:")
print(average_price_per_location)

# ii. The number of properties with more than four bedrooms
properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_more_than_four_bedrooms)
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)
