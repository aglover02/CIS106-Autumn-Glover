yesorno = input("Would you like to continue? ")
noofstudents = 0
while yesorno == "yes":
    lastname = input("Last name: ")
    exam1 = float(input("Exam score 1: "))
    exam2 = float(input("Exam score 2: "))
    average = (exam1 + exam2) / 2
    noofstudents = noofstudents + 1
    print("Last name:", lastname)
    print("Average score:", average)
    yesorno = input("Would you like to continue? ")
else:
    print("Number of students who entered data: ", noofstudents)