import pandas as pd

# Load datasets
customer_demographics = pd.read_csv('customer_demographics.csv')
user_activity_logs = pd.read_csv('user_activity_logs.csv')
customer_support = pd.read_csv('customer_support.csv')

# Inspect the data (optional but recommended)
print("Customer Demographics:")
print(customer_demographics.head())
print("\nUser Activity Logs:")
print(user_activity_logs.head())
print("\nCustomer Support Interactions:")
print(customer_support.head())

# Merge datasets on 'customer_id'
merged_data = pd.merge(customer_demographics, user_activity_logs, on='customer_id', how='outer')
merged_data = pd.merge(merged_data, customer_support, on='customer_id', how='outer')

# Display the unified dataset
print("\nUnified Dataset:")
print(merged_data)

