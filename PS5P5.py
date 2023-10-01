lastname = input("Last name:")
dependents = float(input("Number of dependents: "))
grossincome = float(input("Gross Income: $"))
adjustedgrossincome = grossincome - dependents * 12000

if adjustedgrossincome>50000:
    taxrate = 0.2
else:
    taxrate = 0.1

incometax = adjustedgrossincome * taxrate
print("Last Name: ", lastname)
print("Gross income: $", grossincome)
print("Number of dependents: ", dependents)
print("Adjusted gross income: $", adjustedgrossincome)
print("Income tax: $", incometax)