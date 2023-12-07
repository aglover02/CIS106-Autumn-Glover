class student:
    def __init__(self, first, last, district_code, credits):
        self.first = first
        self.last = last
        self.district_code = district_code
        self.credits = credits
    def tuition(self):
        if self.district_code == 'I':
            tuition = 250 * self.credits
        else:
            tuition = 500 * self.credits
        return tuition

stu_1 = student('James', 'Smith', 'I', 8)
stu_2 = student('Emma', 'Johnson', 'O', 5)
stu_3 = student('Micheal', 'Brown', 'I', 10)

print(stu_1.first)
print(stu_1.last)
print(stu_1.district_code)
print(stu_1.credits)
print(stu_1.tuition())

print(stu_2.first)
print(stu_2.last)
print(stu_2.district_code)
print(stu_2.credits)
print(stu_2.tuition())

print(stu_3.first)
print(stu_3.last)
print(stu_3.district_code)
print(stu_3.credits)
print(stu_3.tuition())