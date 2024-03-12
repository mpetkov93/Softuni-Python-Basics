square_meters = float(input())

square_meter_price = 7.61
discount_percentage = 0.18

price = square_meters * square_meter_price
discount = price * discount_percentage
total_price = price - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")