def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        # Calculate the final price after discount
        final_price = price - discount_amount
    else:
        # If discount is less than 20%, return the original price
        final_price = price
    
    return final_price


