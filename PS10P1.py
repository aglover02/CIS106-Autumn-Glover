qty = float(input("Quantity: "))
price = float(input("Price: $"))
discrate = float(input("Discount rate: "))

def computedisc(qty,price,discrate):
    extprice = qty * price
    discamt = extprice * discrate
    discprice = extprice - discamt

    return discamt,discprice

discamt,discprice = computedisc(qty, price, discrate)

print("Quantity: ", qty)
print("Price: $", price)
print("Discount amount: $", discamt)
print("Discounted price: $", discprice)