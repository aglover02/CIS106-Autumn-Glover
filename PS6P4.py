ticketno = float(input("Number of tickets:"))

if ticketno >= 25:
    ticketprice = 50
elif ticketno >= 10 and ticketno <= 24:
    ticketprice = 60
elif ticketno >= 5 and ticketno <= 9:
    ticketprice = 70
else:
    ticketprice = 75

total = ticketno * ticketprice

print("Number of tickets:", ticketno)
print("Price per ticket: $", ticketprice)
print("Total cost: $", total)