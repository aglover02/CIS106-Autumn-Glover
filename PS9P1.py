def comptotal(qty, price):
    total = float(qty) * float(price)

    if total > 10000:
        discount = total * 0.1
        total = total - discount
    else:
        total = total
    return total

qty = float(input("Quantity: "))
price = float(input("Price: $"))

total = comptotal(qty,price)

print("Total is: $", total)