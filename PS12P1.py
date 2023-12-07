class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def rate(self):
        bonus_rate = float(input('Bonus rate: '))
        bonus = bonus_rate * self.pay
        return bonus


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())

print(emp_1.rate())
print(emp_2.rate())