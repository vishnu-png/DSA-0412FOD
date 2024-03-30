import pandas as pd

data = {
    'Property_ID': [123, 124, 125, 127],
    'Location': ['Chennai', 'Andhra', 'Kerala', 'Maharashtra'],
    'Number_of_Bedrooms': [1, 2, 3, 4],
    'Area_Square_Feet': [1101, 2323, 2342, 2342],
    'Listing_Price': [8236672, 87235, 23423, 23453]
}

df = pd.DataFrame(data)

avg_listing_price_per_location = df.groupby('Location')['Listing_Price'].mean().reset_index()

print("Average listing price of properties in each location:")
print(avg_listing_price_per_location)
print()

num_properties_more_than_four_bedrooms = df[df['Number_of_Bedrooms'] > 4].shape[0]

print(f"Number of properties with more than four bedrooms: {num_properties_more_than_four_bedrooms}")
print()

property_with_largest_area = df.loc[df['Area_Square_Feet'].idxmax()]

print("Property with the largest area:")
print(property_with_largest_area)
