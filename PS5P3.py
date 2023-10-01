books = float(input("Amount of books: "))
costperbook = float(input("Cost per book: $"))
total = books * costperbook

if total>50:
    shipping = 0
else:
    shipping = 25

print("Total: $",total)
print("Shipping: $",shipping)