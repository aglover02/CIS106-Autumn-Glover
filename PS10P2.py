lname = input("Last name: ")
score1 = float(input("Exam score 1: "))
score2 = float(input("Exam score 2: "))
score3 = float(input("Exam score 3: "))

def computepoints(score1,score2,score3):
    total = score1 + score2 + score3
    avgscore = total / 3

    return total,avgscore

total,avgscore = computepoints(score1, score2, score3)

print("Last name: ", lname)
print("Total point: ", total)
print("Average exam score: ", avgscore)