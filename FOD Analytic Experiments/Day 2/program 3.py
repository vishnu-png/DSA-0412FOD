import numpy as np

# Assuming fuel_efficiency is a NumPy array containing fuel efficiency values for different car models

# Step 1: Calculate the average fuel efficiency across all car models
average_fuel_efficiency = np.mean(fuel_efficiency)

# Step 2: Select fuel efficiency values for the two car models you want to compare
# Let's assume you have indices for the two car models you want to compare: model_1_index and model_2_index
model_1_index = 0
model_2_index = 1

fuel_efficiency_model_1 = fuel_efficiency[model_1_index]
fuel_efficiency_model_2 = fuel_efficiency[model_2_index]

# Step 3: Calculate the percentage improvement in fuel efficiency between the two car models
percentage_improvement = ((fuel_efficiency_model_2 - fuel_efficiency_model_1) / fuel_efficiency_model_1) * 100

# Print the results
print("Average fuel efficiency across all car models:", average_fuel_efficiency)
print("Fuel efficiency of Model 1:", fuel_efficiency_model_1)
print("Fuel efficiency of Model 2:", fuel_efficiency_model_2)
print("Percentage improvement in fuel efficiency between Model 1 and Model 2:", percentage_improvement)
