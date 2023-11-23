def computecom(sales, lname):
    if sales >= 100000:
        commission = sales * 0.10
    elif sales < 100000:
        commission = sales * 0.05
    target = sales * 0.05

    print("Last name: ", lname)
    print("Commission: $", commission)
    print("Next year's target: $", target)


f = open("PS10P3.txt", "r")

lname = f.readline()
sales = float(f.readline())
computecom(sales, lname)
while f:
    lname = f.readline()
    if lname == "":
        break
    sales = float(f.readline())
    computecom(sales, lname)
