#Product Price Calculator
Original_price=float(input("Enter the Original Price:"))
Discout_percent=float(input("Enter the Discount %:"))
Discount_amount=Discout_percent/100*Original_price
Final_price=Original_price-Discount_amount
print(f"Final_price after{Discout_percent}%Discount:{Final_price}")
print(f"Original price:Rs.{Original_price}")
print(f"Discount:{Discout_percent}%")
print(f"Final price:Rs.{Final_price}")

