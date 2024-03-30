import pandas as pd
import numpy as np

np.random.seed(0)
num_products = 100 
products = [f'Product_{i}' for i in range(1, num_products+1)]
quantity_sold = np.random.randint(1, 100, num_products)

date_range = pd.date_range(end=pd.Timestamp.today(), periods=30, freq='D')

sales_dates = np.random.choice(date_range, size=num_products)

sales_data = pd.DataFrame({
    'Product': products,
    'Quantity_Sold': quantity_sold,
    'Sale_Date': sales_dates
})

past_month_start = pd.Timestamp.today() - pd.DateOffset(months=1)
past_month_data = sales_data[sales_data['Sale_Date'] >= past_month_start]

product_sales = past_month_data.groupby('Product')['Quantity_Sold'].sum().reset_index()

sorted_product_sales = product_sales.sort_values(by='Quantity_Sold', ascending=False)

top_5_products = sorted_product_sales.head(5)

print(top_5_products)
