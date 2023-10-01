item = input("Item: ")
quantity = float(input("Quantity: "))

if item=="a":
    unitprice = 10.00
else:
    unitprice = 20.00

extendedprice = quantity * unitprice
print("Item",item)
print("Unit price: $", unitprice)
print("Extended price: $", extendedprice)