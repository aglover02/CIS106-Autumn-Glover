yesorno = input("Would you like to continue? ")
noofworkers = 0
sumgrosspay = 0
while yesorno == "yes":
    lastname = input("Last name: ")
    hours = float(input("Number of hours: "))
    rate = float(input("Pay rate: $"))

    if hours >= 40:
        grosspay = (rate * hours) + (hours - 40) * 1.5 * rate
    else:
        grosspay = rate * hours

    noofworkers = noofworkers + 1
    sumgrosspay = sumgrosspay + grosspay
    print("Gross pay: $", grosspay)
    print("Last name", lastname)
    yesorno = input("Would you like to continue? ")

average = sumgrosspay / noofworkers
print("Number of employees: ", noofworkers)
print("Sum of all the gross pays:", sumgrosspay)
print("Average pay $", average)
