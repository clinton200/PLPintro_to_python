# Creating a function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price*(discount_percent/100)
        final_price = price - discount_amount
        return final_price
    else:  
        return price
    
price = int(input("Enter the buying price: "))

discount_percent = int(input("Enter the discount percentage: "))

print(f'The final price after discount allowed is: {calculate_discount(price, discount_percent)}')
