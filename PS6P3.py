principle = float(input("Principle: $"))
years = float(input("Years to maturity: "))

if principle > 100000 and years == 5:
    interest = 0.06
elif principle >= 50000 and principle <= 100000 and years == 10:
    interest = 0.05
elif principle >= 50000 and principle <= 100000 and years == 5:
    interest = 0.04
else:
    interest = 0.02

firstinterest = principle * interest

print("Princple: $", principle)
print("Interest rate:", interest)
print("Interest amount for first year: $", firstinterest)