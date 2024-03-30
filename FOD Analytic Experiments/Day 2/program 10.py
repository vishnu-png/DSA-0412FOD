import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [100, 120, 150, 130, 140, 160, 170, 180, 200, 210, 220, 230]

plt.figure(figsize=(10, 6))
plt.plot(months, sales, marker='o', color='b', linestyle='-')
plt.title('Sales of Product Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45) 

plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(months, sales, color='r', marker='o')
plt.title('Sales of Product Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.xticks(rotation=45)  

plt.show()
