# classes: user defined prototype
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


print(Employee.num_of_emps) # 0
emp_1 = Employee('bob', 'ghosh', 50000)
emp_2 = Employee('test', 'user', 60000)
print(Employee.num_of_emps) # 2 -> because the class was instanced twice at emp_1 and 2

# print(emp_1)
# print(emp_2, end='\n')

# print(emp_1.email)
# print(emp_2.email)
print(emp_1.fullName())
print(emp_2.fullName())
