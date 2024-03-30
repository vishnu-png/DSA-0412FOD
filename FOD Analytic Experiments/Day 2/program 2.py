import numpy as np

# Assuming house_data is a NumPy array containing the dataset
# Let's assume the structure of the house_data array:
# house_data[:, 0] represents the number of bedrooms
# house_data[:, 1] represents the square footage
# house_data[:, 2] represents the sale price

# Step 1: Identify the column representing the number of bedrooms
bedrooms_column = 0  # Assuming the number of bedrooms is in the first column

# Step 2: Filter the dataset to select houses with more than four bedrooms
houses_more_than_four_bedrooms = house_data[house_data[:, bedrooms_column] > 4]

# Step 3: Extract the sale prices for these houses
sale_prices = houses_more_than_four_bedrooms[:, 2]  # Assuming sale price is in the third column

# Step 4: Calculate the average sale price
average_sale_price = np.mean(sale_prices)

print("Average sale price of houses with more than four bedrooms:", average_sale_price)
