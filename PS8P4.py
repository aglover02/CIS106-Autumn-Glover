f = open("PS8P4.txt", "r")

sumofprices = 0
count = 0
average = 0

item = f.readline()

while item != "":
    qty = float(f.readline())
    price = float(f.readline())

    extendedprice = qty * price
    sumofprices = sumofprices + extendedprice
    count = count + 1
    average = sumofprices / count
    print("Item: ", item)
    print("Quantity: ", qty)
    print("Price: ", price)
    print("Extended price: ", extendedprice)

    item = f.readline()

print("Sum of all extended prices: ", sumofprices)
print("Number of orders: ", count)
print("Average order price: ", average)
