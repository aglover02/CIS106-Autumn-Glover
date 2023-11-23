lname = input("Last name: ")
score1 = float(input("Game score 1: "))
score2 = float(input("Game score 2: "))
score3 = float(input("Game score 3: "))
handicap = float(input("Handicap: "))

def computescore(score1,score2,score3):
    avgscore = (score1 + score2 + score3)/3
    avgscorewhandicap = avgscore + handicap

    return avgscore, avgscorewhandicap
avgscore,avgscorewhandicap = computescore(score1, score2, score3)

print("Last name: ", lname)
print("Average score: ", avgscore)
print("Average score with handicap: ", avgscorewhandicap)