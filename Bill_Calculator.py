product_name=input("Enter Product Name:")
product_price=int(input("Enter Product Price:"))
quantity=int(input("Enter Product Quantity:"))
total_price=product_price*quantity
print(f'Product Name: {product_name}')
print(f'Product Price: {product_price}')
print(f'Quantity: {quantity}')
print(f'total_price: {total_price}')
if total_price>=5000:
    discount=20
    disc_price=total_price*discount/100
    final_price=total_price-disc_price
    print(f'Discount:{discount}%')
    print(f'Final Price: {final_price}')
elif total_price>=3000:
    discount=10
    disc_price=total_price*discount/100
    final_price=total_price-disc_price
    print(f'Discount: {discount} %')
    print(f'Final Price: {final_price}')
elif total_price>=1500:
    discount=5
    disc_price=total_price*discount/100
    final_price=total_price-disc_price
    print(f'Discount: {discount} %')
    print(f'Final Price: {final_price}')
else:
    print("No Discount")

print("Thank You, visit again")


