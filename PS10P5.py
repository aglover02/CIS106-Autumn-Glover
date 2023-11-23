qty = float(input("Quantity: "))
unitprice = float(input("Price per unit: $"))

total = 0
tax = 0

def computetax(qty,unitprice):
    global total
    global tax

    total = qty * unitprice
    tax = total * 0.07


computetax(qty,unitprice)

print("Total: $", total)
print("Tax: $", tax)