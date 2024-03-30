# Define the dataset
dataset = {
    "Common Cold": 320,
    "Diabetes": 120,
    "Bronchitis": 100,
    "Influenza": 150,
    "Kidney Stones": 60
}

# Calculate the total number of diagnosed patients
total_patients = sum(dataset.values())

# Calculate the frequency distribution of diseases
frequency_distribution = {disease: count / total_patients for disease, count in dataset.items()}

# Find the most common disease
most_common_disease = max(frequency_distribution, key=frequency_distribution.get)

# Print the frequency distribution of diseases
print("Frequency distribution of diseases:")
for disease, frequency in frequency_distribution.items():
    print(f"{disease}: {frequency:.2%}")

# Print the most common disease
print("\nThe most common disease is:", most_common_disease)
