lastname = input("Last name: ")
salary = float(input("Salary: $"))
level = float(input("Job level: "))

if level >= 10:
    bonusrate = 0.25
if level >=5 and level <= 9:
    bonusrate = 0.2
else:
    bonusrate = 0.1

bonus = salary * bonusrate

print("Last name: ", lastname)
print("Bonus: $", bonus)