name = input("Name:")
cost = float(input("Cost: $"))
if cost>1000:
    warrantee = cost * 0.1
else:
    warrantee = cost * 0.05
total = cost + warrantee

print("Name:", name)
print("Cost of appliance: $", cost)
print("Warrantee: $", warrantee)
print("Total: $", total)
