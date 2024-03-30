def calculate_total_cost(prices, quantities, discount_rate, tax_rate):
    # Calculate subtotal
    subtotal = sum(price * quantity for price, quantity in zip(prices, quantities))
    
    # Calculate discount amount
    discount_amount = subtotal * (discount_rate / 100)
    
    # Calculate subtotal after discount
    subtotal_after_discount = subtotal - discount_amount
    
    # Calculate tax amount
    tax_amount = subtotal_after_discount * (tax_rate / 100)
    
    # Calculate total cost
    total_cost = subtotal_after_discount + tax_amount
    
    return total_cost

# Example data
item_prices = [2.50, 3.00, 4.50, 2.00]
item_quantities = [3, 2, 1, 2]
discount_rate = 10  # 10%
tax_rate = 7  # 7%

# Calculate total cost
total_cost = calculate_total_cost(item_prices, item_quantities, discount_rate, tax_rate)
print("Total cost including discounts and taxes:", round(total_cost, 2))
