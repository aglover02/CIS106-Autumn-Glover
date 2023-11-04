f = open("PS8P3.txt", "r")

sumofbonuses = 0.0

lastname = f.readline()

while lastname != "":
    salary = float(f.readline())

    if salary >= 100000:
        bonusrate = 0.2
    elif 50000 <= salary <= 99999:
        bonusrate = 0.15
    else:
        bonusrate = 0.1

    bonus = salary * bonusrate
    sumofbonuses = sumofbonuses + bonus

    print("Last name: ", lastname)
    print("Salary: ", salary)
    print("Bonus: ", bonus)

    lastname = f.readline()

print("Sum of all the bonuses: ", sumofbonuses)
