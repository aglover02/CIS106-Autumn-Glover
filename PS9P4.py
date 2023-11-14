lastname = input("Last name: ")
jobcode = input("Job code: ")
hours = float(input("Hours worked: "))

def comprate(jobcode):
    if jobcode == "L":
        rate = 25
    elif jobcode == "A":
        rate = 30
    elif jobcode == "J":
        rate = 50
    return rate
rate = comprate(jobcode)

if hours > 40:
    rate = rate*1.5

def compgross(hours, rate):
    grosspay = float(hours)*float(rate)
    return grosspay
grosspay = compgross(hours, rate)

print("Last name: ", lastname)
print("Gross pay: $", grosspay)