yesorno = input("Would you like to continue? ")
discountsum = 0

while yesorno == "yes":
    qty = float(input("Quantity: "))
    price = float(input("Price: $ "))
    extendedprice = qty * price
    if extendedprice > 10000:
        discount = 0.25
    else:
        discount = 0.1
    discountamount = extendedprice * discount
    discountsum = discountsum + discountamount
    total = extendedprice - discountamount
    print("Extended price: $", extendedprice)
    print("Discount amount: $", discountamount)
    print("Total: $", total)
    yesorno = input("Would you like to continue? ")

print("Sum of discounts: $", discountsum)
