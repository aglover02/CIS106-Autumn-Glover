qty = float(input("Quantity:"))

if qty > 10000:
    price = 10.00
elif 5000 <= qty <= 10000:
    price = 20.00
else:
    price = 30.00

extendedprice = qty * price
tax = extendedprice * 0.07
total = extendedprice + tax

print("Extended price: $", extendedprice)
print("Tax: $", tax)
print("Total: $", total)