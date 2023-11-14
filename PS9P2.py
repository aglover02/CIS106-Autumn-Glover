lastname = input("Last name: ")
hits = float(input("Number of hits: "))
atbats = float(input("Number of at bats: "))

def compaverage(hits,atbats):
    average = float(hits)/float(atbats)
    return average

average = compaverage(hits,atbats)
print("Batting average: ", average)