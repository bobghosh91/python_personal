# classes: user defined prototype
import datetime


class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


emp_1 = Employee('bob', 'ghosh', 50000)
emp_2 = Employee('test', 'user', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

##static methods
mDate = datetime.date(2022, 12, 23)
print(Employee.is_workday(mDate))
