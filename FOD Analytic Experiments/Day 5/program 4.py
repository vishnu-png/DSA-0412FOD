import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# Provided dataset
data = {
    'age': [12, 14],
    'mileage': [60, 50],
    'brand': ['swift', 'swift'],
    'engine_type': ['123efe', 'df1124'],
    'price': [15000, 16000]  # Assuming target variable 'price' is also provided
}

# Creating DataFrame
df = pd.DataFrame(data)

# Preprocessing
categorical_features = ['brand', 'engine_type']
numeric_features = ['mileage', 'age']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(), categorical_features)])

X = df[['mileage', 'age', 'brand', 'engine_type']]  # Features
y = df['price']  # Target variable

X = preprocessor.fit_transform(X)

# Splitting the dataset into training and testing sets (not necessary for this small dataset)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Building a regression model using the CART algorithm
model = DecisionTreeRegressor()

# Training the model
model.fit(X, y)

# Prompting the user to input features of the new car
print("Enter the following features for the new car:")
mileage = float(input("Mileage of the car: "))
age = int(input("Age of the car: "))
brand = input("Brand of the car: ")
engine_type = input("Engine type of the car: ")

# Using the trained model to predict the price of the new car
new_car_features = preprocessor.transform([[mileage, age, brand, engine_type]])
predicted_price = model.predict(new_car_features)

print("Predicted price of the new car: $", predicted_price[0])
