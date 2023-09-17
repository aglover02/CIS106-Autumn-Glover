pricepershare = float(input("Purchase price per share: $"))
currentstockprice = float(input("Current stock price: $"))
quantityofstock = float(input("Quantity of stock: "))
finalvalue = (currentstockprice - pricepershare) * quantityofstock

print("The final value is: $", finalvalue)