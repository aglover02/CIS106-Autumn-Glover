names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
scores = [90, 75, 100, 60, 85, 95, 99, 78, 80, 88]


def displayscores(names, scores):
    minscore = min(scores)
    maxscore = max(scores)
    minscore_index = scores.index(minscore)
    maxscore_index = scores.index(maxscore)

    print(names[minscore_index], minscore)
    print(names[maxscore_index], maxscore)

displayscores(names, scores)