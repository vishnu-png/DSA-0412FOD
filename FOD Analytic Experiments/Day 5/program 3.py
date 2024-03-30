import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {
    'square_footage': [2981, 2431,2561],
    'number_of_bedrooms': [4,2,4],
    'number_of_bathrooms':[4,2,4],
    'location':['andhra','tamilnadu','kerala']
}

df = pd.DataFrame(data)

selected_feature = 'number_of_bedrooms'
target_variable = 'number_of_bathrooms'  

plt.scatter(df[selected_feature], df[target_variable])
plt.title("Bivariate Analysis: selling house price")
plt.xlabel(selected_feature)
plt.ylabel(target_variable)
plt.show()

X = df[[selected_feature]]  
y = df[target_variable]     

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.title("Linear Regression: selling price of the house")
plt.xlabel(selected_feature)
plt.ylabel(target_variable)
plt.show()
