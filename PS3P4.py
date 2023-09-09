make = input("Make:  ")
model = input("Model: ")
msrp = float(input("MSRP: $ "))
discount = float(input("Discount: $ "))
amount_off = msrp * discount
discounted_price = msrp - amount_off

print("Make:", make)
print("Model:", model)
print("Amount off:$", amount_off)
print("Discounted price:$", discounted_price)
