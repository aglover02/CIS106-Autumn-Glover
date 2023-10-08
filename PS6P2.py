partno = float(input("Part number:"))
qty = float(input("Quantity:"))

if partno == 10 or partno == 55:
    unitcost = 1.00
elif partno == 99:
    unitcost = 2.00
elif partno == 80 or partno == 70:
    unitcost = 3.00
else:
    unitcost = 5.00

total = qty * unitcost
print("Part number:", partno)
print("Cost per unit: $", unitcost)
print("Total Cost: $", total)