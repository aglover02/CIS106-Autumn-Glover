city = input("Destination city: ")
miles = input("Miles traveled: ")
gallons = input("Number of gallons used: ")

def compmpg(miles,gallons):
    mpg = float(miles)/float(gallons)
    return mpg
mpg = compmpg(miles,gallons)

def compcost(gallons):
    cost = float(gallons)*2.50
    return cost
cost = compcost(gallons)

print("Destination city: ", city)
print("Miles per gallon: ", mpg)
print("Total cost of gas:", cost)