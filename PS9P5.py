lastname = input("Last name: ")
hours = float(input("Amount of credit hours: "))
code = input("District code: ")

def comptuition(hours,code):
    if code == "I":
        tuition = hours*250
    elif code == "O":
        tuition = hours*550
    return tuition

tuition = comptuition(hours,code)

print("Last name: ", lastname)
print("Total tuition owed: $", tuition)