#Property decorator

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    @property
    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print('deleting name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Doe')

emp_1.fullName = 'Jimmy anderson'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullName)

del emp_1.fullName