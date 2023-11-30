f = open("PS11P4.txt", "r")
names = []
averages = []

for line in f:
    line = line.strip()
    line = line.split(",")
    names.append(line[0])
    averages.append(line[1])

f.close()


def displayarrays(names, averages):
    l = len(names)
    for i in range(0, l, 1):
        print(names[i], averages[i])

displayarrays(names, averages)

def search(name, names, averages):
    name_index = names.index(name)
    print(name, averages[name_index])

while True:
    name = input("Player name: ")
    search(name, names, averages)