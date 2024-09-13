def calculate_discount(price, discount_percent):
    discount_percentage = discount_percent / 100
    if discount_percentage > 20 / 100:
        discount_amount = price * discount_percentage
        final_price = price - discount_amount
        return final_price
    else:
        return price
price = int(input("Enter Original price "))
discount_percent = int(input("Enter discount in percentage "))
final_price = calculate_discount(price, discount_percent)
print("Your final price is:", final_price)
