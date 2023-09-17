fixedcosts = float(input("Fixed costs: $"))
priceperunit = float(input("Price per unit: $"))
costperunit = float(input("Cost per unit: $"))
breakevenpoint = fixedcosts/(priceperunit-costperunit)

print("Break even point: ", breakevenpoint)
