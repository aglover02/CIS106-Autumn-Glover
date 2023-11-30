names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]

def displaynames(names):
    l = len(names)
    for i in range(0, l, 1):
        print(names[i])


def displaynamesreverse(names):
    l = len(names)
    for i in range(l-1, 0, -1):
        print(names[i])


displaynames(names)
displaynamesreverse(names)