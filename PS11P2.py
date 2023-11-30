names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
scores = [90, 75, 100, 60, 85, 95, 99, 78, 80, 88]


def displaynames(names, scores):
    l = len(names)
    for i in range(0, l, 1):
        print(names[i], scores[i])

def displaynamesreverse(names, scores):
    l = len(names)
    for i in range(l-1, 0, -1):
        print(names[i], scores[i])

displaynames(names, scores)
displaynamesreverse(names, scores)