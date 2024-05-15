# question 1
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discounted price
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Example usage:
original_price = 100
discount_percent = 25
final_price = calculate_discount(original_price, discount_percent)
print("Final price after discount:", final_price)

#question 2
# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying the discount, or the original price if no discount was applied
if final_price != original_price:
    print("Final price after discount:", final_price)
else:
    print("No discount applied, original price:", final_price)