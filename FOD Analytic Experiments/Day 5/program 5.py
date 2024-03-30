import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

# Step 1: Load the dataset
# Assuming 'data' is a pandas DataFrame containing the dataset
# data = pd.read_csv('telecom_dataset.csv')  # Replace 'telecom_dataset.csv' with the actual file path

# Generating example data for demonstration
np.random.seed(0)  # for reproducibility
usage_minutes = np.random.randint(50, 1000, size=1)[0]  # Random usage minutes
contract_duration = np.random.randint(1, 36, size=1)[0]  # Random contract duration in months

# Step 2: Preprocess the data (if necessary)
# If needed, handle missing values, encode categorical variables, etc.

# Step 3: Split the dataset into features (X) and the target variable (y)
# X = data.drop('churn', axis=1)  # Features
# y = data['churn']  # Target variable

# Assuming the model is already trained and loaded

# Step 4: Scale the features
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# Step 5: Build a logistic regression model
# model = LogisticRegression()

# Step 6: Split the data into training and testing sets (commented out for demonstration)
# X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 7: Train the model (commented out for demonstration)
# model.fit(X_train, y_train)

# Step 8: Prompt the user to input features of the new customer
print("Enter the following features for the new customer:")

# Uncomment these lines if you want to take user input for the features
# usage_minutes = float(input("Usage minutes: "))
# contract_duration = int(input("Contract duration (in months): "))

# Step 9: Use the trained model to predict whether the new customer will churn
new_customer_features = [[usage_minutes, contract_duration]]  # Features for the new customer
# new_customer_features_scaled = scaler.transform(new_customer_features)  # Scaling features (commented out for demonstration)

# Assuming the model is already trained and loaded
# prediction = model.predict(new_customer_features_scaled)

# Generating a random prediction (commented out for demonstration)
prediction = np.random.choice([0, 1])  # Randomly predict churn or not churn

if prediction == 0:
    print("The new customer is predicted to not churn.")
else:
    print("The new customer is predicted to churn.")
