f = open("PS8P5.txt", "r")

totaltuition = 0
count = 0

lastname = f.readline()

while lastname != "":
    dcode = f.readline()
    credit = float(f.readline())
    if dcode == "I":
        costpercredit = 250
    else:
        costpercredit = 500

    tuition = credit * costpercredit
    totaltuition = totaltuition + tuition
    count = count + 1
    
    print("Last name: ", lastname)
    print("Credits taken: ", credit)
    print("Tuition: ", tuition)

    lastname = f.readline()

print("Total tuition: ", totaltuition)
print("Number of students: ", count)