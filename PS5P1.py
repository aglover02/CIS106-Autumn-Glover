quantity = float(input("Quantity: "))
a = quantity
b = 1000
if a>=b:
    unitprice = 3.00
else:
    unitprice = 5.00

extendedprice = quantity * unitprice
tax = extendedprice * 0.07
total = extendedprice + tax

print("Quantity: ",quantity)
print("Unit price: $",unitprice)
print("Extended price: $",extendedprice)
print("Tax: $",tax)
print("Total: $",total)